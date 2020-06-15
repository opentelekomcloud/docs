# Reading the Status of a Specified Deployment<a name="cce_02_0123"></a>

## Function<a name="section37553505"></a>

This API is used to read the status of a specified Deployment object under a specified Namespace.

## URI<a name="section2437233"></a>

GET /apis/apps/v1/namespaces/\{namespace\}/deployments/\{name\}/status \(Supports only1.9\)

GET /apis/apps/v1beta1/namespaces/\{namespace\}/deployments/\{name\}/status \(Supports only1.7\)

GET /apis/extensions/v1beta1/namespaces/\{namespace\}/deployments/\{name\}/status \(Compatible\)

[Table 1](#d0e35701)  describes the parameters of this API.

**Table  1**  Parameter description

<a name="d0e35701"></a>
<table><thead align="left"><tr id="row65104669"><th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.2.4.1.1"><p id="p65652297517"><a name="p65652297517"></a><a name="p65652297517"></a>Parameters</p>
</th>
<th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.2.4.1.2"><p id="p165661629135114"><a name="p165661629135114"></a><a name="p165661629135114"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="67.34326567343265%" id="mcps1.2.4.1.3"><p id="p14567629115114"><a name="p14567629115114"></a><a name="p14567629115114"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row31480888"><td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.4.1.1 "><p id="p66924004"><a name="p66924004"></a><a name="p66924004"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.4.1.2 "><p id="p52135240"><a name="p52135240"></a><a name="p52135240"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="67.34326567343265%" headers="mcps1.2.4.1.3 "><p id="p62204941"><a name="p62204941"></a><a name="p62204941"></a>Name of the Deployment.</p>
</td>
</tr>
<tr id="row22973563"><td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.4.1.1 "><p id="p48919348"><a name="p48919348"></a><a name="p48919348"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.4.1.2 "><p id="p3044257"><a name="p3044257"></a><a name="p3044257"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="67.34326567343265%" headers="mcps1.2.4.1.3 "><p id="p45258283"><a name="p45258283"></a><a name="p45258283"></a>Object name and auth scope, such as for teams and projects.</p>
</td>
</tr>
<tr id="row4671366"><td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.4.1.1 "><p id="p42836357"><a name="p42836357"></a><a name="p42836357"></a>pretty</p>
</td>
<td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.4.1.2 "><p id="p47192917"><a name="p47192917"></a><a name="p47192917"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="67.34326567343265%" headers="mcps1.2.4.1.3 "><p id="p64529950"><a name="p64529950"></a><a name="p64529950"></a>If 'true', then the output is pretty printed.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section21935102"></a>

N/A

## Response<a name="section63198193"></a>

**Response parameters:**

For the description about response parameters, see  [Table 2](creating-a-deployment.md#table12862324102610).

**Example response:**

```
{
    "kind": "Deployment",
    "apiVersion": "apps/v1beta1",
    "metadata": {
        "name": "deploy-12130306",
        "namespace": "ns-12130306-s",
        "selfLink": "/apis/apps/v1beta1/namespaces/ns-12130306-s/deployments/deploy-12130306/status",
        "uid": "27072a31-dfb3-11e7-9c19-fa163e2d897b",
        "resourceVersion": "418598",
        "generation": 2,
        "creationTimestamp": "2017-12-13T03:10:20Z",
        "labels": {
            "cce/appgroup": "deploy_test"
        },
        "annotations": {
            "deployment.kubernetes.io/revision": "1"
        },
        "enable": true
    },
    "spec": {
        "replicas": 1,
        "selector": {
            "matchLabels": {
                "cce/appgroup": "deploy_test"
            }
        },
        "template": {
            "metadata": {
                "creationTimestamp": null,
                "labels": {
            "cce/appgroup": "deploy_test"
                },
        "enable": true
    },
            "spec": {
                "containers": [
                    {
                        "name": "deploycon-12130306",
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
        "strategy": {
            "type": "RollingUpdate",
            "rollingUpdate": {
                "maxUnavailable": "25%",
                "maxSurge": "25%"
            }
        },
        "revisionHistoryLimit": 2,
        "progressDeadlineSeconds": 600
    },
    "status": {
        "observedGeneration": 2,
        "replicas": 1,
        "updatedReplicas": 1,
        "readyReplicas": 1,
        "availableReplicas": 1,
        "conditions": [
            {
                "type": "Progressing",
                "status": "True",
                "lastUpdateTime": "2017-12-13T03:10:20Z",
                "lastTransitionTime": "2017-12-13T03:10:20Z",
                "reason": "NewReplicaSetAvailable",
                "message": "ReplicaSet \"deploy-12130306-3417241766\" has successfully progressed."
            },
            {
                "type": "Available",
                "status": "True",
                "lastUpdateTime": "2017-12-13T03:10:23Z",
                "lastTransitionTime": "2017-12-13T03:10:23Z",
                "reason": "MinimumReplicasAvailable",
                "message": "Deployment has minimum availability."
            }
        ]
    }
}
```

## Status Code<a name="section31912827"></a>

[Table 2](#d0e35779)  describes the status code of this API.

**Table  2**  Status code

<a name="d0e35779"></a>
<table><thead align="left"><tr id="row14389536"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p24701750"><a name="p24701750"></a><a name="p24701750"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p54684770"><a name="p54684770"></a><a name="p54684770"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row281353"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p22789653"><a name="p22789653"></a><a name="p22789653"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p34022638"><a name="p34022638"></a><a name="p34022638"></a>This operation succeeds, and a Deployment resource object is returned.</p>
</td>
</tr>
</tbody>
</table>

For the description about status codes, see  [Status Code](status-code.md).

