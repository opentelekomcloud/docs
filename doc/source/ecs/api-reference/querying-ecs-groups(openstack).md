# Querying ECS Groups<a name="EN-US_TOPIC_0065817721"></a>

## Function<a name="en-us_topic_0057973158_section14574577"></a>

This API is used to query ECS groups.

## URI<a name="en-us_topic_0057973158_section64062336"></a>

GET /v2/\{project\_id\}/os-server-groups\{?all\_projects\}

GET /v2.1/\{project\_id\}/os-server-groups\{?all\_projects\}

[Table 1](#en-us_topic_0057973158_en-us_topic_0020212650_table62669527)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057973158_en-us_topic_0020212650_table62669527"></a>
<table><thead align="left"><tr id="en-us_topic_0057973158_en-us_topic_0020212650_row33894570"><th class="cellrowborder" valign="top" width="16.98%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.73%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.29%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973158_en-us_topic_0020212650_row8419032"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973158_en-us_topic_0020212650_p10852974"><a name="en-us_topic_0057973158_en-us_topic_0020212650_p10852974"></a><a name="en-us_topic_0057973158_en-us_topic_0020212650_p10852974"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.73%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973158_en-us_topic_0020212650_p6675738"><a name="en-us_topic_0057973158_en-us_topic_0020212650_p6675738"></a><a name="en-us_topic_0057973158_en-us_topic_0020212650_p6675738"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.29%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

Parameters in the following table can be used as URI parameters to filter query results.

Usage: /v2/\{project\_id\}/os-server-groups?all\_projects=True

[Table 2](#en-us_topic_0057973158_table7928881)  describes the request parameters.

**Table  2**  Request parameters

<a name="en-us_topic_0057973158_table7928881"></a>
<table><thead align="left"><tr id="en-us_topic_0057973158_row34501696"><th class="cellrowborder" valign="top" width="16.869999999999997%" id="mcps1.2.5.1.1"><p id="en-us_topic_0057972670_p57733603"><a name="en-us_topic_0057972670_p57733603"></a><a name="en-us_topic_0057972670_p57733603"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.96%" id="mcps1.2.5.1.2"><p id="en-us_topic_0057972670_p27743545"><a name="en-us_topic_0057972670_p27743545"></a><a name="en-us_topic_0057972670_p27743545"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.66%" id="mcps1.2.5.1.3"><p id="en-us_topic_0057972670_p45910260"><a name="en-us_topic_0057972670_p45910260"></a><a name="en-us_topic_0057972670_p45910260"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50.51%" id="mcps1.2.5.1.4"><p id="en-us_topic_0057972670_p32634650"><a name="en-us_topic_0057972670_p32634650"></a><a name="en-us_topic_0057972670_p32634650"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973158_row40757976"><td class="cellrowborder" valign="top" width="16.869999999999997%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973158_p13061725"><a name="en-us_topic_0057973158_p13061725"></a><a name="en-us_topic_0057973158_p13061725"></a>all_projects</p>
</td>
<td class="cellrowborder" valign="top" width="17.96%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057973158_p67068709"><a name="en-us_topic_0057973158_p67068709"></a><a name="en-us_topic_0057973158_p67068709"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.66%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973158_p51366782"><a name="en-us_topic_0057973158_p51366782"></a><a name="en-us_topic_0057973158_p51366782"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="50.51%" headers="mcps1.2.5.1.4 "><p id="p5581113710555"><a name="p5581113710555"></a><a name="p5581113710555"></a>Determines whether to query ECSs of all tenants.</p>
<p id="p134905286119"><a name="p134905286119"></a><a name="p134905286119"></a>The ECSs of all tenants can be queried only if this parameter is used, even if its value is not <strong id="b842352706155247"><a name="b842352706155247"></a><a name="b842352706155247"></a>True</strong>.</p>
</td>
</tr>
</tbody>
</table>

-   Tenants can query only their  **server\_group**  lists. A maximum of 1000 query results can be returned.

## Request<a name="section3227155991615"></a>

None

## Response<a name="en-us_topic_0057973158_section10175274"></a>

[Table 3](#en-us_topic_0057973158_table37835893)  describes the response parameters.

**Table  3**  Response parameters

<a name="en-us_topic_0057973158_table37835893"></a>
<table><thead align="left"><tr id="en-us_topic_0057973158_row61250015"><th class="cellrowborder" valign="top" width="18.740000000000002%" id="mcps1.2.5.1.1"><p id="p64251742182612"><a name="p64251742182612"></a><a name="p64251742182612"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.49%" id="mcps1.2.5.1.2"><p id="p4425114212266"><a name="p4425114212266"></a><a name="p4425114212266"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.6%" id="mcps1.2.5.1.3"><p id="p164258426261"><a name="p164258426261"></a><a name="p164258426261"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.17%" id="mcps1.2.5.1.4"><p id="p1942534214263"><a name="p1942534214263"></a><a name="p1942534214263"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973158_row43900666"><td class="cellrowborder" valign="top" width="18.740000000000002%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973158_p66293025"><a name="en-us_topic_0057973158_p66293025"></a><a name="en-us_topic_0057973158_p66293025"></a>server_groups</p>
</td>
<td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057973158_p15994374"><a name="en-us_topic_0057973158_p15994374"></a><a name="en-us_topic_0057973158_p15994374"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.6%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973158_p1025965"><a name="en-us_topic_0057973158_p1025965"></a><a name="en-us_topic_0057973158_p1025965"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="49.17%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973158_p20475923"><a name="en-us_topic_0057973158_p20475923"></a><a name="en-us_topic_0057973158_p20475923"></a>Specifies the ECS group information.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **server\_groups**  parameter information

<a name="en-us_topic_0057973158_table47937085"></a>
<table><thead align="left"><tr id="en-us_topic_0057973158_row65811616"><th class="cellrowborder" valign="top" width="16.919999999999998%" id="mcps1.2.5.1.1"><p id="p6654124612269"><a name="p6654124612269"></a><a name="p6654124612269"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.52%" id="mcps1.2.5.1.2"><p id="p193178411326"><a name="p193178411326"></a><a name="p193178411326"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16.28%" id="mcps1.2.5.1.3"><p id="p1865454611261"><a name="p1865454611261"></a><a name="p1865454611261"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.28%" id="mcps1.2.5.1.4"><p id="p6654446102616"><a name="p6654446102616"></a><a name="p6654446102616"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973158_row33147825"><td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973158_p619317"><a name="en-us_topic_0057973158_p619317"></a><a name="en-us_topic_0057973158_p619317"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="17.52%" headers="mcps1.2.5.1.2 "><p id="p731784113211"><a name="p731784113211"></a><a name="p731784113211"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973158_p50164680"><a name="en-us_topic_0057973158_p50164680"></a><a name="en-us_topic_0057973158_p50164680"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.28%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973158_p28602690"><a name="en-us_topic_0057973158_p28602690"></a><a name="en-us_topic_0057973158_p28602690"></a>Specifies the ECS group UUID.</p>
</td>
</tr>
<tr id="en-us_topic_0057973158_row56097620"><td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973158_p47613365"><a name="en-us_topic_0057973158_p47613365"></a><a name="en-us_topic_0057973158_p47613365"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="17.52%" headers="mcps1.2.5.1.2 "><p id="p73176418323"><a name="p73176418323"></a><a name="p73176418323"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973158_p31477322"><a name="en-us_topic_0057973158_p31477322"></a><a name="en-us_topic_0057973158_p31477322"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.28%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973158_p28736562"><a name="en-us_topic_0057973158_p28736562"></a><a name="en-us_topic_0057973158_p28736562"></a>Specifies the ECS group name.</p>
</td>
</tr>
<tr id="en-us_topic_0057973158_row29632828"><td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973158_p51448853"><a name="en-us_topic_0057973158_p51448853"></a><a name="en-us_topic_0057973158_p51448853"></a>members</p>
</td>
<td class="cellrowborder" valign="top" width="17.52%" headers="mcps1.2.5.1.2 "><p id="p163171544326"><a name="p163171544326"></a><a name="p163171544326"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973158_p6607563"><a name="en-us_topic_0057973158_p6607563"></a><a name="en-us_topic_0057973158_p6607563"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="49.28%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973158_p67004395"><a name="en-us_topic_0057973158_p67004395"></a><a name="en-us_topic_0057973158_p67004395"></a>Specifies the ECSs in an ECS group.</p>
</td>
</tr>
<tr id="en-us_topic_0057973158_row66168651"><td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973158_p58060511"><a name="en-us_topic_0057973158_p58060511"></a><a name="en-us_topic_0057973158_p58060511"></a>metadata</p>
</td>
<td class="cellrowborder" valign="top" width="17.52%" headers="mcps1.2.5.1.2 "><p id="p173171444324"><a name="p173171444324"></a><a name="p173171444324"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973158_p5280980"><a name="en-us_topic_0057973158_p5280980"></a><a name="en-us_topic_0057973158_p5280980"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="49.28%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973158_p20340992"><a name="en-us_topic_0057973158_p20340992"></a><a name="en-us_topic_0057973158_p20340992"></a>Specifies ECS group metadata.</p>
</td>
</tr>
<tr id="en-us_topic_0057973158_row32671040185312"><td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973158_p64633146"><a name="en-us_topic_0057973158_p64633146"></a><a name="en-us_topic_0057973158_p64633146"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.52%" headers="mcps1.2.5.1.2 "><p id="p12317204163220"><a name="p12317204163220"></a><a name="p12317204163220"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973158_p793464"><a name="en-us_topic_0057973158_p793464"></a><a name="en-us_topic_0057973158_p793464"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.28%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973158_p38538274"><a name="en-us_topic_0057973158_p38538274"></a><a name="en-us_topic_0057973158_p38538274"></a>Specifies the tenant ID in UUID format for the ECS group.</p>
<p id="en-us_topic_0057973158_p457295075618"><a name="en-us_topic_0057973158_p457295075618"></a><a name="en-us_topic_0057973158_p457295075618"></a>This field is newly added in version 2.13.</p>
</td>
</tr>
<tr id="en-us_topic_0057973158_row146121548185317"><td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973158_p11612848145317"><a name="en-us_topic_0057973158_p11612848145317"></a><a name="en-us_topic_0057973158_p11612848145317"></a>policies</p>
</td>
<td class="cellrowborder" valign="top" width="17.52%" headers="mcps1.2.5.1.2 "><p id="p131734123219"><a name="p131734123219"></a><a name="p131734123219"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973158_p961210488537"><a name="en-us_topic_0057973158_p961210488537"></a><a name="en-us_topic_0057973158_p961210488537"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="49.28%" headers="mcps1.2.5.1.4 "><div class="p" id="p11241458144516"><a name="p11241458144516"></a><a name="p11241458144516"></a>Specifies the policies associated with an ECS group. Options:<a name="en-us_topic_0057973153_ul1237514118527"></a><a name="en-us_topic_0057973153_ul1237514118527"></a><ul id="en-us_topic_0057973153_ul1237514118527"><li><strong id="b76011237203011"><a name="b76011237203011"></a><a name="b76011237203011"></a>anti-affinity</strong>: ECSs in this group must be deployed on different hosts.</li><li><strong id="b25134843012"><a name="b25134843012"></a><a name="b25134843012"></a>affinity</strong>: ECSs in this group must be deployed on the same host.</li><li><strong id="b433245743011"><a name="b433245743011"></a><a name="b433245743011"></a>soft-anti-affinity</strong>: ECSs in this group are deployed on different hosts if possible. If the ECSs cannot be deployed on different hosts, deploy them based on the actual condition for successful ECS creation.</li><li><strong id="b1613110294319"><a name="b1613110294319"></a><a name="b1613110294319"></a>soft-affinity</strong>: ECSs in this group are deployed on the same host if possible. If the ECSs cannot be deployed on the same host, deploy them based on the actual condition for successful ECS creation.<div class="note" id="en-us_topic_0057973153_note172209325315"><a name="en-us_topic_0057973153_note172209325315"></a><a name="en-us_topic_0057973153_note172209325315"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0057973153_p17221036536"><a name="en-us_topic_0057973153_p17221036536"></a><a name="en-us_topic_0057973153_p17221036536"></a>Only the anti-affinity policy is supported.</p>
</div></div>
</li></ul>
</div>
</td>
</tr>
<tr id="en-us_topic_0057973158_row1110365011537"><td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973158_p110325019536"><a name="en-us_topic_0057973158_p110325019536"></a><a name="en-us_topic_0057973158_p110325019536"></a>user_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.52%" headers="mcps1.2.5.1.2 "><p id="p12317134183217"><a name="p12317134183217"></a><a name="p12317134183217"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973158_p1310325019539"><a name="en-us_topic_0057973158_p1310325019539"></a><a name="en-us_topic_0057973158_p1310325019539"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.28%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973158_p16833172165712"><a name="en-us_topic_0057973158_p16833172165712"></a><a name="en-us_topic_0057973158_p16833172165712"></a>Specifies the user ID in UUID format for the ECS group.</p>
<p id="en-us_topic_0057973158_p1783472155719"><a name="en-us_topic_0057973158_p1783472155719"></a><a name="en-us_topic_0057973158_p1783472155719"></a>This field is newly added in version 2.13.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="en-us_topic_0057973158_section24468610"></a>

```
GET https://{endpoint}/v2/9c53a566cb3443ab910cf0daebca90c4/os-server-groups
GET https://{endpoint}/v2.1/9c53a566cb3443ab910cf0daebca90c4/os-server-groups
```

## Example Response<a name="section451882185114"></a>

```
{
    "server_groups": [
        {
            "id": "616fb98f-46ca-475e-917e-2563e5a8cd19",
            "name": "test",
            "policies": ["anti-affinity"],
            "members": [],
            "metadata": {},
            "project_id": "9c53a566cb3443ab910cf0daebca90c4"
        }
    ]
}
```

## Returned Values<a name="en-us_topic_0057973158_section1220312142315"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

