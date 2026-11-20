"""Development alias of `bhashabid.creative.audit`."""
import importlib
import sys

sys.modules[__name__] = importlib.import_module("bhashabid.creative.audit")
