# Updating a Specified Namespace<a name="cce_02_0057"></a>

## Function<a name="sc61ab07a6774411fb5e23e4e03f0e408"></a>

This API is used to update some information about a specified Namespace.

The following fields can be updated:

-   metadata.selfLink
-   metadata.resourceVersion
-   metadata.generation
-   metadata.creationTimestamp
-   metadata.deletionTimestamp
-   metadata.labels
-   metadata.generateName
-   metadata.annotations

## URI<a name="s5c4ede3df2254d4f9f948470a4167390"></a>

PATCH /api/v1/namespaces/\{name\}

[Table 1](#en-us_topic_0079614923_table59025204)  describes the parameters of this API.

**Table  1**  Parameter description

<a name="en-us_topic_0079614923_table59025204"></a>
<table><thead align="left"><tr id="row63400648"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="en-us_topic_0079614923_p35178835"><a name="en-us_topic_0079614923_p35178835"></a><a name="en-us_topic_0079614923_p35178835"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p22220716201640"><a name="p22220716201640"></a><a name="p22220716201640"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p55047609201640"><a name="p55047609201640"></a><a name="p55047609201640"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row19774328"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0079614923_p58216758"><a name="en-us_topic_0079614923_p58216758"></a><a name="en-us_topic_0079614923_p58216758"></a>pretty</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0079614923_p17936932"><a name="en-us_topic_0079614923_p17936932"></a><a name="en-us_topic_0079614923_p17936932"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0079614923_p43605354"><a name="en-us_topic_0079614923_p43605354"></a><a name="en-us_topic_0079614923_p43605354"></a>If 'true', then the output is pretty printed.</p>
</td>
</tr>
<tr id="row56903870"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0079614923_p45810748"><a name="en-us_topic_0079614923_p45810748"></a><a name="en-us_topic_0079614923_p45810748"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0079614923_p19683111"><a name="en-us_topic_0079614923_p19683111"></a><a name="en-us_topic_0079614923_p19683111"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0079614923_p50828134"><a name="en-us_topic_0079614923_p50828134"></a><a name="en-us_topic_0079614923_p50828134"></a>Name of the Namespace.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="s4d6a0dae909c4b3d800845ccdd482356"></a>

**Request parameters**:

For the description about the  **Content-Type** message header, see section [Patch Request Method Operation Description](patch-request-method-operation-description.md).

**Example request**:

```
Content-Type: application/json-patch+json
[ 
 { 
     "op": "add", 
     "path": "/spec/finalizers/0", 
     "value": "kubernetes" 
 } 
 ]
```

## Response<a name="s89a8214dd2d7407393601192524b8ada"></a>

**Response parameters**:

For the description about response parameters, see  [Request](creating-a-namespace.md#en-us_topic_0079615062_ref458675483)

**Example response**:

```
{ 
   "kind": "Namespace", 
   "apiVersion": "v1", 
   "metadata": { 
     "name": "helloworld", 
     "selfLink": "/api/v1/namespaces/helloworld", 
     "uid": "1298d13a-5d34-11e6-aeb9-286ed488fafe", 
     "resourceVersion": "3043", 
     "creationTimestamp": "2016-08-08T06:48:11Z" 
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

## Status Code<a name="s49d4dd78f7d2431d8a003bd92b596d76"></a>

[Table 2](#en-us_topic_0079614923_table61464796)  describes the status code of this API.

**Table  2**  Status code

<a name="en-us_topic_0079614923_table61464796"></a>
<table><thead align="left"><tr id="row24265995"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p6837280201640"><a name="p6837280201640"></a><a name="p6837280201640"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p16948825201640"><a name="p16948825201640"></a><a name="p16948825201640"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row37389755"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0079614923_p8671305"><a name="en-us_topic_0079614923_p8671305"></a><a name="en-us_topic_0079614923_p8671305"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0079614923_p31287108"><a name="en-us_topic_0079614923_p31287108"></a><a name="en-us_topic_0079614923_p31287108"></a>This operation succeeds, and a Namespace resource object is returned.</p>
</td>
</tr>
</tbody>
</table>

For the description about status codes, see section  [Status Code](status-code.md).

