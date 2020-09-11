# Querying a Direct Connect Endpoint Group<a name="en-dc_topic_0055025339"></a>

## Function<a name="en-us_topic_0070658800_section17487184"></a>

This API is used to query a Direct Connect endpoint group.

## URI<a name="en-us_topic_0070658800_section23166934"></a>

GET /v2.0/dcaas/dc-endpoint-groups/\{endpoint\_group\_id\}

**Table  1**  Parameter description

<a name="table1297211334365"></a>
<table><thead align="left"><tr id="row6972123313361"><th class="cellrowborder" valign="top" width="19.388061193880613%" id="mcps1.2.5.1.1"><p id="p7972133143612"><a name="p7972133143612"></a><a name="p7972133143612"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21.42785721427857%" id="mcps1.2.5.1.2"><p id="p997213303616"><a name="p997213303616"></a><a name="p997213303616"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.2.5.1.3"><p id="p597215330365"><a name="p597215330365"></a><a name="p597215330365"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="42.85571442855714%" id="mcps1.2.5.1.4"><p id="p69722339368"><a name="p69722339368"></a><a name="p69722339368"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row14972143317361"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.5.1.1 "><p id="p0972633143618"><a name="p0972633143618"></a><a name="p0972633143618"></a>endpoint_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.2 "><p id="p5972633193614"><a name="p5972633193614"></a><a name="p5972633193614"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p7972193343618"><a name="p7972193343618"></a><a name="p7972193343618"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.5.1.4 "><p id="p59808335369"><a name="p59808335369"></a><a name="p59808335369"></a>Indicates the ID of the Direct Connect endpoint group.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0070658800_section64582388"></a>

