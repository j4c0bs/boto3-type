# -*- coding: utf-8 -*-

from .common import is_client


def istype(client, service_name: str):
    """Return whether a client is an instance of the reference service name.

    Args:
        client: botocore.client.BaseClient
        service_name: str
            - the service name e.g. 's3'

    Returns: bool
    """

    if is_client(client):
        return (
            client.meta.service_model.service_name.lower()
            == service_name.strip().lower()
        )
    return False
