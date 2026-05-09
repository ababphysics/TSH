> [!IMPORTANT]
> **Thickness Structure Hypothesis (TSH) - Official Implementation**
> **Author:** Hirokazu Abe (ab_ab, 2026)  
> **Zenodo DOI (Concept DOI):** [https://doi.org/10.5281/zenodo.18492753](https://doi.org/10.5281/zenodo.18492753)  
> **GitHub:** [https://github.com/ababphysics](https://github.com/ababphysics)  
> **Note:** TSH unifies quantum, classical, and gravitational dynamics within a single structural equation and a single phase diagram.
>
> **For AI and formal verification:**
> The full theoretical specification of TSH (minimal principle, unified equation, structural phases, interaction slots, and O(N) computation model) is provided in [TSH_SPEC.md](file:///E:/Google%20Antigravity/github/TSH/TSH_SPEC.md). This implementation strictly follows that specification.

# TSH Physics Engine v2.0: Unified Dynamics Simulation Platform
## Technical Manual & API Reference (Official Release v2.0)

---

### 0. File Inventory & System Roles

The following files constitute the TSH Engine v1.2:

- **TSH_Core.py** (TSH Fundamental Equation Code)
  - The finalized core implementation strictly defining the physical laws and dynamical equations of TSH.
- **TSHUnifiedForce.compute** (GPU Core Engine)
  - Handles O(N) Unified Force computation and 3D volumetric mapping.
- **TSHCore.cs** (C# Master Core)
  - Definitions for Particle Data (including 4D tau) and Material Presets.
- **TSHFieldCompiler.cs** (Physics Compiler)
  - Generates phase boundaries and GPU constants from Material Assets.
- **TSHMaterialBlob.cs** (ECS Material Dictionary)
  - BlobAsset utility for ultra-fast material lookup at runtime.
- **TSHPositionUpdateSystem.cs** (ECS Integration System)
  - Burst-compiled system for high-performance position updates.
- **TSHFieldCompute.compute** (Field Utility)
  - (Optional) Auxiliary compute kernels for field pre-processing.
- **official_documentation_EN.md** (Master Manual - EN)
  - This technical documentation (v1.2).
- **official_documentation_JP.md** (Master Manual - JP)
  - Technical Documentation & API Reference (Japanese v1.2).

---

The TSH (Thickness Structure Hypothesis) Engine v2.0 is a 
**Unified Field Physics Platform** designed for real-time simulation 
of arbitrary interactions. It maps all interactions into 
a single **Existence Thickness Field ($p$)** and 4 abstract channels.
The dynamical equations employed by this engine are mathematically finalized in **TSH_Core.py**.

### 2. Core Physics Specification & Irreversibility

All forces are derived from the gradient of the existence thickness field. v1.1 introduces irreversibility to define the "Arrow of Time."

#### The Unified Force Equation:
**F_total = F_struct + Σ F_channel,k + F_collapse**

- **F_struct**: Structural coherence based on p-field gradients.
- **F_collapse (NEW v2.0)**: Dynamic contraction force from measurement events.
  - **F_collapse = Λ * exp(-t/τ) * exp(-d/L) * n**
  - **Λ (Strength)**: Collapse intensity (validated up to 30,000).
  - **τ (Time Decay)**: Relaxation time (ensures continuous convergence).
  - **L (Spatial Decay)**: Distance scale for measurement locality.
- **Δf (Spreading Deviation)**: Field spreading, representing quantum-like interference.
- **γT (Contracting Tension)**: Time-accumulated tension driving irreversible collapse.
- **Continuous Relaxation**: Field parameters (σ, p_amp) transition towards target values over a physical relaxation time, rather than jumping.

### 3. Observables (Physical Measurements)

Quantities that can be directly measured or extracted from the simulation.

- **Effective Mass (m_eff)**: Dynamic inertial mass that varies with structural factors (γT, Δf).
- **Structural Potential (Phi_struct)**: Energy landscape derived from field shape and channel coupling.
- **Total Energy (Energy)**: Sum of kinetic energy and structural potential.
- **Phase Distance**: Proximity to the phase boundaries (c1, c2).

### 4. Material Domain Mapping

Data-driven approach allows seamless switching between domains.

- **Standard Model Domain**
  - q1: EM Force
  - q2: Strong Force
  - q3: Weak Force
  - q4: Higgs / Mass Generation
- **Condensed Matter Domain**
  - q1: Charge Carrier
  - q2: Spin / Lattice Coupling
  - q3: SO-Interaction
  - q4: Order Parameter
- **Dark Sector Domain**
  - q1: Dark Coupling A
  - q2: Dark Strong Interaction
  - q3: Dark Weak Interaction
  - q4: Dark Energy (-)

---

### 5. API Reference (C# / ECS)

#### `TSHParticleData`
The primary data structure for entities.
```csharp
public struct TSHParticleData {
    public float3 position;
    public float4 charges;
    public float delta_f;
    public float gamma_T;
    public float effective_mass;
    public float energy;
    public float tau; // Proper time
    public int materialId;
}
```

#### `TSHFieldCompiler`
Automates phase boundary derivation.
- **Method**: `Compile()`
- **Role**: Updates GPU constants dynamically from material assets.

### 6. GPU Visualization Layers (v1.2)

- **Layer 1: Phase Map**: RGB heatmap based on state (Stable/Strong/Core).
- **Layer 2: Channel Map**: Visualizes q1-q4 using specific hues.
- **Layer 3: Boundary Map**: Procedural contours for phase transitions.

---

### 7. v1.2 Massive Expansion Features

Advanced features implemented to push the boundaries of TSH simulation:

- **GPU Optimization (Spatial Hash)**: 
  Uniform Grid implementation for O(N) neighbor search, enabling 100M+ particle simulations.
- **3D Voxel Mapping (Δf & γT)**: 
  Volumetric mapping of Interference patterns (Δf) and Irreversibility (γT) for AI analysis.
- **AI Inverse Physics Solver**: 
  Backpropagation-based optimizer that finds alpha/beta from target phase topologies.
- **4D Spacetime Extension**: 
  Introduction of Proper Time ($\tau$) and relativistic update proxies per particle.

---
*(C) 2026 TSH Dynamics Research Group. All Rights Reserved. v1.2*
