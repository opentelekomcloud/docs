# Querying Details of a Whitelist<a name="EN-US_TOPIC_0143878051"></a>

## Function<a name="section8091756"></a>

This API is used to query details about a whitelist using its ID.

## URI<a name="section5716946"></a>

GET /v2.0/lbaas/whitelists/\{whitelist\_id\}

**Table  1**  Parameter description

<a name="table25787259"></a>
<table><thead align="left"><tr id="row48433782"><th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.2.5.1.1"><p id="p30822233"><a name="p30822233"></a><a name="p30822233"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12.121212121212121%" id="mcps1.2.5.1.2"><p id="p13572982"><a name="p13572982"></a><a name="p13572982"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17.171717171717173%" id="mcps1.2.5.1.3"><p id="p25669747"><a name="p25669747"></a><a name="p25669747"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.515151515151516%" id="mcps1.2.5.1.4"><p id="p65983608"><a name="p65983608"></a><a name="p65983608"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row43072046"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.1 "><p id="p66283708"><a name="p66283708"></a><a name="p66283708"></a>whitelist_id</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.2 "><p id="p271307"><a name="p271307"></a><a name="p271307"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.3 "><p id="p21975939"><a name="p21975939"></a><a name="p21975939"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.2.5.1.4 "><p id="p35220619"><a name="p35220619"></a><a name="p35220619"></a>Specifies the whitelist ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section60419481"></a>

None

## Response<a name="section6904420"></a>

**Table  2**  Response parameters

<a name="table47760062"></a>
<table><thead align="left"><tr id="row15270149"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="p28922579"><a name="p28922579"></a><a name="p28922579"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.4.1.2"><p id="p61027537"><a name="p61027537"></a><a name="p61027537"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="63%" id="mcps1.2.4.1.3"><p id="p44283431"><a name="p44283431"></a><a name="p44283431"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row30188158"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p29321725"><a name="p29321725"></a><a name="p29321725"></a>whitelist</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="p26249549"><a name="p26249549"></a><a name="p26249549"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p45838742"><a name="p45838742"></a><a name="p45838742"></a>Specifies the whitelist. For details, see <a href="#table21950591">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **whitelist**  parameter description

<a name="table21950591"></a>
<table><thead align="left"><tr id="row45839354"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="p22000213"><a name="p22000213"></a><a name="p22000213"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.4.1.2"><p id="p37186841"><a name="p37186841"></a><a name="p37186841"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.2.4.1.3"><p id="p59344108"><a name="p59344108"></a><a name="p59344108"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row42143481"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p58178790"><a name="p58178790"></a><a name="p58178790"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p0581358125019"><a name="p0581358125019"></a><a name="p0581358125019"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.2.4.1.3 "><p id="p62933377"><a name="p62933377"></a><a name="p62933377"></a>Specifies the whitelist ID.</p>
</td>
</tr>
<tr id="row29529486"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p43078143"><a name="p43078143"></a><a name="p43078143"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p66777590"><a name="p66777590"></a><a name="p66777590"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.2.4.1.3 "><p id="p40275672"><a name="p40275672"></a><a name="p40275672"></a>Specifies the ID of the project where the forwarding rule is used.</p>
<p id="p1264211013318"><a name="p1264211013318"></a><a name="p1264211013318"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row26936734"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p34391822"><a name="p34391822"></a><a name="p34391822"></a>listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p83812145113"><a name="p83812145113"></a><a name="p83812145113"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.2.4.1.3 "><p id="p24747384"><a name="p24747384"></a><a name="p24747384"></a>Specifies the ID of the listener to which the whitelist is added.</p>
</td>
</tr>
<tr id="row21399872"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p55668057"><a name="p55668057"></a><a name="p55668057"></a>enable_whitelist</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p12818767"><a name="p12818767"></a><a name="p12818767"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.2.4.1.3 "><p id="p31687177"><a name="p31687177"></a><a name="p31687177"></a>Specifies whether to enable access control.</p>
<p id="p07333135114"><a name="p07333135114"></a><a name="p07333135114"></a><strong id="b176871916576"><a name="b176871916576"></a><a name="b176871916576"></a>true</strong>: Access control is enabled.</p>
<p id="p57393175115"><a name="p57393175115"></a><a name="p57393175115"></a><strong id="b1563012258534"><a name="b1563012258534"></a><a name="b1563012258534"></a>false</strong>: Access control is disabled.</p>
</td>
</tr>
<tr id="row16749139"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p14503023"><a name="p14503023"></a><a name="p14503023"></a>whitelist</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p33894211"><a name="p33894211"></a><a name="p33894211"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.2.4.1.3 "><p id="p61076600"><a name="p61076600"></a><a name="p61076600"></a>Specifies the IP addresses in the whitelist.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section7142737162217"></a>

-   Example request: Querying details of a whitelist

    ```
    GET https://{Endpoint}/v2.0/lbaas/whitelists/09e64049-2ab0-4763-a8c5-f4207875dc3e
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


## Status Code<a name="section79527292816"></a>

For details, see  [HTTP Status Codes for Enhanced Load Balancers](http-status-codes-for-enhanced-load-balancers.md).

