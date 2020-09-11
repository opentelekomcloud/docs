# Deleting Backup Resource Tags<a name="EN-US_TOPIC_0098635089"></a>

## Function<a name="section49623694"></a>

The API is idempotent.

When you delete a nonexistent tag, error code  **404**  will be returned. Tag keys cannot be empty or be empty character strings.

## URI<a name="section43960067"></a>

-   URI format

    DELETE https://\{endpoint\}/v1/\{project\_id\}/csbs\_backup/\{resource\_id\}/tags/\{key\}

-   Request header

    **Table  1**  Request header

    <a name="table44294601"></a>
    <table><thead align="left"><tr id="row43746220"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p209623317216"><a name="p209623317216"></a><a name="p209623317216"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="p15962193221"><a name="p15962193221"></a><a name="p15962193221"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.3"><p id="p99783315213"><a name="p99783315213"></a><a name="p99783315213"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="p6978835213"><a name="p6978835213"></a><a name="p6978835213"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row65816909"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p29569442"><a name="p29569442"></a><a name="p29569442"></a>Content-type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p1518215126512"><a name="p1518215126512"></a><a name="p1518215126512"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p46314624"><a name="p46314624"></a><a name="p46314624"></a>MIME type of the body in the request</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p1313012"><a name="p1313012"></a><a name="p1313012"></a>application/json</p>
    </td>
    </tr>
    <tr id="row11817112"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p17662006"><a name="p17662006"></a><a name="p17662006"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p18181141210512"><a name="p18181141210512"></a><a name="p18181141210512"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p21336385"><a name="p21336385"></a><a name="p21336385"></a>User token</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p66041788"><a name="p66041788"></a><a name="p66041788"></a>-</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Parameter description

    **Table  2**  Parameter description

    <a name="table45345096"></a>
    <table><thead align="left"><tr id="row20859864"><th class="cellrowborder" valign="top" width="25.252525252525253%" id="mcps1.2.5.1.1"><p id="p831374913227"><a name="p831374913227"></a><a name="p831374913227"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.2.5.1.2"><p id="p83131949182210"><a name="p83131949182210"></a><a name="p83131949182210"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.2.5.1.3"><p id="p53131849152214"><a name="p53131849152214"></a><a name="p53131849152214"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.46464646464647%" id="mcps1.2.5.1.4"><p id="p1231314902216"><a name="p1231314902216"></a><a name="p1231314902216"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row52061686"><td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.2.5.1.1 "><p id="p56247066"><a name="p56247066"></a><a name="p56247066"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.2 "><p id="p59718498"><a name="p59718498"></a><a name="p59718498"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.3 "><p id="p5360183"><a name="p5360183"></a><a name="p5360183"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.46464646464647%" headers="mcps1.2.5.1.4 "><p id="p65779720"><a name="p65779720"></a><a name="p65779720"></a>Project ID</p>
    </td>
    </tr>
    <tr id="row46680697"><td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.2.5.1.1 "><p id="p23040133"><a name="p23040133"></a><a name="p23040133"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.2 "><p id="p54311518"><a name="p54311518"></a><a name="p54311518"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.3 "><p id="p37156843"><a name="p37156843"></a><a name="p37156843"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.46464646464647%" headers="mcps1.2.5.1.4 "><p id="p56914325"><a name="p56914325"></a><a name="p56914325"></a>Resource ID</p>
    </td>
    </tr>
    <tr id="row42466880"><td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.2.5.1.1 "><p id="p17265247"><a name="p17265247"></a><a name="p17265247"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.2 "><p id="p56307791"><a name="p56307791"></a><a name="p56307791"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.3 "><p id="p64637240"><a name="p64637240"></a><a name="p64637240"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.46464646464647%" headers="mcps1.2.5.1.4 "><p id="p13216186"><a name="p13216186"></a><a name="p13216186"></a>Tag key</p>
    <p id="p482715431313"><a name="p482715431313"></a><a name="p482715431313"></a>A tag key consists of up to 127 characters.</p>
    <p id="p182716437311"><a name="p182716437311"></a><a name="p182716437311"></a>A tag key cannot be an empty string.</p>
    <p id="p7988143725117"><a name="p7988143725117"></a><a name="p7988143725117"></a>Spaces before and after a key will be deprecated.</p>
    <p id="p98272043731"><a name="p98272043731"></a><a name="p98272043731"></a>It cannot contain the following characters: ASCII (0-31), asterisks (*), less-than signs (&lt;), greater-than signs (&gt;), backslashes (\), equal signs (=), commas (,), vertical bars (|), and slashes (/). </p>
    <p id="p1831113845514"><a name="p1831113845514"></a><a name="p1831113845514"></a>(The code only verifies whether the key is an empty character string, instead of the length and character set. Keys are checked and used after deleting the spaces before and after them. Even invalid tags existing at the bottom layer can be deleted.)</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section60096286"></a>

-   Example request

    ```
    DELETE https://{endpoint}/v1/{project_id}/csbs_backup/{resource_id}/tags/{key}
    ```


## Status Codes<a name="section3995664"></a>

-   Normal

    <a name="table14380054"></a>
    <table><thead align="left"><tr id="row66507565"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p18403674"><a name="p18403674"></a><a name="p18403674"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p14302607"><a name="p14302607"></a><a name="p14302607"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row17660533"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p21217075"><a name="p21217075"></a><a name="p21217075"></a>204</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p40861554"><a name="p40861554"></a><a name="p40861554"></a>No Content</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    <a name="table21451610"></a>
    <table><thead align="left"><tr id="row16328535"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p47542959"><a name="p47542959"></a><a name="p47542959"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p25774484"><a name="p25774484"></a><a name="p25774484"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row7358445"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p59163171"><a name="p59163171"></a><a name="p59163171"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p27487517"><a name="p27487517"></a><a name="p27487517"></a>Invalid parameters.</p>
    </td>
    </tr>
    <tr id="row46061063"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p39958627"><a name="p39958627"></a><a name="p39958627"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p15423351"><a name="p15423351"></a><a name="p15423351"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row4592438"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p36443218"><a name="p36443218"></a><a name="p36443218"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p66219579"><a name="p66219579"></a><a name="p66219579"></a>You do not have permission to perform this operation.</p>
    </td>
    </tr>
    <tr id="row59105304"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p22800286"><a name="p22800286"></a><a name="p22800286"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p34883877"><a name="p34883877"></a><a name="p34883877"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row45519440"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p63196027"><a name="p63196027"></a><a name="p63196027"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p18604538"><a name="p18604538"></a><a name="p18604538"></a>A system exception occurs.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section61541938486"></a>

For details, see  [Error Codes](error-codes.md).

