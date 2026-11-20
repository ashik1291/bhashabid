"""Development alias of `bhashabid.lint.models`."""
import importlib
import sys

sys.modules[__name__] = importlib.import_module("bhashabid.lint.models")
