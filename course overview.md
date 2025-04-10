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

# Message and Special Tokens:
 Aim to understand how LLMs manage chats.
  Behind the scenes, the messages written to the LLM are concatenated and formatted into a prompt that the model can understand.
  ![image](https://github.com/user-attachments/assets/1990c660-a7a0-4499-843b-7541731a44d5)

  ## Chat templates:
   They act as the bridge between conversational messages (user and assistant turns) and the specific formatting requirements of your chosen LLM.

   ## Messages:

  ### System Messages:
System messages (also called System Prompts) define how the model should behave. They serve as persistent instructions, guiding every subsequent interaction.
   
For example:
system_message = {
    "role": "system",
    "content": "You are a professional customer service agent. Always be polite, clear, and helpful."
}

System Message also gives information about:
   the available tools
   provides instructions to the model on how to format the actions to take
   includes guidelines on how the thought process should be segmented.

### Conversations:
A conversation consists of alternating messages between a Human (user) and an LLM (assistant).

Chat templates help maintain context by preserving conversation history, storing previous exchanges between the user and the assistant. This leads to more coherent multi-turn conversations.

We always concatenate all the messages in the conversation and pass it to the LLM as a single stand-alone sequence. 
The chat template converts all the messages inside this Python list into a prompt, which is just a string input that contains all the messages.

![image](https://github.com/user-attachments/assets/387e5cb8-df53-4fb9-876b-add0a60202db) ![image](https://github.com/user-attachments/assets/cf0a71a6-1032-41e7-afa4-93039fa235ba)

# Base Models vs. Instruct Models
Another point we need to understand is the difference between a Base Model vs. an Instruct Model:

A **Base Model** is trained on raw text data to predict the next token.

An **Instruct Model** is fine-tuned specifically to follow instructions and engage in conversations. For example, SmolLM2-135M is a base model, while SmolLM2-135M-Instruct is its instruction-tuned variant.

To make a Base Model behave like an instruct model, we need to format our prompts in a consistent way that the model can understand. This is where chat templates come in.

# Messages to prompt
The easiest way to ensure your LLM receives a conversation correctly formatted is to use the chat_template from the model’s tokenizer.

To convert the previous conversation into a prompt, we load the tokenizer and call apply_chat_template:
![image](https://github.com/user-attachments/assets/a3256032-5324-4949-bf90-a793934f7a59)


# Tools:
A Tool should contain:
   - A textual description of what the function does.
   - A Callable (something to perform an action).
   - Arguments with typings.
   - (Optional) Outputs with typings.

LLMs, as we saw, can only receive text inputs and generate text outputs. They have no way to call tools on their own. When we talk about providing tools to an Agent, we mean teaching the **LLM** about the existence of these tools and instructing it to **generate text-based invocations** when needed.

The **Agent then reads this response**, identifies that a tool call is required, **executes the tool** on the LLM’s behalf, and retrieves the actual weather data.

**How do we give tools to an LLM?**
The complete answer may seem overwhelming, but we essentially use the system prompt to provide textual descriptions of available tools to the model.
If we want to provide multiple tools, we must be consistent and always use the same format. This process can be fragile, and we might accidentally overlook some details.
There is a better way:

# Auto-formatting Tool sections
Our tool was written in Python, and the implementation already provides everything we need:

A descriptive name of what it does: calculator
A longer description, provided by the function’s docstring comment: Multiply two integers.
The inputs and their type: the function clearly expects two ints.
The type of the output.
There’s a reason people use programming languages: they are expressive, concise, and precise.

We could provide the Python source code as the specification of the tool for the LLM, but the way the tool is implemented does not matter. All that matters is its name, what it does, the inputs it expects and the output it provides.

We will leverage Python’s **introspection** features to leverage the source code and **build a tool description** automatically for us. 

All we need is that the tool implementation uses **type** hints, **docstrings**, and **sensible function names**. We will write some code to extract the relevant portions from the source code.

After we are done, we’ll only need to use a **Python decorator** to indicate that the calculator function is a tool. 
Use the Tool’s to_string method to automatically retrieve a text suitable to be used as a tool description for an LLM.
![image](https://github.com/user-attachments/assets/508c6127-87dc-4ba8-8013-d538430775c5)
![image](https://github.com/user-attachments/assets/31ba2fae-a97c-459e-b8f2-e0d3aca2303b)

The description is injected in the system prompt. Taking the example with which we started this section, here is how it would look like after replacing the tools_description:
![image](https://github.com/user-attachments/assets/df40175c-3712-4ba3-8426-b3258d40b18a)


# Model Context Protocol(MCP): unified tool interface
 - An open protocol that standardizes how tools are provided to LLMs. Features:
      - A growing list of **pre-built integrations** that your LLM can directly plug into
      - The flexibility to **switch between LLM providers** and vendors
      - Best practices for securing your data within your infrastructure
   This means that any framework implementing MCP can leverage tools defined within the protocol, eliminating the need to reimplement the same tool interface for each framework.













