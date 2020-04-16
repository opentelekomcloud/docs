# Querying API Version Information<a name="dds_api_0019"></a>

## Function<a name="section50404481154838"></a>

This API is used to query the specified API version.

## URI<a name="section36318247154838"></a>

URI format

GET /v3

## Requests<a name="section47398739154838"></a>

-   Request header

    ```
    GET https://DDS endpoint/v3
    ```

-   Request body

    N/A


## Responses<a name="section59724852154838"></a>

-   Parameter description

    **Table  1**  Parameter description

    <a name="table62971306105515"></a>
    <table><thead align="left"><tr id="row21185732105515"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p19221610105536"><a name="p19221610105536"></a><a name="p19221610105536"></a><strong id="b842352706102328_3"><a name="b842352706102328_3"></a><a name="b842352706102328_3"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p13446610105536"><a name="p13446610105536"></a><a name="p13446610105536"></a><strong id="b842352706164541_1"><a name="b842352706164541_1"></a><a name="b842352706164541_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p2775334615440"><a name="p2775334615440"></a><a name="p2775334615440"></a><strong id="b561212380301"><a name="b561212380301"></a><a name="b561212380301"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3452848511416"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p4534392511416"><a name="p4534392511416"></a><a name="p4534392511416"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p146911450319"><a name="p146911450319"></a><a name="p146911450319"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p790243911416"><a name="p790243911416"></a><a name="p790243911416"></a>Indicates the list of detailed API version information. For more information, see <a href="#table57914909154838">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2** **version**  field data structure description

    <a name="table57914909154838"></a>
    <table><thead align="left"><tr id="row17905664154838"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p41072674154838"><a name="p41072674154838"></a><a name="p41072674154838"></a><strong id="b842352706102328_5"><a name="b842352706102328_5"></a><a name="b842352706102328_5"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p38552284154838"><a name="p38552284154838"></a><a name="p38552284154838"></a><strong id="b842352706164541_3"><a name="b842352706164541_3"></a><a name="b842352706164541_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p35727319154838"><a name="p35727319154838"></a><a name="p35727319154838"></a><strong id="b190914406302"><a name="b190914406302"></a><a name="b190914406302"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8231739154838"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p62791086154838"><a name="p62791086154838"></a><a name="p62791086154838"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p52913243154838"><a name="p52913243154838"></a><a name="p52913243154838"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p58114280154838"><a name="p58114280154838"></a><a name="p58114280154838"></a>Indicates the API version.</p>
    </td>
    </tr>
    <tr id="row83118291298"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p2684540212911"><a name="p2684540212911"></a><a name="p2684540212911"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p121791290324"><a name="p121791290324"></a><a name="p121791290324"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p16707192915253"><a name="p16707192915253"></a><a name="p16707192915253"></a>Specifies the API version link information. For more information, see <a href="#table630875915440">Table 3</a>.</p>
    <div class="note" id="note1766615256328"><a name="note1766615256328"></a><a name="note1766615256328"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p566620258325"><a name="p566620258325"></a><a name="p566620258325"></a>If the version is <strong id="b178932184317"><a name="b178932184317"></a><a name="b178932184317"></a>v3</strong>, the value is <strong id="b1191332194310"><a name="b1191332194310"></a><a name="b1191332194310"></a>[]</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row53266474154838"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p19617131154838"><a name="p19617131154838"></a><a name="p19617131154838"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p45483744154838"><a name="p45483744154838"></a><a name="p45483744154838"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p60304625154838"><a name="p60304625154838"></a><a name="p60304625154838"></a>Indicates the version status. The value <strong id="b1392026309"><a name="b1392026309"></a><a name="b1392026309"></a>CURRENT</strong> indicates that the version has been released.</p>
    </td>
    </tr>
    <tr id="row1144294017433"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p154811524144020"><a name="p154811524144020"></a><a name="p154811524144020"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p10856104114111"><a name="p10856104114111"></a><a name="p10856104114111"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p44820241403"><a name="p44820241403"></a><a name="p44820241403"></a>Indicates the subversion of the API version.</p>
    </td>
    </tr>
    <tr id="row17567134264316"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p12508727124012"><a name="p12508727124012"></a><a name="p12508727124012"></a>min_version</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p468916534116"><a name="p468916534116"></a><a name="p468916534116"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p050922734018"><a name="p050922734018"></a><a name="p050922734018"></a>Indicates the minimum API version.</p>
    </td>
    </tr>
    <tr id="row5870720154838"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p5766344154838"><a name="p5766344154838"></a><a name="p5766344154838"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p64420704154838"><a name="p64420704154838"></a><a name="p64420704154838"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p50694512154838"><a name="p50694512154838"></a><a name="p50694512154838"></a>Indicates the version update time.</p>
    <p id="p53597429154838"><a name="p53597429154838"></a><a name="p53597429154838"></a>The format is yyyy-mm-ddThh:mm:ssZ.</p>
    <p id="p12614817154838"><a name="p12614817154838"></a><a name="p12614817154838"></a><strong id="b124899218206"><a name="b124899218206"></a><a name="b124899218206"></a>T</strong> is the separator between the calendar and the hourly notation of time. <strong id="b174898242017"><a name="b174898242017"></a><a name="b174898242017"></a>Z</strong> indicates the UTC.</p>
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
    <th class="cellrowborder" valign="top" width="33.67%" id="mcps1.2.4.1.3"><p id="p5699506015440"><a name="p5699506015440"></a><a name="p5699506015440"></a><strong id="b1054218448304"><a name="b1054218448304"></a><a name="b1054218448304"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5319717215440"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p1400369315440"><a name="p1400369315440"></a><a name="p1400369315440"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.2 "><p id="p6055731815440"><a name="p6055731815440"></a><a name="p6055731815440"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.67%" headers="mcps1.2.4.1.3 "><p id="p619568715440"><a name="p619568715440"></a><a name="p619568715440"></a>Indicates the API URL and the value is <strong id="b842352706181135"><a name="b842352706181135"></a><a name="b842352706181135"></a>""</strong>.</p>
    </td>
    </tr>
    <tr id="row5576118615440"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p2036224315440"><a name="p2036224315440"></a><a name="p2036224315440"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.2 "><p id="p3872902515440"><a name="p3872902515440"></a><a name="p3872902515440"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.67%" headers="mcps1.2.4.1.3 "><p id="p5004333115440"><a name="p5004333115440"></a><a name="p5004333115440"></a>Its value is <strong id="b6291128112011"><a name="b6291128112011"></a><a name="b6291128112011"></a>self</strong>, indicating that URL is a local link.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    {
        "version": {
            "id": "v3",
            "links": [],
            "status": "CURRENT",
            "version": "",
            "min_version": "",
            "updated": "2017-02-07T17:34:02Z"
        }
    }
    ```


## **Status Code**<a name="section5382712154838"></a>

For more information, see  [Status Code](status-code.md).

## Error Code<a name="section6522193710339"></a>

For more information, see  [Error Code](error-code.md).

