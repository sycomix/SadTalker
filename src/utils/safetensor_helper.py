

def load_x_from_safetensor(checkpoint, key):
    return {k.replace(f'{key}.', ''): v for k, v in checkpoint.items() if key in k}