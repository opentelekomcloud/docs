# Updating a Specified Service<a name="cce_02_0031"></a>

## Function<a name="s79a46a3bbf834e65a768cf502c42239e"></a>

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

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >The update priority of the value of  **spec.type**  is as follows:  **LoadBalancer**  \>  **NodePort**  \>  **ClusterIP**. When  **spec.type**  is set to  **ClusterIP**, it can be updated to  **LoadBalancer**  or  **NodePort**. When  **spec.type**  is set to  **Nodeport**, it can be updated to  **LoadBalancer**. When  **spec.type**  is set to  **LoadBalancer**, it cannot be updated.   

-   spec.port
-   spec.selector
-   spec.externalIPs
-   spec.loadBalancerIP
-   spec.loadBalancerSourceRanges

## URI<a name="s2bcf1feaf0bc43ee938e4fcc63b3849c"></a>

PATCH /api/v1/namespaces/\{namespace\}/services/\{name\}

[Table 1](#en-us_topic_0079614894_table66627661)  describes the parameters of this API.

**Table  1**  Parameter description

<a name="en-us_topic_0079614894_table66627661"></a>
<table><thead align="left"><tr id="en-us_topic_0079614894_row3622792"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="en-us_topic_0079614894_p25010772"><a name="en-us_topic_0079614894_p25010772"></a><a name="en-us_topic_0079614894_p25010772"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p38778720203035"><a name="p38778720203035"></a><a name="p38778720203035"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="en-us_topic_0079614894_p14503239"><a name="en-us_topic_0079614894_p14503239"></a><a name="en-us_topic_0079614894_p14503239"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0079614894_row33911744"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0079614894_p62496749"><a name="en-us_topic_0079614894_p62496749"></a><a name="en-us_topic_0079614894_p62496749"></a>pretty</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0079614894_p29071927"><a name="en-us_topic_0079614894_p29071927"></a><a name="en-us_topic_0079614894_p29071927"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0079614894_p6015877"><a name="en-us_topic_0079614894_p6015877"></a><a name="en-us_topic_0079614894_p6015877"></a>If 'true', then the output is pretty printed.</p>
</td>
</tr>
<tr id="en-us_topic_0079614894_row23698059"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0079614894_p40494599"><a name="en-us_topic_0079614894_p40494599"></a><a name="en-us_topic_0079614894_p40494599"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0079614894_p58837112"><a name="en-us_topic_0079614894_p58837112"></a><a name="en-us_topic_0079614894_p58837112"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0079614894_p1076806"><a name="en-us_topic_0079614894_p1076806"></a><a name="en-us_topic_0079614894_p1076806"></a>Object name and auth scope, such as for teams and projects.</p>
</td>
</tr>
<tr id="en-us_topic_0079614894_row9691259"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0079614894_p46794527"><a name="en-us_topic_0079614894_p46794527"></a><a name="en-us_topic_0079614894_p46794527"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0079614894_p32260306"><a name="en-us_topic_0079614894_p32260306"></a><a name="en-us_topic_0079614894_p32260306"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0079614894_p62948031"><a name="en-us_topic_0079614894_p62948031"></a><a name="en-us_topic_0079614894_p62948031"></a>Name of the Service.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="s6972b4d28cf840328e55c95e180ccd87"></a>

**Request parameters:**

For the description about the  **Content-Type**  field, see  [Patch Request Method Operation Description](patch-request-method-operation-description.md).

For the description about request parameters, see  [Table 2](creating-a-service.md#en-us_topic_0079615000_ref458759328).

**Example request:**

```
Content-Type: application/strategic-merge-patch+json
```

```
 { 
     "spec": { 
         "ports": [ 
             { 
                 "name": "ttt1", 
                 "protocol": "TCP", 
                 "port": 8765, 
                 "targetPort": 9376 
             }, 
             { 
                 "name": "ttt2", 
                 "protocol": "TCP", 
                 "port": 8765, 
                 "targetPort": 9076 
             } 
         ], 
         "selector": { 
             "app": "example" 
         } 
     } 
 }
```

## Response<a name="sab68cc958da442f79a8bdd2c90aae544"></a>

**Response parameters:**

For the description about response parameters, see  [Table 2](obtaining-a-specified-service.md#en-us_topic_0079614941_ref458765062).

**Example response:**

```
{ 
   "kind": "Service", 
   "apiVersion": "v1", 
   "metadata": { 
     "name": "raoy", 
     "namespace": "default", 
     "selfLink": "/api/v1/namespaces/default/services/raoy", 
     "uid": "e0d681b7-5d17-11e6-aeb9-286ed488fafe", 
     "resourceVersion": "1602", 
     "creationTimestamp": "2016-08-08T03:26:21Z" 
   }, 
   "spec": { 
     "ports": [ 
       { 
         "name": "ttt1", 
         "protocol": "TCP", 
         "port": 8765, 
         "targetPort": 9376 
       }, 
       { 
         "name": "ttt2", 
         "protocol": "TCP", 
         "port": 8765, 
         "targetPort": 9076 
       } 
     ], 
     "selector": { 
       "app": "example" 
     }, 
     "clusterIP": "10.0.0.193", 
     "type": "ClusterIP", 
     "sessionAffinity": "None" 
   }, 
   "status": { 
     "loadBalancer": {} 
   } 
 }
```

## Status Code<a name="s3f10ef39263445cabc5b032a11c66233"></a>

[Table 2](#en-us_topic_0079614894_table62778039)  describes the status code of this API.

**Table  2**  Status code

<a name="en-us_topic_0079614894_table62778039"></a>
<table><thead align="left"><tr id="en-us_topic_0079614894_row29754946"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p50518267203035"><a name="p50518267203035"></a><a name="p50518267203035"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="en-us_topic_0079614894_p2516162"><a name="en-us_topic_0079614894_p2516162"></a><a name="en-us_topic_0079614894_p2516162"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0079614894_row2482606"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0079614894_p66873365"><a name="en-us_topic_0079614894_p66873365"></a><a name="en-us_topic_0079614894_p66873365"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0079614894_p48033505"><a name="en-us_topic_0079614894_p48033505"></a><a name="en-us_topic_0079614894_p48033505"></a>This operation succeeds, and a Service resource object is returned.</p>
</td>
</tr>
</tbody>
</table>

For the description about error status codes, see  [Status Code](status-code.md).

