"""Development alias of `bhashabid.prosody.metre`."""
import importlib
import sys

sys.modules[__name__] = importlib.import_module("bhashabid.prosody.metre")
