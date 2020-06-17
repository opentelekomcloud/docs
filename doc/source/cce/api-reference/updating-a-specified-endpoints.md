# Updating a Specified Endpoints<a name="cce_02_0065"></a>

## Function<a name="sac12fa31d2e14eb987df783ddacf3321"></a>

This API is used to update some specified Endpoints resource objects under a Namespace.

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

## URI<a name="sf83f35293a2a41608535afbee14767bf"></a>

PATCH /api/v1/namespaces/\{namespace\}/endpoints/\{name\}

[Table 1](#en-us_topic_0079614972_table5045213)  describes the parameters of this API.

**Table  1**  Parameter description

<a name="en-us_topic_0079614972_table5045213"></a>
<table><thead align="left"><tr id="row25584516"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p59079892"><a name="p59079892"></a><a name="p59079892"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p20741957"><a name="p20741957"></a><a name="p20741957"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p2376958"><a name="p2376958"></a><a name="p2376958"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row58315944"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p25971051"><a name="p25971051"></a><a name="p25971051"></a>pretty</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p23280366"><a name="p23280366"></a><a name="p23280366"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p6661465"><a name="p6661465"></a><a name="p6661465"></a>If 'true', then the output is pretty printed.</p>
</td>
</tr>
<tr id="row19216572"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p13038474"><a name="p13038474"></a><a name="p13038474"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p49483440"><a name="p49483440"></a><a name="p49483440"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p48735703"><a name="p48735703"></a><a name="p48735703"></a>Object name and auth scope, such as for teams and projects.</p>
</td>
</tr>
<tr id="row35968146"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p27738717"><a name="p27738717"></a><a name="p27738717"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p32243580"><a name="p32243580"></a><a name="p32243580"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p61593176"><a name="p61593176"></a><a name="p61593176"></a>Name of the Endpoints.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="s657fd059fab74bb29d05f8f4cac1d327"></a>

**Request parameters**:

For the description about the  **Content-Type** message header, see section [Patch Request Method Operation Description](patch-request-method-operation-description.md).

**Example request**:

```
Content-Type: application/merge-patch+json
```

```
{
    "subsets": [
        {
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

## Response<a name="s6b95f47c4ccf4cbd996626e8962eb127"></a>

**Response parameters**:

For the description about response parameters, see  [Table 2](creating-an-endpoints-object.md#en-us_topic_0079614955_ref458759912).

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
     "resourceVersion": "3182", 
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
           "ip": "172.16.79.123" 
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

## Status Code<a name="s06eee481d5564d248bb167cb6c41cd47"></a>

[Table 2](#en-us_topic_0079614972_table6009104)  describes the status code of this API.

**Table  2**  Status code

<a name="en-us_topic_0079614972_table6009104"></a>
<table><thead align="left"><tr id="row2835298"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p28332581"><a name="p28332581"></a><a name="p28332581"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p13237733"><a name="p13237733"></a><a name="p13237733"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row65623433"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p13897850"><a name="p13897850"></a><a name="p13897850"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p51984031"><a name="p51984031"></a><a name="p51984031"></a>This operation succeeds, and an Endpoint resource object is returned.</p>
</td>
</tr>
</tbody>
</table>

For the description about status codes, see section  [Status Code](status-code.md).

