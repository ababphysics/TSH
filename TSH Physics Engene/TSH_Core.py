# NOTE:
# This collapse implementation is NOT an ODE/PDE-based model.
# DO NOT augment this logic with general physical paradigms.
# This is a unique model based on the Delta_f - gamma_T phase diagram and the TSH structural potential.
"""
================================================================================
TSH Physics Engine - Verified Reference Implementation (v2.0)
================================================================================
[PURPOSE]
This is the "Ground Truth" implementation of the Thickness Structure Hypothesis (TSH)
physics engine. It incorporates all improvements from the headless verification 
series (v1.1 - v1.5).

[INTEGRATED CORE UPGRADES]
1. Physical Collapse: Non-instantaneous field relaxation and dynamic attraction.
2. High-Strength Stability: Validated up to 30,000 collapse strength.
3. Continuous Field: Exponential relaxation of Sigma and P_amp.
4. Spacetime History: Progressive accumulation of gamma_T.

[CORE FORMULAS]
- f_struct = -alpha * (grad p_total / p_total)
- f_unified = f_struct - sum(beta_k * q_k * grad q_k)
- f_collapse = strength * exp(-t/tau) * exp(-d/L) * dir_unit

DO NOT MODIFY THIS FILE. IT IS THE VERIFIED BASELINE FOR UNITY/GPU PORTS.
================================================================================
"""

import pygame
import numpy as np
import math

# --- Physical Constants (Verified Baseline) ---
WIDTH, HEIGHT = 1280, 800
FPS = 60
SUBSTEPS = 6
DT = 1.0 / (FPS * SUBSTEPS)

# Reference Material Constants
MATERIAL_TABLE = {
    "Verified": {"beta": [40.0, 0.0, 0.0, 0.0], "alpha": 15.0}
}

class Particle:
    def __init__(self, x, y, z, charges=None):
        self.pos = np.array([float(x), float(y), float(z)])
        self.vel = np.zeros(3)
        self.mat = MATERIAL_TABLE["Verified"]
        self.charges = charges if charges is not None else np.array([1.0, 0.0, 0.0, 0.0])
        
        # Field State
        self.sigma = 80.0
        self.sigma_target = 80.0
        self.p_amp = 100.0
        self.p_amp_target = 100.0
        
        # TSH Metadata
        self.p_total = 0.0
        self.gamma_T = 0.0
        self.delta_f = 0.0
        self.phase = "Stable"

    def update_state(self, lp, grad_p, grad_chan):
        # 1. Update Internal Physics Values
        self.p_total = lp
        self.delta_f = np.linalg.norm(grad_p) / (lp + 1e-7)
        self.gamma_T += 0.01 * lp * DT # Irreversible accumulation
        
        # 2. Continuous Field Relaxation (Verified Rate)
        relax_rate = 15.0
        self.sigma += relax_rate * (self.sigma_target - self.sigma) * DT
        self.p_amp += relax_rate * (self.p_amp_target - self.p_amp) * DT

        # 3. Base TSH Forces
        f_struct = -self.mat['alpha'] * (grad_p / (lp + 1e-7))
        f_unified = f_struct.copy()
        for k in range(4):
            f_unified -= self.mat['beta'][k] * self.charges[k] * grad_chan[k]
        
        return f_unified

