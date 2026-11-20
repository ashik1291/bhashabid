"""Development alias of `bhashabid.lint.grammar`."""
import importlib
import sys

sys.modules[__name__] = importlib.import_module("bhashabid.lint.grammar")
