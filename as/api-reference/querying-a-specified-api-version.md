# Querying a Specified API Version<a name="EN-US_TOPIC_0133153747"></a>

## Function<a name="section11355891"></a>

This interface is used to query a specified API version of the AS service.

## URI<a name="section35094160"></a>

GET /\{api\_version\}

**Table  1**  Parameter description

<a name="table53255854"></a>
<table><thead align="left"><tr id="row14242537"><th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.2.5.1.1"><p id="p12794876"><a name="p12794876"></a><a name="p12794876"></a><strong id="b1928321516472"><a name="b1928321516472"></a><a name="b1928321516472"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.2.5.1.2"><p id="p29752015"><a name="p29752015"></a><a name="p29752015"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16.161616161616163%" id="mcps1.2.5.1.3"><p id="p61102986"><a name="p61102986"></a><a name="p61102986"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="44.44444444444445%" id="mcps1.2.5.1.4"><p id="p50394838"><a name="p50394838"></a><a name="p50394838"></a><strong id="b90161613473"><a name="b90161613473"></a><a name="b90161613473"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row5926171820323"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.1 "><p id="p20926201863219"><a name="p20926201863219"></a><a name="p20926201863219"></a>api_version</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.2 "><p id="p5926151873215"><a name="p5926151873215"></a><a name="p5926151873215"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.3 "><p id="p992671833216"><a name="p992671833216"></a><a name="p992671833216"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.5.1.4 "><p id="p1392631853211"><a name="p1392631853211"></a><a name="p1392631853211"></a>Specifies the ID of the AS API version.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section47411987"></a>

-   Request parameters

    None

-   Example request

    This example shows how to query V1 AS API.

    ```
    GET https://{Endpoint}/v1
    ```


## Response Message<a name="section24054701"></a>

