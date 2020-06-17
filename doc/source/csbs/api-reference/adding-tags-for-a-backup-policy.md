# Adding Tags for a Backup Policy<a name="EN-US_TOPIC_0098635094"></a>

## Function<a name="section663215"></a>

A resource can have up to 10 tags.

The API is idempotent.

If a to-be-created tag has the same key as an existing tag, the tag will be created and overwrite the existing one.

## URI<a name="section5968939"></a>

-   URI format

    POST https://\{endpoint\}/v1/\{project\_id\}/csbs\_backup\_policy/\{resource\_id\}/tags

-   Request header

    **Table  1**  Request header

    <a name="table12695920"></a>
    <table><thead align="left"><tr id="row324668"><th class="cellrowborder" valign="top" width="24.752475247524753%" id="mcps1.2.5.1.1"><p id="p209623317216"><a name="p209623317216"></a><a name="p209623317216"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.2.5.1.2"><p id="p15962193221"><a name="p15962193221"></a><a name="p15962193221"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.2.5.1.3"><p id="p99783315213"><a name="p99783315213"></a><a name="p99783315213"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.54455445544555%" id="mcps1.2.5.1.4"><p id="p6978835213"><a name="p6978835213"></a><a name="p6978835213"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row35224963"><td class="cellrowborder" valign="top" width="24.752475247524753%" headers="mcps1.2.5.1.1 "><p id="p34649765"><a name="p34649765"></a><a name="p34649765"></a>Content-type</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.2 "><p id="p10902133220614"><a name="p10902133220614"></a><a name="p10902133220614"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="p55167604"><a name="p55167604"></a><a name="p55167604"></a>MIME type of the body in the request</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.5.1.4 "><p id="p36549175"><a name="p36549175"></a><a name="p36549175"></a>application/json</p>
    </td>
    </tr>
    <tr id="row60507121"><td class="cellrowborder" valign="top" width="24.752475247524753%" headers="mcps1.2.5.1.1 "><p id="p2129750"><a name="p2129750"></a><a name="p2129750"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.2 "><p id="p119005323616"><a name="p119005323616"></a><a name="p119005323616"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="p38292076"><a name="p38292076"></a><a name="p38292076"></a>User token</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.5.1.4 "><p id="p45836489"><a name="p45836489"></a><a name="p45836489"></a>-</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Parameter description

    **Table  2**  Parameter description

    <a name="table18390601"></a>
    <table><thead align="left"><tr id="row7035667"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p1245682610254"><a name="p1245682610254"></a><a name="p1245682610254"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p12456152615256"><a name="p12456152615256"></a><a name="p12456152615256"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p20456152682512"><a name="p20456152682512"></a><a name="p20456152682512"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="p2456122642515"><a name="p2456122642515"></a><a name="p2456122642515"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row60784581"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p24604028"><a name="p24604028"></a><a name="p24604028"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p46769243"><a name="p46769243"></a><a name="p46769243"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p30212363"><a name="p30212363"></a><a name="p30212363"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p65779720"><a name="p65779720"></a><a name="p65779720"></a>Project ID</p>
    </td>
    </tr>
    <tr id="row41882373"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p37029065"><a name="p37029065"></a><a name="p37029065"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p46564252"><a name="p46564252"></a><a name="p46564252"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p13608105"><a name="p13608105"></a><a name="p13608105"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p28514710"><a name="p28514710"></a><a name="p28514710"></a>Resource ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section53720453"></a>

