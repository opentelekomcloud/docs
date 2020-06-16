# Querying Details About a Specified TMS API Version<a name="EN-US_TOPIC_0170553615"></a>

## Function<a name="section112333415306"></a>

This API is used to query the details of a specified TMS API version.

## URI<a name="section9128153473016"></a>

GET /\{api\_version\}

## Request<a name="section32381034103013"></a>

-   Parameter description

    **Table  1**  Parameters in the request

    <a name="table12569102910"></a>
    <table><thead align="left"><tr id="row863915010914"><th class="cellrowborder" valign="top" width="21.43%" id="mcps1.2.5.1.1"><p id="p86399015915"><a name="p86399015915"></a><a name="p86399015915"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="10.2%" id="mcps1.2.5.1.2"><p id="p15639401794"><a name="p15639401794"></a><a name="p15639401794"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="28.57%" id="mcps1.2.5.1.3"><p id="p363930296"><a name="p363930296"></a><a name="p363930296"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="39.800000000000004%" id="mcps1.2.5.1.4"><p id="p2640101992"><a name="p2640101992"></a><a name="p2640101992"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1864013012915"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.5.1.1 "><p id="p1364000890"><a name="p1364000890"></a><a name="p1364000890"></a>api_version</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.2%" headers="mcps1.2.5.1.2 "><p id="p146400018913"><a name="p146400018913"></a><a name="p146400018913"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.2.5.1.3 "><p id="p9640601896"><a name="p9640601896"></a><a name="p9640601896"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.5.1.4 "><p id="p1464011017920"><a name="p1464011017920"></a><a name="p1464011017920"></a>Specifies the API version.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    GET https://{TMS endpoint}/v1.0
    ```


## Response<a name="section17252434193018"></a>

-   Parameter description

    **Table  2**  Parameters in the response

    <a name="table638373419305"></a>
    <table><thead align="left"><tr id="row163831536143019"><th class="cellrowborder" valign="top" width="24.83%" id="mcps1.2.4.1.1"><p id="p1738363612307"><a name="p1738363612307"></a><a name="p1738363612307"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="29.65%" id="mcps1.2.4.1.2"><p id="p4383136193010"><a name="p4383136193010"></a><a name="p4383136193010"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.519999999999996%" id="mcps1.2.4.1.3"><p id="p153838362301"><a name="p153838362301"></a><a name="p153838362301"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row163832366304"><td class="cellrowborder" valign="top" width="24.83%" headers="mcps1.2.4.1.1 "><p id="p3383133610301"><a name="p3383133610301"></a><a name="p3383133610301"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.65%" headers="mcps1.2.4.1.2 "><p id="p2383133616305"><a name="p2383133616305"></a><a name="p2383133616305"></a>object</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.519999999999996%" headers="mcps1.2.4.1.3 "><p id="p1238343618301"><a name="p1238343618301"></a><a name="p1238343618301"></a>Specifies the version of a specified API.</p>
    <p id="p041917181204"><a name="p041917181204"></a><a name="p041917181204"></a>For details, see <a href="#table7480934143011">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   **version**  field data structure

    **Table  3** **version**  field data structure description

    <a name="table7480934143011"></a>
    <table><thead align="left"><tr id="row5383153610309"><th class="cellrowborder" valign="top" width="18.688131186881314%" id="mcps1.2.4.1.1"><p id="p2384153663010"><a name="p2384153663010"></a><a name="p2384153663010"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.077792220777923%" id="mcps1.2.4.1.2"><p id="p8384203618302"><a name="p8384203618302"></a><a name="p8384203618302"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="59.23407659234077%" id="mcps1.2.4.1.3"><p id="p17384123612304"><a name="p17384123612304"></a><a name="p17384123612304"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row838413616301"><td class="cellrowborder" valign="top" width="18.688131186881314%" headers="mcps1.2.4.1.1 "><p id="p638463613305"><a name="p638463613305"></a><a name="p638463613305"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.077792220777923%" headers="mcps1.2.4.1.2 "><p id="p43841036173017"><a name="p43841036173017"></a><a name="p43841036173017"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.23407659234077%" headers="mcps1.2.4.1.3 "><p id="p153844368307"><a name="p153844368307"></a><a name="p153844368307"></a>Specifies the version ID, for example, v1.0.</p>
    </td>
    </tr>
    <tr id="row143841136183018"><td class="cellrowborder" valign="top" width="18.688131186881314%" headers="mcps1.2.4.1.1 "><p id="p2038423643018"><a name="p2038423643018"></a><a name="p2038423643018"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.077792220777923%" headers="mcps1.2.4.1.2 "><p id="p2384736163019"><a name="p2384736163019"></a><a name="p2384736163019"></a>List&lt;Link&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.23407659234077%" headers="mcps1.2.4.1.3 "><p id="p8384123653010"><a name="p8384123653010"></a><a name="p8384123653010"></a>Specifies the API URL.</p>
    <p id="p149851402025"><a name="p149851402025"></a><a name="p149851402025"></a>For details, see <a href="#table86914347304">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="row14384173643012"><td class="cellrowborder" valign="top" width="18.688131186881314%" headers="mcps1.2.4.1.1 "><p id="p8384153619301"><a name="p8384153619301"></a><a name="p8384153619301"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.077792220777923%" headers="mcps1.2.4.1.2 "><p id="p8384133683015"><a name="p8384133683015"></a><a name="p8384133683015"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.23407659234077%" headers="mcps1.2.4.1.3 "><p id="p113841236183014"><a name="p113841236183014"></a><a name="p113841236183014"></a>If the APIs of this version support microversions, set this parameter to the supported latest microversion. If not, leave this parameter blank.</p>
    </td>
    </tr>
    <tr id="row1138415367307"><td class="cellrowborder" valign="top" width="18.688131186881314%" headers="mcps1.2.4.1.1 "><p id="p20385143614301"><a name="p20385143614301"></a><a name="p20385143614301"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.077792220777923%" headers="mcps1.2.4.1.2 "><p id="p123851236133011"><a name="p123851236133011"></a><a name="p123851236133011"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.23407659234077%" headers="mcps1.2.4.1.3 "><p id="p41220831142214"><a name="p41220831142214"></a><a name="p41220831142214"></a>Specifies the version status.</p>
    <p id="p43374538142233"><a name="p43374538142233"></a><a name="p43374538142233"></a>Possible values are as follows:</p>
    <a name="ul012713412324"></a><a name="ul012713412324"></a><ul id="ul012713412324"><li><strong id="b842352706192132"><a name="b842352706192132"></a><a name="b842352706192132"></a>CURRENT</strong>: indicates that the version is the primary version.</li><li><strong id="b842352706192150"><a name="b842352706192150"></a><a name="b842352706192150"></a>SUPPORTED</strong>: indicates that the version is an old version, but it is still supported.</li><li><strong>DEPRECATED</strong>: indicates a deprecated version which may be deleted later.</li></ul>
    </td>
    </tr>
    <tr id="row038814361309"><td class="cellrowborder" valign="top" width="18.688131186881314%" headers="mcps1.2.4.1.1 "><p id="p8388133673018"><a name="p8388133673018"></a><a name="p8388133673018"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.077792220777923%" headers="mcps1.2.4.1.2 "><p id="p123891236183012"><a name="p123891236183012"></a><a name="p123891236183012"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.23407659234077%" headers="mcps1.2.4.1.3 "><p id="p1938918364303"><a name="p1938918364303"></a><a name="p1938918364303"></a>Specifies the version release time, which must be the UTC time. For example, the release time of TMS 1.0 is 2016-12-09T00:00:00Z.</p>
    </td>
    </tr>
    <tr id="row1638943618309"><td class="cellrowborder" valign="top" width="18.688131186881314%" headers="mcps1.2.4.1.1 "><p id="p63894367302"><a name="p63894367302"></a><a name="p63894367302"></a>min_version</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.077792220777923%" headers="mcps1.2.4.1.2 "><p id="p1738912361308"><a name="p1738912361308"></a><a name="p1738912361308"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.23407659234077%" headers="mcps1.2.4.1.3 "><p id="p638963653019"><a name="p638963653019"></a><a name="p638963653019"></a>If the APIs of this version support microversions, set this parameter to the supported earliest microversion. If not, leave this parameter blank.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   **Links**  field data structure

    **Table  4** **Links**  field data structure description

    <a name="table86914347304"></a>
    <table><thead align="left"><tr id="row53898368307"><th class="cellrowborder" valign="top" width="20.79%" id="mcps1.2.4.1.1"><p id="p13895362301"><a name="p13895362301"></a><a name="p13895362301"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="33%" id="mcps1.2.4.1.2"><p id="p438913365302"><a name="p438913365302"></a><a name="p438913365302"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.21%" id="mcps1.2.4.1.3"><p id="p6389143683018"><a name="p6389143683018"></a><a name="p6389143683018"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8389103623010"><td class="cellrowborder" valign="top" width="20.79%" headers="mcps1.2.4.1.1 "><p id="p7389436193014"><a name="p7389436193014"></a><a name="p7389436193014"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.2 "><p id="p73891236123010"><a name="p73891236123010"></a><a name="p73891236123010"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.2.4.1.3 "><p id="p5389536123014"><a name="p5389536123014"></a><a name="p5389536123014"></a>Specifies the API URL.</p>
    </td>
    </tr>
    <tr id="row6389163653017"><td class="cellrowborder" valign="top" width="20.79%" headers="mcps1.2.4.1.1 "><p id="p63891036163012"><a name="p63891036163012"></a><a name="p63891036163012"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.2 "><p id="p13389133693017"><a name="p13389133693017"></a><a name="p13389133693017"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.2.4.1.3 "><p id="p03899362303"><a name="p03899362303"></a><a name="p03899362303"></a>self</p>
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
                    "rel": "self",
                   "href": "https://API URL/v1.0"
                }
            ],
            "version": "",
            "status": "CURRENT",
            "updated": "2016-12-09T00:00:00Z",
            "min_version": ""
        }
    }
    ```


## Status Codes<a name="section17789101582315"></a>

For details, see  [Status Code](status-code.md).

## Error Codes<a name="section18604165622519"></a>

For details, see  [Error Code Description](error-code-description.md).

