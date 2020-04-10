# Updating the Status of a Specified DaemonSet<a name="cce_02_0143"></a>

## Function<a name="section47376726"></a>

This API is used to update the status of a specified DaemonSet object under a specified Namespace.

## URI<a name="section23737353"></a>

PUT /apis/apps/v1/namespaces/\{namespace\}/daemonsets/\{name\}/status \(Supports only1.9\)

PATCH /apis/extensions/v1beta1/namespaces/\{namespace\}/daemonsets/\{name\}/status \(Compatible\)

[Table 1](#d0e32918)  describes the parameters of this API.

**Table  1**  Parameter description

<a name="d0e32918"></a>
<table><thead align="left"><tr id="row1175919498713"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="p65652297517"><a name="p65652297517"></a><a name="p65652297517"></a>Parameters</p>
</th>
<th class="cellrowborder" valign="top" width="17.51%" id="mcps1.2.4.1.2"><p id="p165661629135114"><a name="p165661629135114"></a><a name="p165661629135114"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="59.489999999999995%" id="mcps1.2.4.1.3"><p id="p14567629115114"><a name="p14567629115114"></a><a name="p14567629115114"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row675911491676"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p24449721"><a name="p24449721"></a><a name="p24449721"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="17.51%" headers="mcps1.2.4.1.2 "><p id="p34270416"><a name="p34270416"></a><a name="p34270416"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="59.489999999999995%" headers="mcps1.2.4.1.3 "><p id="p24440274"><a name="p24440274"></a><a name="p24440274"></a>name of the DaemonSet</p>
</td>
</tr>
<tr id="row67596491078"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p33111288"><a name="p33111288"></a><a name="p33111288"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="17.51%" headers="mcps1.2.4.1.2 "><p id="p64768681"><a name="p64768681"></a><a name="p64768681"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="59.489999999999995%" headers="mcps1.2.4.1.3 "><p id="p11771810"><a name="p11771810"></a><a name="p11771810"></a>object name and auth scope, such as for teams and projects</p>
</td>
</tr>
<tr id="row97591549176"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p58824435"><a name="p58824435"></a><a name="p58824435"></a>pretty</p>
</td>
<td class="cellrowborder" valign="top" width="17.51%" headers="mcps1.2.4.1.2 "><p id="p49929"><a name="p49929"></a><a name="p49929"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="59.489999999999995%" headers="mcps1.2.4.1.3 "><p id="p4044259"><a name="p4044259"></a><a name="p4044259"></a>If 'true', then the output is pretty printed.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section12309589"></a>

**Request parameters**:

For the description about the  **Content-Type** message header, see section [Patch Request Method Operation Description](patch-request-method-operation-description.md).

**Example request**:

```
Content-Type: application/merge-patch+json
```

```
[
    {
        "op": "add",
        "path": "/status/numberAvailable",
        "value": 2
    }
]
```

## Response<a name="section43677444"></a>

**Response parameters:**

For the description about response parameters, see  [Table 2](creating-a-daemonset.md#d0e31376).

**Example response:**

```
{
    "kind": "DaemonSet",
    "apiVersion": "extensions/v1beta1",
    "metadata": {
        "name": "ds-12130306",
        "namespace": "ns-12130306-s",
        "selfLink": "/apis/extensions/v1beta1/namespaces/ns-12130306-s/daemonsets/ds-12130306/status",
        "uid": "dc72a82b-dfb3-11e7-9c19-fa163e2d897b",
        "resourceVersion": "419051",
        "generation": 1,
        "creationTimestamp": "2017-12-13T03:15:24Z",
        "labels": {
            "name": "daemonset-test"
        },
        "enable": true
    },
    "spec": {
        "selector": {
            "matchLabels": {
                "name": "daemonset-test"
            }
        },
        "template": {
            "metadata": {
                "creationTimestamp": null,
                "labels": {
                    "name": "daemonset-test"
                },
                "enable": true
            },
            "spec": {
                "containers": [
                    {
                        "name": "dscon-12130306",
                        "image": "172.16.5.235:20202/test/redis:latest",
                        "resources": {},
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File",
                        "imagePullPolicy": "IfNotPresent"
                    }
                ],
                "restartPolicy": "Always",
                "terminationGracePeriodSeconds": 30,
                "dnsPolicy": "ClusterFirst",
                "securityContext": {},
                "schedulerName": "default-scheduler"
            }
        },
        "updateStrategy": {
            "type": "OnDelete"
        },
        "templateGeneration": 1,
        "revisionHistoryLimit": 10
    },
    "status": {
        "currentNumberScheduled": 1,
        "numberMisscheduled": 0,
        "desiredNumberScheduled": 1,
        "numberReady": 1,
        "observedGeneration": 1,
        "updatedNumberScheduled": 1,
        "numberAvailable": 2
    }
}
```

## Status Code<a name="section57552677"></a>

[Table 2](#d0e33007)  describes the status code of this API.

**Table  2**  Status code

<a name="d0e33007"></a>
<table><thead align="left"><tr id="row58580616171015"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p39569378"><a name="p39569378"></a><a name="p39569378"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p51003075"><a name="p51003075"></a><a name="p51003075"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3769153171015"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p26385539"><a name="p26385539"></a><a name="p26385539"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p56853938"><a name="p56853938"></a><a name="p56853938"></a>This operation succeeds, and a DaemonSet resource object is returned.</p>
</td>
</tr>
</tbody>
</table>

For the description about status codes, see  [Status Code](status-code.md).

