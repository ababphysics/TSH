from typing import Protocol, Any
from .phase_diagram import phase, Phase


class FourVelocity(Protocol):
    def covariant_derivative(self, x: Any) -> float:
        ...


class ProbabilityField(Protocol):
    def grad_log_p(self, x: Any) -> float:
        ...


class StructureForce(Protocol):
    def value(self, delta_f: float, gamma_T: float) -> float:
        ...


def unified_equation(u: FourVelocity,
                     prob: ProbabilityField,
                     F: StructureForce,
                     delta_f: float,
                     gamma_T: float,
                     x: Any) -> float:
    """
    Du^μ/Dτ = -∇^μ ln p + F^μ(Δf, γT)
    """
    return (
        -prob.grad_log_p(x)
        + F.value(delta_f, gamma_T)
    )
