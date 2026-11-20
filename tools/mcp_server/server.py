"""Development alias of `bhashabid.mcp.server`."""
import importlib
import sys

sys.modules[__name__] = importlib.import_module("bhashabid.mcp.server")
