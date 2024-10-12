from .conftest import get_suop_api
from utils.checking import Checking

suop_api = get_suop_api()


def test_get_cluster(get_token):

    print(" -----------------------------------------------------------------------------------------------")
    print("*****  Проверка авторизации  *****")
    print("Метод GET POST")
    print("кластер айди в самом тест_апи: " + get_token)
    result_get = suop_api.get_suop_clusters_id(get_token)
    Checking.check_status_code(result_get, 200)
    Checking.check_json_token(result_get,
                              ['id', 'name', 'title', 'platform_id', 'kubernetes_id', 'control_planes_count',
                               'nfs_capacity', 'pv_limit', 'pv_used', 'cluster_network_id', 'internal_ip', 'external_ip',
                               'facilities', 'status', 'stage', 'created_at', 'updated_at', 'disks_capacity', 'vcpu', 'ram'])
    # Checking.check_json_value(result_get, 'id', 993)
    Checking.check_json_search_word_in_value(result_get, 'title', 'amanuylov')
    # token = json.loads(result_get.text)  # Эта конструкция нужна для получения списка обязательных полей, удобно
    # print(list(token))


def test_get_persistent_volumes(get_token):
    """ Тест-кейс persistent_volumes"""

    print("*****  Проверка получения persistent_volumes  *****")
    result_get_persistent_volumes = suop_api.get_suop_persistent_volumes(get_token)
    Checking.check_status_code(result_get_persistent_volumes, 200)
    print(" -----------------------------------------------------------------------------------------------")


""" Тест-кейс запрос platforms """
def test_get_platforms():
    print("*****  Проверка получения записей platforms  *****")
    result_get_platforms = suop_api.get_suop_platforms()
    Checking.check_status_code(result_get_platforms, 200)
    print(" -----------------------------------------------------------------------------------------------")


""" Тест-кейс запрос записей notifications"""
def test_get_notifications(get_token):
    print("*****  Проверка получения записей notifications  *****")
    result_get_notifications = suop_api.get_suop_notifications(get_token)
    Checking.check_status_code(result_get_notifications, 200)
    print(" -----------------------------------------------------------------------------------------------")

""" Тест-кейс monitoring services"""
def test_get_monitoring_services(get_token):
    print("*****  Проверка получения кредов мониторинга  *****")
    result_get_monitoring_services = suop_api.get_suop_monitoring_services(get_token)
    Checking.check_status_code(result_get_monitoring_services, 200)
    print(" -----------------------------------------------------------------------------------------------")

""" Тест-кейс №97 успешно """
# def test_get_facilities():
#     print("*****  Проверка удаления NFS-VM  *****")
#     result_get_facilities = Suop_api.get_suop_facilities()
#     Checking.check_status_code(result_get_facilities, 200)
#     print(" -----------------------------------------------------------------------------------------------")

""" Тест-кейс nateruls успешно"""
# def test_get_nat_rules(get_token):
#     print("*****  Проверка получения nat-rules *****")
#     result_get_natrules = Suop_api.get_suop_nat_rules(get_token)
#     Checking.check_status_code(result_get_natrules, 200)
#     print(" -----------------------------------------------------------------------------------------------")
"""========================================================================================================="""
""" Тест INFINIDAT SHARE POST"""
# def test_post_infinidat_share(get_token):
#     print("*****  Проверка создания INFINIDAT SHARE *****")
#     # каким запросом можно проверить, что инфинидат создан или что его нет
#     result_post_infinidat_share = Suop_api.post_suop_cluster_id_storage_infinidat_share(get_token)
#     Checking.check_status_code(result_post_infinidat_share, 200)
#     time.sleep(30)
    # каким запросом можно проверить, что инфинидат создан или что его нет

""" Тест INFINIDAT SHARE PATCH"""
# def test_patch_infinidat_share(get_token):
#     print("*****  Проверка изменения INFINIDAT SHARE *****")
#     # каким запросом можно проверить, что инфинидат создан или что его нет
#     result_patch_infinidat_share = Suop_api.patch_suop_cluster_id_storage_infinidat_share(get_token)
#     Checking.check_status_code(result_patch_infinidat_share, 200)
#     time.sleep(30)
    # каким запросом можно проверить, что инфинидат создан или что его нет


""" Тест INFINIDAT SHARE DELETE"""
# def test_delete_infinidat_share(get_token):
#     print("*****  Проверка удаления INFINIDAT SHARE  *****")
#     # каким запросом можно проверить, что инфинидат создан или что его нет
#     result_delete_infinidat_share = Suop_api.delete_suop_cluster_id_storage_infinidat_share(get_token)
#     Checking.check_status_code(result_delete_infinidat_share, 204)
#     time.sleep(30)
    # каким запросом можно проверить, что инфинидат создан или что его нет
