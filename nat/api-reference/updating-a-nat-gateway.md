# Updating a NAT Gateway<a name="nat_api_0003"></a>

## Function<a name="section53650918"></a>

This API is used to update a NAT gateway.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>**admin\_state\_up = True & status = "ACTIVE"**  can be updated. The name, description, and type of a NAT gateway can be updated.  

## URI<a name="section13096217"></a>

PUT /v2.0/nat\_gateways/\{nat\_gateway\_id\}

**Table  1**  Parameter description

<a name="table285161395713"></a>
<table><thead align="left"><tr id="row12912101317577"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.1"><p id="p791271313579"><a name="p791271313579"></a><a name="p791271313579"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.5.1.2"><p id="p7912013105718"><a name="p7912013105718"></a><a name="p7912013105718"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.3"><p id="p1391221355716"><a name="p1391221355716"></a><a name="p1391221355716"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="48%" id="mcps1.2.5.1.4"><p id="p1191216131572"><a name="p1191216131572"></a><a name="p1191216131572"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1591281345717"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p69121213115717"><a name="p69121213115717"></a><a name="p69121213115717"></a>nat_gateway_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.2 "><p id="p179129138573"><a name="p179129138573"></a><a name="p179129138573"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.3 "><p id="p1291281325710"><a name="p1291281325710"></a><a name="p1291281325710"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.5.1.4 "><p id="p20912111395719"><a name="p20912111395719"></a><a name="p20912111395719"></a>Specifies the NAT gateway ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section54160660"></a>

