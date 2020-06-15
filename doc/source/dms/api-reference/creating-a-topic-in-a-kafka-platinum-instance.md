# Creating a Topic in a Kafka Platinum Instance<a name="EN-US_TOPIC_0128036928"></a>

## Function<a name="section281017251256"></a>

This API is available for only Kafka instances.

This API is used to create a topic in a Kafka instance.

## URI<a name="section133368463119"></a>

POST /v1.0/\{project\_id\}/instances/\{instance\_id\}/topics

[Table 1](#table5338194611119)  describes the parameters.

**Table  1**  Parameter description

<a name="table5338194611119"></a>
<table><thead align="left"><tr id="row84911646141118"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.1"><p id="p1449164691113"><a name="p1449164691113"></a><a name="p1449164691113"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.2"><p id="p2491164601115"><a name="p2491164601115"></a><a name="p2491164601115"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.5.1.3"><p id="p144911646191112"><a name="p144911646191112"></a><a name="p144911646191112"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="59%" id="mcps1.2.5.1.4"><p id="p74911246171112"><a name="p74911246171112"></a><a name="p74911246171112"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row144911946201115"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.1 "><p id="p349174618112"><a name="p349174618112"></a><a name="p349174618112"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p949114651114"><a name="p949114651114"></a><a name="p949114651114"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="p1949117464112"><a name="p1949117464112"></a><a name="p1949117464112"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.5.1.4 "><p id="p849114621111"><a name="p849114621111"></a><a name="p849114621111"></a>Indicates the ID of a project.</p>
</td>
</tr>
<tr id="row54910467110"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.1 "><p id="p6491174620116"><a name="p6491174620116"></a><a name="p6491174620116"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p2491184671114"><a name="p2491184671114"></a><a name="p2491184671114"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="p1549164610114"><a name="p1549164610114"></a><a name="p1549164610114"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.5.1.4 "><p id="p3491144613110"><a name="p3491144613110"></a><a name="p3491144613110"></a>Indicates the instance ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section8345124651115"></a>

**Request parameters**

[Table 2](#table14347154691119)  describes the parameter.

**Table  2**  Parameter description

<a name="table14347154691119"></a>
<table><thead align="left"><tr id="row154923465114"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="p204921146111112"><a name="p204921146111112"></a><a name="p204921146111112"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.2"><p id="p13492104681119"><a name="p13492104681119"></a><a name="p13492104681119"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.5.1.3"><p id="p13492124651111"><a name="p13492124651111"></a><a name="p13492124651111"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="53%" id="mcps1.2.5.1.4"><p id="p9492154601120"><a name="p9492154601120"></a><a name="p9492154601120"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row18492646191114"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p749214615115"><a name="p749214615115"></a><a name="p749214615115"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="p449294631114"><a name="p449294631114"></a><a name="p449294631114"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="p16492846161110"><a name="p16492846161110"></a><a name="p16492846161110"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><p id="p12492124681111"><a name="p12492124681111"></a><a name="p12492124681111"></a>Indicates the name of a topic. A topic name consists of 4 to 64 characters, starts with a letter, and contains only letters, hyphens (-), underscores (_), and digits.</p>
</td>
</tr>
<tr id="row1749224618119"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p449224615114"><a name="p449224615114"></a><a name="p449224615114"></a>partition</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="p164921446121117"><a name="p164921446121117"></a><a name="p164921446121117"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="p12492204613114"><a name="p12492204613114"></a><a name="p12492204613114"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><p id="p9494846151117"><a name="p9494846151117"></a><a name="p9494846151117"></a>Indicates the number of topic partitions, which is used to set the number of concurrently consumed messages.</p>
<p id="p74941746121117"><a name="p74941746121117"></a><a name="p74941746121117"></a>Value range: 1–20. Default value: <strong id="b11262153841617"><a name="b11262153841617"></a><a name="b11262153841617"></a>3</strong>.</p>
</td>
</tr>
<tr id="row3494346171114"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p04947464119"><a name="p04947464119"></a><a name="p04947464119"></a>replication</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="p154941346121115"><a name="p154941346121115"></a><a name="p154941346121115"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="p1449420463110"><a name="p1449420463110"></a><a name="p1449420463110"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><p id="p1149414601112"><a name="p1149414601112"></a><a name="p1149414601112"></a>Indicates the number of replicas, which is configured to ensure data reliability.</p>
<p id="p16494646181112"><a name="p16494646181112"></a><a name="p16494646181112"></a>Value range: 1–3. Default value: <strong id="b8302226162311"><a name="b8302226162311"></a><a name="b8302226162311"></a>3</strong>.</p>
</td>
</tr>
<tr id="row5439123414418"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p126894217446"><a name="p126894217446"></a><a name="p126894217446"></a>sync_replication</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="p12681342184417"><a name="p12681342184417"></a><a name="p12681342184417"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="p102687426440"><a name="p102687426440"></a><a name="p102687426440"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><p id="p62689423441"><a name="p62689423441"></a><a name="p62689423441"></a>Indicates whether to enable synchronous replication. After this function is enabled, the <strong id="b612714530233"><a name="b612714530233"></a><a name="b612714530233"></a>acks</strong> parameter on the producer client must be set to <strong id="b163774562239"><a name="b163774562239"></a><a name="b163774562239"></a>–1</strong>. Otherwise, this parameter does not take effect.</p>
<p id="p1822717394320"><a name="p1822717394320"></a><a name="p1822717394320"></a>Options:</p>
<a name="ul2046195510424"></a><a name="ul2046195510424"></a><ul id="ul2046195510424"><li><strong id="b862519318216"><a name="b862519318216"></a><a name="b862519318216"></a>true</strong>: enable</li><li><strong id="b161724916224"><a name="b161724916224"></a><a name="b161724916224"></a>false</strong>: disable</li></ul>
<p id="p19830254247"><a name="p19830254247"></a><a name="p19830254247"></a>By default, synchronous replication is disabled. If <strong id="b3317171162320"><a name="b3317171162320"></a><a name="b3317171162320"></a>replication</strong> is set to <strong id="b3318513102317"><a name="b3318513102317"></a><a name="b3318513102317"></a>1</strong>, this parameter can only be set to <strong id="b818381715233"><a name="b818381715233"></a><a name="b818381715233"></a>false</strong>.</p>
</td>
</tr>
<tr id="row4494846201111"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p6494134661119"><a name="p6494134661119"></a><a name="p6494134661119"></a>retention_time</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="p194941446151118"><a name="p194941446151118"></a><a name="p194941446151118"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="p549413462117"><a name="p549413462117"></a><a name="p549413462117"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><p id="p8494184661118"><a name="p8494184661118"></a><a name="p8494184661118"></a>Indicates the retention period of a message. Its default value is <strong id="b1195453154817"><a name="b1195453154817"></a><a name="b1195453154817"></a>72</strong>.</p>
<p id="p12494546161116"><a name="p12494546161116"></a><a name="p12494546161116"></a>Value range: 1–168. Default value: <strong id="b197211520162413"><a name="b197211520162413"></a><a name="b197211520162413"></a>72</strong>. Unit: hour.</p>
</td>
</tr>
<tr id="row1049444651117"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p114941646151117"><a name="p114941646151117"></a><a name="p114941646151117"></a>sync_message_flush</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="p2049413469114"><a name="p2049413469114"></a><a name="p2049413469114"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="p049494615110"><a name="p049494615110"></a><a name="p049494615110"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><p id="p19494144617119"><a name="p19494144617119"></a><a name="p19494144617119"></a>Indicates whether to enable synchronous flushing. Default value: <strong id="b151438394241"><a name="b151438394241"></a><a name="b151438394241"></a>false</strong>. Synchronous flushing compromises performance.</p>
</td>
</tr>
</tbody>
</table>

**Example request**

```
{
  "id" : "haha", 
  "partition" : 3, 
  "replication" : 3, 
  "sync_replication " : true, 
  "retention_time" : 10, 
  "sync_message_flush" : true
}
```

## Response<a name="section837314461114"></a>

**Response parameters**

[Table 3](#table113758463117)  describes the parameter.

**Table  3**  Parameter description

<a name="table113758463117"></a>
<table><thead align="left"><tr id="row049524619114"><th class="cellrowborder" valign="top" width="23.23%" id="mcps1.2.4.1.1"><p id="p154951446141113"><a name="p154951446141113"></a><a name="p154951446141113"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21.21%" id="mcps1.2.4.1.2"><p id="p9495174614117"><a name="p9495174614117"></a><a name="p9495174614117"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="55.559999999999995%" id="mcps1.2.4.1.3"><p id="p949515469114"><a name="p949515469114"></a><a name="p949515469114"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row16495194631111"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p649554610116"><a name="p649554610116"></a><a name="p649554610116"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="21.21%" headers="mcps1.2.4.1.2 "><p id="p19495184671120"><a name="p19495184671120"></a><a name="p19495184671120"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.559999999999995%" headers="mcps1.2.4.1.3 "><p id="p44956464114"><a name="p44956464114"></a><a name="p44956464114"></a>Indicates the name of a topic.</p>
</td>
</tr>
</tbody>
</table>

**Example response**

```
{  
"id": "haha"
}
```

## Status Code<a name="section5381204691118"></a>

[Table 4](#table4381154610118)  describes the status code of successful operations. For details about other status codes, see  [Status Code](status-code.md).

**Table  4**  Status code

<a name="table4381154610118"></a>
<table><thead align="left"><tr id="row549534661115"><th class="cellrowborder" valign="top" width="15.15%" id="mcps1.2.3.1.1"><p id="p13495134691117"><a name="p13495134691117"></a><a name="p13495134691117"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="84.85000000000001%" id="mcps1.2.3.1.2"><p id="p11496174618117"><a name="p11496174618117"></a><a name="p11496174618117"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row14965461118"><td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.2.3.1.1 "><p id="p1449610463118"><a name="p1449610463118"></a><a name="p1449610463118"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="84.85000000000001%" headers="mcps1.2.3.1.2 "><p id="p14496204612119"><a name="p14496204612119"></a><a name="p14496204612119"></a>The topic is created successfully.</p>
</td>
</tr>
</tbody>
</table>

