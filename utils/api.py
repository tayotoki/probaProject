import json
import time
from pprint import pprint
from typing import TextIO
from tests.conftest import get_token
from utils.httpmethod import HttpMethod


"""Сдесь собираем тестовые кирпичики для дальнейшего построения тестового сценария"""
# base_url = "https://kuberpanel-be-stg.dtln.cloud/suop/"
base_url = "https://kuberpanel-be-test.dtln.cloud/suop/"
line = '==================================================================================================='

class Suop_api():

    @staticmethod #success
    def get_suop_clusters_id(get_token):
        cluster_id = get_token
        get_cluster_resourse = f"clusters/{cluster_id}"
        get_cluster_url = base_url + get_cluster_resourse
        print("Сформированный URL для запроса: " + get_cluster_url)
        result_get = HttpMethod.get(get_cluster_url)
        result_get.encoding = 'utf-8'
        print(line)
        print("Полученный результат: ")
        pprint(result_get.json())
        return result_get


    @staticmethod
    def patch_suop_clusters_id_suspend(get_token):
        cluster_id = get_token
        patch_clusters_suspend_resourse = f"cluster/{cluster_id}/suspend"
        patch_clusters_suspend_url = base_url + patch_clusters_suspend_resourse #https://kuberpanel-be-stg.dtln.cloud/suop/cluster/993/suspend
        print("Сформированный URL для запроса: " + patch_clusters_suspend_url)
        result_patch = HttpMethod.patch(patch_clusters_suspend_url)
        result_patch.encoding = 'utf-8'
        print(line)
        print("Полученный результат: ")
        pprint(result_patch.json())
        return result_patch


    @staticmethod
    def patch_suop_clusters_id_resume(get_token):
        cluster_id = get_token
        patch_clusters_resume_resourse = f"cluster/{cluster_id}/resume"
        patch_clusters_resume_url = base_url + patch_clusters_resume_resourse #https://kuberpanel-be-stg.dtln.cloud/suop/cluster/993/resume
        print("Сформированный URL для запроса: " + patch_clusters_resume_url)
        result_patch = HttpMethod.patch(patch_clusters_resume_url)
        result_patch.encoding = 'utf-8'
        print(line)
        print("Полученный результат: ")
        pprint(result_patch.json())
        return result_patch


    @staticmethod
    def get_suop_clusters_organization_id(get_token): #исправить - нужен организатион айди вместо кластер айди
        organisation_id = get_token
        get_cluster_resourse = "clusters?organization_id="
        get_cluster_url = base_url + get_cluster_resourse + organisation_id #https://kuberpanel-be-stg.dtln.cloud/suop/clusters?organization_id=1019
        print("Сформированный URL для запроса: " + get_cluster_url)
        result_get = HttpMethod.get(get_cluster_url)
        result_get.encoding = 'utf-8'
        print(line)
        print("Полученный результат: ")
        pprint(result_get.json())
        return result_get


    @staticmethod
    def get_suop_clusters_user_id(get_token):  # исправить - нужен user айди вместо кластер айди
        user_id = get_token
        get_cluster_resourse = "clusters?user_id="
        get_cluster_url = base_url + get_cluster_resourse + user_id #https://kuberpanel-be-stg.dtln.cloud/suop/clusters?user_id=7777
        print("Сформированный URL для запроса: " + get_cluster_url)
        result_get = HttpMethod.get(get_cluster_url)
        result_get.encoding = 'utf-8'
        print(line)
        print("Полученный результат: ")
        pprint(result_get.json())
        return result_get


    @staticmethod
    def get_suop_facilities():
        get_facilities_resourse = "facilities"
        get_facilities_url= base_url + get_facilities_resourse #https://kuberpanel-be-stg.dtln.cloud/suop/facilities
        print("Сформированный URL для запроса: " + get_facilities_url)
        result_get = HttpMethod.get(get_facilities_url)
        result_get.encoding = 'utf-8'
        print(line)
        print("Полученный результат: ")
        pprint(result_get.json())
        return result_get


    @staticmethod
    def get_suop_nat_rules(get_token):
        cluster_id = get_token
        get_nat_rules_resourse = f"nat-rules?cluster_id={cluster_id}"
        get_nat_rules_url = base_url + get_nat_rules_resourse #https://kuberpanel-be-stg.dtln.cloud/suop/nat-rules?cluster_id=993
        print("Сформированный URL для запроса: " + get_nat_rules_url)
        result_get = HttpMethod.get(get_nat_rules_url)
        result_get.encoding = 'utf-8'
        print(line)
        print("Полученный результат: ")
        pprint(result_get.json())
        return result_get

    """ NFS VM """
    @staticmethod
    def post_suop_cluster_id_storage_nfsvm(get_token):
        cluster_id = get_token
        post_nfsvm_resourse = f"clusters/{cluster_id}/storages/nfs-vm"
        post_nfsvm_url = base_url + post_nfsvm_resourse
        print("Сформированный URL для запроса: " + post_nfsvm_url)
        result_post = HttpMethod.post_nfsvm(post_nfsvm_url)
        return result_post


    @staticmethod
    def patch_suop_cluster_id_storage_nfsvm(get_token):
        cluster_id = get_token
        patch_nfsvm_resourse = f"clusters/{cluster_id}/storages/nfs-vm"
        patch_nfsvm_url = base_url + patch_nfsvm_resourse
        print("Сформированный URL для запроса: " + patch_nfsvm_url)
        result_patch = HttpMethod.patch_nvsvm(patch_nfsvm_url)
        return result_patch


    @staticmethod
    def delete_suop_cluster_id_storage_nfsvm(get_token):
        cluster_id = get_token
        delete_nfsvm_resourse = f"clusters/{cluster_id}/storages/nfs-vm" #https://kuberpanel-be-stg.dtln.cloud/suop/clusters/3333/storages/nfs-vm
        delete_nfsvm_url = base_url + delete_nfsvm_resourse
        print("Сформированный URL для запроса: " + delete_nfsvm_url)
        result_delete = HttpMethod.delete(delete_nfsvm_url)
        return result_delete


    """ INFINIDAT SHARE """

    @staticmethod
    def post_suop_cluster_id_storage_infinidat_share(get_token):
        cluster_id = get_token
        post_infinidat_share_resourse = f"clusters/{cluster_id}/storages/infinidat-share"
        post_infinidat_share_url = base_url + post_infinidat_share_resourse
        print("Сформированный URL для запроса: " + post_infinidat_share_url)
        result_post = HttpMethod.post_infinidat_share(post_infinidat_share_url) #добавить метод
        return result_post

    @staticmethod
    def patch_suop_cluster_id_storage_infinidat_share(get_token):
        cluster_id = get_token
        patch_infinidat_share_resourse = f"clusters/{cluster_id}/storages/infinidat-share"
        patch_infinidat_share_url = base_url + patch_infinidat_share_resourse
        print("Сформированный URL для запроса: " + patch_infinidat_share_url)
        result_patch = HttpMethod.patch_infinidat_share(patch_infinidat_share_url) #добавить метод
        return result_patch

    @staticmethod
    def delete_suop_cluster_id_storage_infinidat_share(get_token):
        cluster_id = get_token
        delete_infinidat_share_resourse = f"clusters/{cluster_id}/storages/infinidat-share"
        delete_infinidat_share_url = base_url + delete_infinidat_share_resourse
        print("Сформированный URL для запроса: " + delete_infinidat_share_url)
        result_delete = HttpMethod.delete(delete_infinidat_share_url)
        return result_delete



    """ NODE GROUPS """

    @staticmethod
    def get_suop_node_groups_id(get_token):
        cluster_id = get_token
        get_node_groups_id_resourse = "node-groups/"
        get_node_groups_id_url = base_url + get_node_groups_id_resourse + cluster_id  # https://kuberpanel-be-stg.dtln.cloud/suop/node-groups/88
        print("Сформированный URL для запроса: " + get_node_groups_id_url)
        result_get = HttpMethod.get(get_node_groups_id_url)
        result_get.encoding = 'utf-8'
        print(line)
        print("Полученный результат: ")
        pprint(result_get.json())
        return result_get


    @staticmethod #success
    def get_suop_node_groups(get_token):
        cluster_id = get_token
        get_node_groups_resourse = "node-groups?cluster_id="
        get_node_groups_url = base_url + get_node_groups_resourse + cluster_id #https://kuberpanel-be-stg.dtln.cloud/suop/node-groups?cluster_id=993
        print("Сформированный URL для запроса: " + get_node_groups_url)
        result_get = HttpMethod.get(get_node_groups_url)
        result_get.encoding = 'utf-8'
        print(line)
        print("Полученный результат: ")
        pprint(result_get.json())
        return result_get


    @staticmethod
    def delete_suop_node_groups_id(get_token):
        cluster_id = get_token
        delete_node_groups_id_resourse = "node-groups/"
        delete_node_groups_id_url = base_url + delete_node_groups_id_resourse + cluster_id  # https://kuberpanel-be-stg.dtln.cloud/suop/node-groups/3333
        print("Сформированный URL для запроса: " + delete_node_groups_id_url)
        result_delete = HttpMethod.delete(delete_node_groups_id_url)
        result_delete.encoding = 'utf-8'
        print(line)
        print("Полученный результат: ")
        pprint(result_delete.json())
        return result_delete



    """ VIRTUAL MACHINES """
    @staticmethod #success
    def get_suop_virtual_machines(get_token):
        cluster_id = get_token
        get_virtual_machines_resourse = "virtual-machines?cluster_id="
        get_virtual_machines_url = base_url + get_virtual_machines_resourse + cluster_id  # https://kuberpanel-be-stg.dtln.cloud/suop/virtual-machines?cluster_id=99
        print("Сформированный URL для запроса: " + get_virtual_machines_url)
        result_get = HttpMethod.get(get_virtual_machines_url)
        result_get.encoding = 'utf-8'
        print(line)
        print("Полученный результат: ")
        pprint(result_get.json())
        return result_get


    @staticmethod
    def get_suop_virtual_machines_id():
        f = open('vm_id.txt', 'r')
        vm_id = f.read()
        get_virtual_machines_id_resourse = f"virtual-machines/{vm_id}"
        get_virtual_machines_id_url = base_url + get_virtual_machines_id_resourse  # https://kuberpanel-be-stg.dtln.cloud/suop/virtual-machines/334
        print("Сформированный URL для запроса: " + get_virtual_machines_id_url)
        result_get = HttpMethod.get(get_virtual_machines_id_url)
        result_get.encoding = 'utf-8'
        print(line)
        print("Полученный результат: ")
        pprint(result_get.json())
        return result_get


    @staticmethod
    def post_suop_virtual_machines_restart():
        f = open('vm_id.txt', 'r')
        vm_id = f.read()
        post_vm_restart_resourse = f"virtual-machines/{vm_id}/restart" #https://kuberpanel-be-stg.dtln.cloud/suop/virtual-machines/333/restart
        post_vm_restart_url = base_url + post_vm_restart_resourse
        print("Сформированный URL для запроса: " + post_vm_restart_url)
        result_post = HttpMethod.post(post_vm_restart_url)
        result_post.encoding = 'utf-8'
        print(line)
        print("Полученный результат: ")
        pprint(result_post.json())
        return result_post


    @staticmethod
    def post_suop_virtual_machines_start():
        f = open('vm_id.txt', 'r')
        vm_id = f.read()
        post_vm_start_resourse = f"virtual-machines/{vm_id}/start"  # https://kuberpanel-be-stg.dtln.cloud/suop/virtual-machines/333/start
        post_vm_start_url = base_url + post_vm_start_resourse
        print("Сформированный URL для запроса: " + post_vm_start_url)
        result_post = HttpMethod.post(post_vm_start_url)
        result_post.encoding = 'utf-8'
        print(line)
        print("Полученный результат: ")
        pprint(result_post.json())
        return result_post


    @staticmethod
    def post_suop_virtual_machines_stop():
        f = open('vm_id.txt', 'r')
        vm_id = f.read()
        post_vm_stop_resourse = f"virtual-machines/{vm_id}/stop"  # https://kuberpanel-be-stg.dtln.cloud/suop/virtual-machines/333/stop
        post_vm_stop_url = base_url + post_vm_stop_resourse
        print("Сформированный URL для запроса: " + post_vm_stop_url)
        result_post = HttpMethod.post(post_vm_stop_url)
        result_post.encoding = 'utf-8'
        print(line)
        print("Полученный результат: ")
        pprint(result_post.json())
        return result_post


    @staticmethod
    def delete_suop_virtual_machines():
        f = open('vm_id.txt', 'r')
        vm_id = f.read()
        delete_vm_resourse = f"virtual-machines/{vm_id}"  # https://kuberpanel-be-stg.dtln.cloud/suop/virtual-machines/333
        delete_vm_url = base_url + delete_vm_resourse
        print("Сформированный URL для запроса: " + delete_vm_url)
        result_delete = HttpMethod.delete(delete_vm_url)
        return result_delete

    """ Черновик """