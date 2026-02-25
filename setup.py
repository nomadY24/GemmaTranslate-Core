from setuptools import setup, find_packages
import os

setup(
    name='gemmatranslate-core',
    version='0.1.2',
    description='VRAM-optimized and 4-bit quantized inference engine for Google Gemma-based translation models.',
    long_description=open('README.md').read() if os.path.exists('README.md') else '',
    long_description_content_type='text/markdown',
    author='nomadY24',
    url='https://github.com/nomadY24/GemmaTranslate-Core',
    packages=find_packages(),
    install_requires=[
        'torch>=2.0.0',
        'transformers>=4.38.0',
        'bitsandbytes>=0.41.0',
        'accelerate',
        'colorama'
    ],
    entry_points={
        'console_scripts': [
            'gemma-optimize=gemmatranslate_core.main:run_warning',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)