import token
from pathlib import Path
from typing import Optional

import certifi
import requests

from utils.config import configure_or_get_config
from .httpconfig import (
    DataPostNfsvmConfig,
    DataPatchNfsvmConfig,
    DataPostInfinidatShareConfig,
    DataPatchInfinidatShareConfig
)


class HttpMethod:
    """Список HTTP методов"""

    INFINIDAT_POST_SHARE_BODY = DataPostInfinidatShareConfig(
        infinidat_filesystem_size=7,
        infinidat_filesystem_ip="10.231.9.158",
        infinidat_nfs_network="10.231.16.80/28",
    )
    INFINIDAT_PATCH_NFSVM_BODY = DataPatchInfinidatShareConfig(
        infinidat_filesystem_size=8,
    )
    NFSVM_POST_BODY = DataPostNfsvmConfig(
        nfs_capacity=50,
    )
    NFSVM_PATCH_BODY = DataPatchNfsvmConfig(
        nfs_capacity=50,
    )

    def __new__(cls, *args, **kwargs):
        cls.headers = cls.get_token()
        return super().__new__(cls)

    def __init__(self):
        self.client = requests

    @staticmethod
    def get_token():
        token = (
            configure_or_get_config()
            .get("jwt_token", "")
        )
        headers = {'Authorization': token}
        return headers

    def _api_request(self, url: str, method: str, headers: dict = None, data: dict = None, params: dict = None):
        return self.client.request(
            method=method,
            url=url,
            headers=headers or self.headers,
            data=data,
            params=params,
            verify=certifi.where(),
        )

    def get(self, url: str, params: Optional[dict] = None):
        return self._api_request(url, method="GET", params=params)

    def patch(self, url: str, body: Optional[dict] = None):
        return self._api_request(url, method="PATCH", data=body)

    def post(self, url: str, body: Optional[dict] = None):
        return self._api_request(url, method="POST", data=body)

    def put(self, url: str, body: Optional[dict] = None):
        return self._api_request(url, method="PUT", data=body)

    def delete(self, url: str, params: Optional[dict] = None):
        return self._api_request(url, method="DELETE", params=params)

    def patch_nvsvm(self, url: str):
        return self.patch(
            url,
            body=self.NFSVM_PATCH_BODY,
        )

    def patch_infinidat_share(self, url: str):
        return self.patch(
            url,
            body=self.INFINIDAT_PATCH_NFSVM_BODY,
        )

    def post_infinidat_share(self, url: str):
        return self.post(
            url,
            body=self.INFINIDAT_POST_SHARE_BODY
        )

    def post_nfsvm(self, url: str):
        return self.post(
            url,
            body=self.NFSVM_POST_BODY,
        )
