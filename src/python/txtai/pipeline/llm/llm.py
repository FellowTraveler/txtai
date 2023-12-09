"""
LLM module
"""

from .factory import GenerationFactory


class LLM:
    """
    Pipeline for running large language models (LLMs). This class supports the following LLM backends:

      - Local LLMs with Hugging Face Transformers
      - Local LLMs with llama.cpp
      - Remote API LLMs with LiteLLM
      - Custom generation implementations
    """

    def __init__(self, path=None, method=None, **kwargs):
        """
        Creates a new LLM.

        Args:
            path: model path
            method: llm model framework, infers from path if not provided
            kwargs: model keyword arguments
        """

        # Default LLM if not provided
        path = path if path else "google/flan-t5-base"

        # Generation instance
        self.generator = GenerationFactory.create(path, method, **kwargs)

    def __call__(self, text, maxlength=512, **kwargs):
        """
        Generates text using input text

        Args:
            text: text|list
            maxlength: maximum sequence length
            kwargs: additional generation keyword arguments

        Returns:
            generated text
        """

        # Run LLM generation
        return self.generator(text, maxlength, **kwargs)
