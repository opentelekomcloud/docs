# Reading a Specified PersistentVolume<a name="cce_02_0078"></a>

## Function<a name="s1a129d01d7064ee39544c508ecd9cb42"></a>

This API is used to read a specified PersistentVolume.

## URI<a name="s38d2d7ac9d9f4951888e3f4f6779980a"></a>

GET /api/v1/persistentvolumes/\{name\}

[Table 1](#t822b09e3c061429a994cacea8be759ae)  describes the parameters of this API.

**Table  1**  Parameter description

<a name="t822b09e3c061429a994cacea8be759ae"></a>
<table><thead align="left"><tr id="rc21b8b3e51304c9e8a38c370e9339ca8"><th class="cellrowborder" valign="top" width="22.06%" id="mcps1.2.4.1.1"><p id="a71a1a49de42f4918a4d54407842274d9"><a name="a71a1a49de42f4918a4d54407842274d9"></a><a name="a71a1a49de42f4918a4d54407842274d9"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.24%" id="mcps1.2.4.1.2"><p id="p3964669201717"><a name="p3964669201717"></a><a name="p3964669201717"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="58.699999999999996%" id="mcps1.2.4.1.3"><p id="a7695d01414db465c83aa8b69871a25bd"><a name="a7695d01414db465c83aa8b69871a25bd"></a><a name="a7695d01414db465c83aa8b69871a25bd"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="rd8795e7381364fee9547f9eade682583"><td class="cellrowborder" valign="top" width="22.06%" headers="mcps1.2.4.1.1 "><p id="a9bf082cde6a149a3a1ee51a984806855"><a name="a9bf082cde6a149a3a1ee51a984806855"></a><a name="a9bf082cde6a149a3a1ee51a984806855"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.2 "><p id="a98f847249f554de6b47792116337a553"><a name="a98f847249f554de6b47792116337a553"></a><a name="a98f847249f554de6b47792116337a553"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="58.699999999999996%" headers="mcps1.2.4.1.3 "><p id="a72e6b14d501e46deaa513c9739330098"><a name="a72e6b14d501e46deaa513c9739330098"></a><a name="a72e6b14d501e46deaa513c9739330098"></a>Name of the PersistentVolume.</p>
</td>
</tr>
<tr id="r80ecb3c1002f4d1eade431fecf9551f7"><td class="cellrowborder" valign="top" width="22.06%" headers="mcps1.2.4.1.1 "><p id="a3f531af307d5455b8c27a9f9e358c945"><a name="a3f531af307d5455b8c27a9f9e358c945"></a><a name="a3f531af307d5455b8c27a9f9e358c945"></a>pretty</p>
</td>
<td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.2 "><p id="a7014233960be431db054e5e23abadaae"><a name="a7014233960be431db054e5e23abadaae"></a><a name="a7014233960be431db054e5e23abadaae"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="58.699999999999996%" headers="mcps1.2.4.1.3 "><p id="a991ad6caeb3d461fa123c157c2e47dcf"><a name="a991ad6caeb3d461fa123c157c2e47dcf"></a><a name="a991ad6caeb3d461fa123c157c2e47dcf"></a>If 'true', then the output is pretty printed.</p>
</td>
</tr>
<tr id="rbdfb4603c4bc4ea0b2bfb718f21a4da3"><td class="cellrowborder" valign="top" width="22.06%" headers="mcps1.2.4.1.1 "><p id="a8d767cee22e24e7185439b4bc38368f9"><a name="a8d767cee22e24e7185439b4bc38368f9"></a><a name="a8d767cee22e24e7185439b4bc38368f9"></a>exact</p>
</td>
<td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.2 "><p id="a149b6910e42a452e9e2679855fb1b6e3"><a name="a149b6910e42a452e9e2679855fb1b6e3"></a><a name="a149b6910e42a452e9e2679855fb1b6e3"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="58.699999999999996%" headers="mcps1.2.4.1.3 "><p id="a945d98bb597b4b06b6ee5d9e006a8af0"><a name="a945d98bb597b4b06b6ee5d9e006a8af0"></a><a name="a945d98bb597b4b06b6ee5d9e006a8af0"></a>Should the export be exact. Exact export maintains cluster-specific fields like 'Namespace'.</p>
</td>
</tr>
<tr id="rd52530d8432549da9f6b6fbeb92e04f9"><td class="cellrowborder" valign="top" width="22.06%" headers="mcps1.2.4.1.1 "><p id="a5ce6f9ebc7f542f8be881f16225d0ada"><a name="a5ce6f9ebc7f542f8be881f16225d0ada"></a><a name="a5ce6f9ebc7f542f8be881f16225d0ada"></a>export</p>
</td>
<td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.2 "><p id="af3aa437c6e9f4373a2afb24cd45cdd63"><a name="af3aa437c6e9f4373a2afb24cd45cdd63"></a><a name="af3aa437c6e9f4373a2afb24cd45cdd63"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="58.699999999999996%" headers="mcps1.2.4.1.3 "><p id="a310aae98c91940cfa64dd5691c9ea1db"><a name="a310aae98c91940cfa64dd5691c9ea1db"></a><a name="a310aae98c91940cfa64dd5691c9ea1db"></a>Should this value be exported. Export strips fields that a user cannot specify.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="s870c946f326046289170d757dfdb3866"></a>

N/A

## Response<a name="s386e508d5c284fd3a83b7aab0b783acb"></a>

**Response parameters:**

For the description about response parameters, see  [Table 2](creating-a-persistentvolume.md#tfdb73431f39846d4a56ec4eb558e1617).

**Example response:**

```
{
    "kind": "PersistentVolume",
    "apiVersion": "v1",
    "metadata": {
        "name": "pv-test-02",
        "namespace": "default",
        "selfLink": "/api/v1/namespaces/default/persistentvolumes/pv-test-02",
        "uid": "98efd6aa-920a-11e8-81cc-fa163e49263c",
        "resourceVersion": "5672676",
        "creationTimestamp": "2018-07-28T02:04:44Z",
        "labels":
            "failure-domain.beta.kubernetes.io/region": "eu-de",
            "failure-domain.beta.kubernetes.io/zone": "eu-de-01",
            "name": "pv-test-02"
        },
        "annotations": {
            "volume.beta.kubernetes.io/storage-class": "sata",
            "volume.beta.kubernetes.io/storage-provisioner": "flexvolume-huawei.com/fuxivol"
        }
    },
    "spec": {
        "capacity": {
            "storage": "10Gi"
        },
        "hostPath": {
            "path": "/home",
            "type": ""
        },
        "accessModes": [
            "ReadWriteMany"
        ],
        "persistentVolumeReclaimPolicy": "Delete"
    },
    "status": {
        "phase": "Available"
    }
}
```

## Status Code<a name="sda50de2a2d004d1b9016ed5749e80a29"></a>

[Table 2](#t49c9fb5a3ca549efa601f87efd7502e8)  describes the status code of this API.

**Table  2**  Status code

<a name="t49c9fb5a3ca549efa601f87efd7502e8"></a>
<table><thead align="left"><tr id="r7ed1b859a8014e66b3ba442728c19ce9"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p16859329201717"><a name="p16859329201717"></a><a name="p16859329201717"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="a874b7481035e4ff6bbe5ad7f441758f9"><a name="a874b7481035e4ff6bbe5ad7f441758f9"></a><a name="a874b7481035e4ff6bbe5ad7f441758f9"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r793600e685d64dfe80bc1a36549a33d4"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="a8fd023dd4f7f49ed94ef1bdfa7dd09ed"><a name="a8fd023dd4f7f49ed94ef1bdfa7dd09ed"></a><a name="a8fd023dd4f7f49ed94ef1bdfa7dd09ed"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="a807f97d68e804ff4b8d0fb2c8a84250d"><a name="a807f97d68e804ff4b8d0fb2c8a84250d"></a><a name="a807f97d68e804ff4b8d0fb2c8a84250d"></a>This operation succeeds, and a PersistentVolume resource object is returned.</p>
</td>
</tr>
</tbody>
</table>

For the description about error status codes, see  [Status Code](status-code.md).

