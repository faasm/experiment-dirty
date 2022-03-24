from subprocess import run
from invoke import task

from os import makedirs
from os.path import exists
from shutil import rmtree

from tasks.util import (
    PROJ_ROOT,
    BUILD_DIR,
)


@task(default=True)
def build(ctx, clean=False, debug=False):
    """
    Compile dirty tracking benchmark
    """
    if clean and exists(BUILD_DIR):
        rmtree(BUILD_DIR)

    makedirs(BUILD_DIR, exist_ok=True)

    cmd = [
        "cmake",
        "-GNinja",
        "-DCMAKE_BUILD_TYPE={}".format("Debug" if debug else "Release"),
        "-DBUILD_SHARED_LIBS=OFF",
        "-DCMAKE_CXX_COMPILER=/usr/bin/clang++-13",
        "-DCMAKE_C_COMPILER=/usr/bin/clang-13",
        PROJ_ROOT,
    ]

    run(
        " ".join(cmd),
        shell=True,
        check=True,
        cwd=BUILD_DIR,
    )

    run(
        "cmake --build . --target dirty_bench",
        shell=True,
        check=True,
        cwd=BUILD_DIR,
    )
