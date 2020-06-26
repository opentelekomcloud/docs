# Querying Tags in a Specified Project<a name="smn_api_56006"></a>

## Description<a name="section4995141120217"></a>

-   API name

    GetProjectTags


-   Function

    Query all tags of a resource type in a specified project.


## URI<a name="section1999581115219"></a>

-   URI format

    GET /v2/\{project\_id\}/\{resource\_type\}/tags

-   Parameter description

    <a name="table1710612152111"></a>
    <table><thead align="left"><tr id="row5167161218218"><th class="cellrowborder" valign="top" width="21.84%" id="mcps1.1.5.1.1"><p id="p216712123213"><a name="p216712123213"></a><a name="p216712123213"></a><strong>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24.14%" id="mcps1.1.5.1.2"><p id="p616715121219"><a name="p616715121219"></a><a name="p616715121219"></a><strong>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.54%" id="mcps1.1.5.1.3"><p id="p191671312162117"><a name="p191671312162117"></a><a name="p191671312162117"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="34.48%" id="mcps1.1.5.1.4"><p id="p11167171282115"><a name="p11167171282115"></a><a name="p11167171282115"></a><strong>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row61671612152120"><td class="cellrowborder" valign="top" width="21.84%" headers="mcps1.1.5.1.1 "><p id="p15167712142119"><a name="p15167712142119"></a><a name="p15167712142119"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.14%" headers="mcps1.1.5.1.2 "><p id="p816781216216"><a name="p816781216216"></a><a name="p816781216216"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.54%" headers="mcps1.1.5.1.3 "><p id="p716731217212"><a name="p716731217212"></a><a name="p716731217212"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.48%" headers="mcps1.1.5.1.4 "><p id="p12167412162111"><a name="p12167412162111"></a><a name="p12167412162111"></a>Project ID</p>
    <p id="p118812918506"><a name="p118812918506"></a><a name="p118812918506"></a>See section <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row416718122211"><td class="cellrowborder" valign="top" width="21.84%" headers="mcps1.1.5.1.1 "><p id="p99531421797"><a name="p99531421797"></a><a name="p99531421797"></a>resource_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.14%" headers="mcps1.1.5.1.2 "><p id="p1495310421799"><a name="p1495310421799"></a><a name="p1495310421799"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.54%" headers="mcps1.1.5.1.3 "><p id="p149531342296"><a name="p149531342296"></a><a name="p149531342296"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.48%" headers="mcps1.1.5.1.4 "><p id="p52661238184213"><a name="p52661238184213"></a><a name="p52661238184213"></a>Resource type</p>
    <p id="p1034904075316"><a name="p1034904075316"></a><a name="p1034904075316"></a>The value can be the following:</p>
    <p id="p14550953686"><a name="p14550953686"></a><a name="p14550953686"></a><strong id="b691911631815"><a name="b691911631815"></a><a name="b691911631815"></a>smn_topic</strong>: topic</p>
    <p id="p8682201993"><a name="p8682201993"></a><a name="p8682201993"></a></p>
    <p id="p278251314214"><a name="p278251314214"></a><a name="p278251314214"></a></p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section142631216210"></a>

-   Parameter description

    None


-   Request example

    ```
    GET https://{SMN_Endpoint}/v2/{project_id}/{resource_type}/tags
    ```


## Response<a name="section172616120211"></a>

