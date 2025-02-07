import torch

# TODO: add your custom model config here:
gpt_configs = {
    "o1-mini": {
        "model": "o1-mini",
        "temperature": 1.0,
        "max_completion_tokens": 59999,
        "top_p": 1.0,
        "frequency_penalty": 0.0,
        "presence_penalty": 0.0,
    },
    "gpt-4o-mini": {
        "model": "gpt-4o-mini",
        "temperature": 0.0,
        "max_tokens": 15999,
        "top_p": 1.0,
        "frequency_penalty": 0.0,
        "presence_penalty": 0.0,
        "stop": None
    },
    "gpt-4o": {
        "model": "gpt-4o-2024-08-06",
        "temperature": 0.0,
        "max_tokens": 15999,
        "top_p": 1.0,
        "frequency_penalty": 0.0,
        "presence_penalty": 0.0,
        "stop": None
    },
    "gpt35-turbo": {
        "model": "gpt-3.5-turbo",
        "temperature": 0.0,
        "max_tokens": 3999,
        "top_p": 1.0,
        "frequency_penalty": 0.0,
        "presence_penalty": 0.0,
        "stop": None
    }
}

llama_configs = {
    "meta-llama/Llama-2-7b-chat-hf": {
        "task": "text-generation",
        "model": "meta-llama/Llama-2-7b-chat-hf",
        "torch_dtype": torch.float16,
        "device_map": "auto",
        "do_sample":False,
    },
    "meta-llama/Llama-2-13b-chat-hf": {
        "task": "text-generation",
        "model": "meta-llama/Llama-2-13b-chat-hf",
        "torch_dtype": torch.float16,
        "device_map": "auto",
        "do_sample":False,
    }
}

default_llama_config = {
    "task": "text-generation",
    "model": None,
    "torch_dtype": torch.float16,
    "device_map": "auto",
    "do_sample":False,
}

default_gpt_config = {
    "model": None,
    "temperature": 0.0,
    "max_tokens": 5000,
    "top_p": 1.0,
    "frequency_penalty": 0.0,
    "presence_penalty": 0.0,
    "stop": None
}