[Table 2](#en-us_topic_0070658800_table2198437322244)  lists the request parameter.

**Table  2**  Request parameter

<a name="en-us_topic_0070658800_table2198437322244"></a>
<table><thead align="left"><tr id="en-us_topic_0070658800_row4304807922244"><th class="cellrowborder" valign="top" width="19.388061193880613%" id="mcps1.2.5.1.1"><p id="en-us_topic_0070658800_p6505580022244"><a name="en-us_topic_0070658800_p6505580022244"></a><a name="en-us_topic_0070658800_p6505580022244"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21.42785721427857%" id="mcps1.2.5.1.2"><p id="en-us_topic_0070658800_p329696222244"><a name="en-us_topic_0070658800_p329696222244"></a><a name="en-us_topic_0070658800_p329696222244"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.2.5.1.3"><p id="en-us_topic_0070658800_p3257067222244"><a name="en-us_topic_0070658800_p3257067222244"></a><a name="en-us_topic_0070658800_p3257067222244"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="42.85571442855714%" id="mcps1.2.5.1.4"><p id="en-us_topic_0070658800_p5470821922244"><a name="en-us_topic_0070658800_p5470821922244"></a><a name="en-us_topic_0070658800_p5470821922244"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0070658800_row5451891922244"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0070658800_p5675124985931"><a name="en-us_topic_0070658800_p5675124985931"></a><a name="en-us_topic_0070658800_p5675124985931"></a>endpoint_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0070658800_p757920222316"><a name="en-us_topic_0070658800_p757920222316"></a><a name="en-us_topic_0070658800_p757920222316"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0070658800_p4706384922316"><a name="en-us_topic_0070658800_p4706384922316"></a><a name="en-us_topic_0070658800_p4706384922316"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0070658800_p970883222316"><a name="en-us_topic_0070658800_p970883222316"></a><a name="en-us_topic_0070658800_p970883222316"></a>Indicates the ID of the Direct Connect endpoint group.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0070658800_section44370581"></a>

[Table 3](#en-us_topic_0070658800_table33326591155835)  lists the response parameter.

**Table  3**  Response parameter

<a name="en-us_topic_0070658800_table33326591155835"></a>
<table><thead align="left"><tr id="en-us_topic_0070658800_row62151438155835"><th class="cellrowborder" valign="top" width="23.04%" id="mcps1.2.4.1.1"><p id="en-us_topic_0070658800_p1101727155835"><a name="en-us_topic_0070658800_p1101727155835"></a><a name="en-us_topic_0070658800_p1101727155835"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25.759999999999998%" id="mcps1.2.4.1.2"><p id="en-us_topic_0070658800_p22131064155835"><a name="en-us_topic_0070658800_p22131064155835"></a><a name="en-us_topic_0070658800_p22131064155835"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.2%" id="mcps1.2.4.1.3"><p id="en-us_topic_0070658800_p45444133155835"><a name="en-us_topic_0070658800_p45444133155835"></a><a name="en-us_topic_0070658800_p45444133155835"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0070658800_row57096136155835"><td class="cellrowborder" valign="top" width="23.04%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0070658800_p61384275155835"><a name="en-us_topic_0070658800_p61384275155835"></a><a name="en-us_topic_0070658800_p61384275155835"></a>dc_endpoint_group</p>
</td>
<td class="cellrowborder" valign="top" width="25.759999999999998%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0070658800_p6070383155835"><a name="en-us_topic_0070658800_p6070383155835"></a><a name="en-us_topic_0070658800_p6070383155835"></a>Dictionary data structure</p>
</td>
<td class="cellrowborder" valign="top" width="51.2%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0070658800_p32229496155835"><a name="en-us_topic_0070658800_p32229496155835"></a><a name="en-us_topic_0070658800_p32229496155835"></a>Indicates the <strong id="b84235270692654"><a name="b84235270692654"></a><a name="b84235270692654"></a>dc_endpoint_group</strong> object.</p>
</td>
</tr>
</tbody>
</table>

Description of field  **dc\_endpoint\_group**

<a name="en-us_topic_0070658800_table14681450"></a>
<table><thead align="left"><tr id="en-us_topic_0070658800_row21069217"><th class="cellrowborder" valign="top" width="23.169999999999998%" id="mcps1.1.4.1.1"><p id="en-us_topic_0070658800_p28885026"><a name="en-us_topic_0070658800_p28885026"></a><a name="en-us_topic_0070658800_p28885026"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25.61%" id="mcps1.1.4.1.2"><p id="en-us_topic_0070658800_p57985771"><a name="en-us_topic_0070658800_p57985771"></a><a name="en-us_topic_0070658800_p57985771"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.22%" id="mcps1.1.4.1.3"><p id="en-us_topic_0070658800_p4499576"><a name="en-us_topic_0070658800_p4499576"></a><a name="en-us_topic_0070658800_p4499576"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0070658800_row6614602622620"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0070658800_p53899497155718"><a name="en-us_topic_0070658800_p53899497155718"></a><a name="en-us_topic_0070658800_p53899497155718"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0070658800_p27469194155718"><a name="en-us_topic_0070658800_p27469194155718"></a><a name="en-us_topic_0070658800_p27469194155718"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0070658800_p46888307155718"><a name="en-us_topic_0070658800_p46888307155718"></a><a name="en-us_topic_0070658800_p46888307155718"></a>Indicates the ID of the Direct Connect endpoint group.</p>
</td>
</tr>
<tr id="en-us_topic_0070658800_row4620915422620"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0070658800_p9842188155718"><a name="en-us_topic_0070658800_p9842188155718"></a><a name="en-us_topic_0070658800_p9842188155718"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0070658800_p66208886155718"><a name="en-us_topic_0070658800_p66208886155718"></a><a name="en-us_topic_0070658800_p66208886155718"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0070658800_p48740843155718"><a name="en-us_topic_0070658800_p48740843155718"></a><a name="en-us_topic_0070658800_p48740843155718"></a>Indicates the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0070658800_row1146602622620"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0070658800_p43439215155718"><a name="en-us_topic_0070658800_p43439215155718"></a><a name="en-us_topic_0070658800_p43439215155718"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0070658800_p51799105155718"><a name="en-us_topic_0070658800_p51799105155718"></a><a name="en-us_topic_0070658800_p51799105155718"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0070658800_p24601733155718"><a name="en-us_topic_0070658800_p24601733155718"></a><a name="en-us_topic_0070658800_p24601733155718"></a>Indicates the name of the Direct Connect endpoint group.</p>
</td>
</tr>
<tr id="en-us_topic_0070658800_row2411573022620"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0070658800_p61357604155718"><a name="en-us_topic_0070658800_p61357604155718"></a><a name="en-us_topic_0070658800_p61357604155718"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0070658800_p30641944155718"><a name="en-us_topic_0070658800_p30641944155718"></a><a name="en-us_topic_0070658800_p30641944155718"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0070658800_p42009298155718"><a name="en-us_topic_0070658800_p42009298155718"></a><a name="en-us_topic_0070658800_p42009298155718"></a>Provides supplementary information about the Direct Connect endpoint group.</p>
</td>
</tr>
<tr id="en-us_topic_0070658800_row1544898622620"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0070658800_p6403812155718"><a name="en-us_topic_0070658800_p6403812155718"></a><a name="en-us_topic_0070658800_p6403812155718"></a>endpoints</p>
</td>
<td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0070658800_p15708548155718"><a name="en-us_topic_0070658800_p15708548155718"></a><a name="en-us_topic_0070658800_p15708548155718"></a>List&lt;String&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0070658800_p21827696155718"><a name="en-us_topic_0070658800_p21827696155718"></a><a name="en-us_topic_0070658800_p21827696155718"></a>Indicates the list of the Direct Connect endpoints.</p>
</td>
</tr>
<tr id="en-us_topic_0070658800_row1078246722620"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0070658800_p9214955155718"><a name="en-us_topic_0070658800_p9214955155718"></a><a name="en-us_topic_0070658800_p9214955155718"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0070658800_p4021487155718"><a name="en-us_topic_0070658800_p4021487155718"></a><a name="en-us_topic_0070658800_p4021487155718"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0070658800_p62809153191456"><a name="en-us_topic_0070658800_p62809153191456"></a><a name="en-us_topic_0070658800_p62809153191456"></a>Indicates the type of the Direct Connect endpoint.</p>
<p id="en-us_topic_0070658800_p17050059155718"><a name="en-us_topic_0070658800_p17050059155718"></a><a name="en-us_topic_0070658800_p17050059155718"></a>The value is <strong id="b842352706185352"><a name="b842352706185352"></a><a name="b842352706185352"></a>cidr</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="en-us_topic_0070658800_section63790914"></a>

-   Example request

    ```
    GET /v2.0/dcaas/dc-endpoint-groups/{endpoint_group_id}
    ```


-   Example response

    ```
    {
        "dc_endpoint_group" : {
             "id" : "6ecd9cf3-ca64-46c7-863f-f2eb1b9e838a",
             "tenant_id" : "6fbe9263116a4b68818cf1edce16bc4f",
             "name" : "endpoint group1",
             "description" : "",
             "endpoints" : [ "10.2.0.0/24", "10.3.0.0/24" ],      
             "type" : "cidr"
        }
    }
    ```


## Returned Value<a name="section12113171955820"></a>

For details, see section  [Common Returned Values](common-returned-values.md).

