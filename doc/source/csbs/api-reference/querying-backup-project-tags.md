# Querying Backup Project Tags<a name="EN-US_TOPIC_0098635091"></a>

## Function<a name="section43678285"></a>

This API is used to query a tenant's tag set in a specific region and of a specific instance type.

TMS uses this API to list tags created by a tenant to facilitate tag creation and resource filtering on the console.

## URI<a name="section57560251"></a>

-   URI format

    GET https://\{endpoint\}/v1/\{project\_id\}/csbs\_backup/tags

-   Request header

    **Table  1**  Request header

    <a name="table57317854"></a>
    <table><thead align="left"><tr id="row16062491"><th class="cellrowborder" valign="top" width="24.752475247524753%" id="mcps1.2.5.1.1"><p id="p209623317216"><a name="p209623317216"></a><a name="p209623317216"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.2.5.1.2"><p id="p15962193221"><a name="p15962193221"></a><a name="p15962193221"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.2.5.1.3"><p id="p99783315213"><a name="p99783315213"></a><a name="p99783315213"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.54455445544555%" id="mcps1.2.5.1.4"><p id="p6978835213"><a name="p6978835213"></a><a name="p6978835213"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row18787345"><td class="cellrowborder" valign="top" width="24.752475247524753%" headers="mcps1.2.5.1.1 "><p id="p45380005"><a name="p45380005"></a><a name="p45380005"></a>Content-type</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.2 "><p id="p639019461246"><a name="p639019461246"></a><a name="p639019461246"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="p51901789"><a name="p51901789"></a><a name="p51901789"></a>MIME type of the body in the request</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.5.1.4 "><p id="p17266011"><a name="p17266011"></a><a name="p17266011"></a>application/json</p>
    </td>
    </tr>
    <tr id="row21176375"><td class="cellrowborder" valign="top" width="24.752475247524753%" headers="mcps1.2.5.1.1 "><p id="p37564794"><a name="p37564794"></a><a name="p37564794"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.2 "><p id="p14388146944"><a name="p14388146944"></a><a name="p14388146944"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="p22849445"><a name="p22849445"></a><a name="p22849445"></a>User token</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.5.1.4 "><p id="p61118933"><a name="p61118933"></a><a name="p61118933"></a>-</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Parameter description

    **Table  2**  Parameter description

    <a name="table31437385"></a>
    <table><thead align="left"><tr id="row54135154"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p131182811236"><a name="p131182811236"></a><a name="p131182811236"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p412281238"><a name="p412281238"></a><a name="p412281238"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p191192822317"><a name="p191192822317"></a><a name="p191192822317"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="p1217928162315"><a name="p1217928162315"></a><a name="p1217928162315"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row29261955"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p21408163"><a name="p21408163"></a><a name="p21408163"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p56339623"><a name="p56339623"></a><a name="p56339623"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p106744"><a name="p106744"></a><a name="p106744"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p65779720"><a name="p65779720"></a><a name="p65779720"></a>Project ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section48280214"></a>

-   Parameter description

    None


-   Example request

    ```
    GET https://{endpoint}/v1/{project_id}/csbs_backup/tags
    ```


## Response<a name="section31868743"></a>

-   Parameter description

    **Table  3**  Parameter description

    <a name="table22647000"></a>
    <table><thead align="left"><tr id="row39481153"><th class="cellrowborder" valign="top" width="29.409999999999997%" id="mcps1.2.4.1.1"><p id="p111763222313"><a name="p111763222313"></a><a name="p111763222313"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.470000000000002%" id="mcps1.2.4.1.2"><p id="p517153214237"><a name="p517153214237"></a><a name="p517153214237"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="54.120000000000005%" id="mcps1.2.4.1.3"><p id="p51773292320"><a name="p51773292320"></a><a name="p51773292320"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row14925917"><td class="cellrowborder" valign="top" width="29.409999999999997%" headers="mcps1.2.4.1.1 "><p id="p1039755"><a name="p1039755"></a><a name="p1039755"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.2.4.1.2 "><p id="p17111334"><a name="p17111334"></a><a name="p17111334"></a>List&lt;tag&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.120000000000005%" headers="mcps1.2.4.1.3 "><p id="p43840789"><a name="p43840789"></a><a name="p43840789"></a>Tag list</p>
    <p id="p35151347750"><a name="p35151347750"></a><a name="p35151347750"></a>Keys in the tag list must be unique.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **tag**

    **Table  4**  Parameter description of field  **tag**

    <a name="table61443009"></a>
    <table><thead align="left"><tr id="row39972798"><th class="cellrowborder" valign="top" width="29.409999999999997%" id="mcps1.2.4.1.1"><p id="p434518458234"><a name="p434518458234"></a><a name="p434518458234"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.470000000000002%" id="mcps1.2.4.1.2"><p id="p3345144562316"><a name="p3345144562316"></a><a name="p3345144562316"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="54.120000000000005%" id="mcps1.2.4.1.3"><p id="p33451245132318"><a name="p33451245132318"></a><a name="p33451245132318"></a>Description</p>
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
    <td class="cellrowborder" valign="top" width="54.120000000000005%" headers="mcps1.2.4.1.3 "><p id="p22942434"><a name="p22942434"></a><a name="p22942434"></a>List of tag values.</p>
    <p id="p8808725135910"><a name="p8808725135910"></a><a name="p8808725135910"></a>It consists of up to 43 characters.</p>
    <p id="p919321595"><a name="p919321595"></a><a name="p919321595"></a>It can be an empty string.</p>
    <p id="p163811127183219"><a name="p163811127183219"></a><a name="p163811127183219"></a>It can contain only letters, digits, hyphens (-), and underscores (_).</p>
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


## Status Codes<a name="section18383231"></a>

-   Normal

    <a name="table813059"></a>
    <table><thead align="left"><tr id="row27516461"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p14240860"><a name="p14240860"></a><a name="p14240860"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p12659036"><a name="p12659036"></a><a name="p12659036"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row18749013"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p42275054"><a name="p42275054"></a><a name="p42275054"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p1727311"><a name="p1727311"></a><a name="p1727311"></a>OK</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    <a name="table5694497"></a>
    <table><thead align="left"><tr id="row38964203"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p1983898"><a name="p1983898"></a><a name="p1983898"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p26478045"><a name="p26478045"></a><a name="p26478045"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row64346909"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p44717121"><a name="p44717121"></a><a name="p44717121"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p65317042"><a name="p65317042"></a><a name="p65317042"></a>Invalid parameters.</p>
    </td>
    </tr>
    <tr id="row50982466"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p35939088"><a name="p35939088"></a><a name="p35939088"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p25385055"><a name="p25385055"></a><a name="p25385055"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row27138911"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p50768145"><a name="p50768145"></a><a name="p50768145"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p18579096"><a name="p18579096"></a><a name="p18579096"></a>You do not have permission to perform this operation.</p>
    </td>
    </tr>
    <tr id="row32994143"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p55279936"><a name="p55279936"></a><a name="p55279936"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p48489833"><a name="p48489833"></a><a name="p48489833"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row33755321"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p49826466"><a name="p49826466"></a><a name="p49826466"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p9411944"><a name="p9411944"></a><a name="p9411944"></a>A system exception occurs.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section61541938486"></a>

For details, see  [Error Codes](error-codes.md).

