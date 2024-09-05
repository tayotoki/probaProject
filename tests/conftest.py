import os
from pathlib import Path
from typing import TextIO
import pytest
import requests
import certifi

@pytest.fixture(scope="session")
def get_token():
    print("Запуск авторизации! Получение нового токена!")
    """STG"""
    # host = "https://kuberpanel-be-stg.dtln.cloud"
    # # username = input("Введите логин: ") # username = "avmanuylov"
    # # password = input("Введите пароль: ") # password = ""
    # username = "avmanuylov"
    # password = ""
    """TEST"""
    host = "https://kuberpanel-be-test.dtln.cloud"
    username = input("Введите логин: ") # username = "avmanuylov"
    password = input("Введите пароль: ") # password = ""


    cluster_id = input("Введите ID тестового кластера: ")
    virtual_machines_id = input("Введите ID виртуальной машины: ")
    def write_file_vm_id()->TextIO:
        FILE_PATH = Path(__file__).parent / "vm_id.txt"
        with open(FILE_PATH, "w") as file:
            file.write(str(virtual_machines_id))
    write_file_vm_id()

    t1_nfs_network = input("Введите T1 NFS NETWORK (+2): ")
    def write_t1_nfs_network() -> TextIO:
        FILE_PATH = Path(__file__).parent / "t1_nfs_network.txt"
        with open(FILE_PATH, "w") as file:
            file.write(str(t1_nfs_network))
    write_t1_nfs_network()

    nfs_network = input("Введите NFS NETWORK: ")
    def write_nfs_network() -> TextIO:
        FILE_PATH = Path(__file__).parent / "nfs_network.txt"
        with open(FILE_PATH, "w") as file:
            file.write(str(nfs_network))
    write_nfs_network()

    # with open("vm_id.txt", "w") as file:
    #     file.write(virtual_machines_id)
    """Авторизация"""
    headers = {"Content-Type": "application/json"}
    body = {"username": username, "password": password}
    response_token = requests.post(f'{host}/users/auth/login/', headers=headers, json=body, verify=certifi.where())

    """ Загрузка токена в файл """
    check = response_token.json()
    check_token = check.get('token')
    print(check_token)
    def write_file()->TextIO:
        FILE_PATH = Path(__file__).parent / "auth_token.txt"
        with open(FILE_PATH, "w") as file:
            file.write('JWT ' + str(check_token))
    write_file()
    print("Текстовый файл создан! Токен записан!")
    return cluster_id















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