-   Parameter description

    **Table  3**  Parameter description

    <a name="table47570623"></a>
    <table><thead align="left"><tr id="row40977906"><th class="cellrowborder" valign="top" width="25.252525252525253%" id="mcps1.2.5.1.1"><p id="p15769330112512"><a name="p15769330112512"></a><a name="p15769330112512"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.2.5.1.2"><p id="p117692030142515"><a name="p117692030142515"></a><a name="p117692030142515"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.2.5.1.3"><p id="p27697305250"><a name="p27697305250"></a><a name="p27697305250"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.46464646464647%" id="mcps1.2.5.1.4"><p id="p4769153092519"><a name="p4769153092519"></a><a name="p4769153092519"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row57980147"><td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.2.5.1.1 "><p id="p65880360"><a name="p65880360"></a><a name="p65880360"></a>tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.2 "><p id="p34708966"><a name="p34708966"></a><a name="p34708966"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.3 "><p id="p59962836"><a name="p59962836"></a><a name="p59962836"></a>tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.46464646464647%" headers="mcps1.2.5.1.4 "><p id="p25151514"><a name="p25151514"></a><a name="p25151514"></a>List of included tags. Backup resource instances with these tags will be filtered.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **tag**

    **Table  4**  Parameter description of field  **tag**

    <a name="table24006753"></a>
    <table><thead align="left"><tr id="row22527890"><th class="cellrowborder" valign="top" width="25.742574257425744%" id="mcps1.2.5.1.1"><p id="p4957332182518"><a name="p4957332182518"></a><a name="p4957332182518"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.2.5.1.2"><p id="p9957632162511"><a name="p9957632162511"></a><a name="p9957632162511"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.2.5.1.3"><p id="p209575323251"><a name="p209575323251"></a><a name="p209575323251"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.54455445544555%" id="mcps1.2.5.1.4"><p id="p495723218252"><a name="p495723218252"></a><a name="p495723218252"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row53989823"><td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.5.1.1 "><p id="p11099566"><a name="p11099566"></a><a name="p11099566"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.2 "><p id="p26649649"><a name="p26649649"></a><a name="p26649649"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.3 "><p id="p11137969"><a name="p11137969"></a><a name="p11137969"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.5.1.4 "><p id="p798643483310"><a name="p798643483310"></a><a name="p798643483310"></a>Tag key</p>
    <p id="p036816391334"><a name="p036816391334"></a><a name="p036816391334"></a>It consists of up to 36 characters.</p>
    <p id="p1815945343312"><a name="p1815945343312"></a><a name="p1815945343312"></a>It cannot be an empty string.</p>
    <p id="p139819543334"><a name="p139819543334"></a><a name="p139819543334"></a>Spaces before and after a key will be deprecated.</p>
    <p id="p14766132412516"><a name="p14766132412516"></a><a name="p14766132412516"></a>It can contain only letters, digits, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    <tr id="row66515904"><td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.5.1.1 "><p id="p19079158"><a name="p19079158"></a><a name="p19079158"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.2 "><p id="p1907972"><a name="p1907972"></a><a name="p1907972"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.3 "><p id="p20328083"><a name="p20328083"></a><a name="p20328083"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.5.1.4 "><p id="p11608421163420"><a name="p11608421163420"></a><a name="p11608421163420"></a>Tag value</p>
    <p id="p489413816351"><a name="p489413816351"></a><a name="p489413816351"></a>It consists of up to 43 characters.</p>
    <p id="p14194717123517"><a name="p14194717123517"></a><a name="p14194717123517"></a>It can be an empty string.</p>
    <p id="p1146913338362"><a name="p1146913338362"></a><a name="p1146913338362"></a>Spaces before and after a tag value will be deprecated.</p>
    <p id="p13867418343"><a name="p13867418343"></a><a name="p13867418343"></a>It can contain only letters, digits, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    POST https://{endpoint}/v1/{project_id}/csbs_backup_policy/{resource_id}/tags
    ```


-   Request body

    ```
    {
        "tag":
        {
            "key":"DEV",
            "value":"DEV1"
        }
    }
    ```


## Status Codes<a name="section13722030"></a>

-   Normal

    <a name="table51926520"></a>
    <table><thead align="left"><tr id="row5115727"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p11720763"><a name="p11720763"></a><a name="p11720763"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p9857780"><a name="p9857780"></a><a name="p9857780"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row60282721"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p51062251"><a name="p51062251"></a><a name="p51062251"></a>204</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p42401657"><a name="p42401657"></a><a name="p42401657"></a>No Content</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    <a name="table11982196"></a>
    <table><thead align="left"><tr id="row7949639"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p39940984"><a name="p39940984"></a><a name="p39940984"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p13994266"><a name="p13994266"></a><a name="p13994266"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row59793748"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p11455439"><a name="p11455439"></a><a name="p11455439"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p55475379"><a name="p55475379"></a><a name="p55475379"></a>Invalid action.</p>
    </td>
    </tr>
    <tr id="row29516363"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p42015198"><a name="p42015198"></a><a name="p42015198"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p47787886"><a name="p47787886"></a><a name="p47787886"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row27437792"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p7868661"><a name="p7868661"></a><a name="p7868661"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p33381819"><a name="p33381819"></a><a name="p33381819"></a>You do not have permission to perform this operation.</p>
    </td>
    </tr>
    <tr id="row32000920"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p41937705"><a name="p41937705"></a><a name="p41937705"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p41510976"><a name="p41510976"></a><a name="p41510976"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row38054464"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p62512728"><a name="p62512728"></a><a name="p62512728"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p30366184"><a name="p30366184"></a><a name="p30366184"></a>A system exception occurs.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section61541938486"></a>

For details, see  [Error Codes](error-codes.md).

