# Replacing the Status of a Specified Job<a name="cce_02_0163"></a>

## Function<a name="section43760555"></a>

This API is used to replace the status of the specified Job object.

## URI<a name="section58300681"></a>

PUT /apis/batch/v1/namespaces/\{namespace\}/jobs/\{name\}/status

[Table 1](#d0e41971)  describes the parameters of this API.

**Table  1**  Parameter description

<a name="d0e41971"></a>
<table><thead align="left"><tr id="row14601642"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p65652297517"><a name="p65652297517"></a><a name="p65652297517"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p165661629135114"><a name="p165661629135114"></a><a name="p165661629135114"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p14567629115114"><a name="p14567629115114"></a><a name="p14567629115114"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row13608105"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p43041563"><a name="p43041563"></a><a name="p43041563"></a>pretty</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p63814603"><a name="p63814603"></a><a name="p63814603"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1600372"><a name="p1600372"></a><a name="p1600372"></a>If 'true', then the output is pretty printed.</p>
</td>
</tr>
<tr id="row27655246"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p25820581"><a name="p25820581"></a><a name="p25820581"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p11092289"><a name="p11092289"></a><a name="p11092289"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p26060242"><a name="p26060242"></a><a name="p26060242"></a>name of the Job</p>
</td>
</tr>
<tr id="row14161658121016"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p6108613"><a name="p6108613"></a><a name="p6108613"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p25035657"><a name="p25035657"></a><a name="p25035657"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p14622300"><a name="p14622300"></a><a name="p14622300"></a>object name and auth scope, such as for teams and projects</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="d0e42020"></a>

**Request parameters**:

For the description about request parameters, see  [Table 2](creating-a-job.md#table8040885).

**Example request**:

```
{
    "kind" : "Job",
    "apiVersion" : "batch/v1",
    "metadata": {
        "name": "jobs-12130306",
        "namespace": "ns-12130306-s",
        "selfLink": "/apis/batch/v1/namespaces/ns-12130306-s/jobs/jobs-12130306",
        "uid": "eed6b02b-dfb3-11e7-9c19-fa163e2d897b",
        "resourceVersion": "419068",
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
        "active": 1
    }
}
```

## Response<a name="section24734697"></a>

**Response parameters**:

For the description about response parameters, see the parameter description in  [Request](#d0e42020).

**Example response**:

```
{
    "kind": "Job",
    "apiVersion": "batch/v1",
    "metadata": {
        "name": "jobs-12130306",
        "namespace": "ns-12130306-s",
        "selfLink": "/apis/batch/v1/namespaces/ns-12130306-s/jobs/jobs-12130306",
        "uid": "eed6b02b-dfb3-11e7-9c19-fa163e2d897b",
        "resourceVersion": "419068",
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
        "active": 1
    }
}
```

## Status Code<a name="section21285686"></a>

[Table 2](#d0e42063)  describes the status code of this API.

**Table  2**  Status code

<a name="d0e42063"></a>
<table><thead align="left"><tr id="row47812724"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p51992856"><a name="p51992856"></a><a name="p51992856"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p50671784"><a name="p50671784"></a><a name="p50671784"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row11627434"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p266578"><a name="p266578"></a><a name="p266578"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p21592892"><a name="p21592892"></a><a name="p21592892"></a>This operation succeeds, and a Job resource object is returned.</p>
</td>
</tr>
</tbody>
</table>

For the description about status codes, see section  [Status Code](status-code.md).

