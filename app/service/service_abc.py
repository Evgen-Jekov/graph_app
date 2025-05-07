from abc import ABC, abstractmethod
import numpy as np

mat_evel = []

SAFE_FUNCS = {
    "sin": np.sin,
    "cos": np.cos,
    "tan": np.tan,
    "arcsin": np.arcsin,
    "arccos": np.arccos,
    "arctan": np.arctan,
    "exp": np.exp,
    "log": np.log,
    "log10": np.log10,
    "sqrt": np.sqrt,
    "abs": np.abs,
    "floor": np.floor,
    "ceil": np.ceil,
    "round": np.round,
    "maximum": np.maximum,
    "minimum": np.minimum,
    "where": np.where,
    "clip": np.clip,
    "pi": np.pi,
    "e": np.e,
}

class WorkGraphBase(ABC):
    @abstractmethod
    def add_graph(self):
        pass