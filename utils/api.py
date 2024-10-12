from collections.abc import Callable
from pprint import pprint
from typing import Optional

from requests import Response

from tests.conftest import get_token
from utils.config import configure_or_get_config
from utils.http.httpmethod import HttpMethod


"""Сдесь собираем тестовые кирпичики для дальнейшего построения тестового сценария"""
# base_url = "https://kuberpanel-be-stg.dtln.cloud/suop/"
BASE_URL = "https://kuberpanel-be-test.dtln.cloud/suop/"
line = '==================================================================================================='


class SuopApi:
    ROUTES = {
        "get_suop_clusters_id": BASE_URL + "clusters/{some_id}",
        "patch_suop_clusters_id_suspend": BASE_URL + "cluster/{some_id}/suspend",
        "patch_suop_clusters_id_resume": BASE_URL + "cluster/{some_id}/resume",
        "get_suop_clusters_organization_id": BASE_URL + "clusters?organization_id={some_id}",
        "get_suop_clusters_user_id": BASE_URL + "clusters?user_id={some_id}",
        "get_suop_facilities": BASE_URL + "facilities",
        "get_suop_nat_rules": BASE_URL + "nat-rules?cluster_id={some_id}",
        "post_suop_cluster_id_storage_nfsvm": BASE_URL + "clusters/{some_id}/storages/nfs-vm",
        "patch_suop_cluster_id_storage_nfsvm": BASE_URL + "clusters/{some_id}/storages/nfs-vm",
        "delete_suop_cluster_id_storage_nfsvm": BASE_URL + "clusters/{some_id}/storages/nfs-vm",
        "post_suop_cluster_id_storage_infinidat_share": BASE_URL + "clusters/{some_id}/storages/infinidat-share",
        "patch_suop_cluster_id_storage_infinidat_share": BASE_URL + "clusters/{some_id}/storages/infinidat-share",
        "delete_suop_cluster_id_storage_infinidat_share": BASE_URL + "clusters/{some_id}/storages/infinidat-share",
        "get_suop_node_groups_id": BASE_URL + "node-groups/{some_id}",
        "get_suop_node_groups": BASE_URL + "node-groups?cluster_id={some_id}",
        "delete_suop_node_groups_id": BASE_URL + "node-groups/{some_id}",
        "get_suop_virtual_machines": BASE_URL + "virtual-machines?cluster_id={some_id}",
        "get_suop_virtual_machines_id": BASE_URL + "virtual-machines/{some_id}",
        "post_suop_virtual_machines_restart": BASE_URL + "virtual-machines/{some_id}/restart",
        "post_suop_virtual_machines_start": BASE_URL + "virtual-machines/{some_id}/start",
        "post_suop_virtual_machines_stop": BASE_URL + "virtual-machines/{some_id}/stop",
        "delete_suop_virtual_machines": BASE_URL + "virtual-machines/{some_id}",
    }

    def __init__(self):
        self.HttpMethod = HttpMethod()

    def _make_request(self, http_method: Callable[[str], Response], method_name: str, some_id: Optional[str] = None):
        url = self.__class__.ROUTES[method_name].format(some_id=some_id)
        print("Сформированный URL для запроса: " + url)
        result = http_method(url)
        result.encoding = "utf-8"
        print(line)
        print("Полученный результат: ")
        pprint(result.json())
        return result

    @property
    def vm_id(self) -> str:
        """
        ID виртуальной машины
        :return: str
        """
        return configure_or_get_config().get("virtual_machines_id")

    def get_suop_clusters_id(self, get_token):
        return self._make_request(
            http_method=self.HttpMethod.get,
            method_name=self.get_suop_clusters_id.__name__,
            some_id=get_token,
        )

    def patch_suop_clusters_id_suspend(self, get_token):
        return self._make_request(
            http_method=self.HttpMethod.patch,
            method_name=self.patch_suop_clusters_id_suspend.__name__,
            some_id=get_token,
        )

    def patch_suop_clusters_id_resume(self, get_token):
        return self._make_request(
            http_method=self.HttpMethod.patch,
            method_name=self.patch_suop_clusters_id_resume.__name__,
            some_id=get_token,
        )

    # TODO: исправить - нужен организатион айди вместо кластер айди
    def get_suop_clusters_organization_id(self, get_token):
        return self._make_request(
            http_method=self.HttpMethod.get,
            method_name=self.get_suop_clusters_organization_id.__name__,
            some_id=get_token,
        )

    # TODO: исправить - нужен user айди вместо кластер айди
    def get_suop_clusters_user_id(self, get_token):
        return self._make_request(
            http_method=self.HttpMethod.get,
            method_name=self.get_suop_clusters_user_id.__name__,
            some_id=get_token,
        )

    def get_suop_facilities(self):
        return self._make_request(
            http_method=self.HttpMethod.get,
            method_name=self.get_suop_facilities.__name__,
        )

    def get_suop_nat_rules(self, get_token):
        return self._make_request(
            http_method=self.HttpMethod.get,
            method_name=self.get_suop_nat_rules.__name__,
            some_id=get_token,
        )

    # NFS VM
    def post_suop_cluster_id_storage_nfsvm(self, get_token):
        return self._make_request(
            http_method=self.HttpMethod.post_nfsvm,
            method_name=self.post_suop_cluster_id_storage_nfsvm.__name__,
            some_id=get_token,
        )

    def patch_suop_cluster_id_storage_nfsvm(self, get_token):
        return self._make_request(
            http_method=self.HttpMethod.patch_nvsvm,
            method_name=self.patch_suop_cluster_id_storage_nfsvm.__name__,
            some_id=get_token,
        )

    def delete_suop_cluster_id_storage_nfsvm(self, get_token):
        return self._make_request(
            http_method=self.HttpMethod.delete,
            method_name=self.delete_suop_cluster_id_storage_nfsvm.__name__,
            some_id=get_token,
        )

    # INFINIDAT SHARE
    def post_suop_cluster_id_storage_infinidat_share(self, get_token):
        return self._make_request(
            http_method=self.HttpMethod.post_infinidat_share,
            method_name=self.post_suop_cluster_id_storage_infinidat_share.__name__,
            some_id=get_token,
        )

    def patch_suop_cluster_id_storage_infinidat_share(self, get_token):
        return self._make_request(
            http_method=self.HttpMethod.patch_infinidat_share,
            method_name=self.patch_suop_cluster_id_storage_infinidat_share.__name__,
            some_id=get_token,
        )

    def delete_suop_cluster_id_storage_infinidat_share(self, get_token):
        return self._make_request(
            http_method=self.HttpMethod.delete,
            method_name=self.delete_suop_cluster_id_storage_infinidat_share.__name__,
            some_id=get_token,
        )

    # NODE GROUPS
    def get_suop_node_groups_id(self, get_token):
        return self._make_request(
            http_method=self.HttpMethod.get,
            method_name=self.get_suop_node_groups_id.__name__,
            some_id=get_token,
        )

    def get_suop_node_groups(self, get_token):
        return self._make_request(
            http_method=self.HttpMethod.get,
            method_name=self.get_suop_node_groups.__name__,
            some_id=get_token,
        )

    def delete_suop_node_groups_id(self, get_token):
        return self._make_request(
            http_method=self.HttpMethod.delete,
            method_name=self.delete_suop_node_groups_id.__name__,
            some_id=get_token,
        )

    # VIRTUAL MACHINES
    def get_suop_virtual_machines(self, get_token):
        return self._make_request(
            http_method=self.HttpMethod.get,
            method_name=self.get_suop_virtual_machines.__name__,
            some_id=get_token,
        )

    def get_suop_virtual_machines_id(self):
        return self._make_request(
            http_method=self.HttpMethod.get,
            method_name=self.get_suop_virtual_machines.__name__,
            some_id=self.vm_id,
        )

    def post_suop_virtual_machines_restart(self):
        return self._make_request(
            http_method=self.HttpMethod.post,
            method_name=self.post_suop_virtual_machines_restart.__name__,
            some_id=self.vm_id,
        )

    def post_suop_virtual_machines_start(self):
        return self._make_request(
            http_method=self.HttpMethod.post,
            method_name=self.post_suop_virtual_machines_start.__name__,
            some_id=self.vm_id,
        )

    def post_suop_virtual_machines_stop(self):
        return self._make_request(
            http_method=self.HttpMethod.post,
            method_name=self.post_suop_virtual_machines_stop.__name__,
            some_id=self.vm_id,
        )

    def delete_suop_virtual_machines(self):
        return self._make_request(
            http_method=self.HttpMethod.delete,
            method_name=self.delete_suop_virtual_machines.__name__,
            some_id=self.vm_id,
        )

    def get_suop_monitoring_services(self, get_token):
        return self._make_request(
            http_method=self.HttpMethod.get,
            method_name=self.get_suop_monitoring_services.__name__,
            some_id=get_token,
        )

    def get_suop_notifications(self, get_token):
        return self._make_request(
            http_method=self.HttpMethod.get,
            method_name=self.get_suop_notifications.__name__,
            some_id=get_token,
        )

    def get_suop_platforms(self):
        return self._make_request(
            http_method=self.HttpMethod.get,
            method_name=self.get_suop_platforms.__name__,
        )

    def get_suop_persistent_volumes(self, get_token):
        return self._make_request(
            http_method=self.HttpMethod.get,
            method_name=self.get_suop_persistent_volumes.__name__,
            some_id=get_token,
        )

    # """ Черновик """
    #
    # @staticmethod  # success
    # def get_suop_clusters_id(get_token):
    #     cluster_id = get_token
    #     get_cluster_resourse = f"clusters/{cluster_id}"
    #     get_cluster_url = base_url + get_cluster_resourse
    #     print("Сформированный URL для запроса: " + get_cluster_url)
    #     result_get = HttpMethod.get(get_cluster_url)
    #     result_get.encoding = 'utf-8'
    #     print(line)
    #     print("Полученный результат: ")
    #     pprint(result_get.json())
    #     return result_get