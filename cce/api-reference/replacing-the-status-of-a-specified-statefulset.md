# Replacing the Status of a Specified StatefulSet<a name="cce_02_0151"></a>

## Function<a name="section50502051"></a>

This API is used to replace the status of a specified StatefulSet object under a specified Namespace, that is, to modify the parameter values of the  **status**  field of the StatefulSet object.

## URI<a name="section51865283"></a>

PUT /apis/apps/v1/namespaces/\{namespace\}/statefulsets/\{name\}/status \(Supports only1.9\)

PUT /apis/apps/v1beta1/namespaces/\{namespace\}/statefulsets/\{name\}/status \(Compatible\)

[Table 1](#d0e39176)  describes the parameters of this API.

**Table  1**  Parameter description

<a name="d0e39176"></a>
<table><thead align="left"><tr id="row2074176211829"><th class="cellrowborder" valign="top" width="20.560000000000002%" id="mcps1.2.4.1.1"><p id="p65652297517"><a name="p65652297517"></a><a name="p65652297517"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.6%" id="mcps1.2.4.1.2"><p id="p165661629135114"><a name="p165661629135114"></a><a name="p165661629135114"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="62.839999999999996%" id="mcps1.2.4.1.3"><p id="p14567629115114"><a name="p14567629115114"></a><a name="p14567629115114"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1441474611829"><td class="cellrowborder" valign="top" width="20.560000000000002%" headers="mcps1.2.4.1.1 "><p id="p28539942"><a name="p28539942"></a><a name="p28539942"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.6%" headers="mcps1.2.4.1.2 "><p id="p30033962"><a name="p30033962"></a><a name="p30033962"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="62.839999999999996%" headers="mcps1.2.4.1.3 "><p id="p16831887"><a name="p16831887"></a><a name="p16831887"></a>Name of the StatefulSet.</p>
</td>
</tr>
<tr id="row32867931172518"><td class="cellrowborder" valign="top" width="20.560000000000002%" headers="mcps1.2.4.1.1 "><p id="p56632934"><a name="p56632934"></a><a name="p56632934"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="16.6%" headers="mcps1.2.4.1.2 "><p id="p23864947"><a name="p23864947"></a><a name="p23864947"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="62.839999999999996%" headers="mcps1.2.4.1.3 "><p id="p54012573"><a name="p54012573"></a><a name="p54012573"></a>Object name and auth scope, such as for teams and projects.</p>
</td>
</tr>
<tr id="row608477501011"><td class="cellrowborder" valign="top" width="20.560000000000002%" headers="mcps1.2.4.1.1 "><p id="p49371687"><a name="p49371687"></a><a name="p49371687"></a>pretty</p>
</td>
<td class="cellrowborder" valign="top" width="16.6%" headers="mcps1.2.4.1.2 "><p id="p39683735"><a name="p39683735"></a><a name="p39683735"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="62.839999999999996%" headers="mcps1.2.4.1.3 "><p id="p60265984"><a name="p60265984"></a><a name="p60265984"></a>If 'true', then the output is pretty printed.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section64134368"></a>

**Request parameters:**

For the description about request parameters, see  [Table 2](creating-a-statefulset.md#d0e37568).

**Example request**:

```
{
    "apiVersion": "apps/v1beta1",
    "kind": "StatefulSet",
    "metadata": {
        "generateName": "sz",
        "name": "numberlimit",
        "namespace": "default"
    },
    "spec": {
        "replicas": 1,
        "serviceName": "service-number",
        "template": {
            "metadata": {
                "labels": {
                    "app": "mysql"
                }
            },
            "spec": {
                "containers": [
                    {
                        "image": "10.154.52.159:443/test/mongo:latest",
                        "imagePullPolicy": "IfNotPresent",
                        "name": "container01",
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
                                "cpu": "0.3G"
                            }
                        },
                        "terminationMessagePath": "/dev/termination-log"
                    }
                ]
            }
        }
    },
    "status": {
        "replicas": 3
    }
}
```

## Response<a name="section40338403"></a>

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
        "resourceVersion": "1399495",
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

## Status Code<a name="section27501309"></a>

[Table 2](#d0e39265)  describes the status code of this API.

**Table  2**  Status code

<a name="d0e39265"></a>
<table><thead align="left"><tr id="row58580616171015"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p21773275"><a name="p21773275"></a><a name="p21773275"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p18804863"><a name="p18804863"></a><a name="p18804863"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3769153171015"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p32614431"><a name="p32614431"></a><a name="p32614431"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p24523244"><a name="p24523244"></a><a name="p24523244"></a>This operation succeeds, and a StatefulSet resource object is returned.</p>
</td>
</tr>
</tbody>
</table>

For the description about status codes, see  [Status Code](status-code.md).

