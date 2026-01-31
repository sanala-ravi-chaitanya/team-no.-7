# 🔑 Getting Your Groq API Key - Step by Step Guide

Follow these simple steps to get your Groq API key:

## Step 1: Visit Groq Console

Open your web browser and go to: **https://console.groq.com/**

## Step 2: Create an Account or Sign In

- If you're new: Click "Sign Up" and create an account
- If you have an account: Click "Sign In" and log in

## Step 3: Navigate to API Keys

Once logged in:
1. Look for the **"API Keys"** section in the left sidebar or settings
2. Click on it to open the API Keys page

## Step 4: Create a New API Key

1. Click the **"Create API Key"** button
2. Give your key a name (e.g., "Kisan Call Centre App")
3. Click **"Create"**
4. **IMPORTANT**: Copy the API key immediately - you won't be able to see it again!

Your API key will look something like: `gsk_xxxxxxxxxxxxx...`

## Step 5: Set Up Your .env File

1. In your project folder (`c:\project`), you should see a file called `.env.example`
2. Create a copy of this file and name it `.env` (just `.env`, no `.example`)
3. Open the `.env` file in a text editor
4. Replace `your-groq-api-key-here` with your actual API key:

```
GROQ_API_KEY=gsk_your-actual-key-here
```

5. Save the file

## Step 6: Run the Application

Open a terminal/command prompt in your project folder and run:

```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

## 💰 Free Credits

Good news! Groq provides **free API access** with generous rate limits, perfect for testing and development!

## ⚠️ Important Security Notes

- **Never share your API key** with anyone
- **Never commit** your `.env` file to Git (it's already in `.gitignore`)
- If you accidentally expose your key, delete it immediately from the Groq console and create a new one

## 🆘 Troubleshooting

### "API key not found" error
- Make sure your `.env` file is in the same folder as `app.py`
- Check that the file is named exactly `.env` (not `.env.txt` or `.env.example`)
- Verify the API key is on the line starting with `GROQ_API_KEY=`

### "Invalid API key" error
- Double-check you copied the entire key (they're quite long!)
- Make sure there are no extra spaces before or after the key
- Verify the key starts with `gsk_`

### Can't find .env file in Windows
- Windows might hide file extensions
- In File Explorer, go to View → Show → File name extensions
- Then you can rename `.env.example` to `.env` properly

---

**Need more help?** Check the [Groq Documentation](https://console.groq.com/docs)
