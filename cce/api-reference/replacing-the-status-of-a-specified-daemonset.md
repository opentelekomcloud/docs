# Replacing the Status of a Specified DaemonSet<a name="cce_02_0140"></a>

## Function<a name="section12089840"></a>

This API is used to replace the status of a specified DaemonSet object under a specified Namespace, that is, to modify the parameter values of the status field of the DaemonSet object.

## URI<a name="section41699700"></a>

PATCH /apis/apps/v1/namespaces/\{namespace\}/daemonsets/\{name\}/status \(Supports only1.9\)

PUT /apis/extensions/v1beta1/namespaces/\{namespace\}/daemonsets/\{name\}/status \(Compatible\)

[Table 1](#d0e33741)  describes the parameters of this API.

**Table  1**  Parameter description

<a name="d0e33741"></a>
<table><thead align="left"><tr id="row3730929181219"><th class="cellrowborder" valign="top" width="17.45%" id="mcps1.2.4.1.1"><p id="p65652297517"><a name="p65652297517"></a><a name="p65652297517"></a>Parameters</p>
</th>
<th class="cellrowborder" valign="top" width="17.080000000000002%" id="mcps1.2.4.1.2"><p id="p165661629135114"><a name="p165661629135114"></a><a name="p165661629135114"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.47%" id="mcps1.2.4.1.3"><p id="p14567629115114"><a name="p14567629115114"></a><a name="p14567629115114"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row15730172981214"><td class="cellrowborder" valign="top" width="17.45%" headers="mcps1.2.4.1.1 "><p id="p48575428"><a name="p48575428"></a><a name="p48575428"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="17.080000000000002%" headers="mcps1.2.4.1.2 "><p id="p42295582"><a name="p42295582"></a><a name="p42295582"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.47%" headers="mcps1.2.4.1.3 "><p id="p3390137"><a name="p3390137"></a><a name="p3390137"></a>name of the DaemonSet</p>
</td>
</tr>
<tr id="row1373010294121"><td class="cellrowborder" valign="top" width="17.45%" headers="mcps1.2.4.1.1 "><p id="p55491237"><a name="p55491237"></a><a name="p55491237"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="17.080000000000002%" headers="mcps1.2.4.1.2 "><p id="p65605208"><a name="p65605208"></a><a name="p65605208"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.47%" headers="mcps1.2.4.1.3 "><p id="p12421640"><a name="p12421640"></a><a name="p12421640"></a>object name and auth scope, such as for teams and projects</p>
</td>
</tr>
<tr id="row2730829101210"><td class="cellrowborder" valign="top" width="17.45%" headers="mcps1.2.4.1.1 "><p id="p62787967"><a name="p62787967"></a><a name="p62787967"></a>pretty</p>
</td>
<td class="cellrowborder" valign="top" width="17.080000000000002%" headers="mcps1.2.4.1.2 "><p id="p52660581"><a name="p52660581"></a><a name="p52660581"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="65.47%" headers="mcps1.2.4.1.3 "><p id="p37648675"><a name="p37648675"></a><a name="p37648675"></a>If 'true', then the output is pretty printed.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section39752982"></a>

**Request parameters:**

For the description about request parameters, see  [Table 2](creating-a-daemonset.md#d0e31376).

**Example request**:

```
{
    "kind": "DaemonSet",
    "apiVersion": "extensions/v1beta1",
    "metadata": {
        "name": "ds-12130306",
        "namespace": "ns-12130306-s",
        "selfLink": "/apis/extensions/v1beta1/namespaces/ns-12130306-s/daemonsets/ds-12130306/status",
        "uid": "dc72a82b-dfb3-11e7-9c19-fa163e2d897b",
        "resourceVersion": "419052",
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

## Response<a name="section22232519"></a>

**Response parameters:**

For the description about request parameters, see  [Table 2](creating-a-daemonset.md#d0e31376).

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
        "resourceVersion": "419053",
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

## Status Code<a name="section65874944"></a>

[Table 2](#d0e33836)  describes the status code of this API.

**Table  2**  Status code

<a name="d0e33836"></a>
<table><thead align="left"><tr id="row58580616171015"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p7664333"><a name="p7664333"></a><a name="p7664333"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p16831240"><a name="p16831240"></a><a name="p16831240"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3769153171015"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p35685603"><a name="p35685603"></a><a name="p35685603"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p4852691"><a name="p4852691"></a><a name="p4852691"></a>This operation succeeds, and a DaemonSet resource object is returned.</p>
</td>
</tr>
</tbody>
</table>

For the description about status codes, see  [Status Code](status-code.md).

