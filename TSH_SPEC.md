# Thickness Structure Hypothesis (TSH): Formal Specification

---

## 1. Minimal Structural Principle
TSH is defined by three irreducible degrees of freedom:
- **$p(x)$ (Existence Thickness)**: A scalar field representing the intensity of existence.
- **$\Delta f$ (Spreading Variable)**: Internal degree of freedom governing structural expansion/interference.
- **$\gamma_T$ (Contracting Variable)**: Internal degree of freedom governing structural localization/collapse.

## 2. Unified Structural Equation of Motion
All dynamics in TSH (quantum, classical, and gravitational) are governed by a single covariant equation:
$$\frac{Du^{\mu}}{D\tau} = -\nabla^{\mu} \ln p + F^{\mu}(\Delta f, \gamma_T)$$
Where:
- $\frac{Du^{\mu}}{D\tau}$ is the geometric covariant acceleration.
- $-\nabla^{\mu} \ln p$ represents the structural "spreading tendency" (quantum behavior).
- $F^{\mu}(\Delta f, \gamma_T)$ is the structural force arising from the competition between internal variables.

## 3. Structural Phase Diagram
The state space of $(\Delta f, \gamma_T)$ is organized into three discrete structural phases:
1. **Stable Phase (Quantum-like)**: High $\Delta f$, low $\gamma_T$. Governed by interference and spreading.
2. **Composite Phase (Classical-like)**: Balanced $\Delta f$ and $\gamma_T$. Governed by trajectories and stable structures.
3. **Core Phase (Gravitational-like)**: High $\gamma_T$, low $\Delta f$. Governed by irreversible collapse and singularity-like localization.

## 4. Interaction Slots
TSH provides a parallel architecture for integrating external fields:
- **Geometry Slot**: General Relativity metric $g_{\mu\nu}$.
- **Matter/Gauge Slots**: External forces/potentials are appended to the right-hand side of the unified equation without altering the core structural update rules.

## 5. Computational Model
- **Direct Update**: Behavioral transitions are computed via phase thresholds rather than iterative solvers.
- **Neighbor Search**: $O(N)$ efficiency using Uniform Grid Spatial Hashing.
- **Parallelism**: Single-kernel execution (GPU compute) for all phases, ensuring zero-branching overhead.

## 6. Structural Action
The unified structural dynamics of TSH can be generated from the following minimal action:
$$S = \int d^4x [L_{\text{GR}} + p \ln p + (\nabla p)^2 + \Phi_{\text{struct}}(p, \Delta f, \gamma_T)]$$
This action defines the minimal structural principle from which the unified equation of motion follows.

---

