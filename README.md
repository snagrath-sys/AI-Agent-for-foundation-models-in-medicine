# Medical AI Assistant

A medical AI system using SmoLAGent and clinical LLMs for patient prognosis analysis.

## Features

- SmoLAGent integration for advanced reasoning
- Clinical LLM implementation
- Medical database integration
- Patient parameter processing
- Prognosis analysis engine
- HIPAA compliance and medical data privacy

## Setup

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Create a `.streamlit/secrets.toml` file with your HuggingFace API token:
```toml
HF_TOKEN = "your-token-here"
```

## Running the Application

```bash
python -m streamlit run app.py
```

## Project Structure

- `app.py` - Main Streamlit application
- `smol_agent.py` - SmoLAGent initialization and message processing
- `streamlit_ui.py` - UI components and layout
- `tools/` - Custom tools for the agent
  - `math_tools.py` - Mathematical operations tools
  - More tools coming soon...

## Security and Privacy

This application is designed with medical data privacy in mind. However, this is a demo version - do not use real patient data.
