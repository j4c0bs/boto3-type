#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

import boto3
import moto
import pytest

import boto3_type as bt


@pytest.fixture(scope="function")
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"


@pytest.fixture(scope="function")
def client(aws_credentials):
    with moto.mock_s3():
        yield boto3.client("s3", region_name="us-west-2")


@pytest.fixture(scope="function")
def bucket(aws_credentials):
    with moto.mock_s3():
        yield boto3.resource("s3", region_name="us-west-2").Bucket("test-bucket")


@pytest.fixture(scope="function")
def resource(aws_credentials):
    with moto.mock_cloudwatch():
        yield boto3.resource("cloudwatch", region_name="us-west-2")


@pytest.mark.parametrize(
    "service_name, expected", [("s3", True), (["s3", "x"], True), ("ecs", False)]
)
def test_client(service_name, expected, client):
    assert bt.client.istype(client, service_name) == expected


@pytest.mark.parametrize(
    "service_name, expected",
    [("cloudwatch", True), (["x", "cloudwatch"], True), ("ecs", False)],
)
def test_resource(service_name, expected, resource):
    assert bt.resource.istype(resource, service_name) == expected


@pytest.mark.parametrize(
    "name, expected", [("bucket", True), (["x", "bucket"], True), ("ecs", False)]
)
def test_s3(name, expected, bucket):
    assert bt.s3.istype(bucket, name) == expected


@pytest.mark.parametrize(
    "resource_service, service_names, expected",
    [
        ("a", "a", True),
        ("A", "a", True),
        ("A", ["a", "x"], True),
        ("a", "x", False),
        ("", "x", False),
    ],
)
def test_compare(resource_service, service_names, expected):
    assert bt.util.compare(resource_service, service_names) == expected
