# Updating the Status of a Specified Job<a name="cce_02_0166"></a>

## Function<a name="section21968375"></a>

This API is used to update the status of a specified Job under a specified Namespace.

## URI<a name="section63497648"></a>

PATCH /apis/batch/v1/namespaces/\{namespace\}/jobs/\{name\}/status

[Table 1](#d0e42516)  describes the parameters of this API.

**Table  1**  Parameter description

<a name="d0e42516"></a>
<table><thead align="left"><tr id="row2074176211829"><th class="cellrowborder" valign="top" width="22.06%" id="mcps1.2.4.1.1"><p id="p65652297517"><a name="p65652297517"></a><a name="p65652297517"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15.1%" id="mcps1.2.4.1.2"><p id="p165661629135114"><a name="p165661629135114"></a><a name="p165661629135114"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="62.839999999999996%" id="mcps1.2.4.1.3"><p id="p14567629115114"><a name="p14567629115114"></a><a name="p14567629115114"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1441474611829"><td class="cellrowborder" valign="top" width="22.06%" headers="mcps1.2.4.1.1 "><p id="p44630865"><a name="p44630865"></a><a name="p44630865"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="15.1%" headers="mcps1.2.4.1.2 "><p id="p58330314"><a name="p58330314"></a><a name="p58330314"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="62.839999999999996%" headers="mcps1.2.4.1.3 "><p id="p27135028"><a name="p27135028"></a><a name="p27135028"></a>Name of the Job.</p>
</td>
</tr>
<tr id="row32867931172518"><td class="cellrowborder" valign="top" width="22.06%" headers="mcps1.2.4.1.1 "><p id="p51430001"><a name="p51430001"></a><a name="p51430001"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="15.1%" headers="mcps1.2.4.1.2 "><p id="p5080523"><a name="p5080523"></a><a name="p5080523"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="62.839999999999996%" headers="mcps1.2.4.1.3 "><p id="p8869201"><a name="p8869201"></a><a name="p8869201"></a>Object name and auth scope, such as for teams and projects.</p>
</td>
</tr>
<tr id="row6089515610654"><td class="cellrowborder" valign="top" width="22.06%" headers="mcps1.2.4.1.1 "><p id="p23197269"><a name="p23197269"></a><a name="p23197269"></a>pretty</p>
</td>
<td class="cellrowborder" valign="top" width="15.1%" headers="mcps1.2.4.1.2 "><p id="p67039530"><a name="p67039530"></a><a name="p67039530"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="62.839999999999996%" headers="mcps1.2.4.1.3 "><p id="p61492872"><a name="p61492872"></a><a name="p61492872"></a>If 'true', then the output is pretty printed.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section34607923"></a>

**Request parameters**:

For the description about the  **Content-Type** message header, see section [Patch Request Method Operation Description](patch-request-method-operation-description.md).

**Example request**:

```
Content-Type: application/json-patch+json
[
    {
        "op": "add",
        "path": "/status/active",
        "value": 2
    }
]
```

## Response<a name="section43035858"></a>

**Response parameters:**

For the description about response parameters, see  [Table 1](data-structure-of-response-parameters.md#en-us_topic_0079614930_table30479638).

**Example response:**

```
{
    "kind": "Job",
    "apiVersion": "batch/v1",
    "metadata": {
        "name": "jobs-12130306",
        "namespace": "ns-12130306-s",
        "selfLink": "/apis/batch/v1/namespaces/ns-12130306-s/jobs/jobs-12130306/status",
        "uid": "eed6b02b-dfb3-11e7-9c19-fa163e2d897b",
        "resourceVersion": "419067",
        "creationTimestamp": "2017-12-13T03:15:55Z",
        "labels": {
            "app": "new-jobs",
            "name": "job-test"
        },
        "enable": true
    },
    "spec": {
        "parallelism": 1,
        "completions": 1,
        "selector": {
            "matchLabels": {
                "controller-uid": "eed6b02b-dfb3-11e7-9c19-fa163e2d897b"
            }
        },
        "template": {
            "metadata": {
                "name": "jobs-12130306",
                "creationTimestamp": null,
                "labels": {
                    "controller-uid": "eed6b02b-dfb3-11e7-9c19-fa163e2d897b",
                    "job-name": "jobs-12130306",
                    "name": "job-test"
                },
                "enable": true
            },
            "spec": {
                "containers": [
                    {
                        "name": "jobs-12130306",
                        "image": "172.16.5.235:20202/test/redis:latest",
                        "resources": {},
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File",
                        "imagePullPolicy": "Always"
                    }
                ],
                "restartPolicy": "Never",
                "terminationGracePeriodSeconds": 30,
                "dnsPolicy": "ClusterFirst",
                "securityContext": {},
                "schedulerName": "default-scheduler"
            }
        }
    },
    "status": {
        "startTime": "2017-12-13T03:15:55Z",
        "active": 2
    }
}
```

## Status Code<a name="section51778404"></a>

[Table 2](#d0e42609)  describes the status code of this API.

**Table  2**  Status code

<a name="d0e42609"></a>
<table><thead align="left"><tr id="row58580616171015"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p45271266"><a name="p45271266"></a><a name="p45271266"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p43093911"><a name="p43093911"></a><a name="p43093911"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3769153171015"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p9510459"><a name="p9510459"></a><a name="p9510459"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p32149754"><a name="p32149754"></a><a name="p32149754"></a>This operation succeeds, and a Job resource object is returned.</p>
</td>
</tr>
</tbody>
</table>

For the description about status codes, see  [Status Code](status-code.md).

