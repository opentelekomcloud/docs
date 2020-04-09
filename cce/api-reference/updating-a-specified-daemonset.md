# Updating a Specified DaemonSet<a name="cce_02_0138"></a>

## Function<a name="section24346747"></a>

This API is used to update a DaemonSet object under a specified Namespace.

The following fields can be updated:

-   metadata.selfLink
-   metadata.resourceVersion
-   metadata.generation
-   metadata.creationTimestamp
-   metadata.labels
-   spec.selector
-   spec.template.spec.containers
-   spec.templateGeneration
-   spec.revisionHistoryLimit

The other fields cannot be updated.

## URI<a name="section17794137"></a>

PUT /apis/apps/v1/namespaces/\{namespace\}/daemonsets/\{name\} \(Supports only1.9\)

PATCH /apis/extensions/v1beta1/namespaces/\{namespace\}/daemonsets/\{name\} \(Compatible\)

[Table 1](#d0e32763)  describes the parameters of this API.

**Table  1**  Parameter description

<a name="d0e32763"></a>
<table><thead align="left"><tr id="row94420231206"><th class="cellrowborder" valign="top" width="17.580000000000002%" id="mcps1.2.4.1.1"><p id="p65652297517"><a name="p65652297517"></a><a name="p65652297517"></a>Parameters</p>
</th>
<th class="cellrowborder" valign="top" width="16.950000000000003%" id="mcps1.2.4.1.2"><p id="p165661629135114"><a name="p165661629135114"></a><a name="p165661629135114"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.47%" id="mcps1.2.4.1.3"><p id="p14567629115114"><a name="p14567629115114"></a><a name="p14567629115114"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row7450233011"><td class="cellrowborder" valign="top" width="17.580000000000002%" headers="mcps1.2.4.1.1 "><p id="p30962572"><a name="p30962572"></a><a name="p30962572"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.950000000000003%" headers="mcps1.2.4.1.2 "><p id="p24940388"><a name="p24940388"></a><a name="p24940388"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.47%" headers="mcps1.2.4.1.3 "><p id="p6905524"><a name="p6905524"></a><a name="p6905524"></a>name of the DaemonSet</p>
</td>
</tr>
<tr id="row74592314010"><td class="cellrowborder" valign="top" width="17.580000000000002%" headers="mcps1.2.4.1.1 "><p id="p962641"><a name="p962641"></a><a name="p962641"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="16.950000000000003%" headers="mcps1.2.4.1.2 "><p id="p10865110"><a name="p10865110"></a><a name="p10865110"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.47%" headers="mcps1.2.4.1.3 "><p id="p7658703"><a name="p7658703"></a><a name="p7658703"></a>object name and auth scope, such as for teams and projects</p>
</td>
</tr>
<tr id="row4452023403"><td class="cellrowborder" valign="top" width="17.580000000000002%" headers="mcps1.2.4.1.1 "><p id="p13159118"><a name="p13159118"></a><a name="p13159118"></a>pretty</p>
</td>
<td class="cellrowborder" valign="top" width="16.950000000000003%" headers="mcps1.2.4.1.2 "><p id="p59255609"><a name="p59255609"></a><a name="p59255609"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="65.47%" headers="mcps1.2.4.1.3 "><p id="p34975029"><a name="p34975029"></a><a name="p34975029"></a>If 'true', then the output is pretty printed.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section25929511"></a>

**Request parameters**:

For the description about the  **Content-Type** message header, see section [Patch Request Method Operation Description](patch-request-method-operation-description.md).

**Example request**:

```
Content-Type: application/json-patch+json
```

```
[
    {
        "op": "add",
        "path": "/spec/template/spec/containers/0/image",
        "value": "172.16.5.235:20202/test/redis:latest"
    }
]
```

## Response<a name="section32039015"></a>

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
        "selfLink": "/apis/extensions/v1beta1/namespaces/ns-12130306-s/daemonsets/ds-12130306",
        "uid": "dc72a82b-dfb3-11e7-9c19-fa163e2d897b",
        "resourceVersion": "419012",
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

## Status Code<a name="section19915680"></a>

[Table 2](#d0e32851)  describes the status code of this API.

**Table  2**  Status code

<a name="d0e32851"></a>
<table><thead align="left"><tr id="row58580616171015"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p9676191"><a name="p9676191"></a><a name="p9676191"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p45574026"><a name="p45574026"></a><a name="p45574026"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3769153171015"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p41199681"><a name="p41199681"></a><a name="p41199681"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p48839902"><a name="p48839902"></a><a name="p48839902"></a>This operation succeeds, and a DaemonSet resource object is returned.</p>
</td>
</tr>
</tbody>
</table>

For the description about status codes, see  [Status Code](status-code.md).

