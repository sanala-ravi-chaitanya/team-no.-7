"""
Kisan Call Centre Query Assistant
A Streamlit application that combines local agricultural knowledge with Groq AI (Llama 3.3)
"""
import streamlit as st
from groq import Groq
import sys

# Import configuration and semantic query engine
try:
    from config import Config
    from semantic_query import SemanticQuery
except ImportError as e:
    st.error(f"Error: Could not import required modules. Make sure all files are in the same folder. Details: {e}")
    st.stop()

# Configure Streamlit page
st.set_page_config(
    page_title=Config.PAGE_TITLE,
    page_icon="🌾",
    layout="centered"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #2E7D32;
        text-align: center;
        margin-bottom: 1rem;
    }
    .info-box {
        background-color: #E8F5E9;
        color: #1B5E20;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border-left: 4px solid #4CAF50;
        margin: 1rem 0;
        font-size: 1rem;
        line-height: 1.6;
    }
    .info-box p {
        color: #1B5E20 !important;
        margin: 0.5rem 0;
    }
    .result-card {
        background-color: #F5F5F5;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown(f'<div class="main-header">{Config.APP_TITLE}</div>', unsafe_allow_html=True)

# Sidebar with information
with st.sidebar:
    st.header("ℹ️ About")
    st.write("This assistant helps farmers with agricultural queries using:")
    st.write("- 📚 Local knowledge base")
    st.write("- 🤖 Groq AI (Llama 3.3)")
    
    st.divider()
    
    st.header("💡 Example Queries")
    st.write("- How to improve soil fertility?")
    st.write("- Best fertilizer for rice?")
    st.write("- When to plant wheat?")
    st.write("- How to control pests?")
    
    st.divider()
    
    st.caption(f"🤖 Model: {Config.GROQ_MODEL}")

# Validate configuration
is_valid, message = Config.validate()
if not is_valid:
    st.error(f"⚠️ Configuration Error: {message}")
    st.info("""
    **Setup Instructions:**
    1. Copy `.env.example` to `.env`
    2. Get your API key from https://console.groq.com/
    3. Add your API key to the `.env` file
    4. Restart the application
    """)
    st.stop()

# Initialize the semantic query engine
@st.cache_resource
def get_query_engine():
    return SemanticQuery()

query_engine = get_query_engine()

# Main input
query_input = st.text_input(
    "✏️ Enter your agricultural query:",
    placeholder="e.g., How to increase crop yield?",
    help="Ask any question related to farming, crops, or agriculture"
)

# Process query when button is clicked
if st.button("🔍 Get Answer", type="primary", use_container_width=True):
    if not query_input.strip():
        st.warning("⚠️ Please enter a query.")
    else:
        # --- 1. Offline Retrieval (KCC Data) ---
        st.subheader("📚 Retrieved Knowledge Base Records")
        
        with st.spinner("Searching local database..."):
            offline_results = query_engine.search(query_input)
        
        context_text = ""
        if not offline_results:
            st.info("No matching local records found. Consulting AI expert...")
            context_text = "No local context available."
        else:
            for i, item in enumerate(offline_results):
                with st.expander(f"📌 Result {i+1}: {item['question']} (Relevance: {item['relevance']:.2f})"):
                    st.write(f"**Answer:** {item['answer']}")
                context_text += f"Q: {item['question']}\nA: {item['answer']}\n\n"
        
        st.divider()
        
        # --- 2. Online Answer (Groq AI) ---
        st.subheader("🤖 AI Expert Analysis")
        
        with st.spinner("Consulting Groq AI (Llama 3.3)..."):
            try:
                # Initialize Groq client
                client = Groq(api_key=Config.GROQ_API_KEY)
                
                # Create the prompt
                prompt = f"""You are an expert agricultural advisor helping farmers. Based on the following context from our knowledge base and the user's question, provide a comprehensive, practical answer.

Context from Knowledge Base:
{context_text}

User Question: {query_input}

Please provide:
1. A clear, actionable answer
2. Practical recommendations
3. Any important warnings or considerations

Keep your response concise but informative, suitable for farmers."""

                # Call Groq API
                response = client.chat.completions.create(
                    model=Config.GROQ_MODEL,
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    max_tokens=Config.MAX_TOKENS,
                    temperature=Config.TEMPERATURE
                )
                
                # Display the response
                answer = response.choices[0].message.content
                st.markdown(f'<div class="info-box">{answer}</div>', unsafe_allow_html=True)
                
                # Show usage statistics
                with st.expander("📊 API Usage Statistics"):
                    st.write(f"**Prompt tokens:** {response.usage.prompt_tokens}")
                    st.write(f"**Completion tokens:** {response.usage.completion_tokens}")
                    st.write(f"**Total tokens:** {response.usage.total_tokens}")
                    st.write(f"**Model:** {Config.GROQ_MODEL}")
                
            except Exception as e:
                st.error(f"❌ Groq API Error: {str(e)}")
                st.info("""
                **Troubleshooting:**
                - Verify your API key is correct in the `.env` file
                - Check your internet connection
                - Ensure you have API credits available
                - Visit https://console.groq.com/ to check your account
                """)

# Footer
st.divider()
st.caption("🌾 Kisan Call Centre Assistant | Powered by Groq AI (Llama 3.3)")
