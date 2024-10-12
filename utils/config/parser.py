from configparser import ConfigParser
from pathlib import Path
from typing import Optional

from settings import CONFIG_INI


# Дефолтные секции в файле настроек
default_sections: list[str] = [
    "auth",
    "id",
    "t1_nfs_network",
    "nfs_network",
    "jwt_token",
]


class ConfigError(Exception):
    def __init__(self, message: str = "Invalid section/params in config file"):
        self.message = message

    def __repr__(self):
        return self.message

    __str__ = __repr__


def write_config_sections(sections_data: dict[str, dict], filename: Path = CONFIG_INI):
    parser = ConfigParser()
    parser.read_dict(sections_data)

    with open(filename, "w") as config_file:
        parser.write(config_file)


def config(sections: Optional[list[str]] = None, filename: Path = CONFIG_INI):
    """Считывание файла конфигурации."""

    sections = sections or default_sections
    parser = ConfigParser()
    parser.read(filename)

    config_ = {}

    for section in sections:
        if parser.has_section(section):
            params = parser.items(section)

            for param in params:
                config_[param[0]] = param[1]
        else:
            raise ConfigError
    print(config_)
    return config_


def is_config_exist() -> bool:
    return CONFIG_INI.is_file()


def configure_or_get_config(sections: Optional[dict] = None) -> dict[str, str]:
    return config()
