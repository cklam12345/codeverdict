# setup.py
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read().splitlines()

setup(
    name="codeverdict",
    version="1.0.0",
    author="CodeVerdict Team",
    author_email="team@codeverdict.ai",
    description="⚖️ Where AI Code Stands Trial - Comprehensive AI Code Evaluation Platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/codeverdict/codeverdict",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Testing",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "codeverdict=codeverdict.api.main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "codeverdict": ["py.typed", "*.md", "config/*.yml", "config/*.yaml"],
    },
)