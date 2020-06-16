# Querying Tags of All Protected Instances in a Specified Project<a name="sdrs_05_0806"></a>

## Function<a name="section1986421154818"></a>

This API is used to query all resource tags of a protected instance in a specified project.

## URI<a name="section598614216482"></a>

-   URI format

    GET /v1/\{project\_id\}/protected-instances/tags

-   Parameter description

    <a name="table698812134817"></a>
    <table><thead align="left"><tr id="row71033220480"><th class="cellrowborder" valign="top" width="19.59%" id="mcps1.1.5.1.1"><p id="p91039224483"><a name="p91039224483"></a><a name="p91039224483"></a><strong id="b842352706162023"><a name="b842352706162023"></a><a name="b842352706162023"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.9%" id="mcps1.1.5.1.2"><p id="p510314222487"><a name="p510314222487"></a><a name="p510314222487"></a><strong id="b84235270615447"><a name="b84235270615447"></a><a name="b84235270615447"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="12.370000000000001%" id="mcps1.1.5.1.3"><p id="p101031522124820"><a name="p101031522124820"></a><a name="p101031522124820"></a><strong id="b84235270615453"><a name="b84235270615453"></a><a name="b84235270615453"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="38.14%" id="mcps1.1.5.1.4"><p id="p111033221486"><a name="p111033221486"></a><a name="p111033221486"></a><strong id="b84235270615457"><a name="b84235270615457"></a><a name="b84235270615457"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1710482224815"><td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.1.5.1.1 "><p id="p61043220484"><a name="p61043220484"></a><a name="p61043220484"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.9%" headers="mcps1.1.5.1.2 "><p id="p16104422134818"><a name="p16104422134818"></a><a name="p16104422134818"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.1.5.1.3 "><p id="p4104122104818"><a name="p4104122104818"></a><a name="p4104122104818"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.14%" headers="mcps1.1.5.1.4 "><p id="p17104162204817"><a name="p17104162204817"></a><a name="p17104162204817"></a>Specifies the project ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section199272115482"></a>

-   Request parameters

    None

-   Example request

    GET https://\{Endpoint\}/v1/\{project\_id\}/protected-instances/tags


## Response<a name="section15992132118483"></a>

-   Parameter description

    <a name="table4995142119483"></a>
    <table><thead align="left"><tr id="row71041522144811"><th class="cellrowborder" valign="top" width="10.31103110311031%" id="mcps1.1.5.1.1"><p id="p1510472224819"><a name="p1510472224819"></a><a name="p1510472224819"></a><strong id="b842352706162023_1"><a name="b842352706162023_1"></a><a name="b842352706162023_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.77257725772577%" id="mcps1.1.5.1.2"><p id="p21041522124812"><a name="p21041522124812"></a><a name="p21041522124812"></a><strong id="b84235270615447_1"><a name="b84235270615447_1"></a><a name="b84235270615447_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.491649164916492%" id="mcps1.1.5.1.3"><p id="p3104202212485"><a name="p3104202212485"></a><a name="p3104202212485"></a><strong id="b84235270615453_1"><a name="b84235270615453_1"></a><a name="b84235270615453_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="47.42474247424743%" id="mcps1.1.5.1.4"><p id="p710452217480"><a name="p710452217480"></a><a name="p710452217480"></a><strong id="b84235270615457_1"><a name="b84235270615457_1"></a><a name="b84235270615457_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1610492234812"><td class="cellrowborder" valign="top" width="10.31103110311031%" headers="mcps1.1.5.1.1 "><p id="p810413220488"><a name="p810413220488"></a><a name="p810413220488"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.77257725772577%" headers="mcps1.1.5.1.2 "><p id="p10104132210483"><a name="p10104132210483"></a><a name="p10104132210483"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.491649164916492%" headers="mcps1.1.5.1.3 "><p id="p8104622164819"><a name="p8104622164819"></a><a name="p8104622164819"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.42474247424743%" headers="mcps1.1.5.1.4 "><p id="p51041522134815"><a name="p51041522134815"></a><a name="p51041522134815"></a>Specifies the tag list.</p>
    <p id="p18245114391515"><a name="p18245114391515"></a><a name="p18245114391515"></a>For details, see <a href="#table09990210488">Table 1</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  1**  Data structure of the  **tag**  field

    <a name="table09990210488"></a>
    <table><thead align="left"><tr id="row1910412264814"><th class="cellrowborder" valign="top" width="9.180000000000001%" id="mcps1.2.5.1.1"><p id="p51041822104817"><a name="p51041822104817"></a><a name="p51041822104817"></a><strong id="b842352706162023_2"><a name="b842352706162023_2"></a><a name="b842352706162023_2"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.509999999999998%" id="mcps1.2.5.1.2"><p id="p10104112234815"><a name="p10104112234815"></a><a name="p10104112234815"></a><strong id="b84235270615447_2"><a name="b84235270615447_2"></a><a name="b84235270615447_2"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.349999999999998%" id="mcps1.2.5.1.3"><p id="p19104822204816"><a name="p19104822204816"></a><a name="p19104822204816"></a><strong id="b84235270615453_2"><a name="b84235270615453_2"></a><a name="b84235270615453_2"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="47.96%" id="mcps1.2.5.1.4"><p id="p010542217484"><a name="p010542217484"></a><a name="p010542217484"></a><strong id="b84235270615457_2"><a name="b84235270615457_2"></a><a name="b84235270615457_2"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row81051522144818"><td class="cellrowborder" valign="top" width="9.180000000000001%" headers="mcps1.2.5.1.1 "><p id="p1105172264814"><a name="p1105172264814"></a><a name="p1105172264814"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.5.1.2 "><p id="p2010519228482"><a name="p2010519228482"></a><a name="p2010519228482"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.5.1.3 "><p id="p181051122104816"><a name="p181051122104816"></a><a name="p181051122104816"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.96%" headers="mcps1.2.5.1.4 "><p id="p16938773138"><a name="p16938773138"></a><a name="p16938773138"></a>Specifies the tag key. The tag key of a resource must be unique.</p>
    </td>
    </tr>
    <tr id="row410512226486"><td class="cellrowborder" valign="top" width="9.180000000000001%" headers="mcps1.2.5.1.1 "><p id="p410572224817"><a name="p410572224817"></a><a name="p410572224817"></a>values</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.5.1.2 "><p id="p710512284811"><a name="p710512284811"></a><a name="p710512284811"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.5.1.3 "><p id="p5105132215482"><a name="p5105132215482"></a><a name="p5105132215482"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.96%" headers="mcps1.2.5.1.4 "><p id="p7808113171318"><a name="p7808113171318"></a><a name="p7808113171318"></a>Lists the tag values.</p>
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


