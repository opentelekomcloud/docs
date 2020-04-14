# Modifying Predefined Tags<a name="EN-US_TOPIC_0170553614"></a>

## Function<a name="section18143273182827"></a>

This API is used for modifying predefined tags.

## URI<a name="section6000243182827"></a>

PUT /v1.0/predefine\_tags

## Request<a name="section54624715182827"></a>

-   Parameter description

    **Table  1**  Parameters in the request

    <a name="table31427211182827"></a>
    <table><thead align="left"><tr id="row44416069182827"><th class="cellrowborder" valign="top" width="14.719999999999999%" id="mcps1.2.5.1.1"><p id="p40931822182827"><a name="p40931822182827"></a><a name="p40931822182827"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.1%" id="mcps1.2.5.1.2"><p id="p27143284182827"><a name="p27143284182827"></a><a name="p27143284182827"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="28.38%" id="mcps1.2.5.1.3"><p id="p51122366182827"><a name="p51122366182827"></a><a name="p51122366182827"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="39.800000000000004%" id="mcps1.2.5.1.4"><p id="p47270964182827"><a name="p47270964182827"></a><a name="p47270964182827"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3742912182827"><td class="cellrowborder" valign="top" width="14.719999999999999%" headers="mcps1.2.5.1.1 "><p id="p34740423182827"><a name="p34740423182827"></a><a name="p34740423182827"></a>old_tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.1%" headers="mcps1.2.5.1.2 "><p id="p62510899182827"><a name="p62510899182827"></a><a name="p62510899182827"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.38%" headers="mcps1.2.5.1.3 "><p id="p30218092182827"><a name="p30218092182827"></a><a name="p30218092182827"></a>predefine_tag_request</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.5.1.4 "><p id="p31746393182827"><a name="p31746393182827"></a><a name="p31746393182827"></a>Specifies the tag to be modified.</p>
    <p id="p11490457172114"><a name="p11490457172114"></a><a name="p11490457172114"></a>For details, see <a href="#table62639743182827">Table 2</a>.</p>
    </td>
    </tr>
    <tr id="row17282087182827"><td class="cellrowborder" valign="top" width="14.719999999999999%" headers="mcps1.2.5.1.1 "><p id="p57671806182827"><a name="p57671806182827"></a><a name="p57671806182827"></a>new_tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.1%" headers="mcps1.2.5.1.2 "><p id="p40904701182827"><a name="p40904701182827"></a><a name="p40904701182827"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.38%" headers="mcps1.2.5.1.3 "><p id="p24946509182827"><a name="p24946509182827"></a><a name="p24946509182827"></a>predefine_tag_request</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.5.1.4 "><p id="p7401366182827"><a name="p7401366182827"></a><a name="p7401366182827"></a>Specifies the tag that has been modified.</p>
    <p id="p1644791932216"><a name="p1644791932216"></a><a name="p1644791932216"></a>For details, see <a href="#table62639743182827">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   **predefine\_tag\_request**  data structure

    **Table  2** **predefine\_tag\_request**  data structure description

    <a name="table62639743182827"></a>
    <table><thead align="left"><tr id="row49571698182827"><th class="cellrowborder" valign="top" width="13.209999999999999%" id="mcps1.2.5.1.1"><p id="p55884612182827"><a name="p55884612182827"></a><a name="p55884612182827"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.86%" id="mcps1.2.5.1.2"><p id="p30359747182827"><a name="p30359747182827"></a><a name="p30359747182827"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.91%" id="mcps1.2.5.1.3"><p id="p43220438182827"><a name="p43220438182827"></a><a name="p43220438182827"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.02%" id="mcps1.2.5.1.4"><p id="p11194598182827"><a name="p11194598182827"></a><a name="p11194598182827"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row34347226182827"><td class="cellrowborder" valign="top" width="13.209999999999999%" headers="mcps1.2.5.1.1 "><p id="p30661915182827"><a name="p30661915182827"></a><a name="p30661915182827"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.2.5.1.2 "><p id="p587152182827"><a name="p587152182827"></a><a name="p587152182827"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.91%" headers="mcps1.2.5.1.3 "><p id="p47559329182827"><a name="p47559329182827"></a><a name="p47559329182827"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.02%" headers="mcps1.2.5.1.4 "><p id="p108587120631"><a name="p108587120631"></a><a name="p108587120631"></a>Specifies the key.</p>
    <p id="p16424462153146"><a name="p16424462153146"></a><a name="p16424462153146"></a>It cannot be left blank and can contain a maximum of 36 Unicode characters. Can contain only digits, letters, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    <tr id="row42577656182827"><td class="cellrowborder" valign="top" width="13.209999999999999%" headers="mcps1.2.5.1.1 "><p id="p26238096182827"><a name="p26238096182827"></a><a name="p26238096182827"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.2.5.1.2 "><p id="p44911008182827"><a name="p44911008182827"></a><a name="p44911008182827"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.91%" headers="mcps1.2.5.1.3 "><p id="p13913041182827"><a name="p13913041182827"></a><a name="p13913041182827"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.02%" headers="mcps1.2.5.1.4 "><p id="p2486891184110"><a name="p2486891184110"></a><a name="p2486891184110"></a>Specifies the value.</p>
    <p id="p10159585153243"><a name="p10159585153243"></a><a name="p10159585153243"></a>Each value contains a maximum of 43 Unicode characters and can be an empty string. Can contain only digits, letters, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    PUT https://{TMS endpoint}/v1.0/predefined_tags
    ```

    ```
    {
        "new_tag": {
            "key": "ENV1",
            "value": "DEV1"
        },
        "old_tag": {
            "key": "ENV2",
            "value": "DEV2"
        }
    }
    ```


## Response<a name="section26969841182827"></a>

-   Parameter description

    None


-   Example response

    None


## Status Codes<a name="section17789101582315"></a>

For details, see  [Status Code](status-code.md).

## Error Codes<a name="section18604165622519"></a>

For details, see  [Error Code Description](error-code-description.md).

