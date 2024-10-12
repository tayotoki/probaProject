from pathlib import Path


CONFIG_INI = Path(__file__).resolve().parent / "config.ini"

# Дефолтные секции в файле настроек
DEFAULT_CONFIG_SECTIONS: list[str] = [
    "auth",
    "id",
    "t1_nfs_network",
    "nfs_network",
    "jwt_token",
]
