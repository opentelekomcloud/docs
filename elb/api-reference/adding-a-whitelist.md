# Adding a Whitelist<a name="EN-US_TOPIC_0143878053"></a>

## Function<a name="section34484227"></a>

This API is used to add a whitelist to control access to a specific listener. After a whitelist is added, only IP addresses in the whitelist can access the listener.

## URI<a name="section41922587"></a>

POST /v2.0/lbaas/whitelists

## Request<a name="section40286359"></a>

**Table  1**  Request parameters

<a name="table48141425"></a>
<table><thead align="left"><tr id="row7942332"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="p39349140"><a name="p39349140"></a><a name="p39349140"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.5.1.2"><p id="p33163748"><a name="p33163748"></a><a name="p33163748"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.3"><p id="p1909077"><a name="p1909077"></a><a name="p1909077"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="57.99999999999999%" id="mcps1.2.5.1.4"><p id="p20417550"><a name="p20417550"></a><a name="p20417550"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row43208888"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p10259067"><a name="p10259067"></a><a name="p10259067"></a>whitelist</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.2 "><p id="p25678078"><a name="p25678078"></a><a name="p25678078"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p15116172541612"><a name="p15116172541612"></a><a name="p15116172541612"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><p id="p30622053"><a name="p30622053"></a><a name="p30622053"></a>Specifies the whitelist. For details, see <a href="#table7163025">Table 2</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  2** **whitelist**  parameter description

<a name="table7163025"></a>
<table><thead align="left"><tr id="row48043114"><th class="cellrowborder" valign="top" width="25.86%" id="mcps1.2.5.1.1"><p id="p66287044"><a name="p66287044"></a><a name="p66287044"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="11.23%" id="mcps1.2.5.1.2"><p id="p43859437"><a name="p43859437"></a><a name="p43859437"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13.11%" id="mcps1.2.5.1.3"><p id="p541474"><a name="p541474"></a><a name="p541474"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.8%" id="mcps1.2.5.1.4"><p id="p62953484"><a name="p62953484"></a><a name="p62953484"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row66067432"><td class="cellrowborder" valign="top" width="25.86%" headers="mcps1.2.5.1.1 "><p id="p49861736"><a name="p49861736"></a><a name="p49861736"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="11.23%" headers="mcps1.2.5.1.2 "><p id="p54247797"><a name="p54247797"></a><a name="p54247797"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.11%" headers="mcps1.2.5.1.3 "><p id="p12268788"><a name="p12268788"></a><a name="p12268788"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.8%" headers="mcps1.2.5.1.4 "><p id="p11184131"><a name="p11184131"></a><a name="p11184131"></a>Specifies the ID of the project where the whitelist is used.</p>
<p id="p8222164914610"><a name="p8222164914610"></a><a name="p8222164914610"></a></p>
<p id="p2038118462238"><a name="p2038118462238"></a><a name="p2038118462238"></a>The value must be the same as the value of <strong id="b1778453224618"><a name="b1778453224618"></a><a name="b1778453224618"></a>project_id</strong> in the token.</p>
<p id="p1264211013318"><a name="p1264211013318"></a><a name="p1264211013318"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row19523824"><td class="cellrowborder" valign="top" width="25.86%" headers="mcps1.2.5.1.1 "><p id="p37925924"><a name="p37925924"></a><a name="p37925924"></a>listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="11.23%" headers="mcps1.2.5.1.2 "><p id="p59428836"><a name="p59428836"></a><a name="p59428836"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.11%" headers="mcps1.2.5.1.3 "><p id="p818511863514"><a name="p818511863514"></a><a name="p818511863514"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.8%" headers="mcps1.2.5.1.4 "><p id="p1733144994211"><a name="p1733144994211"></a><a name="p1733144994211"></a>Specifies the listener ID.</p>
<p id="p49006401"><a name="p49006401"></a><a name="p49006401"></a>Only one whitelist can be created for a listener.</p>
</td>
</tr>
<tr id="row38404427"><td class="cellrowborder" valign="top" width="25.86%" headers="mcps1.2.5.1.1 "><p id="p23750876"><a name="p23750876"></a><a name="p23750876"></a>enable_whitelist</p>
</td>
<td class="cellrowborder" valign="top" width="11.23%" headers="mcps1.2.5.1.2 "><p id="p2715650"><a name="p2715650"></a><a name="p2715650"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.11%" headers="mcps1.2.5.1.3 "><p id="p44772769"><a name="p44772769"></a><a name="p44772769"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="49.8%" headers="mcps1.2.5.1.4 "><p id="p18641129"><a name="p18641129"></a><a name="p18641129"></a>Specifies whether to enable access control.</p>
<p id="p952924417504"><a name="p952924417504"></a><a name="p952924417504"></a><strong id="b842352706152844"><a name="b842352706152844"></a><a name="b842352706152844"></a>true</strong>: Access control is enabled.</p>
<p id="p315412015112"><a name="p315412015112"></a><a name="p315412015112"></a><strong id="b4867121184716"><a name="b4867121184716"></a><a name="b4867121184716"></a>false</strong>: Access control is disabled.</p>
<p id="p19957125510422"><a name="p19957125510422"></a><a name="p19957125510422"></a>The default value is <strong id="b842352706145246"><a name="b842352706145246"></a><a name="b842352706145246"></a>true</strong>.</p>
</td>
</tr>
<tr id="row33552433"><td class="cellrowborder" valign="top" width="25.86%" headers="mcps1.2.5.1.1 "><p id="p33392537"><a name="p33392537"></a><a name="p33392537"></a>whitelist</p>
</td>
<td class="cellrowborder" valign="top" width="11.23%" headers="mcps1.2.5.1.2 "><p id="p45104506"><a name="p45104506"></a><a name="p45104506"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.11%" headers="mcps1.2.5.1.3 "><p id="p20440953"><a name="p20440953"></a><a name="p20440953"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.8%" headers="mcps1.2.5.1.4 "><p id="p058752114472"><a name="p058752114472"></a><a name="p058752114472"></a>Specifies the IP addresses in the whitelist. Use commas (,) to separate the multiple IP addresses.</p>
<p id="p2602102514718"><a name="p2602102514718"></a><a name="p2602102514718"></a>You can specify an IP address, for example, 192.168.11.1.</p>
<p id="p29586371"><a name="p29586371"></a><a name="p29586371"></a>You can also specify a network segment, for example, 192.168.0.1/24.</p>
<p id="p28402003453"><a name="p28402003453"></a><a name="p28402003453"></a>The default value is an empty string, that is, <strong id="b65571821195610"><a name="b65571821195610"></a><a name="b65571821195610"></a>""</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section27032918"></a>

