# Batch Adding or Deleting Tags of a Backup Resource<a name="EN-US_TOPIC_0098635087"></a>

## Function<a name="section42185888"></a>

This API is used to add or delete tags of a specific instance in batches.

The TMS may use this API to manage service resource tags.

A resource can have up to 10 tags.

The API is idempotent.

If there are duplicate keys in the request body when you add tags, an error is reported.

If the key of the to-be-created tag is the same as that of an existing tag, the value of the existing tag will be overwritten.

When deleting tags, you can upload duplicate keys.

When tags are being deleted and some tags do not exist, the operation is considered successful by default, and the character set of the tags will not be checked upon deletion. A key and a value can respectively consist of up to 127 and 255 characters. The tag structure cannot be missing, and the key cannot be left blank or an empty string.

## URI<a name="section44128673"></a>

-   URI format

    POST https://\{endpoint\}/v1/\{project\_id\}/csbs\_backup/\{resource\_id\}/tags/action

-   Request header

    **Table  1**  Request header

    <a name="table25360113"></a>
    <table><thead align="left"><tr id="row47522535"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p209623317216"><a name="p209623317216"></a><a name="p209623317216"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p15962193221"><a name="p15962193221"></a><a name="p15962193221"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p99783315213"><a name="p99783315213"></a><a name="p99783315213"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="p6978835213"><a name="p6978835213"></a><a name="p6978835213"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row57706137"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p43685501"><a name="p43685501"></a><a name="p43685501"></a>Content-type</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p673312391953"><a name="p673312391953"></a><a name="p673312391953"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p48864686"><a name="p48864686"></a><a name="p48864686"></a>MIME type of the body in the request</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p22161940"><a name="p22161940"></a><a name="p22161940"></a>application/json</p>
    </td>
    </tr>
    <tr id="row65239739"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p49927539"><a name="p49927539"></a><a name="p49927539"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p47311539957"><a name="p47311539957"></a><a name="p47311539957"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p17598843"><a name="p17598843"></a><a name="p17598843"></a>User token</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p38764188"><a name="p38764188"></a><a name="p38764188"></a>-</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Parameter description

    **Table  2**  Parameter description

    <a name="table37434462"></a>
    <table><thead align="left"><tr id="row15090892"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p1539025782119"><a name="p1539025782119"></a><a name="p1539025782119"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.2"><p id="p4390165712120"><a name="p4390165712120"></a><a name="p4390165712120"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p10390257132116"><a name="p10390257132116"></a><a name="p10390257132116"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="p10390175712116"><a name="p10390175712116"></a><a name="p10390175712116"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row23205303"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p581351"><a name="p581351"></a><a name="p581351"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p47089443"><a name="p47089443"></a><a name="p47089443"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p56148564"><a name="p56148564"></a><a name="p56148564"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p65779720"><a name="p65779720"></a><a name="p65779720"></a>Project ID</p>
    </td>
    </tr>
    <tr id="row46927178"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p43005067"><a name="p43005067"></a><a name="p43005067"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p60858368"><a name="p60858368"></a><a name="p60858368"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p30580753"><a name="p30580753"></a><a name="p30580753"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p61121960"><a name="p61121960"></a><a name="p61121960"></a>Resource ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section61613739"></a>