[Table 2](#table52686130)  describes the request parameters.

**Table  2**  Request parameters

<a name="table52686130"></a>
<table><thead align="left"><tr id="row64917235"><th class="cellrowborder" valign="top" width="24.15%" id="mcps1.2.5.1.1"><p id="p23804665"><a name="p23804665"></a><a name="p23804665"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="8.89%" id="mcps1.2.5.1.2"><p id="p20086700"><a name="p20086700"></a><a name="p20086700"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17.61%" id="mcps1.2.5.1.3"><p id="p49129749"><a name="p49129749"></a><a name="p49129749"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.35%" id="mcps1.2.5.1.4"><p id="p16410024"><a name="p16410024"></a><a name="p16410024"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row2330579495259"><td class="cellrowborder" valign="top" width="24.15%" headers="mcps1.2.5.1.1 "><p id="p872120095259"><a name="p872120095259"></a><a name="p872120095259"></a>nat_gateway</p>
</td>
<td class="cellrowborder" valign="top" width="8.89%" headers="mcps1.2.5.1.2 "><p id="p4304518595259"><a name="p4304518595259"></a><a name="p4304518595259"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.61%" headers="mcps1.2.5.1.3 "><p id="p3532861095259"><a name="p3532861095259"></a><a name="p3532861095259"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="49.35%" headers="mcps1.2.5.1.4 "><p id="p6410795695259"><a name="p6410795695259"></a><a name="p6410795695259"></a>Specifies the NAT gateway object. For details, see <a href="#table0906373491">Table 3</a>.</p>
<p id="p2978120995417"><a name="p2978120995417"></a><a name="p2978120995417"></a>Mandatory field: None. Only the <strong id="b84235270610132"><a name="b84235270610132"></a><a name="b84235270610132"></a>name</strong>, <strong id="b84235270610135"><a name="b84235270610135"></a><a name="b84235270610135"></a>description</strong>, and <strong id="b84235270610138"><a name="b84235270610138"></a><a name="b84235270610138"></a>spec</strong> fields can be updated. At least one attribute must be specified for the NAT gateway to be updated.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Description of the  **nat\_gateway**  field

<a name="table0906373491"></a>
<table><thead align="left"><tr id="row1926123710498"><th class="cellrowborder" valign="top" width="23.72%" id="mcps1.2.5.1.1"><p id="p12261203754915"><a name="p12261203754915"></a><a name="p12261203754915"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="8.219999999999999%" id="mcps1.2.5.1.2"><p id="p026183710495"><a name="p026183710495"></a><a name="p026183710495"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="18.56%" id="mcps1.2.5.1.3"><p id="p12611537194919"><a name="p12611537194919"></a><a name="p12611537194919"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.5%" id="mcps1.2.5.1.4"><p id="p4261537124914"><a name="p4261537124914"></a><a name="p4261537124914"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1526113794918"><td class="cellrowborder" valign="top" width="23.72%" headers="mcps1.2.5.1.1 "><p id="p1426114376495"><a name="p1426114376495"></a><a name="p1426114376495"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="8.219999999999999%" headers="mcps1.2.5.1.2 "><p id="p4261153734911"><a name="p4261153734911"></a><a name="p4261153734911"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.56%" headers="mcps1.2.5.1.3 "><p id="p62611137194910"><a name="p62611137194910"></a><a name="p62611137194910"></a>String(64)</p>
</td>
<td class="cellrowborder" valign="top" width="49.5%" headers="mcps1.2.5.1.4 "><p id="p626113711491"><a name="p626113711491"></a><a name="p626113711491"></a>Specifies the NAT gateway name.</p>
<p id="p426118376490"><a name="p426118376490"></a><a name="p426118376490"></a>The name can contain only digits, letters, underscores (_), and hyphens (-).</p>
</td>
</tr>
<tr id="row6261133718490"><td class="cellrowborder" valign="top" width="23.72%" headers="mcps1.2.5.1.1 "><p id="p1226113734915"><a name="p1226113734915"></a><a name="p1226113734915"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="8.219999999999999%" headers="mcps1.2.5.1.2 "><p id="p426153724918"><a name="p426153724918"></a><a name="p426153724918"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.56%" headers="mcps1.2.5.1.3 "><p id="p82619377493"><a name="p82619377493"></a><a name="p82619377493"></a>String(255)</p>
</td>
<td class="cellrowborder" valign="top" width="49.5%" headers="mcps1.2.5.1.4 "><p id="p926113710497"><a name="p926113710497"></a><a name="p926113710497"></a>Provides supplementary information about the NAT gateway.</p>
</td>
</tr>
<tr id="row142611379498"><td class="cellrowborder" valign="top" width="23.72%" headers="mcps1.2.5.1.1 "><p id="p12261193794913"><a name="p12261193794913"></a><a name="p12261193794913"></a>spec</p>
</td>
<td class="cellrowborder" valign="top" width="8.219999999999999%" headers="mcps1.2.5.1.2 "><p id="p12261153724911"><a name="p12261153724911"></a><a name="p12261153724911"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.56%" headers="mcps1.2.5.1.3 "><p id="p1326133711499"><a name="p1326133711499"></a><a name="p1326133711499"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.5%" headers="mcps1.2.5.1.4 "><p id="p142611837184914"><a name="p142611837184914"></a><a name="p142611837184914"></a>Specifies the NAT gateway type.</p>
<p id="p1126123713499"><a name="p1126123713499"></a><a name="p1126123713499"></a>The value can be:</p>
<a name="ul1526193711496"></a><a name="ul1526193711496"></a><ul id="ul1526193711496"><li><strong>1</strong>: small type, which supports up to 10,000 SNAT connections.</li><li><strong>2</strong>: medium type, which supports up to 50,000 SNAT connections.</li><li><strong>3</strong>: large type, which supports up to 200,000 SNAT connections.</li><li><strong>4</strong>: extra-large type, which supports up to 1,000,000 SNAT connections.</li></ul>
</td>
</tr>
</tbody>
</table>

## Response<a name="section17683893"></a>

[Table 4](#table26619133)  lists response parameters.

**Table  4**  Response parameters

<a name="table26619133"></a>
<table><thead align="left"><tr id="row25196298"><th class="cellrowborder" valign="top" width="31.7%" id="mcps1.2.4.1.1"><p id="p27634258"><a name="p27634258"></a><a name="p27634258"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.080000000000002%" id="mcps1.2.4.1.2"><p id="p23782439"><a name="p23782439"></a><a name="p23782439"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.22%" id="mcps1.2.4.1.3"><p id="p8475542"><a name="p8475542"></a><a name="p8475542"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row15430272"><td class="cellrowborder" valign="top" width="31.7%" headers="mcps1.2.4.1.1 "><p id="p41892502"><a name="p41892502"></a><a name="p41892502"></a>nat_gateway</p>
</td>
<td class="cellrowborder" valign="top" width="17.080000000000002%" headers="mcps1.2.4.1.2 "><p id="p37849538"><a name="p37849538"></a><a name="p37849538"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.2.4.1.3 "><p id="p28022645"><a name="p28022645"></a><a name="p28022645"></a>Specifies the NAT gateway object. For details, see <a href="#table144824405116">Table 5</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  5**  Description of the  **nat\_gateway**  field

<a name="table144824405116"></a>
<table><thead align="left"><tr id="row1265444165113"><th class="cellrowborder" valign="top" width="23.23%" id="mcps1.2.4.1.1"><p id="p2065413495118"><a name="p2065413495118"></a><a name="p2065413495118"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18.18%" id="mcps1.2.4.1.2"><p id="p1465464125116"><a name="p1465464125116"></a><a name="p1465464125116"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="58.589999999999996%" id="mcps1.2.4.1.3"><p id="p1865414435114"><a name="p1865414435114"></a><a name="p1865414435114"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row196541147512"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p176541446512"><a name="p176541446512"></a><a name="p176541446512"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p9654444513"><a name="p9654444513"></a><a name="p9654444513"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p26546435114"><a name="p26546435114"></a><a name="p26546435114"></a>Specifies the NAT gateway ID.</p>
</td>
</tr>
<tr id="row186542045510"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p10654204185111"><a name="p10654204185111"></a><a name="p10654204185111"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p2654114145119"><a name="p2654114145119"></a><a name="p2654114145119"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p86549465118"><a name="p86549465118"></a><a name="p86549465118"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row465474125112"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p36541418515"><a name="p36541418515"></a><a name="p36541418515"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p146544425110"><a name="p146544425110"></a><a name="p146544425110"></a>String(64)</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p196541435113"><a name="p196541435113"></a><a name="p196541435113"></a>Specifies the NAT gateway name.</p>
<p id="p126544413514"><a name="p126544413514"></a><a name="p126544413514"></a>The name can contain only digits, letters, underscores (_), and hyphens (-).</p>
</td>
</tr>
<tr id="row467013417513"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p1670248519"><a name="p1670248519"></a><a name="p1670248519"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p767013465115"><a name="p767013465115"></a><a name="p767013465115"></a>String(255)</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p367015455118"><a name="p367015455118"></a><a name="p367015455118"></a>Provides supplementary information about the NAT gateway.</p>
</td>
</tr>
<tr id="row367094135115"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p11670104135119"><a name="p11670104135119"></a><a name="p11670104135119"></a>spec</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p1267004195114"><a name="p1267004195114"></a><a name="p1267004195114"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p2067064195110"><a name="p2067064195110"></a><a name="p2067064195110"></a>Specifies the NAT gateway type.</p>
<p id="p76708418513"><a name="p76708418513"></a><a name="p76708418513"></a>The value can be:</p>
<a name="ul1167010455119"></a><a name="ul1167010455119"></a><ul id="ul1167010455119"><li><strong>1</strong>: small type, which supports up to 10,000 SNAT connections.</li><li><strong>2</strong>: medium type, which supports up to 50,000 SNAT connections.</li><li><strong>3</strong>: large type, which supports up to 200,000 SNAT connections.</li><li><strong>4</strong>: extra-large type, which supports up to 1,000,000 SNAT connections.</li></ul>
</td>
</tr>
<tr id="row967013418512"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p18670241513"><a name="p18670241513"></a><a name="p18670241513"></a>router_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p2670144155116"><a name="p2670144155116"></a><a name="p2670144155116"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p126701419511"><a name="p126701419511"></a><a name="p126701419511"></a>Specifies the router ID.</p>
</td>
</tr>
<tr id="row86706419513"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p46700418514"><a name="p46700418514"></a><a name="p46700418514"></a>internal_network_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p56701045510"><a name="p56701045510"></a><a name="p56701045510"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p12670746512"><a name="p12670746512"></a><a name="p12670746512"></a>Specifies the network ID of the downstream interface (the next hop of the DVR) of the NAT gateway.</p>
</td>
</tr>
<tr id="row2067015413511"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p76701143516"><a name="p76701143516"></a><a name="p76701143516"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p86704419513"><a name="p86704419513"></a><a name="p86704419513"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><a name="ul967015411514"></a><a name="ul967015411514"></a><ul id="ul967015411514"><li>Specifies the status of the NAT gateway.</li><li>For details about all its values, see <a href="resource-status-description.md#table1390614366107">Table 1</a>.</li></ul>
</td>
</tr>
<tr id="row76701542515"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p19670443510"><a name="p19670443510"></a><a name="p19670443510"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p1764614265487"><a name="p1764614265487"></a><a name="p1764614265487"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><a name="ul71858556358"></a><a name="ul71858556358"></a><ul id="ul71858556358"><li>Specifies whether the NAT gateway is up or down.</li><li>The value can be:<a name="ul16205638124410"></a><a name="ul16205638124410"></a><ul id="ul16205638124410"><li><strong id="b1082212644919"><a name="b1082212644919"></a><a name="b1082212644919"></a>true</strong>: The NAT gateway is up.</li><li><strong id="b775182813495"><a name="b775182813495"></a><a name="b775182813495"></a>false</strong>: The NAT gateway is down.</li></ul>
</li></ul>
</td>
</tr>
<tr id="row1967044145114"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p1167011416513"><a name="p1167011416513"></a><a name="p1167011416513"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p2670141515"><a name="p2670141515"></a><a name="p2670141515"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p1914253805918"><a name="p1914253805918"></a><a name="p1914253805918"></a>Specifies when the NAT gateway is created (UTC time). Its value rounds to 6 decimal places for seconds. The format is yyyy-mm-dd hh:mm:ss.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section24937315"></a>

-   Example request

    ```
    PUT https://{Endpoint}/v2.0/nat_gateways/a78fb3eb-1654-4710-8742-3fc49d5f04f8 
      {
        "nat_gateway": {
            "name": "new_name",
            "description": "new description",
            "spec": "1"
        }
    }
    ```


-   Example response

    ```
    {
        "nat_gateway": {
            "router_id": "d84f345c-80a1-4fa2-a39c-d0d397c3f09a", 
             "status": "ACTIVE", 
             "description": "new description", 
             "admin_state_up": true, 
             "tenant_id": "27e25061336f4af590faeabeb7fcd9a3", 
             "created_at": "2017-11-18 07:34:32.203044", 
             "spec": "1", 
             "internal_network_id": "89d66639-aacb-4929-969d-07080b0f9fd9", 
             "id": "a78fb3eb-1654-4710-8742-3fc49d5f04f8", 
             "name": "new_name"
        }
    } 
    ```


## Status Code<a name="section6656623"></a>

See  [Status Codes](status-codes.md).

