import math
from dataclasses import dataclass
from typing import Protocol, Any


class Metric(Protocol):
    def curvature_scalar(self) -> float:
        ...


class ProbabilityField(Protocol):
    def value(self, x: Any) -> float:
        ...

    def grad_norm_sq(self, x: Any) -> float:
        ...


class StructurePotential(Protocol):
    def value(self, x: Any) -> float:
        ...


@dataclass
class ActionParams:
    k_gr: float
    k_entropy: float
    k_quantum: float
    k_struct: float


class TSHAction:
    """
    S = k_gr * S_GR
      + k_entropy * p ln p
      + k_quantum * |∇p|^2 / p
      + k_struct * Φ_struct
    """

    def __init__(self, metric, prob, struct, params: ActionParams):
        self.metric = metric
        self.prob = prob
        self.struct = struct
        self.params = params

    def S_gr(self) -> float:
        return self.metric.curvature_scalar()

    def S_entropy(self, x: Any) -> float:
        p = self.prob.value(x)
        if p <= 0:
            return 0.0
        return p * math.log(p)

    def S_quantum(self, x: Any) -> float:
        return self.prob.grad_norm_sq(x)

    def S_struct(self, x: Any) -> float:
        return self.struct.value(x)

    def density(self, x: Any) -> float:
        return (
            self.params.k_gr * self.S_gr()
            + self.params.k_entropy * self.S_entropy(x)
            + self.params.k_quantum * self.S_quantum(x)
            + self.params.k_struct * self.S_struct(x)
        )
