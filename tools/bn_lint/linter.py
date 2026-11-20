"""Development alias of `bhashabid.lint.linter`."""
import importlib
import sys

sys.modules[__name__] = importlib.import_module("bhashabid.lint.linter")
