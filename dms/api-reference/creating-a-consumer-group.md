# Creating a Consumer Group<a name="EN-US_TOPIC_0128036889"></a>

## Function<a name="section44497505"></a>

This API is used to create a consumer group.

Multiple consumer groups can be created for a queue at a time.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>After you create a consumer group, it takes 1s to 3s to initialize the system. If you operate the queue immediately after creating the consumer group, the consumption may fail. You are advised to perform these operations three seconds after creating the queue.  

## URI<a name="section64933228"></a>

POST /v1.0/\{project\_id\}/queues/\{queue\_id\}/groups

[Table 1](#d0e1744)  describes the parameters of this API.

**Table  1**  Parameters

<a name="d0e1744"></a>
<table><thead align="left"><tr id="row7657338"><th class="cellrowborder" valign="top" width="18.60813918608139%" id="mcps1.2.5.1.1"><p id="p16264673"><a name="p16264673"></a><a name="p16264673"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.84851514848515%" id="mcps1.2.5.1.2"><p id="p42370099"><a name="p42370099"></a><a name="p42370099"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="19.73802619738026%" id="mcps1.2.5.1.3"><p id="p5067421217428"><a name="p5067421217428"></a><a name="p5067421217428"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="46.8053194680532%" id="mcps1.2.5.1.4"><p id="p9426010"><a name="p9426010"></a><a name="p9426010"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row25309374"><td class="cellrowborder" valign="top" width="18.60813918608139%" headers="mcps1.2.5.1.1 "><p id="p36793414"><a name="p36793414"></a><a name="p36793414"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.84851514848515%" headers="mcps1.2.5.1.2 "><p id="p27476571"><a name="p27476571"></a><a name="p27476571"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="19.73802619738026%" headers="mcps1.2.5.1.3 "><p id="p1619719917428"><a name="p1619719917428"></a><a name="p1619719917428"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="46.8053194680532%" headers="mcps1.2.5.1.4 "><p id="p11009764"><a name="p11009764"></a><a name="p11009764"></a>Indicates the ID of a project.</p>
</td>
</tr>
<tr id="row31979016"><td class="cellrowborder" valign="top" width="18.60813918608139%" headers="mcps1.2.5.1.1 "><p id="p40163483"><a name="p40163483"></a><a name="p40163483"></a>queue_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.84851514848515%" headers="mcps1.2.5.1.2 "><p id="p32016662"><a name="p32016662"></a><a name="p32016662"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="19.73802619738026%" headers="mcps1.2.5.1.3 "><p id="p6370723617428"><a name="p6370723617428"></a><a name="p6370723617428"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="46.8053194680532%" headers="mcps1.2.5.1.4 "><p id="p43212834"><a name="p43212834"></a><a name="p43212834"></a>Indicates the ID of a queue.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section47528147"></a>

**Request parameters**

[Table 2](#table21618074)  describes the request parameters.

**Table  2**  Request parameters

<a name="table21618074"></a>
<table><thead align="left"><tr id="row43909159"><th class="cellrowborder" valign="top" width="18.7981201879812%" id="mcps1.2.5.1.1"><p id="p66980994"><a name="p66980994"></a><a name="p66980994"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.91830816918308%" id="mcps1.2.5.1.2"><p id="p56751409"><a name="p56751409"></a><a name="p56751409"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="17.858214178582145%" id="mcps1.2.5.1.3"><p id="p33461405"><a name="p33461405"></a><a name="p33461405"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="46.42535746425357%" id="mcps1.2.5.1.4"><p id="p26019245"><a name="p26019245"></a><a name="p26019245"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3401105218108"><td class="cellrowborder" valign="top" width="18.7981201879812%" headers="mcps1.2.5.1.1 "><p id="p7401185211019"><a name="p7401185211019"></a><a name="p7401185211019"></a>groups</p>
</td>
<td class="cellrowborder" valign="top" width="16.91830816918308%" headers="mcps1.2.5.1.2 "><p id="p240115291010"><a name="p240115291010"></a><a name="p240115291010"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="17.858214178582145%" headers="mcps1.2.5.1.3 "><p id="p6538811151117"><a name="p6538811151117"></a><a name="p6538811151117"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="46.42535746425357%" headers="mcps1.2.5.1.4 "><p id="p4402145220108"><a name="p4402145220108"></a><a name="p4402145220108"></a>Indicates the consumer group information.</p>
<p id="p766542920491"><a name="p766542920491"></a><a name="p766542920491"></a>A maximum of three consumer groups can be created for a queue. If there are more than three consumer groups in the request, the request will fail and consumer groups cannot be created.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  groups parameter description

<a name="table27981048111112"></a>
<table><thead align="left"><tr id="row780234851110"><th class="cellrowborder" valign="top" width="18.7981201879812%" id="mcps1.2.5.1.1"><p id="p4804154811118"><a name="p4804154811118"></a><a name="p4804154811118"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.91830816918308%" id="mcps1.2.5.1.2"><p id="p380684831120"><a name="p380684831120"></a><a name="p380684831120"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="17.858214178582145%" id="mcps1.2.5.1.3"><p id="p48071348171119"><a name="p48071348171119"></a><a name="p48071348171119"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="46.42535746425357%" id="mcps1.2.5.1.4"><p id="p1280824811114"><a name="p1280824811114"></a><a name="p1280824811114"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1781574815113"><td class="cellrowborder" valign="top" width="18.7981201879812%" headers="mcps1.2.5.1.1 "><p id="p1181774817117"><a name="p1181774817117"></a><a name="p1181774817117"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.91830816918308%" headers="mcps1.2.5.1.2 "><p id="p181918484111"><a name="p181918484111"></a><a name="p181918484111"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.858214178582145%" headers="mcps1.2.5.1.3 "><p id="p58191448101112"><a name="p58191448101112"></a><a name="p58191448101112"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="46.42535746425357%" headers="mcps1.2.5.1.4 "><p id="p6820164818115"><a name="p6820164818115"></a><a name="p6820164818115"></a>Indicates the name of a consumer group.</p>
<p id="p28227482115"><a name="p28227482115"></a><a name="p28227482115"></a>The value is a string of 1 to 32 characters that contain letters, digits, hyphens (-), and underscores (_).</p>
</td>
</tr>
</tbody>
</table>

**Example request**

```
{
  "groups" : [{
      "name" : "group-aa"
    }
  ]
}
```

## Response<a name="section25100141"></a>

**Response parameters**

[Table 4](#d0e1855)  describes the response parameters.

**Table  4**  Response parameters

<a name="d0e1855"></a>
<table><thead align="left"><tr id="row56350302"><th class="cellrowborder" valign="top" width="20.8%" id="mcps1.2.4.1.1"><p id="p971734"><a name="p971734"></a><a name="p971734"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="22.68%" id="mcps1.2.4.1.2"><p id="p11601606"><a name="p11601606"></a><a name="p11601606"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="56.52%" id="mcps1.2.4.1.3"><p id="p206039"><a name="p206039"></a><a name="p206039"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row16689200"><td class="cellrowborder" valign="top" width="20.8%" headers="mcps1.2.4.1.1 "><p id="p9647994"><a name="p9647994"></a><a name="p9647994"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="22.68%" headers="mcps1.2.4.1.2 "><p id="p43290077"><a name="p43290077"></a><a name="p43290077"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.52%" headers="mcps1.2.4.1.3 "><p id="p16835328"><a name="p16835328"></a><a name="p16835328"></a>Indicates the consumer group ID.</p>
</td>
</tr>
<tr id="row17300225"><td class="cellrowborder" valign="top" width="20.8%" headers="mcps1.2.4.1.1 "><p id="p59140967"><a name="p59140967"></a><a name="p59140967"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="22.68%" headers="mcps1.2.4.1.2 "><p id="p25689059"><a name="p25689059"></a><a name="p25689059"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.52%" headers="mcps1.2.4.1.3 "><p id="p439002"><a name="p439002"></a><a name="p439002"></a>Indicates the name of a consumer group.</p>
</td>
</tr>
</tbody>
</table>

**Example response**

```
{
  "groups" : [{
      "id" : "g-02fb1974-9be1-4eee-8448-ed2d3e89884a",
      "name" : "group-aa"
    }
  ]
}
```

## Status Code<a name="section24574685"></a>

[Table 5](#d0e1909)  lists the status code indicating that the operation is successful. For details about the status codes indicating that the operation fails, see  [Status Code](status-code.md).

**Table  5**  Status code

<a name="d0e1909"></a>
<table><thead align="left"><tr id="row45240216"><th class="cellrowborder" valign="top" width="21.240000000000002%" id="mcps1.2.3.1.1"><p id="p40578897"><a name="p40578897"></a><a name="p40578897"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="78.75999999999999%" id="mcps1.2.3.1.2"><p id="p65665194"><a name="p65665194"></a><a name="p65665194"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row17280459"><td class="cellrowborder" valign="top" width="21.240000000000002%" headers="mcps1.2.3.1.1 "><p id="p59250555145847"><a name="p59250555145847"></a><a name="p59250555145847"></a>201</p>
</td>
<td class="cellrowborder" valign="top" width="78.75999999999999%" headers="mcps1.2.3.1.2 "><p id="p30222983"><a name="p30222983"></a><a name="p30222983"></a>The consumer group is created successfully.</p>
</td>
</tr>
</tbody>
</table>

