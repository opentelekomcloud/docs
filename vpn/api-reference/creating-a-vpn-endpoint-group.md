# Creating a VPN Endpoint Group<a name="en_topic_0093011516"></a>

## **Function**<a name="en-us_topic_0053740037_section57841469"></a>

This interface is used to create a VPN endpoint group.

## URI<a name="en-us_topic_0053740037_section50811173"></a>

POST /v2.0/vpn/endpoint-groups

## Request Message<a name="en-us_topic_0053740037_section22064367"></a>

[Table 1](#en-us_topic_0053740037_table31025868)  describes the request parameters.

**Table  1**  Request parameters

<a name="en-us_topic_0053740037_table31025868"></a>
<table><thead align="left"><tr id="en-us_topic_0053740037_row17177639"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="en-us_topic_0053740037_p49211517"><a name="en-us_topic_0053740037_p49211517"></a><a name="en-us_topic_0053740037_p49211517"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="en-us_topic_0053740037_p26709911"><a name="en-us_topic_0053740037_p26709911"></a><a name="en-us_topic_0053740037_p26709911"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="en-us_topic_0053740037_p16019165"><a name="en-us_topic_0053740037_p16019165"></a><a name="en-us_topic_0053740037_p16019165"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="en-us_topic_0053740037_p22484025"><a name="en-us_topic_0053740037_p22484025"></a><a name="en-us_topic_0053740037_p22484025"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0053740037_row9266704"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0053740037_p12405580"><a name="en-us_topic_0053740037_p12405580"></a><a name="en-us_topic_0053740037_p12405580"></a>endpoints</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0053740037_p65327957"><a name="en-us_topic_0053740037_p65327957"></a><a name="en-us_topic_0053740037_p65327957"></a>List&lt;String&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0053740037_p57073170"><a name="en-us_topic_0053740037_p57073170"></a><a name="en-us_topic_0053740037_p57073170"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0053740037_p59524076"><a name="en-us_topic_0053740037_p59524076"></a><a name="en-us_topic_0053740037_p59524076"></a>Specifies the endpoint list. The endpoints in a list must be of the same type.</p>
</td>
</tr>
<tr id="en-us_topic_0053740037_row65954639"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0053740037_p40725534"><a name="en-us_topic_0053740037_p40725534"></a><a name="en-us_topic_0053740037_p40725534"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0053740037_p10433982"><a name="en-us_topic_0053740037_p10433982"></a><a name="en-us_topic_0053740037_p10433982"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0053740037_p39846231"><a name="en-us_topic_0053740037_p39846231"></a><a name="en-us_topic_0053740037_p39846231"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0053740037_p6319248"><a name="en-us_topic_0053740037_p6319248"></a><a name="en-us_topic_0053740037_p6319248"></a>Specifies the endpoint type. The value can be <strong id="en-us_topic_0053740037_b126583707521264"><a name="en-us_topic_0053740037_b126583707521264"></a><a name="en-us_topic_0053740037_b126583707521264"></a>subnet</strong>&nbsp;or&nbsp;<strong id="en-us_topic_0053740037_b191796307321264"><a name="en-us_topic_0053740037_b191796307321264"></a><a name="en-us_topic_0053740037_b191796307321264"></a>cidr</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0053740037_row56873232"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0053740037_p43329052"><a name="en-us_topic_0053740037_p43329052"></a><a name="en-us_topic_0053740037_p43329052"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0053740037_p19992349"><a name="en-us_topic_0053740037_p19992349"></a><a name="en-us_topic_0053740037_p19992349"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0053740037_p8767611"><a name="en-us_topic_0053740037_p8767611"></a><a name="en-us_topic_0053740037_p8767611"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0053740037_p39087901"><a name="en-us_topic_0053740037_p39087901"></a><a name="en-us_topic_0053740037_p39087901"></a>Specifies the VPN endpoint group name.</p>
</td>
</tr>
<tr id="en-us_topic_0053740037_row16246796"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0053740037_p40922063"><a name="en-us_topic_0053740037_p40922063"></a><a name="en-us_topic_0053740037_p40922063"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0053740037_p26352844"><a name="en-us_topic_0053740037_p26352844"></a><a name="en-us_topic_0053740037_p26352844"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0053740037_p54205609"><a name="en-us_topic_0053740037_p54205609"></a><a name="en-us_topic_0053740037_p54205609"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0053740037_p28578190"><a name="en-us_topic_0053740037_p28578190"></a><a name="en-us_topic_0053740037_p28578190"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0053740037_row8017921"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0053740037_p45471841"><a name="en-us_topic_0053740037_p45471841"></a><a name="en-us_topic_0053740037_p45471841"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0053740037_p59340514"><a name="en-us_topic_0053740037_p59340514"></a><a name="en-us_topic_0053740037_p59340514"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0053740037_p41852331"><a name="en-us_topic_0053740037_p41852331"></a><a name="en-us_topic_0053740037_p41852331"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0053740037_p34595685"><a name="en-us_topic_0053740037_p34595685"></a><a name="en-us_topic_0053740037_p34595685"></a>Provides supplementary information about the VPN endpoint group.</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>1.  The  **project\_id**  parameter is not supported.  
>2.  The value of  **tenant\_id**  can contain a maximum of 255 characters.  
>3.  The value of  **name**  can contain 1 to 64 characters.  
>4.  The value of  **description**  can contain a maximum of 255 characters.  
>5.  The value of  **type** can only be **subnet** or **cidr**.  

## Response Message<a name="en-us_topic_0053740037_section64361578"></a>

[Table 2](#en-us_topic_0053740037_table50787128)  describes the response parameters.

**Table  2**  Response parameters

<a name="en-us_topic_0053740037_table50787128"></a>
<table><thead align="left"><tr id="en-us_topic_0053740037_row43130086"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="en-us_topic_0053740037_p3876045"><a name="en-us_topic_0053740037_p3876045"></a><a name="en-us_topic_0053740037_p3876045"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="en-us_topic_0053740037_p45524249"><a name="en-us_topic_0053740037_p45524249"></a><a name="en-us_topic_0053740037_p45524249"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="en-us_topic_0053740037_p63585586"><a name="en-us_topic_0053740037_p63585586"></a><a name="en-us_topic_0053740037_p63585586"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="en-us_topic_0053740037_p50158847"><a name="en-us_topic_0053740037_p50158847"></a><a name="en-us_topic_0053740037_p50158847"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0053740037_row36334825"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0053740037__Hlk477536615"><a name="en-us_topic_0053740037__Hlk477536615"></a><a name="en-us_topic_0053740037__Hlk477536615"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0053740037_p22104370"><a name="en-us_topic_0053740037_p22104370"></a><a name="en-us_topic_0053740037_p22104370"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0053740037_p45623521"><a name="en-us_topic_0053740037_p45623521"></a><a name="en-us_topic_0053740037_p45623521"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0053740037_p4517709"><a name="en-us_topic_0053740037_p4517709"></a><a name="en-us_topic_0053740037_p4517709"></a>Provides supplementary information about the VPN endpoint group.</p>
</td>
</tr>
<tr id="en-us_topic_0053740037_row40659381"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0053740037_p5075526"><a name="en-us_topic_0053740037_p5075526"></a><a name="en-us_topic_0053740037_p5075526"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0053740037_p8464456"><a name="en-us_topic_0053740037_p8464456"></a><a name="en-us_topic_0053740037_p8464456"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0053740037_p14532322"><a name="en-us_topic_0053740037_p14532322"></a><a name="en-us_topic_0053740037_p14532322"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0053740037_p36267453"><a name="en-us_topic_0053740037_p36267453"></a><a name="en-us_topic_0053740037_p36267453"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0053740037_row57971626"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0053740037_p65190153"><a name="en-us_topic_0053740037_p65190153"></a><a name="en-us_topic_0053740037_p65190153"></a>endpoints</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0053740037_p45911036"><a name="en-us_topic_0053740037_p45911036"></a><a name="en-us_topic_0053740037_p45911036"></a>List&lt;String&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0053740037_p27806444"><a name="en-us_topic_0053740037_p27806444"></a><a name="en-us_topic_0053740037_p27806444"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0053740037_p37729472"><a name="en-us_topic_0053740037_p37729472"></a><a name="en-us_topic_0053740037_p37729472"></a>Specifies the endpoint list. The endpoints in a list must be of the same type.</p>
</td>
</tr>
<tr id="en-us_topic_0053740037_row4020931"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0053740037_p57260009"><a name="en-us_topic_0053740037_p57260009"></a><a name="en-us_topic_0053740037_p57260009"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0053740037_p7549159"><a name="en-us_topic_0053740037_p7549159"></a><a name="en-us_topic_0053740037_p7549159"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0053740037_p7502182"><a name="en-us_topic_0053740037_p7502182"></a><a name="en-us_topic_0053740037_p7502182"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0053740037_p3697038"><a name="en-us_topic_0053740037_p3697038"></a><a name="en-us_topic_0053740037_p3697038"></a>Specifies the endpoint type. The value can be <strong id="en-us_topic_0053740037_b126583707521264_1"><a name="en-us_topic_0053740037_b126583707521264_1"></a><a name="en-us_topic_0053740037_b126583707521264_1"></a>subnet</strong>&nbsp;or&nbsp;<strong id="en-us_topic_0053740037_b191796307321264_1"><a name="en-us_topic_0053740037_b191796307321264_1"></a><a name="en-us_topic_0053740037_b191796307321264_1"></a>cidr</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0053740037_row33273344"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0053740037_p10786359"><a name="en-us_topic_0053740037_p10786359"></a><a name="en-us_topic_0053740037_p10786359"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0053740037_p1279915"><a name="en-us_topic_0053740037_p1279915"></a><a name="en-us_topic_0053740037_p1279915"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0053740037_p36564291"><a name="en-us_topic_0053740037_p36564291"></a><a name="en-us_topic_0053740037_p36564291"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0053740037_p8917608"><a name="en-us_topic_0053740037_p8917608"></a><a name="en-us_topic_0053740037_p8917608"></a>Specifies the VPN endpoint group ID.</p>
</td>
</tr>
<tr id="en-us_topic_0053740037_row13149610"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0053740037_p58485517"><a name="en-us_topic_0053740037_p58485517"></a><a name="en-us_topic_0053740037_p58485517"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0053740037_p39706416"><a name="en-us_topic_0053740037_p39706416"></a><a name="en-us_topic_0053740037_p39706416"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0053740037_p62103099"><a name="en-us_topic_0053740037_p62103099"></a><a name="en-us_topic_0053740037_p62103099"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0053740037_p64295127"><a name="en-us_topic_0053740037_p64295127"></a><a name="en-us_topic_0053740037_p64295127"></a>Specifies the VPN endpoint group name.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="en-us_topic_0053740037_section42383293"></a>

-   Example Request

    ```
    POST /v2.0/vpn/endpoint-groups
    {
      "endpoint_group" : {
        "endpoints" : [ "10.2.0.0/24", "10.3.0.0/24" ],
        "type" : "cidr",
        "name" : "peers"
      }
    }
    ```


-   Example Response

    ```
    {
      "endpoint_group" : {
        "description" : "",
        "tenant_id" : "4ad57e7ce0b24fca8f12b9834d91079d",
        "endpoints" : [ "10.2.0.0/24", "10.3.0.0/24" ],
        "type" : "cidr",
        "id" : "6ecd9cf3-ca64-46c7-863f-f2eb1b9e838a",
        "name" : "peers"
      }
    }
    ```


## Returned Values<a name="section6578292"></a>

For details, see section  [Common Returned Values](common-returned-values.md).

