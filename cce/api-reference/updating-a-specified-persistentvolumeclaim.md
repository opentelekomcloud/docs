# Updating a Specified PersistentVolumeClaim<a name="cce_02_0074"></a>

## Function<a name="se00066b4a9cb424d9cb68af31ce81778"></a>

This API is used to update a PersistentVolumeClaim.

The following fields can be updated:

-   metadata.labels
-   metadata.generateName

## URI<a name="sff35d4fc1520499fa4883e120baea67b"></a>

PATCH /api/v1/namespaces/\{namespace\}/persistentvolumeclaims/\{name\}

[Table 1](#t0574ec9a011a40fd8ad96f50202da0a9)  describes the parameters of this API.

**Table  1**  Parameter description

<a name="t0574ec9a011a40fd8ad96f50202da0a9"></a>
<table><thead align="left"><tr id="r545e09c18fb5490096cd420752707835"><th class="cellrowborder" valign="top" width="22.06%" id="mcps1.2.4.1.1"><p id="af1f4480328904e79a9f95edc6ce947f7"><a name="af1f4480328904e79a9f95edc6ce947f7"></a><a name="af1f4480328904e79a9f95edc6ce947f7"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.98%" id="mcps1.2.4.1.2"><p id="p46723325201713"><a name="p46723325201713"></a><a name="p46723325201713"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="60.96%" id="mcps1.2.4.1.3"><p id="p26493003201713"><a name="p26493003201713"></a><a name="p26493003201713"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="rb4214c5a91b54647b39062d92456e676"><td class="cellrowborder" valign="top" width="22.06%" headers="mcps1.2.4.1.1 "><p id="a34c5bb9bd12049e1a54762b6a7aabbc6"><a name="a34c5bb9bd12049e1a54762b6a7aabbc6"></a><a name="a34c5bb9bd12049e1a54762b6a7aabbc6"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.2 "><p id="a97c59b68740645328ca54e29c2f895aa"><a name="a97c59b68740645328ca54e29c2f895aa"></a><a name="a97c59b68740645328ca54e29c2f895aa"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="60.96%" headers="mcps1.2.4.1.3 "><p id="a1a8b0811b5c34e0cbf4bcc20e2860035"><a name="a1a8b0811b5c34e0cbf4bcc20e2860035"></a><a name="a1a8b0811b5c34e0cbf4bcc20e2860035"></a>Name of the PersistentVolumeClaim.</p>
</td>
</tr>
<tr id="r3f4ff43961994f6b99962d788a0f29e6"><td class="cellrowborder" valign="top" width="22.06%" headers="mcps1.2.4.1.1 "><p id="a87cfac4ce16a4d7a9aae0b42f26dcc6e"><a name="a87cfac4ce16a4d7a9aae0b42f26dcc6e"></a><a name="a87cfac4ce16a4d7a9aae0b42f26dcc6e"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.2 "><p id="ad033f82bd957462b91b010bf4032748e"><a name="ad033f82bd957462b91b010bf4032748e"></a><a name="ad033f82bd957462b91b010bf4032748e"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="60.96%" headers="mcps1.2.4.1.3 "><p id="aec96e343964d4cf0a5079e92cc82ea3f"><a name="aec96e343964d4cf0a5079e92cc82ea3f"></a><a name="aec96e343964d4cf0a5079e92cc82ea3f"></a>Object name and auth scope, such as for teams and projects.</p>
</td>
</tr>
<tr id="r9c6f46d583224df6955e5784c08b8c63"><td class="cellrowborder" valign="top" width="22.06%" headers="mcps1.2.4.1.1 "><p id="ab90bece2db9b45a4a9107554b8cd94bf"><a name="ab90bece2db9b45a4a9107554b8cd94bf"></a><a name="ab90bece2db9b45a4a9107554b8cd94bf"></a>pretty</p>
</td>
<td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.2 "><p id="aea00e786055a4d98a6dca409947fb5ed"><a name="aea00e786055a4d98a6dca409947fb5ed"></a><a name="aea00e786055a4d98a6dca409947fb5ed"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="60.96%" headers="mcps1.2.4.1.3 "><p id="a27b0b833722a4d11a54a73089218ee5e"><a name="a27b0b833722a4d11a54a73089218ee5e"></a><a name="a27b0b833722a4d11a54a73089218ee5e"></a>If 'true', then the output is pretty printed.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="sa0d90d294d4e402cb4be966d1d2f86fb"></a>

**Request parameters:**

For the description about the  **Content-Type**  field, see  [Patch Request Method Operation Description](patch-request-method-operation-description.md).

**Example request:**

```
Content-Type: application/merge-patch+json
```

```
{
    "metadata": {
        "labels": {
            "failure-domain.beta.kubernetes.io/region": "eu-de",
            "failure-domain.beta.kubernetes.io/zone": "eu-de-01",
            "app":"mysql"
        }
    }
}
```

## Response<a name="s6c6bf0629d1249f58b3c0b049326c709"></a>

**Response parameters:**

For the description about response parameters, see  [Table 2](creating-a-persistentvolumeclaim.md#t8268aeafde034542ab17a36c7fca65c3).

**Example response:**

-   Example for clusters of v1.15:

    ```
    {
        "kind":"PersistentVolumeClaim",
        "apiVersion":"v1",
        "metadata":{
            "name":"cce-evs-k6m131jj-i1px",
            "namespace":"default",
            "selfLink":"/api/v1/namespaces/default/persistentvolumeclaims/cce-evs-k6m131jj-i1px",
            "uid":"d34f6a93-9eba-4a33-9320-8fa4addd3753",
            "resourceVersion":"2286592",
            "creationTimestamp":"2020-02-14T10:27:43Z",
            "labels":{
                "failure-domain.beta.kubernetes.io/region":"eu-de",
                "failure-domain.beta.kubernetes.io/zone":"eu-de-01"
            },
            "annotations":{
                "everest.io/disk-volume-type":"SATA",
                "pv.kubernetes.io/bind-completed":"yes",
                "pv.kubernetes.io/bound-by-controller":"yes",
                "volume.beta.kubernetes.io/storage-provisioner":"everest-csi-provisioner"
            },
            "finalizers":[
                "kubernetes.io/pvc-protection"
            ]
        },
        "spec":{
            "accessModes":[
                "ReadWriteOnce"
            ],
            "resources":{
                "requests":{
                    "storage":"10Gi"
                }
            },
            "volumeName":"pvc-d34f6a93-9eba-4a33-9320-8fa4addd3753",
            "storageClassName":"csi-disk",
            "volumeMode":"Filesystem"
        },
        "status":{
            "phase":"Bound",
            "accessModes":[
                "ReadWriteOnce"
            ],
            "capacity":{
                "storage":"10Gi"
            }
        }
    }
    ```

-   Example for clusters of v1.13 or earlier:

    ```
    {
        "kind": "PersistentVolumeClaim",
        "apiVersion": "v1",
        "metadata": {
            "name": "db-mysql-0",
            "namespace": "default",
            "selfLink": "/api/v1/namespaces/default/persistentvolumeclaims/db-mysql-0",
            "uid": "9d070d77-8ce1-11e8-8ee0-fa163e49263c",
            "resourceVersion": "4202924",
            "creationTimestamp": "2018-07-21T12:28:46Z",
            "labels": {
                "app": "mysql",
                "failure-domain.beta.kubernetes.io/region": "eu-de",
                "failure-domain.beta.kubernetes.io/zone": "eu-de-01"
            },
            "annotations": {
                "pv.kubernetes.io/bind-completed": "yes",
                "pv.kubernetes.io/bound-by-controller": "yes",
                "volume.beta.kubernetes.io/storage-class": "sata",
                "volume.beta.kubernetes.io/storage-provisioner": "flexvolume-huawei.com/fuxivol"
            }
        },
        "spec": {
            "accessModes": [
                "ReadWriteMany"
            ],
            "resources": {
                "requests": {
                    "storage": "5Gi"
                }
            },
            "volumeName": "pvc-9d070d77-8ce1-11e8-8ee0-fa163e49263c",
            "volumeNamespace": "default"
        },
        "status": {
            "phase": "Bound",
            "accessModes": [
                "ReadWriteMany"
            ],
            "capacity": {
                "storage": "5Gi"
            }
        }
    }
    ```


## Status Code<a name="s800fc422a2ea4527bad9e1828fcea6e1"></a>

[Table 2](#ta79a4737936f4bdcb1d32582427d705a)  describes the status code of this API.

**Table  2**  Status code

<a name="ta79a4737936f4bdcb1d32582427d705a"></a>
<table><thead align="left"><tr id="rc27c5c4693b9464fafb369c0343cc98a"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p15466013201713"><a name="p15466013201713"></a><a name="p15466013201713"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p44787545201713"><a name="p44787545201713"></a><a name="p44787545201713"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r21695d833be74934b7fa7b21618fd110"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="ab2de9cf35f9644588ef1efc1107831c4"><a name="ab2de9cf35f9644588ef1efc1107831c4"></a><a name="ab2de9cf35f9644588ef1efc1107831c4"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="ae7f83f60916741ceaf33944da173498a"><a name="ae7f83f60916741ceaf33944da173498a"></a><a name="ae7f83f60916741ceaf33944da173498a"></a>This operation succeeds, and a PersistentVolumeClaim resource object is returned.</p>
</td>
</tr>
</tbody>
</table>

For the description about error status codes, see  [Status Code](status-code.md).

