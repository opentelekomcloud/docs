# Querying an API Version<a name="EN-US_TOPIC_0133576327"></a>

## Function<a name="section54478915181842"></a>

This API is used to query a specified API version.

## URI<a name="section53791107181842"></a>

GET /\{api\_version\}

[Table 1](#table46110007)  describes the parameters.

**Table  1**  Parameters description

<a name="table46110007"></a>
<table><thead align="left"><tr id="row14148614"><th class="cellrowborder" valign="top" width="20.74%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a><strong id="b114121766204"><a name="b114121766204"></a><a name="b114121766204"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19.99%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a><strong id="b15192157132016"><a name="b15192157132016"></a><a name="b15192157132016"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="59.27%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a><strong id="b29120892011"><a name="b29120892011"></a><a name="b29120892011"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row17201924"><td class="cellrowborder" valign="top" width="20.74%" headers="mcps1.2.4.1.1 "><p id="p51178607"><a name="p51178607"></a><a name="p51178607"></a>api_version</p>
</td>
<td class="cellrowborder" valign="top" width="19.99%" headers="mcps1.2.4.1.2 "><p id="p51826478"><a name="p51826478"></a><a name="p51826478"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="59.27%" headers="mcps1.2.4.1.3 "><p id="p37195178"><a name="p37195178"></a><a name="p37195178"></a>Specifies the API version, for example, v1.0.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section15830195355312"></a>

-   Request parameters

    None

-   Example request

    ```
    GET /v1.0
    ```


## Response<a name="section12542181845412"></a>

-   Response parameters

    <a name="table16998288231"></a>
    <table><thead align="left"><tr id="row2104142816233"><th class="cellrowborder" valign="top" width="23.332333233323332%" id="mcps1.1.4.1.1"><p id="p1310662813237"><a name="p1310662813237"></a><a name="p1310662813237"></a><strong id="b15107145172014"><a name="b15107145172014"></a><a name="b15107145172014"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26.002600260026004%" id="mcps1.1.4.1.2"><p id="p0108202812239"><a name="p0108202812239"></a><a name="p0108202812239"></a><strong id="b18471115222014"><a name="b18471115222014"></a><a name="b18471115222014"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.66506650665067%" id="mcps1.1.4.1.3"><p id="p111002818232"><a name="p111002818232"></a><a name="p111002818232"></a><strong id="b1242615510205"><a name="b1242615510205"></a><a name="b1242615510205"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row141111428152316"><td class="cellrowborder" valign="top" width="23.332333233323332%" headers="mcps1.1.4.1.1 "><p id="p10113152813235"><a name="p10113152813235"></a><a name="p10113152813235"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.002600260026004%" headers="mcps1.1.4.1.2 "><p id="p4114228122310"><a name="p4114228122310"></a><a name="p4114228122310"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.66506650665067%" headers="mcps1.1.4.1.3 "><p id="p1118182852311"><a name="p1118182852311"></a><a name="p1118182852311"></a>Specifies information about a specified API version.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **version**  field description

    <a name="table1838124772311"></a>
    <table><thead align="left"><tr id="row4841347112318"><th class="cellrowborder" valign="top" width="23.44%" id="mcps1.1.4.1.1"><p id="p191191836202612"><a name="p191191836202612"></a><a name="p191191836202612"></a><strong id="b81808549239"><a name="b81808549239"></a><a name="b81808549239"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26.11%" id="mcps1.1.4.1.2"><p id="p9120153642612"><a name="p9120153642612"></a><a name="p9120153642612"></a><strong id="b1146885616235"><a name="b1146885616235"></a><a name="b1146885616235"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.449999999999996%" id="mcps1.1.4.1.3"><p id="p121212368264"><a name="p121212368264"></a><a name="p121212368264"></a><strong id="b183701457182312"><a name="b183701457182312"></a><a name="b183701457182312"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15845104718237"><td class="cellrowborder" valign="top" width="23.44%" headers="mcps1.1.4.1.1 "><p id="p138462047112319"><a name="p138462047112319"></a><a name="p138462047112319"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.11%" headers="mcps1.1.4.1.2 "><p id="p1584774762320"><a name="p1584774762320"></a><a name="p1584774762320"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.449999999999996%" headers="mcps1.1.4.1.3 "><p id="p38481947132315"><a name="p38481947132315"></a><a name="p38481947132315"></a>Specifies the ID of the API version.</p>
    </td>
    </tr>
    <tr id="row2084912474237"><td class="cellrowborder" valign="top" width="23.44%" headers="mcps1.1.4.1.1 "><p id="p1850104742317"><a name="p1850104742317"></a><a name="p1850104742317"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.11%" headers="mcps1.1.4.1.2 "><p id="p1185174712238"><a name="p1185174712238"></a><a name="p1185174712238"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.449999999999996%" headers="mcps1.1.4.1.3 "><p id="p16853154711236"><a name="p16853154711236"></a><a name="p16853154711236"></a>Specifies the URL of the API version.</p>
    </td>
    </tr>
    <tr id="row98531947192314"><td class="cellrowborder" valign="top" width="23.44%" headers="mcps1.1.4.1.1 "><p id="p108551547142313"><a name="p108551547142313"></a><a name="p108551547142313"></a>min_version</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.11%" headers="mcps1.1.4.1.2 "><p id="p8857947122310"><a name="p8857947122310"></a><a name="p8857947122310"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.449999999999996%" headers="mcps1.1.4.1.3 "><p id="p98584476239"><a name="p98584476239"></a><a name="p98584476239"></a>Specifies the microversion. If the APIs of this version support microversions, set this parameter to the supported minimum microversion. If the microversion is not supported, leave this parameter blank.</p>
    </td>
    </tr>
    <tr id="row98627474234"><td class="cellrowborder" valign="top" width="23.44%" headers="mcps1.1.4.1.1 "><p id="p19862047192316"><a name="p19862047192316"></a><a name="p19862047192316"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.11%" headers="mcps1.1.4.1.2 "><p id="p1986344742313"><a name="p1986344742313"></a><a name="p1986344742313"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.449999999999996%" headers="mcps1.1.4.1.3 "><p id="p19864147172319"><a name="p19864147172319"></a><a name="p19864147172319"></a>Specifies the API version status.</p>
    <a name="ul158667479233"></a><a name="ul158667479233"></a><ul id="ul158667479233"><li><strong id="b8172322417"><a name="b8172322417"></a><a name="b8172322417"></a>CURRENT</strong>: indicates a primary version.</li><li><strong id="b9516142419245"><a name="b9516142419245"></a><a name="b9516142419245"></a>SUPPORTED</strong>: indicates an earlier version which is still supported.</li><li><strong id="b1889752617249"><a name="b1889752617249"></a><a name="b1889752617249"></a>DEPRECATED</strong>: indicates a deprecated version which may be deleted later.</li></ul>
    </td>
    </tr>
    <tr id="row1086915473231"><td class="cellrowborder" valign="top" width="23.44%" headers="mcps1.1.4.1.1 "><p id="p487004712236"><a name="p487004712236"></a><a name="p487004712236"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.11%" headers="mcps1.1.4.1.2 "><p id="p1287294715230"><a name="p1287294715230"></a><a name="p1287294715230"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.449999999999996%" headers="mcps1.1.4.1.3 "><p id="p2873647152314"><a name="p2873647152314"></a><a name="p2873647152314"></a>Specifies the API version update time.</p>
    </td>
    </tr>
    <tr id="row1987416479234"><td class="cellrowborder" valign="top" width="23.44%" headers="mcps1.1.4.1.1 "><p id="p8876194718236"><a name="p8876194718236"></a><a name="p8876194718236"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.11%" headers="mcps1.1.4.1.2 "><p id="p287913471236"><a name="p287913471236"></a><a name="p287913471236"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.449999999999996%" headers="mcps1.1.4.1.3 "><p id="p4879114712310"><a name="p4879114712310"></a><a name="p4879114712310"></a>Specifies the API version. If the APIs of this version support microversions, set this parameter to the supported minimum microversion. If the microversion is not supported, leave this parameter blank.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **links**  field description

    <a name="table1318657102611"></a>
    <table><thead align="left"><tr id="row31901475268"><th class="cellrowborder" valign="top" width="23.669999999999998%" id="mcps1.1.4.1.1"><p id="p5117113922619"><a name="p5117113922619"></a><a name="p5117113922619"></a><strong id="b1273811533244"><a name="b1273811533244"></a><a name="b1273811533244"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26.11%" id="mcps1.1.4.1.2"><p id="p31185397262"><a name="p31185397262"></a><a name="p31185397262"></a><strong id="b337919553249"><a name="b337919553249"></a><a name="b337919553249"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.22%" id="mcps1.1.4.1.3"><p id="p311915395267"><a name="p311915395267"></a><a name="p311915395267"></a><strong id="b158175782413"><a name="b158175782413"></a><a name="b158175782413"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row51960714268"><td class="cellrowborder" valign="top" width="23.669999999999998%" headers="mcps1.1.4.1.1 "><p id="p1219827192613"><a name="p1219827192613"></a><a name="p1219827192613"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.11%" headers="mcps1.1.4.1.2 "><p id="p22011275263"><a name="p22011275263"></a><a name="p22011275263"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.22%" headers="mcps1.1.4.1.3 "><p id="p1620414742615"><a name="p1620414742615"></a><a name="p1620414742615"></a>Specifies the URL of the API version.</p>
    </td>
    </tr>
    <tr id="row92068702616"><td class="cellrowborder" valign="top" width="23.669999999999998%" headers="mcps1.1.4.1.1 "><p id="p19206147182612"><a name="p19206147182612"></a><a name="p19206147182612"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.11%" headers="mcps1.1.4.1.2 "><p id="p1220827172620"><a name="p1220827172620"></a><a name="p1220827172620"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.22%" headers="mcps1.1.4.1.3 "><p id="p120913711267"><a name="p120913711267"></a><a name="p120913711267"></a>Specifies the API URL dependency.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "version": {
            "id": "v1.0",
            "links": [
                {
                    "href": "https//deh.xxx.com/v1.0/",
                    "rel": "self"
                }
            ],
            "min_version": "",
            "status": "SUPPORTED",
            "updated": "2016-12-01T11:33:21Z",
            "version": ""
        }
    }
    ```


## Status Code<a name="section9992350"></a>

See  [Status Codes](status-codes.md).