-   Parameter description

    <a name="table1226141212116"></a>
    <table><thead align="left"><tr id="row1167171216218"><th class="cellrowborder" valign="top" width="18.63%" id="mcps1.1.4.1.1"><p id="p016731216215"><a name="p016731216215"></a><a name="p016731216215"></a><strong>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.73%" id="mcps1.1.4.1.2"><p id="p131679120217"><a name="p131679120217"></a><a name="p131679120217"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.64%" id="mcps1.1.4.1.3"><p id="p19167212182113"><a name="p19167212182113"></a><a name="p19167212182113"></a><strong>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3167151282112"><td class="cellrowborder" valign="top" width="18.63%" headers="mcps1.1.4.1.1 "><p id="p8167151292115"><a name="p8167151292115"></a><a name="p8167151292115"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.73%" headers="mcps1.1.4.1.2 "><p id="p016751262114"><a name="p016751262114"></a><a name="p016751262114"></a>Tags structure array</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.64%" headers="mcps1.1.4.1.3 "><p id="p616718127213"><a name="p616718127213"></a><a name="p616718127213"></a>Tag list. For details, see <a href="#table7893236124418">Table 1</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  1**  Tags structure

    <a name="table7893236124418"></a>
    <table><thead align="left"><tr id="smn_api_56001_row12526442141213"><th class="cellrowborder" valign="top" width="18.16%" id="mcps1.2.6.1.1"><p id="smn_api_56001_p1252612428129"><a name="smn_api_56001_p1252612428129"></a><a name="smn_api_56001_p1252612428129"></a><strong id="smn_api_56001_b47901755163415"><a name="smn_api_56001_b47901755163415"></a><a name="smn_api_56001_b47901755163415"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="12.030000000000001%" id="mcps1.2.6.1.2"><p id="smn_api_56001_p852612421125"><a name="smn_api_56001_p852612421125"></a><a name="smn_api_56001_p852612421125"></a><strong id="smn_api_56001_b895256445"><a name="smn_api_56001_b895256445"></a><a name="smn_api_56001_b895256445"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.81%" id="mcps1.2.6.1.3"><p id="smn_api_56001_p14526542121214"><a name="smn_api_56001_p14526542121214"></a><a name="smn_api_56001_p14526542121214"></a><strong id="smn_api_56001_b2041287441"><a name="smn_api_56001_b2041287441"></a><a name="smn_api_56001_b2041287441"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.65%" id="mcps1.2.6.1.4"><p id="smn_api_56001_p17526124281215"><a name="smn_api_56001_p17526124281215"></a><a name="smn_api_56001_p17526124281215"></a><strong id="smn_api_56001_b63411457103415"><a name="smn_api_56001_b63411457103415"></a><a name="smn_api_56001_b63411457103415"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="34.35%" id="mcps1.2.6.1.5"><p id="smn_api_56001_p12294162622414"><a name="smn_api_56001_p12294162622414"></a><a name="smn_api_56001_p12294162622414"></a><strong id="smn_api_56001_b167841358163418"><a name="smn_api_56001_b167841358163418"></a><a name="smn_api_56001_b167841358163418"></a>Constraint</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="smn_api_56001_row1526194218129"><td class="cellrowborder" valign="top" width="18.16%" headers="mcps1.2.6.1.1 "><p id="smn_api_56001_p65262427126"><a name="smn_api_56001_p65262427126"></a><a name="smn_api_56001_p65262427126"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.2.6.1.2 "><p id="smn_api_56001_p4526154211123"><a name="smn_api_56001_p4526154211123"></a><a name="smn_api_56001_p4526154211123"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.81%" headers="mcps1.2.6.1.3 "><p id="smn_api_56001_p35261242171216"><a name="smn_api_56001_p35261242171216"></a><a name="smn_api_56001_p35261242171216"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.65%" headers="mcps1.2.6.1.4 "><p id="smn_api_56001_p552604213129"><a name="smn_api_56001_p552604213129"></a><a name="smn_api_56001_p552604213129"></a>Tag key</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.35%" headers="mcps1.2.6.1.5 "><p id="smn_api_56001_p6294172612244"><a name="smn_api_56001_p6294172612244"></a><a name="smn_api_56001_p6294172612244"></a>A key contains 127 Unicode characters and cannot be blank.</p>
    </td>
    </tr>
    <tr id="smn_api_56001_row55261142141216"><td class="cellrowborder" valign="top" width="18.16%" headers="mcps1.2.6.1.1 "><p id="smn_api_56001_p1852614219127"><a name="smn_api_56001_p1852614219127"></a><a name="smn_api_56001_p1852614219127"></a>values</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.2.6.1.2 "><p id="smn_api_56001_p11526104271211"><a name="smn_api_56001_p11526104271211"></a><a name="smn_api_56001_p11526104271211"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.81%" headers="mcps1.2.6.1.3 "><p id="smn_api_56001_p45262426129"><a name="smn_api_56001_p45262426129"></a><a name="smn_api_56001_p45262426129"></a>String list</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.65%" headers="mcps1.2.6.1.4 "><p id="smn_api_56001_p152694220126"><a name="smn_api_56001_p152694220126"></a><a name="smn_api_56001_p152694220126"></a>Value list</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.35%" headers="mcps1.2.6.1.5 "><p id="smn_api_56001_p18294152612244"><a name="smn_api_56001_p18294152612244"></a><a name="smn_api_56001_p18294152612244"></a>Each value contains a maximum of 255 Unicode characters. If the value starts with an asterisk (*), the character string following the asterisk is fuzzy-matched. The <strong id="smn_api_56001_b18353175912112"><a name="smn_api_56001_b18353175912112"></a><a name="smn_api_56001_b18353175912112"></a>values</strong> field cannot be missing, but can be an empty list. If it is empty, any value will be matched. The values are in OR relationship.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    {
          "tags": [
            {
                "key": "key1",
                "values": ["value1""value2"]
            },
            {
                "key": "key2",
                "values": ["value1","value2"]
            }
        ]
    }
    ```


## Returned Value<a name="section242171292113"></a>

See section  [Returned Value](returned-value.md).

## Error Code<a name="section73211020122511"></a>

See section  [Error Code](error-code.md).

