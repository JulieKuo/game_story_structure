import numpy as np
import os
import random
import shutil
import torch
import yaml

from transformers import TrainingArguments


def set_seed(seed: int) -> None:
    """
    Set seed for reproducibility of model training

    Parameters
    ----------
    seed : int
        Seed value for random number generators
    """
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
1
def load_config(config_path: str) -> dict:
    """
    Load configuration file

    Parameters
    ----------
    config_path : str
        Path to configuration file
    """
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def remove_directory(path: str) -> None:
    """
    Remove directory

    Parameters
    ----------
    path : str
        Path to directory to remove
    """
    try:
        if os.path.exists(path):
            shutil.rmtree(path)
        else:
            print(f"Path {path} does not exist.")
    except Exception as e:
        print(f"Error removing directory: {e}")

def check_device(model: object, train_args: TrainingArguments = None) -> dict:
    """
    Check if model is using GPU

    Parameters
    ----------
    model : object
        Model object from Hugging Face Transformers library
    train_args : TrainingArguments, optional
        Training arguments object, by default None
    
    Returns
    -------
    gpu_dict : dict
        Dictionary containing GPU information
    """
    gpu_dict = {}

    use_device = next(model.parameters()).device
    gpu_dict['device_idx'] = use_device.index if use_device.type == 'cuda' else -1
    
    if train_args is not None:
        gpu_dict['model_gpu_idx'] = train_args.device
    
    return gpu_dict
