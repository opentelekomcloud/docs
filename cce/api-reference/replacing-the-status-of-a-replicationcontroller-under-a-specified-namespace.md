# Replacing the Status of a ReplicationController Under a Specified Namespace<a name="cce_02_0020"></a>

## Function<a name="s5cd699f1cc7646178135f9434a99fb74"></a>

This API is used to replace the status of a ReplicationController object under a specified Namespace, that is, to modify the parameter values of the  **status**  field of the ReplicationController object.

## URI<a name="se57cf21fb2e540ecad94c48767ea612d"></a>

PUT /api/v1/namespaces/\{namespace\}/replicationcontrollers/\{name\}/status

[Table 1](#table2042316458519)  describes the parameters of this API.

**Table  1**  Parameter description

<a name="table2042316458519"></a>
<table><thead align="left"><tr id="row1342317451054"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p10423134517519"><a name="p10423134517519"></a><a name="p10423134517519"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p1842319451516"><a name="p1842319451516"></a><a name="p1842319451516"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p164231145250"><a name="p164231145250"></a><a name="p164231145250"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row12423545659"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p174238451758"><a name="p174238451758"></a><a name="p174238451758"></a>pretty</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p134241645554"><a name="p134241645554"></a><a name="p134241645554"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1342454518512"><a name="p1342454518512"></a><a name="p1342454518512"></a>If 'true', then the output is pretty printed.</p>
</td>
</tr>
<tr id="row194241345955"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p642419453510"><a name="p642419453510"></a><a name="p642419453510"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p124248451510"><a name="p124248451510"></a><a name="p124248451510"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p642417451453"><a name="p642417451453"></a><a name="p642417451453"></a>Object name and auth scope, such as for teams and projects.</p>
</td>
</tr>
<tr id="row84241945755"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p542419452056"><a name="p542419452056"></a><a name="p542419452056"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p442418451352"><a name="p442418451352"></a><a name="p442418451352"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p142411451954"><a name="p142411451954"></a><a name="p142411451954"></a>Name of the ReplicationController.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0079614898_ref458790189"></a>

**Request parameters:**

For the description about request parameters, see  [Table 1](data-structure-of-request-parameters.md#en-us_topic_0079614925_table51284307).

**Example request:**

```
{
  "kind": "ReplicationController",
  "apiVersion": "v1",
  "metadata": {
    "name": "frontend-controller",
    "namespace": "default",
    "selfLink": "/api/v1/namespaces/default/replicationcontrollers/frontend-controller",
    "uid": "cd4594b6-5d0b-11e6-aeb9-286ed488fafe",
    "resourceVersion": "3586",
    "generation": 4,
    "creationTimestamp": "2016-08-08T01:59:55Z",
    "labels": {
      "app": "nginx",
      "label1": "testexample"
    }
  },
  "status": {
    "replicas": 1,
    "observedGeneration": 3
  }
}
```

## Response<a name="s76a8b9fc01944171a9a63cbfbc490b3b"></a>

**Response parameters:**

For the description about response parameters, see the parameter description in  [Request](#en-us_topic_0079614898_ref458790189).

**Example response:**

```
{
  "kind": "ReplicationController",
  "apiVersion": "v1",
  "metadata": {
    "name": "frontend-controller",
    "namespace": "default",
    "selfLink": "/api/v1/namespaces/default/replicationcontrollers/frontend-controller/status",
    "uid": "cd4594b6-5d0b-11e6-aeb9-286ed488fafe",
    "resourceVersion": "3593",
    "generation": 4,
    "creationTimestamp": "2016-08-08T01:59:55Z",
    "labels": {
      "app": "nginx",
      "label1": "testexample"
    }
  },
  "spec": {
    "replicas": 2,
    "selector": {
      "app": "nginx"
    },
    "template": {
      "metadata": {
        "creationTimestamp": null,
        "labels": {
      "app": "nginx",
      "label1": "testexample"
    }
  },
      "spec": {
        "containers": [
          {
            "name": "redis",
            "image": "redis:latest",
            "ports": [
              {
                "containerPort": 80,
                "protocol": "TCP"
              }
            ],
            "resources": {},
            "terminationMessagePath": "/dev/termination-log",
            "imagePullPolicy": "Always"
          }
        ],
        "restartPolicy": "Always",
        "terminationGracePeriodSeconds": 30,
        "dnsPolicy": "ClusterFirst",
        "securityContext": {}
      }
    }
  },
  "status": {
    "replicas": 1,
    "observedGeneration": 3
  }
}
```

## Status Code<a name="s640db036c4474963bd0cfa6776ea90b2"></a>

[Table 2](#en-us_topic_0079614898_table29218602)  describes the status code of this API.

**Table  2**  Status code

<a name="en-us_topic_0079614898_table29218602"></a>
<table><thead align="left"><tr id="en-us_topic_0079614898_row8218569"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p33367786194649"><a name="p33367786194649"></a><a name="p33367786194649"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p18436160194649"><a name="p18436160194649"></a><a name="p18436160194649"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0079614898_row38731835"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0079614898_p50270949"><a name="en-us_topic_0079614898_p50270949"></a><a name="en-us_topic_0079614898_p50270949"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p133631213613"><a name="p133631213613"></a><a name="p133631213613"></a>This operation succeeds, and a ReplicationController resource object is returned.</p>
</td>
</tr>
</tbody>
</table>

For the description about status codes, see section  [Status Code](status-code.md).

