
import torch

def detach_to_cpu(x):
    if torch.is_tensor(x):
        return x.detach().cpu()
    return x

def safe_float(x):
    try:
        return float(x)
    except:
        return 0.0

