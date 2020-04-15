# Responses \(Task\)<a name="EN-US_TOPIC_0022067714"></a>

-   Normal response description

    <a name="table757167711151"></a>
    <table><thead align="left"><tr id="row5251903911151"><th class="cellrowborder" valign="top" width="16.48%" id="mcps1.1.4.1.1"><p id="p2618376611151"><a name="p2618376611151"></a><a name="p2618376611151"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.98%" id="mcps1.1.4.1.2"><p id="p4051029311151"><a name="p4051029311151"></a><a name="p4051029311151"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="65.53999999999999%" id="mcps1.1.4.1.3"><p id="p6010832511151"><a name="p6010832511151"></a><a name="p6010832511151"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3693617411151"><td class="cellrowborder" valign="top" width="16.48%" headers="mcps1.1.4.1.1 "><p id="p3904008711151"><a name="p3904008711151"></a><a name="p3904008711151"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.98%" headers="mcps1.1.4.1.2 "><p id="p813044011151"><a name="p813044011151"></a><a name="p813044011151"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.53999999999999%" headers="mcps1.1.4.1.3 "><p id="p5458589811151"><a name="p5458589811151"></a><a name="p5458589811151"></a>Specifies the returned task ID after delivering the task. Users can query the task progress using this ID. For how to query the execution status of the task based on the task ID, see <a href="task-status-management.md">Task Status Management</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Abnormal response description

    <a name="table6467239411151"></a>
    <table><thead align="left"><tr id="row2581079811151"><th class="cellrowborder" valign="top" width="16.55%" id="mcps1.1.4.1.1"><p id="p1029990211151"><a name="p1029990211151"></a><a name="p1029990211151"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.86%" id="mcps1.1.4.1.2"><p id="p2898571411151"><a name="p2898571411151"></a><a name="p2898571411151"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="65.59%" id="mcps1.1.4.1.3"><p id="p6614149111151"><a name="p6614149111151"></a><a name="p6614149111151"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5586052011151"><td class="cellrowborder" valign="top" width="16.55%" headers="mcps1.1.4.1.1 "><p id="p2840824911151"><a name="p2840824911151"></a><a name="p2840824911151"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.1.4.1.2 "><p id="p1936686411151"><a name="p1936686411151"></a><a name="p1936686411151"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.59%" headers="mcps1.1.4.1.3 "><p id="p2558244011151"><a name="p2558244011151"></a><a name="p2558244011151"></a>Specifies the returned error message when an error occurs. For details, see <a href="#table6409189311151">Table 1</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  1** **error**  field structure

    <a name="table6409189311151"></a>
    <table><thead align="left"><tr id="row2324327311151"><th class="cellrowborder" valign="top" width="16.6%" id="mcps1.2.4.1.1"><p id="p365693111151"><a name="p365693111151"></a><a name="p365693111151"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.919999999999998%" id="mcps1.2.4.1.2"><p id="p2777597711151"><a name="p2777597711151"></a><a name="p2777597711151"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="65.48%" id="mcps1.2.4.1.3"><p id="p3526170111151"><a name="p3526170111151"></a><a name="p3526170111151"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3762550011151"><td class="cellrowborder" valign="top" width="16.6%" headers="mcps1.2.4.1.1 "><p id="p2776668011151"><a name="p2776668011151"></a><a name="p2776668011151"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.919999999999998%" headers="mcps1.2.4.1.2 "><p id="p3450864111151"><a name="p3450864111151"></a><a name="p3450864111151"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.48%" headers="mcps1.2.4.1.3 "><p id="p4373654211151"><a name="p4373654211151"></a><a name="p4373654211151"></a>Describes the error message when an error occurs.</p>
    </td>
    </tr>
    <tr id="row5808456411151"><td class="cellrowborder" valign="top" width="16.6%" headers="mcps1.2.4.1.1 "><p id="p722924311151"><a name="p722924311151"></a><a name="p722924311151"></a>code</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.919999999999998%" headers="mcps1.2.4.1.2 "><p id="p4869780211151"><a name="p4869780211151"></a><a name="p4869780211151"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.48%" headers="mcps1.2.4.1.3 "><p id="p5220791411151"><a name="p5220791411151"></a><a name="p5220791411151"></a>Specifies the error code when an error occurs.</p>
    </td>
    </tr>
    <tr id="row152703448361"><td class="cellrowborder" valign="top" width="16.6%" headers="mcps1.2.4.1.1 "><p id="p6270164414368"><a name="p6270164414368"></a><a name="p6270164414368"></a>details</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.919999999999998%" headers="mcps1.2.4.1.2 "><p id="p1527164413365"><a name="p1527164413365"></a><a name="p1527164413365"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.48%" headers="mcps1.2.4.1.3 "><p id="p6161120143914"><a name="p6161120143914"></a><a name="p6161120143914"></a>Specifies error details.</p>
    <p id="p12711744153618"><a name="p12711744153618"></a><a name="p12711744153618"></a>Error details provide the error code and fault description, facilitating error handling.</p>
    <p id="p1036024715422"><a name="p1036024715422"></a><a name="p1036024715422"></a>This field is optional.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2** **details**  field description

    <a name="table13473121174414"></a>
    <table><thead align="left"><tr id="row1047321116442"><th class="cellrowborder" valign="top" width="20.03200320032003%" id="mcps1.2.4.1.1"><p id="p16841815164410"><a name="p16841815164410"></a><a name="p16841815164410"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.492349234923495%" id="mcps1.2.4.1.2"><p id="p156848154441"><a name="p156848154441"></a><a name="p156848154441"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.47564756475647%" id="mcps1.2.4.1.3"><p id="p2684915114416"><a name="p2684915114416"></a><a name="p2684915114416"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row154741118449"><td class="cellrowborder" valign="top" width="20.03200320032003%" headers="mcps1.2.4.1.1 "><p id="p20684191534416"><a name="p20684191534416"></a><a name="p20684191534416"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.492349234923495%" headers="mcps1.2.4.1.2 "><p id="p136843156446"><a name="p136843156446"></a><a name="p136843156446"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47564756475647%" headers="mcps1.2.4.1.3 "><p id="p186847153447"><a name="p186847153447"></a><a name="p186847153447"></a>Describes the error message when an error occurs.</p>
    <p id="p39751736204614"><a name="p39751736204614"></a><a name="p39751736204614"></a>This field is optional.</p>
    </td>
    </tr>
    <tr id="row1747410114445"><td class="cellrowborder" valign="top" width="20.03200320032003%" headers="mcps1.2.4.1.1 "><p id="p968411574417"><a name="p968411574417"></a><a name="p968411574417"></a>code</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.492349234923495%" headers="mcps1.2.4.1.2 "><p id="p268510154449"><a name="p268510154449"></a><a name="p268510154449"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47564756475647%" headers="mcps1.2.4.1.3 "><p id="p968518151442"><a name="p968518151442"></a><a name="p968518151442"></a>Specifies the error code when an error occurs.</p>
    <p id="p940013934613"><a name="p940013934613"></a><a name="p940013934613"></a>This field is optional.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    Normal response

    ```
    { 
        "job_id": "70a599e0-31e7-49b7-b260-868f441e862b"
    } 
    ```

    Abnormal response

    ```
    { 
        "error": {"message": "", "code": XXX,""}
    } 
    ```


