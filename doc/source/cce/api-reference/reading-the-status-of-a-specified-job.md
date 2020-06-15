# Reading the Status of a specified Job<a name="cce_02_0161"></a>

## Function<a name="section872215"></a>

This API is used to read the status of a specified Job object.

## URI<a name="section7849943"></a>

GET /apis/batch/v1/namespaces/\{namespace\}/jobs/\{name\}/status

[Table 1](#d0e41637)  describes the parameters of this API.

**Table  1**  Parameter description

<a name="d0e41637"></a>
<table><thead align="left"><tr id="row42466880"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p65652297517"><a name="p65652297517"></a><a name="p65652297517"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="30.303030303030305%" id="mcps1.2.4.1.2"><p id="p165661629135114"><a name="p165661629135114"></a><a name="p165661629135114"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="36.36363636363636%" id="mcps1.2.4.1.3"><p id="p14567629115114"><a name="p14567629115114"></a><a name="p14567629115114"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1125057"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p14729974"><a name="p14729974"></a><a name="p14729974"></a>pretty</p>
</td>
<td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.2 "><p id="p52277209"><a name="p52277209"></a><a name="p52277209"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.4.1.3 "><p id="p6595574"><a name="p6595574"></a><a name="p6595574"></a>If 'true', then the output is pretty printed.</p>
</td>
</tr>
<tr id="row55687332"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p43444365"><a name="p43444365"></a><a name="p43444365"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.2 "><p id="p29332670"><a name="p29332670"></a><a name="p29332670"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.4.1.3 "><p id="p27136035"><a name="p27136035"></a><a name="p27136035"></a>Object name and auth scope, such as for teams and projects.</p>
</td>
</tr>
<tr id="row66507565"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p52163659"><a name="p52163659"></a><a name="p52163659"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.2 "><p id="p64506883"><a name="p64506883"></a><a name="p64506883"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.4.1.3 "><p id="p57675019"><a name="p57675019"></a><a name="p57675019"></a>Name of the Job.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section3540627"></a>

N/A

## Response<a name="section31865643"></a>

**Response parameters**:

For the description about response parameters, see  [Table 3](data-structure-of-response-parameters.md#en-us_topic_0079614930_table52931650).

**Example response**:

```
{
  "kind" : "Job",
  "apiVersion" : "batch/v1",
  "metadata" : {
    "name" : "jobs-12130306",
    "namespace" : "ns-12130306-s",
    "selfLink" : "/apis/batch/v1/namespaces/ns-12130306-s/jobs/jobs-12130306/status",
    "uid" : "eed6b02b-dfb3-11e7-9c19-fa163e2d897b",
    "resourceVersion" : "419068",
    "creationTimestamp" : "2017-12-13T03:15:55Z",
    "labels" : {
      "app" : "new-jobs",
      "name" : "job-test"
    },
    "enable" : true
  },
  "spec" : {
    "parallelism" : 1,
    "completions" : 1,
    "selector" : {
      "matchLabels" : {
        "controller-uid" : "eed6b02b-dfb3-11e7-9c19-fa163e2d897b"
      }
    },
    "template" : {
      "metadata" : {
        "name" : "jobs-12130306",
        "creationTimestamp" : null,
        "labels" : {
          "controller-uid" : "eed6b02b-dfb3-11e7-9c19-fa163e2d897b",
          "job-name" : "jobs-12130306",
          "name" : "job-test"
        },
        "enable" : true
      },
      "spec" : {
        "containers" : [ {
          "name" : "jobs-12130306",
          "image" : "172.16.5.235:20202/test/redis:latest",
          "resources" : { },
          "terminationMessagePath" : "/dev/termination-log",
          "terminationMessagePolicy" : "File",
          "imagePullPolicy" : "Always"
        } ],
        "restartPolicy" : "Never",
        "terminationGracePeriodSeconds" : 30,
        "dnsPolicy" : "ClusterFirst",
        "securityContext" : { },
        "schedulerName" : "default-scheduler"
      }
    }
  },
  "status" : {
    "startTime" : "2017-12-13T03:15:55Z",
    "active" : 1
  }
```

## Status Code<a name="section18355338"></a>

[Table 2](#d0e41716)  describes the status code of this API.

**Table  2**  Status code

<a name="d0e41716"></a>
<table><thead align="left"><tr id="row35122812"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p18020555"><a name="p18020555"></a><a name="p18020555"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p50378833"><a name="p50378833"></a><a name="p50378833"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row43124371"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p24374276"><a name="p24374276"></a><a name="p24374276"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p28159360"><a name="p28159360"></a><a name="p28159360"></a>This operation succeeds, and a Job resource object is returned.</p>
</td>
</tr>
</tbody>
</table>

For the description about status codes, see section  [Status Code](status-code.md).