**Table  3**  Response parameters

<a name="table50156668"></a>
<table><thead align="left"><tr id="row42413523"><th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.2.4.1.1"><p id="p12943361"><a name="p12943361"></a><a name="p12943361"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.4.1.2"><p id="p41779295"><a name="p41779295"></a><a name="p41779295"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.2.4.1.3"><p id="p28679701"><a name="p28679701"></a><a name="p28679701"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row41354444"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p61375659"><a name="p61375659"></a><a name="p61375659"></a>whitelist</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p162533953520"><a name="p162533953520"></a><a name="p162533953520"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p32519940"><a name="p32519940"></a><a name="p32519940"></a>Specifies the whitelist. For details, see <a href="#table24244005">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **whitelist**  parameter description

<a name="table24244005"></a>
<table><thead align="left"><tr id="row45839354"><th class="cellrowborder" valign="top" width="27.27272727272727%" id="mcps1.2.4.1.1"><p id="p22000213"><a name="p22000213"></a><a name="p22000213"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.17171717171717%" id="mcps1.2.4.1.2"><p id="p37186841"><a name="p37186841"></a><a name="p37186841"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="55.55555555555556%" id="mcps1.2.4.1.3"><p id="p59344108"><a name="p59344108"></a><a name="p59344108"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row42143481"><td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.1 "><p id="p58178790"><a name="p58178790"></a><a name="p58178790"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.2.4.1.2 "><p id="p8601456153613"><a name="p8601456153613"></a><a name="p8601456153613"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.55555555555556%" headers="mcps1.2.4.1.3 "><p id="p62933377"><a name="p62933377"></a><a name="p62933377"></a>Specifies the whitelist ID.</p>
</td>
</tr>
<tr id="row29529486"><td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.1 "><p id="p43078143"><a name="p43078143"></a><a name="p43078143"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.2.4.1.2 "><p id="p66777590"><a name="p66777590"></a><a name="p66777590"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.55555555555556%" headers="mcps1.2.4.1.3 "><p id="p40275672"><a name="p40275672"></a><a name="p40275672"></a>Specifies the ID of the project where the whitelist is used.</p>
<p id="p13774541163418"><a name="p13774541163418"></a><a name="p13774541163418"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row26936734"><td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.1 "><p id="p34391822"><a name="p34391822"></a><a name="p34391822"></a>listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.2.4.1.2 "><p id="p1044313103716"><a name="p1044313103716"></a><a name="p1044313103716"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.55555555555556%" headers="mcps1.2.4.1.3 "><p id="p24747384"><a name="p24747384"></a><a name="p24747384"></a>Specifies the ID of the listener to which the whitelist is added.</p>
</td>
</tr>
<tr id="row21399872"><td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.1 "><p id="p55668057"><a name="p55668057"></a><a name="p55668057"></a>enable_whitelist</p>
</td>
<td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.2.4.1.2 "><p id="p12818767"><a name="p12818767"></a><a name="p12818767"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="55.55555555555556%" headers="mcps1.2.4.1.3 "><p id="p31687177"><a name="p31687177"></a><a name="p31687177"></a>Specifies whether to enable access control.</p>
<p id="p07333135114"><a name="p07333135114"></a><a name="p07333135114"></a><strong id="b1072540155010"><a name="b1072540155010"></a><a name="b1072540155010"></a>true</strong>: Access control is enabled.</p>
<p id="p57393175115"><a name="p57393175115"></a><a name="p57393175115"></a><strong id="b978484145016"><a name="b978484145016"></a><a name="b978484145016"></a>false</strong>: Access control is disabled.</p>
</td>
</tr>
<tr id="row16749139"><td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.1 "><p id="p14503023"><a name="p14503023"></a><a name="p14503023"></a>whitelist</p>
</td>
<td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.2.4.1.2 "><p id="p33894211"><a name="p33894211"></a><a name="p33894211"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.55555555555556%" headers="mcps1.2.4.1.3 "><p id="p61076600"><a name="p61076600"></a><a name="p61076600"></a>Specifies the IP addresses in the whitelist.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section558753351315"></a>

-   Example request: Adding a whitelist

    ```
    POST https://{Endpoint}/v2.0/lbaas/whitelists 
    
    { 
        "whitelist": { 
            "listener_id": "eabfefa3fd1740a88a47ad98e132d238",  
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


## Status Code<a name="section41969672"></a>

For details, see  [HTTP Status Codes for Enhanced Load Balancers](http-status-codes-for-enhanced-load-balancers.md).

