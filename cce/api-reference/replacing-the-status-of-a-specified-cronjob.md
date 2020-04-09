# Replacing the Status of a Specified CronJob<a name="cce_02_0231"></a>

## Function<a name="section43760555"></a>

This API is used to replace the status of a specified CronJob resource object.

## URI<a name="section58300681"></a>

PUT /apis/batch/v1beta1/namespaces/\{namespace\}/cronjobs/\{name\}/status

[Table 1](#d0e41971)  describes the parameters of this API.

**Table  1**  Parameter description

<a name="d0e41971"></a>
<table><thead align="left"><tr id="row65203523"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p65652297517"><a name="p65652297517"></a><a name="p65652297517"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p165661629135114"><a name="p165661629135114"></a><a name="p165661629135114"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p14567629115114"><a name="p14567629115114"></a><a name="p14567629115114"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row59355196"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p43041563"><a name="p43041563"></a><a name="p43041563"></a>pretty</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p63814603"><a name="p63814603"></a><a name="p63814603"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1600372"><a name="p1600372"></a><a name="p1600372"></a>If 'true', then the output is pretty printed.</p>
</td>
</tr>
<tr id="row14403349"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p25820581"><a name="p25820581"></a><a name="p25820581"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p11092289"><a name="p11092289"></a><a name="p11092289"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p26060242"><a name="p26060242"></a><a name="p26060242"></a>Name of the CronJob.</p>
</td>
</tr>
<tr id="row33215594"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p6108613"><a name="p6108613"></a><a name="p6108613"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p25035657"><a name="p25035657"></a><a name="p25035657"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p14622300"><a name="p14622300"></a><a name="p14622300"></a>Object name and auth scope, such as for teams and projects.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="d0e42020"></a>

**Request parameters**:

For the description about request parameters, see  [Table 2](creating-a-cronjob.md#table8040885).

**Example request**:

```
{
    "apiVersion": "batch/v1beta1",
    "kind": "CronJob",
    "metadata": {
        "creationTimestamp": "2018-03-07T12:17:22Z",
        "enable": true,
        "name": "cronjob-test",
        "namespace": "default",
        "resourceVersion": "442543",
        "selfLink": "/apis/batch/v1beta1/namespaces/default/cronjobs/cronjob-test",
        "uid": "7cf2c54b-2201-11e8-96aa-fa163ecd089c"
    },
    "spec": {
        "concurrencyPolicy": "Forbid",
        "failedJobsHistoryLimit": 1,
        "jobTemplate": {
            "metadata": {
                "creationTimestamp": null,
                "enable": true
            },
            "spec": {
                "template": {
                    "metadata": {
                        "creationTimestamp": null,
                        "enable": true,
                        "labels": {
                            "sjname": "cronjob-test"
                        }
                    },
                    "spec": {
                        "containers": [
                            {
                                "image": "nginx:stable-perl",
                                "imagePullPolicy": "IfNotPresent",
                                "lifecycle": {},
                                "name": "container-0",
                                "resources": {},
                                "terminationMessagePath": "/dev/termination-log",
                                "terminationMessagePolicy": "File"
                            }
                        ],
                        "dnsPolicy": "ClusterFirst",
                        "imagePullSecrets": [
                            {
                                "name": "default-secret"
                            }
                        ],
                        "restartPolicy": "OnFailure",
                        "schedulerName": "default-scheduler",
                        "securityContext": {},
                        "terminationGracePeriodSeconds": 30
                    }
                }
            }
        },
        "schedule": "*/2 * * * *",
        "successfulJobsHistoryLimit": 3,
        "suspend": false
    },
    "status": {
        "active": [
            {
                "apiVersion": "batch",
                "kind": "Job",
                "name": "cronjob-test-1520425800",
                "namespace": "default",
                "resourceVersion": "442542",
                "uid": "75aede3f-2203-11e8-96aa-fa163ecd089c"
            }
        ],
        "lastScheduleTime": "2018-03-07T12:30:00Z"
    }
}
```

## Response<a name="section24734697"></a>

**Response parameters:**

For the description about response parameters, see the parameter description in  [Table 2](creating-a-cronjob.md#table8040885).

**Example response:**

```
{
    "apiVersion": "batch/v1beta1",
    "kind": "CronJob",
    "metadata": {
        "creationTimestamp": "2018-03-07T12:17:22Z",
        "enable": true,
        "name": "cronjob-test",
        "namespace": "default",
        "resourceVersion": "442543",
        "selfLink": "/apis/batch/v1beta1/namespaces/default/cronjobs/cronjob-test",
        "uid": "7cf2c54b-2201-11e8-96aa-fa163ecd089c"
    },
    "spec": {
        "concurrencyPolicy": "Forbid",
        "failedJobsHistoryLimit": 1,
        "jobTemplate": {
            "metadata": {
                "creationTimestamp": null,
                "enable": true
            },
            "spec": {
                "template": {
                    "metadata": {
                        "creationTimestamp": null,
                        "enable": true,
                        "labels": {
                            "sjname": "cronjob-test"
                        }
                    },
                    "spec": {
                        "containers": [
                            {
                                "image": "nginx:stable-perl",
                                "imagePullPolicy": "IfNotPresent",
                                "lifecycle": {},
                                "name": "container-0",
                                "resources": {},
                                "terminationMessagePath": "/dev/termination-log",
                                "terminationMessagePolicy": "File"
                            }
                        ],
                        "dnsPolicy": "ClusterFirst",
                        "imagePullSecrets": [
                            {
                                "name": "default-secret"
                            }
                        ],
                        "restartPolicy": "OnFailure",
                        "schedulerName": "default-scheduler",
                        "securityContext": {},
                        "terminationGracePeriodSeconds": 30
                    }
                }
            }
        },
        "schedule": "*/2 * * * *",
        "successfulJobsHistoryLimit": 3,
        "suspend": false
    },
    "status": {
        "active": [
            {
                "apiVersion": "batch",
                "kind": "Job",
                "name": "cronjob-test-1520425800",
                "namespace": "default",
                "resourceVersion": "442542",
                "uid": "75aede3f-2203-11e8-96aa-fa163ecd089c"
            }
        ],
        "lastScheduleTime": "2018-03-07T12:30:00Z"
    }
}
```

## Status Code<a name="section21285686"></a>

[Table 2](#d0e42063)  describes the status code of this API.

**Table  2**  Status code

<a name="d0e42063"></a>
<table><thead align="left"><tr id="row42895616"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p51992856"><a name="p51992856"></a><a name="p51992856"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p50671784"><a name="p50671784"></a><a name="p50671784"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row10773849"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p266578"><a name="p266578"></a><a name="p266578"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p21592892"><a name="p21592892"></a><a name="p21592892"></a>This operation succeeds, and a Job resource object is returned.</p>
</td>
</tr>
</tbody>
</table>

For the description about status codes, see  [Status Code](status-code.md).

