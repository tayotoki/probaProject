import token
from pathlib import Path

import certifi
import requests

from .config import configure_or_get_config


class HttpMethod:
    """Список HTTP методов"""

    def __new__(cls, *args, **kwargs):
        cls.headers = cls.get_token()

        cls.data_post_nfsvm = {"nfs_capacity": 50}
        cls.data_patch_nfsvm = {"nfs_capacity": 51}

        cls.data_post_infinidat_share = {
            "infinidat_filesystem_size": 7,
            "infinidat_filesystem_ip": "10.231.9.158",
            "infinidat_nfs_network": "10.231.16.80/28"
        }
        cls.data_patch_infinidat_share = {
            "infinidat_filesystem_size": 8
        }
        return super().__new__(cls)

    @staticmethod
    def get_token():
        token = (
            configure_or_get_config()
            .get("jwt_token", "")
        )
        headers = {'Authorization': token}
        return headers

    def get(self, url):
        result = requests.get(url, headers=self.headers, verify=certifi.where())
        return result

    def patch(self, url):
        result = requests.patch(url, headers=self.headers, verify=certifi.where())
        return result

    def patch_nvsvm(self, url):
        result = requests.patch(url, headers=self.headers, data=self.data_patch_nfsvm, verify=certifi.where())
        return result

    def patch_infinidat_share(self, url):
        result = requests.patch(url, headers=self.headers, data=self.data_patch_infinidat_share, verify=certifi.where())

    def post_nfsvm(self, url):
        result = requests.post(url, headers=self.headers, data=self.data_post_nfsvm, verify=certifi.where())
        return result

    def post(self, url):
        result = requests.post(url, headers=self.headers, verify=certifi.where())
        return result

    def post_infinidat_share(self, url):
        result = requests.post(url, headers=self.headers, data=self.data_post_infinidat_share, verify=certifi.where())
        return result

    def delete(self, url):
        result = requests.delete(url, headers=self.headers, verify=certifi.where())
        return result
