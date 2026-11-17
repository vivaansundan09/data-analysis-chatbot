# Data Analysis Knowledge Chatbot

A Streamlit chatbot powered by the Google Gemini API. The application uses the full 30-section data-analysis manual and system instructions from the supplied Python chatbot code. It covers data analysis, statistics, SQL, Excel, Python, Power BI, Tableau, business analytics, forecasting, machine-learning fundamentals, ethics, projects, and interview preparation.

## Files

- `app.py` — Streamlit application, Gemini integration, chat history, and full knowledge base.
- `requirements.txt` — Python dependencies.
- `.streamlit/secrets.toml.example` — safe TOML template; contains no real API key.
- `.gitignore` — prevents local secrets and development files from being committed.

## 1. Add your Gemini API key locally

1. Open the `.streamlit` folder.
2. Copy `secrets.toml.example` and rename the copy to `secrets.toml`.
3. Open `.streamlit/secrets.toml` and replace the placeholder:

```toml
GOOGLE_API_KEY = "PASTE_YOUR_GEMINI_API_KEY_HERE"
GEMINI_MODEL = "gemini-3.5-flash-lite"
```

The local `secrets.toml` is excluded by `.gitignore`. Do not upload it to GitHub.

### Windows PowerShell

From the project folder, run:

```powershell
Copy-Item .streamlit/secrets.toml.example .streamlit/secrets.toml
```

Then edit `.streamlit/secrets.toml` and add your key.

## 2. Install and run locally

Python 3.10 or newer is recommended.

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

Install packages and start Streamlit:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 3. Upload to GitHub

Upload the project files and folders, including `app.py`, `requirements.txt`, `README.md`, `.gitignore`, and `.streamlit/secrets.toml.example`.

Do **not** upload `.streamlit/secrets.toml`, `.env`, or any file containing a real API key. The `.gitignore` is configured to exclude the local secrets file.

## 4. Deploy on Streamlit Community Cloud

1. Push the safe project files to your GitHub repository.
2. In Streamlit Community Cloud, create an app and select that repository, branch, and `app.py` as the main file.
3. Open the app's **Settings → Secrets**.
4. Paste the following TOML, replacing the placeholder with your Gemini API key:

```toml
GOOGLE_API_KEY = "PASTE_YOUR_GEMINI_API_KEY_HERE"
GEMINI_MODEL = "gemini-3.5-flash-lite"
```

5. Save the settings. Streamlit will restart the app with the configured secrets.

The cloud Secrets editor is separate from the files in your GitHub repository. Do not add your real API key to `app.py` or commit it to GitHub.

## 5. Chat features

- Data-analysis knowledge base from the supplied chatbot code.
- Gemini-powered question answering.
- Conversation context using the most recent 12 messages.
- Session-based chat history.
- Clear-conversation control.
- Configurable Gemini model name through TOML secrets.

## Troubleshooting

**“Gemini API configuration was not found”**

- Local: confirm the file is named exactly `.streamlit/secrets.toml` and contains `GOOGLE_API_KEY`.
- Streamlit Community Cloud: add the TOML values under the deployed app's Settings → Secrets, then save.
- Ensure the key has not been revoked and the selected model is available to the Google AI project.

**API or model errors**

Check the key, model access, API quota, and Google AI project configuration. The default model is `gemini-3.5-flash-lite`; it can be changed using `GEMINI_MODEL`.

## Security reminder

The API key included in the source code shared for this update has deliberately not been copied into this project. Because it was included in a shared chat attachment, revoke that key and create a fresh one. Put the fresh key only in local `secrets.toml` or Streamlit Community Cloud Secrets.
