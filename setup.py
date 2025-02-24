from setuptools import setup

setup(
    name="gvt",
    use_scm_version={
        "write_to": "src/gvt/_version.py",
        "write_to_template": '__version__ = "{version}"',
    },
    setup_requires=['setuptools_scm'],
    packages=['gvt'],
    package_dir={'': 'src'},
)