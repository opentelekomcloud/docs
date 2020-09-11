# Batch Adding or Deleting Tags of a Backup Policy<a name="EN-US_TOPIC_0098635093"></a>

## Function<a name="section56903338"></a>

This API is used to add or delete tags of a specific instance in batches.

The TMS may use this API to manage service resource tags.

A resource can have up to 10 tags.

The API is idempotent.

If there are duplicate keys in the request body when you add tags, an error is reported.

If the key of the to-be-created tag is the same as that of an existing tag, the value of the existing tag will be overwritten.

When tags are being deleted and some tags do not exist, the operation is considered successful by default, and the character set of the tags will not be checked upon deletion. A key and a value can respectively consist of up to 127 and 255 characters. The tag structure cannot be missing, and the key cannot be left blank or an empty string.

## URI<a name="section42368002"></a>

-   URI format

    POST https://\{endpoint\}/v1/\{project\_id\}/csbs\_backup\_policy/\{resource\_id\}/tags/action

-   Request header

    **Table  1**  Request header

    <a name="table51600525"></a>
    <table><thead align="left"><tr id="row60328301"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p209623317216"><a name="p209623317216"></a><a name="p209623317216"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.2"><p id="p15962193221"><a name="p15962193221"></a><a name="p15962193221"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.3"><p id="p99783315213"><a name="p99783315213"></a><a name="p99783315213"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="34%" id="mcps1.2.5.1.4"><p id="p6978835213"><a name="p6978835213"></a><a name="p6978835213"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row45359475"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p50238873"><a name="p50238873"></a><a name="p50238873"></a>Content-type</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="p16193056413"><a name="p16193056413"></a><a name="p16193056413"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.3 "><p id="p42816919"><a name="p42816919"></a><a name="p42816919"></a>MIME type of the body in the request</p>
    </td>
    <td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.5.1.4 "><p id="p4107326"><a name="p4107326"></a><a name="p4107326"></a>application/json</p>
    </td>
    </tr>
    <tr id="row36965936"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p41450855"><a name="p41450855"></a><a name="p41450855"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="p71891458410"><a name="p71891458410"></a><a name="p71891458410"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.3 "><p id="p2076123"><a name="p2076123"></a><a name="p2076123"></a>User token</p>
    </td>
    <td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.5.1.4 "><p id="p65455768"><a name="p65455768"></a><a name="p65455768"></a>-</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Parameter description

    **Table  2**  Parameter description

    <a name="table29749984"></a>
    <table><thead align="left"><tr id="row45863866"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p96904382513"><a name="p96904382513"></a><a name="p96904382513"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p1869043112518"><a name="p1869043112518"></a><a name="p1869043112518"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p196903302517"><a name="p196903302517"></a><a name="p196903302517"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p3690113192517"><a name="p3690113192517"></a><a name="p3690113192517"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row43875243"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p64233789"><a name="p64233789"></a><a name="p64233789"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p35554407"><a name="p35554407"></a><a name="p35554407"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p61334738"><a name="p61334738"></a><a name="p61334738"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p65779720"><a name="p65779720"></a><a name="p65779720"></a>Project ID</p>
    </td>
    </tr>
    <tr id="row54165854"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p25358060"><a name="p25358060"></a><a name="p25358060"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p40737019"><a name="p40737019"></a><a name="p40737019"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p11364275"><a name="p11364275"></a><a name="p11364275"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p48091067"><a name="p48091067"></a><a name="p48091067"></a>Resource ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section45767702"></a>

