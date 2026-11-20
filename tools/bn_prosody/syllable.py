"""Development alias of `bhashabid.prosody.syllable`."""
import importlib
import sys

sys.modules[__name__] = importlib.import_module("bhashabid.prosody.syllable")
