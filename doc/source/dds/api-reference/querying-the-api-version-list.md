# Querying the API Version List<a name="dds_api_0018"></a>

## Function<a name="section9793815440"></a>

This API is used to query the currently supported API version list.

## URI<a name="section428804115440"></a>

-   URI format

    GET /

-   Parameter description

    N/A


## Requests<a name="section2907369315440"></a>

-   Request header

    ```
    GET https://DDS endpoint/
    ```

-   Request body

    N/A


## Responses<a name="section5543006115440"></a>

-   Parameter description

    **Table  1**  Parameter description

    <a name="table3575976715440"></a>
    <table><thead align="left"><tr id="row5028223115440"><th class="cellrowborder" valign="top" width="26.26262626262626%" id="mcps1.2.4.1.1"><p id="p4632888215440"><a name="p4632888215440"></a><a name="p4632888215440"></a><strong id="b842352706102328_3"><a name="b842352706102328_3"></a><a name="b842352706102328_3"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="40.40404040404041%" id="mcps1.2.4.1.2"><p id="p6165196615440"><a name="p6165196615440"></a><a name="p6165196615440"></a><strong id="b842352706164541_1"><a name="b842352706164541_1"></a><a name="b842352706164541_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p2775334615440"><a name="p2775334615440"></a><a name="p2775334615440"></a><strong id="b12381182592918"><a name="b12381182592918"></a><a name="b12381182592918"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3342858315440"><td class="cellrowborder" valign="top" width="26.26262626262626%" headers="mcps1.2.4.1.1 "><p id="p2336072515440"><a name="p2336072515440"></a><a name="p2336072515440"></a>versions</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.40404040404041%" headers="mcps1.2.4.1.2 "><p id="p94851531275"><a name="p94851531275"></a><a name="p94851531275"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p476126915440"><a name="p476126915440"></a><a name="p476126915440"></a>Indicates the list of detailed API version information. For more information, see <a href="#table37479565104653">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  versions field data structure description

    <a name="table37479565104653"></a>
    <table><thead align="left"><tr id="row65790814104653"><th class="cellrowborder" valign="top" width="26.529999999999998%" id="mcps1.2.4.1.1"><p id="p27455703104653"><a name="p27455703104653"></a><a name="p27455703104653"></a><strong id="b842352706102328_5"><a name="b842352706102328_5"></a><a name="b842352706102328_5"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="40.23%" id="mcps1.2.4.1.2"><p id="p9319469104653"><a name="p9319469104653"></a><a name="p9319469104653"></a><strong id="b842352706164541_3"><a name="b842352706164541_3"></a><a name="b842352706164541_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.239999999999995%" id="mcps1.2.4.1.3"><p id="p1143415283591"><a name="p1143415283591"></a><a name="p1143415283591"></a><strong id="b1453553216296"><a name="b1453553216296"></a><a name="b1453553216296"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8861837104653"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p46720233104653"><a name="p46720233104653"></a><a name="p46720233104653"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.23%" headers="mcps1.2.4.1.2 "><p id="p26242496104653"><a name="p26242496104653"></a><a name="p26242496104653"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p45267452104653"><a name="p45267452104653"></a><a name="p45267452104653"></a>Indicates the API version.</p>
    </td>
    </tr>
    <tr id="row1548795912115"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p26342211121111"><a name="p26342211121111"></a><a name="p26342211121111"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.23%" headers="mcps1.2.4.1.2 "><p id="p18625313281"><a name="p18625313281"></a><a name="p18625313281"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p31978734121111"><a name="p31978734121111"></a><a name="p31978734121111"></a>Indicates the API link information. For more information, see <a href="#table630875915440">Table 3</a>.</p>
    <div class="note" id="note1766615256328"><a name="note1766615256328"></a><a name="note1766615256328"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p566620258325"><a name="p566620258325"></a><a name="p566620258325"></a>If the version is <strong id="b180722435413"><a name="b180722435413"></a><a name="b180722435413"></a>v3</strong>, the value is <strong id="b7463134518547"><a name="b7463134518547"></a><a name="b7463134518547"></a>[]</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row4753892104653"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p49520946104653"><a name="p49520946104653"></a><a name="p49520946104653"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.23%" headers="mcps1.2.4.1.2 "><p id="p51773656104653"><a name="p51773656104653"></a><a name="p51773656104653"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p32916607104653"><a name="p32916607104653"></a><a name="p32916607104653"></a>Indicates the version status.</p>
    </td>
    </tr>
    <tr id="row1648012414408"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p154811524144020"><a name="p154811524144020"></a><a name="p154811524144020"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.23%" headers="mcps1.2.4.1.2 "><p id="p10856104114111"><a name="p10856104114111"></a><a name="p10856104114111"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p44820241403"><a name="p44820241403"></a><a name="p44820241403"></a>Indicates the subversion of the API version.</p>
    </td>
    </tr>
    <tr id="row050892716406"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p12508727124012"><a name="p12508727124012"></a><a name="p12508727124012"></a>min_version</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.23%" headers="mcps1.2.4.1.2 "><p id="p468916534116"><a name="p468916534116"></a><a name="p468916534116"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p050922734018"><a name="p050922734018"></a><a name="p050922734018"></a>Indicates the minimum API version.</p>
    </td>
    </tr>
    <tr id="row27814010104653"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p38342341104653"><a name="p38342341104653"></a><a name="p38342341104653"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.23%" headers="mcps1.2.4.1.2 "><p id="p18721892104653"><a name="p18721892104653"></a><a name="p18721892104653"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p40078272104653"><a name="p40078272104653"></a><a name="p40078272104653"></a>Indicates the version update time.</p>
    <p id="p25160128104653"><a name="p25160128104653"></a><a name="p25160128104653"></a>The format is yyyy-mm-ddThh:mm:ssZ.</p>
    <p id="p25114560104653"><a name="p25114560104653"></a><a name="p25114560104653"></a><strong id="b842352706104536"><a name="b842352706104536"></a><a name="b842352706104536"></a>T</strong> is the separator between the calendar and the hourly notation of time. <strong id="b842352706161738"><a name="b842352706161738"></a><a name="b842352706161738"></a>Z</strong> indicates the UTC.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  links field data structure description

    <a name="table630875915440"></a>
    <table><thead align="left"><tr id="row4191288815440"><th class="cellrowborder" valign="top" width="26.529999999999998%" id="mcps1.2.4.1.1"><p id="p3950073415440"><a name="p3950073415440"></a><a name="p3950073415440"></a><strong id="b842352706102328_7"><a name="b842352706102328_7"></a><a name="b842352706102328_7"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.800000000000004%" id="mcps1.2.4.1.2"><p id="p4544288515440"><a name="p4544288515440"></a><a name="p4544288515440"></a><strong id="b842352706164541_5"><a name="b842352706164541_5"></a><a name="b842352706164541_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.67%" id="mcps1.2.4.1.3"><p id="p2056123485910"><a name="p2056123485910"></a><a name="p2056123485910"></a><strong id="b7237133832914"><a name="b7237133832914"></a><a name="b7237133832914"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5319717215440"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p1400369315440"><a name="p1400369315440"></a><a name="p1400369315440"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.2 "><p id="p6055731815440"><a name="p6055731815440"></a><a name="p6055731815440"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.67%" headers="mcps1.2.4.1.3 "><p id="p619568715440"><a name="p619568715440"></a><a name="p619568715440"></a>Indicates the API URL and the value is <strong id="b84235270618633"><a name="b84235270618633"></a><a name="b84235270618633"></a>""</strong>.</p>
    </td>
    </tr>
    <tr id="row5576118615440"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p2036224315440"><a name="p2036224315440"></a><a name="p2036224315440"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.2 "><p id="p3872902515440"><a name="p3872902515440"></a><a name="p3872902515440"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.67%" headers="mcps1.2.4.1.3 "><p id="p5004333115440"><a name="p5004333115440"></a><a name="p5004333115440"></a>Its value is <strong id="b84235270616818"><a name="b84235270616818"></a><a name="b84235270616818"></a>self</strong>, indicating that URL is a local link.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    {
        "versions": [
            {
                "id": "v3",
                "links": [],
                "status": "CURRENT",
                "version": "",
                "min_version": "",
                "updated": "2017-02-07T17:34:02Z"
            }
        ]
    }
    ```


## **Status Code**<a name="section17992204432820"></a>

For more information, see  [Status Code](status-code.md).

## Error Code<a name="section6522193710339"></a>

For more information, see  [Error Code](error-code.md).

