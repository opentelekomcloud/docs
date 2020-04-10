# Reading a Specified CronJob<a name="cce_02_0228"></a>

## Function<a name="section34495516"></a>

This API is used to read a specified CronJob resource object.

## URI<a name="section42024188"></a>

GET /apis/batch/v1beta1/namespaces/\{namespace\}/cronjobs/\{name\}

[Table 1](#d0e41471)  describes the parameters of this API.

**Table  1**  Parameter description

<a name="d0e41471"></a>
<table><thead align="left"><tr id="row14497772"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p65652297517"><a name="p65652297517"></a><a name="p65652297517"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="30.303030303030305%" id="mcps1.2.4.1.2"><p id="p165661629135114"><a name="p165661629135114"></a><a name="p165661629135114"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="36.36363636363636%" id="mcps1.2.4.1.3"><p id="p14567629115114"><a name="p14567629115114"></a><a name="p14567629115114"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row66636327"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p28833370"><a name="p28833370"></a><a name="p28833370"></a>pretty</p>
</td>
<td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.2 "><p id="p53801671"><a name="p53801671"></a><a name="p53801671"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.4.1.3 "><p id="p62968084"><a name="p62968084"></a><a name="p62968084"></a>If 'true', then the output is pretty printed.</p>
</td>
</tr>
<tr id="row29841846"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1270455"><a name="p1270455"></a><a name="p1270455"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.2 "><p id="p35797996"><a name="p35797996"></a><a name="p35797996"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.4.1.3 "><p id="p13956541"><a name="p13956541"></a><a name="p13956541"></a>Object name and auth scope, such as for teams and projects.</p>
</td>
</tr>
<tr id="row58500012"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p40880564"><a name="p40880564"></a><a name="p40880564"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.2 "><p id="p22991372"><a name="p22991372"></a><a name="p22991372"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.4.1.3 "><p id="p50361820"><a name="p50361820"></a><a name="p50361820"></a>Name of the Pod.</p>
</td>
</tr>
<tr id="row50603201"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p5218617"><a name="p5218617"></a><a name="p5218617"></a>exact</p>
</td>
<td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.2 "><p id="p20054846"><a name="p20054846"></a><a name="p20054846"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.4.1.3 "><p id="p13829815"><a name="p13829815"></a><a name="p13829815"></a>Should the export be exact. Exact export maintains cluster-specific fields like 'Namespace'.</p>
</td>
</tr>
<tr id="row57359475"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p15605878"><a name="p15605878"></a><a name="p15605878"></a>export</p>
</td>
<td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.2 "><p id="p56116577"><a name="p56116577"></a><a name="p56116577"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.4.1.3 "><p id="p49148893"><a name="p49148893"></a><a name="p49148893"></a>Should this value be exported. Export strips fields that a user cannot specify.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section42673379"></a>

N/A

## Response<a name="section48516097"></a>

**Response parameters:**

For the description about response parameters, see the parameter description in  [Table 2](creating-a-job.md#table8040885).

**Example response:**

```
{
  "kind": "CronJob",
  "apiVersion": "batch/v1beta1",
  "metadata": {
    "name": "cronjob-test",
    "namespace": "default",
    "selfLink": "/apis/batch/v1beta1/namespaces/default/cronjobs/cronjob-test",
    "uid": "7cf2c54b-2201-11e8-96aa-fa163ecd089c",
    "resourceVersion": "441600",
    "creationTimestamp": "2018-03-07T12:17:22Z",
    "enable": true
  },
  "spec": {
    "schedule": "*/59 * * * *",
    "concurrencyPolicy": "Allow",
    "suspend": false,
    "jobTemplate": {
      "metadata": {
        "creationTimestamp": null,
        "enable": true
  },
      "spec": {
        "template": {
          "metadata": {
            "creationTimestamp": null,
            "labels": {
              "sjname": "cronjob-test"
            },
            "enable": true
  },
          "spec": {
            "containers": [
              {
                "name": "container-0",
                "image": "nginx:stable-perl",
                "resources": {

                },
                "lifecycle": {

                },
                "terminationMessagePath": "/dev/termination-log",
                "terminationMessagePolicy": "File",
                "imagePullPolicy": "IfNotPresent"
              }
            ],
            "restartPolicy": "OnFailure",
            "terminationGracePeriodSeconds": 30,
            "dnsPolicy": "ClusterFirst",
            "securityContext": {

            },
            "imagePullSecrets": [
              {
                "name": "default-secret"
              }
            ],
            "schedulerName": "default-scheduler"
          }
        }
      }
    },
    "successfulJobsHistoryLimit": 3,
    "failedJobsHistoryLimit": 1
  },
  "status": {

  }
}
```

## Status Code<a name="section33991695"></a>

[Table 2](#d0e41570)  describes the status code of this API.

**Table  2**  Status code

<a name="d0e41570"></a>
<table><thead align="left"><tr id="row22801529"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p34984551"><a name="p34984551"></a><a name="p34984551"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p15176386"><a name="p15176386"></a><a name="p15176386"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row21327729"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p49824477"><a name="p49824477"></a><a name="p49824477"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p9250797"><a name="p9250797"></a><a name="p9250797"></a>This operation succeeds, and a Job resource object is returned.</p>
</td>
</tr>
</tbody>
</table>

For the description about status codes, see  [Status Code](status-code.md).

