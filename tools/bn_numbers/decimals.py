"""Development alias of `bhashabid.numbers.decimals`."""
import importlib
import sys

sys.modules[__name__] = importlib.import_module("bhashabid.numbers.decimals")