## **Returned Value**<a name="section1212182214816"></a>

-   Normal

    <a name="table19142225485"></a>
    <table><thead align="left"><tr id="row6105222114818"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p141051122124817"><a name="p141051122124817"></a><a name="p141051122124817"></a><strong id="b842352706175024_1"><a name="b842352706175024_1"></a><a name="b842352706175024_1"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p191051922144815"><a name="p191051922144815"></a><a name="p191051922144815"></a><strong id="b84235270615457_3"><a name="b84235270615457_3"></a><a name="b84235270615457_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row31051822194814"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p3105112234810"><a name="p3105112234810"></a><a name="p3105112234810"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p1110512212485"><a name="p1110512212485"></a><a name="p1110512212485"></a>OK</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Abnormal

    <a name="table16167225487"></a>
    <table><thead align="left"><tr id="row101064228487"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p41061722154810"><a name="p41061722154810"></a><a name="p41061722154810"></a><strong id="b842352706175024_2"><a name="b842352706175024_2"></a><a name="b842352706175024_2"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p21067227488"><a name="p21067227488"></a><a name="p21067227488"></a><strong id="b84235270615457_4"><a name="b84235270615457_4"></a><a name="b84235270615457_4"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row310618226488"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p20106112220487"><a name="p20106112220487"></a><a name="p20106112220487"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p1510617226482"><a name="p1510617226482"></a><a name="p1510617226482"></a>Invalid parameters.</p>
    </td>
    </tr>
    <tr id="row510672294820"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p9106192212484"><a name="p9106192212484"></a><a name="p9106192212484"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p6106112284814"><a name="p6106112284814"></a><a name="p6106112284814"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row4106222114810"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p8106142294820"><a name="p8106142294820"></a><a name="p8106142294820"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p1810617229480"><a name="p1810617229480"></a><a name="p1810617229480"></a>Insufficient permission.</p>
    </td>
    </tr>
    <tr id="row10106182214814"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p13106622144820"><a name="p13106622144820"></a><a name="p13106622144820"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p15106192212482"><a name="p15106192212482"></a><a name="p15106192212482"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row810672218488"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p161067227484"><a name="p161067227484"></a><a name="p161067227484"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p121071622174812"><a name="p121071622174812"></a><a name="p121071622174812"></a>Internal service error.</p>
    </td>
    </tr>
    </tbody>
    </table>


