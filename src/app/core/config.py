from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):  
  NAME: str
  SECRET_KEY: str

  # API versions
  API_V1_STR: str = "/api/v1"
  API_V2_STR: str = "/api/v2"

  model_config = SettingsConfigDict(
    env_file=".env",
    extra="ignore",
    env_ignore_empty=True
  )


settings = Settings()
