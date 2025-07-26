# TokStack

__TokStack__ is a Python library created by Patrick Ghetea to simplify building complex nested structures without requiring indentation, making coding feel more like writing text. TokStack is an eDSL fully supported by the Python compiler and syntax, allowing coding without explicit syntax. The phrase-like architecture of the eDSL makes coding much more enjoyable and straightforward while remaining powerful in its primary domain of building deterministic context-aware AI assistants.

__TockStack__ versions:
__alpha__ - A _single-stack_ eDSL supporting all the main functions. The main idea is to present the structure and concept and identify any bugs in the core structure.
__beta__ - Multi-stack support using the __Thread Manager__, which handles threading to ensure _thread-safe_ projects. Developers won't need to write thread-related code, simplifying development for complex projects. This version allows testing and ensures that the eDSL is stable.
__v1.0__ - A _stable version_ supporting multi-stack and other functions, considered __production-ready__.
