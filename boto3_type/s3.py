# -*- coding: utf-8 -*-

import boto3

from .util import compare


def istype(subresource, name):
    """Return whether an S3 subresource is an instance of the reference name.

    An iterable may be provided to check against multiple services. This is equivalent
    to ``istype(x, A) or istype(x, B)``.

    Args:
        client: boto3.resources.base.ServiceResource
        service_name: str | iterable
            - the subresource name(s)

    Returns:
        bool
    """
    if isinstance(subresource, boto3.resources.base.ServiceResource):
        return compare(subresource.meta.resource_model.name, name)
    return False
