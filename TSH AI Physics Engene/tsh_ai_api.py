import json
import os

class TSHAI_API:
    """
    Universe Editing API for AI
    ===========================
    Enables AI to write physical laws by editing JSON material tables 
    and evaluating the resulting phase topology.
    """
    def __init__(self, materials_path="materials.json"):
        self.materials_path = materials_path
        self.materials = self.load_materials()

    def load_materials(self):
        if os.path.exists(self.materials_path):
            with open(self.materials_path, "r") as f:
                return json.load(f)
        return {}

    def edit_material(self, mat_key, beta=None, alpha=None):
        """AI edits the universe's material properties."""
        if mat_key not in self.materials:
            self.materials[mat_key] = {"beta": [0,0,0,0], "alpha": 12.8}
        
        if beta is not None: self.materials[mat_key]["beta"] = beta
        if alpha is not None: self.materials[mat_key]["alpha"] = alpha
        
        self.save()
        print(f"AI Update: {mat_key} laws rewritten.")

    def save(self):
        with open(self.materials_path, "w") as f:
            json.dump(self.materials, f, indent=2)

    def evaluate_phase_topology(self, p_total_array):
        """
        AI Evaluation Function (Example Objective Functions)
        """
        metrics = {
            "core_density": float((p_total_array > 40.0).mean()),
            "strong_coverage": float(((p_total_array > 15.0) & (p_total_array <= 40.0)).mean()),
            "structural_entropy": float(self._compute_entropy(p_total_array))
        }
        return metrics

    def _compute_entropy(self, arr):
        # Placeholder for structural complexity score
        return (arr.max() - arr.min()) / (arr.mean() + 1e-7)

# --- Compiler JSON Bridge ---
def export_compiler_results(mat_id, strong_th, core_th, path="compiler_out.json"):
    data = {
        "materialId": mat_id,
        "strong_threshold": float(strong_th),
        "core_threshold": float(core_th)
    }
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
