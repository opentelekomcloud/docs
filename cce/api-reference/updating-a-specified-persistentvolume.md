# Updating a Specified PersistentVolume<a name="cce_02_0082"></a>

## Function<a name="sf73a650b6a444b9ba3c103ce0b66d6d5"></a>

This API is used to update a PersistentVolume.

The following fields can be updated:

-   metadata.labels
-   metadata.generateName
-   spec.accessModes
-   spec.capacity
-   spec.persistentVolumeReclaimPolicy

## URI<a name="sf1dc882c095a4a6f8992f9e1a42fdf50"></a>

PATCH /api/v1/persistentvolumes/\{name\}

[Table 1](#t4a3d4744a32d4acdb19c5f63c2e3dd20)  describes the parameters of this API.

**Table  1**  Parameter description

<a name="t4a3d4744a32d4acdb19c5f63c2e3dd20"></a>
<table><thead align="left"><tr id="rfa0875bb6a95415c82e1d32e3bfbc4c5"><th class="cellrowborder" valign="top" width="22.06%" id="mcps1.2.4.1.1"><p id="ac04929e39d6443719b17153edd2baa6b"><a name="ac04929e39d6443719b17153edd2baa6b"></a><a name="ac04929e39d6443719b17153edd2baa6b"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.919999999999998%" id="mcps1.2.4.1.2"><p id="p2951269201731"><a name="p2951269201731"></a><a name="p2951269201731"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="60.019999999999996%" id="mcps1.2.4.1.3"><p id="p37726225201731"><a name="p37726225201731"></a><a name="p37726225201731"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r8d9c36a771724e518bffab5d29f6ee1b"><td class="cellrowborder" valign="top" width="22.06%" headers="mcps1.2.4.1.1 "><p id="a555771c040784d6a8fa8814934e8984a"><a name="a555771c040784d6a8fa8814934e8984a"></a><a name="a555771c040784d6a8fa8814934e8984a"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="17.919999999999998%" headers="mcps1.2.4.1.2 "><p id="a85bd579a2ce54f89ae5ce9ca08135b96"><a name="a85bd579a2ce54f89ae5ce9ca08135b96"></a><a name="a85bd579a2ce54f89ae5ce9ca08135b96"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="60.019999999999996%" headers="mcps1.2.4.1.3 "><p id="afa7585b5ff154d04b34f3514525fd3b0"><a name="afa7585b5ff154d04b34f3514525fd3b0"></a><a name="afa7585b5ff154d04b34f3514525fd3b0"></a>Name of the PersistentVolume.</p>
</td>
</tr>
<tr id="r4838ad594d0e4d65a446f3144fbf6e83"><td class="cellrowborder" valign="top" width="22.06%" headers="mcps1.2.4.1.1 "><p id="a2987180e58b14a7eb3cf3cee3febcb2f"><a name="a2987180e58b14a7eb3cf3cee3febcb2f"></a><a name="a2987180e58b14a7eb3cf3cee3febcb2f"></a>pretty</p>
</td>
<td class="cellrowborder" valign="top" width="17.919999999999998%" headers="mcps1.2.4.1.2 "><p id="a336551b95abb4f32853050ceb8904b60"><a name="a336551b95abb4f32853050ceb8904b60"></a><a name="a336551b95abb4f32853050ceb8904b60"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="60.019999999999996%" headers="mcps1.2.4.1.3 "><p id="ae6af284c06664514ba0276d82f7b952d"><a name="ae6af284c06664514ba0276d82f7b952d"></a><a name="ae6af284c06664514ba0276d82f7b952d"></a>If 'true', then the output is pretty printed.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="s52cab53f2b52447d8d9dd6f9d24e550e"></a>

**Request parameters:**

For the description about the  **Content-Type**  field, see  [Patch Request Method Operation Description](patch-request-method-operation-description.md).

**Example request:**

```
Content-Type: application/json-patch+json
[
    {
        "op": "add",
        "path": "/spec/persistentVolumeReclaimPolicy",
        "value": "Retain"
    }
]
```

## Response<a name="s0cde720189a34695b15f116a711b70c9"></a>

**Response parameters:**

For the description about response parameters, see  [Table 2](creating-a-persistentvolume.md#tfdb73431f39846d4a56ec4eb558e1617).

**Example response:**

```
{
    "kind": "PersistentVolume",
    "apiVersion": "v1",
    "metadata": {
        "name": "pv-test-03",
        "namespace": "default",
        "selfLink": "/api/v1/namespaces/default/persistentvolumes/pv-test-03",
        "uid": "45eb3e76-9212-11e8-8cd0-fa163e082286",
        "resourceVersion": "5690537",
        "creationTimestamp": "2018-07-28T02:59:41Z",
        "labels": {
            "failure-domain.beta.kubernetes.io/region": "eu-de",
            "failure-domain.beta.kubernetes.io/zone": "eu-de-01",
            "name": "pv-test-03"
        },
        "annotations": {
            "volume.beta.kubernetes.io/storage-class": "sata",
            "volume.beta.kubernetes.io/storage-provisioner": "flexvolume-huawei.com/fuxivol"
        }
    },
    "spec": {
        "capacity": {
            "storage": "20Gi"
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

## Status Code<a name="s52cc52d636374150a319ab8a943a72e6"></a>

[Table 2](#t00c0806bba8842b097224b11d277e83a)  describes the status code of this API.

**Table  2**  Status code

<a name="t00c0806bba8842b097224b11d277e83a"></a>
<table><thead align="left"><tr id="r0ce9dfb00d75450b83caab4ba601192e"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p44027343201731"><a name="p44027343201731"></a><a name="p44027343201731"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p9445060201731"><a name="p9445060201731"></a><a name="p9445060201731"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="rb482670905b549f0b5aecb7033bd8da5"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="a8f694a79c0ab440d990e01a9ef53d834"><a name="a8f694a79c0ab440d990e01a9ef53d834"></a><a name="a8f694a79c0ab440d990e01a9ef53d834"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="afe847dde41094b3cbc31b161d021a0ab"><a name="afe847dde41094b3cbc31b161d021a0ab"></a><a name="afe847dde41094b3cbc31b161d021a0ab"></a>This operation succeeds, and a PersistentVolume resource object is returned.</p>
</td>
</tr>
</tbody>
</table>

For the description about error status codes, see  [Status Code](status-code.md).

