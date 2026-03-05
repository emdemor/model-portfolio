from pydantic_settings import BaseSettings, SettingsConfigDict


class MongoDBSettings(BaseSettings):
    HOST: str
    USER: str
    PASSWORD: str
    DATABASE: str

    model_config = SettingsConfigDict(env_prefix="MONGODB_")


class Settings(BaseSettings):
    app_name: str = "Supersimple Streamlit App"
    debug: bool = False
    db_settings: MongoDBSettings = MongoDBSettings()

    model_config = SettingsConfigDict(
        env_prefix="",
        case_sensitive=False,
    )
