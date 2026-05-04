from enum import Enum
import math

class Phase(Enum):
    STABLE = "Stable"
    COMPOSITE = "Composite"
    CORE = "Core"

def f_crit(gamma_T: float) -> float:
    return 0.12 + 0.08 * math.tanh(2.0 * gamma_T)

def f_core(gamma_T: float) -> float:
    return 0.25 + 0.10 * math.tanh(1.5 * gamma_T)

def phase(delta_f: float, gamma_T: float) -> Phase:
    fc = f_crit(gamma_T)
    fo = f_core(gamma_T)

    if delta_f < fc:
        return Phase.STABLE
    elif delta_f < fo:
        return Phase.COMPOSITE
    else:
        return Phase.CORE

# -------------------------
# 実行部分
# -------------------------
if __name__ == "__main__":
    delta_f = 0.15
    gamma_T = 0.5
    result = phase(delta_f, gamma_T)
    print("Phase:", result.value)
