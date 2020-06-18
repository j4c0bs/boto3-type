# -*- coding: utf-8 -*-

"""Shared functions."""

import boto3
import botocore


__all__ = ["is_client", "is_resource"]


def is_client(client):
    return isinstance(client, botocore.client.BaseClient)


def is_resource(resource):
    return isinstance(resource, boto3.resources.base.ServiceResource)
