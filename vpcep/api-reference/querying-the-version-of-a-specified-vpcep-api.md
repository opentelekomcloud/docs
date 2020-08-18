# Querying the Version of a Specified VPCEP API<a name="vpcep_06_0102"></a>

## Function<a name="section911804819271"></a>

This API is used to query the version of a specified VPCEP API.

## URI<a name="section8252172943111"></a>

GET /\{version\}

## Request<a name="section4451152618322"></a>

-   Parameters

    **Table  1**  Request parameters

    <a name="table5505175211710"></a>
    <table><thead align="left"><tr id="row1665510521073"><th class="cellrowborder" valign="top" width="27.347265273472654%" id="mcps1.2.5.1.1"><p id="p196553528716"><a name="p196553528716"></a><a name="p196553528716"></a><strong id="b33951224160"><a name="b33951224160"></a><a name="b33951224160"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.328267173282672%" id="mcps1.2.5.1.2"><p id="p565513525720"><a name="p565513525720"></a><a name="p565513525720"></a><strong id="b1267132351613"><a name="b1267132351613"></a><a name="b1267132351613"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26.547345265473453%" id="mcps1.2.5.1.3"><p id="p1565535214710"><a name="p1565535214710"></a><a name="p1565535214710"></a><strong id="b10886524131615"><a name="b10886524131615"></a><a name="b10886524131615"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.777122287771224%" id="mcps1.2.5.1.4"><p id="p14655165220712"><a name="p14655165220712"></a><a name="p14655165220712"></a><strong id="b414362671614"><a name="b414362671614"></a><a name="b414362671614"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row765515219718"><td class="cellrowborder" valign="top" width="27.347265273472654%" headers="mcps1.2.5.1.1 "><p id="p33593591418"><a name="p33593591418"></a><a name="p33593591418"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.328267173282672%" headers="mcps1.2.5.1.2 "><p id="p8359259143"><a name="p8359259143"></a><a name="p8359259143"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.547345265473453%" headers="mcps1.2.5.1.3 "><p id="p0655115210718"><a name="p0655115210718"></a><a name="p0655115210718"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.777122287771224%" headers="mcps1.2.5.1.4 "><p id="p202009491205"><a name="p202009491205"></a><a name="p202009491205"></a>Specifies the version to be queried. The value starts with v, for example, v1.</p>
    <p id="p7382592141"><a name="p7382592141"></a><a name="p7382592141"></a>If this parameter is left blank, versions of all APIs are queried.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    GET https://\{endpoint\}/v1


## Response<a name="section17102195273319"></a>

