 # Qwen 2.5 / 3 model research 

*Ed Ras - 215279167* 

 

## Introduction to Model:  

**Overview**: The Qwen series of models consists of large language and large multimodal models capable of natural language understanding, text generation, reasoning, vision understanding, audio understanding and tool use. The models are pre-trained on large scale multilingual and multimodal data and post-trained on quality data to align with human preferences. 

The models for consideration are Qwen 2.5-0.5B and the newer Qwen 3-0.6B compact models. The newer Qwen 3 improves with mixture of experts (MoE), advancements in reasoning, and agent capabilities. 

**Developer/Organisation**: Alibaba Group - a Chinese multinational technology company specializing in e-commerce, retail, Internet, and technology 

 

## From the developer: 

---

>**Qwen2.5** is the latest series of Qwen large language models. For Qwen2.5, we release a number of base language models and instruction-tuned language models ranging from 0.5 to 72 billion parameters. Qwen2.5 brings the following improvements upon Qwen2: 

>Significantly more knowledge and has greatly improved capabilities in coding and mathematics, thanks to our specialized expert models in these domains. 

>Significant improvements in instruction following, generating long texts (over 8K tokens), understanding structured data (e.g, tables), and generating structured outputs especially JSON. More resilient to the diversity of system prompts, enhancing role-play implementation and condition-setting for chatbots. 

>Long-context Support up to 128K tokens and can generate up to 8K tokens. 

>Multilingual support for over 29 languages, including Chinese, English, French, Spanish, Portuguese, German, Italian, Russian, Japanese, Korean, Vietnamese, Thai, Arabic, and more. 

 ---

>**Qwen3** is the latest generation of large language models in Qwen series, offering a comprehensive suite of dense and mixture-of-experts (MoE) models. Built upon extensive training, Qwen3 delivers groundbreaking advancements in reasoning, instruction-following, agent capabilities, and multilingual support, with the following key features: 

>Uniquely support of seamless switching between thinking mode (for complex logical reasoning, math, and coding) and non-thinking mode (for efficient, general-purpose dialogue) within single model, ensuring optimal performance across various scenarios. 

>Significantly enhancement in its reasoning capabilities, surpassing previous QwQ (in thinking mode) and Qwen2.5 instruct models (in non-thinking mode) on mathematics, code generation, and commonsense logical reasoning. 

>Superior human preference alignment, excelling in creative writing, role-playing, multi-turn dialogues, and instruction following, to deliver a more natural, engaging, and immersive conversational experience. 

>Expertise in agent capabilities, enabling precise integration with external tools in both thinking and unthinking modes and achieving leading performance among open-source models in complex agent-based tasks. 

>Support of 100+ languages and dialects with strong capabilities for multilingual instruction following and translation. 

 

## Key Features: 

| | Qwen 2.5 - 0.5B |  Qwen 3 – 0.6B |
| --- | --- | --- |
| Model size (parameters) | 0.49B | 0.6B |
| Context window size | 32,768/8192 | 32,768/8192 |
| Architecture type | Causal Language Model (autoregressive/decoder-only) | Causal Language Model (autoregressive/decoder-only) |
| Target use case | Instruct | Instruct, Reasoning, Agent | 
| Training data | Models are pretrained on large scale multilingual and multimodal data and post trained on quality data to align with human preferences. No other details are provided |Models are pretrained on large scale multilingual and multimodal data and post trained on quality data to align with human preferences. No other details are provided. |
| License | Apache 2.0 | Apache 2.0 |
| Links | https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct | https://huggingface.co/Qwen/Qwen3-0.6B |
Additional info: https://qwen.readthedocs.io/en/v2.5/getting_started/concepts.html 

## Compute Requirements: 
| | Qwen 2.5 - 0.5B | Qwen 3 – 0.6B |
| --- | --- | --- | 
| Hardware | NVIDIA A100 80GB | NVIDIA H20 96GB | 
| Memory | 30720 input 2.34GB | 30720 input 4.76GB | 
| Storage | 988MB | 1.6GB | 
| Throughput (tokens per second) | 47.16 | 175.93 | 
| Links | https://qwen.readthedocs.io/en/v2.5/benchmark/speed_benchmark.html | https://qwen.readthedocs.io/en/latest/getting_started/speed_benchmark.html |

 

## Advantages: 
* Can scale up to Qwen model that support up to 1M token context lengths, or other Qwen models with up to 72B parameters 
* Good documentation available from developer 
* Able to deploy model with OpenAI-compatible API endpoint 
* Lots of community support and involvement, eg Nvidia, and Deepseek models based on Qwen eg: https://huggingface.co/models?sort=trending&search=qwen

## Disadvantages: 
* Apache 2.0 license more restrictive than MIT license 
* Context windows may not be sufficient size for AAIE task 
* Qwen 3 0.6B may still be too resource/compute heavy for fine tuning task (dependent on GPU availabilities) 

 