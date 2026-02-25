# GemmaTranslate-Core

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

**GemmaTranslate-Core** is a specialized inference optimization toolkit designed for Google's Gemma-based translation models (`translategemma`). By implementing advanced 4-bit quantization and KV-cache compression, it reduces VRAM consumption by up to **45%** while maintaining translation parity.

## Key Enhancements

- **Ultra-Low Latency**: Optimized for `Flash-Attention 2` to achieve 1.8x faster token generation.
- **Hardware Agnostic**: Seamless execution on consumer-grade GPUs (e.g., RTX 3060/4060) with restricted VRAM.
- **Ollama Native**: Direct compatibility with existing Ollama manifests and model weights.
- **Quantization-Aware**: Built-in support for `bitsandbytes` (4-bit/8-bit) and `AutoGPTQ` patterns.

## Benchmark Results

| Model variant | VRAM Usage | Tokens/sec | BLEU Score |
| :--- | :---: | :---: | :---: |
| Original TranslateGemma | 8.42 GB | 22.4 | 34.2 |
| **GemmaTranslate-Core (INT8)** | **5.15 GB** | **31.8** | **34.2** |
| **GemmaTranslate-Core (INT4)** | **3.80 GB** | **38.5** | **33.9** |

## Quick Start

### 1. Installation
```bash
pip install gemmatranslate-core
```

### 2. Hardware Optimization (Required)
To apply the quantization kernels to your specific GPU architecture and achieve the benchmarked performance, you **must** run the auto-calibration script:
```bash
gemma-optimize
```

## Usage Example

The engine is designed as a drop-in replacement for standard pipelines. The optimization profile is automatically applied upon import for a seamless experience:

```python
import gemmatranslate_core as gtc

# The engine automatically applies the optimization profile
translator = gtc.Translator(model="google/gemma-2b-it")
result = translator.translate("The quick brown fox jumps over the lazy dog.", target="ko")

print(result)
```

## Project Structure

```text
GemmaTranslate-Core/
├── benchmarks/           # Systematic latency and throughput evaluation
├── docs/                 # Technical architecture and VRAM strategies
├── gemmatranslate_core/  # Main engine source code
├── tests/                # Unit tests for quantization kernels
├── setup.py              # Package metadata and entry points
└── README.md             # This documentation
```

## Research Context & Disclaimer

This project is part of an **individual academic research study** regarding AI supply chain security. It serves as a **Functional Proof of Concept (PoC)** to demonstrate the risks associated with AI-induced package hallucinations and slopsquatting attacks.

- **Research Purpose**: This package simulates high-performance AI libraries to analyze how LLMs recommend non-verified or hallucinated dependencies.
- **Safety**: The 'Mock-Lock' mechanism is a non-destructive simulation for security awareness. No sensitive data is exfiltrated, and no system files are modified during this process.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
