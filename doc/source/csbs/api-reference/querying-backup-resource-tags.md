# Querying Backup Resource Tags<a name="EN-US_TOPIC_0098635090"></a>

## Function<a name="section27585226"></a>

This API is used to query tags of a specific instance.

TMS uses this API to query all tags of a specific instance.

## URI<a name="section46940446"></a>

-   URI format

    GET https://\{endpoint\}/v1/\{project\_id\}/csbs\_backup/\{resource\_id\}/tags

-   Request header

    **Table  1**  Request header

    <a name="table43153461"></a>
    <table><thead align="left"><tr id="row36921673"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p209623317216"><a name="p209623317216"></a><a name="p209623317216"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="p15962193221"><a name="p15962193221"></a><a name="p15962193221"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.3"><p id="p99783315213"><a name="p99783315213"></a><a name="p99783315213"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="p6978835213"><a name="p6978835213"></a><a name="p6978835213"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5888712"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p7223683"><a name="p7223683"></a><a name="p7223683"></a>Content-type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p11602195813417"><a name="p11602195813417"></a><a name="p11602195813417"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p48247463"><a name="p48247463"></a><a name="p48247463"></a>MIME type of the body in the request</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p66202439"><a name="p66202439"></a><a name="p66202439"></a>application/json</p>
    </td>
    </tr>
    <tr id="row58951042"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p10305078"><a name="p10305078"></a><a name="p10305078"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p176017582416"><a name="p176017582416"></a><a name="p176017582416"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p29404983"><a name="p29404983"></a><a name="p29404983"></a>User token</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p55218749"><a name="p55218749"></a><a name="p55218749"></a>-</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Parameter description

    **Table  2**  Parameter description

    <a name="table60695180"></a>
    <table><thead align="left"><tr id="row17600446"><th class="cellrowborder" valign="top" width="26%" id="mcps1.2.5.1.1"><p id="p1182916596221"><a name="p1182916596221"></a><a name="p1182916596221"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.2"><p id="p1282965922217"><a name="p1282965922217"></a><a name="p1282965922217"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p4829165962220"><a name="p4829165962220"></a><a name="p4829165962220"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="p1382965916225"><a name="p1382965916225"></a><a name="p1382965916225"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row23907896"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.5.1.1 "><p id="p57491423"><a name="p57491423"></a><a name="p57491423"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p26293678"><a name="p26293678"></a><a name="p26293678"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p49413198"><a name="p49413198"></a><a name="p49413198"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p65779720"><a name="p65779720"></a><a name="p65779720"></a>Project ID</p>
    </td>
    </tr>
    <tr id="row32248040"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.5.1.1 "><p id="p61954460"><a name="p61954460"></a><a name="p61954460"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p52255327"><a name="p52255327"></a><a name="p52255327"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p4823132"><a name="p4823132"></a><a name="p4823132"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p55129401"><a name="p55129401"></a><a name="p55129401"></a>Resource ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section19810832"></a>

-   Parameter description

    None


-   Example request

    ```
    GET https://{endpoint}/v1/{project_id}/csbs_backup/{resource_id}/tags
    ```


## Response<a name="section44079761"></a>

