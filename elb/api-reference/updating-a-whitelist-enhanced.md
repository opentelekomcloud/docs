# Updating a Whitelist<a name="EN-US_TOPIC_0143878054"></a>

## Function<a name="section25599027"></a>

This API is used to update a whitelist. You can enable or disable the whitelist function or update IP addresses in the whitelist.

## URI<a name="section29064658"></a>

PUT /v2.0/lbaas/whitelists/\{whitelist\_id\}

**Table  1**  Parameter description

<a name="table7796376"></a>
<table><thead align="left"><tr id="row40506252"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.1"><p id="p59780960"><a name="p59780960"></a><a name="p59780960"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.5.1.2"><p id="p6960976515"><a name="p6960976515"></a><a name="p6960976515"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.3"><p id="p38680022"><a name="p38680022"></a><a name="p38680022"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54%" id="mcps1.2.5.1.4"><p id="p46074055"><a name="p46074055"></a><a name="p46074055"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row41011006"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p33557152"><a name="p33557152"></a><a name="p33557152"></a>whitelist_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.2 "><p id="p33774807"><a name="p33774807"></a><a name="p33774807"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p51404875"><a name="p51404875"></a><a name="p51404875"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.5.1.4 "><p id="p3045347"><a name="p3045347"></a><a name="p3045347"></a>Specifies the whitelist ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section5427073"></a>

**Table  2**  Request parameters

<a name="table25240599"></a>
<table><thead align="left"><tr id="row39640618"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.1"><p id="p56773510"><a name="p56773510"></a><a name="p56773510"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.2"><p id="p35251631"><a name="p35251631"></a><a name="p35251631"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.3"><p id="p36809868"><a name="p36809868"></a><a name="p36809868"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="53%" id="mcps1.2.5.1.4"><p id="p9493129175219"><a name="p9493129175219"></a><a name="p9493129175219"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row51856004"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p39586799"><a name="p39586799"></a><a name="p39586799"></a>whitelist</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p52414126"><a name="p52414126"></a><a name="p52414126"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p17685802"><a name="p17685802"></a><a name="p17685802"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><p id="p23263818"><a name="p23263818"></a><a name="p23263818"></a>Specifies the whitelist. For details, see <a href="#table8047771">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **whitelist**  parameter description

<a name="table8047771"></a>
<table><thead align="left"><tr id="row55214998"><th class="cellrowborder" valign="top" width="17.17171717171717%" id="mcps1.2.5.1.1"><p id="p43229817"><a name="p43229817"></a><a name="p43229817"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.13131313131313%" id="mcps1.2.5.1.2"><p id="p11954326"><a name="p11954326"></a><a name="p11954326"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16.16161616161616%" id="mcps1.2.5.1.3"><p id="p28776339"><a name="p28776339"></a><a name="p28776339"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="53.535353535353536%" id="mcps1.2.5.1.4"><p id="p49182104"><a name="p49182104"></a><a name="p49182104"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row24327502"><td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.2.5.1.1 "><p id="p24370652"><a name="p24370652"></a><a name="p24370652"></a>enable_whitelist</p>
</td>
<td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.2.5.1.2 "><p id="p27865835"><a name="p27865835"></a><a name="p27865835"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.5.1.3 "><p id="p19315100237"><a name="p19315100237"></a><a name="p19315100237"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="53.535353535353536%" headers="mcps1.2.5.1.4 "><p id="p18641129"><a name="p18641129"></a><a name="p18641129"></a>Specifies whether to enable access control.</p>
<p id="p952924417504"><a name="p952924417504"></a><a name="p952924417504"></a><strong id="b1376051812584"><a name="b1376051812584"></a><a name="b1376051812584"></a>true</strong>: Access control is enabled.</p>
<p id="p315412015112"><a name="p315412015112"></a><a name="p315412015112"></a><strong id="b652142114584"><a name="b652142114584"></a><a name="b652142114584"></a>false</strong>: Access control is disabled.</p>
<p id="p19957125510422"><a name="p19957125510422"></a><a name="p19957125510422"></a>The default value is <strong id="b1474822218583"><a name="b1474822218583"></a><a name="b1474822218583"></a>true</strong>.</p>
</td>
</tr>
<tr id="row7507204"><td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.2.5.1.1 "><p id="p4103816"><a name="p4103816"></a><a name="p4103816"></a>whitelist</p>
</td>
<td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.2.5.1.2 "><p id="p63973680"><a name="p63973680"></a><a name="p63973680"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.5.1.3 "><p id="p14485605"><a name="p14485605"></a><a name="p14485605"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.535353535353536%" headers="mcps1.2.5.1.4 "><p id="p058752114472"><a name="p058752114472"></a><a name="p058752114472"></a>Specifies the IP addresses in the whitelist. Use commas (,) to separate the multiple IP addresses.</p>
<p id="p2602102514718"><a name="p2602102514718"></a><a name="p2602102514718"></a>You can specify an IP address, for example, 192.168.11.1.</p>
<p id="p29586371"><a name="p29586371"></a><a name="p29586371"></a>You can also specify an IP address range, for example, 192.168.0.1/24.</p>
<p id="p28402003453"><a name="p28402003453"></a><a name="p28402003453"></a>The default value is an empty string, that is, <strong id="b069415612563"><a name="b069415612563"></a><a name="b069415612563"></a>""</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section48843660"></a>

