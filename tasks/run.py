from subprocess import run
from invoke import task

from os.path import join

from tasks.util import (
    BUILD_DIR,
)

BIN_DIR = join(BUILD_DIR, "bin")
EXE_BINARY = join(BIN_DIR, "dirty_bench")


@task(default=True)
def execute(ctx, clean=False):
    """
    Run dirty tracking benchmark
    """
    run(
        "sudo {}".format(EXE_BINARY),
        shell=True,
        check=True,
        cwd=BIN_DIR,
    )