"""========================================================================================================="""
""" Тест VM STOP УСПЕХ"""
# def test_post_stop_vm():
#     print("*****  Проверка остановки VM  *****")
#     result_get = Suop_api.get_suop_virtual_machines_id()
#     Checking.check_json_value(result_get, 'power_state', 'POWERED_ON')
#     result_post_stop_vm = Suop_api.post_suop_virtual_machines_stop()
#     Checking.check_status_code(result_post_stop_vm, 200)
#     time.sleep(30)
#     result_get = Suop_api.get_suop_virtual_machines_id()
#     Checking.check_json_value(result_get, 'power_state', 'POWERED_OFF')


""" Тест VM START УСПЕХ"""
# def test_post_start_vm():
#     print("*****  Проверка старта VM  *****")
#     result_get = Suop_api.get_suop_virtual_machines_id()
#     Checking.check_json_value(result_get, 'power_state', 'POWERED_OFF')
#     result_post_start_vm = Suop_api.post_suop_virtual_machines_start()
#     Checking.check_status_code(result_post_start_vm, 200)
#     time.sleep(30)
#     result_get = Suop_api.get_suop_virtual_machines_id()
#     Checking.check_json_value(result_get, 'power_state', 'POWERED_ON')


""" Тест VM RESTART УСПЕХ"""
# def test_post_restart_vm():
#     print("*****  Проверка рестарта VM  *****")
#     result_get = Suop_api.get_suop_virtual_machines_id()
#     Checking.check_json_value(result_get, 'power_state', 'POWERED_ON')
#     result_post_restart_vm = Suop_api.post_suop_virtual_machines_restart()
#     Checking.check_status_code(result_post_restart_vm, 200)
#     time.sleep(30)
#     result_get = Suop_api.get_suop_virtual_machines_id()
#     Checking.check_json_value(result_get, 'power_state', 'POWERED_ON')


""" Тест VM DELETE проверить"""
# def test_delete_vm():
#     print("*****  Проверка удаления VM  *****")
#     result_get = Suop_api.get_suop_virtual_machines_id()
#     Checking.check_status_code(result_get, 200)
#     result_delete_vm = Suop_api.delete_suop_virtual_machines()
#     Checking.check_status_code(result_delete_vm, 204)
#     time.sleep(30)
#     result_get = Suop_api.get_suop_virtual_machines_id()
#     Checking.check_status_code(result_get, 404)


"""========================================================================================================="""
""" Тест-кейс №50 УСПЕХ"""
# def test_post_nfsvm(get_token):
#     print("*****  Проверка создания NFS-VM  *****")
#     result_get = Suop_api.get_suop_clusters_id(get_token)
#     Checking.check_json_value(result_get, 'nfs_capacity', None)
#     result_post_nfsvm = Suop_api.post_suop_cluster_id_storage_nfsvm(get_token)
#     Checking.check_status_code(result_post_nfsvm, 200)
#     time.sleep(40)
#     result_get = Suop_api.get_suop_clusters_id(get_token)
#     Checking.check_json_value(result_get, 'nfs_capacity', 50)


""" Тест изменение NFS-VM УСПЕХ"""
# def test_patch_nfsvm(get_token):
#     print("*****  Проверка изменения NFS-VM  *****")
#     result_patch_nfsvm = Suop_api.patch_suop_cluster_id_storage_nfsvm(get_token)
#     Checking.check_status_code(result_patch_nfsvm, 200)
#     time.sleep(40)
#     result_get = Suop_api.get_suop_clusters_id(get_token)
#     Checking.check_json_value(result_get, 'nfs_capacity', 51)


""" Тест удаление NFS VM УСПЕХ"""
# def test_delete_nfsvm(get_token):
#     print("*****  Проверка удаления NFS-VM  *****")
#     result_delete_nfsvm = Suop_api.delete_suop_cluster_id_storage_nfsvm(get_token)
#     Checking.check_status_code(result_delete_nfsvm, 204)
#     time.sleep(60)
#     result_get = Suop_api.get_suop_clusters_id(get_token)
#     Checking.check_json_value(result_get, 'nfs_capacity', None)
"""========================================================================================================="""

""" Тест-кейс №36 готов, осталось добавить редактирование """
# def test_suspend_cluster(get_token): #success
#     # print(" -----------------------------------------------------------------------------------------------")
#     # print("*****  Тест-кейс №36 старт!  *****")
#     # print("*****  Проверка редактирования кластера  *****")
#     # result_get = Suop_api.get_suop_clusters_id(get_token)
#
#     print("*****  Проверка остановки работы кластера  *****")
#     result_patch_suspend = Suop_api.patch_suop_clusters_id_suspend(get_token)
#     Checking.check_status_code(result_patch_suspend, 200)
#     time.sleep(60)
#     result_get = Suop_api.get_suop_clusters_id(get_token)
#     Checking.check_json_value(result_get, 'status', 'SUSPENDED')
#     print("*****  Проверка восстановления работы кластера  *****")
#     result_patch_resume = Suop_api.patch_suop_clusters_id_resume(get_token)
#     Checking.check_status_code(result_patch_resume, 200)
#     time.sleep(60)
#     result_get = Suop_api.get_suop_clusters_id(get_token)
#     Checking.check_json_value(result_get, 'status', 'DONE')
#     print("*****  Тест-кейс №36 финиш!  *****")