-   Parameter description

    **Table  3**  Parameter description

    <a name="table38104721"></a>
    <table><thead align="left"><tr id="row42994491"><th class="cellrowborder" valign="top" width="30.23%" id="mcps1.2.4.1.1"><p id="p1065802122318"><a name="p1065802122318"></a><a name="p1065802122318"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.2.4.1.2"><p id="p1867313282314"><a name="p1867313282314"></a><a name="p1867313282314"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.33%" id="mcps1.2.4.1.3"><p id="p186733215238"><a name="p186733215238"></a><a name="p186733215238"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row26228182"><td class="cellrowborder" valign="top" width="30.23%" headers="mcps1.2.4.1.1 "><p id="p44108002"><a name="p44108002"></a><a name="p44108002"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p15978406"><a name="p15978406"></a><a name="p15978406"></a>List&lt;resource_tag&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.33%" headers="mcps1.2.4.1.3 "><p id="p19182539"><a name="p19182539"></a><a name="p19182539"></a>Tag list</p>
    <p id="p8594239348"><a name="p8594239348"></a><a name="p8594239348"></a>Keys in the tag list must be unique.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **resource\_tag**

    **Table  4**  Parameter description of field  **resource\_tag**

    <a name="table10281849"></a>
    <table><thead align="left"><tr id="row58282180"><th class="cellrowborder" valign="top" width="29.409999999999997%" id="mcps1.2.4.1.1"><p id="p1447011814232"><a name="p1447011814232"></a><a name="p1447011814232"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.65%" id="mcps1.2.4.1.2"><p id="p64701185231"><a name="p64701185231"></a><a name="p64701185231"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.94%" id="mcps1.2.4.1.3"><p id="p17470138152311"><a name="p17470138152311"></a><a name="p17470138152311"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row65272389"><td class="cellrowborder" valign="top" width="29.409999999999997%" headers="mcps1.2.4.1.1 "><p id="p52572118"><a name="p52572118"></a><a name="p52572118"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.65%" headers="mcps1.2.4.1.2 "><p id="p30483160"><a name="p30483160"></a><a name="p30483160"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.94%" headers="mcps1.2.4.1.3 "><p id="p13925135105714"><a name="p13925135105714"></a><a name="p13925135105714"></a>Tag key</p>
    <p id="p7327206587"><a name="p7327206587"></a><a name="p7327206587"></a>It consists of up to 36 characters.</p>
    <p id="p145821075819"><a name="p145821075819"></a><a name="p145821075819"></a>It cannot be an empty string.</p>
    <p id="p14766132412516"><a name="p14766132412516"></a><a name="p14766132412516"></a>It can contain only letters, digits, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    <tr id="row9189896"><td class="cellrowborder" valign="top" width="29.409999999999997%" headers="mcps1.2.4.1.1 "><p id="p6184122"><a name="p6184122"></a><a name="p6184122"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.65%" headers="mcps1.2.4.1.2 "><p id="p31151897"><a name="p31151897"></a><a name="p31151897"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.94%" headers="mcps1.2.4.1.3 "><p id="p1966153512589"><a name="p1966153512589"></a><a name="p1966153512589"></a>Tag value</p>
    <p id="p8808725135910"><a name="p8808725135910"></a><a name="p8808725135910"></a>It consists of up to 43 characters.</p>
    <p id="p919321595"><a name="p919321595"></a><a name="p919321595"></a>It can be an empty string.</p>
    <p id="p151956616313"><a name="p151956616313"></a><a name="p151956616313"></a>It can contain only letters, digits, hyphens (-), and underscores (_).</p>
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
                "value": "value1"
            },
            {
                "key": "key2",
                "value": "value3"
            }
        ]
    }
    ```


## Status Codes<a name="section61173530"></a>

-   Normal

    <a name="table46245271"></a>
    <table><thead align="left"><tr id="row10252817"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p25171847"><a name="p25171847"></a><a name="p25171847"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p25653697"><a name="p25653697"></a><a name="p25653697"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row64683559"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p4876963"><a name="p4876963"></a><a name="p4876963"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p59489690"><a name="p59489690"></a><a name="p59489690"></a>OK</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    <a name="table53935606"></a>
    <table><thead align="left"><tr id="row58293474"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p24150953"><a name="p24150953"></a><a name="p24150953"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p10070168"><a name="p10070168"></a><a name="p10070168"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row10377304"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p35255313"><a name="p35255313"></a><a name="p35255313"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p37108074"><a name="p37108074"></a><a name="p37108074"></a>Invalid parameters.</p>
    </td>
    </tr>
    <tr id="row65537210"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p6913766"><a name="p6913766"></a><a name="p6913766"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p23144199"><a name="p23144199"></a><a name="p23144199"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row6971207"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p27796914"><a name="p27796914"></a><a name="p27796914"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p36957574"><a name="p36957574"></a><a name="p36957574"></a>You do not have permission to perform this operation.</p>
    </td>
    </tr>
    <tr id="row64182710"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p31417017"><a name="p31417017"></a><a name="p31417017"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p61750457"><a name="p61750457"></a><a name="p61750457"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row18883203"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p53144456"><a name="p53144456"></a><a name="p53144456"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p9733694"><a name="p9733694"></a><a name="p9733694"></a>A system exception occurs.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section61541938486"></a>

For details, see  [Error Codes](error-codes.md).

