import os

import requests
from dotenv import load_dotenv

load_dotenv()

try:
    import streamlit as st
except Exception:
    st = None

_CHAT_URL = "https://prod-1-data.ke.pinecone.io/assistant/chat/reg"


def _get_setting(key: str, default: str = "") -> str:
    value = os.environ.get(key)
    if value is not None and str(value).strip() != "":
        return str(value)
    if st is not None:
        try:
            secret_value = st.secrets.get(key, default)
            if secret_value is not None and str(secret_value).strip() != "":
                return str(secret_value)
        except Exception:
            pass
    return default


def chat(prompt: str) -> str:
    api_key = _get_setting("PINECONE_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("Missing PINECONE_API_KEY (env var or Streamlit secret)")
    resp = requests.post(
        _CHAT_URL,
        headers={"Api-Key": api_key, "Content-Type": "application/json"},
        json={"messages": [{"role": "user", "content": prompt}]},
        timeout=60,
    )
    resp.raise_for_status()
    return resp.json()["message"]["content"]
