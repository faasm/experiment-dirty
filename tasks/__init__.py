from invoke import Collection

from . import build
from . import run

import logging

logging.getLogger().setLevel(logging.DEBUG)

ns = Collection(build, run)
