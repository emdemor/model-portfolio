from __future__ import annotations

from typing import Any
from urllib.parse import quote_plus

import streamlit as st
from pymongo import MongoClient

from interface.settings import Settings


settings = Settings()


def _build_mongo_uri() -> str:
    if settings.db_settings.URI:
        return settings.db_settings.URI

    user = quote_plus(settings.db_settings.USER)
    password = quote_plus(settings.db_settings.PASSWORD)
    host = settings.db_settings.HOST
    database = settings.db_settings.DATABASE
    return f"mongodb://{user}:{password}@{host}/{database}"


@st.cache_resource(show_spinner=False)
def get_mongo_client() -> MongoClient:
    return MongoClient(_build_mongo_uri())


def get_users_collection():
    client = get_mongo_client()
    return client[settings.db_settings.DATABASE][settings.auth_settings.user_collection]


def load_credentials() -> dict[str, Any]:
    """
    Loads user credentials from MongoDB and formats them for streamlit-authenticator.
    Expects hashed passwords in the database.
    """
    collection = get_users_collection()
    usernames: dict[str, Any] = {}

    for doc in collection.find({}, {"_id": 0}):
        username = doc.get("username")
        password = doc.get("password") or doc.get("password_hash")
        if not username or not password:
            continue

        usernames[username] = {
            "email": doc.get("email", ""),
            "first_name": doc.get("first_name", ""),
            "last_name": doc.get("last_name", ""),
            "password": password,
            "roles": doc.get("roles", []),
            "failed_login_attempts": doc.get("failed_login_attempts", 0),
            "logged_in": doc.get("logged_in", False),
        }

    return {"usernames": usernames}
