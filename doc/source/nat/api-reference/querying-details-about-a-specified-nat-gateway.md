# Querying Details About a Specified NAT Gateway<a name="nat_api_0062"></a>

## Function<a name="section45827181"></a>

This API is used to query details about a specified NAT gateway.

## URI<a name="section9791447"></a>

GET /v2.0/nat\_gateways/\{nat\_gateway\_id\}

**Table  1**  Parameter description

<a name="table285161395713"></a>
<table><thead align="left"><tr id="row12912101317577"><th class="cellrowborder" valign="top" width="22.57%" id="mcps1.2.5.1.1"><p id="p791271313579"><a name="p791271313579"></a><a name="p791271313579"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="8.649999999999999%" id="mcps1.2.5.1.2"><p id="p1391221355716"><a name="p1391221355716"></a><a name="p1391221355716"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="12.9%" id="mcps1.2.5.1.3"><p id="p7912013105718"><a name="p7912013105718"></a><a name="p7912013105718"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="55.879999999999995%" id="mcps1.2.5.1.4"><p id="p1191216131572"><a name="p1191216131572"></a><a name="p1191216131572"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1591281345717"><td class="cellrowborder" valign="top" width="22.57%" headers="mcps1.2.5.1.1 "><p id="p69121213115717"><a name="p69121213115717"></a><a name="p69121213115717"></a>nat_gateway_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.649999999999999%" headers="mcps1.2.5.1.2 "><p id="p1291281325710"><a name="p1291281325710"></a><a name="p1291281325710"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="12.9%" headers="mcps1.2.5.1.3 "><p id="p179129138573"><a name="p179129138573"></a><a name="p179129138573"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.879999999999995%" headers="mcps1.2.5.1.4 "><p id="p20912111395719"><a name="p20912111395719"></a><a name="p20912111395719"></a>Specifies the NAT gateway ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section54909781"></a>

None

## Response<a name="section24425986"></a>

