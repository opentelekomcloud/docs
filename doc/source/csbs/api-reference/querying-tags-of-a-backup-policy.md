# Querying Tags of a Backup Policy<a name="EN-US_TOPIC_0098635096"></a>

## Function<a name="section50368838"></a>

This API is used to query tags of a specific instance.

TMS uses this API to query all tags of a specific instance.

## URI<a name="section50666366"></a>

-   URI format

    GET https://\{endpoint\}/v1/\{project\_id\}/csbs\_backup\_policy/\{resource\_id\}/tags

-   Request header

    **Table  1**  Request header

    <a name="table17897732"></a>
    <table><thead align="left"><tr id="row29912730"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p209623317216"><a name="p209623317216"></a><a name="p209623317216"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.2"><p id="p15962193221"><a name="p15962193221"></a><a name="p15962193221"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.3"><p id="p99783315213"><a name="p99783315213"></a><a name="p99783315213"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="34%" id="mcps1.2.5.1.4"><p id="p6978835213"><a name="p6978835213"></a><a name="p6978835213"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row42564588"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p25179629"><a name="p25179629"></a><a name="p25179629"></a>Content-type</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="p16198190187"><a name="p16198190187"></a><a name="p16198190187"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.3 "><p id="p26284107"><a name="p26284107"></a><a name="p26284107"></a>MIME type of the body in the request</p>
    </td>
    <td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.5.1.4 "><p id="p47358524"><a name="p47358524"></a><a name="p47358524"></a>application/json</p>
    </td>
    </tr>
    <tr id="row23573535"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p30408220"><a name="p30408220"></a><a name="p30408220"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="p181961807811"><a name="p181961807811"></a><a name="p181961807811"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.3 "><p id="p47146745"><a name="p47146745"></a><a name="p47146745"></a>User token</p>
    </td>
    <td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.5.1.4 "><p id="p25041524"><a name="p25041524"></a><a name="p25041524"></a>-</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Parameter description

    **Table  2**  Parameter description

    <a name="table275553"></a>
    <table><thead align="left"><tr id="row10635570"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p1011541116264"><a name="p1011541116264"></a><a name="p1011541116264"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p101311711112614"><a name="p101311711112614"></a><a name="p101311711112614"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p9131181117262"><a name="p9131181117262"></a><a name="p9131181117262"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p313120110264"><a name="p313120110264"></a><a name="p313120110264"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row16018178"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p22404047"><a name="p22404047"></a><a name="p22404047"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p2788537"><a name="p2788537"></a><a name="p2788537"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p24544935"><a name="p24544935"></a><a name="p24544935"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p65779720"><a name="p65779720"></a><a name="p65779720"></a>Project ID</p>
    </td>
    </tr>
    <tr id="row37269850"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p66067912"><a name="p66067912"></a><a name="p66067912"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p49900666"><a name="p49900666"></a><a name="p49900666"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p15422169"><a name="p15422169"></a><a name="p15422169"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p41236172"><a name="p41236172"></a><a name="p41236172"></a>Resource ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section53344112"></a>

-   Parameter description

    None


-   Example request

    ```
    GET https://{endpoint}/v1/{project_id}/csbs_backup_policy/{resource_id}/tags
    ```


## Response<a name="section10334967"></a>

