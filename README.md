# TSH (Thickness Structure Hypothesis)

**Author:** Hirokazu Abe (2026)

*Thickness Structure Hypothesis.*  
Zenodo DOI: [https://doi.org/10.5281/zenodo.19564362](https://doi.org/10.5281/zenodo.19564362)

---

## 1. Executable Structural Model

<img src="assets/simulation_demo.gif"
     alt="Dynamic TSH simulation: irreversible phase transitions of existence thickness p(x) across Stable (quantum), Composite (classical), and Core (gravitational/measurement) phases, driven by structural deviation Δf, structural tension γ_T, and mass-dependent boundary scaling in the unified dynamical equation."
     width="700">

The animation above is generated directly from the Ultimate TSH Simulator,
a fully runnable implementation of the unified dynamical equation.

The simulator computes:
- the $\Delta f - \gamma_T$ phase deformation
- mass‑dependent boundary scaling
- irreversible phase transitions
- the evolving thickness distribution $p(x)$

## 2. Overview

TSH is a unified structural theory that derives quantum mechanics, classical physics, and general relativity as phase‑dependent limits of a single covariant action.

<img src="assets/phase_diagram.png"
     alt="TSH Phase Diagram showing the three structural phases—Stable (quantum), Composite (classical), and Core (gravitational)—as regions in the Δf–γT plane, with smooth boundaries c1(γT) and c2(γT) defining phase transitions."
     width="400">

TSH provides structural resolutions to several long‑standing problems:
- objective wave‑packet collapse
- Bohmian mechanics vs general relativity
- quantum nonlocality vs relativistic locality
- unified dynamics across quantum/classical/GR
- covariant collapse-like behavior
- decoherence vs gravitational localization

## 3. Key Breakthroughs of TSH

### 3.1 One Action, Three Regimes

TSH derives three structural phases from one covariant action:
- **Core** → GR geodesics
- **Composite** → classical limit
- **Stable** → Bohm‑type quantum force

### 3.2 Unified Tensor Equation
$$
E_{\mu\nu} = G_{\mu\nu} + U_{\mu\nu}
$$

### 3.3 Structural Phase Architecture

The $\Delta f - \gamma_T$ diagram provides a continuous bridge between regimes.

## 4. Comparison with Existing Approaches

| Feature | String Theory | Loop Quantum Gravity | TSH (This Model) |
| :--- | :--- | :--- | :--- |
| **Unification Mechanism** | Strings / Branes | Spin Networks | $\Delta f - \gamma_T$ Phase Structure |
| **Measurement Problem** | External Postulate | Not Addressed | Internal Phase Transition ($\gamma_T$) |
| **GR Limit** | Requires Compactification | Nontrivial | Exact ($\Phi \to 0$) |
| **Quantum–Classical Bridge** | Not Explicit | Not Explicit | Continuous Structural Transition |
| **Collapse Behavior** | Absent | Absent | Core Phase Localization |
| **Executable Model** | No | No | Yes (Ultimate TSH Simulator) |

## 5. Internal Variables and Phase Structure

TSH introduces three internal quantities:
- $p(x)$ — existence thickness
- $\Delta f$ — structural deviation
- $\gamma_T$ — structural tension

<img src="assets/three_phases.png"
     alt="Comparison of the three TSH structural phases via p(x): Stable phase shows quantum interference fringes and wide nonlocal spreading; Composite phase shows a smooth classical Gaussian-like packet with suppressed fringes; Core phase shows strong gravitational localization with collapse-like sharp peak."
     width="1000">

## 6. Structural Force and Phase‑Diagram Mapping

The structural force in the unified equation,
$$
F^\mu = -\nabla^\mu \Phi_{\text{struct}}(\Delta f, \gamma_T)
$$
is determined directly by the position on the $\Delta f - \gamma_T$ phase diagram:

- **Stable phase (quantum)**  
  $\Phi_{\text{struct}}$ shallow → $F^\mu$ small/oscillatory → interference & spreading
- **Composite phase (classical)**  
  $\Phi_{\text{struct}}$ nearly flat → $F^\mu \approx 0$ → classical deterministic motion
- **Core phase (gravitational/measurement)**  
  $\Phi_{\text{struct}}$ steep → $F^\mu$ strongly attractive → collapse-like localization

Crossing the boundaries
$$
\Delta f = c_1(\gamma_T), \quad \Delta f = c_2(\gamma_T)
$$
induces non‑perturbative jumps in $\Phi_{\text{struct}}$, producing irreversible transitions.

Thus the entire right-hand side of the unified equation is compressed into three regimes by the $\Delta f - \gamma_T$ phase diagram.

## 7. Phase Diagram and Dynamic Feedback

$$
F^\mu = -\nabla^\mu \Phi_{\text{struct}}
$$

Feedback loop:
`phase` → `structural force` → `motion` → `update of` $p, \Delta f, \gamma_T$ → `phase`

## 8. Minimal Covariant Action

$$
\mathcal{L} = R + p \ln p + (\nabla \ln p)^2 + \Phi_{\text{struct}}(\Delta f, \gamma_T)
$$

## 9. Unified Dynamical Equation

$$
\frac{D u^\mu}{D\tau} = -\nabla^\mu \ln p + F^\mu(\Delta f, \gamma_T)
$$

This single equation reproduces:
- quantum behavior
- classical trajectories
- GR geodesics

## 10. Limiting Regimes

**Quantum**  
$-\nabla \ln p$ dominates → Bohm‑type force

**Classical**  
Gradients small → deterministic motion

**GR**  
$\Phi_{\text{struct}} \to 0$ → geodesic equation

## 11. Phase‑Diagram Compression

The $\Delta f - \gamma_T$ diagram compresses:
- phase structure
- structural potential
- structural force
- unified equation
- tensor equation
- interaction slot

into one representation.

## 12. Hierarchical Interaction Slot

$$
E_{\mu\nu} = G_{\mu\nu} + U_{\mu\nu}
$$

## 13. Experimental Predictions

- Interference fringe on/off
- Weak‑measurement collapse
- Non‑Gaussian noise
- Two‑component spectra

## 14. Tensor Form of the Unified Equation

$$
\frac{D u^\mu}{D\tau} = -\nabla^\mu \ln p + F^\mu(\Delta f, \gamma_T)
$$

**Covariant derivative**
$$
\frac{D u^\mu}{D\tau} = \frac{d u^\mu}{d\tau} + \Gamma^\mu_{\alpha\beta} u^\alpha u^\beta
$$

**Structural force**
$$
F^\mu = -\nabla^\mu \Phi_{\text{struct}}
$$

## 15. Full Lagrangian Density

$$
\mathcal{L} = R + p \ln p + (\nabla \ln p)^2 + \Phi_{\text{struct}}
$$

## 16. Phase‑Diagram Boundary Conditions

$$
\Delta f = c_1(\gamma_T), \quad \Delta f = c_2(\gamma_T)
$$

## 17. GR Limit (One‑Line Proof)

$$
\Phi_{\text{struct}} \to 0 \implies F^\mu \to 0 \implies \frac{D u^\mu}{D\tau} = 0
$$

## 18. Quantum Limit and Born Rule

$$
\int p(x) \, dx = 1 \implies p(x) = |\psi(x)|^2
$$

## 19. Theory ↔ Code Mapping Table

| Theory | Code | Function |
| :--- | :--- | :--- |
| $p(x)$ | `p` | `generate_wave` |
| $\Delta f$ | `mouse_df` | `update` |
| $\gamma_T$ | `mouse_g` | `update` |
| $c_1, c_2$ | `get_ultimate_boundaries` | `boundaries` |
| Phase | `color` | `generate_wave` |

## 20. Mathematical Closure of TSH

- Closed action
- Closed variables
- Closed phase diagram
- Closed unified equation
- Closed limits
- Closed simulator

## 21. Notation Summary

| Symbol | Meaning |
| :--- | :--- |
| $p(x)$ | Existence thickness |
| $\Delta f$ | Structural deviation |
| $\gamma_T$ | Structural tension |
| $F^\mu$ | Structural force |
| $\Phi_{\text{struct}}$ | Structural potential |
| $u^\mu$ | Four‑velocity |
| $c_1, c_2$ | Phase boundaries |

## 22. Formal Definitions

**Definition 1 — Existence Thickness**  
$p(x)$ is a normalized scalar field representing structural thickness.

**Definition 2 — Structural Deviation**  
$\Delta f$ quantifies deviation from minimal‑spread configuration.

**Definition 3 — Structural Tension**  
$\gamma_T$ controls phase transitions and collapse.

## 23. Proposition (Exact GR Limit)

**Proposition.**  
If $\Phi_{\text{struct}} \to 0$, then the unified equation reduces to the geodesic equation.

**Proof.**  
$F^\mu = -\nabla^\mu \Phi_{\text{struct}}$.  
Thus $\Phi_{\text{struct}} \to 0 \implies F^\mu \to 0$.  

Thus the unified equation reduces to the geodesic equation:
$$
\frac{D u^\mu}{D\tau} = 0.
$$

## 24. TSH in One Equation

$$
\frac{D u^\mu}{D\tau} = -\nabla^\mu \ln p - \nabla^\mu \Phi_{\text{struct}}(\Delta f, \gamma_T)
$$

## 25. Unified Regime Table

| Regime | Dominant Term | Behavior |
| :--- | :--- | :--- |
| Quantum | $-\nabla \ln p$ | Interference, nonlocality |
| Classical | small gradients | Deterministic motion |
| GR | $\Phi_{\text{struct}} \to 0$ | Geodesic motion |

## 26. License

All code and scripts in this repository are released under the **MIT License**.
The code may be used, modified, and redistributed with attribution.

The Thickness Structure Hypothesis paper (PDF and HTML) in the `data/` directory, as well as the figures (e.g., `Figure_1.png`) and theoretical content in this README, are **© 2026 Hirokazu Abe**.
These materials are not covered by the MIT License.
Unauthorized redistribution is prohibited.

## 27. Citation

Hirokazu Abe (2026).  
*Thickness Structure Hypothesis.*  
Zenodo DOI: [https://doi.org/10.5281/zenodo.19564362](https://doi.org/10.5281/zenodo.19564362)

