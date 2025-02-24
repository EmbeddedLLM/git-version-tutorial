from setuptools import setup

setup(
    name="gvt",
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    packages=['gvt'],
    package_dir={'': 'src'},
)