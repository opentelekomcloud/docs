# Creating a ReplicationController<a name="cce_02_0016"></a>

## Function<a name="sf70db589a84041ef9dced29703222a45"></a>

This API is used to create a ReplicationController.

## URI<a name="s58267715f43d4b4594c42fbc549c050c"></a>

POST /api/v1/namespaces/\{namespace\}/replicationcontrollers

[Table 1](#en-us_topic_0079615078_table29772226)  describes the parameters of this API.

**Table  1**  Parameter description

<a name="en-us_topic_0079615078_table29772226"></a>
<table><thead align="left"><tr id="en-us_topic_0079615078_row36286570"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="en-us_topic_0079615078_p53531063"><a name="en-us_topic_0079615078_p53531063"></a><a name="en-us_topic_0079615078_p53531063"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p2005499620266"><a name="p2005499620266"></a><a name="p2005499620266"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="en-us_topic_0079615078_p36623759"><a name="en-us_topic_0079615078_p36623759"></a><a name="en-us_topic_0079615078_p36623759"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0079615078_row13734506"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0079615078_p38753177"><a name="en-us_topic_0079615078_p38753177"></a><a name="en-us_topic_0079615078_p38753177"></a>pretty</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0079615078_p51999621"><a name="en-us_topic_0079615078_p51999621"></a><a name="en-us_topic_0079615078_p51999621"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p161723320581"><a name="p161723320581"></a><a name="p161723320581"></a>If 'true', then the output is pretty printed.</p>
</td>
</tr>
<tr id="en-us_topic_0079615078_row36003682"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0079615078_p30617153"><a name="en-us_topic_0079615078_p30617153"></a><a name="en-us_topic_0079615078_p30617153"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0079615078_p64070324"><a name="en-us_topic_0079615078_p64070324"></a><a name="en-us_topic_0079615078_p64070324"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p798973795815"><a name="p798973795815"></a><a name="p798973795815"></a>Object name and auth scope, such as for teams and projects.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0079615078_ref458783257"></a>

**Request parameters:**

For the description about request parameters, see  [Table 1](data-structure-of-request-parameters.md#en-us_topic_0079614925_table51284307).

**Example request:**

```
{
    "kind": "ReplicationController",
    "apiVersion": "v1",
    "metadata": {
        "name": "frontend-controller",
        "labels": {
            "cce/group": "frontend-controller",
            "name": "frontend"
        }
    },
    "spec": {
        "replicas": 2,
        "selector": {
            "cce/group": "frontend-controller",
            "name": "frontend"
        },
        "template": {
            "metadata": {
                "labels": {
                    "cce/group": "frontend-controller",
                    "name": "frontend"
                }
            },
            "spec": {
                "volumes": null,
                "containers": [
                    {
                        "name": "php-redis",
                        "image": "redis",
                        "ports": [
                            {
                                "containerPort": 80,
                                "protocol": "TCP"
                            }
                        ],
                        "imagePullPolicy": "IfNotPresent"
                    }
                ],
                "restartPolicy": "Always",
                "dnsPolicy": "ClusterFirst"
            }
        }
    }
}
```

## Response<a name="s17b1fd8a9c8c4bc3bcf3e05f795861c6"></a>

**Response parameters:**

For the description about response parameters, see the parameter description in  [Request](#en-us_topic_0079615078_ref458783257).

**Example response:**

```
{
    "apiVersion": "v1",
    "kind": "ReplicationController",
    "metadata": {
        "creationTimestamp": "2017-06-23T08:40:52Z",
        "generation": 1,
        "labels": {
            "cce/group": "frontend-controller",
            "name": "frontend"
        },
        "name": "frontend-controller",
        "namespace": "default",
        "resourceVersion": "850929",
        "selfLink": "/api/v1/namespaces/default/replicationcontrollers/frontend-controller",
        "uid": "aa123f3f-57ef-11e7-97f8-fa163e61f3f9"
    },
    "spec": {
        "replicas": 2,
        "selector": {
            "cce/group": "frontend-controller",
            "name": "frontend"
        },
        "template": {
            "metadata": {
                "creationTimestamp": null,
                "labels": {
                    "cce/group": "frontend-controller",
                    "name": "frontend"
                }
            },
            "spec": {
                "containers": [
                    {
                        "image": "redis",
                        "imagePullPolicy": "IfNotPresent",
                        "name": "php-redis",
                        "ports": [
                            {
                                "containerPort": 80,
                                "protocol": "TCP"
                            }
                        ],
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
        "availableReplicas": 2,
        "fullyLabeledReplicas": 2,
        "observedGeneration": 1,
        "readyReplicas": 2,
        "replicas": 2
    }
}
```

## Status Code<a name="s33091caa928947d0a6280827c903169a"></a>

[Table 2](#en-us_topic_0079615078_table66623444)  describes the status code of this API.

**Table  2**  Status code

<a name="en-us_topic_0079615078_table66623444"></a>
<table><thead align="left"><tr id="en-us_topic_0079615078_row62669098"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p1701330220266"><a name="p1701330220266"></a><a name="p1701330220266"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="en-us_topic_0079615078_p63055227"><a name="en-us_topic_0079615078_p63055227"></a><a name="en-us_topic_0079615078_p63055227"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0079615078_row7199758"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0079615078_p46309534"><a name="en-us_topic_0079615078_p46309534"></a><a name="en-us_topic_0079615078_p46309534"></a>201</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0079615078_p60084754"><a name="en-us_topic_0079615078_p60084754"></a><a name="en-us_topic_0079615078_p60084754"></a>If the operation is successful, the ReplicationController is returned.</p>
</td>
</tr>
</tbody>
</table>

For the description about status codes, see section  [Status Code](status-code.md).

