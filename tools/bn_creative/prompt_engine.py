"""Development alias of `bhashabid.creative.prompt_engine`."""
import importlib
import sys

sys.modules[__name__] = importlib.import_module("bhashabid.creative.prompt_engine")
