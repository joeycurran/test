# New Lightning Core Refactor Module

from typing import List
import torch

def l2_norm(t: torch.Tensor) -> float:
    return float(torch.linalg.norm(t, ord=2))

def l1_norm(t: torch.Tensor) -> float:
    return float(torch.linalg.norm(t, ord=1))

def cosine_sim(a: torch.Tensor, b: torch.Tensor) -> float:
    return float(torch.nn.functional.cosine_similarity(a, b, dim=0))

