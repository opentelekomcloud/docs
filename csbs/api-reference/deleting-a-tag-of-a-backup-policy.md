# Deleting a Tag of a Backup Policy<a name="EN-US_TOPIC_0098635095"></a>

## Function<a name="section48650648"></a>

The API is idempotent.

When you delete a nonexistent tag, error code  **404**  will be returned. Tag keys cannot be empty or be empty character strings.

## URI<a name="section35202648"></a>

-   URI format

    DELETE https://\{endpoint\}/v1/\{project\_id\}/csbs\_backup\_policy/\{resource\_id\}/tags/\{key\}

-   Request header

    **Table  1**  Request header

    <a name="table35680165"></a>
    <table><thead align="left"><tr id="row21584674"><th class="cellrowborder" valign="top" width="20.62%" id="mcps1.2.5.1.1"><p id="p209623317216"><a name="p209623317216"></a><a name="p209623317216"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.77%" id="mcps1.2.5.1.2"><p id="p15962193221"><a name="p15962193221"></a><a name="p15962193221"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.59%" id="mcps1.2.5.1.3"><p id="p99783315213"><a name="p99783315213"></a><a name="p99783315213"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="34.02%" id="mcps1.2.5.1.4"><p id="p6978835213"><a name="p6978835213"></a><a name="p6978835213"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row35410022"><td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.1 "><p id="p49639570"><a name="p49639570"></a><a name="p49639570"></a>Content-type</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.77%" headers="mcps1.2.5.1.2 "><p id="p144771859261"><a name="p144771859261"></a><a name="p144771859261"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.5.1.3 "><p id="p61382201"><a name="p61382201"></a><a name="p61382201"></a>MIME type of the body in the request</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p8332830"><a name="p8332830"></a><a name="p8332830"></a>application/json</p>
    </td>
    </tr>
    <tr id="row7886611"><td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.1 "><p id="p34835721"><a name="p34835721"></a><a name="p34835721"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.77%" headers="mcps1.2.5.1.2 "><p id="p647610591369"><a name="p647610591369"></a><a name="p647610591369"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.5.1.3 "><p id="p3121152"><a name="p3121152"></a><a name="p3121152"></a>User token</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p9677327"><a name="p9677327"></a><a name="p9677327"></a>-</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Parameter description

    **Table  2**  Parameter description

    <a name="table7961729"></a>
    <table><thead align="left"><tr id="row46636132"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p0674144172518"><a name="p0674144172518"></a><a name="p0674144172518"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p1367454172514"><a name="p1367454172514"></a><a name="p1367454172514"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p3674341142516"><a name="p3674341142516"></a><a name="p3674341142516"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p13674104114257"><a name="p13674104114257"></a><a name="p13674104114257"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row60309786"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p53254482"><a name="p53254482"></a><a name="p53254482"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p18645762"><a name="p18645762"></a><a name="p18645762"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p33911763"><a name="p33911763"></a><a name="p33911763"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p65779720"><a name="p65779720"></a><a name="p65779720"></a>Project ID</p>
    </td>
    </tr>
    <tr id="row1462819"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p51379511"><a name="p51379511"></a><a name="p51379511"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p990892"><a name="p990892"></a><a name="p990892"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p13153450"><a name="p13153450"></a><a name="p13153450"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p58796504"><a name="p58796504"></a><a name="p58796504"></a>Resource ID</p>
    </td>
    </tr>
    <tr id="row59406488"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p47196242"><a name="p47196242"></a><a name="p47196242"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p64799248"><a name="p64799248"></a><a name="p64799248"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p14247739"><a name="p14247739"></a><a name="p14247739"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p13216186"><a name="p13216186"></a><a name="p13216186"></a>Tag key</p>
    <p id="p482715431313"><a name="p482715431313"></a><a name="p482715431313"></a>A tag key consists of up to 127 characters.</p>
    <p id="p182716437311"><a name="p182716437311"></a><a name="p182716437311"></a>A tag key cannot be an empty string.</p>
    <p id="p7988143725117"><a name="p7988143725117"></a><a name="p7988143725117"></a>Spaces before and after a key will be deprecated.</p>
    <p id="p98272043731"><a name="p98272043731"></a><a name="p98272043731"></a>It cannot contain the following characters: ASCII (0-31), asterisks (*), less-than signs (&lt;), greater-than signs (&gt;), backslashes (\), equal signs (=), commas (,), vertical bars (|), and slashes (/). </p>
    <p id="p182644299542"><a name="p182644299542"></a><a name="p182644299542"></a>(The code only verifies whether the key is an empty character string, instead of the length and character set. Keys are checked and used after deleting the spaces before and after them. Even invalid tags existing at the bottom layer can be deleted.)</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section48388379"></a>

-   Example request

    ```
    DELETE https://{endpoint}/v1/{project_id}/csbs_backup_policy/{resource_id}/tags/{key}
    ```


## Status Codes<a name="section32842235"></a>

-   Normal

    <a name="table5596611"></a>
    <table><thead align="left"><tr id="row30280082"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p36767573"><a name="p36767573"></a><a name="p36767573"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p25383445"><a name="p25383445"></a><a name="p25383445"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row42793145"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p43692714"><a name="p43692714"></a><a name="p43692714"></a>204</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p49448911"><a name="p49448911"></a><a name="p49448911"></a>No Content</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    <a name="table45938832"></a>
    <table><thead align="left"><tr id="row34750807"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p63351959"><a name="p63351959"></a><a name="p63351959"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p31235064"><a name="p31235064"></a><a name="p31235064"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row47012257"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p49896507"><a name="p49896507"></a><a name="p49896507"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p15085294"><a name="p15085294"></a><a name="p15085294"></a>Invalid parameters.</p>
    </td>
    </tr>
    <tr id="row1549920"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p58434666"><a name="p58434666"></a><a name="p58434666"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p35587488"><a name="p35587488"></a><a name="p35587488"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row51851944"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p39257932"><a name="p39257932"></a><a name="p39257932"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p25775953"><a name="p25775953"></a><a name="p25775953"></a>You do not have permission to perform this operation.</p>
    </td>
    </tr>
    <tr id="row30656991"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p188376"><a name="p188376"></a><a name="p188376"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p15258501"><a name="p15258501"></a><a name="p15258501"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row3108787"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p50485194"><a name="p50485194"></a><a name="p50485194"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p62768905"><a name="p62768905"></a><a name="p62768905"></a>A system exception occurs.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section61541938486"></a>

For details, see  [Error Codes](error-codes.md).

