# Querying Versions of VPCEP APIs<a name="vpcep_06_0101"></a>

## Function<a name="section911804819271"></a>

This API is used to query versions of VPCEP APIs.

## URI<a name="section8252172943111"></a>

GET /

## Request<a name="section4451152618322"></a>

-   Example request

    GET https://\{endpoint\}/


## Response<a name="section17102195273319"></a>

-   Parameters

    **Table  1**  Response parameters

    <a name="table173673267343"></a>
    <table><thead align="left"><tr id="row6419026173412"><th class="cellrowborder" valign="top" width="24.240000000000002%" id="mcps1.2.4.1.1"><p id="p6419426123416"><a name="p6419426123416"></a><a name="p6419426123416"></a><strong id="b79351534181412"><a name="b79351534181412"></a><a name="b79351534181412"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.25%" id="mcps1.2.4.1.2"><p id="p841911268345"><a name="p841911268345"></a><a name="p841911268345"></a><strong id="b391323541416"><a name="b391323541416"></a><a name="b391323541416"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.51%" id="mcps1.2.4.1.3"><p id="p1241982643410"><a name="p1241982643410"></a><a name="p1241982643410"></a><strong id="b18898113610143"><a name="b18898113610143"></a><a name="b18898113610143"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1841962613418"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.1 "><p id="p184199268345"><a name="p184199268345"></a><a name="p184199268345"></a>versions</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p4419426193412"><a name="p4419426193412"></a><a name="p4419426193412"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.51%" headers="mcps1.2.4.1.3 "><p id="p1941992619345"><a name="p1941992619345"></a><a name="p1941992619345"></a>Lists the versions of VPCEP APIs. For details, see <a href="#table13687304356">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2** **VersionModel**  parameters

    <a name="table13687304356"></a>
    <table><thead align="left"><tr id="row1148330133514"><th class="cellrowborder" valign="top" width="18.62%" id="mcps1.2.4.1.1"><p id="p12148163012355"><a name="p12148163012355"></a><a name="p12148163012355"></a><strong id="b5941859181415"><a name="b5941859181415"></a><a name="b5941859181415"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.12%" id="mcps1.2.4.1.2"><p id="p21481930173516"><a name="p21481930173516"></a><a name="p21481930173516"></a><strong id="b14023511169"><a name="b14023511169"></a><a name="b14023511169"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="54.26%" id="mcps1.2.4.1.3"><p id="p191487308357"><a name="p191487308357"></a><a name="p191487308357"></a><strong id="b199114616165"><a name="b199114616165"></a><a name="b199114616165"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row13148730103514"><td class="cellrowborder" valign="top" width="18.62%" headers="mcps1.2.4.1.1 "><p id="p414873012353"><a name="p414873012353"></a><a name="p414873012353"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.12%" headers="mcps1.2.4.1.2 "><p id="p19148133018351"><a name="p19148133018351"></a><a name="p19148133018351"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.26%" headers="mcps1.2.4.1.3 "><p id="p15148130173519"><a name="p15148130173519"></a><a name="p15148130173519"></a>Specifies the version status.</p>
    <a name="ul12195132314920"></a><a name="ul12195132314920"></a><ul id="ul12195132314920"><li><strong id="b345764344013"><a name="b345764344013"></a><a name="b345764344013"></a>CURRENT</strong>: indicates a major version.</li><li><strong id="b842352706115419"><a name="b842352706115419"></a><a name="b842352706115419"></a>SUPPORT</strong>: indicates an earlier version which is still supported.</li><li><strong id="b11835470403"><a name="b11835470403"></a><a name="b11835470403"></a>DEPRECATED</strong>: indicates a deprecated version that may be deleted later.</li></ul>
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
    <td class="cellrowborder" valign="top" width="54.26%" headers="mcps1.2.4.1.3 "><p id="p6149113014357"><a name="p6149113014357"></a><a name="p6149113014357"></a>Specifies the API URL. For details, see <a href="#table2072420713363">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **VersionLink**  parameters

    <a name="table2072420713363"></a>
    <table><thead align="left"><tr id="row1879514712367"><th class="cellrowborder" valign="top" width="18.67%" id="mcps1.2.4.1.1"><p id="p6795975366"><a name="p6795975366"></a><a name="p6795975366"></a><strong id="b282411211183"><a name="b282411211183"></a><a name="b282411211183"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.04%" id="mcps1.2.4.1.2"><p id="p9795127193619"><a name="p9795127193619"></a><a name="p9795127193619"></a><strong id="b73128148187"><a name="b73128148187"></a><a name="b73128148187"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="54.290000000000006%" id="mcps1.2.4.1.3"><p id="p147955719369"><a name="p147955719369"></a><a name="p147955719369"></a><strong id="b1448217851810"><a name="b1448217851810"></a><a name="b1448217851810"></a>Description</strong></p>
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
    <td class="cellrowborder" valign="top" width="54.290000000000006%" headers="mcps1.2.4.1.3 "><p id="p5712332143113"><a name="p5712332143113"></a><a name="p5712332143113"></a>Specifies the MIME type of the entity sending the request. The value is <strong id="b1842810364613"><a name="b1842810364613"></a><a name="b1842810364613"></a>application/json</strong>.</p>
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
      "versions":[
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
      ]
    }
    ```


## Status Code<a name="section88561438153717"></a>

For details about status codes, see  [Status Code](/vpcep/api-reference/common/status-code.md).

