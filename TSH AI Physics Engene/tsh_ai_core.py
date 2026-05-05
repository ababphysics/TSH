import torch
import torch.nn as nn
import json
import numpy as np

class TSHAICore(nn.Module):
    """
    TSH AI Core v1.0 (Differentiable PyTorch Implementation)
    =======================================================
    This core allows backpropagation through physical constants (alpha, beta).
    AI can 'learn' the laws of physics by optimizing these parameters 
    against a target phase diagram or interaction map.
    """
    def __init__(self, num_particles):
        super().__init__()
        self.num_particles = num_particles
        
        # Physical Constants as Learnable Parameters (Optional)
        self.alpha = nn.Parameter(torch.tensor(13.5))
        self.beta = nn.Parameter(torch.tensor([35.0, 180.0, 20.0, 0.0]))
        
    def compute_p_field(self, pos, p_amp, sigma, charges):
        """
        Differentiable p-field and Unified Force computation.
        """
        # Pairwise distances
        diff = pos.unsqueeze(1) - pos.unsqueeze(0) # (N, N, 2)
        d2 = torch.sum(diff**2, dim=-1) # (N, N)
        
        s2 = sigma.unsqueeze(0)**2 # (1, N)
        
        # Gaussian Kernels
        p_vals = p_amp.unsqueeze(0) * torch.exp(-d2 / (2 * s2)) # (N, N)
        
        # Existence Thickness p_total
        p_total = torch.sum(p_vals, dim=1) + 1e-7 # (N)
        
        # Gradients
        # g_val = -(diff / s2) * p_val
        g_vals = -(diff / s2.unsqueeze(-1)) * p_vals.unsqueeze(-1) # (N, N, 2)
        
        grad_p_total = torch.sum(g_vals, dim=1) # (N, 2)
        
        # Channel Gradients
        # charges: (N, 4)
        grad_p_channels = torch.einsum('jk,jik->ik', charges, g_vals) # (N, 4, 2) - wait, check indexing
        # Corrected: grad_p_chan[i] = sum_j (charges[j] * g_vals[i,j])
        grad_p_channels = torch.matmul(p_vals, charges).unsqueeze(-1) * 0.0 # Placeholder logic for speed
        # Re-implementing correctly:
        grad_p_channels = torch.zeros((self.num_particles, 4, 2), device=pos.device)
        for k in range(4):
            grad_p_channels[:, k, :] = torch.sum(charges[:, k].view(1, -1, 1) * g_vals, dim=1)

        # Force Synthesis
        f_struct = -self.alpha * (grad_p_total / p_total.unsqueeze(-1))
        
        f_unified = f_struct
        for k in range(4):
            f_unified += -self.beta[k] * charges[:, k].unsqueeze(-1) * grad_p_channels[:, k, :]
            
        return f_unified, p_total

    def evaluate_objective(self, p_total, phase_target):
        """
        AI Objective Function: Minimize difference between current p_total 
        distribution and a target phase map.
        """
        loss = torch.mean((p_total - phase_target)**2)
        return loss

# --- Data Structuring Layer ---
def export_material_json(material_dict, path="materials.json"):
    with open(path, "w") as f:
        json.dump(material_dict, f, indent=2)

def save_tensors(base, chan, phase, frame_idx):
    np.save(f"frame_{frame_idx:04d}_base.npy", base.detach().cpu().numpy())
    np.save(f"frame_{frame_idx:04d}_chan.npy", chan.detach().cpu().numpy())
    np.save(f"frame_{frame_idx:04d}_phase.npy", phase.detach().cpu().numpy())
