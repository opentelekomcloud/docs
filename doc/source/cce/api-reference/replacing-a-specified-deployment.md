# Replacing a Specified Deployment<a name="cce_02_0097"></a>

## Function<a name="section49665120162716"></a>

This API is used to replace a Deployment object under a specified Namespace.

The following fields can be updated:

-   metadata.selfLink
-   metadata.resourceVersion
-   metadata.generation
-   metadata.creationTimestamp
-   metadata.deletionTimestamp
-   metadata.labels
-   metadata.clusterName
-   metadata.generateName
-   metadata.annotations
-   spec.replicas
-   template.contaions
-   spec.restartPolicy
-   spec.activeDeadlineSeconds

The other fields cannot be updated.

## URI<a name="section1524832914503"></a>

PUT /apis/apps/v1/namespaces/\{namespace\}/deployments/\{name\} \(Supports only1.9\)

PUT /apis/apps/v1beta1/namespaces/\{namespace\}/deployments/\{name\} \(Supports only1.7\)

PUT /apis/extensions/v1beta1/namespaces/\{namespace\}/deployments/\{name\} \(Compatible\)

[Table 1](#table14970324122818)  describes the parameters of this API.

**Table  1**  Parameter description

<a name="table14970324122818"></a>
<table><thead align="left"><tr id="row0971162417289"><th class="cellrowborder" valign="top" width="17.23%" id="mcps1.2.4.1.1"><p id="en-us_topic_0079616860_en-us_topic_0079614957_p54329699"><a name="en-us_topic_0079616860_en-us_topic_0079614957_p54329699"></a><a name="en-us_topic_0079616860_en-us_topic_0079614957_p54329699"></a>Parameters</p>
</th>
<th class="cellrowborder" valign="top" width="16.71%" id="mcps1.2.4.1.2"><p id="p6151164282819"><a name="p6151164282819"></a><a name="p6151164282819"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="66.06%" id="mcps1.2.4.1.3"><p id="p21518421288"><a name="p21518421288"></a><a name="p21518421288"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row83198295289"><td class="cellrowborder" valign="top" width="17.23%" headers="mcps1.2.4.1.1 "><p id="p153191729102818"><a name="p153191729102818"></a><a name="p153191729102818"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.71%" headers="mcps1.2.4.1.2 "><p id="p63193293289"><a name="p63193293289"></a><a name="p63193293289"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.06%" headers="mcps1.2.4.1.3 "><p id="p231992915285"><a name="p231992915285"></a><a name="p231992915285"></a>Name of the DaemonSet.</p>
</td>
</tr>
<tr id="row6971102432818"><td class="cellrowborder" valign="top" width="17.23%" headers="mcps1.2.4.1.1 "><p id="p397172413282"><a name="p397172413282"></a><a name="p397172413282"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="16.71%" headers="mcps1.2.4.1.2 "><p id="p14971824142810"><a name="p14971824142810"></a><a name="p14971824142810"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.06%" headers="mcps1.2.4.1.3 "><p id="p89717240289"><a name="p89717240289"></a><a name="p89717240289"></a>Object name and auth scope, such as for teams and projects.</p>
</td>
</tr>
<tr id="row11971122412819"><td class="cellrowborder" valign="top" width="17.23%" headers="mcps1.2.4.1.1 "><p id="p1597142412282"><a name="p1597142412282"></a><a name="p1597142412282"></a>pretty</p>
</td>
<td class="cellrowborder" valign="top" width="16.71%" headers="mcps1.2.4.1.2 "><p id="p497132410288"><a name="p497132410288"></a><a name="p497132410288"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="66.06%" headers="mcps1.2.4.1.3 "><p id="p1597132420289"><a name="p1597132420289"></a><a name="p1597132420289"></a>If 'true', then the output is pretty printed.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section632192162716"></a>

**Request parameters:**

For the description about request parameters, see  [Table 2](creating-a-deployment.md#table12862324102610).

**Example request**:

```
{
    "kind": "Deployment",
    "apiVersion": "apps/v1beta1",
    "metadata": {
        "name": "deploy-example",
        "namespace": "default",
        "selfLink": "/apis/apps/v1beta1/namespaces/default/deployments/deploy-example",
        "uid": "27072a31-dfb3-11e7-9c19-fa163e2d897b",
        "resourceVersion": "418453",
        "generation": 1,
        "creationTimestamp": "2017-12-13T03:10:20Z",
        "labels": {
            "app": "test"
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
                "app": "test"
            }
        },
        "template": {
            "metadata": {
                "creationTimestamp": null,
                "labels": {
                    "app": "test"
                },
                "enable": true
            },
            "spec": {
                "containers": [
                    {
                        "name": "deploycon-12130306",
                        "image": "nginx",
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
        "observedGeneration": 1,
        "conditions": [
            {
                "type": "Available",
                "status": "True",
                "lastUpdateTime": "2017-12-13T03:10:20Z",
                "lastTransitionTime": "2017-12-13T03:10:20Z",
                "reason": "MinimumReplicasAvailable",
                "message": "Deployment has minimum availability."
            },
            {
                "type": "Progressing",
                "status": "True",
                "lastUpdateTime": "2017-12-13T03:10:20Z",
                "lastTransitionTime": "2017-12-13T03:10:20Z",
                "reason": "NewReplicaSetAvailable",
                "message": "ReplicaSet \"deploy-12130306-3417241766\" has successfully progressed."
            }
        ]
    }
}
```

## Response<a name="section32420053133613"></a>

**Response parameters:**

For the description about response parameters, see  [Table 2](creating-a-deployment.md#table12862324102610).

**Example response:**

```
{
    "apiVersion": "apps/v1beta1",
    "kind": "Deployment",
    "metadata": {
        "annotations": {
            "deployment.kubernetes.io/revision": "1"
        },
        "creationTimestamp": "2017-11-09T01:35:00Z",
        "enable": true,
        "generation": 1,
        "labels": {
            "app": "test"
        },
        "name": "deployment-example",
        "namespace": "default",
        "resourceVersion": "12857132",
        "selfLink": "/apis/apps/v1beta1/namespaces/default/deployments/deployment-example",
        "uid": "33a5e8fd-c4ee-11e7-aad0-286ed488d4c6"
    },
    "spec": {
        "replicas": 3,
        "selector": {
            "matchLabels": {
                "app": "test"
            }
        },
        "strategy": {
            "rollingUpdate": {
                "maxSurge": 1,
                "maxUnavailable": 1
            },
            "type": "RollingUpdate"
        },
        "template": {
            "metadata": {
                "creationTimestamp": null,
                "enable": true,
                "labels": {
                    "app": "test"
                }
            },
            "spec": {
                "containers": [
                    {
                        "image": "nginx:1.13.6",
                        "imagePullPolicy": "Always",
                        "name": "nginx",
                        "resources": {},
                        "terminationMessagePath": "/dev/termination-log"
                    }
                ],
                "dnsPolicy": "ClusterFirst",
                "restartPolicy": "Always",
                "securityContext": {},
                "terminationGracePeriodSeconds": 30
            }
        }
    },
    "status": {
        "conditions": [
            {
                "lastTransitionTime": "2017-11-10T17:02:50Z",
                "lastUpdateTime": "2017-11-10T01:35:01Z",
                "message": "Deployment does not have minimum availability.",
                "reason": "MinimumReplicasUnavailable",
                "status": "False",
                "type": "Available"
            }
        ],
        "observedGeneration": 1,
        "replicas": 3,
        "unavailableReplicas": 3,
        "updatedReplicas": 3
    }
}
```

## Status Code<a name="section23844563171015"></a>

[Table 2](#en-us_topic_0079616860_en-us_topic_0079614957_table12683857)  describes the status code of this API.

**Table  2**  Status code

<a name="en-us_topic_0079616860_en-us_topic_0079614957_table12683857"></a>
<table><thead align="left"><tr id="row58580616171015"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p47409442171015"><a name="p47409442171015"></a><a name="p47409442171015"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p14959613171015"><a name="p14959613171015"></a><a name="p14959613171015"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3769153171015"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p34614774161656"><a name="p34614774161656"></a><a name="p34614774161656"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p20339135502118"><a name="p20339135502118"></a><a name="p20339135502118"></a>This operation succeeds, and a Deployment resource object is returned.</p>
</td>
</tr>
</tbody>
</table>

For the description about status codes, see  [Status Code](status-code.md).

