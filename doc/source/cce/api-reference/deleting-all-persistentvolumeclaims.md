# Deleting All PersistentVolumeClaims<a name="cce_02_0118"></a>

## Function<a name="section14672911"></a>

This API is used to delete all PersistentVolumeClaims.

## URI<a name="section64947336"></a>

DELETE /api/v1/namespaces/\{namespace\}/persistentvolumeclaims

[Table 1](#d0e27629)  describes the parameters of this API.

**Table  1**  Parameter description

<a name="d0e27629"></a>
<table><thead align="left"><tr id="row38917299"><th class="cellrowborder" valign="top" width="22.45%" id="mcps1.2.4.1.1"><p id="p65293496"><a name="p65293496"></a><a name="p65293496"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.33%" id="mcps1.2.4.1.2"><p id="p54281838"><a name="p54281838"></a><a name="p54281838"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="61.22%" id="mcps1.2.4.1.3"><p id="p34752764"><a name="p34752764"></a><a name="p34752764"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row63510539"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.4.1.1 "><p id="p44080067"><a name="p44080067"></a><a name="p44080067"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="16.33%" headers="mcps1.2.4.1.2 "><p id="p13715659"><a name="p13715659"></a><a name="p13715659"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="61.22%" headers="mcps1.2.4.1.3 "><p id="p37226571"><a name="p37226571"></a><a name="p37226571"></a>object name and auth scope, such as for teams and projects</p>
</td>
</tr>
<tr id="row66603688"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.4.1.1 "><p id="p26189648"><a name="p26189648"></a><a name="p26189648"></a>pretty</p>
</td>
<td class="cellrowborder" valign="top" width="16.33%" headers="mcps1.2.4.1.2 "><p id="p40986757"><a name="p40986757"></a><a name="p40986757"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="61.22%" headers="mcps1.2.4.1.3 "><p id="p31593006"><a name="p31593006"></a><a name="p31593006"></a>If 'true', then the output is pretty printed.</p>
</td>
</tr>
<tr id="row15901602"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.4.1.1 "><p id="p12961365"><a name="p12961365"></a><a name="p12961365"></a>fieldSelector</p>
</td>
<td class="cellrowborder" valign="top" width="16.33%" headers="mcps1.2.4.1.2 "><p id="p43237616"><a name="p43237616"></a><a name="p43237616"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="61.22%" headers="mcps1.2.4.1.3 "><p id="p12586012"><a name="p12586012"></a><a name="p12586012"></a>A selector to restrict the list of returned objects by their fields. Defaults to everything.</p>
</td>
</tr>
<tr id="row46165248"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.4.1.1 "><p id="p48397575"><a name="p48397575"></a><a name="p48397575"></a>includeUninitialized</p>
</td>
<td class="cellrowborder" valign="top" width="16.33%" headers="mcps1.2.4.1.2 "><p id="p27889523"><a name="p27889523"></a><a name="p27889523"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="61.22%" headers="mcps1.2.4.1.3 "><p id="p44458924"><a name="p44458924"></a><a name="p44458924"></a>If true, partially initialized resources are included in the response.</p>
</td>
</tr>
<tr id="row64586001"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.4.1.1 "><p id="p64083559"><a name="p64083559"></a><a name="p64083559"></a>labelSelector</p>
</td>
<td class="cellrowborder" valign="top" width="16.33%" headers="mcps1.2.4.1.2 "><p id="p23385790"><a name="p23385790"></a><a name="p23385790"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="61.22%" headers="mcps1.2.4.1.3 "><p id="p15200829"><a name="p15200829"></a><a name="p15200829"></a>A selector to restrict the list of returned objects by their labels. Defaults to everything.</p>
</td>
</tr>
<tr id="row2589740"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.4.1.1 "><p id="p8442363"><a name="p8442363"></a><a name="p8442363"></a>resourceVersion</p>
</td>
<td class="cellrowborder" valign="top" width="16.33%" headers="mcps1.2.4.1.2 "><p id="p12742791"><a name="p12742791"></a><a name="p12742791"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="61.22%" headers="mcps1.2.4.1.3 "><p id="p25533111"><a name="p25533111"></a><a name="p25533111"></a>When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it is 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.</p>
</td>
</tr>
<tr id="row28471408"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.4.1.1 "><p id="p24482706"><a name="p24482706"></a><a name="p24482706"></a>timeoutSeconds</p>
</td>
<td class="cellrowborder" valign="top" width="16.33%" headers="mcps1.2.4.1.2 "><p id="p36942156"><a name="p36942156"></a><a name="p36942156"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="61.22%" headers="mcps1.2.4.1.3 "><p id="p39524679"><a name="p39524679"></a><a name="p39524679"></a>Timeout for the list/watch call.</p>
</td>
</tr>
<tr id="row20177796"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.4.1.1 "><p id="p23788803"><a name="p23788803"></a><a name="p23788803"></a>watch</p>
</td>
<td class="cellrowborder" valign="top" width="16.33%" headers="mcps1.2.4.1.2 "><p id="p47844886"><a name="p47844886"></a><a name="p47844886"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="61.22%" headers="mcps1.2.4.1.3 "><p id="p50230566"><a name="p50230566"></a><a name="p50230566"></a>Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section47655118"></a>

N/A

## Response<a name="section26242881"></a>

**Response parameters:**

For the description about response parameters, see  [Table 2](creating-a-persistentvolumeclaim.md#t8268aeafde034542ab17a36c7fca65c3).

**Example response:**

```
{
    "kind": "PersistentVolumeClaimList",
    "apiVersion": "v1",
    "metadata": {
        "selfLink": "/api/v1/namespaces/default/persistentvolumeclaims",
        "resourceVersion": "4203652"
    },
    "items": [
        {
            "metadata": {
                "name": "db-mysql",
                "namespace": "default",
                "selfLink": "/api/v1/namespaces/default/persistentvolumeclaims/db-mysql",
                "uid": "ac34af93-8cdd-11e8-8ee0-fa163e49263c",
                "resourceVersion": "4197709",
                "creationTimestamp": "2018-07-21T12:00:33Z",
                "labels": {
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
                        "storage": "10Gi"
                    }
                },
                "volumeName": "pvc-ac34af93-8cdd-11e8-8ee0-fa163e49263c",
                "volumeNamespace": "default"
            },
            "status": {
                "phase": "Bound",
                "accessModes": [
                    "ReadWriteMany"
                ],
                "capacity": {
                    "storage": "10Gi"
                }
            }
        }
    ]
}
```

## Status Code<a name="section34859338"></a>

[Table 2](#d0e27756)  describes the status code of this API.

**Table  2**  Status code

<a name="d0e27756"></a>
<table><thead align="left"><tr id="row40798935"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p16379425"><a name="p16379425"></a><a name="p16379425"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p51665068"><a name="p51665068"></a><a name="p51665068"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row24120992"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p7643299"><a name="p7643299"></a><a name="p7643299"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p15127520"><a name="p15127520"></a><a name="p15127520"></a>Delete a DaemonSet resource object successfully.</p>
</td>
</tr>
</tbody>
</table>

For the description about error status codes, see  [Status Code](status-code.md).

