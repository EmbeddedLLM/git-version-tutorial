try:
    from ._version import __version__
except ImportError:
    import warnings
    warnings.warn('No version number found for the package')
    __version__ = '0.0.0'