[Table 2](#table129831149144215)  lists response parameters.

**Table  2**  Response parameter

<a name="table129831149144215"></a>
<table><thead align="left"><tr id="row2233175015424"><th class="cellrowborder" valign="top" width="20.200000000000003%" id="mcps1.2.4.1.1"><p id="p112331950124213"><a name="p112331950124213"></a><a name="p112331950124213"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="28.28%" id="mcps1.2.4.1.2"><p id="p1023335020429"><a name="p1023335020429"></a><a name="p1023335020429"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.519999999999996%" id="mcps1.2.4.1.3"><p id="p1123319502426"><a name="p1123319502426"></a><a name="p1123319502426"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1223325010421"><td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.4.1.1 "><p id="p202331450134211"><a name="p202331450134211"></a><a name="p202331450134211"></a>nat_gateway</p>
</td>
<td class="cellrowborder" valign="top" width="28.28%" headers="mcps1.2.4.1.2 "><p id="p12331150184217"><a name="p12331150184217"></a><a name="p12331150184217"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="51.519999999999996%" headers="mcps1.2.4.1.3 "><p id="p62331505427"><a name="p62331505427"></a><a name="p62331505427"></a>Specifies the NAT gateway object. For details, see <a href="#table514165011429">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Description of the  **nat\_gateway**  field

<a name="table514165011429"></a>
<table><thead align="left"><tr id="row1233175044210"><th class="cellrowborder" valign="top" width="23.23%" id="mcps1.2.4.1.1"><p id="p16233350194217"><a name="p16233350194217"></a><a name="p16233350194217"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18.18%" id="mcps1.2.4.1.2"><p id="p1123375010428"><a name="p1123375010428"></a><a name="p1123375010428"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="58.589999999999996%" id="mcps1.2.4.1.3"><p id="p2023313507424"><a name="p2023313507424"></a><a name="p2023313507424"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row623313504427"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p162338502421"><a name="p162338502421"></a><a name="p162338502421"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p92331950144219"><a name="p92331950144219"></a><a name="p92331950144219"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p5233165034219"><a name="p5233165034219"></a><a name="p5233165034219"></a>Specifies the NAT gateway ID.</p>
</td>
</tr>
<tr id="row72331550164211"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p1123335024220"><a name="p1123335024220"></a><a name="p1123335024220"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p8233450174216"><a name="p8233450174216"></a><a name="p8233450174216"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p172332504428"><a name="p172332504428"></a><a name="p172332504428"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row17233185084220"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p323355014426"><a name="p323355014426"></a><a name="p323355014426"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p323355044218"><a name="p323355044218"></a><a name="p323355044218"></a>String(64)</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p42331650144212"><a name="p42331650144212"></a><a name="p42331650144212"></a>Specifies the NAT gateway name.</p>
<p id="p72333505429"><a name="p72333505429"></a><a name="p72333505429"></a>The name can contain only digits, letters, underscores (_), and hyphens (-).</p>
</td>
</tr>
<tr id="row1623315018422"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p19233145020424"><a name="p19233145020424"></a><a name="p19233145020424"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p423318503426"><a name="p423318503426"></a><a name="p423318503426"></a>String(255)</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p923335014212"><a name="p923335014212"></a><a name="p923335014212"></a>Provides supplementary information about the NAT gateway.</p>
</td>
</tr>
<tr id="row1623315506427"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p18233350184218"><a name="p18233350184218"></a><a name="p18233350184218"></a>spec</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p15233105018428"><a name="p15233105018428"></a><a name="p15233105018428"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p1023385084218"><a name="p1023385084218"></a><a name="p1023385084218"></a>Specifies the NAT gateway type.</p>
<p id="p1223319508422"><a name="p1223319508422"></a><a name="p1223319508422"></a>The value can be:</p>
<a name="ul132334508424"></a><a name="ul132334508424"></a><ul id="ul132334508424"><li><strong>1</strong>: small type, which supports up to 10,000 SNAT connections.</li><li><strong>2</strong>: medium type, which supports up to 50,000 SNAT connections.</li><li><strong>3</strong>: large type, which supports up to 200,000 SNAT connections.</li><li><strong>4</strong>: extra-large type, which supports up to 1,000,000 SNAT connections.</li></ul>
</td>
</tr>
<tr id="row42331050144212"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p1723325015428"><a name="p1723325015428"></a><a name="p1723325015428"></a>router_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p3233115094213"><a name="p3233115094213"></a><a name="p3233115094213"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p102331150144211"><a name="p102331150144211"></a><a name="p102331150144211"></a>Specifies the router ID.</p>
</td>
</tr>
<tr id="row72331650164215"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p8233195017429"><a name="p8233195017429"></a><a name="p8233195017429"></a>internal_network_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p223314508421"><a name="p223314508421"></a><a name="p223314508421"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p4233125084214"><a name="p4233125084214"></a><a name="p4233125084214"></a>Specifies the network ID of the downstream interface (the next hop of the DVR) of the NAT gateway.</p>
</td>
</tr>
<tr id="row102339502423"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p82331150114212"><a name="p82331150114212"></a><a name="p82331150114212"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p1823311508429"><a name="p1823311508429"></a><a name="p1823311508429"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><a name="ul9233155034214"></a><a name="ul9233155034214"></a><ul id="ul9233155034214"><li>Specifies the NAT gateway status.</li><li>For details about all its values, see <a href="resource-status-description.md#table1390614366107">Table 1</a>.</li></ul>
</td>
</tr>
<tr id="row20233450104210"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p32333502427"><a name="p32333502427"></a><a name="p32333502427"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p1764614265487"><a name="p1764614265487"></a><a name="p1764614265487"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><a name="ul71858556358"></a><a name="ul71858556358"></a><ul id="ul71858556358"><li>Specifies whether the NAT gateway is up or down.</li><li>The value can be:<a name="ul16205638124410"></a><a name="ul16205638124410"></a><ul id="ul16205638124410"><li><strong id="b951617194433"><a name="b951617194433"></a><a name="b951617194433"></a>true</strong>: The NAT gateway is up.</li><li><strong id="b44261220114312"><a name="b44261220114312"></a><a name="b44261220114312"></a>false</strong>: The NAT gateway is down.</li></ul>
</li></ul>
</td>
</tr>
<tr id="row22331050154211"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p723305014427"><a name="p723305014427"></a><a name="p723305014427"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p423312509427"><a name="p423312509427"></a><a name="p423312509427"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p16351227165916"><a name="p16351227165916"></a><a name="p16351227165916"></a>Specifies when the NAT gateway is created (UTC time). Its value rounds to 6 decimal places for seconds. The format is yyyy-mm-dd hh:mm:ss.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section18507287"></a>

-   Example request

    ```
    GET https://{Endpoint}/v2.0/nat_gateways/a78fb3eb-1654-4710-8742-3fc49d5f04f8
    ```


-   Example response

    ```
    {
        "nat_gateway": { 
             "router_id": "d84f345c-80a1-4fa2-a39c-d0d397c3f09a", 
             "status": "ACTIVE", 
             "description": "my nat gateway 01", 
             "admin_state_up": true, 
             "tenant_id": "27e25061336f4af590faeabeb7fcd9a3", 
             "created_at": "2017-11-18 07:34:32.203044", 
             "spec": "1", 
             "internal_network_id": "89d66639-aacb-4929-969d-07080b0f9fd9", 
             "id": "a78fb3eb-1654-4710-8742-3fc49d5f04f8", 
             "name": "nat_001" 
        }
    }
    ```


## Status Code<a name="section22695302"></a>

See  [Status Codes](status-codes.md).

