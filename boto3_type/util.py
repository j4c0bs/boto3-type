# -*- coding: utf-8 -*-


def compare(resource_service, service_names):

    resource_service = resource_service.lower()

    if isinstance(service_names, str):
        service_names = [service_names]

    return any((resource_service == name.lower() for name in service_names))
