"""Development alias of `bhashabid.numbers.ordinals`."""
import importlib
import sys

sys.modules[__name__] = importlib.import_module("bhashabid.numbers.ordinals")
