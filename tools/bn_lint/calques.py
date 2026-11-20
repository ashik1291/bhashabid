"""Development alias of `bhashabid.lint.calques`."""
import importlib
import sys

sys.modules[__name__] = importlib.import_module("bhashabid.lint.calques")
