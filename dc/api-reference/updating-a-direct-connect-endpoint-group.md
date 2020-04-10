# Updating a Direct Connect Endpoint Group<a name="en-dc_topic_0055025340"></a>

## Function<a name="en-us_topic_0070658694_section3515885216025"></a>

This API is used to update a Direct Connect endpoint group.

## URI<a name="en-us_topic_0070658694_section616356616025"></a>

PUT /v2.0/dcaas/dc-endpoint-groups/\{endpoint\_group\_id\}

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

## Request<a name="en-us_topic_0070658694_section1877718216025"></a>

[Table 2](#en-us_topic_0070658694_table49278871155710)  lists the request parameter.

**Table  2**  Request parameter

<a name="en-us_topic_0070658694_table49278871155710"></a>
<table><thead align="left"><tr id="en-us_topic_0070658694_row34163686155710"><th class="cellrowborder" valign="top" width="26.27262726272627%" id="mcps1.2.5.1.1"><p id="en-us_topic_0070658694_p15795191155710"><a name="en-us_topic_0070658694_p15795191155710"></a><a name="en-us_topic_0070658694_p15795191155710"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.641464146414643%" id="mcps1.2.5.1.2"><p id="en-us_topic_0070658694_p4342096155710"><a name="en-us_topic_0070658694_p4342096155710"></a><a name="en-us_topic_0070658694_p4342096155710"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="16.14161416141614%" id="mcps1.2.5.1.3"><p id="en-us_topic_0070658694_p16165530155710"><a name="en-us_topic_0070658694_p16165530155710"></a><a name="en-us_topic_0070658694_p16165530155710"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="42.94429442944294%" id="mcps1.2.5.1.4"><p id="en-us_topic_0070658694_p34339581155710"><a name="en-us_topic_0070658694_p34339581155710"></a><a name="en-us_topic_0070658694_p34339581155710"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0070658694_row30042656155710"><td class="cellrowborder" valign="top" width="26.27262726272627%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0070658694_p17536043155710"><a name="en-us_topic_0070658694_p17536043155710"></a><a name="en-us_topic_0070658694_p17536043155710"></a>dc_endpoint_group</p>
</td>
<td class="cellrowborder" valign="top" width="14.641464146414643%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0070658694_p11133383155710"><a name="en-us_topic_0070658694_p11133383155710"></a><a name="en-us_topic_0070658694_p11133383155710"></a>Dictionary data structure</p>
</td>
<td class="cellrowborder" valign="top" width="16.14161416141614%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0070658694_p29388827155710"><a name="en-us_topic_0070658694_p29388827155710"></a><a name="en-us_topic_0070658694_p29388827155710"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="42.94429442944294%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0070658694_p31684816155710"><a name="en-us_topic_0070658694_p31684816155710"></a><a name="en-us_topic_0070658694_p31684816155710"></a>Indicates the <strong id="b842352706201450"><a name="b842352706201450"></a><a name="b842352706201450"></a>dc_endpoint_group</strong> object.</p>
</td>
</tr>
</tbody>
</table>

Description of field  **dc\_endpoint\_group**

<a name="en-us_topic_0070658694_table4017731716025"></a>
<table><thead align="left"><tr id="en-us_topic_0070658694_row2231098116025"><th class="cellrowborder" valign="top" width="26.52734726527347%" id="mcps1.1.5.1.1"><p id="en-us_topic_0070658694_p1547301516025"><a name="en-us_topic_0070658694_p1547301516025"></a><a name="en-us_topic_0070658694_p1547301516025"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.1.5.1.2"><p id="en-us_topic_0070658694_p6012563716025"><a name="en-us_topic_0070658694_p6012563716025"></a><a name="en-us_topic_0070658694_p6012563716025"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.1.5.1.3"><p id="en-us_topic_0070658694_p1893695816025"><a name="en-us_topic_0070658694_p1893695816025"></a><a name="en-us_topic_0070658694_p1893695816025"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="42.85571442855714%" id="mcps1.1.5.1.4"><p id="en-us_topic_0070658694_p2817987216025"><a name="en-us_topic_0070658694_p2817987216025"></a><a name="en-us_topic_0070658694_p2817987216025"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0070658694_row33904501145431"><td class="cellrowborder" valign="top" width="26.52734726527347%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0070658694_p61111525145431"><a name="en-us_topic_0070658694_p61111525145431"></a><a name="en-us_topic_0070658694_p61111525145431"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0070658694_p51086506145431"><a name="en-us_topic_0070658694_p51086506145431"></a><a name="en-us_topic_0070658694_p51086506145431"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0070658694_p44366307145431"><a name="en-us_topic_0070658694_p44366307145431"></a><a name="en-us_topic_0070658694_p44366307145431"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0070658694_p36901113145431"><a name="en-us_topic_0070658694_p36901113145431"></a><a name="en-us_topic_0070658694_p36901113145431"></a>Provides supplementary information about the Direct Connect endpoint group.</p>
</td>
</tr>
<tr id="en-us_topic_0070658694_row63419490145431"><td class="cellrowborder" valign="top" width="26.52734726527347%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0070658694_p57365869145431"><a name="en-us_topic_0070658694_p57365869145431"></a><a name="en-us_topic_0070658694_p57365869145431"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0070658694_p16123817145431"><a name="en-us_topic_0070658694_p16123817145431"></a><a name="en-us_topic_0070658694_p16123817145431"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0070658694_p27720644181110"><a name="en-us_topic_0070658694_p27720644181110"></a><a name="en-us_topic_0070658694_p27720644181110"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0070658694_p24796658145431"><a name="en-us_topic_0070658694_p24796658145431"></a><a name="en-us_topic_0070658694_p24796658145431"></a>Indicates the name of the Direct Connect endpoint group.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0070658694_section5537288616025"></a>

[Table 3](#en-us_topic_0070658694_table33326591155835)  lists the response parameter.

**Table  3**  Response parameter

<a name="en-us_topic_0070658694_table33326591155835"></a>
<table><thead align="left"><tr id="en-us_topic_0070658694_row62151438155835"><th class="cellrowborder" valign="top" width="31.683168316831683%" id="mcps1.2.4.1.1"><p id="en-us_topic_0070658694_p1101727155835"><a name="en-us_topic_0070658694_p1101727155835"></a><a name="en-us_topic_0070658694_p1101727155835"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25.742574257425744%" id="mcps1.2.4.1.2"><p id="en-us_topic_0070658694_p22131064155835"><a name="en-us_topic_0070658694_p22131064155835"></a><a name="en-us_topic_0070658694_p22131064155835"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="42.57425742574257%" id="mcps1.2.4.1.3"><p id="en-us_topic_0070658694_p45444133155835"><a name="en-us_topic_0070658694_p45444133155835"></a><a name="en-us_topic_0070658694_p45444133155835"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0070658694_row57096136155835"><td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0070658694_p61384275155835"><a name="en-us_topic_0070658694_p61384275155835"></a><a name="en-us_topic_0070658694_p61384275155835"></a>dc_endpoint_group</p>
</td>
<td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0070658694_p6070383155835"><a name="en-us_topic_0070658694_p6070383155835"></a><a name="en-us_topic_0070658694_p6070383155835"></a>Dictionary data structure</p>
</td>
<td class="cellrowborder" valign="top" width="42.57425742574257%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0070658694_p32229496155835"><a name="en-us_topic_0070658694_p32229496155835"></a><a name="en-us_topic_0070658694_p32229496155835"></a>Indicates the <strong id="b84235270620159"><a name="b84235270620159"></a><a name="b84235270620159"></a>dc_endpoint_group</strong> object.</p>
</td>
</tr>
</tbody>
</table>

Description of field  **dc\_endpoint\_group**

<a name="en-us_topic_0070658694_table5829218816025"></a>
<table><thead align="left"><tr id="en-us_topic_0070658694_row1193121016025"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.4.1.1"><p id="en-us_topic_0070658694_p151079216025"><a name="en-us_topic_0070658694_p151079216025"></a><a name="en-us_topic_0070658694_p151079216025"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.1.4.1.2"><p id="en-us_topic_0070658694_p3945643916025"><a name="en-us_topic_0070658694_p3945643916025"></a><a name="en-us_topic_0070658694_p3945643916025"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="42%" id="mcps1.1.4.1.3"><p id="en-us_topic_0070658694_p1354606316025"><a name="en-us_topic_0070658694_p1354606316025"></a><a name="en-us_topic_0070658694_p1354606316025"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0070658694_row45689609145447"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0070658694_p8891931145447"><a name="en-us_topic_0070658694_p8891931145447"></a><a name="en-us_topic_0070658694_p8891931145447"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0070658694_p49157836145447"><a name="en-us_topic_0070658694_p49157836145447"></a><a name="en-us_topic_0070658694_p49157836145447"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0070658694_p66476844145447"><a name="en-us_topic_0070658694_p66476844145447"></a><a name="en-us_topic_0070658694_p66476844145447"></a>Indicates the ID of the Direct Connect endpoint group.</p>
</td>
</tr>
<tr id="en-us_topic_0070658694_row42359325145447"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0070658694_p9020038145447"><a name="en-us_topic_0070658694_p9020038145447"></a><a name="en-us_topic_0070658694_p9020038145447"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0070658694_p59534515145447"><a name="en-us_topic_0070658694_p59534515145447"></a><a name="en-us_topic_0070658694_p59534515145447"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0070658694_p32366805145447"><a name="en-us_topic_0070658694_p32366805145447"></a><a name="en-us_topic_0070658694_p32366805145447"></a>Indicates the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0070658694_row41989293145447"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0070658694_p40190072145447"><a name="en-us_topic_0070658694_p40190072145447"></a><a name="en-us_topic_0070658694_p40190072145447"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0070658694_p34170377145447"><a name="en-us_topic_0070658694_p34170377145447"></a><a name="en-us_topic_0070658694_p34170377145447"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0070658694_p48243490145447"><a name="en-us_topic_0070658694_p48243490145447"></a><a name="en-us_topic_0070658694_p48243490145447"></a>Indicates the name of the Direct Connect endpoint group.</p>
</td>
</tr>
<tr id="en-us_topic_0070658694_row12122017145447"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0070658694_p4459976145447"><a name="en-us_topic_0070658694_p4459976145447"></a><a name="en-us_topic_0070658694_p4459976145447"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0070658694_p25713785145447"><a name="en-us_topic_0070658694_p25713785145447"></a><a name="en-us_topic_0070658694_p25713785145447"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0070658694_p63571548145447"><a name="en-us_topic_0070658694_p63571548145447"></a><a name="en-us_topic_0070658694_p63571548145447"></a>Provides supplementary information about the Direct Connect endpoint group.</p>
</td>
</tr>
<tr id="en-us_topic_0070658694_row8803431145447"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0070658694_p38542937145447"><a name="en-us_topic_0070658694_p38542937145447"></a><a name="en-us_topic_0070658694_p38542937145447"></a>endpoints</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0070658694_p34970163145447"><a name="en-us_topic_0070658694_p34970163145447"></a><a name="en-us_topic_0070658694_p34970163145447"></a>List&lt;String&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="42%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0070658694_p61144149145447"><a name="en-us_topic_0070658694_p61144149145447"></a><a name="en-us_topic_0070658694_p61144149145447"></a>Indicates the list of the Direct Connect endpoints.</p>
</td>
</tr>
<tr id="en-us_topic_0070658694_row53173942145447"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0070658694_p13798994145447"><a name="en-us_topic_0070658694_p13798994145447"></a><a name="en-us_topic_0070658694_p13798994145447"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0070658694_p43976752145447"><a name="en-us_topic_0070658694_p43976752145447"></a><a name="en-us_topic_0070658694_p43976752145447"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0070658694_p55374378191835"><a name="en-us_topic_0070658694_p55374378191835"></a><a name="en-us_topic_0070658694_p55374378191835"></a>Indicates the type of the Direct Connect endpoint.</p>
<p id="en-us_topic_0070658694_p30464676145447"><a name="en-us_topic_0070658694_p30464676145447"></a><a name="en-us_topic_0070658694_p30464676145447"></a>The value is <strong id="b842352706185352"><a name="b842352706185352"></a><a name="b842352706185352"></a>cidr</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="en-us_topic_0070658694_section5526447416025"></a>

-   Example request

    ```
    PUT /v2.0/dcaas/dc-endpoint-groups/{endpoint_group_id}
    {
        "dc_endpoint_group" : {
            "name" : "endpoint group1",
            "description" : "New description"
        }
    }
    ```


-   Example response

    ```
    {        
         "dc_endpoint_groups" : {
             "id" : "6ecd9cf3-ca64-46c7-863f-f2eb1b9e838a",
             "tenant_id" : "6fbe9263116a4b68818cf1edce16bc4f",
             "name" : "endpoint group1",
             "description" : "New description",
             "endpoints" : [ "10.2.0.0/24", "10.3.0.0/24" ],      
             "type" : "cidr"
        }
    }
    ```


## Returned Value<a name="section12113171955820"></a>

For details, see section  [Common Returned Values](common-returned-values.md).

