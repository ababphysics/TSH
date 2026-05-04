# TSH (Thickness Structure Hypothesis)

**Author:** Hirokazu Abe (2026)

---

## 1. Executable Structural Model

<img src="assets/simulation_demo.gif" width="800">

The animation above is generated directly from the Ultimate TSH Simulator,
a fully runnable implementation of the unified dynamical equation.
The simulator computes:

- the $\Delta f$–$\gamma_T$ phase deformation
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

<img src="assets/phase_diagram.png" width="400">

### Key Breakthroughs of TSH

**1. One Action, Three Regimes**  
TSH derives three distinct structural phases from the same underlying principles:
- **Core phase** → geodesic equation of general relativity
- **Stable phase** → Bohm‑type quantum force
- **Composite phase** → classical limit of quantum mechanics

**2. Plug-and-Play Interaction Slot**  
$$
E_{\mu\nu} = G_{\mu\nu} + U_{\mu\nu}
$$

**3. Resolving Quantum Inconsistencies**  
The $\Delta f$–$\gamma_T$ phase structure provides a continuous bridge between regimes.

## 3. Internal Variables and Phase Structure

TSH introduces three internal quantities:

- $p(x)$ — existence thickness
- $\Delta f$ — structural deviation
- $\gamma_T$ — structural tension

These span the $\Delta f$–$\gamma_T$ phase diagram:

- Stable (quantum)
- Composite (classical)
- Core (gravitational / measurement)

<img src="assets/three_phases.png" width="1000">

## 4. Phase Diagram and Dynamic Feedback

$$
F^\mu = -\nabla^\mu \Phi_{\text{struct}}(\Delta f, \gamma_T)
$$

Feedback loop:

`phase` → `structural force` → `motion` → `update of` $p, \Delta f, \gamma_T$ → `phase`

## 5. Minimal Covariant Action

$$
\mathcal{L} = R + p \ln p + (\nabla \ln p)^2 + \Phi_{\text{struct}}(\Delta f, \gamma_T)
$$

## 6. Unified Dynamical Equation

$$
\frac{D u^\mu}{D\tau} = -\nabla^\mu \ln p + F^\mu(\Delta f, \gamma_T)
$$

This single equation reproduces:

- quantum behavior (Stable)
- classical trajectories (Composite)
- GR geodesics (Core)

## 7. Limiting Regimes

**Quantum limit**  
$-\nabla \ln p$ dominates → Bohm‑type force

**Classical limit**  
Gradients small → deterministic motion

**GR limit**  
$\Phi_{\text{struct}} \to 0$ → exact geodesic equation

## 8. Phase‑Diagram Compression

The $\Delta f$–$\gamma_T$ diagram compresses:

- phase structure
- structural potential
- structural force
- unified equation
- tensor equation
- interaction slot

into one representation.

## 9. Hierarchical Interaction Slot

$$
E_{\mu\nu} = G_{\mu\nu} + U_{\mu\nu}
$$

## 10. Usage

```bash
python scripts/run_simulation.py
```

## 11. License

MIT for code.  
Theory & figures © 2026 Hirokazu Abe.

## 12. Citation

Hirokazu Abe (2026). *Thickness Structure Hypothesis.*  
DOI: [https://doi.org/10.5281/zenodo.19564362](https://doi.org/10.5281/zenodo.19564362)

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
Substituting yields $\frac{D u^\mu}{D\tau} = 0$. ∎

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
