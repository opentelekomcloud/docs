# Reading a Specified StatefulSet<a name="cce_02_0148"></a>

## Function<a name="section15132207"></a>

This API is used to read a StatefulSet object under a specified Namespace.

## URI<a name="section1972143"></a>

GET /apis/apps/v1/namespaces/\{namespace\}/statefulsets/\{name\} \(Supports only1.9\)

GET /apis/apps/v1beta1/namespaces/\{namespace\}/statefulsets/\{name\} \(Compatible\)

[Table 1](#d0e38675)  describes the parameters of this API.

**Table  1**  Parameter description

<a name="d0e38675"></a>
<table><thead align="left"><tr id="row2074176211829"><th class="cellrowborder" valign="top" width="20.93%" id="mcps1.2.4.1.1"><p id="p65652297517"><a name="p65652297517"></a><a name="p65652297517"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.23%" id="mcps1.2.4.1.2"><p id="p165661629135114"><a name="p165661629135114"></a><a name="p165661629135114"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="62.839999999999996%" id="mcps1.2.4.1.3"><p id="p14567629115114"><a name="p14567629115114"></a><a name="p14567629115114"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1441474611829"><td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.2.4.1.1 "><p id="p1508084"><a name="p1508084"></a><a name="p1508084"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.23%" headers="mcps1.2.4.1.2 "><p id="p55045998"><a name="p55045998"></a><a name="p55045998"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="62.839999999999996%" headers="mcps1.2.4.1.3 "><p id="p29540844"><a name="p29540844"></a><a name="p29540844"></a>Name of the StatefulSet.</p>
</td>
</tr>
<tr id="row32867931172518"><td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.2.4.1.1 "><p id="p60439184"><a name="p60439184"></a><a name="p60439184"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="16.23%" headers="mcps1.2.4.1.2 "><p id="p63735753"><a name="p63735753"></a><a name="p63735753"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="62.839999999999996%" headers="mcps1.2.4.1.3 "><p id="p62322338"><a name="p62322338"></a><a name="p62322338"></a>Object name and auth scope, such as for teams and projects.</p>
</td>
</tr>
<tr id="row7878773212658"><td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.2.4.1.1 "><p id="p283486"><a name="p283486"></a><a name="p283486"></a>pretty</p>
</td>
<td class="cellrowborder" valign="top" width="16.23%" headers="mcps1.2.4.1.2 "><p id="p22962431"><a name="p22962431"></a><a name="p22962431"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="62.839999999999996%" headers="mcps1.2.4.1.3 "><p id="p48017661"><a name="p48017661"></a><a name="p48017661"></a>If 'true', then the output is pretty printed.</p>
</td>
</tr>
<tr id="row1564701821274"><td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.2.4.1.1 "><p id="p41157182"><a name="p41157182"></a><a name="p41157182"></a>exact</p>
</td>
<td class="cellrowborder" valign="top" width="16.23%" headers="mcps1.2.4.1.2 "><p id="p45397409"><a name="p45397409"></a><a name="p45397409"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="62.839999999999996%" headers="mcps1.2.4.1.3 "><p id="p53311550"><a name="p53311550"></a><a name="p53311550"></a>Should the export be exact. Exact export maintains cluster-specific fields like 'Namespace'.</p>
</td>
</tr>
<tr id="row1692500521277"><td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.2.4.1.1 "><p id="p8087957"><a name="p8087957"></a><a name="p8087957"></a>export</p>
</td>
<td class="cellrowborder" valign="top" width="16.23%" headers="mcps1.2.4.1.2 "><p id="p51144774"><a name="p51144774"></a><a name="p51144774"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="62.839999999999996%" headers="mcps1.2.4.1.3 "><p id="p49085995"><a name="p49085995"></a><a name="p49085995"></a>Should this value be exported. Export strips fields that a user cannot specify.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section17749294"></a>

N/A

## Response<a name="section25525926"></a>

**Response parameters:**

For the description about response parameters, see  [Table 2](creating-a-statefulset.md#d0e37568).

**Example response**:

```
{
    "kind": "StatefulSet",
    "apiVersion": "apps/v1beta1",
    "metadata": {
        "name": "mysql",
        "generateName": "sz",
        "namespace": "default",
        "selfLink": "/apis/apps/v1beta1/namespaces/default/statefulsets/mysql",
        "uid": "f5cf50f5-23fc-11e7-9c83-fa163ec08232",
        "resourceVersion": "1808945",
        "generation": 1,
        "creationTimestamp": "2017-04-18T06:05:02Z",
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
                "name": "-sz",
                "creationTimestamp": null,
                "labels": {
                    "app": "mysql"
                }
            },
            "spec": {
                "containers": [
                    {
                        "name": "container01",
                        "image": "10.154.52.159:443/test/nginx:latest",
                        "ports": [
                            {
                                "containerPort": 80,
                                "protocol": "TCP"
                            }
                        ],
                        "resources": {},
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
        "volumeClaimTemplates": [
            {
                "metadata": {
                    "name": "db",
                    "creationTimestamp": null
                },
                "spec": {
                    "accessModes": [
                        "ReadWriteOnce"
                    ],
                    "resources": {
                        "requests": {
                            "storage": "1Gi"
                        }
                    }
                },
                "status": {
                    "phase": "Pending"
                }
            }
        ],
        "serviceName": "mysql-service"
    },
    "status": {
        "replicas": 1
    }
}
```

## Status Code<a name="section28406742"></a>

[Table 2](#d0e38773)  describes the status code of this API.

**Table  2**  Status code

<a name="d0e38773"></a>
<table><thead align="left"><tr id="row58580616171015"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p60271674"><a name="p60271674"></a><a name="p60271674"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p50167450"><a name="p50167450"></a><a name="p50167450"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3769153171015"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p46775020"><a name="p46775020"></a><a name="p46775020"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p30680237"><a name="p30680237"></a><a name="p30680237"></a>This operation succeeds, and a StatefulSet resource object is returned.</p>
</td>
</tr>
</tbody>
</table>

For the description about status codes, see  [Status Code](status-code.md).

