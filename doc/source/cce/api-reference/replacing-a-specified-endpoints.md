# Replacing a Specified Endpoints<a name="cce_02_0062"></a>

## Function<a name="sc37501af9b7044f4ae092cb00715a785"></a>

This API is used to replace a specified Endpoints resource object under a Namespace.

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
-   subnet.\*

## URI<a name="s86f7cb5e4d6541d0914295e89856a8f2"></a>

PUT /api/v1/namespaces/\{namespace\}/endpoints/\{name\}

[Table 1](#en-us_topic_0079614957_table31235479)  describes the parameters of this API.

**Table  1**  Parameter description

<a name="en-us_topic_0079614957_table31235479"></a>
<table><thead align="left"><tr id="row3156250"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="en-us_topic_0079614957_p54329699"><a name="en-us_topic_0079614957_p54329699"></a><a name="en-us_topic_0079614957_p54329699"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p811366201648"><a name="p811366201648"></a><a name="p811366201648"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p65720655201648"><a name="p65720655201648"></a><a name="p65720655201648"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row45300995"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0079614957_p45501950"><a name="en-us_topic_0079614957_p45501950"></a><a name="en-us_topic_0079614957_p45501950"></a>pretty</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0079614957_p61779338"><a name="en-us_topic_0079614957_p61779338"></a><a name="en-us_topic_0079614957_p61779338"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0079614957_p38070478"><a name="en-us_topic_0079614957_p38070478"></a><a name="en-us_topic_0079614957_p38070478"></a>If 'true', then the output is pretty printed.</p>
</td>
</tr>
<tr id="row18472885"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0079614957_p19908716"><a name="en-us_topic_0079614957_p19908716"></a><a name="en-us_topic_0079614957_p19908716"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0079614957_p1993291"><a name="en-us_topic_0079614957_p1993291"></a><a name="en-us_topic_0079614957_p1993291"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0079614957_p27238907"><a name="en-us_topic_0079614957_p27238907"></a><a name="en-us_topic_0079614957_p27238907"></a>Object name and auth scope, such as for teams and projects.</p>
</td>
</tr>
<tr id="row43823577"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0079614957_p60048837"><a name="en-us_topic_0079614957_p60048837"></a><a name="en-us_topic_0079614957_p60048837"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0079614957_p32117589"><a name="en-us_topic_0079614957_p32117589"></a><a name="en-us_topic_0079614957_p32117589"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0079614957_p51387889"><a name="en-us_topic_0079614957_p51387889"></a><a name="en-us_topic_0079614957_p51387889"></a>Name of the Endpoints.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0079614957_ref458707209"></a>

**Request parameters**:

For the description about request parameters, see  [Table 2](creating-an-endpoints-object.md#en-us_topic_0079614955_ref458759912).

**Example request**:

```
{ 
   "kind": "Endpoints", 
   "apiVersion": "v1", 
   "metadata": { 
     "name": "cluster-test" 
   }, 
   "subsets": [ 
     { 
       "addresses": [ 
         { 
           "ip": "172.16.106.150" 
         } 
       ], 
       "ports": [ 
         { 
           "port": 1 
         } 
       ] 
     }, 
     { 
       "addresses": [ 
         { 
           "ip": "172.16.79.223" 
         } 
       ], 
       "ports": [ 
         { 
           "port": 1 
         } 
       ] 
     },{ 
       "addresses": [ 
         { 
           "ip": "172.16.106.154" 
         } 
       ], 
       "ports": [ 
         { 
           "port": 1 
         } 
       ] 
     } 
   ] 
 }
```

## Response<a name="s53cdaea7a7a849248695c65ad5d83aa2"></a>

**Response parameters**:

For the description about response parameters, see the parameter description in  [Request](#en-us_topic_0079614957_ref458707209).

**Example response**:

```
{ 
   "kind": "Endpoints", 
   "apiVersion": "v1", 
   "metadata": { 
     "name": "cluster-test", 
     "namespace": "default", 
     "selfLink": "/api/v1/namespaces/default/endpoints/cluster-test", 
     "uid": "88a7230f-5d36-11e6-aeb9-286ed488fafe", 
     "resourceVersion": "3203", 
     "creationTimestamp": "2016-08-08T07:05:48Z" 
   }, 
   "subsets": [ 
     { 
       "addresses": [ 
         { 
           "ip": "172.16.106.150" 
         }, 
         { 
           "ip": "172.16.106.154" 
         }, 
         { 
           "ip": "172.16.79.223" 
         } 
       ], 
       "ports": [ 
         { 
           "port": 1, 
           "protocol": "TCP" 
         } 
       ] 
     } 
   ] 
 }
```

## Status Code<a name="s3fa127a04c544cefb712cbbcb09fc524"></a>

[Table 2](#en-us_topic_0079614957_table12683857)  describes the status code of this API.

**Table  2**  Status code

<a name="en-us_topic_0079614957_table12683857"></a>
<table><thead align="left"><tr id="row49320909"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p12685718201648"><a name="p12685718201648"></a><a name="p12685718201648"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p20910256201648"><a name="p20910256201648"></a><a name="p20910256201648"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row41609976"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0079614957_p14964925"><a name="en-us_topic_0079614957_p14964925"></a><a name="en-us_topic_0079614957_p14964925"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0079614957_p4199435"><a name="en-us_topic_0079614957_p4199435"></a><a name="en-us_topic_0079614957_p4199435"></a>This operation succeeds, and a group of Endpoint resource objects is returned.</p>
</td>
</tr>
</tbody>
</table>

For the description about status codes, see section  [Status Code](status-code.md).

