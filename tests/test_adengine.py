import os
import pytest
import logging
logging.basicConfig(level=logging.DEBUG)

@pytest.mark.parametrize(
    "gather",
    (True, False),
)
@pytest.mark.parametrize("which", ("serial", "multiproc", "concurrent", "dask"))  # , "mpi"),
@pytest.mark.parametrize(
    "batched",
    (True, False),
)
@pytest.mark.parametrize(
    "share",
    (True, False),
)
@pytest.mark.parametrize(
    "generator",
    (True, False),
)
@pytest.mark.parametrize(
    "max_cpu",
    (2, "None", 1),
)
def test_engine(which, gather, batched, share, generator, max_cpu):
    if which != "mpi":
        assert os.system(f"python tests/main.py {which} {gather} {batched} {share} {generator} {max_cpu}") == 0
    else:
        assert (
            os.system(
                f"mpirun $VIRTUAL_ENV/bin/python -m mpi4py.futures tests/main.py"
                f" {which} {gather} {batched} {share} {generator} {max_cpu}"
            )
            == 0
        )
