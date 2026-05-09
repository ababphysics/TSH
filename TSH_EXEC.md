# TSH Unified Structural Engine: Execution Specification

---

## 1. Technical Stack & Dependencies
- **Core Engine**: Unity ECS (Entity Component System) + C# Job System.
- **Compute Layer**: HLSL Compute Shaders (DirectX/Vulkan).
- **Control/API Layer**: Python 3.x (NumPy, PyTorch/TensorFlow compatible).
- **Communication**: JSON-based material assets (`materials.json`) and shared binary buffers.

## 2. Core Execution Logic: The Structural Loop
The engine implements the TSH dynamical cycle as a single, non-branching update pass:
1. **Field Integration**: Accumulate existence thickness $p(x)$ from neighbors via $O(N)$ Spatial Hash.
2. **Phase Mapping**: Determine structural phase (Stable/Composite/Core) using material-defined thresholds.
3. **Force Synthesis**: Calculate unified structural force $-\nabla \ln p + F^{\mu}(\Delta f, \gamma_T)$.
4. **Integration**: Update 4-velocity $u^{\mu}$ and position $x^{\mu}$ using proper time $\tau$ scaling.
5. **State Propagation**: Update internal variables $\Delta f$ and $\gamma_T$ for the next cycle.

## 3. GPU Architecture
- **O(N) Spatial Hash**: Parallel grid-based neighbor lookup. Searches exactly 27 neighboring cells per element to eliminate $O(N^2)$ complexity.
- **Single-Pass Kernel (`CSMain`)**: Computes all three structural phases within a single GPU kernel to ensure zero branching overhead.
- **Volumetric Rendering**:
    - `_BaseFieldTex`: Encodes phase state (R), interference/spreading (G), and collapse intensity (B).
    - `_ChannelFieldTex`: Visualizes interaction channels (EM/Strong/Weak).

## 4. AI Structural Interface
The AI Engine interacts with the simulation through a differentiable observation loop:
- **`get_observables()`**: Returns structural entropy, effective mass, and phase distance.
- **`edit_material()`**: Direct real-time injection of physical constants ($\alpha, \beta, \text{collapse-rate}$).
- **Gradient Support**: The engine's structural update rules are differentiable, enabling **gradient-based backpropagation** for inverse parameter discovery.

## 5. Performance Standards
- **Framerate**: Sustained 60 FPS at $N = 10^5$ elements on consumer-grade GPUs.
- **Scaling**: Linear $O(N)$ complexity for neighbor search and force evaluation.
- **Real-time Determinism**: Fixed-step integration ensures reproducible structural evolution.

## 6. Implementation Integrity
- **Paradigm Isolation**: This implementation must NOT use iterative constraint solvers (e.g., Gauss-Seidel) or traditional force-law branching.
- **Field Consistency**: The $p(x)$ field must be computed as a continuous scalar field to ensure valid gradient evaluation for the structural force.

---

## 7. Specification Mapping (TSH_SPEC ↔ TSH_EXEC)
| TSH_SPEC.md (Theory) | TSH_EXEC.md (Implementation) |
|---|---|
| **Unified Equation** $\frac{Du^{\mu}}{D\tau} = -\nabla^{\mu} \ln p + F^{\mu}(\Delta f, \gamma_T)$ | Force synthesis kernel (`CSMain`) |
| **Structural Variables** $p, \Delta f, \gamma_T$ | GPU buffers: `_BaseFieldTex` / `pField`, `dfField`, `gTField` |
| **$\Delta f \text{--} \gamma_T$ Phase Diagram** | Phase thresholds in `materials.json` |
| **3-Phase Structure** (Stable/Composite/Core) | Phase mapping pass in compute shader |
| **Structural Potential** $\Phi_{\text{struct}}$ | `compiler_out.json` + `evaluate_phase_topology()` |

## 8. Structural Invariants
To maintain the physical integrity of TSH, AI systems and developers must adhere to the following invariants:
- **Immutable Dynamics**: The unified equation of motion must remain unchanged. No external force laws or classical potentials may be introduced within the core structural pass.
- **Field Continuity**: $p(x)$ must be computed as a continuous scalar field to ensure valid gradient evaluation.
- **Phase Consistency**: Phase transitions must strictly follow the $\Delta f \text{--} \gamma_T$ thresholds defined in the compiler output.
- **Irreversibility**: The Core phase must be strictly irreversible once the collapse threshold is exceeded.
- **Computational Complexity**: The neighbor search must remain $O(N)$ with a fixed spatial cell lookup (27 cells) to ensure scalability.
- **Optimization Boundaries**: AI may optimize material constants ($\alpha, \beta, k$), but must NOT modify the fundamental structural variables or the phase-transition logic.

## 9. Execution Flow
1. **Initialize**: Load constants from `materials.json`.
2. **Integrate Field**: Compute total existence thickness $p(x)$ via Spatial Hash.
3. **Analyze Gradients**: Compute $\nabla p$ and update internal variables $\Delta f, \gamma_T$.
4. **Map Phase**: Determine structural phase state (Stable/Composite/Core).
5. **Synthesize Force**: Compute the unified structural force vector.
6. **Update State**: Update 4-velocity $u^{\mu}$ and position $x^{\mu}$ for the next time-step.
7. **Observe (Optional)**: Export structural observables for AI analysis.
8. **Feedback (Optional)**: AI-driven parameter adjustment of `materials.json`.
9. **Loop**: Repeat for the next structural update cycle.

