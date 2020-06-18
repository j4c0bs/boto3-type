# boto3-type

Lightweight type check for boto3 service, resource instances.


## Install:

```bash
pip install boto3_type
```

## Problem:

```Python

In [1]: import boto3

In [2]: import botocore

In [3]: s3 = boto3.client("s3")

In [4]: type(s3)
Out[4]: botocore.client.S3

In [5]: isinstance(s3, botocore.client.S3)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-5-a7f37740cc80> in <module>
----> 1 isinstance(s3, botocore.client.S3)

AttributeError: module 'botocore.client' has no attribute 'S3'
```

## Usage:

```Python

In [1]: import boto3

In [2]: import boto3_type as bt

In [3]: client = boto3.client("ecs")

In [4]: resource = boto3.resource("s3")

In [5]: bucket = resource.Bucket("test-bucket")

In [6]: bt.is_client(client)
Out[6]: True

In [7]: bt.client.istype(client, "ecs")
Out[7]: True

In [8]: bt.is_resource(resource)
Out[8]: True

In [9]: bt.resource.istype(resource, "s3")
Out[9]: True

In [10]: bt.s3.istype(bucket, "bucket")
Out[10]: True

In [11]: bt.is_resource(client)
Out[11]: False

In [12]: bt.is_client(resource)
Out[12]: False

```
