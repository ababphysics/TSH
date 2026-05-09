> [!IMPORTANT]
> **Thickness Structure Hypothesis (TSH) - Official Implementation**
> **Author:** Hirokazu Abe (2026)  
> **Zenodo DOI (Concept DOI):** [https://doi.org/10.5281/zenodo.18492753](https://doi.org/10.5281/zenodo.18492753)  
> **GitHub:** [https://github.com/ababphysics](https://github.com/ababphysics)  

# TSH AI Interface: Physics Simulation Analysis & Parameter Control API
## Implementation Manual (v2.0)

---

### 0. File Inventory & Roles

This directory provides a Python interface for AI models to read physics simulation data and dynamically adjust simulation parameters.

- **tsh_ai_api.py** (Simulation Analysis & Control API)
  - An API class to retrieve particle states (position, velocity, energy, etc.) and facilitate analysis or data handoff to external machine learning models.
- **materials.json** (Material Configuration File)
  - A configuration file defining physical constants (interaction strengths, etc.) for each particle type. Updating this file via the API instantly alters simulation behavior.

---

### 1. Overview

This interface serves as a standard Data I/O (Input/Output) layer, treating the physics simulation as an "environment" for AI training.

1. **Data Acquisition**: Retrieves physical quantities from the simulation (effective mass, total energy, field density, etc.) as NumPy arrays for use as AI input data.
2. **Parameter Control**: Enables the exploration of physical laws by optimizing material constants ($\alpha, \beta$, etc.) to induce specific physical phenomena, such as particle aggregation or stabilization.

---

### 2. Key Features of TSHAI_API

#### ■ Dynamic Parameter Updates (Agency)
- **`edit_material()`**: 
  Rewrites physical constants within `materials.json`. When the simulator reloads this file, the laws of the simulated universe change in real-time.

#### ■ Numerical State Evaluation (Evaluation)
- **`evaluate_phase_topology()`**: 
  Quantifies state configurations, such as particle density ("core_density") and topological complexity ("structural_entropy"), based on field distribution.
- **`evaluate_irreversibility()`**: 
  Scores the contraction level and irreversibility of the system, which can be utilized as a "Reward" in reinforcement learning.

#### ■ Data Export for Training (Data Export)
- **`export_observables()`**: 
  Saves simulation observation data in `.npy` format. This simplifies supervised learning of physical phenomena using external frameworks like PyTorch or TensorFlow.

---

### 3. Standard Usage Workflow

1. **Observe**: Retrieve simulation states using the API and calculate evaluation scores.
2. **Infer**: Based on the scores, an external AI model infers better physical parameters.
3. **Apply**: Update `materials.json` using the API.
4. **Verify**: Continue the simulation in the updated environment and observe the results.

---
*(C) 2026 TSH AI Research Lab. Interface for Simulation Analysis. v2.0*
