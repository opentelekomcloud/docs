# Adding Backup Resource Tags<a name="EN-US_TOPIC_0098635088"></a>

## Function<a name="section53029257"></a>

A resource can have up to 10 tags.

The API is idempotent.

If a to-be-created tag has the same key as an existing tag, the tag will be created and overwrite the existing one.

## URI<a name="section7501266"></a>

-   URI format

    POST https://\{endpoint\}/v1/\{project\_id\}/csbs\_backup/\{resource\_id\}/tags

-   Request header

    **Table  1**  Request header

    <a name="table6015877"></a>
    <table><thead align="left"><tr id="row25002739"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p209623317216"><a name="p209623317216"></a><a name="p209623317216"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="p15962193221"><a name="p15962193221"></a><a name="p15962193221"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.3"><p id="p99783315213"><a name="p99783315213"></a><a name="p99783315213"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="p6978835213"><a name="p6978835213"></a><a name="p6978835213"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row46794527"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p32260306"><a name="p32260306"></a><a name="p32260306"></a>Content-type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p154921827359"><a name="p154921827359"></a><a name="p154921827359"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p62948031"><a name="p62948031"></a><a name="p62948031"></a>MIME type of the body in the request</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p14084705"><a name="p14084705"></a><a name="p14084705"></a>application/json</p>
    </td>
    </tr>
    <tr id="row59653487"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p94244"><a name="p94244"></a><a name="p94244"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p2049014274520"><a name="p2049014274520"></a><a name="p2049014274520"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p7633781"><a name="p7633781"></a><a name="p7633781"></a>User token</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p22030350"><a name="p22030350"></a><a name="p22030350"></a>-</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Parameter description

    **Table  2**  Parameter description

    <a name="table55746681"></a>
    <table><thead align="left"><tr id="row59842155"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p17203192132211"><a name="p17203192132211"></a><a name="p17203192132211"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p820322192212"><a name="p820322192212"></a><a name="p820322192212"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p220320218227"><a name="p220320218227"></a><a name="p220320218227"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="p6203121142215"><a name="p6203121142215"></a><a name="p6203121142215"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row55828882"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p25845597"><a name="p25845597"></a><a name="p25845597"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p13118588"><a name="p13118588"></a><a name="p13118588"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p55972696"><a name="p55972696"></a><a name="p55972696"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p65779720"><a name="p65779720"></a><a name="p65779720"></a>Project ID</p>
    </td>
    </tr>
    <tr id="row51334836"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p64481047"><a name="p64481047"></a><a name="p64481047"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p55582327"><a name="p55582327"></a><a name="p55582327"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p5874619"><a name="p5874619"></a><a name="p5874619"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p6082124"><a name="p6082124"></a><a name="p6082124"></a>Resource ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section402532"></a>