-   Parameter description

    **Table  3**  Parameter description

    <a name="table45717377"></a>
    <table><thead align="left"><tr id="row30003108"><th class="cellrowborder" valign="top" width="26%" id="mcps1.2.5.1.1"><p id="p1560890112210"><a name="p1560890112210"></a><a name="p1560890112210"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p14624503220"><a name="p14624503220"></a><a name="p14624503220"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p062430182214"><a name="p062430182214"></a><a name="p062430182214"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="p46241806224"><a name="p46241806224"></a><a name="p46241806224"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8943813"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.5.1.1 "><p id="p53360282"><a name="p53360282"></a><a name="p53360282"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p27215608"><a name="p27215608"></a><a name="p27215608"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p56980614"><a name="p56980614"></a><a name="p56980614"></a>List&lt;resource_tag&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p9244511113310"><a name="p9244511113310"></a><a name="p9244511113310"></a>Tag list</p>
    <p id="p52026988"><a name="p52026988"></a><a name="p52026988"></a>This list cannot be an empty list.</p>
    <p id="p183916535015"><a name="p183916535015"></a><a name="p183916535015"></a>The list can contain up to 10 keys.</p>
    <p id="p1338589319"><a name="p1338589319"></a><a name="p1338589319"></a>Keys in this list must be unique.</p>
    </td>
    </tr>
    <tr id="row65589712"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.5.1.1 "><p id="p11166446"><a name="p11166446"></a><a name="p11166446"></a>action</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p32066937"><a name="p32066937"></a><a name="p32066937"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p47285080"><a name="p47285080"></a><a name="p47285080"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p4886260"><a name="p4886260"></a><a name="p4886260"></a>Operation to be performed. The value can be set to <strong id="b171091221113413"><a name="b171091221113413"></a><a name="b171091221113413"></a>create</strong> or <strong id="b181101021133414"><a name="b181101021133414"></a><a name="b181101021133414"></a>delete</strong> only.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **resource\_tag**

    **Table  4**  Parameter description of field  **resource\_tag**

    <a name="table60242740"></a>
    <table><thead align="left"><tr id="row3310428"><th class="cellrowborder" valign="top" width="26%" id="mcps1.2.5.1.1"><p id="p16688435228"><a name="p16688435228"></a><a name="p16688435228"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p2688153132219"><a name="p2688153132219"></a><a name="p2688153132219"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p196889312219"><a name="p196889312219"></a><a name="p196889312219"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="p56882382220"><a name="p56882382220"></a><a name="p56882382220"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row36890322"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.5.1.1 "><p id="p35326120"><a name="p35326120"></a><a name="p35326120"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p42843478"><a name="p42843478"></a><a name="p42843478"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p47769733"><a name="p47769733"></a><a name="p47769733"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p798643483310"><a name="p798643483310"></a><a name="p798643483310"></a>Tag key (when <strong id="b842352706211644"><a name="b842352706211644"></a><a name="b842352706211644"></a>action</strong> is set to <strong id="b842352706211650"><a name="b842352706211650"></a><a name="b842352706211650"></a>create</strong>)</p>
    <p id="p036816391334"><a name="p036816391334"></a><a name="p036816391334"></a>It consists of up to 36 characters.</p>
    <p id="p1815945343312"><a name="p1815945343312"></a><a name="p1815945343312"></a>It cannot be an empty string.</p>
    <p id="p139819543334"><a name="p139819543334"></a><a name="p139819543334"></a>Spaces before and after a key will be deprecated.</p>
    <p id="p17111023202916"><a name="p17111023202916"></a><a name="p17111023202916"></a>It can contain only letters, digits, hyphens (-), and underscores (_).</p>
    <p id="p4208458163611"><a name="p4208458163611"></a><a name="p4208458163611"></a>Tag key (when <strong id="b757515724"><a name="b757515724"></a><a name="b757515724"></a>action</strong> is set to <strong id="b481666846"><a name="b481666846"></a><a name="b481666846"></a>delete</strong>)</p>
    <p id="p1165515448375"><a name="p1165515448375"></a><a name="p1165515448375"></a>It consists of up to 127 characters.</p>
    <p id="p289271163811"><a name="p289271163811"></a><a name="p289271163811"></a>It cannot be an empty string.</p>
    <p id="p136318151388"><a name="p136318151388"></a><a name="p136318151388"></a>Spaces before and after a key will be deprecated.</p>
    </td>
    </tr>
    <tr id="row61744455"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.5.1.1 "><p id="p35244974"><a name="p35244974"></a><a name="p35244974"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p36270674"><a name="p36270674"></a><a name="p36270674"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p52243482"><a name="p52243482"></a><a name="p52243482"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p11608421163420"><a name="p11608421163420"></a><a name="p11608421163420"></a>Tag value (when <strong id="b1851769556"><a name="b1851769556"></a><a name="b1851769556"></a>action</strong> is set to <strong id="b868886101"><a name="b868886101"></a><a name="b868886101"></a>create</strong>)</p>
    <p id="p17862829154114"><a name="p17862829154114"></a><a name="p17862829154114"></a>This parameter is mandatory.</p>
    <p id="p489413816351"><a name="p489413816351"></a><a name="p489413816351"></a>It consists of up to 43 characters.</p>
    <p id="p14194717123517"><a name="p14194717123517"></a><a name="p14194717123517"></a>It can be an empty string.</p>
    <p id="p1146913338362"><a name="p1146913338362"></a><a name="p1146913338362"></a>Spaces before and after a tag value will be deprecated.</p>
    <p id="p14766132412516"><a name="p14766132412516"></a><a name="p14766132412516"></a>It can contain only letters, digits, hyphens (-), and underscores (_).</p>
    <p id="p239755173813"><a name="p239755173813"></a><a name="p239755173813"></a>Tag value (when <strong id="b2108824033"><a name="b2108824033"></a><a name="b2108824033"></a>action</strong> is set to <strong id="b676827487"><a name="b676827487"></a><a name="b676827487"></a>delete</strong>)</p>
    <p id="p13546172617403"><a name="p13546172617403"></a><a name="p13546172617403"></a>The tag value can be passed or not.</p>
    <p id="p1923221093917"><a name="p1923221093917"></a><a name="p1923221093917"></a>It consists of up to 255 characters.</p>
    <p id="p1211002563912"><a name="p1211002563912"></a><a name="p1211002563912"></a>It can be an empty string.</p>
    <p id="p7821195193918"><a name="p7821195193918"></a><a name="p7821195193918"></a>Spaces before and after a tag value will be deprecated.</p>
    <p id="p1331333124318"><a name="p1331333124318"></a><a name="p1331333124318"></a>If the value is not passed, the tag is located and deleted based on the key and value. If the value is passed, the tag is located and deleted based on the key.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    POST https://{endpoint}/v1/{project_id}/csbs_backup/{resource_id}/tags/action
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


