# Updating the Status of a Specified StatefulSet<a name="cce_02_0155"></a>

## Function<a name="section6571668"></a>

This API is used to update the status of a specified StatefulSet object under a specified Namespace.

## URI<a name="section59145013"></a>

PATCH /apis/apps/v1/namespaces/\{namespace\}/statefulsets/\{name\}/status \(Supports only1.9\)

PATCH /apis/apps/v1beta1/namespaces/\{namespace\}/statefulsets/\{name\}/status \(Compatible\)

[Table 1](#d0e39989)  describes the parameters of this API.

**Table  1**  Parameter description

<a name="d0e39989"></a>
<table><thead align="left"><tr id="row2074176211829"><th class="cellrowborder" valign="top" width="22.06%" id="mcps1.2.4.1.1"><p id="p65652297517"><a name="p65652297517"></a><a name="p65652297517"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15.1%" id="mcps1.2.4.1.2"><p id="p165661629135114"><a name="p165661629135114"></a><a name="p165661629135114"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="62.839999999999996%" id="mcps1.2.4.1.3"><p id="p14567629115114"><a name="p14567629115114"></a><a name="p14567629115114"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1441474611829"><td class="cellrowborder" valign="top" width="22.06%" headers="mcps1.2.4.1.1 "><p id="p12234054"><a name="p12234054"></a><a name="p12234054"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="15.1%" headers="mcps1.2.4.1.2 "><p id="p51434319"><a name="p51434319"></a><a name="p51434319"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="62.839999999999996%" headers="mcps1.2.4.1.3 "><p id="p5430345"><a name="p5430345"></a><a name="p5430345"></a>Name of the StatefulSet.</p>
</td>
</tr>
<tr id="row32867931172518"><td class="cellrowborder" valign="top" width="22.06%" headers="mcps1.2.4.1.1 "><p id="p66407998"><a name="p66407998"></a><a name="p66407998"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="15.1%" headers="mcps1.2.4.1.2 "><p id="p10338728"><a name="p10338728"></a><a name="p10338728"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="62.839999999999996%" headers="mcps1.2.4.1.3 "><p id="p32130622"><a name="p32130622"></a><a name="p32130622"></a>Object name and auth scope, such as for teams and projects.</p>
</td>
</tr>
<tr id="row6089515610654"><td class="cellrowborder" valign="top" width="22.06%" headers="mcps1.2.4.1.1 "><p id="p2230586"><a name="p2230586"></a><a name="p2230586"></a>pretty</p>
</td>
<td class="cellrowborder" valign="top" width="15.1%" headers="mcps1.2.4.1.2 "><p id="p46459807"><a name="p46459807"></a><a name="p46459807"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="62.839999999999996%" headers="mcps1.2.4.1.3 "><p id="p5148045"><a name="p5148045"></a><a name="p5148045"></a>If 'true', then the output is pretty printed.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section62543072"></a>

**Request parameters**:

For the description about request parameters, see  [Patch Request Method Operation Description](patch-request-method-operation-description.md).

**Example request**:

```
Content-Type: application/json-patch+json
```

```
[
    {
        "op": "replace",
        "path": "/status/replicas",
        "value": 3
    }
]
```

## Response<a name="section26016743"></a>

**Response parameters:**

For the description about response parameters, see  [Table 2](creating-a-statefulset.md#d0e37568).

**Example response:**

```
{
    "kind": "StatefulSet",
    "apiVersion": "apps/v1beta1",
    "metadata": {
        "name": "numberlimit",
        "generateName": "sz",
        "namespace": "default",
        "selfLink": "/apis/apps/v1beta1/namespaces/default/statefulsets/numberlimit/status",
        "uid": "841f6be1-2a25-11e7-a2a3-fa163e3a4289",
        "resourceVersion": "1399731",
        "generation": 3,
        "creationTimestamp": "2017-04-26T02:10:27Z",
        "labels": {
            "app": "mysql"
        }
    },
    "spec": {
        "replicas": 1,
        "selector": {
            "matchLabels": {
                "app": "mysql"
            }
        },
        "template": {
            "metadata": {
                "creationTimestamp": null,
                "labels": {
                    "app": "mysql"
                }
            },
            "spec": {
                "containers": [
                    {
                        "name": "container01",
                        "image": "10.154.52.159:443/test/mongo:latest",
                        "ports": [
                            {
                                "containerPort": 80,
                                "protocol": "TCP"
                            }
                        ],
                        "resources": {
                            "limits": {
                                "cpu": "99M"
                            },
                            "requests": {
                                "cpu": "300M"
                            }
                        },
                        "terminationMessagePath": "/dev/termination-log",
                        "imagePullPolicy": "IfNotPresent"
                    }
                ],
                "restartPolicy": "Always",
                "terminationGracePeriodSeconds": 30,
                "dnsPolicy": "ClusterFirst",
                "securityContext": {}
            }
        },
        "serviceName": "service-number"
    },
    "status": {
        "replicas": 3
    }
}
```

## Status Code<a name="section32824097"></a>

[Table 2](#d0e40081)  describes the status code of this API.

**Table  2**  Status code

<a name="d0e40081"></a>
<table><thead align="left"><tr id="row58580616171015"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p48527143"><a name="p48527143"></a><a name="p48527143"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p38384488"><a name="p38384488"></a><a name="p38384488"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3769153171015"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p48173793"><a name="p48173793"></a><a name="p48173793"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p9763176"><a name="p9763176"></a><a name="p9763176"></a>This operation succeeds, and a StatefulSet resource object is returned.</p>
</td>
</tr>
</tbody>
</table>

For the description about status codes, see  [Status Code](status-code.md).

