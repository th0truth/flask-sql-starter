from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):  
  NAME: str
  SECRET_KEY: str

  model_config = SettingsConfigDict(
    env_file=".env",
    extra="ignore",
    env_ignore_empty=True
  )


settings = Settings()
