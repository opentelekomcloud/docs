# Reading the Status of a Specified DaemonSet<a name="cce_02_0137"></a>

## Function<a name="section8900016"></a>

This API is used to read the status of a specified DaemonSet object under a specified Namespace.

## URI<a name="section12991283"></a>

GET /apis/apps/v1/namespaces/\{namespace\}/daemonsets/\{name\}/status \(Supports only1.9\)

GET /apis/extensions/v1beta1/namespaces/\{namespace\}/daemonsets/\{name\}/status \(Compatible\)

[Table 1](#d0e32595)  describes the parameters of this API.

**Table  1**  Parameter description

<a name="d0e32595"></a>
<table><thead align="left"><tr id="row298911354615"><th class="cellrowborder" valign="top" width="18.38%" id="mcps1.2.4.1.1"><p id="p65652297517"><a name="p65652297517"></a><a name="p65652297517"></a>Parameters</p>
</th>
<th class="cellrowborder" valign="top" width="16.950000000000003%" id="mcps1.2.4.1.2"><p id="p165661629135114"><a name="p165661629135114"></a><a name="p165661629135114"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="64.67%" id="mcps1.2.4.1.3"><p id="p14567629115114"><a name="p14567629115114"></a><a name="p14567629115114"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row699016315465"><td class="cellrowborder" valign="top" width="18.38%" headers="mcps1.2.4.1.1 "><p id="p36926006"><a name="p36926006"></a><a name="p36926006"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.950000000000003%" headers="mcps1.2.4.1.2 "><p id="p38216549"><a name="p38216549"></a><a name="p38216549"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="64.67%" headers="mcps1.2.4.1.3 "><p id="p8532797"><a name="p8532797"></a><a name="p8532797"></a>name of the DaemonSet</p>
</td>
</tr>
<tr id="row139901935467"><td class="cellrowborder" valign="top" width="18.38%" headers="mcps1.2.4.1.1 "><p id="p46393742"><a name="p46393742"></a><a name="p46393742"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="16.950000000000003%" headers="mcps1.2.4.1.2 "><p id="p66905650"><a name="p66905650"></a><a name="p66905650"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="64.67%" headers="mcps1.2.4.1.3 "><p id="p50648570"><a name="p50648570"></a><a name="p50648570"></a>object name and auth scope, such as for teams and projects</p>
</td>
</tr>
<tr id="row169901732467"><td class="cellrowborder" valign="top" width="18.38%" headers="mcps1.2.4.1.1 "><p id="p12932809"><a name="p12932809"></a><a name="p12932809"></a>pretty</p>
</td>
<td class="cellrowborder" valign="top" width="16.950000000000003%" headers="mcps1.2.4.1.2 "><p id="p40924636"><a name="p40924636"></a><a name="p40924636"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="64.67%" headers="mcps1.2.4.1.3 "><p id="p26561199"><a name="p26561199"></a><a name="p26561199"></a>If 'true', then the output is pretty printed.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section49812686"></a>

N/A

## Response<a name="section45660994"></a>

**Response parameters:**

For the description about response parameters, see  [Table 2](creating-a-daemonset.md#d0e31376)

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
        "numberAvailable": 1
    }
}
```

## Status Code<a name="section8295769"></a>

[Table 2](#d0e32673)  describes the status code of this API.

**Table  2**  Status code

<a name="d0e32673"></a>
<table><thead align="left"><tr id="row58580616171015"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p45288850"><a name="p45288850"></a><a name="p45288850"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p44518222"><a name="p44518222"></a><a name="p44518222"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3769153171015"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p26278426"><a name="p26278426"></a><a name="p26278426"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p48177787"><a name="p48177787"></a><a name="p48177787"></a>This operation succeeds, and a DaemonSet resource object is returned.</p>
</td>
</tr>
</tbody>
</table>

For the description about status codes, see  [Status Code](status-code.md).