-   Parameter description

    **Table  3**  Parameter description

    <a name="table38104721"></a>
    <table><thead align="left"><tr id="row42994491"><th class="cellrowborder" valign="top" width="30.23%" id="mcps1.2.4.1.1"><p id="p56621914152613"><a name="p56621914152613"></a><a name="p56621914152613"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.2.4.1.2"><p id="p1366220148267"><a name="p1366220148267"></a><a name="p1366220148267"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.33%" id="mcps1.2.4.1.3"><p id="p1366281418264"><a name="p1366281418264"></a><a name="p1366281418264"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row26228182"><td class="cellrowborder" valign="top" width="30.23%" headers="mcps1.2.4.1.1 "><p id="p44108002"><a name="p44108002"></a><a name="p44108002"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p15978406"><a name="p15978406"></a><a name="p15978406"></a>List&lt;resource_tag&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.33%" headers="mcps1.2.4.1.3 "><p id="p19182539"><a name="p19182539"></a><a name="p19182539"></a>Tag list</p>
    <p id="p13733391056"><a name="p13733391056"></a><a name="p13733391056"></a>Keys in the tag list must be unique.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **resource\_tag**

    **Table  4**  Parameter description of field  **resource\_tag**

    <a name="table61443009"></a>
    <table><thead align="left"><tr id="row39972798"><th class="cellrowborder" valign="top" width="29.409999999999997%" id="mcps1.2.4.1.1"><p id="p8569102142610"><a name="p8569102142610"></a><a name="p8569102142610"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.470000000000002%" id="mcps1.2.4.1.2"><p id="p456952122610"><a name="p456952122610"></a><a name="p456952122610"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="54.120000000000005%" id="mcps1.2.4.1.3"><p id="p14569112118269"><a name="p14569112118269"></a><a name="p14569112118269"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row9701936"><td class="cellrowborder" valign="top" width="29.409999999999997%" headers="mcps1.2.4.1.1 "><p id="p47659360"><a name="p47659360"></a><a name="p47659360"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.2.4.1.2 "><p id="p35202932"><a name="p35202932"></a><a name="p35202932"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.120000000000005%" headers="mcps1.2.4.1.3 "><p id="p13925135105714"><a name="p13925135105714"></a><a name="p13925135105714"></a>Tag key</p>
    <p id="p7327206587"><a name="p7327206587"></a><a name="p7327206587"></a>It consists of up to 36 characters.</p>
    <p id="p145821075819"><a name="p145821075819"></a><a name="p145821075819"></a>It cannot be an empty string.</p>
    <p id="p14766132412516"><a name="p14766132412516"></a><a name="p14766132412516"></a>It can contain only letters, digits, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    <tr id="row27351677"><td class="cellrowborder" valign="top" width="29.409999999999997%" headers="mcps1.2.4.1.1 "><p id="p893371"><a name="p893371"></a><a name="p893371"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.2.4.1.2 "><p id="p5254266"><a name="p5254266"></a><a name="p5254266"></a>List&lt;String&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.120000000000005%" headers="mcps1.2.4.1.3 "><p id="p1966153512589"><a name="p1966153512589"></a><a name="p1966153512589"></a>Tag value</p>
    <p id="p8808725135910"><a name="p8808725135910"></a><a name="p8808725135910"></a>It consists of up to 43 characters.</p>
    <p id="p919321595"><a name="p919321595"></a><a name="p919321595"></a>It can be an empty string.</p>
    <p id="p14697173411355"><a name="p14697173411355"></a><a name="p14697173411355"></a>It can contain only letters, digits, hyphens (-), and underscores (_).</p>
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


## Status Codes<a name="section25905843"></a>

-   Normal

    <a name="table34543924"></a>
    <table><thead align="left"><tr id="row10296933"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p28745279"><a name="p28745279"></a><a name="p28745279"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p46666290"><a name="p46666290"></a><a name="p46666290"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row21873125"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p26892672"><a name="p26892672"></a><a name="p26892672"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p30822828"><a name="p30822828"></a><a name="p30822828"></a>OK</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    <a name="table13621136"></a>
    <table><thead align="left"><tr id="row14775484"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p55963561"><a name="p55963561"></a><a name="p55963561"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p36754611"><a name="p36754611"></a><a name="p36754611"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row24333505"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p24856892"><a name="p24856892"></a><a name="p24856892"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p142347"><a name="p142347"></a><a name="p142347"></a>Invalid parameters.</p>
    </td>
    </tr>
    <tr id="row1281126"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p36662351"><a name="p36662351"></a><a name="p36662351"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p16860416"><a name="p16860416"></a><a name="p16860416"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row17526019"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p10321460"><a name="p10321460"></a><a name="p10321460"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p30731970"><a name="p30731970"></a><a name="p30731970"></a>You do not have permission to perform this operation.</p>
    </td>
    </tr>
    <tr id="row8152279"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p56354875"><a name="p56354875"></a><a name="p56354875"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p1342126"><a name="p1342126"></a><a name="p1342126"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row12079142"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p38886454"><a name="p38886454"></a><a name="p38886454"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p62795050"><a name="p62795050"></a><a name="p62795050"></a>A system exception occurs.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section61541938486"></a>

For details, see  [Error Codes](error-codes.md).

