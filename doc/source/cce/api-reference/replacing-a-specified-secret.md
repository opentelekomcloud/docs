# Replacing a Specified Secret<a name="cce_02_0046"></a>

## Function<a name="s2fa7c6b09ad0449ebce13163ee876960"></a>

This API is used to replace the secret in a specified namespace.

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

>![](/images/icon-note.gif) **NOTE:**   
>-   When  **type**  is set to  **Opaque**, the key and value of  **data**  can be updated.  
>-   When  **type**  is not set to  **Opaque**, only the value of  **data**  can be updated.  

## URI<a name="se7a801b22ec44205a03503a15151ba92"></a>

PUT /api/v1/namespaces/\{namespace\}/secrets/\{name\}

[Table 1](#table195518420539)  describes the parameters of this API.

**Table  1**  Parameter description

<a name="table195518420539"></a>
<table><thead align="left"><tr id="row1895516485313"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p49558415538"><a name="p49558415538"></a><a name="p49558415538"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p495518435314"><a name="p495518435314"></a><a name="p495518435314"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p395615465319"><a name="p395615465319"></a><a name="p395615465319"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row159562040536"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p395612415535"><a name="p395612415535"></a><a name="p395612415535"></a>pretty</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p119561495319"><a name="p119561495319"></a><a name="p119561495319"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0079615031_p61052759"><a name="en-us_topic_0079615031_p61052759"></a><a name="en-us_topic_0079615031_p61052759"></a>If 'true', then the output is pretty printed.</p>
</td>
</tr>
<tr id="row1795634105314"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1195619465319"><a name="p1195619465319"></a><a name="p1195619465319"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p169561249530"><a name="p169561249530"></a><a name="p169561249530"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0079615031_p11408737"><a name="en-us_topic_0079615031_p11408737"></a><a name="en-us_topic_0079615031_p11408737"></a>Object name and auth scope, such as for teams and projects.</p>
</td>
</tr>
<tr id="row195616417532"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p9956104155314"><a name="p9956104155314"></a><a name="p9956104155314"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p795619475316"><a name="p795619475316"></a><a name="p795619475316"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0079615031_p13513185"><a name="en-us_topic_0079615031_p13513185"></a><a name="en-us_topic_0079615031_p13513185"></a>Name of the secret.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0079615031_ref458786529"></a>

**Request parameters**:

For the description about request parameters, see  [Table 2](creating-a-secret.md#en-us_topic_0079614900_ref458786458).

**Example request**:

```
{ 
   "apiVersion": "v1", 
   "kind": "Secret", 
   "metadata": { 
     "name": "mysecret" 
   }, 
   "type": "Opaque", 
   "data": { 
     "password": "******", #Encoded using Base64. Method: echo -n "to-be-encoded content" | base64
     "username": "*****" #Encoded using Base64. Method: echo -n "to-be-encoded content" | base64
   } 
 }
```

## Response<a name="s62e9d00c756e4ae99025f3a29117287f"></a>

**Response parameters**:

For the description about response parameters, see  [Table 2](creating-a-secret.md#en-us_topic_0079614900_ref458786458).

**Example Response**:

```
{
    "kind": "Secret",
    "apiVersion": "v1",
    "metadata": {
        "name": "mysecret",
        "namespace": "ns-12130306-s",
        "selfLink": "/api/v1/namespaces/ns-12130306-s/secrets/mysecret",
        "uid": "0bbfb314-dfb3-11e7-9c19-fa163e2d897b",
        "resourceVersion": "418375",
        "creationTimestamp": "2017-12-13T03:09:34Z",
        "enable": true
    },
    "data": {
        "password": "******",
        "username": "*****" 
    },
    "type": "Opaque",
    "httpcode": 200,
    "header": {
        "X-Frame-Options": "SAMEORIGIN",
        "Strict-Transport-Security": "max-age=31536000; includeSubdomains;",
        "Server": "Web Server",
        "X-Router-Status": "fresh,upstream return 200",
        "X-Content-Type-Options": "nosniff",
        "Connection": "keep-alive",
        "X-Download-Options": "noopen",
        "Set-Cookie": "******; Expires=Thu, 14-Dec-17 03:09:34 GMT; Domain=192.168.50.250; Path=/; Secure; HttpOnly",
        "Content-Length": "364",
        "X-XSS-Protection": "1; mode=block;",
        "Date": "Wed, 13 Dec 2017 03:09:34 GMT",
        "Content-Type": "application/json"
    }
}
```

## Status Code<a name="s0cae25a23bb14c80b7b9465f8da69cd7"></a>

[Table 2](#en-us_topic_0079615031_table64060950)  describes the status code of this API.

**Table  2**  Status code

<a name="en-us_topic_0079615031_table64060950"></a>
<table><thead align="left"><tr id="en-us_topic_0079615031_row64282674"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p57631252201621"><a name="p57631252201621"></a><a name="p57631252201621"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="en-us_topic_0079615031_p46527158"><a name="en-us_topic_0079615031_p46527158"></a><a name="en-us_topic_0079615031_p46527158"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0079615031_row10603493"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0079615031_p53576637"><a name="en-us_topic_0079615031_p53576637"></a><a name="en-us_topic_0079615031_p53576637"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0079615031_p44740325"><a name="en-us_topic_0079615031_p44740325"></a><a name="en-us_topic_0079615031_p44740325"></a>If the operation is successful, the updated secret is returned.</p>
</td>
</tr>
</tbody>
</table>

For the description about error status codes, see  [Status Code](status-code.md).

