# Updating a VPN Endpoint Group<a name="en_topic_0093011519"></a>

## **Function**<a name="en-us_topic_0053740031_section21433709"></a>

This interface is used to update a VPN endpoint group.

## URI<a name="en-us_topic_0053740031_section58685656"></a>

PUT /v2.0/vpn/endpoint-groups/\{endpoint\_group\_id\}

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

## Request Message<a name="en-us_topic_0053740031_section55917699"></a>

[Table 2](#en-us_topic_0053740031_table16221316)  describes the request parameters.

**Table  2**  Request parameters

<a name="en-us_topic_0053740031_table16221316"></a>
<table><thead align="left"><tr id="en-us_topic_0053740031_row20649961"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="en-us_topic_0053740031_p62034116"><a name="en-us_topic_0053740031_p62034116"></a><a name="en-us_topic_0053740031_p62034116"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="en-us_topic_0053740031_p58707504"><a name="en-us_topic_0053740031_p58707504"></a><a name="en-us_topic_0053740031_p58707504"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="en-us_topic_0053740031_p57687380"><a name="en-us_topic_0053740031_p57687380"></a><a name="en-us_topic_0053740031_p57687380"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="en-us_topic_0053740031_p42166233"><a name="en-us_topic_0053740031_p42166233"></a><a name="en-us_topic_0053740031_p42166233"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0053740031_row58467488"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0053740031_p38246063"><a name="en-us_topic_0053740031_p38246063"></a><a name="en-us_topic_0053740031_p38246063"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0053740031_p10923387"><a name="en-us_topic_0053740031_p10923387"></a><a name="en-us_topic_0053740031_p10923387"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0053740031_p12379115"><a name="en-us_topic_0053740031_p12379115"></a><a name="en-us_topic_0053740031_p12379115"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0053740031_p63184231"><a name="en-us_topic_0053740031_p63184231"></a><a name="en-us_topic_0053740031_p63184231"></a>Provides supplementary information about the VPN endpoint group.</p>
</td>
</tr>
<tr id="en-us_topic_0053740031_row31787174"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0053740031_p24624288"><a name="en-us_topic_0053740031_p24624288"></a><a name="en-us_topic_0053740031_p24624288"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0053740031_p48410331"><a name="en-us_topic_0053740031_p48410331"></a><a name="en-us_topic_0053740031_p48410331"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0053740031_p28922751"><a name="en-us_topic_0053740031_p28922751"></a><a name="en-us_topic_0053740031_p28922751"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0053740031_p61041458"><a name="en-us_topic_0053740031_p61041458"></a><a name="en-us_topic_0053740031_p61041458"></a>Specifies the VPN endpoint group name.</p>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:**   
>1.  The  **endpoint\_group\_id**  parameter must be specified.  
>2.  The value of  **name**  can contain 1 to 64 characters.  
>3.  The value of  **description**  can contain a maximum of 255 characters.  
>4.  The  **project\_id**  parameter is not supported.  

## Response Message<a name="en-us_topic_0053740031_section33497244"></a>

[Table 3](#en-us_topic_0053740031_table45411103)  describes the response parameters.

**Table  3**  Response parameters

<a name="en-us_topic_0053740031_table45411103"></a>
<table><thead align="left"><tr id="en-us_topic_0053740031_row48031108"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="en-us_topic_0053740031_p65314517"><a name="en-us_topic_0053740031_p65314517"></a><a name="en-us_topic_0053740031_p65314517"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="en-us_topic_0053740031_p55984556"><a name="en-us_topic_0053740031_p55984556"></a><a name="en-us_topic_0053740031_p55984556"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="en-us_topic_0053740031_p27859461"><a name="en-us_topic_0053740031_p27859461"></a><a name="en-us_topic_0053740031_p27859461"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0053740031_row42023897"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0053740031_p48492497"><a name="en-us_topic_0053740031_p48492497"></a><a name="en-us_topic_0053740031_p48492497"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0053740031_p35578198"><a name="en-us_topic_0053740031_p35578198"></a><a name="en-us_topic_0053740031_p35578198"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0053740031_p23930149"><a name="en-us_topic_0053740031_p23930149"></a><a name="en-us_topic_0053740031_p23930149"></a>Provides supplementary information about the VPN endpoint group.</p>
</td>
</tr>
<tr id="en-us_topic_0053740031_row14044750"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0053740031_p63882937"><a name="en-us_topic_0053740031_p63882937"></a><a name="en-us_topic_0053740031_p63882937"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0053740031_p7135413"><a name="en-us_topic_0053740031_p7135413"></a><a name="en-us_topic_0053740031_p7135413"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0053740031_p40569470"><a name="en-us_topic_0053740031_p40569470"></a><a name="en-us_topic_0053740031_p40569470"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0053740031_row29580916"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0053740031_p47244029"><a name="en-us_topic_0053740031_p47244029"></a><a name="en-us_topic_0053740031_p47244029"></a>endpoints</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0053740031_p1561146"><a name="en-us_topic_0053740031_p1561146"></a><a name="en-us_topic_0053740031_p1561146"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0053740031_p42136306"><a name="en-us_topic_0053740031_p42136306"></a><a name="en-us_topic_0053740031_p42136306"></a>Specifies the endpoint list. The endpoints in a list must be of the same type.</p>
</td>
</tr>
<tr id="en-us_topic_0053740031_row43682438"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0053740031_p48616614"><a name="en-us_topic_0053740031_p48616614"></a><a name="en-us_topic_0053740031_p48616614"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0053740031_p45631679"><a name="en-us_topic_0053740031_p45631679"></a><a name="en-us_topic_0053740031_p45631679"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0053740031_p16804345"><a name="en-us_topic_0053740031_p16804345"></a><a name="en-us_topic_0053740031_p16804345"></a>Specifies the endpoint type. The value can be <strong id="en-us_topic_0053740031_b126583707521264"><a name="en-us_topic_0053740031_b126583707521264"></a><a name="en-us_topic_0053740031_b126583707521264"></a>subnet</strong>&nbsp;or&nbsp;<strong id="en-us_topic_0053740031_b191796307321264"><a name="en-us_topic_0053740031_b191796307321264"></a><a name="en-us_topic_0053740031_b191796307321264"></a>cidr</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0053740031_row17021380"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0053740031_p36554565"><a name="en-us_topic_0053740031_p36554565"></a><a name="en-us_topic_0053740031_p36554565"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0053740031_p8129827"><a name="en-us_topic_0053740031_p8129827"></a><a name="en-us_topic_0053740031_p8129827"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0053740031_p55361044"><a name="en-us_topic_0053740031_p55361044"></a><a name="en-us_topic_0053740031_p55361044"></a>Specifies the VPN endpoint group ID.</p>
</td>
</tr>
<tr id="en-us_topic_0053740031_row28487351"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0053740031_p25774132"><a name="en-us_topic_0053740031_p25774132"></a><a name="en-us_topic_0053740031_p25774132"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0053740031_p7329937"><a name="en-us_topic_0053740031_p7329937"></a><a name="en-us_topic_0053740031_p7329937"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0053740031_p41771788"><a name="en-us_topic_0053740031_p41771788"></a><a name="en-us_topic_0053740031_p41771788"></a>Provides supplementary information about the VPN endpoint group.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="en-us_topic_0053740031_section33039746"></a>

-   Example Request

    ```
    PUT /v2.0/vpn/endpoint-groups/{endpoint_group_id}
    {
      "endpoint_group" : {
        "description" : "New description"
      }
    }
    ```


-   Example Response

    ```
    {
      "endpoint_group" : {
        "description" : "New description",
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