-   Parameter description

    **Table  3**  Parameter description

    <a name="table8462442"></a>
    <table><thead align="left"><tr id="row29754946"><th class="cellrowborder" valign="top" width="25.252525252525253%" id="mcps1.2.5.1.1"><p id="p950072422214"><a name="p950072422214"></a><a name="p950072422214"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.2.5.1.2"><p id="p195001224202211"><a name="p195001224202211"></a><a name="p195001224202211"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.2.5.1.3"><p id="p850020246221"><a name="p850020246221"></a><a name="p850020246221"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.46464646464647%" id="mcps1.2.5.1.4"><p id="p2500224152214"><a name="p2500224152214"></a><a name="p2500224152214"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row48033505"><td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.2.5.1.1 "><p id="p65508730"><a name="p65508730"></a><a name="p65508730"></a>tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.2 "><p id="p4606919"><a name="p4606919"></a><a name="p4606919"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.3 "><p id="p37616177"><a name="p37616177"></a><a name="p37616177"></a>tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.46464646464647%" headers="mcps1.2.5.1.4 "><p id="p27011487"><a name="p27011487"></a><a name="p27011487"></a>List of included tags. Backups with these tags will be filtered.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **tag**

    **Table  4**  Parameter description of field  **tag**

    <a name="table40446842"></a>
    <table><thead align="left"><tr id="row62127694"><th class="cellrowborder" valign="top" width="26%" id="mcps1.2.5.1.1"><p id="p11561928102219"><a name="p11561928102219"></a><a name="p11561928102219"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.2"><p id="p13156428142218"><a name="p13156428142218"></a><a name="p13156428142218"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p41721428172212"><a name="p41721428172212"></a><a name="p41721428172212"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="p12172628112218"><a name="p12172628112218"></a><a name="p12172628112218"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row57846236"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.5.1.1 "><p id="p55033577"><a name="p55033577"></a><a name="p55033577"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p28534742"><a name="p28534742"></a><a name="p28534742"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p29612747"><a name="p29612747"></a><a name="p29612747"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p798643483310"><a name="p798643483310"></a><a name="p798643483310"></a>Tag key</p>
    <p id="p036816391334"><a name="p036816391334"></a><a name="p036816391334"></a>It consists of up to 36 characters.</p>
    <p id="p1815945343312"><a name="p1815945343312"></a><a name="p1815945343312"></a>It cannot be an empty string.</p>
    <p id="p139819543334"><a name="p139819543334"></a><a name="p139819543334"></a>Spaces before and after a key will be deprecated.</p>
    <p id="p14766132412516"><a name="p14766132412516"></a><a name="p14766132412516"></a>It can contain only letters, digits, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    <tr id="row45747710"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.5.1.1 "><p id="p14577007"><a name="p14577007"></a><a name="p14577007"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p39886950"><a name="p39886950"></a><a name="p39886950"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p9617480"><a name="p9617480"></a><a name="p9617480"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p11608421163420"><a name="p11608421163420"></a><a name="p11608421163420"></a>Tag value</p>
    <p id="p489413816351"><a name="p489413816351"></a><a name="p489413816351"></a>It consists of up to 43 characters.</p>
    <p id="p14194717123517"><a name="p14194717123517"></a><a name="p14194717123517"></a>It can be an empty string.</p>
    <p id="p1146913338362"><a name="p1146913338362"></a><a name="p1146913338362"></a>Spaces before and after a tag value will be deprecated.</p>
    <p id="p12929161920302"><a name="p12929161920302"></a><a name="p12929161920302"></a>It can contain only letters, digits, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    POST https://{endpoint}/v1/{project_id}/csbs_backup/{resource_id}/tags
    ```


-   Example request

    ```
    {
        "tag":
        {
            "key":"DEV",
            "value":"DEV1"
        }
    }
    ```


## Status Codes<a name="section3622792"></a>

-   Normal

    <a name="table8957019"></a>
    <table><thead align="left"><tr id="row18063398"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p53849108"><a name="p53849108"></a><a name="p53849108"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p66810458"><a name="p66810458"></a><a name="p66810458"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row42938017"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p55427344"><a name="p55427344"></a><a name="p55427344"></a>204</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p60429904"><a name="p60429904"></a><a name="p60429904"></a>No Content</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    <a name="table62984073"></a>
    <table><thead align="left"><tr id="row40399134"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p51104447"><a name="p51104447"></a><a name="p51104447"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p45819581"><a name="p45819581"></a><a name="p45819581"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row20398591"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p41673198"><a name="p41673198"></a><a name="p41673198"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p20085873"><a name="p20085873"></a><a name="p20085873"></a>Invalid action.</p>
    </td>
    </tr>
    <tr id="row46555134"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p12869499"><a name="p12869499"></a><a name="p12869499"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p35796480"><a name="p35796480"></a><a name="p35796480"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row53732870"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p57395179"><a name="p57395179"></a><a name="p57395179"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p18497900"><a name="p18497900"></a><a name="p18497900"></a>You do not have permission to perform this operation.</p>
    </td>
    </tr>
    <tr id="row32263379"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p63196939"><a name="p63196939"></a><a name="p63196939"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p18678419"><a name="p18678419"></a><a name="p18678419"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row33888044"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p60577072"><a name="p60577072"></a><a name="p60577072"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p7795800"><a name="p7795800"></a><a name="p7795800"></a>A system exception occurs.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section61541938486"></a>

For details, see  [Error Codes](error-codes.md).

