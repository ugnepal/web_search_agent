import os
import asyncio
import streamlit as st
from openai import AsyncOpenAI
from agents import (
    Agent,
    Runner,
    function_tool,
    ModelSettings,
    OpenAIChatCompletionsModel,
    set_tracing_disabled
)
from duckduckgo_search import DDGS  # Fixed import here


# ----------- TOOL DEFINITION -----------

@function_tool
async def web_search(query: str) -> str:
    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=3))
    if not results:
        return "No relevant results found."
    formatted = "\n\n".join(f"{r['title']}\n{r['href']}" for r in results)
    return f"Top search results:\n\n{formatted}"

# ----------- MODEL & AGENT SETUP -----------

# Set your API key in the environment
token = os.getenv("SECRET")  # Make sure SECRET is set in your environment
endpoint = "https://models.github.ai/inference"  # Replace if using official OpenAI

client = AsyncOpenAI(
    base_url=endpoint,
    api_key=token
)

set_tracing_disabled(True)

model_instance = OpenAIChatCompletionsModel(
    model="openai/gpt-4.1-nano",
    openai_client=client
)

agent = Agent(
    name="WebSearchBot",
    instructions=(
        "You are a helpful assistant. "
        "If you are unsure about something or lack knowledge, use the 'web_search' tool to find the information."
    ),
    model=model_instance,
    model_settings=ModelSettings(temperature=0.2),
    tools=[web_search]
)

# ----------- STREAMLIT UI -----------

st.set_page_config(page_title="Web Search Chatbot", page_icon="🌐")
st.title("🌐 Web Search Chatbot")
st.caption("Ask me anything — I’ll search the web if I don’t know.")

if "history" not in st.session_state:
    st.session_state.history = []

query = st.text_input("Ask your question here:")

if st.button("Send") and query:
    async def get_response():
        result = await Runner.run(agent, query)
        return result.final_output

    with st.spinner("Thinking..."):
        try:
            response = asyncio.run(get_response())
        except Exception as e:
            response = f"Error: {str(e)}"

        st.session_state.history.append((query, response))

# Display conversation history
for user_query, bot_response in reversed(st.session_state.history):
    st.markdown(f"**You:** {user_query}")
    st.markdown(f"**Bot:** {bot_response}")