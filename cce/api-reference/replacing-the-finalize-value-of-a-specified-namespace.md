# Replacing the Finalize Value of a Specified Namespace<a name="cce_02_0055"></a>

## Function<a name="s5e1060eaef574f08a8dd061ec40e6157"></a>

This API is used to replace the  **finalize**  value of a specified Namespace.

## URI<a name="s7acf80d17ff84f0c9c2b7eb00f80eb00"></a>

PUT /api/v1/namespaces/\{name\}/finalize

[Table 1](#en-us_topic_0079615020_table40478462)  describes the parameters of this API.

**Table  1**  Parameter description

<a name="en-us_topic_0079615020_table40478462"></a>
<table><thead align="left"><tr id="row34476226"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="en-us_topic_0079615020_p41110918"><a name="en-us_topic_0079615020_p41110918"></a><a name="en-us_topic_0079615020_p41110918"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p4951575721146"><a name="p4951575721146"></a><a name="p4951575721146"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p5135336221146"><a name="p5135336221146"></a><a name="p5135336221146"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row66066743"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0079615020_p49805933"><a name="en-us_topic_0079615020_p49805933"></a><a name="en-us_topic_0079615020_p49805933"></a>pretty</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0079615020_p7748772"><a name="en-us_topic_0079615020_p7748772"></a><a name="en-us_topic_0079615020_p7748772"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0079615020_p23670787"><a name="en-us_topic_0079615020_p23670787"></a><a name="en-us_topic_0079615020_p23670787"></a>If 'true', then the output is pretty printed.</p>
</td>
</tr>
<tr id="row12872118"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0079615020_p36008632"><a name="en-us_topic_0079615020_p36008632"></a><a name="en-us_topic_0079615020_p36008632"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0079615020_p31018066"><a name="en-us_topic_0079615020_p31018066"></a><a name="en-us_topic_0079615020_p31018066"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0079615020_p29435437"><a name="en-us_topic_0079615020_p29435437"></a><a name="en-us_topic_0079615020_p29435437"></a>Name of the Namespace.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0079615020_ref458679422"></a>

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

## Response<a name="s3398a68b6b4a4acea2b731d527a51b83"></a>

**Response parameters**:

For the description about response parameters, see the parameter description in  [Request](#en-us_topic_0079615020_ref458679422).

**Example response**:

```
{
    "kind": "Namespace",
    "apiVersion": "v1",
    "metadata": {
        "name": "test",
        "selfLink": "/api/v1/namespaces/test/finalize",
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

## Status Code<a name="s7e7c27ac6cea4d3da1df2bfdcf6c65f5"></a>

[Table 2](#en-us_topic_0079615020_table28761840)  describes the status code of this API.

**Table  2**  Status code

<a name="en-us_topic_0079615020_table28761840"></a>
<table><thead align="left"><tr id="row27551015"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p665304121146"><a name="p665304121146"></a><a name="p665304121146"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p202540921146"><a name="p202540921146"></a><a name="p202540921146"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row61624137"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0079615020_p25499238"><a name="en-us_topic_0079615020_p25499238"></a><a name="en-us_topic_0079615020_p25499238"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0079615020_p52172387"><a name="en-us_topic_0079615020_p52172387"></a><a name="en-us_topic_0079615020_p52172387"></a>This operation succeeds, and a Namespace resource object is returned.</p>
</td>
</tr>
</tbody>
</table>

For the description about status codes, see section  [Status Code](status-code.md).

