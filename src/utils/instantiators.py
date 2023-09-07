from typing import List

import hydra
from lightning import Callback
from lightning.pytorch.loggers import Logger
from omegaconf import DictConfig

from . import pylogger


log = pylogger.get_pylogger(__name__)


def instantiate_callbacks(callback_configs: DictConfig) -> list[Callback]:
    """Instantiates callbacks from config."""
    callbacks: list[Callback] = []

    if not callback_configs:
        log.warning("No callback configs found! Skipping..")
        return callbacks

    if not isinstance(callback_configs, DictConfig):
        raise TypeError("Callbacks config must be a DictConfig!")

    for _, cb_conf in callback_configs.items():
        if isinstance(cb_conf, DictConfig) and "_target_" in cb_conf:
            log.info(f"Instantiating callback <{cb_conf._target_}>")
            callbacks.append(hydra.utils.instantiate(cb_conf))

    return callbacks


def instantiate_loggers(logger_configs: DictConfig) -> list[Logger]:
    """Instantiates loggers from config."""
    loggers: list[Logger] = []

    if not logger_configs:
        log.warning("No logger configs found! Skipping...")
        return loggers

    if not isinstance(logger_configs, DictConfig):
        raise TypeError("Logger config must be a DictConfig!")

    for _, lg_conf in logger_configs.items():
        if isinstance(lg_conf, DictConfig) and "_target_" in lg_conf:
            log.info(f"Instantiating logger <{lg_conf._target_}>")
            loggers.append(hydra.utils.instantiate(lg_conf))

    return loggers
