# -*- coding: utf-8 -*-

import boto3

from .util import compare


def istype(resource, service_name):
    """Return whether a resource service is an instance of the reference service name.

    An iterable may be provided to check against multiple services. This is equivalent
    to ``istype(x, A) or istype(x, B)``.

    Args:
        client: boto3.resources.base.ServiceResource
        service_name: str | iterable
            - the service client name(s)

    Returns:
        bool
    """

    if isinstance(resource, boto3.resources.base.ServiceResource):
        return compare(resource.meta.service_name, service_name)
    return False
