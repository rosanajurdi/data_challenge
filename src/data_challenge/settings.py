"""Project settings for data_challenge Kedro project."""

from kedro.config import OmegaConfigLoader

# Instantiate and configure OmegaConfigLoader
CONFIG_LOADER_CLASS = OmegaConfigLoader
CONFIG_LOADER_ARGS = {
    "base_env": "base",
    "default_run_env": "local",
}
