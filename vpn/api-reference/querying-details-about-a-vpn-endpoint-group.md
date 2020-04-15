# Querying Details About a VPN Endpoint Group<a name="en_topic_0093011517"></a>

## **Function**<a name="en-us_topic_0053740027_section33876408"></a>

This interface is used to query details about a VPN endpoint group.

## URI<a name="en-us_topic_0053740027_section36452220"></a>

GET /v2.0/vpn/endpoint-groups/\{endpoint\_group\_id\}

**Table  1**  Parameter description

<a name="table19418153522110"></a>
<table><thead align="left"><tr id="row10418143532118"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p11427103572112"><a name="p11427103572112"></a><a name="p11427103572112"></a><strong id="b842352706172115"><a name="b842352706172115"></a><a name="b842352706172115"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p84273352212"><a name="p84273352212"></a><a name="p84273352212"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p242718358217"><a name="p242718358217"></a><a name="p242718358217"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p104271435152111"><a name="p104271435152111"></a><a name="p104271435152111"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row44271735192115"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p743473572111"><a name="p743473572111"></a><a name="p743473572111"></a>endpoint_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p3434143514215"><a name="p3434143514215"></a><a name="p3434143514215"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p10434143592116"><a name="p10434143592116"></a><a name="p10434143592116"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p043443522110"><a name="p043443522110"></a><a name="p043443522110"></a>Specifies the VPN endpoint group ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="en-us_topic_0053740027_section66948675"></a>

None

## Response Message<a name="en-us_topic_0053740027_section65667169"></a>

[Table 2](#en-us_topic_0053740027_table58761073)  describes the response parameters.

**Table  2**  Response parameters

<a name="en-us_topic_0053740027_table58761073"></a>
<table><thead align="left"><tr id="en-us_topic_0053740027_row2491394"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="en-us_topic_0053740027_p476380"><a name="en-us_topic_0053740027_p476380"></a><a name="en-us_topic_0053740027_p476380"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="en-us_topic_0053740027_p38586810"><a name="en-us_topic_0053740027_p38586810"></a><a name="en-us_topic_0053740027_p38586810"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="en-us_topic_0053740027_p33428900"><a name="en-us_topic_0053740027_p33428900"></a><a name="en-us_topic_0053740027_p33428900"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0053740027_row23386368"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0053740027_p15247616"><a name="en-us_topic_0053740027_p15247616"></a><a name="en-us_topic_0053740027_p15247616"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0053740027_p27097356"><a name="en-us_topic_0053740027_p27097356"></a><a name="en-us_topic_0053740027_p27097356"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0053740027_p14377323"><a name="en-us_topic_0053740027_p14377323"></a><a name="en-us_topic_0053740027_p14377323"></a>Provides supplementary information about the VPN endpoint group.</p>
</td>
</tr>
<tr id="en-us_topic_0053740027_row62287048"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0053740027_p12086140"><a name="en-us_topic_0053740027_p12086140"></a><a name="en-us_topic_0053740027_p12086140"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0053740027_p39453247"><a name="en-us_topic_0053740027_p39453247"></a><a name="en-us_topic_0053740027_p39453247"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0053740027_p13871385"><a name="en-us_topic_0053740027_p13871385"></a><a name="en-us_topic_0053740027_p13871385"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0053740027_row57733603"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0053740027_p45910260"><a name="en-us_topic_0053740027_p45910260"></a><a name="en-us_topic_0053740027_p45910260"></a>endpoints</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0053740027_p27743545"><a name="en-us_topic_0053740027_p27743545"></a><a name="en-us_topic_0053740027_p27743545"></a>List</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0053740027_p26161025"><a name="en-us_topic_0053740027_p26161025"></a><a name="en-us_topic_0053740027_p26161025"></a>Specifies the endpoint list. The endpoints in a list must be of the same type.</p>
</td>
</tr>
<tr id="en-us_topic_0053740027_row34122633"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0053740027_p12469873"><a name="en-us_topic_0053740027_p12469873"></a><a name="en-us_topic_0053740027_p12469873"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0053740027_p3426769"><a name="en-us_topic_0053740027_p3426769"></a><a name="en-us_topic_0053740027_p3426769"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0053740027_p1565979"><a name="en-us_topic_0053740027_p1565979"></a><a name="en-us_topic_0053740027_p1565979"></a>Specifies the endpoint type. The value can be <strong id="en-us_topic_0053740027_b126583707521264"><a name="en-us_topic_0053740027_b126583707521264"></a><a name="en-us_topic_0053740027_b126583707521264"></a>subnet</strong>&nbsp;or&nbsp;<strong id="en-us_topic_0053740027_b191796307321264"><a name="en-us_topic_0053740027_b191796307321264"></a><a name="en-us_topic_0053740027_b191796307321264"></a>cidr</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0053740027_row14093819"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0053740027_p748676"><a name="en-us_topic_0053740027_p748676"></a><a name="en-us_topic_0053740027_p748676"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0053740027_p60642794"><a name="en-us_topic_0053740027_p60642794"></a><a name="en-us_topic_0053740027_p60642794"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0053740027_p56026474"><a name="en-us_topic_0053740027_p56026474"></a><a name="en-us_topic_0053740027_p56026474"></a>Specifies the VPN endpoint group ID.</p>
</td>
</tr>
<tr id="en-us_topic_0053740027_row34476226"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0053740027_p41110918"><a name="en-us_topic_0053740027_p41110918"></a><a name="en-us_topic_0053740027_p41110918"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0053740027_p41650091"><a name="en-us_topic_0053740027_p41650091"></a><a name="en-us_topic_0053740027_p41650091"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0053740027_p66066743"><a name="en-us_topic_0053740027_p66066743"></a><a name="en-us_topic_0053740027_p66066743"></a>Specifies the VPN endpoint group name.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="en-us_topic_0053740027_section54133615"></a>

-   Example Request

    ```
    GET /v2.0/vpn/endpoint-groups/{endpoint_group_id}
    ```


-   Example Response

    ```
    {
        "endpoint_group": {
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
    }
    ```


## Returned Values<a name="section6578292"></a>

For details, see section  [Common Returned Values](common-returned-values.md).