## Response<a name="section24656967"></a>

-   Parameter description

None

## Status Codes<a name="section20586115"></a>

-   Normal

    <a name="table59352792"></a>
    <table><thead align="left"><tr id="row29757668"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p61560901"><a name="p61560901"></a><a name="p61560901"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p20377050"><a name="p20377050"></a><a name="p20377050"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row39928331"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p12969410"><a name="p12969410"></a><a name="p12969410"></a>204</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p43889252"><a name="p43889252"></a><a name="p43889252"></a>No Content</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    <a name="table65368539"></a>
    <table><thead align="left"><tr id="row46378660"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p65684014"><a name="p65684014"></a><a name="p65684014"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p18804945"><a name="p18804945"></a><a name="p18804945"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row46805556"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p33153663"><a name="p33153663"></a><a name="p33153663"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p1092187"><a name="p1092187"></a><a name="p1092187"></a>Invalid action.</p>
    </td>
    </tr>
    <tr id="row9829687"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p58007150"><a name="p58007150"></a><a name="p58007150"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p958730"><a name="p958730"></a><a name="p958730"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row8628578"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p27826192"><a name="p27826192"></a><a name="p27826192"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p39329046"><a name="p39329046"></a><a name="p39329046"></a>You do not have permission to perform this operation.</p>
    </td>
    </tr>
    <tr id="row18417098"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p15389960"><a name="p15389960"></a><a name="p15389960"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p38627251"><a name="p38627251"></a><a name="p38627251"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row12100940"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p40652101"><a name="p40652101"></a><a name="p40652101"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p4485854"><a name="p4485854"></a><a name="p4485854"></a>A system exception occurs.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section61541938486"></a>

For details, see  [Error Codes](error-codes.md).