-   Parameters

    **Table  2**  Response parameters

    <a name="table173673267343"></a>
    <table><thead align="left"><tr id="row6419026173412"><th class="cellrowborder" valign="top" width="18.57%" id="mcps1.2.4.1.1"><p id="p6419426123416"><a name="p6419426123416"></a><a name="p6419426123416"></a><strong id="b7357165321617"><a name="b7357165321617"></a><a name="b7357165321617"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26.939999999999998%" id="mcps1.2.4.1.2"><p id="p841911268345"><a name="p841911268345"></a><a name="p841911268345"></a><strong id="b441915411167"><a name="b441915411167"></a><a name="b441915411167"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="54.49%" id="mcps1.2.4.1.3"><p id="p1241982643410"><a name="p1241982643410"></a><a name="p1241982643410"></a><strong id="b328911551164"><a name="b328911551164"></a><a name="b328911551164"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1841962613418"><td class="cellrowborder" valign="top" width="18.57%" headers="mcps1.2.4.1.1 "><p id="p184199268345"><a name="p184199268345"></a><a name="p184199268345"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p4419426193412"><a name="p4419426193412"></a><a name="p4419426193412"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.49%" headers="mcps1.2.4.1.3 "><p id="p1941992619345"><a name="p1941992619345"></a><a name="p1941992619345"></a>Lists the versions of VPCEP APIs. For details, see <a href="#table13687304356">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **VersionModel**  parameters

    <a name="table13687304356"></a>
    <table><thead align="left"><tr id="row1148330133514"><th class="cellrowborder" valign="top" width="18.62%" id="mcps1.2.4.1.1"><p id="p12148163012355"><a name="p12148163012355"></a><a name="p12148163012355"></a><strong id="b13156911151719"><a name="b13156911151719"></a><a name="b13156911151719"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.12%" id="mcps1.2.4.1.2"><p id="p21481930173516"><a name="p21481930173516"></a><a name="p21481930173516"></a><strong id="b17171171271719"><a name="b17171171271719"></a><a name="b17171171271719"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="54.26%" id="mcps1.2.4.1.3"><p id="p191487308357"><a name="p191487308357"></a><a name="p191487308357"></a><strong id="b5839111381714"><a name="b5839111381714"></a><a name="b5839111381714"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row13148730103514"><td class="cellrowborder" valign="top" width="18.62%" headers="mcps1.2.4.1.1 "><p id="p414873012353"><a name="p414873012353"></a><a name="p414873012353"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.12%" headers="mcps1.2.4.1.2 "><p id="p19148133018351"><a name="p19148133018351"></a><a name="p19148133018351"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.26%" headers="mcps1.2.4.1.3 "><p id="p15148130173519"><a name="p15148130173519"></a><a name="p15148130173519"></a>Specifies the version status.</p>
    <a name="ul12195132314920"></a><a name="ul12195132314920"></a><ul id="ul12195132314920"><li><strong id="b15854171891711"><a name="b15854171891711"></a><a name="b15854171891711"></a>CURRENT</strong>: indicates a major version.</li><li><strong id="b17262721151713"><a name="b17262721151713"></a><a name="b17262721151713"></a>SUPPORT</strong>: indicates an earlier version which is still supported.</li><li><strong id="b88408249179"><a name="b88408249179"></a><a name="b88408249179"></a>DEPRECATED</strong>: indicates a deprecated version that may be deleted later.</li></ul>
    </td>
    </tr>
    <tr id="row2148153033517"><td class="cellrowborder" valign="top" width="18.62%" headers="mcps1.2.4.1.1 "><p id="p814815307351"><a name="p814815307351"></a><a name="p814815307351"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.12%" headers="mcps1.2.4.1.2 "><p id="p181488307350"><a name="p181488307350"></a><a name="p181488307350"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.26%" headers="mcps1.2.4.1.3 "><p id="p214943013351"><a name="p214943013351"></a><a name="p214943013351"></a>Specifies the version ID.</p>
    </td>
    </tr>
    <tr id="row61491030163510"><td class="cellrowborder" valign="top" width="18.62%" headers="mcps1.2.4.1.1 "><p id="p0149143014358"><a name="p0149143014358"></a><a name="p0149143014358"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.12%" headers="mcps1.2.4.1.2 "><p id="p121491630183517"><a name="p121491630183517"></a><a name="p121491630183517"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.26%" headers="mcps1.2.4.1.3 "><p id="p4149830103515"><a name="p4149830103515"></a><a name="p4149830103515"></a>Specifies the time when the API version was released.</p>
    <p id="p871616113394"><a name="p871616113394"></a><a name="p871616113394"></a>The UTC time format is used: YYYY-MM-DDTHH:MM:SSZ.</p>
    </td>
    </tr>
    <tr id="row17149930163514"><td class="cellrowborder" valign="top" width="18.62%" headers="mcps1.2.4.1.1 "><p id="p514933013358"><a name="p514933013358"></a><a name="p514933013358"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.12%" headers="mcps1.2.4.1.2 "><p id="p914923015352"><a name="p914923015352"></a><a name="p914923015352"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.26%" headers="mcps1.2.4.1.3 "><p id="p214923015359"><a name="p214923015359"></a><a name="p214923015359"></a>Specifies the supported version. </p>
    </td>
    </tr>
    <tr id="row138921150194"><td class="cellrowborder" valign="top" width="18.62%" headers="mcps1.2.4.1.1 "><p id="p837715239193"><a name="p837715239193"></a><a name="p837715239193"></a>min_version</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.12%" headers="mcps1.2.4.1.2 "><p id="p193771823181917"><a name="p193771823181917"></a><a name="p193771823181917"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.26%" headers="mcps1.2.4.1.3 "><p id="p378134613518"><a name="p378134613518"></a><a name="p378134613518"></a>Specifies the microversion number. If the APIs do not support microversions, the value is left blank.</p>
    </td>
    </tr>
    <tr id="row101495301354"><td class="cellrowborder" valign="top" width="18.62%" headers="mcps1.2.4.1.1 "><p id="p18149173013518"><a name="p18149173013518"></a><a name="p18149173013518"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.12%" headers="mcps1.2.4.1.2 "><p id="p171493308352"><a name="p171493308352"></a><a name="p171493308352"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.26%" headers="mcps1.2.4.1.3 "><p id="p6149113014357"><a name="p6149113014357"></a><a name="p6149113014357"></a>Specifies the API URL. For details, see <a href="#table2072420713363">Table 4</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **VersionLink**  parameters

    <a name="table2072420713363"></a>
    <table><thead align="left"><tr id="row1879514712367"><th class="cellrowborder" valign="top" width="18.67%" id="mcps1.2.4.1.1"><p id="p6795975366"><a name="p6795975366"></a><a name="p6795975366"></a><strong id="b2464165541711"><a name="b2464165541711"></a><a name="b2464165541711"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.04%" id="mcps1.2.4.1.2"><p id="p9795127193619"><a name="p9795127193619"></a><a name="p9795127193619"></a><strong id="b18795145614170"><a name="b18795145614170"></a><a name="b18795145614170"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="54.290000000000006%" id="mcps1.2.4.1.3"><p id="p147955719369"><a name="p147955719369"></a><a name="p147955719369"></a><strong id="b146291157141716"><a name="b146291157141716"></a><a name="b146291157141716"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row187958715368"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="p197951713612"><a name="p197951713612"></a><a name="p197951713612"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.04%" headers="mcps1.2.4.1.2 "><p id="p197951874369"><a name="p197951874369"></a><a name="p197951874369"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.290000000000006%" headers="mcps1.2.4.1.3 "><p id="p779520783617"><a name="p779520783617"></a><a name="p779520783617"></a>Specifies the reference address of the current API version.</p>
    </td>
    </tr>
    <tr id="row879514763612"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="p107951710363"><a name="p107951710363"></a><a name="p107951710363"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.04%" headers="mcps1.2.4.1.2 "><p id="p10795472366"><a name="p10795472366"></a><a name="p10795472366"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.290000000000006%" headers="mcps1.2.4.1.3 "><p id="p5712332143113"><a name="p5712332143113"></a><a name="p5712332143113"></a>Specifies the MIME type of the entity sending the request. The value is <strong id="b977375111820"><a name="b977375111820"></a><a name="b977375111820"></a>application/json</strong>.</p>
    </td>
    </tr>
    <tr id="row079519743614"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="p117951723611"><a name="p117951723611"></a><a name="p117951723611"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.04%" headers="mcps1.2.4.1.2 "><p id="p979557123615"><a name="p979557123615"></a><a name="p979557123615"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.290000000000006%" headers="mcps1.2.4.1.3 "><p id="p1179513753617"><a name="p1179513753617"></a><a name="p1179513753617"></a>Specifies the relationship between the current API version and the referenced address.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
      "version":{
        {
          "updated":"2018-09-30T00:00:00Z",
          "version":"1",
          "min_version":"",
          "status":"CURRENT",
          "id":"v1",
          "links":[
            {
              "href":"https://{vpcep_uri}/v1",
              "type":"application/json",
              "rel":"self"
            }
          ]
        }
      }
    }
    ```


## Status Code<a name="section88561438153717"></a>

For details about status codes, see  [Status Code](status-code.md).

