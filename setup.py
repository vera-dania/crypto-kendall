from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='crypto-kendall',  # Required
    version='1.0.0',  # Required
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional
    url='https://github.com/wtaylor17/crypto-kendall',  # Optional
    author='William Taylor-Melanson',  # Optional
    author_email='wtaylor@upei.ca',  # Optional
    packages=find_packages(where='.'),  # Required
    python_requires='>=3.6, <4',
    install_requires=['pymannkendall', 'matplotlib', 'cryptocompare'],  # Optional

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    #
    # For example, the following would provide a command called `sample` which
    # executes the function `main` from this package when invoked:
    entry_points={  # Optional
        'console_scripts': [
            'crypto_kendall=crypto_kendall:main',
        ],
    }
)
