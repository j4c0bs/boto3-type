# -*- coding: utf-8 -*-

from .common import is_resource


def istype(resource, service_name):
    """Return whether a resource service is an instance of the reference service name.

    Args:
        client: boto3.resources.base.ServiceResource
        service_name: str
            - the service name e.g. 's3'

    Returns: bool
    """

    if is_resource(resource):
        return resource.meta.service_name.lower() == service_name.strip().lower()
    return False
