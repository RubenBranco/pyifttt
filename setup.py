from setuptools import setup, find_packages
from os import path
import re


def packagefile(*relpath):
    return path.join(path.dirname(__file__), *relpath)


def read(*relpath):
    with open(packagefile(*relpath)) as f:
        return f.read()


def get_version(*relpath):
    match = re.search(
        r'''^__version__ = ['"]([^'"]*)['"]''',
        read(*relpath),
        re.M
    )
    if not match:
        raise RuntimeError('Unable to find version string.')
    return match.group(1)


setup(
    name='pyifttt',
    version=get_version('src', 'pyifttt', "__init__.py"),
    description='Python Wrapper for IFTTT Webhook interaction.',
    long_description=read('README.rst'),
    url='https://github.com/RubenBranco/pyifttt',
    author='Ruben Branco',
    author_email='ruben.branco@outlook.pt',
    license='GPLv3',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
    ],
    keywords='ifttt, webhook',
    install_requires=[
        'requests',
    ],
    package_dir={'': 'src'},
    packages=find_packages('src'),
)