# TSH (Thickness Structure Hypothesis)

**Author:** Hirokazu Abe (2026)

## 1. Overview

This repository provides the official computational model and reference materials for the Thickness Structure Hypothesis (TSH), a structural framework that unifies quantum, classical, and gravitational behavior within a single minimal covariant action.

TSH provides a structural unification of the major physical frameworks: it reproduces the geodesic equation of general relativity in the Core phase, the Bohm‑type quantum force in the Stable phase, and the classical limit of quantum mechanics in the Composite phase.

The Δf–γT phase structure resolves long‑standing inconsistencies across these theories—such as the measurement problem, the tension between quantum nonlocality and relativistic locality, and the lack of a continuous bridge between quantum, classical, and gravitational behavior.

Because the structural tensor equation Eμν = Gμν + Uμν accepts arbitrary interaction tensors, TSH incorporates the Standard Model and potential GUT sectors without modifying the structural dynamics.

TSH treats these three regimes as distinct structural phases—Stable, Composite, and Core—of one underlying system.
The framework is self‑contained and derives all regimes from the same structural principles.

The tsh_core/ module provides a runnable simulation of the unified dynamical equation, allowing numerical evolution of the internal variables p(x),Δf,γT across the Δf–γT phase diagram.

## 2. Internal Variables and Phase Structure

TSH introduces three internal quantities that characterize physical existence:

- **p(x):** existence thickness, providing a unified basis for quantum spreading and gravitational localization  
- **Δf:** structural deviation in the spreading direction, governing interference, nonlocality, and entanglement  
- **γT:** structural tension in the contracting direction, governing phase transitions, irreversibility, and wave‑packet collapse  

These variables span the Δf–γT phase diagram, which contains three regimes:

- Stable (quantum)  
- Composite (classical)  
- Core (gravitational / measurement)  

The differences among quantum, classical, and gravitational behavior arise from the relative balance among these three quantities.

## 3. Phase Diagram and Dynamic Feedback

The Δf–γT phase diagram functions both as a classification tool and as a dynamical map.

The structural force is defined by:

Fμ = −∇μ Φ_struct(Δf, γT)



TSH dynamics form a closed feedback loop:

phase → structural force → motion → update of (p, Δf, γT) → phase



This mechanism continuously connects the quantum, classical, and gravitational regimes.

## 4. Minimal Covariant Action

The minimal covariant action consists of four components:

1. the curvature term of general relativity  
2. an entropy‑like term p ln p  
3. a quantum gradient term (∇ ln p)²  
4. the structural potential Φ_struct(Δf, γT)  

Variation of this action yields a unified dynamical equation in which geometric, quantum, and structural contributions appear in a cleanly separated form.

## 5. Unified Dynamical Equation

Duμ / Dτ = −∇μ ln p + Fμ(Δf, γT)



This single equation reproduces:

- quantum behavior in the Stable phase  
- classical trajectories in the Composite phase  
- the geodesic equation of general relativity in the Core phase  

The transitions among these regimes occur continuously through changes in the internal structural variables.

## 6. Limiting Regimes

### Quantum limit (Stable)
The gradient term −∇ln p dominates, reproducing a Bohm‑type quantum force.

### Classical limit (Composite)
Both the gradient and structural force are small, yielding deterministic trajectories.

### Gravitational limit (Core)
As Φ → 0, the unified equation reduces exactly to the geodesic equation of general relativity.

## 7. Phase‑Diagram Compression

The Δf–γT phase diagram compresses the following structural hierarchy into a single representation:

- phase structure  
- structural potential  
- structural force  
- unified dynamical equation  
- tensor equation  
- hierarchical interaction slot  

The position on the phase diagram directly determines the structural force and therefore the system’s dynamics.

## 8. Hierarchical Interaction Slot

The TSH tensor equation:

Eμν = Gμν + Uμν



depends only on the internal variables **p, Δf, γT**.

Because external gauge and matter fields do not appear in the structural action, arbitrary interaction energy‑momentum tensors can be added to the right‑hand side without modifying the structural dynamics.

This includes:

- Standard Model fields  
- GUT fields  
- effective string‑theoretic sectors  
- fluid or condensed‑matter tensors  

The classical limit reproduces GR + SM without requiring reconstruction of the interaction sectors.

## 9. Repository Structure

code/
tsh_core/
phase_diagram.py
action.py
unified_equation.py
init.py

scripts/
extract_text.py
generate_qa_dataset.py

data/
Thickness Structure Hypothesis.html
Figure_1.png
Thickness Structure Hypothesis.pdf

rag_chatbot.py
requirements.txt



## 10. Usage

### Extract text from the paper

python scripts/extract_text.py



### Run the TSH RAG chatbot

python rag_chatbot.py



### Generate the AI training dataset

python scripts/generate_qa_dataset.py



## 11. License

All code and scripts in this repository are released under the MIT License.  
The code may be used, modified, and redistributed with attribution.

The *Thickness Structure Hypothesis* paper (PDF and HTML) in the `data/` directory, as well as the figures (e.g., `Figure_1.png`) and theoretical content in this README, are © 2026 Hirokazu Abe.  
These materials are **not** covered by the MIT License.  
Unauthorized redistribution is prohibited.

## 12. Citation

Hirokazu Abe (2026).  
*Thickness Structure Hypothesis.*  
Zenodo DOI: **10.5281/zenodo.19564362**
