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

This ensures that the GIF reflects the exact mathematical structure of TSH,
not an illustration.

## 2. Overview

TSH is a unified structural theory that derives quantum mechanics, classical physics, and general relativity as phase‑dependent limits of a single covariant action.

This repository provides the official computational model and reference materials for the Thickness Structure Hypothesis (TSH), a structural framework that unifies quantum, classical, and gravitational behavior within a single minimal covariant action.
TSH treats these three regimes as distinct structural phases—Stable, Composite, and Core—of one underlying system.

TSH provides a continuous structural resolution to the measurement problem, quantum nonlocality, and the classical–quantum transition.

<img src="assets/phase_diagram.png"
     alt="TSH Phase Diagram showing the three structural phases—Stable (quantum), Composite (classical), and Core (gravitational)—as regions in the Δf–γT plane, with smooth boundaries c1(γT) and c2(γT) defining phase transitions."
     width="400">

TSH provides structural resolutions to several long‑standing problems in modern physics:

- the measurement problem and objective wave‑packet collapse
- the lack of a continuous bridge between Bohmian mechanics and general relativity
- quantum nonlocality vs relativistic locality
- the absence of a unified dynamical equation covering quantum, classical, and gravitational regimes
- the need for a covariant formulation of collapse‑like behavior
- the incompatibility between decoherence models and gravitational localization

## 3. Key Breakthroughs of TSH

**1. One Action, Three Regimes**  
TSH derives three distinct structural phases from the same underlying principles:

- **Core phase** → geodesic equation of general relativity
- **Composite phase** → classical limit of quantum mechanics
- **Stable phase** → Bohm‑type quantum force

**2. Plug-and-Play Interaction Slot**

$$
E_{\mu\nu} = G_{\mu\nu} + U_{\mu\nu}
$$

**3. Resolving Quantum Inconsistencies**  
The $\Delta f - \gamma_T$ phase structure provides a continuous bridge between regimes.

### 3.4 Comparison with Existing Approaches

| Feature | String Theory | Loop Quantum Gravity | TSH (This Model) |
| :--- | :--- | :--- | :--- |
| **Unification Mechanism** | Strings / Branes | Spin Networks | $\Delta f - \gamma_T$ Phase Structure |
| **Measurement Problem** | External Postulate | Not Addressed | Internal Phase Transition ($\gamma_T$) |
| **GR Limit** | Requires Compactification | Nontrivial | Exact ($\Phi \to 0$) |
| **Quantum–Classical Bridge** | Not Explicit | Not Explicit | Continuous Structural Transition |
| **Collapse‑like Behavior** | Absent | Absent | Core Phase Localization |
| **Executable Model** | No | No | Yes (Ultimate TSH Simulator) |

## 4. Internal Variables and Phase Structure

TSH introduces three internal quantities:

- $p(x)$ — existence thickness
- $\Delta f$ — structural deviation
- $\gamma_T$ — structural tension

These span the $\Delta f - \gamma_T$ phase diagram:

- Core (gravitational / measurement)
- Composite (classical)
- Stable (quantum)

<img src="assets/three_phases.png"
     alt="Comparison of the three TSH structural phases via p(x): Stable phase shows quantum interference fringes and wide nonlocal spreading; Composite phase shows a smooth classical Gaussian-like packet with suppressed fringes; Core phase shows strong gravitational localization with collapse-like sharp peak."
     width="1000">

## 5. Phase Diagram and Dynamic Feedback

$$
F^\mu = -\nabla^\mu \Phi_{\text{struct}}(\Delta f, \gamma_T)
$$

Feedback loop:

`phase` → `structural force` → `motion` → `update of` $p, \Delta f, \gamma_T$ → `phase`

## 6. Minimal Covariant Action

$$
\mathcal{L} = R + p \ln p + (\nabla \ln p)^2 + \Phi_{\text{struct}}(\Delta f, \gamma_T)
$$

## 7. Unified Dynamical Equation

$$
\frac{D u^\mu}{D\tau} = -\nabla^\mu \ln p + F^\mu(\Delta f, \gamma_T)
$$

This single equation reproduces:

- quantum behavior (Stable)
- classical trajectories (Composite)
- GR geodesics (Core)

## 8. Limiting Regimes

