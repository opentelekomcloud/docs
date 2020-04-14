# Querying the Project Tags of a Backup Policy<a name="EN-US_TOPIC_0098635097"></a>

## Function<a name="section66080062"></a>

This API is used to query a tenant's tag set in a specific region and of a specific instance type.

TMS uses this API to list tags created by a tenant to facilitate tag creation and resource filtering on the console.

## URI<a name="section57849650"></a>

-   URI format

    GET https://\{endpoint\}/v1/\{project\_id\}/csbs\_backup\_policy/tags

-   Request header

    **Table  1**  Request header

    <a name="table2166929"></a>
    <table><thead align="left"><tr id="row65022077"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p209623317216"><a name="p209623317216"></a><a name="p209623317216"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p15962193221"><a name="p15962193221"></a><a name="p15962193221"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p99783315213"><a name="p99783315213"></a><a name="p99783315213"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="p6978835213"><a name="p6978835213"></a><a name="p6978835213"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6053677"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p20585813"><a name="p20585813"></a><a name="p20585813"></a>Content-type</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p33411215287"><a name="p33411215287"></a><a name="p33411215287"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p56838133"><a name="p56838133"></a><a name="p56838133"></a>MIME type of the body in the request</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p58146239"><a name="p58146239"></a><a name="p58146239"></a>application/json</p>
    </td>
    </tr>
    <tr id="row53554111"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p42915720"><a name="p42915720"></a><a name="p42915720"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p233917151284"><a name="p233917151284"></a><a name="p233917151284"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p53621294"><a name="p53621294"></a><a name="p53621294"></a>User token</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p24645678"><a name="p24645678"></a><a name="p24645678"></a>-</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Parameter description

    **Table  2**  Parameter description

    <a name="table46979855"></a>
    <table><thead align="left"><tr id="row34292765"><th class="cellrowborder" valign="top" width="25.252525252525253%" id="mcps1.2.5.1.1"><p id="p16803133832618"><a name="p16803133832618"></a><a name="p16803133832618"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.151515151515152%" id="mcps1.2.5.1.2"><p id="p1380316381266"><a name="p1380316381266"></a><a name="p1380316381266"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.2.5.1.3"><p id="p281913872612"><a name="p281913872612"></a><a name="p281913872612"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.45454545454546%" id="mcps1.2.5.1.4"><p id="p5819103802617"><a name="p5819103802617"></a><a name="p5819103802617"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4089365"><td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.2.5.1.1 "><p id="p62803112"><a name="p62803112"></a><a name="p62803112"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.2 "><p id="p53887349"><a name="p53887349"></a><a name="p53887349"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.3 "><p id="p2799138"><a name="p2799138"></a><a name="p2799138"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.5.1.4 "><p id="p65779720"><a name="p65779720"></a><a name="p65779720"></a>Project ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section50884809"></a>

-   Parameter description

None

-   Example request

    ```
    GET https://{endpoint}/v1/{project_id}/csbs_backup_policy/tags
    ```


## Response<a name="section55310098"></a>

