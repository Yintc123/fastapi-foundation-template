import os
from functools import lru_cache

from .base import BaseAppSettings
from .local import LocalAppSettings
from .dev import DevAppSettings
from .prod import ProdAppSettings

_ENV_MAP: dict[str, type[BaseAppSettings]] = {
    "local": LocalAppSettings,
    "development": DevAppSettings,
    "production": ProdAppSettings
}

@lru_cache
def get_app_settings() -> BaseAppSettings:
    env: str = os.getenv("APP_ENV", "local").lower()
    settings_cls: type[BaseAppSettings] = _ENV_MAP.get(env, LocalAppSettings)

    return settings_cls()

# 對外只 export 這兩個物件，使用者不需要知道不同環境是否有分檔
__all__ = ["BaseAppSettings", "get_app_settings"]