-   Response parameters

    **Table  2**  Response parameters

    <a name="table59665636"></a>
    <table><thead align="left"><tr id="row28755990"><th class="cellrowborder" valign="top" width="19.24%" id="mcps1.2.4.1.1"><p id="p47533853"><a name="p47533853"></a><a name="p47533853"></a><strong id="b379571610477"><a name="b379571610477"></a><a name="b379571610477"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.919999999999998%" id="mcps1.2.4.1.2"><p id="p25036876"><a name="p25036876"></a><a name="p25036876"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="62.839999999999996%" id="mcps1.2.4.1.3"><p id="p14721100"><a name="p14721100"></a><a name="p14721100"></a><strong id="b6784317154719"><a name="b6784317154719"></a><a name="b6784317154719"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row34736162"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="p1654215818362"><a name="p1654215818362"></a><a name="p1654215818362"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.919999999999998%" headers="mcps1.2.4.1.2 "><p id="p77023552159"><a name="p77023552159"></a><a name="p77023552159"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.839999999999996%" headers="mcps1.2.4.1.3 "><p id="p48612303"><a name="p48612303"></a><a name="p48612303"></a>Specifies a specified API version.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **version**  field description

    <a name="table786171513527"></a>
    <table><thead align="left"><tr id="row16870715205219"><th class="cellrowborder" valign="top" width="19.23192319231923%" id="mcps1.2.4.1.1"><p id="p787314157521"><a name="p787314157521"></a><a name="p787314157521"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.92179217921792%" id="mcps1.2.4.1.2"><p id="p15875415185216"><a name="p15875415185216"></a><a name="p15875415185216"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="62.84628462846285%" id="mcps1.2.4.1.3"><p id="p1487831516528"><a name="p1487831516528"></a><a name="p1487831516528"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1288051545213"><td class="cellrowborder" valign="top" width="19.23192319231923%" headers="mcps1.2.4.1.1 "><p id="p198824151526"><a name="p198824151526"></a><a name="p198824151526"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.92179217921792%" headers="mcps1.2.4.1.2 "><p id="p4884915105217"><a name="p4884915105217"></a><a name="p4884915105217"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.84628462846285%" headers="mcps1.2.4.1.3 "><p id="p088519150526"><a name="p088519150526"></a><a name="p088519150526"></a>Specifies the API version ID.</p>
    </td>
    </tr>
    <tr id="row8887191525212"><td class="cellrowborder" valign="top" width="19.23192319231923%" headers="mcps1.2.4.1.1 "><p id="p9888151505213"><a name="p9888151505213"></a><a name="p9888151505213"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.92179217921792%" headers="mcps1.2.4.1.2 "><p id="p1489112150526"><a name="p1489112150526"></a><a name="p1489112150526"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.84628462846285%" headers="mcps1.2.4.1.3 "><p id="p1894161514527"><a name="p1894161514527"></a><a name="p1894161514527"></a>Specifies the API URL. For details, see <a href="#t759e6d15d244474e8f286185ede143fb">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="row20895111565214"><td class="cellrowborder" valign="top" width="19.23192319231923%" headers="mcps1.2.4.1.1 "><p id="p9107111411399"><a name="p9107111411399"></a><a name="p9107111411399"></a>min_version</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.92179217921792%" headers="mcps1.2.4.1.2 "><p id="p58981015115218"><a name="p58981015115218"></a><a name="p58981015115218"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.84628462846285%" headers="mcps1.2.4.1.3 "><p id="p19907734114018"><a name="p19907734114018"></a><a name="p19907734114018"></a>Specifies the earliest supported API version number.</p>
    </td>
    </tr>
    <tr id="row9901141525214"><td class="cellrowborder" valign="top" width="19.23192319231923%" headers="mcps1.2.4.1.1 "><p id="p3903415185215"><a name="p3903415185215"></a><a name="p3903415185215"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.92179217921792%" headers="mcps1.2.4.1.2 "><p id="p390610159525"><a name="p390610159525"></a><a name="p390610159525"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.84628462846285%" headers="mcps1.2.4.1.3 "><p id="p4907191535213"><a name="p4907191535213"></a><a name="p4907191535213"></a>Specifies the API version status.</p>
    <a name="ul19909615185218"></a><a name="ul19909615185218"></a><ul id="ul19909615185218"><li><strong id="b19421137703"><a name="b19421137703"></a><a name="b19421137703"></a>CURRENT</strong>: indicates a primary version.</li><li><strong>SUPPORTED</strong>: indicates an earlier version which is still supported.</li><li><strong id="b1113314401707"><a name="b1113314401707"></a><a name="b1113314401707"></a>DEPRECATED</strong>: indicates a deprecated version which may be deleted later.</li></ul>
    </td>
    </tr>
    <tr id="row149151915105212"><td class="cellrowborder" valign="top" width="19.23192319231923%" headers="mcps1.2.4.1.1 "><p id="p4918715155215"><a name="p4918715155215"></a><a name="p4918715155215"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.92179217921792%" headers="mcps1.2.4.1.2 "><p id="p892011518520"><a name="p892011518520"></a><a name="p892011518520"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.84628462846285%" headers="mcps1.2.4.1.3 "><p id="p1255911034615"><a name="p1255911034615"></a><a name="p1255911034615"></a>Specifies the release date of an API version.</p>
    </td>
    </tr>
    <tr id="row17923151519525"><td class="cellrowborder" valign="top" width="19.23192319231923%" headers="mcps1.2.4.1.1 "><p id="p1892416155523"><a name="p1892416155523"></a><a name="p1892416155523"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.92179217921792%" headers="mcps1.2.4.1.2 "><p id="p16926191511523"><a name="p16926191511523"></a><a name="p16926191511523"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.84628462846285%" headers="mcps1.2.4.1.3 "><p id="p12928215185216"><a name="p12928215185216"></a><a name="p12928215185216"></a>Specifies the latest supported API version number.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **links**  field description

    <a name="t759e6d15d244474e8f286185ede143fb"></a>
    <table><thead align="left"><tr id="rce98b9668cd747c88039421afe5ce935"><th class="cellrowborder" valign="top" width="19.24%" id="mcps1.2.4.1.1"><p id="ad9ac3007570a4752b2b2dbc0fb04dadc"><a name="ad9ac3007570a4752b2b2dbc0fb04dadc"></a><a name="ad9ac3007570a4752b2b2dbc0fb04dadc"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.11%" id="mcps1.2.4.1.2"><p id="a602246198adf4a79a13bc4317d4c0d4f"><a name="a602246198adf4a79a13bc4317d4c0d4f"></a><a name="a602246198adf4a79a13bc4317d4c0d4f"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="62.64999999999999%" id="mcps1.2.4.1.3"><p id="a8cbfa8dcb0b943ff8e789755123fec83"><a name="a8cbfa8dcb0b943ff8e789755123fec83"></a><a name="a8cbfa8dcb0b943ff8e789755123fec83"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r43de461181294c56b28da56a1f604b09"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="abc19a41a8f594f1ba6701e10da50a078"><a name="abc19a41a8f594f1ba6701e10da50a078"></a><a name="abc19a41a8f594f1ba6701e10da50a078"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.11%" headers="mcps1.2.4.1.2 "><p id="a15ae7b8585d24e48abc6b9bf45636fda"><a name="a15ae7b8585d24e48abc6b9bf45636fda"></a><a name="a15ae7b8585d24e48abc6b9bf45636fda"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.64999999999999%" headers="mcps1.2.4.1.3 "><p id="p139393206480"><a name="p139393206480"></a><a name="p139393206480"></a>Specifies the API Uniform Resource Locator (URL).</p>
    </td>
    </tr>
    <tr id="rbd5ec7242fef4c03b21636ac14160d9e"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="a18479f6b70b34f29b2b90d754f59282a"><a name="a18479f6b70b34f29b2b90d754f59282a"></a><a name="a18479f6b70b34f29b2b90d754f59282a"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.11%" headers="mcps1.2.4.1.2 "><p id="ae1f14fa2e6a54531aeffd26874fea267"><a name="ae1f14fa2e6a54531aeffd26874fea267"></a><a name="ae1f14fa2e6a54531aeffd26874fea267"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.64999999999999%" headers="mcps1.2.4.1.3 "><p id="p115877381483"><a name="p115877381483"></a><a name="p115877381483"></a>Specifies the API URL dependency.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
      "version": {
        "id": "v1",
        "links": [
          {
            "href": "https://as.XXX.mycloud.com/autoscaling-api/v1/",
            "rel": "self"
          }
        ],
        "min_version": "",
        "status": "CURRENT",
        "updated": "2016-06-30T00:00:00Z",
        "version": ""
      }
    }
    ```


## Returned Values<a name="section15165719"></a>

-   Normal

    200

-   Abnormal

    <a name="table5908907"></a>
    <table><thead align="left"><tr id="row16065622"><th class="cellrowborder" valign="top" width="44.17%" id="mcps1.1.3.1.1"><p id="p26246992"><a name="p26246992"></a><a name="p26246992"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.83%" id="mcps1.1.3.1.2"><p id="p45631627"><a name="p45631627"></a><a name="p45631627"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5174319"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="p16466658"><a name="p16466658"></a><a name="p16466658"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="p58730959"><a name="p58730959"></a><a name="p58730959"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row58816586"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="p66523006"><a name="p66523006"></a><a name="p66523006"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="p19654399"><a name="p19654399"></a><a name="p19654399"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row42671863"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="p33868885"><a name="p33868885"></a><a name="p33868885"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="p59025204"><a name="p59025204"></a><a name="p59025204"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row61464796"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="p12592542"><a name="p12592542"></a><a name="p12592542"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="p13362997"><a name="p13362997"></a><a name="p13362997"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row53158116"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="p10840149"><a name="p10840149"></a><a name="p10840149"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="p5636878"><a name="p5636878"></a><a name="p5636878"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row50731910"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="p15644031"><a name="p15644031"></a><a name="p15644031"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="p59206997"><a name="p59206997"></a><a name="p59206997"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row63100926"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="p10901353"><a name="p10901353"></a><a name="p10901353"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="p10594405"><a name="p10594405"></a><a name="p10594405"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row28240785"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="p5802216"><a name="p5802216"></a><a name="p5802216"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="p217508"><a name="p217508"></a><a name="p217508"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row1957580"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="p24346266"><a name="p24346266"></a><a name="p24346266"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="p25890496"><a name="p25890496"></a><a name="p25890496"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row31687876"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="p16581154"><a name="p16581154"></a><a name="p16581154"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="p896237"><a name="p896237"></a><a name="p896237"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row8066134"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="p49377135"><a name="p49377135"></a><a name="p49377135"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="p40124968"><a name="p40124968"></a><a name="p40124968"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row25580392"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="p58745844"><a name="p58745844"></a><a name="p58745844"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="p60792949"><a name="p60792949"></a><a name="p60792949"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row10265637"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="p26210288"><a name="p26210288"></a><a name="p26210288"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="p42658596"><a name="p42658596"></a><a name="p42658596"></a>Failed to complete the request because the system is unavailable.</p>
    </td>
    </tr>
    <tr id="row48383044"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="p26712487"><a name="p26712487"></a><a name="p26712487"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="p16227847"><a name="p16227847"></a><a name="p16227847"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section17669131616110"></a>

See  [Error Codes](error-codes.md).

