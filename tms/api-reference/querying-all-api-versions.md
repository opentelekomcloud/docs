# Querying All API Versions<a name="EN-US_TOPIC_0170553657"></a>

## Function<a name="section18687215132319"></a>

This API is used to query the versions of all TMS APIs.

## URI<a name="section6695141502313"></a>

GET /

## Request<a name="section147311515172315"></a>

Example request

```
GET https://{TMS endpoint}/
```

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>Domain-level tokens are required for invoking APIs of TMS services. For details, see  [Obtaining the Domain-Level Token](obtaining-the-domain-level-token.md).  

## Response<a name="section11732141562320"></a>

-   Parameter description

    **Table  1**  Parameters in the response

    <a name="table17740171518233"></a>
    <table><thead align="left"><tr id="row8871619238"><th class="cellrowborder" valign="top" width="19.848015198480155%" id="mcps1.2.4.1.1"><p id="p28141692310"><a name="p28141692310"></a><a name="p28141692310"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.44765523447655%" id="mcps1.2.4.1.2"><p id="p18416152317"><a name="p18416152317"></a><a name="p18416152317"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.7043295670433%" id="mcps1.2.4.1.3"><p id="p28171614232"><a name="p28171614232"></a><a name="p28171614232"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row108191642320"><td class="cellrowborder" valign="top" width="19.848015198480155%" headers="mcps1.2.4.1.1 "><p id="p88111614232"><a name="p88111614232"></a><a name="p88111614232"></a>versions</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.44765523447655%" headers="mcps1.2.4.1.2 "><p id="p28141622314"><a name="p28141622314"></a><a name="p28141622314"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.7043295670433%" headers="mcps1.2.4.1.3 "><p id="p4873152115617"><a name="p4873152115617"></a><a name="p4873152115617"></a>Specifies all API versions.</p>
    <p id="p68101682312"><a name="p68101682312"></a><a name="p68101682312"></a>For details, see <a href="#table374991515234">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   **versions**  field data structure

    **Table  2** **versions**  field data structure description

    <a name="table374991515234"></a>
    <table><thead align="left"><tr id="row68201612320"><th class="cellrowborder" valign="top" width="18.87%" id="mcps1.2.4.1.1"><p id="p281616202313"><a name="p281616202313"></a><a name="p281616202313"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.33%" id="mcps1.2.4.1.2"><p id="p15819166237"><a name="p15819166237"></a><a name="p15819166237"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="59.8%" id="mcps1.2.4.1.3"><p id="p15861642317"><a name="p15861642317"></a><a name="p15861642317"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row19861612232"><td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.2.4.1.1 "><p id="p9819160233"><a name="p9819160233"></a><a name="p9819160233"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.33%" headers="mcps1.2.4.1.2 "><p id="p38121612234"><a name="p38121612234"></a><a name="p38121612234"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.8%" headers="mcps1.2.4.1.3 "><p id="p109181619236"><a name="p109181619236"></a><a name="p109181619236"></a>Specifies the version ID, for example, v1.0.</p>
    </td>
    </tr>
    <tr id="row1991916122316"><td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.2.4.1.1 "><p id="p790163234"><a name="p790163234"></a><a name="p790163234"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.33%" headers="mcps1.2.4.1.2 "><p id="p6991642317"><a name="p6991642317"></a><a name="p6991642317"></a>List&lt;Link&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.8%" headers="mcps1.2.4.1.3 "><p id="p15951611231"><a name="p15951611231"></a><a name="p15951611231"></a>Specifies the API URL.</p>
    <p id="p64911367576"><a name="p64911367576"></a><a name="p64911367576"></a>For details, see <a href="#table87796151239">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row16911161237"><td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.2.4.1.1 "><p id="p209216142319"><a name="p209216142319"></a><a name="p209216142319"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.33%" headers="mcps1.2.4.1.2 "><p id="p4931615232"><a name="p4931615232"></a><a name="p4931615232"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.8%" headers="mcps1.2.4.1.3 "><p id="p59616142317"><a name="p59616142317"></a><a name="p59616142317"></a>If the APIs of this version support microversions, set this parameter to the supported latest microversion. If not, leave this parameter blank.</p>
    </td>
    </tr>
    <tr id="row179131652313"><td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.2.4.1.1 "><p id="p5981613232"><a name="p5981613232"></a><a name="p5981613232"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.33%" headers="mcps1.2.4.1.2 "><p id="p1195169236"><a name="p1195169236"></a><a name="p1195169236"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.8%" headers="mcps1.2.4.1.3 "><p id="p5352627314210"><a name="p5352627314210"></a><a name="p5352627314210"></a>Specifies the version status.</p>
    <p id="p29448333142119"><a name="p29448333142119"></a><a name="p29448333142119"></a>Possible values are as follows:</p>
    <a name="ul101632012202419"></a><a name="ul101632012202419"></a><ul id="ul101632012202419"><li><strong id="b842352706192132"><a name="b842352706192132"></a><a name="b842352706192132"></a>CURRENT</strong>: indicates that the version is the primary version.</li><li><strong id="b842352706192150"><a name="b842352706192150"></a><a name="b842352706192150"></a>SUPPORTED</strong>: indicates that the version is an old version, but it is still supported.</li><li><strong id="b8542212327"><a name="b8542212327"></a><a name="b8542212327"></a>DEPRECATED</strong>: indicates a deprecated version which may be deleted later.</li></ul>
    </td>
    </tr>
    <tr id="row2931611231"><td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.2.4.1.1 "><p id="p129101614238"><a name="p129101614238"></a><a name="p129101614238"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.33%" headers="mcps1.2.4.1.2 "><p id="p1391016142310"><a name="p1391016142310"></a><a name="p1391016142310"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.8%" headers="mcps1.2.4.1.3 "><p id="p174961138125815"><a name="p174961138125815"></a><a name="p174961138125815"></a>Specifies the version release time, which must be the UTC time. For example, the release time of TMS 1.0 is 2016-12-09T00:00:00Z.</p>
    </td>
    </tr>
    <tr id="row12971617238"><td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.2.4.1.1 "><p id="p29121692313"><a name="p29121692313"></a><a name="p29121692313"></a>min_version</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.33%" headers="mcps1.2.4.1.2 "><p id="p189111692310"><a name="p189111692310"></a><a name="p189111692310"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.8%" headers="mcps1.2.4.1.3 "><p id="p1595167238"><a name="p1595167238"></a><a name="p1595167238"></a>If the APIs of this version support microversions, set this parameter to the supported earliest microversion. If not, leave this parameter blank.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   **Links**  field data structure

    **Table  3** **Links**  field data structure description

    <a name="table87796151239"></a>
    <table><thead align="left"><tr id="row10941619231"><th class="cellrowborder" valign="top" width="21.11%" id="mcps1.2.4.1.1"><p id="p591816112316"><a name="p591816112316"></a><a name="p591816112316"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="32.87%" id="mcps1.2.4.1.2"><p id="p7915161233"><a name="p7915161233"></a><a name="p7915161233"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.02%" id="mcps1.2.4.1.3"><p id="p8911652317"><a name="p8911652317"></a><a name="p8911652317"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1591116192310"><td class="cellrowborder" valign="top" width="21.11%" headers="mcps1.2.4.1.1 "><p id="p14101016192311"><a name="p14101016192311"></a><a name="p14101016192311"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.87%" headers="mcps1.2.4.1.2 "><p id="p1710116192319"><a name="p1710116192319"></a><a name="p1710116192319"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.02%" headers="mcps1.2.4.1.3 "><p id="p01031642310"><a name="p01031642310"></a><a name="p01031642310"></a>Specifies the API URL.</p>
    </td>
    </tr>
    <tr id="row7101161237"><td class="cellrowborder" valign="top" width="21.11%" headers="mcps1.2.4.1.1 "><p id="p19101216112319"><a name="p19101216112319"></a><a name="p19101216112319"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.87%" headers="mcps1.2.4.1.2 "><p id="p1710121612238"><a name="p1710121612238"></a><a name="p1710121612238"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.02%" headers="mcps1.2.4.1.3 "><p id="p151061632310"><a name="p151061632310"></a><a name="p151061632310"></a>self</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "versions": [
            {
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
        ]
    }
    ```


## Status Codes<a name="section17789101582315"></a>

For details, see  [Status Code](status-code.md).

## Error Codes<a name="section9414853182510"></a>

For details, see  [Error Code Description](error-code-description.md).

