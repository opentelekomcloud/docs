# Querying Tags in a Specified Project<a name="dws_02_0050"></a>

## Function<a name="section35368561349"></a>

This API is used to query all tags of a tenant for a specified resource type in a specified project.

## URI<a name="section1653755613348"></a>

-   URI format

    GET /v1.0/\{project\_id\}/clusters/tags

-   Parameter description

    **Table  1**  URI parameter description

    <a name="table45441956143415"></a>
    <table><thead align="left"><tr id="row106536561341"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p56531256193417"><a name="p56531256193417"></a><a name="p56531256193417"></a><strong id="b162774213314533_1"><a name="b162774213314533_1"></a><a name="b162774213314533_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p1265335615342"><a name="p1265335615342"></a><a name="p1265335615342"></a><strong id="b84235270684256"><a name="b84235270684256"></a><a name="b84235270684256"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p19653195610349"><a name="p19653195610349"></a><a name="p19653195610349"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p1265318564341"><a name="p1265318564341"></a><a name="p1265318564341"></a><strong id="b842352706134712"><a name="b842352706134712"></a><a name="b842352706134712"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row86536563343"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p18653105653412"><a name="p18653105653412"></a><a name="p18653105653412"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p1365355611348"><a name="p1365355611348"></a><a name="p1365355611348"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p1965355623414"><a name="p1965355623414"></a><a name="p1965355623414"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p14202648155510"><a name="p14202648155510"></a><a name="p14202648155510"></a>Project ID. For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section1551856163419"></a>

-   Sample request

    ```
    GET /v1.0/89cd04f168b84af6be287f71730fdb4b/clusters/tags
    ```

-   Parameter description

    None


## Response<a name="section355385618347"></a>

-   Sample response

    ```
    {
          "tags": [
            {
                "key": "key1",
                "values": [
                    "value1",
                    "value2"
                 ]
            },
            {
                "key": "key2",
                "values": [
                    "value1",
                    "value2"
                 ]
            }
        ]
    }
    ```


-   Parameter description

    **Table  2**  Response parameter description

    <a name="table11557185663418"></a>
    <table><thead align="left"><tr id="row5655105616342"><th class="cellrowborder" valign="top" width="16.16161616161616%" id="mcps1.2.5.1.1"><p id="p106554563348"><a name="p106554563348"></a><a name="p106554563348"></a><strong id="b1147239190"><a name="b1147239190"></a><a name="b1147239190"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.14141414141414%" id="mcps1.2.5.1.2"><p id="p13655156163416"><a name="p13655156163416"></a><a name="p13655156163416"></a><strong id="b1806572985"><a name="b1806572985"></a><a name="b1806572985"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.14141414141414%" id="mcps1.2.5.1.3"><p id="p1265525663415"><a name="p1265525663415"></a><a name="p1265525663415"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="55.55555555555556%" id="mcps1.2.5.1.4"><p id="p1965575613418"><a name="p1965575613418"></a><a name="p1965575613418"></a><strong id="b2070128751"><a name="b2070128751"></a><a name="b2070128751"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3655185643411"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.5.1.1 "><p id="p865511569349"><a name="p865511569349"></a><a name="p865511569349"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p146551656203410"><a name="p146551656203410"></a><a name="p146551656203410"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.3 "><p id="p20655175612344"><a name="p20655175612344"></a><a name="p20655175612344"></a>List&lt;tag&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.55555555555556%" headers="mcps1.2.5.1.4 "><p id="p66551056193416"><a name="p66551056193416"></a><a name="p66551056193416"></a>Tag list. For details, see <a href="#table10385122843">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **tag**  field description

    <a name="table10385122843"></a>
    <table><thead align="left"><tr id="row439616219420"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.1"><p id="p1940118218417"><a name="p1940118218417"></a><a name="p1940118218417"></a><strong id="b795461326"><a name="b795461326"></a><a name="b795461326"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.2"><p id="p04038217417"><a name="p04038217417"></a><a name="p04038217417"></a><strong id="b236012534"><a name="b236012534"></a><a name="b236012534"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p144051125412"><a name="p144051125412"></a><a name="p144051125412"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.2.5.1.4"><p id="p194071124410"><a name="p194071124410"></a><a name="p194071124410"></a><strong id="b153082298"><a name="b153082298"></a><a name="b153082298"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row194101821416"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.1 "><p id="p14413122245"><a name="p14413122245"></a><a name="p14413122245"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p114153214416"><a name="p114153214416"></a><a name="p114153214416"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p1941782642"><a name="p1941782642"></a><a name="p1941782642"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.5.1.4 "><p id="p1265110281282"><a name="p1265110281282"></a><a name="p1265110281282"></a>Key. A tag key can contain a maximum of 36 Unicode characters, which cannot be null. The first and last characters cannot be spaces. </p>
    <p id="p1431781718458"><a name="p1431781718458"></a><a name="p1431781718458"></a>It can contain uppercase letters (A to Z), lowercase letters (a to z), digits (0-9), hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    <tr id="row64181625417"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.1 "><p id="p942020216411"><a name="p942020216411"></a><a name="p942020216411"></a>values</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p4434324417"><a name="p4434324417"></a><a name="p4434324417"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p9435129415"><a name="p9435129415"></a><a name="p9435129415"></a>List&lt;String&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.5.1.4 "><p id="p12437123414"><a name="p12437123414"></a><a name="p12437123414"></a>Value. A tag value can contain a maximum of 43 Unicode characters, which can be null. The first and last characters cannot be spaces. It can contain uppercase letters (A to Z), lowercase letters (a to z), digits (0-9), hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    </tbody>
    </table>


## Returned Value<a name="section15576145612346"></a>

-   Normal

    200

-   Abnormal

    **Table  4**  Returned value for failed requests

    <a name="table2581125633415"></a>
    <table><thead align="left"><tr id="row9656556123414"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.2.3.1.1"><p id="p16561556183411"><a name="p16561556183411"></a><a name="p16561556183411"></a><strong id="b842352706153338"><a name="b842352706153338"></a><a name="b842352706153338"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.2.3.1.2"><p id="p3656956123419"><a name="p3656956123419"></a><a name="p3656956123419"></a><strong id="b1550651484"><a name="b1550651484"></a><a name="b1550651484"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row265605653411"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p186565568344"><a name="p186565568344"></a><a name="p186565568344"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p18656145614343"><a name="p18656145614343"></a><a name="p18656145614343"></a>Invalid parameters.</p>
    </td>
    </tr>
    <tr id="row20656556143418"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p116562565344"><a name="p116562565344"></a><a name="p116562565344"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p5656195633411"><a name="p5656195633411"></a><a name="p5656195633411"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row1865620565340"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p465620561347"><a name="p465620561347"></a><a name="p465620561347"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p1765665633412"><a name="p1765665633412"></a><a name="p1765665633412"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="row1565695618344"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p265625683414"><a name="p265625683414"></a><a name="p265625683414"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p1965615567341"><a name="p1965615567341"></a><a name="p1965615567341"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row146561556163420"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p106561256133418"><a name="p106561256133418"></a><a name="p106561256133418"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p1465615610349"><a name="p1465615610349"></a><a name="p1465615610349"></a>Internal service error.</p>
    </td>
    </tr>
    </tbody>
    </table>


