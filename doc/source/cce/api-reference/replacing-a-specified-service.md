# Replacing a Specified Service<a name="cce_02_0028"></a>

## Function<a name="s7f16b6de4e854b61a40ec42af83c7a24"></a>

This API is used to replace a specified service.

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
-   spec.externalTrafficPolicy
-   spec.sessionAffinity
-   spec.type

    >![](/images/icon-note.gif) **NOTE:**   
    >The update priority of the value of  **spec.type**  is as follows:  **LoadBalancer**  \>  **NodePort**  \>  **ClusterIP**. When  **spec.type**  is set to  **ClusterIP**, it can be updated to  **LoadBalancer**  or  **NodePort**. When  **spec.type**  is set to  **Nodeport**, it can be updated to  **LoadBalancer**. When  **spec.type**  is set to  **LoadBalancer**, it cannot be updated.   

-   spec.port
-   spec.selector
-   spec.externalIPs
-   spec.loadBalancerIP
-   spec.loadBalancerSourceRanges

## URI<a name="sd473d9d2d140486eb450698f18eb16e1"></a>

PUT /api/v1/namespaces/\{namespace\}/services/\{name\}

[Table 1](#en-us_topic_0079615066_table59996030)  describes the parameters of this API.

**Table  1**  Parameter description

<a name="en-us_topic_0079615066_table59996030"></a>
<table><thead align="left"><tr id="en-us_topic_0079615066_row4196075"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="en-us_topic_0079615066_p4337788"><a name="en-us_topic_0079615066_p4337788"></a><a name="en-us_topic_0079615066_p4337788"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p45173014195352"><a name="p45173014195352"></a><a name="p45173014195352"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="en-us_topic_0079615066_p6069154"><a name="en-us_topic_0079615066_p6069154"></a><a name="en-us_topic_0079615066_p6069154"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0079615066_row21839497"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0079615066_p24168795"><a name="en-us_topic_0079615066_p24168795"></a><a name="en-us_topic_0079615066_p24168795"></a>pretty</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0079615066_p11515394"><a name="en-us_topic_0079615066_p11515394"></a><a name="en-us_topic_0079615066_p11515394"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0079615066_p60331750"><a name="en-us_topic_0079615066_p60331750"></a><a name="en-us_topic_0079615066_p60331750"></a>If 'true', then the output is pretty printed.</p>
</td>
</tr>
<tr id="en-us_topic_0079615066_row52637298"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0079615066_p35762716"><a name="en-us_topic_0079615066_p35762716"></a><a name="en-us_topic_0079615066_p35762716"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0079615066_p11098866"><a name="en-us_topic_0079615066_p11098866"></a><a name="en-us_topic_0079615066_p11098866"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0079615066_p26592990"><a name="en-us_topic_0079615066_p26592990"></a><a name="en-us_topic_0079615066_p26592990"></a>Object name and auth scope, such as for teams and projects.</p>
</td>
</tr>
<tr id="en-us_topic_0079615066_row38010318"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0079615066_p58936947"><a name="en-us_topic_0079615066_p58936947"></a><a name="en-us_topic_0079615066_p58936947"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0079615066_p9163425"><a name="en-us_topic_0079615066_p9163425"></a><a name="en-us_topic_0079615066_p9163425"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0079615066_p4039935"><a name="en-us_topic_0079615066_p4039935"></a><a name="en-us_topic_0079615066_p4039935"></a>Name of the Service.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0079615066_ref458765758"></a>

**Request parameters:**

For the description about request parameters, see  [Table 2](creating-a-service.md#en-us_topic_0079615000_ref458759328).

**Example request:**

```
{ 
   "kind": "Service", 
   "apiVersion": "v1", 
   "metadata": { 
     "name": "myapp", 
     "resourceVersion": "683" 
   }, 
   "spec": { 
     "ports": [{ 
       "port": 80, 
       "targetPort": 80 
     }], 
     "selector": { 
       "app": "example" 
     }, 
     "clusterIP": "10.0.0.139" 
   } 
 }
```

## Response<a name="s45b51f911829442cae934355300a440d"></a>

**Response parameters:**

For the description about response parameters, see  [Request](#en-us_topic_0079615066_ref458765758).

**Example response:**

```
{ 
   "kind": "Service", 
   "apiVersion": "v1", 
   "metadata": { 
     "name": "myapp", 
     "namespace": "default", 
     "selfLink": "/api/v1/namespaces/default/services/myapp", 
     "uid": "58b5ca7c-5d12-11e6-aeb9-286ed488fafe", 
     "resourceVersion": "1204", 
     "creationTimestamp": "2016-08-08T02:46:46Z" 
   }, 
   "spec": { 
     "ports": [ 
       { 
         "protocol": "TCP", 
         "port": 80, 
         "targetPort": 80 
       } 
   ], 
     "selector": { 
       "app": "example" 
     }, 
     "clusterIP": "10.0.0.139", 
     "type": "ClusterIP", 
     "sessionAffinity": "None" 
   }, 
   "status": { 
     "loadBalancer": {} 
   } 
 }
```

## Status Code<a name="s5ba1a0225c3c4dd8948fdd7a6c393876"></a>

[Table 2](#en-us_topic_0079615066_table3093358)  describes the status code of this API.

**Table  2**  Status code

<a name="en-us_topic_0079615066_table3093358"></a>
<table><thead align="left"><tr id="en-us_topic_0079615066_row66569734"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p53137435195352"><a name="p53137435195352"></a><a name="p53137435195352"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="en-us_topic_0079615066_p19540130"><a name="en-us_topic_0079615066_p19540130"></a><a name="en-us_topic_0079615066_p19540130"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0079615066_row39246670"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0079615066_p24863727"><a name="en-us_topic_0079615066_p24863727"></a><a name="en-us_topic_0079615066_p24863727"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0079615066_p696045"><a name="en-us_topic_0079615066_p696045"></a><a name="en-us_topic_0079615066_p696045"></a>This operation succeeds, and a Service resource object is returned.</p>
</td>
</tr>
</tbody>
</table>

For the description about error status codes, see  [Status Code](status-code.md).

