import os
import glob
from os.path import dirname, basename, isfile

modules = glob.glob(os.path.join(dirname(__file__), "*.py"))
__all__ = [basename(f)[:-3] for f in modules if isfile(f)]
