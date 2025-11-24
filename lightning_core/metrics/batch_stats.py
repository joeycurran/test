# New Lightning Core Refactor Module

from typing import Any, Dict, List
import torch

def compute_batch_stats(batch: torch.Tensor) -> Dict[str, float]:
    mean = batch.mean().item()
    std = batch.std().item()
    max_v = batch.max().item()
    min_v = batch.min().item()
    return {
        'mean': mean,
        'std': std,
        'max': max_v,
        'min': min_v
    }

