# TSH Physics Engine v1.0: Grand Unified Universal OS
## Technical Manual & API Reference (Official Release v1.0)

---

### 0. File Inventory & System Roles

The following files constitute the TSH Engine v1.0:

- **ultimate_tsh_simulator.py** (Physics Reference)
  - Python prototype and the ground truth for all physics logic in v1.0.
- **TSHUnifiedForce.compute** (GPU Core Engine)
  - Handles 3D Unified Force computation and volumetric phase mapping.
- **TSHCore.cs** (C# Master Core)
  - Definitions for Particle Data Structures and Material Presets.
- **TSHFieldCompiler.cs** (Physics Compiler)
  - Generates phase boundaries and GPU constants from Material Assets.
- **TSHMaterialBlob.cs** (ECS Material Dictionary)
  - BlobAsset utility for ultra-fast material lookup at runtime.
- **TSHPositionUpdateSystem.cs** (ECS Integration System)
  - Burst-compiled system for high-performance position updates.
- **TSHFieldCompute.compute** (Field Utility)
  - (Optional) Auxiliary compute kernels for field pre-processing.
- **official_documentation_EN.md** (Master Manual - EN)
  - This technical documentation (v1.0).
- **official_documentation_JP.md** (Master Manual - JP)
  - Technical Documentation & API Reference (Japanese v1.0).

---

### 1. Architectural Overview (v1.0)

The TSH (Thickness Structure Hypothesis) Engine v1.0 is a 
**Unified Field Physics Platform** designed for real-time simulation 
of arbitrary interactions. It maps all fundamental forces into 
a single **Existence Thickness Field ($p$)** and 4 abstract channels.

### 2. Core Physics Specification

All forces are derived from the gradient of the existence thickness field.

#### The Unified Force Equation:
**F_total = F_struct + Σ F_channel,k**

- **F_struct**: Structural coherence based on p-field gradients.
- **F_channel,k**: Interaction dynamics based on charge-weighted gradients.

### 3. Material Domain Mapping

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

### 4. API Reference (C# / ECS)

#### `TSHParticleData`
The primary data structure for entities.
```csharp
public struct TSHParticleData {
    public float3 position;
    public float4 charges; // Abstract q1-q4
    public int materialId; // Lookup index
}
```

#### `TSHFieldCompiler`
Automates phase boundary derivation.
- **Method**: `Compile()`
- **Role**: Updates GPU constants dynamically from material assets.

### 5. GPU Visualization Layers (v1.0)

- **Layer 1: Phase Map**: RGB heatmap based on state (Stable/Strong/Core).
- **Layer 2: Channel Map**: Visualizes q1-q4 using specific hues.
- **Layer 3: Boundary Map**: Procedural contours for phase transitions.

---
*(C) 2026 TSH Dynamics Research Group. All Rights Reserved. v1.0*
