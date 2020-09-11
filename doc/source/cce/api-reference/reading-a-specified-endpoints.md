# Reading a Specified Endpoints<a name="cce_02_0061"></a>

## Function<a name="en-us_topic_0079615072_section885082"></a>

This API is used to read a specified Endpoints object under a Namespace.

## URI<a name="s4c063734e7b04b8aa1818085c9fdd5f3"></a>

GET /api/v1/namespaces/\{namespace\}/endpoints/\{name\}

[Table 1](#en-us_topic_0079615072_table12571834)  describes the parameters of this API.

**Table  1**  Parameter description

<a name="en-us_topic_0079615072_table12571834"></a>
<table><thead align="left"><tr id="row52268049"><th class="cellrowborder" valign="top" width="33%" id="mcps1.2.4.1.1"><p id="en-us_topic_0079615072_p5853587"><a name="en-us_topic_0079615072_p5853587"></a><a name="en-us_topic_0079615072_p5853587"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="p24602870201644"><a name="p24602870201644"></a><a name="p24602870201644"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="42%" id="mcps1.2.4.1.3"><p id="en-us_topic_0079615072_p19119237"><a name="en-us_topic_0079615072_p19119237"></a><a name="en-us_topic_0079615072_p19119237"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row5154373"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0079615072_p14851049"><a name="en-us_topic_0079615072_p14851049"></a><a name="en-us_topic_0079615072_p14851049"></a>pretty</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0079615072_p62084314"><a name="en-us_topic_0079615072_p62084314"></a><a name="en-us_topic_0079615072_p62084314"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0079615072_p62773503"><a name="en-us_topic_0079615072_p62773503"></a><a name="en-us_topic_0079615072_p62773503"></a>If 'true', then the output is pretty printed.</p>
</td>
</tr>
<tr id="row28090616"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0079615072_p60747463"><a name="en-us_topic_0079615072_p60747463"></a><a name="en-us_topic_0079615072_p60747463"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0079615072_p21597503"><a name="en-us_topic_0079615072_p21597503"></a><a name="en-us_topic_0079615072_p21597503"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0079615072_p4567303"><a name="en-us_topic_0079615072_p4567303"></a><a name="en-us_topic_0079615072_p4567303"></a>Object name and auth scope, such as for teams and projects.</p>
</td>
</tr>
<tr id="row41105728"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0079615072_p41229700"><a name="en-us_topic_0079615072_p41229700"></a><a name="en-us_topic_0079615072_p41229700"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0079615072_p51271404"><a name="en-us_topic_0079615072_p51271404"></a><a name="en-us_topic_0079615072_p51271404"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0079615072_p59343073"><a name="en-us_topic_0079615072_p59343073"></a><a name="en-us_topic_0079615072_p59343073"></a>Name of the Endpoints.</p>
</td>
</tr>
<tr id="row13544153421"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0079615072_p145446584212"><a name="en-us_topic_0079615072_p145446584212"></a><a name="en-us_topic_0079615072_p145446584212"></a>exact</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0079615072_p15454594218"><a name="en-us_topic_0079615072_p15454594218"></a><a name="en-us_topic_0079615072_p15454594218"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0079615072_p135451953426"><a name="en-us_topic_0079615072_p135451953426"></a><a name="en-us_topic_0079615072_p135451953426"></a>Should the export be exact. Exact export maintains cluster-specific fields like 'Namespace'.</p>
</td>
</tr>
<tr id="row798577421"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0079615072_p10989774219"><a name="en-us_topic_0079615072_p10989774219"></a><a name="en-us_topic_0079615072_p10989774219"></a>export</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0079615072_p298187154210"><a name="en-us_topic_0079615072_p298187154210"></a><a name="en-us_topic_0079615072_p298187154210"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0079615072_p898677425"><a name="en-us_topic_0079615072_p898677425"></a><a name="en-us_topic_0079615072_p898677425"></a>Should this value be exported. Export strips fields that a user cannot specify.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="se5dc3a3d39a34f22a7353e5b56820ee1"></a>

N/A

## Response<a name="sb016aaee185e4c39889395b7b34f7968"></a>

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
     "uid": "81b1503d-5960-11e6-b444-286ed488fafe", 
     "resourceVersion": "18186", 
     "creationTimestamp": "2016-08-03T09:56:10Z" 
   }, 
   "subsets": [ 
     { 
       "addresses": [ 
         { 
           "ip": "172.16.106.152" 
         }, 
         { 
           "ip": "172.16.79.157" 
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

## Status Code<a name="sf826b071d47f4d51bc560ff6f2ef1fbf"></a>

[Table 2](#en-us_topic_0079615072_table12672824)  describes the status code of this API.

**Table  2**  Status code

<a name="en-us_topic_0079615072_table12672824"></a>
<table><thead align="left"><tr id="row17662689"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p39753582201644"><a name="p39753582201644"></a><a name="p39753582201644"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="en-us_topic_0079615072_p55008403"><a name="en-us_topic_0079615072_p55008403"></a><a name="en-us_topic_0079615072_p55008403"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row26495667"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0079615072_p65774263"><a name="en-us_topic_0079615072_p65774263"></a><a name="en-us_topic_0079615072_p65774263"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0079615072_p26115080"><a name="en-us_topic_0079615072_p26115080"></a><a name="en-us_topic_0079615072_p26115080"></a>This operation succeeds, and an Endpoint resource object is returned.</p>
</td>
</tr>
</tbody>
</table>

For the description about status codes, see section  [Status Code](status-code.md).

