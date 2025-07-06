# web_search_agent

🌐 Web Search Chatbot
Web Search Chatbot is a Streamlit-powered application that combines a custom AI agent with real-time web search capability via DuckDuckGo. When the AI model doesn’t know the answer, it queries the web to find accurate, up-to-date information — delivering a smart, informed response to your question.

🚀 Features
🔍 Real-time Web Search: Uses DuckDuckGo to retrieve live search results.

🤖 Custom AI Agent: Built on top of OpenAI-compatible chat model (gpt-4.1-nano).

🧠 Tool-Augmented Reasoning: The agent knows when to use its tools (like web_search) to improve responses.

🖥️ Streamlit UI: Interactive and easy-to-use web interface.

💬 Session Memory: Maintains chat history within the session.

🛠️ Tech Stack
Python 3.8+

Streamlit for the frontend

OpenAI-compatible API via openai.AsyncOpenAI

duckduckgo_search for live web search

Custom Agent Framework: Uses Agent, Runner, and function_tool abstractions

📦 Setup Instructions
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/web-search-chatbot.git
cd web-search-chatbot
Create a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Set your API key in environment variables:

bash
Copy
Edit
export SECRET=your_openai_api_key_here
Or on Windows:

c
Copy
Edit
set SECRET=your_openai_api_key_here
Run the app:

bash
Copy
Edit
streamlit run app.py
📂 File Structure
bash
Copy
Edit
.
├── agents/                  # Agent framework (Agent, Runner, tools, etc.)
├── app.py                   # Main application script
├── README.md                # Project documentation
├── requirements.txt         # Required Python packages
🧠 How It Works
The app initializes an Agent with an OpenAI-compatible model.

When a user submits a query:

The agent tries to answer based on its training.

If unsure, it uses the web_search tool to fetch real-time data from DuckDuckGo.

The result is displayed back in the Streamlit UI, along with the previous conversation.

🛡️ Notes
Ensure that your OpenAI-compatible endpoint (https://models.github.ai/inference) is valid. Replace it with the official OpenAI endpoint if needed.

This app disables tracing by default for performance and privacy.