# Reading a Specified DaemonSet<a name="cce_02_0136"></a>

## Function<a name="section49931641"></a>

This API is used to read a DaemonSet object under a specified Namespace.

## URI<a name="section46731593"></a>

GET /apis/apps/v1/namespaces/\{namespace\}/daemonsets/\{name\} \(Supports only1.9\)

GET /apis/extensions/v1beta1/namespaces/\{namespace\}/daemonsets/\{name\} \(Compatible\)

[Table 1](#d0e32428)  describes the parameters of this API.

**Table  1**  Parameter description

<a name="d0e32428"></a>
<table><thead align="left"><tr id="row1048815363016"><th class="cellrowborder" valign="top" width="18.08%" id="mcps1.2.4.1.1"><p id="p65652297517"><a name="p65652297517"></a><a name="p65652297517"></a>Parameters</p>
</th>
<th class="cellrowborder" valign="top" width="17.44%" id="mcps1.2.4.1.2"><p id="p165661629135114"><a name="p165661629135114"></a><a name="p165661629135114"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="64.48%" id="mcps1.2.4.1.3"><p id="p14567629115114"><a name="p14567629115114"></a><a name="p14567629115114"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row348833193011"><td class="cellrowborder" valign="top" width="18.08%" headers="mcps1.2.4.1.1 "><p id="p37820334"><a name="p37820334"></a><a name="p37820334"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p43548195"><a name="p43548195"></a><a name="p43548195"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="64.48%" headers="mcps1.2.4.1.3 "><p id="p37742921"><a name="p37742921"></a><a name="p37742921"></a>Name of the DaemonSet.</p>
</td>
</tr>
<tr id="row114887318300"><td class="cellrowborder" valign="top" width="18.08%" headers="mcps1.2.4.1.1 "><p id="p67064455"><a name="p67064455"></a><a name="p67064455"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p63511806"><a name="p63511806"></a><a name="p63511806"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="64.48%" headers="mcps1.2.4.1.3 "><p id="p44182624"><a name="p44182624"></a><a name="p44182624"></a>Object name and auth scope, such as for teams and projects.</p>
</td>
</tr>
<tr id="row248813133016"><td class="cellrowborder" valign="top" width="18.08%" headers="mcps1.2.4.1.1 "><p id="p63987542"><a name="p63987542"></a><a name="p63987542"></a>pretty</p>
</td>
<td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p15608423"><a name="p15608423"></a><a name="p15608423"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="64.48%" headers="mcps1.2.4.1.3 "><p id="p56322752"><a name="p56322752"></a><a name="p56322752"></a>If 'true', then the output is pretty printed.</p>
</td>
</tr>
<tr id="row34895343010"><td class="cellrowborder" valign="top" width="18.08%" headers="mcps1.2.4.1.1 "><p id="p55770977"><a name="p55770977"></a><a name="p55770977"></a>exact</p>
</td>
<td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p21155287"><a name="p21155287"></a><a name="p21155287"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="64.48%" headers="mcps1.2.4.1.3 "><p id="p35856657"><a name="p35856657"></a><a name="p35856657"></a>Should the export be exact. Exact export maintains cluster-specific fields like 'Namespace'.</p>
</td>
</tr>
<tr id="row74892343019"><td class="cellrowborder" valign="top" width="18.08%" headers="mcps1.2.4.1.1 "><p id="p34155063"><a name="p34155063"></a><a name="p34155063"></a>export</p>
</td>
<td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p15096715"><a name="p15096715"></a><a name="p15096715"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="64.48%" headers="mcps1.2.4.1.3 "><p id="p14874432"><a name="p14874432"></a><a name="p14874432"></a>Should this value be exported. Export strips fields that a user cannot specify.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section17931154"></a>

N/A

## Response<a name="section27162663"></a>

**Response parameters:**

For the description about response parameters, see  [Table 2](creating-a-daemonset.md#d0e31376)

**Example response**

```
{
    "kind": "DaemonSet",
    "apiVersion": "extensions/v1beta1",
    "metadata": {
        "name": "ds-12130306",
        "namespace": "ns-12130306-s",
        "selfLink": "/apis/extensions/v1beta1/namespaces/ns-12130306-s/daemonsets/ds-12130306",
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

## Status Code<a name="section43137375"></a>

[Table 2](#d0e32525)  describes the status code of this API.

**Table  2**  Status code

<a name="d0e32525"></a>
<table><thead align="left"><tr id="row58580616171015"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p31376324"><a name="p31376324"></a><a name="p31376324"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p58454354"><a name="p58454354"></a><a name="p58454354"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3769153171015"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p58971811"><a name="p58971811"></a><a name="p58971811"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p11987382"><a name="p11987382"></a><a name="p11987382"></a>This operation succeeds, and a DaemonSet resource object is returned.</p>
</td>
</tr>
</tbody>
</table>

For the description about status codes, see  [Status Code](status-code.md).

