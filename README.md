# AI Code Generator using Transformers

This project is a Streamlit-based web application that generates programming code from natural language descriptions. It uses a pretrained transformer model from Hugging Face to convert user prompts into executable code.

The application allows users to describe a programming problem and select a target language. The AI then generates clean and structured code based on the request.

---

## Project Overview

The application demonstrates how large language models can be used for code generation.

Workflow:

1. User enters a problem description.
2. User selects a programming language.
3. The prompt is formatted with strict instructions.
4. A pretrained code generation model produces the code.
5. The output is displayed in a formatted code block.

The system is powered by the Salesforce CodeGen model.

---

## Features

- Natural language to code generation
- Multi-language support (Python, Java, C++)
- Clean prompt engineering for structured output
- No explanation output (code-only generation)
- Adjustable generation parameters
- Streamlit-based interactive UI
- Cached model loading for performance

---

## Model Used

Model:
Salesforce/codegen-350M-mono

Task:
Text generation

The model is optimized for code generation tasks and supports multiple programming languages.

---

## Technologies Used

- Python
- Streamlit
- Hugging Face Transformers
- PyTorch (backend for Transformers)

---

## Project Structure
