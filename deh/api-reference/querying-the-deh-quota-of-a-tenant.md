# Querying the DeH Quota of a Tenant<a name="EN-US_TOPIC_0087389324"></a>

## Function<a name="section5174319"></a>

This API is used to query the DeH quota of a tenant.

## URI<a name="section46568871"></a>

GET /v1.0/\{project\_id\}/quota-sets/\{tenant\_id\}

[Table 1](#table291625114015)  describes the parameters.

**Table  1**  Parameters description

<a name="table291625114015"></a>
<table><thead align="left"><tr id="row291610574011"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p1467218184410"><a name="p1467218184410"></a><a name="p1467218184410"></a><strong id="b14327624133118"><a name="b14327624133118"></a><a name="b14327624133118"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p0675111204414"><a name="p0675111204414"></a><a name="p0675111204414"></a><strong id="b19815152817316"><a name="b19815152817316"></a><a name="b19815152817316"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p69548610432"><a name="p69548610432"></a><a name="p69548610432"></a><strong id="b9784429103118"><a name="b9784429103118"></a><a name="b9784429103118"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p19679111448"><a name="p19679111448"></a><a name="p19679111448"></a><strong id="b11409311318"><a name="b11409311318"></a><a name="b11409311318"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row69161956409"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p126868117449"><a name="p126868117449"></a><a name="p126868117449"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p1688101174411"><a name="p1688101174411"></a><a name="p1688101174411"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p59527664313"><a name="p59527664313"></a><a name="p59527664313"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p1969317113442"><a name="p1969317113442"></a><a name="p1969317113442"></a>Specifies the project ID.</p>
<p id="p7376194915119"><a name="p7376194915119"></a><a name="p7376194915119"></a>For details about how to obtain the project ID, see <a href="https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html" target="_blank" rel="noopener noreferrer">Obtaining Required Information</a>.</p>
</td>
</tr>
<tr id="row2895162113492"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1895162114495"><a name="p1895162114495"></a><a name="p1895162114495"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p12311833124919"><a name="p12311833124919"></a><a name="p12311833124919"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p72331733174920"><a name="p72331733174920"></a><a name="p72331733174920"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p15234143317494"><a name="p15234143317494"></a><a name="p15234143317494"></a>Specifies the tenant ID.</p>
<p id="p858154817367"><a name="p858154817367"></a><a name="p858154817367"></a>You can obtain the DeH ID from the DeH console or using the <a href="querying-dehs.md">Querying DeHs</a> API.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section13982202"></a>

-   Request parameters

    You can add the  **resource**  parameter to the URI. For example:

    **/v1.0/\{project\_id\}/quota-sets/\{tenant\_id\}?resource=\{resource\}**

    <a name="table1957580"></a>
    <table><thead align="left"><tr id="row896237"><th class="cellrowborder" valign="top" width="21%" id="mcps1.1.6.1.1"><p id="p5486348"><a name="p5486348"></a><a name="p5486348"></a><strong id="b016524515325"><a name="b016524515325"></a><a name="b016524515325"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.1.6.1.2"><p id="p41741032"><a name="p41741032"></a><a name="p41741032"></a><strong id="b20698105223211"><a name="b20698105223211"></a><a name="b20698105223211"></a>In</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.1.6.1.3"><p id="p25580392"><a name="p25580392"></a><a name="p25580392"></a><strong id="b2271195473213"><a name="b2271195473213"></a><a name="b2271195473213"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17%" id="mcps1.1.6.1.4"><p id="p58745844"><a name="p58745844"></a><a name="p58745844"></a><strong id="b88721555143213"><a name="b88721555143213"></a><a name="b88721555143213"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="34%" id="mcps1.1.6.1.5"><p id="p60792949"><a name="p60792949"></a><a name="p60792949"></a><strong id="b1282019564324"><a name="b1282019564324"></a><a name="b1282019564324"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row39387211"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.6.1.1 "><p id="p36247516"><a name="p36247516"></a><a name="p36247516"></a>resource</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.2 "><p id="p50367649"><a name="p50367649"></a><a name="p50367649"></a>query</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.3 "><p id="p53247746"><a name="p53247746"></a><a name="p53247746"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.6.1.4 "><p id="p18100201"><a name="p18100201"></a><a name="p18100201"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.6.1.5 "><p id="p56830139"><a name="p56830139"></a><a name="p56830139"></a>Specifies the resource type.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    GET https://{Endpoint}/v1.0/9c53a566cb3443ab910cf0daebca90c4/quota-sets/45df5566cb3443ab910cf0daebcapoi8
    ```


## Response<a name="section58730959"></a>

-   Response parameters

    <a name="table23002745"></a>
    <table><thead align="left"><tr id="row60524524"><th class="cellrowborder" valign="top" width="25.92740725927407%" id="mcps1.1.4.1.1"><p id="p3539410"><a name="p3539410"></a><a name="p3539410"></a><strong id="b131080712539"><a name="b131080712539"></a><a name="b131080712539"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.45765423457654%" id="mcps1.1.4.1.2"><p id="p18256764"><a name="p18256764"></a><a name="p18256764"></a><strong id="b736858125317"><a name="b736858125317"></a><a name="b736858125317"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.614938506149386%" id="mcps1.1.4.1.3"><p id="p60417086"><a name="p60417086"></a><a name="p60417086"></a><strong id="b19122312535"><a name="b19122312535"></a><a name="b19122312535"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6882862"><td class="cellrowborder" valign="top" width="25.92740725927407%" headers="mcps1.1.4.1.1 "><p id="p20640979"><a name="p20640979"></a><a name="p20640979"></a>quota_set</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.45765423457654%" headers="mcps1.1.4.1.2 "><p id="p61306625"><a name="p61306625"></a><a name="p61306625"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.614938506149386%" headers="mcps1.1.4.1.3 "><p id="p49345813"><a name="p49345813"></a><a name="p49345813"></a>Specifies the quota set of a DeH.</p>
    </td>
    </tr>
    <tr id="row41459137"><td class="cellrowborder" valign="top" width="25.92740725927407%" headers="mcps1.1.4.1.1 "><p id="p2746927"><a name="p2746927"></a><a name="p2746927"></a>resource</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.45765423457654%" headers="mcps1.1.4.1.2 "><p id="p21174538"><a name="p21174538"></a><a name="p21174538"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.614938506149386%" headers="mcps1.1.4.1.3 "><p id="p10796581"><a name="p10796581"></a><a name="p10796581"></a>Specifies the resource type.</p>
    </td>
    </tr>
    <tr id="row30060365"><td class="cellrowborder" valign="top" width="25.92740725927407%" headers="mcps1.1.4.1.1 "><p id="p18970462"><a name="p18970462"></a><a name="p18970462"></a>hard_limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.45765423457654%" headers="mcps1.1.4.1.2 "><p id="p60212448"><a name="p60212448"></a><a name="p60212448"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.614938506149386%" headers="mcps1.1.4.1.3 "><p id="p08713555545"><a name="p08713555545"></a><a name="p08713555545"></a>Specifies the quota hard limit. </p>
    <p id="OLE_LINK45"><a name="OLE_LINK45"></a><a name="OLE_LINK45"></a><strong id="b1741851481812"><a name="b1741851481812"></a><a name="b1741851481812"></a>-1</strong> indicates that the resource quota is not limited.</p>
    </td>
    </tr>
    <tr id="row45458457"><td class="cellrowborder" valign="top" width="25.92740725927407%" headers="mcps1.1.4.1.1 "><p id="p58256364"><a name="p58256364"></a><a name="p58256364"></a>used</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.45765423457654%" headers="mcps1.1.4.1.2 "><p id="p21145081"><a name="p21145081"></a><a name="p21145081"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.614938506149386%" headers="mcps1.1.4.1.3 "><p id="p18856923"><a name="p18856923"></a><a name="p18856923"></a>Specifies the used amount of the quota.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "quota_set": [
            {
                "resource": "c1",
                "hard_limit": 5,
                "used": 2
            },
            {
                "resource": "m1",
                "hard_limit": 5,
                "used": 0
            },
            {
                "resource": "h1",
                "hard_limit": 5,
                "used": 2
            },
            {
                "resource": "d1",
                "hard_limit": 5,
                "used": 2
            }
        ]
    }
    ```


## Status Code<a name="section66523006"></a>

See  [Status Codes](status-codes.md).

