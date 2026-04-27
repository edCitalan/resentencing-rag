# resentencing-rag

Streamlit chat UI backed by a Pinecone Assistant.

## Run locally

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m streamlit run app.py
```

## Streamlit Community Cloud

- Entry point: `app.py`
- Add secrets in the Streamlit Cloud UI (do not commit `.env`):
  - `PINECONE_API_KEY`
  - Optional auth gate settings:
    - `STREAMLIT_AUTH_REQUIRED`
    - `ACCESS_HANDOFF_SECRET`
    - `ACCESS_GATE_URL`
    - `CONTACT_EMAIL`

