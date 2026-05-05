# TSH AI Physics Engine: Universal OS for Artificial Intelligence
## Implementation Manual & Architecture (v1.0)

---

### 0. File Inventory & AI Roles

The following files constitute the TSH AI Universe OS:

- **tsh_ai_core.py** (Differentiable Core)
  - PyTorch implementation allowing backprop through physical laws.
- **tsh_ai_api.py** (Universe Editing)
  - AI bridge to rewrite materials.json and evaluate states.
- **materials.json** (AI Physics Dictionary)
  - JSON-formatted storage for alpha/beta coupling constants.
- **AI_Implementation_Manual_EN.md** (Technical Manual)
  - This master reference document (English).
- **AI_Implementation_Manual_JP.md** (Technical Manual)
  - Master Manual & Implementation Guide (Japanese).

---

### 1. Overview

The TSH AI Engine is a 3-layer framework designed to bridge physical 
simulation with Machine Learning. It enables AI to **perceive** physical 
states, **learn** laws via differentiation, and **edit** the universe 
by re-compiling physical constants.

---

### The 6 Factors of Irreversibility (The Core of AI Universe OS)

To master "Time's Arrow," the AI must interact with these 6 factors:

1. **Δf (Spreading Deviation)**: Field spreading. Its sudden decay triggers learning events.
2. **γT (Contracting Tension)**: Monitored as the "Universe's Memory."
3. **Δf–γT Phase Diagram**: The AI's blueprint for defined irreversible collapse.
4. **Asymmetric Transitions (Hysteresis)**: Hard constraints in inverse problems.
5. **Collapse Internal Structure**: Feature extraction from Δf decay and p_amp spikes.
6. **Memory Effect**: Learning causality from tensor histories.

### Integration of Observables

The AI utilizes physical observables derived from internal variables as features.

1. **Effective Mass (m_eff)**: Learning changes in inertia.
2. **Structural Potential (Phi_struct)**: Learning energy landscape gradients.
3. **Total Energy (Energy)**: Evaluating system conservation and stability.
4. **Phase Distance**: Quantifying the "margin" before collapse.

---

### Layer 1: Data Structuring (Perception)
TSH states are exported as tensors and JSON for seamless integration 
with AI models (CNNs, GNNs, Transformers).

- **`tsh_ai_core.save_tensors()`**: 
  Exports p-field, channels, and phase maps along with **Effective Mass and Energy tensors**.
- **`tsh_ai_api.export_observables()`**: 
  Batch exports observation data per frame.

### Layer 2: Differentiable Engine (Learning)
Implemented in PyTorch, allowing AI to perform **Physical Phenomenon Optimization**.

- **Differentiation**: 
  Allows tuning physical constants to minimize energy or maximize stability.
- **Applications**: 
  Finding coupling constants for stable structural topologies.

### Layer 3: Universe Editing API (Agency)
AI monitors the simulation in real-time and fine-tunes physical laws.

- **`TSHAI_API.get_observables()`**: 
  Retrieves real-time physical quantities of specific particles for decision-making.
- **Feedback Loop**:
  1. AI proposes new `beta` coupling.
  2. `TSHFieldCompiler` reads JSON and re-generates HLSL.
  3. The GPU simulator updates with the new physical laws instantly.

---

### AI Evaluation Metrics (Objective Functions)

AI evaluates the "Universe Quality" through specific metrics:

1. **Core Density**: Ratio of terminal collapse regions.
2. **Structural Entropy**: Complexity of the phase boundaries.
3. **Channel Balance**: Interaction distribution between q1 ~ q4.

---
---

### Online Learning Loop (Self-Evolution Cycle)

A framework for real-time physical law evolution by bridging Unity (Physics) and Python (AI).

#### 1. Perception (GPU → AI)
- Call `GetParticleDataFromGPU()` in Unity to fetch the particle buffer to the CPU.
- Transfer that data to Python as `initial_state` (pos, vel, Δf, γT, uμ, τ).

#### 2. Learning (AI)
- Run `solve_inverse_problem` in Python.
- Calculate optimized physical constants (α, β, etc.) via the differentiable TSHAICore to minimize target error.

#### 3. Action (AI → JSON)
- AI updates `materials.json`.

#### 4. Reaction (JSON → GPU)
- Unity triggers `HotReloadMaterials()`, instantly re-uploading optimized constants to the GPU.

Through this cycle, the TSH universe autonomously converges toward the "Ideal Physical Laws" designed by the AI.

---
*(C) 2026 TSH AI Research Lab. Bridging Physics and Intelligence. v1.2*