**Table  4**  Response parameters

<a name="table1999612"></a>
<table><thead align="left"><tr id="row64631692"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.1"><p id="p675705"><a name="p675705"></a><a name="p675705"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.4.1.2"><p id="p54732163"><a name="p54732163"></a><a name="p54732163"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="66%" id="mcps1.2.4.1.3"><p id="p4120209"><a name="p4120209"></a><a name="p4120209"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row65301516"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p54931419"><a name="p54931419"></a><a name="p54931419"></a>whitelist</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p20259943"><a name="p20259943"></a><a name="p20259943"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.4.1.3 "><p id="p30442647"><a name="p30442647"></a><a name="p30442647"></a>Specifies the whitelist. For details, see <a href="#table5548368">Table 5</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **whitelist**  parameter description

<a name="table5548368"></a>
<table><thead align="left"><tr id="en-us_topic_0143878053_row45839354"><th class="cellrowborder" valign="top" width="27.27272727272727%" id="mcps1.2.4.1.1"><p id="en-us_topic_0143878053_p22000213"><a name="en-us_topic_0143878053_p22000213"></a><a name="en-us_topic_0143878053_p22000213"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.17171717171717%" id="mcps1.2.4.1.2"><p id="en-us_topic_0143878053_p37186841"><a name="en-us_topic_0143878053_p37186841"></a><a name="en-us_topic_0143878053_p37186841"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="55.55555555555556%" id="mcps1.2.4.1.3"><p id="en-us_topic_0143878053_p59344108"><a name="en-us_topic_0143878053_p59344108"></a><a name="en-us_topic_0143878053_p59344108"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0143878053_row42143481"><td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0143878053_p58178790"><a name="en-us_topic_0143878053_p58178790"></a><a name="en-us_topic_0143878053_p58178790"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0143878053_p8601456153613"><a name="en-us_topic_0143878053_p8601456153613"></a><a name="en-us_topic_0143878053_p8601456153613"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.55555555555556%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0143878053_p62933377"><a name="en-us_topic_0143878053_p62933377"></a><a name="en-us_topic_0143878053_p62933377"></a>Specifies the whitelist ID.</p>
</td>
</tr>
<tr id="en-us_topic_0143878053_row29529486"><td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0143878053_p43078143"><a name="en-us_topic_0143878053_p43078143"></a><a name="en-us_topic_0143878053_p43078143"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0143878053_p66777590"><a name="en-us_topic_0143878053_p66777590"></a><a name="en-us_topic_0143878053_p66777590"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.55555555555556%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0143878053_p40275672"><a name="en-us_topic_0143878053_p40275672"></a><a name="en-us_topic_0143878053_p40275672"></a>Specifies the ID of the project where the whitelist is used.</p>
<p id="en-us_topic_0143878053_p13774541163418"><a name="en-us_topic_0143878053_p13774541163418"></a><a name="en-us_topic_0143878053_p13774541163418"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0143878053_row26936734"><td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0143878053_p34391822"><a name="en-us_topic_0143878053_p34391822"></a><a name="en-us_topic_0143878053_p34391822"></a>listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0143878053_p1044313103716"><a name="en-us_topic_0143878053_p1044313103716"></a><a name="en-us_topic_0143878053_p1044313103716"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.55555555555556%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0143878053_p24747384"><a name="en-us_topic_0143878053_p24747384"></a><a name="en-us_topic_0143878053_p24747384"></a>Specifies the ID of the listener to which the whitelist is added.</p>
</td>
</tr>
<tr id="en-us_topic_0143878053_row21399872"><td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0143878053_p55668057"><a name="en-us_topic_0143878053_p55668057"></a><a name="en-us_topic_0143878053_p55668057"></a>enable_whitelist</p>
</td>
<td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0143878053_p12818767"><a name="en-us_topic_0143878053_p12818767"></a><a name="en-us_topic_0143878053_p12818767"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="55.55555555555556%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0143878053_p31687177"><a name="en-us_topic_0143878053_p31687177"></a><a name="en-us_topic_0143878053_p31687177"></a>Specifies whether to enable access control.</p>
<p id="en-us_topic_0143878053_p07333135114"><a name="en-us_topic_0143878053_p07333135114"></a><a name="en-us_topic_0143878053_p07333135114"></a><strong id="en-us_topic_0143878053_b1072540155010"><a name="en-us_topic_0143878053_b1072540155010"></a><a name="en-us_topic_0143878053_b1072540155010"></a>true</strong>: Access control is enabled.</p>
<p id="en-us_topic_0143878053_p57393175115"><a name="en-us_topic_0143878053_p57393175115"></a><a name="en-us_topic_0143878053_p57393175115"></a><strong id="en-us_topic_0143878053_b978484145016"><a name="en-us_topic_0143878053_b978484145016"></a><a name="en-us_topic_0143878053_b978484145016"></a>false</strong>: Access control is disabled.</p>
</td>
</tr>
<tr id="en-us_topic_0143878053_row16749139"><td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0143878053_p14503023"><a name="en-us_topic_0143878053_p14503023"></a><a name="en-us_topic_0143878053_p14503023"></a>whitelist</p>
</td>
<td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0143878053_p33894211"><a name="en-us_topic_0143878053_p33894211"></a><a name="en-us_topic_0143878053_p33894211"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.55555555555556%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0143878053_p61076600"><a name="en-us_topic_0143878053_p61076600"></a><a name="en-us_topic_0143878053_p61076600"></a>Specifies the IP addresses in the whitelist.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section2057311372416"></a>

-   Example request: Updating a whitelist

    ```
    PUT https://{Endpoint}/v2.0/lbaas/whitelists/dcaf46f1-037c-4f63-a31f-e0c4c18032c7 
    
    { 
        "whitelist": { 
            "enable_whitelist": true,  
            "whitelist": "192.168.11.1,192.168.0.1/24,192.168.201.18/8,100.164.0.1/24" 
        } 
    }
    ```

-   Example response

    ```
    { 
        "whitelist": { 
            "id": "eabfefa3fd1740a88a47ad98e132d238",  
            "listener_id": "eabfefa3fd1740a88a47ad98e132d238",  
            "tenant_id": "eabfefa3fd1740a88a47ad98e132d238",  
            "enable_whitelist": true,  
            "whitelist": "192.168.11.1,192.168.0.1/24,192.168.201.18/8,100.164.0.1/24" 
        } 
    }
    ```


## Status Code<a name="section499312491792"></a>

For details, see  [HTTP Status Codes for Enhanced Load Balancers](http-status-codes-for-enhanced-load-balancers.md).

