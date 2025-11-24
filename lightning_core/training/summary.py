
import torch
from typing import Any, Dict
from lightning_core.metrics.batch_stats import compute_batch_stats
from lightning_core.metrics.tensor_norms import l2_norm

def training_summary(batch: torch.Tensor) -> Dict[str, Any]:
    stats = compute_batch_stats(batch)
    stats['l2'] = l2_norm(batch)
    return stats

