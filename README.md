# xAI Grok LangChain Chatbot

## Overview

A chatbot implementation exploring xAI's recently released Grok API through LangChain integration. The project demonstrates how to build a conversational AI assistant using Grok's capabilities, with Seedworld (a metaverse gaming platform) serving as the knowledge domain for testing and demonstration purposes.

## Quick Links

- [xAI Grok Documentation](https://docs.x.ai/docs)

## Technology Stack

- **Backend:**
  - Python
  - LangChain for LLM integration
  - xAI Grok-Beta model for natural language processing
- **Chat Management:**
  - Custom chat history manager for session handling
  - UUID for user session management
- **User Interface:**
  - Streamlit for web interface
  - Custom CSS for styling

## xAI Grok Integration Experience

The integration of xAI's Grok API proved to be straightforward, requiring minimal code modifications from the OpenAI implementation. Key observations:

- **Easy Integration:** LangChain's support for xAI models made the switch from OpenAI simple and efficient
- **Function Calling:** Supports function calling capabilities similar to OpenAI
- **Current Limitations:**
  - Real-time news/events access is currently limited to Grok's chatbot on X
  - Image generation not yet available via API
  - Some advanced features still in development

## Usage

To run the chatbot:
`streamlit run app.py`

## Disclaimer

This is an experimental project exploring the xAI Grok API integration. While the chatbot uses Seedworld's documentation for demonstration purposes, it is not directly affiliated with Seedworld or Seedify. Always refer to the official Seedworld documentation for the most up-to-date and accurate information.
