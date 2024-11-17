from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from chat_history import chat_history_manager
from dotenv import load_dotenv
import streamlit as st
import uuid
from css.custom_css import inject_custom_css
from langchain_xai import ChatXAI
from prompts import PROMPTS_VERSION_ONE, PROMPTS_VERSION_TWO


load_dotenv()


inject_custom_css()

# Initialize session ID if not present
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# Initialize chat model
if "chat_model" not in st.session_state:
    st.session_state.chat_model = ChatXAI(
        temperature=0.7,
        model_name="grok-beta"     #"gpt-3.5-turbo"
    )

# Get chat history for current session
chat_history = chat_history_manager.get_history_by_session_id(st.session_state.session_id)

# Initialize system message if history is empty
if not chat_history.messages:
    system_msg = PROMPTS_VERSION_ONE
    chat_history.add_message(SystemMessage(content=system_msg))

# Page config
st.title("🎮 Seedbot")
st.markdown("🌐 Unofficial Seedworld support assistant built on the top of Seedworld's whitepaper, may not be 100% accurate. Explore Seedworld, one question at a time 🌱")

# Display chat messages (excluding system message)
for message in chat_history.messages[1:]:  # Skip system message
    role = "assistant" if isinstance(message, AIMessage) else "user"
    with st.chat_message(role):
        if role == "assistant":
            st.markdown(f"🌱 Seedbot: {message.content}")
        else:
            st.markdown(message.content)

# Chat input
if prompt := st.chat_input("Plant your idea here..."):
    # Add user message
    user_message = HumanMessage(content=prompt)
    chat_history.add_message(user_message)

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.chat_model.invoke(
                chat_history.messages
            )
            st.markdown(f"🌱 Seedbot: {response.content}")
            chat_history.add_message(response)
            print(chat_history_manager.chat_histories)

# Sidebar settings
with st.sidebar:
    st.title("🌿 Seedbot Settings")
    
    # Add brief description and links
    st.markdown("Seedworld: Immersive AAA metaverse where UGC gaming meets web3 and real-world economies, built by Seedify")
    st.markdown("[X (Twitter)](https://x.com/SeedworldMeta)")
    st.markdown("[Whitepaper](https://seedworld.gitbook.io/seedworld-wp)")
    
    # Display agent configuration
    st.subheader("🤖 Assistant Configuration")
    first_sentence = """I am Seedbot, your unofficial Seedworld support assistant. I can answer any questions you have about Seedworld's economy, gameplay, NFTs, nodes, tokens, land ownership, staking, and more, using detailed information from the Seedworld whitepaper."""
    st.write(f"📝 About me: {first_sentence}")
    st.write(f"🌡️ Temperature: {st.session_state.chat_model.temperature}")
    st.write(f"🧠 Model: {st.session_state.chat_model.model_name}")
    st.write("⚠️ Disclaimer: Responses may not be 100% accurate.")
    
    # Temperature control
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7)
    if temperature != st.session_state.chat_model.temperature:
        st.session_state.chat_model.temperature = temperature
    
    # Clear chat button
    if st.button("Clear Chat History"):
        chat_history.clear()
        system_msg = PROMPTS_VERSION_ONE
        chat_history.add_message(SystemMessage(content=system_msg))
        st.rerun()

# Add footer
st.markdown("---")