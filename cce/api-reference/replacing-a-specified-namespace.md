# Replacing a Specified Namespace<a name="cce_02_0053"></a>

## Function<a name="se64c62bbc28a47689949a123d846c8ca"></a>

This API is used to replace some information about a specified Namespace.

The following fields can be updated:

-   metadata.selfLink
-   metadata.resourceVersion
-   metadata.generation
-   metadata.creationTimestamp
-   metadata.deletionTimestamp
-   metadata.labels
-   metadata.generateName
-   metadata.annotations

## URI<a name="sa913bc0ccab7450b8923451bf9f15c04"></a>

PUT /api/v1/namespaces/\{name\}

[Table 1](#en-us_topic_0079615038_table49444123)  describes the parameters of this API.

**Table  1**  Parameter description

<a name="en-us_topic_0079615038_table49444123"></a>
<table><thead align="left"><tr id="row14601642"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="en-us_topic_0079615038_p41882373"><a name="en-us_topic_0079615038_p41882373"></a><a name="en-us_topic_0079615038_p41882373"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p13489349201632"><a name="p13489349201632"></a><a name="p13489349201632"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p18895455201632"><a name="p18895455201632"></a><a name="p18895455201632"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row13608105"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0079615038_p28514710"><a name="en-us_topic_0079615038_p28514710"></a><a name="en-us_topic_0079615038_p28514710"></a>pretty</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0079615038_p27990155"><a name="en-us_topic_0079615038_p27990155"></a><a name="en-us_topic_0079615038_p27990155"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0079615038_p52610097"><a name="en-us_topic_0079615038_p52610097"></a><a name="en-us_topic_0079615038_p52610097"></a>If 'true', then the output is pretty printed.</p>
</td>
</tr>
<tr id="row27655246"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0079615038_p25482430"><a name="en-us_topic_0079615038_p25482430"></a><a name="en-us_topic_0079615038_p25482430"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0079615038_p50810959"><a name="en-us_topic_0079615038_p50810959"></a><a name="en-us_topic_0079615038_p50810959"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0079615038_p22047016"><a name="en-us_topic_0079615038_p22047016"></a><a name="en-us_topic_0079615038_p22047016"></a>Name of the Namespace.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0079615038_ref458676991"></a>

**Request parameters**:

For the description about request parameters, see  [Table 2](creating-a-namespace.md#en-us_topic_0079615062_ref458759029).

**Example request**:

```
{ 
   "apiVersion": "v1", 
     "kind": "Namespace", 
     "metadata": { 
         "name": "test", 
         "labels": { 
             "name": "test" 
         } 
     }, 
     "spec": { 
         "finalizers": [ 
             "kubernetes" 
         ] 
     }, 
     "status": { 
         "phase": "Active" 
     } 
 }
```

## Response<a name="s71d64222a34d4101aa1732e19c992943"></a>

**Response parameters**:

For the description about response parameters, see the parameter description in  [Request](#en-us_topic_0079615038_ref458676991).

**Example response**:

```
{
    "kind": "Namespace",
    "apiVersion": "v1",
    "metadata": {
        "name": "test",
        "selfLink": "/api/v1/namespaces/test",
        "uid": "00468bb2-fcef-11e7-9193-fa163ecdc4fd",
        "resourceVersion": "95099",
        "creationTimestamp": "2018-01-19T08:01:49Z",
        "labels": {
            "name": "test"
        },
        "annotations": {
            "test": "woil"
        },
        "enable": true
    },
    "spec": {
        "finalizers": [
            "kubernetes"
        ]
    },
    "status": {
        "phase": "Active"
    }
}
```

## Status Code<a name="sa1abf64108814721a77b395a50d806c0"></a>

[Table 2](#en-us_topic_0079615038_table42343927)  describes the status code of this API.

**Table  2**  Status code

<a name="en-us_topic_0079615038_table42343927"></a>
<table><thead align="left"><tr id="row47812724"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p46755442201632"><a name="p46755442201632"></a><a name="p46755442201632"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p29094489201632"><a name="p29094489201632"></a><a name="p29094489201632"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row11627434"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0079615038_p2298077"><a name="en-us_topic_0079615038_p2298077"></a><a name="en-us_topic_0079615038_p2298077"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0079615038_p51926520"><a name="en-us_topic_0079615038_p51926520"></a><a name="en-us_topic_0079615038_p51926520"></a>This operation succeeds, and a Namespace resource object is returned.</p>
</td>
</tr>
</tbody>
</table>

For the description about status codes, see section  [Status Code](status-code.md).

