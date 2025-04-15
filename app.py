import streamlit_ui as ui
import smol_agent

def main():
    # Setup UI
    ui.setup_page()
    ui.load_css()
    ui.display_header()
    ui.init_session_state()
    
    # Initialize agent if needed
    if 'agent' not in ui.st.session_state:
        ui.st.session_state.agent = smol_agent.initialize_agent(
            hf_token=ui.st.secrets["HF_TOKEN"]
        )
    
    # Display chat history
    ui.display_chat_history()
    
    # Get user input
    if prompt := ui.get_user_input():
        # Add user message to chat history
        ui.update_chat_history("user", prompt)
        ui.display_user_message(prompt)
        
        # Format conversation history
        conversation = smol_agent.format_conversation_history(
            ui.st.session_state.messages
        )
        
        # Get agent response
        response = smol_agent.process_message(
            ui.st.session_state.agent,
            prompt,
            conversation
        )
        
        # Add and display assistant response
        ui.update_chat_history("assistant", response)
        ui.display_assistant_response(response)

if __name__ == "__main__":
    main()