-   Parameter description

    **Table  3**  Parameter description

    <a name="table22647000"></a>
    <table><thead align="left"><tr id="row39481153"><th class="cellrowborder" valign="top" width="29.409999999999997%" id="mcps1.2.4.1.1"><p id="p167251543142614"><a name="p167251543142614"></a><a name="p167251543142614"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.470000000000002%" id="mcps1.2.4.1.2"><p id="p172574302613"><a name="p172574302613"></a><a name="p172574302613"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="54.120000000000005%" id="mcps1.2.4.1.3"><p id="p197251743132614"><a name="p197251743132614"></a><a name="p197251743132614"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row14925917"><td class="cellrowborder" valign="top" width="29.409999999999997%" headers="mcps1.2.4.1.1 "><p id="p1039755"><a name="p1039755"></a><a name="p1039755"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.2.4.1.2 "><p id="p17111334"><a name="p17111334"></a><a name="p17111334"></a>List&lt;tag&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.120000000000005%" headers="mcps1.2.4.1.3 "><p id="p43840789"><a name="p43840789"></a><a name="p43840789"></a>Tag list</p>
    <p id="p10226451664"><a name="p10226451664"></a><a name="p10226451664"></a>Keys in the tag list must be unique.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **tag**

    **Table  4**  Parameter description of field  **tag**

    <a name="table61443009"></a>
    <table><thead align="left"><tr id="row39972798"><th class="cellrowborder" valign="top" width="29.409999999999997%" id="mcps1.2.4.1.1"><p id="p534912527262"><a name="p534912527262"></a><a name="p534912527262"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.470000000000002%" id="mcps1.2.4.1.2"><p id="p183491152122620"><a name="p183491152122620"></a><a name="p183491152122620"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="54.120000000000005%" id="mcps1.2.4.1.3"><p id="p163498528263"><a name="p163498528263"></a><a name="p163498528263"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row9701936"><td class="cellrowborder" valign="top" width="29.409999999999997%" headers="mcps1.2.4.1.1 "><p id="p47659360"><a name="p47659360"></a><a name="p47659360"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.2.4.1.2 "><p id="p35202932"><a name="p35202932"></a><a name="p35202932"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.120000000000005%" headers="mcps1.2.4.1.3 "><p id="p32865237"><a name="p32865237"></a><a name="p32865237"></a>Tag key</p>
    <p id="p7327206587"><a name="p7327206587"></a><a name="p7327206587"></a>It consists of up to 36 characters.</p>
    <p id="p145821075819"><a name="p145821075819"></a><a name="p145821075819"></a>It cannot be an empty string.</p>
    <p id="p14766132412516"><a name="p14766132412516"></a><a name="p14766132412516"></a>It can contain only letters, digits, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    <tr id="row27351677"><td class="cellrowborder" valign="top" width="29.409999999999997%" headers="mcps1.2.4.1.1 "><p id="p893371"><a name="p893371"></a><a name="p893371"></a>values</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.2.4.1.2 "><p id="p5254266"><a name="p5254266"></a><a name="p5254266"></a>List&lt;String&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.120000000000005%" headers="mcps1.2.4.1.3 "><p id="p22942434"><a name="p22942434"></a><a name="p22942434"></a>List of tag values</p>
    <p id="p8808725135910"><a name="p8808725135910"></a><a name="p8808725135910"></a>It consists of up to 43 characters.</p>
    <p id="p919321595"><a name="p919321595"></a><a name="p919321595"></a>It can be an empty string.</p>
    <p id="p521018152360"><a name="p521018152360"></a><a name="p521018152360"></a>It can contain only letters, digits, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

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


## Status Codes<a name="section28028840"></a>

-   Normal

    <a name="table7092825"></a>
    <table><thead align="left"><tr id="row64957389"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p27057175"><a name="p27057175"></a><a name="p27057175"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p44147557"><a name="p44147557"></a><a name="p44147557"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row19182368"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p10267951"><a name="p10267951"></a><a name="p10267951"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p26397691"><a name="p26397691"></a><a name="p26397691"></a>OK</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    <a name="table57838187"></a>
    <table><thead align="left"><tr id="row49915680"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p16638299"><a name="p16638299"></a><a name="p16638299"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p5524991"><a name="p5524991"></a><a name="p5524991"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row44871090"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p10679711"><a name="p10679711"></a><a name="p10679711"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p59750252"><a name="p59750252"></a><a name="p59750252"></a>Invalid parameters.</p>
    </td>
    </tr>
    <tr id="row881358"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p4281167"><a name="p4281167"></a><a name="p4281167"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p11230212"><a name="p11230212"></a><a name="p11230212"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row33963045"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p66652164"><a name="p66652164"></a><a name="p66652164"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p30116236"><a name="p30116236"></a><a name="p30116236"></a>You do not have permission to perform this operation.</p>
    </td>
    </tr>
    <tr id="row2610670"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p10137733"><a name="p10137733"></a><a name="p10137733"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p15850073"><a name="p15850073"></a><a name="p15850073"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row8432933"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p11978974"><a name="p11978974"></a><a name="p11978974"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p30772872"><a name="p30772872"></a><a name="p30772872"></a>A system exception occurs.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section61541938486"></a>

For details, see  [Error Codes](error-codes.md).

