from pathlib import Path

import pytest
import torch

from src.datamodule import Cifar10DataModule


@pytest.mark.parametrize("batch_size", [32, 128])
def test_mnist_datamodule(batch_size: int) -> None:
    """Tests `MNISTDataModule` to verify that it can be downloaded correctly, that the necessary
    attributes were created (e.g., the dataloader objects), and that dtypes and batch sizes
    correctly match.

    :param batch_size: Batch size of the data to be loaded by the dataloader.
    """
    data_dir = "data/"

    dm = Cifar10DataModule(data_dir=data_dir, batch_size=batch_size)
    dm.prepare_data()

    assert not dm.trainset and not dm.validset and not dm.testset
    assert Path(data_dir, "cifar-10-batches-py").exists()

    dm.setup()
    assert dm.trainset and dm.validset and dm.testset
    assert dm.train_dataloader() and dm.val_dataloader() and dm.test_dataloader()

    num_datapoints = len(dm.trainset) + len(dm.validset) + len(dm.testset)
    assert num_datapoints == 60_000

    batch = next(iter(dm.train_dataloader()))
    x, y = batch
    assert len(x) == batch_size
    assert len(y) == batch_size
    assert x.dtype == torch.float32
    assert y.dtype == torch.int64
