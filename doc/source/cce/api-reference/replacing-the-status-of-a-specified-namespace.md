# Replacing the Status of a Specified Namespace<a name="cce_02_0054"></a>

## Function<a name="s78dfbbcdb6d145fa829c1398bdff12cb"></a>

This API is used to replace the status of a specified Namespace, that is, to modify the parameter values of the  **status**  field of the Namespace.

When the  **namespace.deletionTimestamp** is set to **null**, the **phase** can be set to **Active**  only.

When the  **namespace.deletionTimestamp** is not set to **null**, the **phase** can be set to **Terminating**  only.

## URI<a name="se9bde8d3a3a34d63a0b229178d79fb98"></a>

PUT /api/v1/namespaces/\{name\}/status

[Table 1](#en-us_topic_0079615057_table45307656)  describes the parameters of this API.

**Table  1**  Parameter description

<a name="en-us_topic_0079615057_table45307656"></a>
<table><thead align="left"><tr id="row38953736"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="en-us_topic_0079615057_p1136017"><a name="en-us_topic_0079615057_p1136017"></a><a name="en-us_topic_0079615057_p1136017"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p44972123201637"><a name="p44972123201637"></a><a name="p44972123201637"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p18863308201637"><a name="p18863308201637"></a><a name="p18863308201637"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row14679294"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0079615057_p48172185"><a name="en-us_topic_0079615057_p48172185"></a><a name="en-us_topic_0079615057_p48172185"></a>pretty</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0079615057_p9632925"><a name="en-us_topic_0079615057_p9632925"></a><a name="en-us_topic_0079615057_p9632925"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0079615057_p42069424"><a name="en-us_topic_0079615057_p42069424"></a><a name="en-us_topic_0079615057_p42069424"></a>If 'true', then the output is pretty printed.</p>
</td>
</tr>
<tr id="row51347269"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0079615057_p65488131"><a name="en-us_topic_0079615057_p65488131"></a><a name="en-us_topic_0079615057_p65488131"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0079615057_p2938434"><a name="en-us_topic_0079615057_p2938434"></a><a name="en-us_topic_0079615057_p2938434"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0079615057_p36686634"><a name="en-us_topic_0079615057_p36686634"></a><a name="en-us_topic_0079615057_p36686634"></a>Name of the Namespace.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0079615057_ref458679189"></a>

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
             "openshift.com/origin", 
             "kubernetes" 
         ] 
     }, 
     "status": { 
         "phase": "Terminating" 
     } 
 }
```

## Response<a name="s22137f9d150f4ebd8a284f006b9a87e9"></a>

**Response parameters**:

For the description about response parameters, see the parameter description in  [Request](#en-us_topic_0079615057_ref458679189).

**Example response**:

```
{
    "kind": "Namespace",
    "apiVersion": "v1",
    "metadata": {
        "name": "test",
        "selfLink": "/api/v1/namespaces/test/status",
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
        "phase": "Terminating"
    }
}
```

## Status Code<a name="sebf55a3e1af64b8abeda106aac36ac25"></a>

[Table 2](#en-us_topic_0079615057_table5115727)  describes the status code of this API.

**Table  2**  Status code

<a name="en-us_topic_0079615057_table5115727"></a>
<table><thead align="left"><tr id="row16339495"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p37586310201637"><a name="p37586310201637"></a><a name="p37586310201637"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p24592292201637"><a name="p24592292201637"></a><a name="p24592292201637"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row60797095"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0079615057_p25617672"><a name="en-us_topic_0079615057_p25617672"></a><a name="en-us_topic_0079615057_p25617672"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0079615057_p61765553"><a name="en-us_topic_0079615057_p61765553"></a><a name="en-us_topic_0079615057_p61765553"></a>This operation succeeds, and a Namespace resource object is returned.</p>
</td>
</tr>
</tbody>
</table>

For the description about status codes, see section  [Status Code](status-code.md).

