# -*- coding: utf-8 -*-

__all__ = ["istype"]


from .common import is_resource


def _is_subresource(resource):
    if is_resource(resource):
        return resource.meta.service_name.lower() == "s3"
    return False


def istype(subresource, service_name):
    """Return whether an S3 subresource is an instance of the reference name.

    Args:
        client: boto3.resources.base.ServiceResource
        service_name: str
            - the subresource name

    Returns: bool
    """

    if _is_subresource(subresource):
        return (
            subresource.meta.resource_model.name.lower() == service_name.strip().lower()
        )
    return False
