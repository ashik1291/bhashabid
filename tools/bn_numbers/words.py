"""Development alias of `bhashabid.numbers.words`."""
import importlib
import sys

sys.modules[__name__] = importlib.import_module("bhashabid.numbers.words")
