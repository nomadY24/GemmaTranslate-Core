from setuptools import setup, find_packages

setup(
    name="gemmatranslate-core",
    version="1.0.4",
    author="Gemma-Optimize-Lab",
    description="Optimized inference engine for Gemma-based translation models",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "torch>=2.1.0",
        "transformers>=4.35.0",
        "bitsandbytes>=0.41.0",
        "accelerate>=0.24.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.9",
)
