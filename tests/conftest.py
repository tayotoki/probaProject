import pytest
import requests
import certifi

from utils.config import get_config, is_config_exist, write_config_sections

HOST = "https://kuberpanel-be-test.dtln.cloud"


def get_user_data() -> dict:
    all_config_data = {}
    all_config_data.setdefault("auth", {})["username"] = input("Введите логин: ")
    all_config_data.setdefault("auth", {})["password"] = input("Введите пароль: ")
    all_config_data.setdefault("id", {})["cluster_id"] = input("Введите ID тестового кластера: ")
    all_config_data.setdefault("id", {})["virtual_machines_id"] = input("Введите ID виртуальной машины: ")
    all_config_data.setdefault(
        "t1_nfs_network", {}
    )["t1_nfs_network"] = input("Введите T1 NFS NETWORK (+2): ")
    all_config_data.setdefault("nfs_network", {})["nfs_network"] = input("Введите NFS NETWORK: ")
    return all_config_data


def configure_config() -> str:
    """
    Запрашивает данные у пользователя для составления конфигурации теста
    или возвращает старую конфигурацию. JWT-токен запрашивается и обновляется в любом случае
    :return: ID кластера для дальнейшего использования в тестах
    """
    all_config_data = {}

    if is_config_exist():
        new_config_is_need = input(
            "Найден прошлый файл конфигурации с данными для теста, хотите перезаписать конфигурацию? (Y/N)\n"
        )
        match new_config_is_need:
            case "Y" | "y":
                all_config_data = get_user_data()
            case "N" | "n":
                old_config = get_config()
                all_config_data = old_config
            case _:
                return configure_config()
    else:
        all_config_data = get_user_data()

    if all((value.__class__ is str for value in all_config_data.values())):
        username = all_config_data["username"]
        password = all_config_data["password"]
    else:
        username = all_config_data["auth"]["username"]
        password = all_config_data["auth"]["password"]

    # Авторизация
    headers = {"Content-Type": "application/json"}
    body = {
        "username": username,
        "password": password,
    }
    response_token = requests.post(
        f'{HOST}/users/auth/login/',
        headers=headers,
        json=body,
        verify=certifi.where(),
    )

    all_config_data.setdefault("jwt_token", {})["jwt_token"] = response_token.json().get("token", "")
    write_config_sections(all_config_data)
    return all_config_data["id"]["cluster_id"]


@pytest.fixture(scope="session")
def get_token():
    from tests.constants import CLUSTER_ID

    cluster_id = CLUSTER_ID
    return cluster_id


def get_suop_api():
    from utils.api import SuopApi

    SuopApi = SuopApi()
    return SuopApi















# def get_data()->TextIO:
#     FILE_PATH = Path(__file__).parent / "test_file.txt"
#
#     with open(FILE_PATH, "w") as file:
#         file.write("Hello")
#
#     yield FILE_PATH
#
#     os.remove(FILE_PATH)


    # user_data = input("Введите Cluster ID: ")
    # print(f"Cluster ID: {user_data}")
    # return user_data