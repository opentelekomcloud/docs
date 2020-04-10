# Querying VPN Endpoint Groups<a name="en_topic_0093011518"></a>

## **Function**<a name="en-us_topic_0053740015_section45028263"></a>

This interface is used to query VPN endpoint groups.

## URI<a name="en-us_topic_0053740015_section2601186"></a>

GET /v2.0/vpn/endpoint-groups

## Request Message<a name="en-us_topic_0053740015_section9369539"></a>

[Table 1](#en-us_topic_0053740015_table20501377)  describes the request parameters.

**Table  1**  Request parameters

<a name="en-us_topic_0053740015_table20501377"></a>
<table><thead align="left"><tr id="en-us_topic_0053740015_row59628243"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="en-us_topic_0053740015_p65158399"><a name="en-us_topic_0053740015_p65158399"></a><a name="en-us_topic_0053740015_p65158399"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="en-us_topic_0053740015_p43339000"><a name="en-us_topic_0053740015_p43339000"></a><a name="en-us_topic_0053740015_p43339000"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="en-us_topic_0053740015_p20798117"><a name="en-us_topic_0053740015_p20798117"></a><a name="en-us_topic_0053740015_p20798117"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="en-us_topic_0053740015_p6925935"><a name="en-us_topic_0053740015_p6925935"></a><a name="en-us_topic_0053740015_p6925935"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0053740015_row24129853"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0053740015_p8361080"><a name="en-us_topic_0053740015_p8361080"></a><a name="en-us_topic_0053740015_p8361080"></a>fields</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0053740015_p6158855"><a name="en-us_topic_0053740015_p6158855"></a><a name="en-us_topic_0053740015_p6158855"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0053740015_p29105235"><a name="en-us_topic_0053740015_p29105235"></a><a name="en-us_topic_0053740015_p29105235"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0053740015_p8713795"><a name="en-us_topic_0053740015_p8713795"></a><a name="en-us_topic_0053740015_p8713795"></a>Controls which parameters are returned. If this parameter is not specified, all parameters will be returned.</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>The  **project\_id**  parameter is not supported.  

## Response Message<a name="en-us_topic_0053740015_section17216995"></a>

[Table 2](#en-us_topic_0053740015_table34728767)  describes the response parameters.

**Table  2**  Response parameters

<a name="en-us_topic_0053740015_table34728767"></a>
<table><thead align="left"><tr id="en-us_topic_0053740015_row34760343"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="en-us_topic_0053740015_p64124362"><a name="en-us_topic_0053740015_p64124362"></a><a name="en-us_topic_0053740015_p64124362"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="en-us_topic_0053740015_p26690871"><a name="en-us_topic_0053740015_p26690871"></a><a name="en-us_topic_0053740015_p26690871"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="en-us_topic_0053740015_p31780825"><a name="en-us_topic_0053740015_p31780825"></a><a name="en-us_topic_0053740015_p31780825"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0053740015_row24110047"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0053740015_p6756797"><a name="en-us_topic_0053740015_p6756797"></a><a name="en-us_topic_0053740015_p6756797"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0053740015_p10429724"><a name="en-us_topic_0053740015_p10429724"></a><a name="en-us_topic_0053740015_p10429724"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0053740015_p45492604"><a name="en-us_topic_0053740015_p45492604"></a><a name="en-us_topic_0053740015_p45492604"></a>Provides supplementary information about the VPN endpoint group.</p>
</td>
</tr>
<tr id="en-us_topic_0053740015_row6780253"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0053740015_p12329649"><a name="en-us_topic_0053740015_p12329649"></a><a name="en-us_topic_0053740015_p12329649"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0053740015_p59177513"><a name="en-us_topic_0053740015_p59177513"></a><a name="en-us_topic_0053740015_p59177513"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0053740015_p38888871"><a name="en-us_topic_0053740015_p38888871"></a><a name="en-us_topic_0053740015_p38888871"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0053740015_row14455523"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0053740015_p30046694"><a name="en-us_topic_0053740015_p30046694"></a><a name="en-us_topic_0053740015_p30046694"></a>endpoints</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0053740015_p17863121"><a name="en-us_topic_0053740015_p17863121"></a><a name="en-us_topic_0053740015_p17863121"></a>List</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0053740015_p27863937"><a name="en-us_topic_0053740015_p27863937"></a><a name="en-us_topic_0053740015_p27863937"></a>Specifies the endpoint list. The endpoints in a list must be of the same type.</p>
</td>
</tr>
<tr id="en-us_topic_0053740015_row49448848"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0053740015_p45933772"><a name="en-us_topic_0053740015_p45933772"></a><a name="en-us_topic_0053740015_p45933772"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0053740015_p29648085"><a name="en-us_topic_0053740015_p29648085"></a><a name="en-us_topic_0053740015_p29648085"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0053740015_p39601516"><a name="en-us_topic_0053740015_p39601516"></a><a name="en-us_topic_0053740015_p39601516"></a>Specifies the endpoint type. The value can be <strong id="en-us_topic_0053740015_b126583707521264"><a name="en-us_topic_0053740015_b126583707521264"></a><a name="en-us_topic_0053740015_b126583707521264"></a>subnet</strong>&nbsp;or&nbsp;<strong id="en-us_topic_0053740015_b191796307321264"><a name="en-us_topic_0053740015_b191796307321264"></a><a name="en-us_topic_0053740015_b191796307321264"></a>cidr</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0053740015_row20869327"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0053740015_p12693918"><a name="en-us_topic_0053740015_p12693918"></a><a name="en-us_topic_0053740015_p12693918"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0053740015_p21574462"><a name="en-us_topic_0053740015_p21574462"></a><a name="en-us_topic_0053740015_p21574462"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0053740015_p17455632"><a name="en-us_topic_0053740015_p17455632"></a><a name="en-us_topic_0053740015_p17455632"></a>Specifies the VPN endpoint group ID.</p>
</td>
</tr>
<tr id="en-us_topic_0053740015_row22882960"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0053740015_p41580444"><a name="en-us_topic_0053740015_p41580444"></a><a name="en-us_topic_0053740015_p41580444"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0053740015_p12572829"><a name="en-us_topic_0053740015_p12572829"></a><a name="en-us_topic_0053740015_p12572829"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0053740015_p13543581"><a name="en-us_topic_0053740015_p13543581"></a><a name="en-us_topic_0053740015_p13543581"></a>Specifies the VPN endpoint group name.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="en-us_topic_0053740015_section20735233"></a>

-   Example Request

    ```
    GET /v2.0/vpn/endpoint-groups
    ```


-   Example Response

    ```
    {
        "endpoint_groups": [
            {
                "description": "",
                "tenant_id": "4ad57e7ce0b24fca8f12b9834d91079d",
                "endpoints": [
                    "a3da778c-adfb-46db-88b3-d2ce53290a89"
                ],
                "type": "subnet",
                "id": "6bf34c7c-864c-4948-a6d4-db791669f9d4",
                "name": "locals"
            },
            {
                "description": "",
                "tenant_id": "4ad57e7ce0b24fca8f12b9834d91079d",
                "endpoints": [
                    "10.2.0.0/24",
                    "10.3.0.0/24"
                ],
                "type": "cidr",
                "id": "6ecd9cf3-ca64-46c7-863f-f2eb1b9e838a",
                "name": "peers"
            }
        ]
    }
    ```


## Returned Values<a name="section6578292"></a>

For details, see section  [Common Returned Values](common-returned-values.md).

