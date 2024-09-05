import token
from pathlib import Path

import certifi
import requests


"""Список HTTP методов"""
class HttpMethod:

    fr = open('tests/auth_token.txt', 'r')
    token = fr.read()
    headers = {'Authorization': token}

    data_post_nfsvm = {"nfs_capacity": 50}
    data_patch_nfsvm = {"nfs_capacity": 51}

    data_post_infinidat_share = {
  "infinidat_filesystem_size": 7,
  "infinidat_filesystem_ip": "10.231.9.158",
  "infinidat_nfs_network": "10.231.16.80/28"
}
    data_patch_infinidat_share = {
  "infinidat_filesystem_size": 8
}

    @staticmethod
    def get(url):
        result = requests.get(url, headers=HttpMethod.headers, verify=certifi.where())
        return result

    """=============================================================================================="""
    @staticmethod
    def patch(url):
        result = requests.patch(url, headers=HttpMethod.headers, verify=certifi.where())
        return result

    @staticmethod
    def patch_nvsvm(url):
        result = requests.patch(url, headers=HttpMethod.headers, data=HttpMethod.data_patch_nfsvm, verify=certifi.where())
        return result

    @staticmethod
    def patch_infinidat_share(url):
        result = requests.patch(url, headers=HttpMethod.headers, data=HttpMethod.data_patch_infinidat_share, verify=certifi.where())
        return result

    """=============================================================================================="""
    @staticmethod
    def post_nfsvm(url):
        result = requests.post(url, headers=HttpMethod.headers, data=HttpMethod.data_post_nfsvm, verify=certifi.where())
        return result

    @staticmethod
    def post(url):
        result = requests.post(url, headers=HttpMethod.headers, verify=certifi.where())
        return result

    @staticmethod
    def post_infinidat_share(url):
        result = requests.post(url, headers=HttpMethod.headers, data=HttpMethod.data_post_infinidat_share, verify=certifi.where())
        return result

    """=============================================================================================="""
    @staticmethod
    def delete(url):
        result = requests.delete(url, headers=HttpMethod.headers, verify=certifi.where())
        return result