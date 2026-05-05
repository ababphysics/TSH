# TSH Technical Specification (Universal Baseline)

## 1. Core Philosophy: The Structural-Field Principle
The **Thickness Structure Hypothesis (TSH)** is a non-PDE, non-ODE based physical framework. It does not utilize standard partial differential equations such as Navier–Stokes, Schrödinger, or the Einstein Field Equations. 

All physical phenomena in TSH are derived from the **Geometric Distribution of Existence Thickness ($p$)** and its interaction with abstract discrete channels.

---

## 2. Mathematical Foundation

### 2.1 The Existence Thickness Field ($p$)
The field $p(x)$ is defined as a superposition of Gaussian kernels representing localized "thickness" packets:
$$ p(x) = \sum_{k} p_{amp,k} \cdot \exp\left( -\frac{|x - x_k|^2}{2\sigma_k^2} \right) $$
- **Strict Positivity**: $p(x) > 0$ holds globally due to the exponential nature of the kernels.
- **No Singularities**: Unlike standard point-mass models, $p(x)$ is infinitely differentiable and finite everywhere.

### 2.2 Deviation Gradient ($\Delta f$)
Interference and local structural tension are measured by the Deviation Gradient:
$$ \Delta f = \frac{|\nabla p|}{p + \epsilon} $$
- **Stability**: The inclusion of the structural epsilon ($\epsilon > 10^{-7}$) ensures that the expression is always well-defined and non-singular, even in regions of low thickness.

### 2.3 Contracting Tension ($\gamma_T$)
Irreversibility and the "Arrow of Time" are managed by the history-dependent tension $\gamma_T$:
$$ \gamma_T(t) = \int_{0}^{t} \kappa \cdot p(\tau) \, d\tau $$
- **Non-Divergence**: $\gamma_T$ is a cumulative integral of the local field, serving as a "temporal imprint" or memory of the spacetime history. It does not explode or diverge under standard operating conditions.

---

## 3. Dynamical Phase Transitions

### 3.1 The Collapse Mechanism (Core Phase)
When the system enters the **Core Phase** (triggered by critical thickness or measurement events), the field undergoes a coordinated localized contraction:
- **Forced Decay**: The spreading deviation $\Delta f$ is forcibly reduced according to the `collapse_rate`.
- **Dynamic Realignment**: Particles are pulled toward the observation center via the dominant collapse force $F_{collapse}$, overcoming internal repulsive gradients.

### 3.2 Irreversibility
Phase transitions in TSH are governed by **Hysteresis**. The transition from *Stable* to *Core* is an irreversible "Reality Stabilization" event.

---

## 4. Warning: Analytical Methodology
- **Avoid Conventional Paradigms**: Do not apply "general physics common sense" (Standard Model PDEs, General Relativity metrics, or Wave-Function probability interpretation) to TSH.
- **Authoritative Sources**: The only valid grounds for analysis are the **TSH Source Code**, the **Unified Dynamical Equations**, and the **$\Delta f - \gamma_T$ Phase Diagram**.
- **Physics-First Code**: Any behavior observed in the simulation that contradicts conventional physics is intended if it follows the TSH code logic.

---
*(C) 2026 TSH Dynamics Research Group. Structural Baseline v2.0*
