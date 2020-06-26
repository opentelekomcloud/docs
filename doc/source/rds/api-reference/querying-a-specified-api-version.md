# Querying a Specified API Version<a name="en-us_topic_0032347779"></a>

## Function<a name="section50404481154838"></a>

This API is used to query the specified API version.

-   Learn how to  [authorize and authenticate](authentication.md)  this API before using it.
-   Before calling this API, obtain the required  [region and endpoint](https://docs.otc.t-systems.com/en-us/endpoint/index.html).

## URI<a name="section36318247154838"></a>

-   URI format

    GET https://\{_Endpoint_\}/rds/\{_versionId_\}

-   Example

    https://rds.eu-de.otc.t-systems.com/rds/v1

-   Parameter description

    **Table  1**  Parameter description

    <a name="table4657088"></a>
    <table><thead align="left"><tr id="row60083059"><th class="cellrowborder" valign="top" width="21.3%" id="mcps1.2.4.1.1"><p id="p34889605"><a name="p34889605"></a><a name="p34889605"></a><strong id="b842352706102328"><a name="b842352706102328"></a><a name="b842352706102328"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.26%" id="mcps1.2.4.1.2"><p id="p7485743"><a name="p7485743"></a><a name="p7485743"></a><strong id="b842352706102346"><a name="b842352706102346"></a><a name="b842352706102346"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.44%" id="mcps1.2.4.1.3"><p id="p2365466"><a name="p2365466"></a><a name="p2365466"></a><strong id="b842352706163417"><a name="b842352706163417"></a><a name="b842352706163417"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row29710333152450"><td class="cellrowborder" valign="top" width="21.3%" headers="mcps1.2.4.1.1 "><p id="p54604978152455"><a name="p54604978152455"></a><a name="p54604978152455"></a>versionId</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.26%" headers="mcps1.2.4.1.2 "><p id="p60927123152455"><a name="p60927123152455"></a><a name="p60927123152455"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.44%" headers="mcps1.2.4.1.3 "><p id="p36149969152455"><a name="p36149969152455"></a><a name="p36149969152455"></a>Specifies the API version. It is case-sensitive.</p>
    <p id="p3406227152312"><a name="p3406227152312"></a><a name="p3406227152312"></a>For details, see <span class="parmname" id="parmname6865125310143"><a name="parmname6865125310143"></a><a name="parmname6865125310143"></a><b>id</b></span> in <a href="querying-api-versions.md#table37479565104653">Table 2</a> in section <a href="querying-api-versions.md">Querying API Versions</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section47398739154838"></a>

None

## Response<a name="section59724852154838"></a>

-   Normal response

    **Table  2**  Parameter description

    <a name="table62971306105515"></a>
    <table><thead align="left"><tr id="row21185732105515"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p19221610105536"><a name="p19221610105536"></a><a name="p19221610105536"></a><strong id="b842352706102328_1"><a name="b842352706102328_1"></a><a name="b842352706102328_1"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p13446610105536"><a name="p13446610105536"></a><a name="p13446610105536"></a><strong id="b842352706164541"><a name="b842352706164541"></a><a name="b842352706164541"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p15433610105536"><a name="p15433610105536"></a><a name="p15433610105536"></a><strong id="b842352706163417_1"><a name="b842352706163417_1"></a><a name="b842352706163417_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row24371359105515"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p59749643105536"><a name="p59749643105536"></a><a name="p59749643105536"></a>versions</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p7882916105536"><a name="p7882916105536"></a><a name="p7882916105536"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p42392997105536"><a name="p42392997105536"></a><a name="p42392997105536"></a>Indicates the list of detailed API version information.</p>
    <p id="p239763262013"><a name="p239763262013"></a><a name="p239763262013"></a>For details, see <a href="#table57914909154838">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row3452848511416"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p4534392511416"><a name="p4534392511416"></a><a name="p4534392511416"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p4897932611416"><a name="p4897932611416"></a><a name="p4897932611416"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p790243911416"><a name="p790243911416"></a><a name="p790243911416"></a>Indicates the list of detailed API version information.</p>
    <p id="p54651241172018"><a name="p54651241172018"></a><a name="p54651241172018"></a>For details, see <a href="#table57914909154838">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  versions field data structure description

    <a name="table57914909154838"></a>
    <table><thead align="left"><tr id="row17905664154838"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p41072674154838"><a name="p41072674154838"></a><a name="p41072674154838"></a><strong id="b842352706102328_2"><a name="b842352706102328_2"></a><a name="b842352706102328_2"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p38552284154838"><a name="p38552284154838"></a><a name="p38552284154838"></a><strong id="b842352706164541_1"><a name="b842352706164541_1"></a><a name="b842352706164541_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p35727319154838"><a name="p35727319154838"></a><a name="p35727319154838"></a><strong id="b842352706163417_2"><a name="b842352706163417_2"></a><a name="b842352706163417_2"></a>Description</strong></p>
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
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p2699394512911"><a name="p2699394512911"></a><a name="p2699394512911"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1568933512911"><a name="p1568933512911"></a><a name="p1568933512911"></a>Indicates the API version link information. Its value is empty.</p>
    <p id="p13789175472010"><a name="p13789175472010"></a><a name="p13789175472010"></a>For details, see <a href="#table630875915440">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="row53266474154838"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p19617131154838"><a name="p19617131154838"></a><a name="p19617131154838"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p45483744154838"><a name="p45483744154838"></a><a name="p45483744154838"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p60304625154838"><a name="p60304625154838"></a><a name="p60304625154838"></a>Indicates the version status.</p>
    </td>
    </tr>
    <tr id="row5870720154838"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p5766344154838"><a name="p5766344154838"></a><a name="p5766344154838"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p64420704154838"><a name="p64420704154838"></a><a name="p64420704154838"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p50694512154838"><a name="p50694512154838"></a><a name="p50694512154838"></a>Indicates the version update time.</p>
    <p id="p53597429154838"><a name="p53597429154838"></a><a name="p53597429154838"></a>The format is yyyy-mm-dd Thh:mm:ssZ.</p>
    <p id="p12614817154838"><a name="p12614817154838"></a><a name="p12614817154838"></a><strong id="b842352706104536"><a name="b842352706104536"></a><a name="b842352706104536"></a>T</strong> is the separator between the calendar and the hourly notation of time. <strong id="b842352706161738"><a name="b842352706161738"></a><a name="b842352706161738"></a>Z</strong> indicates the UTC.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  links field data structure description

    <a name="table630875915440"></a>
    <table><thead align="left"><tr id="row4191288815440"><th class="cellrowborder" valign="top" width="26.529999999999998%" id="mcps1.2.4.1.1"><p id="p3950073415440"><a name="p3950073415440"></a><a name="p3950073415440"></a><strong id="b842352706102328_3"><a name="b842352706102328_3"></a><a name="b842352706102328_3"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.800000000000004%" id="mcps1.2.4.1.2"><p id="p4544288515440"><a name="p4544288515440"></a><a name="p4544288515440"></a><strong id="b842352706164541_2"><a name="b842352706164541_2"></a><a name="b842352706164541_2"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.67%" id="mcps1.2.4.1.3"><p id="p5699506015440"><a name="p5699506015440"></a><a name="p5699506015440"></a><strong id="b842352706163417_3"><a name="b842352706163417_3"></a><a name="b842352706163417_3"></a>Description</strong></p>
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
    <td class="cellrowborder" valign="top" width="33.67%" headers="mcps1.2.4.1.3 "><p id="p5004333115440"><a name="p5004333115440"></a><a name="p5004333115440"></a>Its value is <strong id="b84235270616818"><a name="b84235270616818"></a><a name="b84235270616818"></a>self</strong>, indicating that <strong id="b84235270616856"><a name="b84235270616856"></a><a name="b84235270616856"></a>href</strong> is a local link.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example normal response

    ```
    {
      "version": {
        "id": "v1",
        "links": [],
        "status": "CURRENT",
        "updated": "2017-02-07T17:34:02Z"
      },
      "versions": {
        "id": "v1",
        "links": [],
        "status": "CURRENT",
        "updated": "2017-02-07T17:34:02Z"
      }
    }
    ```

-   Abnormal response

    For details, see  [Abnormal Request Results](abnormal-request-results.md).


## Status Code<a name="section4778540915440"></a>

For details, see  [Status Codes](status-codes.md).

## Error Code<a name="section946032144017"></a>

For details, see  [Error Codes](error-codes.md).

