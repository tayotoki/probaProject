from typing import TypedDict


class DataPostNfsvmConfig(TypedDict):
    nfs_capacity: int


class DataPatchNfsvmConfig(DataPostNfsvmConfig):
    pass


class DataPatchInfinidatShareConfig(TypedDict):
    infinidat_filesystem_size: int


class DataPostInfinidatShareConfig(DataPatchInfinidatShareConfig):
    infinidat_filesystem_ip: str
    infinidat_nfs_network: str
