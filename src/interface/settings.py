from pydantic_settings import BaseSettings, SettingsConfigDict


class MongoDBSettings(BaseSettings):
    HOST: str
    USER: str
    PASSWORD: str
    DATABASE: str

    model_config = SettingsConfigDict(env_prefix="MONGODB_")


class AppSettings(BaseSettings):
    name: str = "Eduardo's Model Portfolio"
    logo_filepath: str = "assets/logo.png"
    style_filepath: str = "assets/style.css"


class Settings(BaseSettings):
    debug: bool = False
    db_settings: MongoDBSettings = MongoDBSettings()
    app_settings: AppSettings = AppSettings()

    model_config = SettingsConfigDict(
        env_prefix="",
        case_sensitive=False,
    )