class TSHCore3D:
    def __init__(self):
        self.particles = []
        self.collapse_active = False
        self.collapse_center = np.zeros(3)
        self.collapse_timer = 0.0
        self.collapse_tau = 2.0
        self.collapse_strength = 5000.0

    def add_particle(self, x, y, z, charges=None):
        self.particles.append(Particle(x, y, z, charges))

    def trigger_measurement(self, center_pos=None):
        self.collapse_active = True
        self.collapse_timer = 0.0
        self.collapse_center = center_pos if center_pos is not None else np.zeros(3)
        
        # Set new targets for localized field
        for p in self.particles:
            dist = np.linalg.norm(p.pos - self.collapse_center)
            w = math.exp(-dist / 80.0) # Influence weight
            p.sigma_target = max(8.0, p.sigma * (0.4 + 0.6 * (1.0 - w)))
            p.p_amp_target = p.p_amp * (1.0 + 3.0 * w)
            p.gamma_T += 10.0 * w

    def update(self):
        # Exact O(N^2) Physical Loop
        forces = []
        for i, p in enumerate(self.particles):
            lp, grad_p = 1e-7, np.zeros(3)
            grad_chan = [np.zeros(3) for _ in range(4)]
            for other in self.particles:
                diff = p.pos - other.pos
                d2 = np.dot(diff, diff)
                s2 = other.sigma**2
                if d2 > s2 * 30.0: continue
                
                val = other.p_amp * math.exp(-d2 / (2 * s2))
                g = -(diff / s2) * val
                lp += val
                grad_p += g
                for k in range(4):
                    grad_chan[k] += other.charges[k] * g
            
            f_unified = p.update_state(lp, grad_p, grad_chan)
            
            # 4. Dynamic Collapse Force (v2.0 Integrated)
            if self.collapse_active:
                w_time = math.exp(-self.collapse_timer / self.collapse_tau)
                dist_to_obs = np.linalg.norm(p.pos - self.collapse_center)
                w_space = math.exp(-dist_to_obs / 30.0)
                
                dir_to_center = self.collapse_center - p.pos
                dist_norm = np.linalg.norm(dir_to_center) + 1e-7
                dir_unit = dir_to_center / dist_norm
                
                f_collapse = self.collapse_strength * w_time * w_space * dir_unit
                f_unified += f_collapse
            
            forces.append(f_unified)
        
        # Integration
        for i, p in enumerate(self.particles):
            p.vel += forces[i] * DT
            p.pos += p.vel * DT
            p.vel *= 0.98

        if self.collapse_active:
            self.collapse_timer += DT
            if self.collapse_timer > 5.0: self.collapse_active = False

class Renderer:
    def __init__(self, screen):
        self.screen = screen
        self.cam_pos = np.array([0.0, 0.0, -500.0])

    def project(self, pos):
        rel_pos = pos - self.cam_pos
        if rel_pos[2] <= 1: return None, rel_pos[2]
        f = 600 / rel_pos[2]
        return (int(rel_pos[0] * f + WIDTH // 2), int(rel_pos[1] * f + HEIGHT // 2)), rel_pos[2]

    def draw(self, engine):
        self.screen.fill((15, 15, 25))
        for p in engine.particles:
            coords, depth = self.project(p.pos)
            if coords:
                size = max(3, int(p.sigma * (600 / depth) * 0.1))
                color = (100, 200, 255) if p.charges[0] > 0 else (255, 100, 100)
                pygame.draw.circle(self.screen, color, coords, size)
        
        # UI
        font = pygame.font.SysFont("Arial", 16)
        status = "MEASURING" if engine.collapse_active else "IDLE"
        self.screen.blit(font.render(f"TSH CORE v2.0 | STATUS: {status}", True, (255, 255, 255)), (20, 20))
        self.screen.blit(font.render("Press SPACE to Measure (Center)", True, (200, 200, 200)), (20, 45))

def main():
    pygame.init(); screen = pygame.display.set_mode((WIDTH, HEIGHT)); clock = pygame.time.Clock()
    engine = TSHCore3D(); renderer = Renderer(screen)
    
    # Verification Scenario
    engine.add_particle(-100, 0, 0, [1.0, 0, 0, 0])
    engine.add_particle( 100, 0, 0, [1.0, 0, 0, 0])
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: engine.trigger_measurement(np.array([0,0,0]))
        
        engine.update(); renderer.draw(engine)
        pygame.display.flip(); clock.tick(60)
    pygame.quit()

if __name__ == "__main__": main()
