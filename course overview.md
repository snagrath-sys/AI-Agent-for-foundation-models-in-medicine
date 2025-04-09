# Introduction

## AI Agent
An **AI agent** is an AI model capable of reasoning, planning, and interacting with its environment.

## Components of an Agent

1. **Brain (AI Model)**  
   This is where the reasoning and planning takes place. It decides what actions to take based on the situation.

2. **Body (Capabilities and Tools)**  
   The design of the tools is very important and has a great impact on the quality of your agent.

## Spectrum of Agency

![image](https://github.com/user-attachments/assets/3a10cc02-12d7-4f05-9fc2-8341312c2df3)

# LLM

Each agent needs an AI model at its core, and **LLMs (Large Language Models)** are the most common type of AI models for this purpose.

An LLM is a type of AI model that excels at understanding and generating human language.

Most LLMs nowadays are built on the **Transformer architecture** — a deep learning architecture based on the “Attention” algorithm, which gained significant interest after the release of **BERT** from Google in 2018.

## Types of Transformers

### 1. Encoder-based Transformers

An encoder-based Transformer takes text (or other data) as input and outputs a dense representation (or embedding) of that text.

- **Example:** BERT (Google)  
- **Use Cases:** Text classification, semantic search, Named Entity Recognition  
- **Typical Size:** Millions of parameters  

### 2. Decoder-based Transformers

A decoder-based Transformer focuses on generating new tokens to complete a sequence, one token at a time.

- **Example:** LLaMA (Meta)  
- **Use Cases:** Text generation, chatbots, code generation  
- **Typical Size:** Billions of parameters  

### 3. Sequence-to-Sequence (Encoder–Decoder) Transformers

A sequence-to-sequence Transformer combines an encoder and a decoder. The encoder processes the input sequence into a context representation, and the decoder generates an output sequence.

- **Examples:** T5, BART  
- **Use Cases:** Translation, summarization, paraphrasing  
- **Typical Size:** Millions of parameters

The underlying principle of an LLM is simple yet highly effective: its objective is to predict the next token, given a sequence of previous tokens. A “token” is the unit of information an LLM works with. You can think of a “token” as if it was a “word”, but for efficiency reasons LLMs don’t use whole words.

LLMs are said to be autoregressive, meaning that the output from one pass becomes the input for the next one. This loop continues until the model predicts the next token to be the EOS token, at which point the model can stop.







