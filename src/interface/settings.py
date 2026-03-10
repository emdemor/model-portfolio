from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class MongoDBSettings(BaseSettings):
    HOST: str
    USER: str
    PASSWORD: str
    DATABASE: str
    URI: str | None = None

    model_config = SettingsConfigDict(env_prefix="MONGODB_")


class AppSettings(BaseSettings):
    name: str = "Eduardo's Model Portfolio"
    logo_filepath: str = "assets/logo.png"
    style_filepath: str = "assets/style.css"


class AuthSettings(BaseSettings):
    cookie_name: str
    cookie_key: str
    cookie_expiry_days: float = 30.0
    user_collection: str = Field(
        default="users",
        validation_alias="MONGODB_AUTH_COLLECTION",
    )

    model_config = SettingsConfigDict(env_prefix="AUTH_")


class ProxySettings(BaseSettings):
    username: str | None = None
    password: str | None = None
    host: str | None = None
    port: str | None = None

    model_config = SettingsConfigDict(env_prefix="PROXY_")

    @property
    def url(self) -> str | None:
        if all([self.username, self.password, self.host, self.port]):
            return f"http://{self.username}:{self.password}@{self.host}:{self.port}/"
        return None


class Settings(BaseSettings):
    debug: bool = False
    db_settings: MongoDBSettings = MongoDBSettings()
    app_settings: AppSettings = AppSettings()
    auth_settings: AuthSettings = AuthSettings()

    model_config = SettingsConfigDict(
        env_prefix="",
        case_sensitive=False,
    )
