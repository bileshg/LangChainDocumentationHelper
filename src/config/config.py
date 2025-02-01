import os
from omegaconf import OmegaConf


def load_config(file_path: str):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Configuration file not found: {file_path}")
    return OmegaConf.load(file_path)


def get_config_path():
    config_dir = os.path.dirname(os.path.abspath(__file__))
    src_dir = os.path.dirname(config_dir)
    project_dir = os.path.dirname(src_dir)

    return os.path.join(project_dir, "config.yaml")


conf = load_config(get_config_path())
