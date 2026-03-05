from __future__ import annotations

import streamlit_authenticator as stauth

from interface.auth_store import load_credentials
from interface.settings import Settings


settings = Settings()


def get_authenticator() -> stauth.Authenticate:
    credentials = load_credentials()
    return stauth.Authenticate(
        credentials,
        settings.auth_settings.cookie_name,
        settings.auth_settings.cookie_key,
        settings.auth_settings.cookie_expiry_days,
        auto_hash=False,
    )
