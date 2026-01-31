# 🌾 Kisan Call Centre Query Assistant

A Streamlit-based agricultural query assistant that combines local knowledge base search with Groq AI (Llama 3.3 70B) to provide comprehensive answers to farming questions.

## Features

- 📚 **Local Knowledge Base**: Fuzzy search through curated agricultural Q&A
- 🤖 **Groq AI Integration**: Advanced AI-powered responses using Llama 3.3 70B Versatile
- 🔒 **Secure Configuration**: API keys managed via environment variables
- 🎯 **Relevance Scoring**: Smart matching algorithm to find the most relevant answers
- 💡 **User-Friendly Interface**: Clean, intuitive Streamlit interface

## Prerequisites

- Python 3.8 or higher
- Groq API key (free!)

## Getting Your Groq API Key

1. Visit [console.groq.com](https://console.groq.com/)
2. Sign up or log in to your account
3. Navigate to "API Keys" section
4. Click "Create API Key" and copy your key
5. **Note**: Groq provides free API access with generous rate limits!

## Installation

1. **Clone or download this repository**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**:
   - Copy `.env.example` to `.env`:
     ```bash
     copy .env.example .env
     ```
   - Open `.env` and replace `your-groq-api-key-here` with your actual Groq API key:
     ```
     GROQ_API_KEY=gsk_your-actual-key-here
     ```

## Usage

1. **Run the application**:
   ```bash
   streamlit run app.py
   ```

2. **Access the interface**:
   - The app will open in your default browser
   - If not, navigate to `http://localhost:8501`

3. **Ask questions**:
   - Enter your agricultural query in the text input
   - Click "Get Answer" to receive results from both the local knowledge base and Groq AI

## Example Queries

- How to improve soil fertility?
- Best fertilizer for rice?
- When to plant wheat?
- How to control pests in cotton?
- What is drip irrigation?
- How to increase crop yield?

## Project Structure

```
kisan-call-centre/
├── app.py                 # Main Streamlit application
├── semantic_query.py      # Enhanced search engine with fuzzy matching
├── config.py              # Configuration management
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variable template
├── .env                  # Your actual API keys (not in git)
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## Configuration

The application uses the following configuration (in `config.py`):

- **Model**: Llama 3.3 70B Versatile (via Groq)
- **Max Tokens**: 1024
- **Temperature**: 0.7 (balanced creativity)

You can modify these settings in `config.py` if needed.

## Troubleshooting

### API Key Error
- Ensure your `.env` file exists and contains a valid API key
- Check that the key starts with `gsk_`
- Verify you have API access at [console.groq.com](https://console.groq.com/)

### Import Errors
- Make sure all files are in the same directory
- Verify all dependencies are installed: `pip install -r requirements.txt`

### No Results from Knowledge Base
- The search uses fuzzy matching, so try different phrasings
- Check the `semantic_query.py` file to see available topics

## Security Notes

⚠️ **Important**: 
- Never commit your `.env` file to version control
- The `.gitignore` file is configured to exclude it
- Keep your API key confidential

## Contributing

Feel free to expand the knowledge base in `semantic_query.py` by adding more agricultural Q&A pairs!

## License

This project is open source and available for educational and agricultural purposes.

## Support

For issues with:
- **The application**: Check the troubleshooting section above
- **Groq API**: Visit [Groq's documentation](https://console.groq.com/docs)
- **Agricultural content**: Consult with local agricultural experts

---

**Built with ❤️ for farmers | Powered by Groq AI (Llama 3.3 70B)**