-   Parameter description

    **Table  3**  Parameter description

    <a name="table46722268"></a>
    <table><thead align="left"><tr id="row54095396"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p1691015752511"><a name="p1691015752511"></a><a name="p1691015752511"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.2"><p id="p1791013762512"><a name="p1791013762512"></a><a name="p1791013762512"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p179101272256"><a name="p179101272256"></a><a name="p179101272256"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="40%" id="mcps1.2.5.1.4"><p id="p159104717251"><a name="p159104717251"></a><a name="p159104717251"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row39295971"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p28857116"><a name="p28857116"></a><a name="p28857116"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="p55725065"><a name="p55725065"></a><a name="p55725065"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p17436435"><a name="p17436435"></a><a name="p17436435"></a>List&lt;resource_tag&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.5.1.4 "><p id="p3065121"><a name="p3065121"></a><a name="p3065121"></a>Tag list</p>
    <p id="p137815273418"><a name="p137815273418"></a><a name="p137815273418"></a>This list cannot be an empty list.</p>
    <p id="p183916535015"><a name="p183916535015"></a><a name="p183916535015"></a>The list can contain up to 10 keys.</p>
    <p id="p1338589319"><a name="p1338589319"></a><a name="p1338589319"></a>Keys in this list must be unique.</p>
    </td>
    </tr>
    <tr id="row27586093"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p19881085"><a name="p19881085"></a><a name="p19881085"></a>action</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="p66864070"><a name="p66864070"></a><a name="p66864070"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p47280559"><a name="p47280559"></a><a name="p47280559"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.5.1.4 "><p id="p4520032"><a name="p4520032"></a><a name="p4520032"></a>Operation to be performed. The value can be set to <strong id="b115513501334"><a name="b115513501334"></a><a name="b115513501334"></a>create</strong> or <strong id="b19552350163316"><a name="b19552350163316"></a><a name="b19552350163316"></a>delete</strong> only.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **resource\_tag**

    **Table  4**  Parameter description of field  **resource\_tag**

    <a name="table30578306"></a>
    <table><thead align="left"><tr id="row46313587"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p118111218254"><a name="p118111218254"></a><a name="p118111218254"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.2"><p id="p158131213253"><a name="p158131213253"></a><a name="p158131213253"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p3811712142511"><a name="p3811712142511"></a><a name="p3811712142511"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="40%" id="mcps1.2.5.1.4"><p id="p108131211257"><a name="p108131211257"></a><a name="p108131211257"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row7522368"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p5332049"><a name="p5332049"></a><a name="p5332049"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="p29242856"><a name="p29242856"></a><a name="p29242856"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p19861098"><a name="p19861098"></a><a name="p19861098"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.5.1.4 "><p id="p798643483310"><a name="p798643483310"></a><a name="p798643483310"></a>Tag key (when <strong id="b842352706211644"><a name="b842352706211644"></a><a name="b842352706211644"></a>action</strong> is set to <strong id="b842352706211650"><a name="b842352706211650"></a><a name="b842352706211650"></a>create</strong>)</p>
    <p id="p036816391334"><a name="p036816391334"></a><a name="p036816391334"></a>It consists of up to 36 characters.</p>
    <p id="p1815945343312"><a name="p1815945343312"></a><a name="p1815945343312"></a>It cannot be an empty string.</p>
    <p id="p139819543334"><a name="p139819543334"></a><a name="p139819543334"></a>Spaces before and after a key will be deprecated.</p>
    <p id="p14766132412516"><a name="p14766132412516"></a><a name="p14766132412516"></a>It can contain only letters, digits, hyphens (-), and underscores (_).</p>
    <p id="p4208458163611"><a name="p4208458163611"></a><a name="p4208458163611"></a>Tag key (when <strong id="b1178062727"><a name="b1178062727"></a><a name="b1178062727"></a>action</strong> is set to <strong id="b1793014523"><a name="b1793014523"></a><a name="b1793014523"></a>delete</strong>)</p>
    <p id="p1165515448375"><a name="p1165515448375"></a><a name="p1165515448375"></a>It consists of up to 127 characters.</p>
    <p id="p289271163811"><a name="p289271163811"></a><a name="p289271163811"></a>It cannot be an empty string.</p>
    <p id="p136318151388"><a name="p136318151388"></a><a name="p136318151388"></a>Spaces before and after a key will be deprecated.</p>
    </td>
    </tr>
    <tr id="row50335184"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p50618113"><a name="p50618113"></a><a name="p50618113"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="p6426490"><a name="p6426490"></a><a name="p6426490"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p50783716"><a name="p50783716"></a><a name="p50783716"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.5.1.4 "><p id="p11608421163420"><a name="p11608421163420"></a><a name="p11608421163420"></a>Tag value (when <strong id="b2008508826"><a name="b2008508826"></a><a name="b2008508826"></a>action</strong> is set to <strong id="b2063869929"><a name="b2063869929"></a><a name="b2063869929"></a>create</strong>)</p>
    <p id="p17862829154114"><a name="p17862829154114"></a><a name="p17862829154114"></a>This parameter is mandatory.</p>
    <p id="p489413816351"><a name="p489413816351"></a><a name="p489413816351"></a>It consists of up to 43 characters.</p>
    <p id="p14194717123517"><a name="p14194717123517"></a><a name="p14194717123517"></a>It can be an empty string.</p>
    <p id="p1146913338362"><a name="p1146913338362"></a><a name="p1146913338362"></a>Spaces before and after a tag value will be deprecated.</p>
    <p id="p181669243419"><a name="p181669243419"></a><a name="p181669243419"></a>It can contain only letters, digits, hyphens (-), and underscores (_).</p>
    <p id="p239755173813"><a name="p239755173813"></a><a name="p239755173813"></a>Tag value (when <strong id="b454388530"><a name="b454388530"></a><a name="b454388530"></a>action</strong> is set to <strong id="b768108274"><a name="b768108274"></a><a name="b768108274"></a>delete</strong>)</p>
    <p id="p13546172617403"><a name="p13546172617403"></a><a name="p13546172617403"></a>The tag value can be passed or not.</p>
    <p id="p1923221093917"><a name="p1923221093917"></a><a name="p1923221093917"></a>It consists of up to 255 characters.</p>
    <p id="p1211002563912"><a name="p1211002563912"></a><a name="p1211002563912"></a>It can be an empty string.</p>
    <p id="p7821195193918"><a name="p7821195193918"></a><a name="p7821195193918"></a>Spaces before and after a tag value will be deprecated.</p>
    <p id="p3863663"><a name="p3863663"></a><a name="p3863663"></a>If the value is not passed, the tag is located and deleted based on the key and value. If the value is passed, the tag is located and deleted based on the key.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    POST https://{endpoint}/v1/{project_id}/csbs_backup_policy/{resource_id}/tags/action
    ```


-   Request body

    ```
    {
        "action": "create",
        "tags": [
            {
                "key": "key1",
                "value": "value1"
            },
            {
                "key": "key",
                "value": "value3"
            }
        ]
    }
    or
    {
        "action": "delete",
        "tags": [
            {
                "key": "key1",
                "value": "value1"
            },
            {
                "key": "key2",
                "value": "value3"
            }
        ]
    }
    ```


## Response<a name="section16196349"></a>

-   Parameter description

None

## Status Codes<a name="section11549419"></a>

-   Normal

    <a name="table57318483"></a>
    <table><thead align="left"><tr id="row30670568"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p1288086"><a name="p1288086"></a><a name="p1288086"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p37226181"><a name="p37226181"></a><a name="p37226181"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row62530717"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p31823301"><a name="p31823301"></a><a name="p31823301"></a>204</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p27550565"><a name="p27550565"></a><a name="p27550565"></a>No Content</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    <a name="table17003302"></a>
    <table><thead align="left"><tr id="row12296056"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p56456478"><a name="p56456478"></a><a name="p56456478"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p9571976"><a name="p9571976"></a><a name="p9571976"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row37132574"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p54948554"><a name="p54948554"></a><a name="p54948554"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p21647857"><a name="p21647857"></a><a name="p21647857"></a>Invalid action.</p>
    </td>
    </tr>
    <tr id="row60612991"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p10705261"><a name="p10705261"></a><a name="p10705261"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p61819787"><a name="p61819787"></a><a name="p61819787"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row19507171"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p36577037"><a name="p36577037"></a><a name="p36577037"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p9950011"><a name="p9950011"></a><a name="p9950011"></a>You do not have permission to perform this operation.</p>
    </td>
    </tr>
    <tr id="row22441239"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p5801095"><a name="p5801095"></a><a name="p5801095"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p126704"><a name="p126704"></a><a name="p126704"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row1140337"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p25258433"><a name="p25258433"></a><a name="p25258433"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p32667165"><a name="p32667165"></a><a name="p32667165"></a>A system exception occurs.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section61541938486"></a>

For details, see  [Error Codes](error-codes.md).

