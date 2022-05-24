import os
import pytest


@pytest.mark.parametrize(
    "gather",
    (True, False),
)
@pytest.mark.parametrize(
    "which",
    ("serial", "multiproc", "concurrent", "dask", "mpi"),
)
@pytest.mark.parametrize(
    "batched",
    (True, False),
)
@pytest.mark.parametrize(
    "share",
    (True, False),
)
def test_engine(which, gather, batched, share):
    assert os.system(f"python tests/main.py {which} {gather} {batched} {share}") == 0
