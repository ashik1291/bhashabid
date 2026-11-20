"""Development alias of `bhashabid.prosody` (single source of truth lives in the package)."""
import importlib

_impl = importlib.import_module("bhashabid.prosody")

globals().update({k: v for k, v in vars(_impl).items() if not k.startswith("__")})
__all__ = getattr(_impl, "__all__", [k for k in vars(_impl) if not k.startswith("_")])
