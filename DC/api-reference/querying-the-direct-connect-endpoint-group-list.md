# Querying the Direct Connect Endpoint Group List<a name="en-dc_topic_0055025337"></a>

## Function<a name="en-us_topic_0070658771_section17487184"></a>

This API is used to query the Direct Connect endpoint group list.

## URI<a name="en-us_topic_0070658771_section23166934"></a>

GET /v2.0/dcaas/dc-endpoint-groups

## Request<a name="en-us_topic_0070658771_section64582388"></a>

[Table 1](#en-us_topic_0070658771_table2198437322244)  lists the request parameter.

**Table  1**  Request parameter

<a name="en-us_topic_0070658771_table2198437322244"></a>
<table><thead align="left"><tr id="en-us_topic_0070658771_row4304807922244"><th class="cellrowborder" valign="top" width="19.388061193880613%" id="mcps1.2.5.1.1"><p id="en-us_topic_0070658771_p6505580022244"><a name="en-us_topic_0070658771_p6505580022244"></a><a name="en-us_topic_0070658771_p6505580022244"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21.42785721427857%" id="mcps1.2.5.1.2"><p id="en-us_topic_0070658771_p329696222244"><a name="en-us_topic_0070658771_p329696222244"></a><a name="en-us_topic_0070658771_p329696222244"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.2.5.1.3"><p id="en-us_topic_0070658771_p3257067222244"><a name="en-us_topic_0070658771_p3257067222244"></a><a name="en-us_topic_0070658771_p3257067222244"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="42.85571442855714%" id="mcps1.2.5.1.4"><p id="en-us_topic_0070658771_p5470821922244"><a name="en-us_topic_0070658771_p5470821922244"></a><a name="en-us_topic_0070658771_p5470821922244"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0070658771_row5451891922244"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0070658771_p6157819622316"><a name="en-us_topic_0070658771_p6157819622316"></a><a name="en-us_topic_0070658771_p6157819622316"></a>fields</p>
</td>
<td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0070658771_p757920222316"><a name="en-us_topic_0070658771_p757920222316"></a><a name="en-us_topic_0070658771_p757920222316"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0070658771_p4706384922316"><a name="en-us_topic_0070658771_p4706384922316"></a><a name="en-us_topic_0070658771_p4706384922316"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0070658771_p6336462419813"><a name="en-us_topic_0070658771_p6336462419813"></a><a name="en-us_topic_0070658771_p6336462419813"></a>Indicates the parameters expected to be returned.</p>
<p id="en-us_topic_0070658771_p970883222316"><a name="en-us_topic_0070658771_p970883222316"></a><a name="en-us_topic_0070658771_p970883222316"></a>If you do not specify it, all parameters will be returned.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0070658771_section44370581"></a>

[Table 2](#en-us_topic_0070658771_table33326591155835)  lists the response parameter.

**Table  2**  Response parameter

<a name="en-us_topic_0070658771_table33326591155835"></a>
<table><thead align="left"><tr id="en-us_topic_0070658771_row62151438155835"><th class="cellrowborder" valign="top" width="28.282828282828287%" id="mcps1.2.4.1.1"><p id="en-us_topic_0070658771_p1101727155835"><a name="en-us_topic_0070658771_p1101727155835"></a><a name="en-us_topic_0070658771_p1101727155835"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="29.292929292929294%" id="mcps1.2.4.1.2"><p id="en-us_topic_0070658771_p22131064155835"><a name="en-us_topic_0070658771_p22131064155835"></a><a name="en-us_topic_0070658771_p22131064155835"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="42.42424242424242%" id="mcps1.2.4.1.3"><p id="en-us_topic_0070658771_p45444133155835"><a name="en-us_topic_0070658771_p45444133155835"></a><a name="en-us_topic_0070658771_p45444133155835"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0070658771_row57096136155835"><td class="cellrowborder" valign="top" width="28.282828282828287%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0070658771_p61384275155835"><a name="en-us_topic_0070658771_p61384275155835"></a><a name="en-us_topic_0070658771_p61384275155835"></a>dc_endpoint_groups</p>
</td>
<td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0070658771_p6070383155835"><a name="en-us_topic_0070658771_p6070383155835"></a><a name="en-us_topic_0070658771_p6070383155835"></a>List data structure</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0070658771_p32229496155835"><a name="en-us_topic_0070658771_p32229496155835"></a><a name="en-us_topic_0070658771_p32229496155835"></a>Indicates the Direct Connect endpoint group list.</p>
</td>
</tr>
</tbody>
</table>

Description of field  **dc\_endpoint\_groups**

<a name="en-us_topic_0070658771_table14681450"></a>
<table><thead align="left"><tr id="en-us_topic_0070658771_row21069217"><th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.1.4.1.1"><p id="en-us_topic_0070658771_p28885026"><a name="en-us_topic_0070658771_p28885026"></a><a name="en-us_topic_0070658771_p28885026"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.1.4.1.2"><p id="en-us_topic_0070658771_p57985771"><a name="en-us_topic_0070658771_p57985771"></a><a name="en-us_topic_0070658771_p57985771"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="43%" id="mcps1.1.4.1.3"><p id="en-us_topic_0070658771_p4499576"><a name="en-us_topic_0070658771_p4499576"></a><a name="en-us_topic_0070658771_p4499576"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0070658771_row6614602622620"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0070658771_p34388252153945"><a name="en-us_topic_0070658771_p34388252153945"></a><a name="en-us_topic_0070658771_p34388252153945"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0070658771_p44319756153945"><a name="en-us_topic_0070658771_p44319756153945"></a><a name="en-us_topic_0070658771_p44319756153945"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0070658771_p46242397153945"><a name="en-us_topic_0070658771_p46242397153945"></a><a name="en-us_topic_0070658771_p46242397153945"></a>Indicates the ID of the Direct Connect endpoint group.</p>
</td>
</tr>
<tr id="en-us_topic_0070658771_row4620915422620"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0070658771_p5791372153945"><a name="en-us_topic_0070658771_p5791372153945"></a><a name="en-us_topic_0070658771_p5791372153945"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0070658771_p50586028153945"><a name="en-us_topic_0070658771_p50586028153945"></a><a name="en-us_topic_0070658771_p50586028153945"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0070658771_p27138588153945"><a name="en-us_topic_0070658771_p27138588153945"></a><a name="en-us_topic_0070658771_p27138588153945"></a>Indicates the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0070658771_row1146602622620"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0070658771_p42210218153945"><a name="en-us_topic_0070658771_p42210218153945"></a><a name="en-us_topic_0070658771_p42210218153945"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0070658771_p46108179153945"><a name="en-us_topic_0070658771_p46108179153945"></a><a name="en-us_topic_0070658771_p46108179153945"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0070658771_p43058442153945"><a name="en-us_topic_0070658771_p43058442153945"></a><a name="en-us_topic_0070658771_p43058442153945"></a>Indicates the name of the Direct Connect endpoint group.</p>
</td>
</tr>
<tr id="en-us_topic_0070658771_row2411573022620"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0070658771_p46605694153945"><a name="en-us_topic_0070658771_p46605694153945"></a><a name="en-us_topic_0070658771_p46605694153945"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0070658771_p21469085153945"><a name="en-us_topic_0070658771_p21469085153945"></a><a name="en-us_topic_0070658771_p21469085153945"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0070658771_p39581077153945"><a name="en-us_topic_0070658771_p39581077153945"></a><a name="en-us_topic_0070658771_p39581077153945"></a>Provides supplementary information about the Direct Connect endpoint group.</p>
</td>
</tr>
<tr id="en-us_topic_0070658771_row1544898622620"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0070658771_p59760215153945"><a name="en-us_topic_0070658771_p59760215153945"></a><a name="en-us_topic_0070658771_p59760215153945"></a>endpoints</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0070658771_p17154880153945"><a name="en-us_topic_0070658771_p17154880153945"></a><a name="en-us_topic_0070658771_p17154880153945"></a>List&lt;String&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0070658771_p8000696153945"><a name="en-us_topic_0070658771_p8000696153945"></a><a name="en-us_topic_0070658771_p8000696153945"></a>Indicates the list of the Direct Connect endpoints.</p>
</td>
</tr>
<tr id="en-us_topic_0070658771_row1078246722620"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0070658771_p59917406153945"><a name="en-us_topic_0070658771_p59917406153945"></a><a name="en-us_topic_0070658771_p59917406153945"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0070658771_p67030345153945"><a name="en-us_topic_0070658771_p67030345153945"></a><a name="en-us_topic_0070658771_p67030345153945"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0070658771_p1503526619832"><a name="en-us_topic_0070658771_p1503526619832"></a><a name="en-us_topic_0070658771_p1503526619832"></a>Indicates the type of the Direct Connect endpoint.</p>
<p id="en-us_topic_0070658771_p14175732153945"><a name="en-us_topic_0070658771_p14175732153945"></a><a name="en-us_topic_0070658771_p14175732153945"></a>The value is <strong id="b842352706185352"><a name="b842352706185352"></a><a name="b842352706185352"></a>cidr</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="en-us_topic_0070658771_section63790914"></a>

-   Example request

    1.  All parameters are returned:

    ```
    GET /v2.0/dcaas/dc-endpoint-groups
    ```

    1.  Filtered parameters are returned \(for example, the filter is ID\):

    ```
    GET /v2.0/dcaas/dc-endpoint-groups?id=6ecd9cf3-ca64-46c7-863f-f2eb1b9e838a
    ```


-   Example response

    ```
    {
         "dc_endpoint_groups" : [{
             "id" : "6ecd9cf3-ca64-46c7-863f-f2eb1b9e838a",
             "tenant_id" : "6fbe9263116a4b68818cf1edce16bc4f",
             "name" : "endpoint group1",
             "description" : "",
             "endpoints" : [ "10.2.0.0/24", "10.3.0.0/24" ],      
             "type" : "cidr"
        }]
    }
    ```


## Returned Value<a name="section1148118488575"></a>

For details, see section  [Common Returned Values](common-returned-values.md).