**Quantum limit**  
$-\nabla \ln p$ dominates → Bohm‑type force

**Classical limit**  
Gradients small → deterministic motion

**GR limit**  
$\Phi_{\text{struct}} \to 0$ → exact geodesic equation

## 9. Phase‑Diagram Compression

The $\Delta f - \gamma_T$ diagram compresses:

- phase structure
- structural potential
- structural force
- unified equation
- tensor equation
- interaction slot

into one representation.

## 10. Hierarchical Interaction Slot

$$
E_{\mu\nu} = G_{\mu\nu} + U_{\mu\nu}
$$

## 11. Experimental Predictions

- Interference fringe on/off
- Weak‑measurement collapse
- Non‑Gaussian noise
- Two‑component spectra

## 12. Tensor Form of the Unified Equation

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

## 13. Full Lagrangian Density

$$
\mathcal{L} = R + p \ln p + (\nabla \ln p)^2 + \Phi_{\text{struct}}
$$

## 14. Phase‑Diagram Boundary Conditions

$$
\Delta f = c_1(\gamma_T), \quad \Delta f = c_2(\gamma_T)
$$

## 15. GR Limit (One‑Line Proof)

$$
\Phi_{\text{struct}} \to 0 \implies F^\mu \to 0 \implies \frac{D u^\mu}{D\tau} = 0
$$

## 16. Quantum Limit and Born Rule

$$
\int p(x) \, dx = 1 \implies p(x) = |\psi(x)|^2
$$

## 17. Theory ↔ Code Mapping Table

| Theory | Code | Function |
| :--- | :--- | :--- |
| $p(x)$ | `p` | `generate_wave` |
| $\Delta f$ | `mouse_df` | `update` |
| $\gamma_T$ | `mouse_g` | `update` |
| $c_1, c_2$ | `get_ultimate_boundaries` | `boundaries` |
| Phase | `color` | `generate_wave` |

## 18. Mathematical Closure of TSH

- Closed action
- Closed variables
- Closed phase diagram
- Closed unified equation
- Closed limits
- Closed simulator

## 19. Notation Summary

| Symbol | Meaning |
| :--- | :--- |
| $p(x)$ | Existence thickness |
| $\Delta f$ | Structural deviation |
| $\gamma_T$ | Structural tension |
| $F^\mu$ | Structural force |
| $\Phi_{\text{struct}}$ | Structural potential |
| $u^\mu$ | Four‑velocity |
| $c_1, c_2$ | Phase boundaries |

## 20. Formal Definitions

**Definition 1 — Existence Thickness**  
$p(x)$ is a normalized scalar field representing structural thickness.

**Definition 2 — Structural Deviation**  
$\Delta f$ quantifies deviation from minimal‑spread configuration.

**Definition 3 — Structural Tension**  
$\gamma_T$ controls phase transitions and collapse.

## 21. Proposition (Exact GR Limit)

**Proposition.**  
If $\Phi_{\text{struct}} \to 0$, then the unified equation reduces to the geodesic equation.

**Proof.**  
$F^\mu = -\nabla^\mu \Phi_{\text{struct}}$.  
Thus $\Phi_{\text{struct}} \to 0 \implies F^\mu \to 0$.  
Thus the unified equation reduces to the geodesic equation:

$$
\frac{D u^\mu}{D\tau} = 0.
$$

## 22. TSH in One Equation

$$
\frac{D u^\mu}{D\tau} = -\nabla^\mu \ln p - \nabla^\mu \Phi_{\text{struct}}(\Delta f, \gamma_T)
$$

## 23. Unified Regime Table

| Regime | Dominant Term | Behavior |
| :--- | :--- | :--- |
| Quantum | $-\nabla \ln p$ | Interference, nonlocality |
| Classical | small gradients | Deterministic motion |
| GR | $\Phi_{\text{struct}} \to 0$ | Geodesic motion |

## 24. License

All code and scripts in this repository are released under the **MIT License**.
The code may be used, modified, and redistributed with attribution.

The Thickness Structure Hypothesis paper (PDF and HTML) in the `data/` directory, as well as the figures (e.g., `Figure_1.png`) and theoretical content in this README, are **© 2026 Hirokazu Abe**.
These materials are not covered by the MIT License.
Unauthorized redistribution is prohibited.
