# -*- coding: utf-8 -*-

import botocore

from .util import compare


def istype(client, service_name):
    """Return whether a client is an instance of the reference service name.

    An iterable may be provided to check against multiple services. This is equivalent
    to ``istype(x, A) or istype(x, B)``.

    Args:
        client: botocore.client.BaseClient
        service_name: str | iterable
            - the service client name(s)

    Returns:
        bool
    """

    if isinstance(client, botocore.client.BaseClient):
        return compare(client.meta.service_model.service_name, service_name)
    return False
