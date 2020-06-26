# Querying an Image Member Schema \(Native OpenStack API\)<a name="EN-US_TOPIC_0049147876"></a>

## Function<a name="section4678164010456"></a>

This API is used to query an image member schema, which allows you to view image member attributes and their data types.

## URI<a name="section1251307010456"></a>

GET /v2/schemas/member

## Request<a name="section2411735110456"></a>

-   Request parameters

    None

-   Example request

    ```
    GET https://{Endpoint}/v2/schemas/member
    ```


## Response<a name="section5835198610456"></a>

-   Response parameters

    <a name="table5842318310456"></a>
    <table><thead align="left"><tr id="row6525201010456"><th class="cellrowborder" valign="top" width="30.486951304869514%" id="mcps1.1.4.1.1"><p id="p5092146210456"><a name="p5092146210456"></a><a name="p5092146210456"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.078292170782923%" id="mcps1.1.4.1.2"><p id="p2779017510456"><a name="p2779017510456"></a><a name="p2779017510456"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.434756524347556%" id="mcps1.1.4.1.3"><p id="p3641172510456"><a name="p3641172510456"></a><a name="p3641172510456"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6366858710456"><td class="cellrowborder" valign="top" width="30.486951304869514%" headers="mcps1.1.4.1.1 "><p id="p5688188910456"><a name="p5688188910456"></a><a name="p5688188910456"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.078292170782923%" headers="mcps1.1.4.1.2 "><p id="p968421510456"><a name="p968421510456"></a><a name="p968421510456"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.434756524347556%" headers="mcps1.1.4.1.3 "><p id="p4622397510456"><a name="p4622397510456"></a><a name="p4622397510456"></a>Specifies the schema name.</p>
    </td>
    </tr>
    <tr id="row1336259710456"><td class="cellrowborder" valign="top" width="30.486951304869514%" headers="mcps1.1.4.1.1 "><p id="p862856110456"><a name="p862856110456"></a><a name="p862856110456"></a>properties</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.078292170782923%" headers="mcps1.1.4.1.2 "><p id="p3921638110456"><a name="p3921638110456"></a><a name="p3921638110456"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.434756524347556%" headers="mcps1.1.4.1.3 "><p id="p1622165310562"><a name="p1622165310562"></a><a name="p1622165310562"></a>Describes basic image attributes, including the type and usage of each attribute.</p>
    <p id="p4120204111445"><a name="p4120204111445"></a><a name="p4120204111445"></a>For details about the parameters, see <a href="image-attributes.md">Image Attributes</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    STATUS CODE 200
    ```

    ```
    {
        "name": "member",
        "properties": {
            "status": {
                "enum": [
                    "pending",
                    "accepted",
                    "rejected"
                ],
                "type": "string",
                "description": "The status of this image member"
            },
            "created_at": {
                "type": "string",
                "description": "Date and time of image member creation"
            },
            "updated_at": {
                "type": "string",
                "description": "Date and time of last modification of image member"
            },
            "image_id": {
                "pattern": "^([0-9a-fA-F]){8}-([0-9a-fA-F]){4}-([0-9a-fA-F]){4}-([0-9a-fA-F]){4}-([0-9a-fA-F]){12}$",
                "type": "string",
                "description": "An identifier for the image"
            },
            "member_id": {
                "type": "string",
                "description": "An identifier for the image member (tenantId)"
            },
            "schema": {
                "readOnly": true,
                "type": "string"
            }
        }
    }
    ```


## Returned Value<a name="section3184290310456"></a>

-   Normal

    200

-   Abnormal

    <a name="table5046465910456"></a>
    <table><thead align="left"><tr id="row5279442910456"><th class="cellrowborder" valign="top" width="46.46%" id="mcps1.1.3.1.1"><p id="p4849034810456"><a name="p4849034810456"></a><a name="p4849034810456"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.54%" id="mcps1.1.3.1.2"><p id="p3540414010456"><a name="p3540414010456"></a><a name="p3540414010456"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4916310910456"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p2278886210456"><a name="p2278886210456"></a><a name="p2278886210456"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p3395849510456"><a name="p3395849510456"></a><a name="p3395849510456"></a>Request error.</p>
    </td>
    </tr>
    <tr id="row3719100210456"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p5968121110456"><a name="p5968121110456"></a><a name="p5968121110456"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p233996110456"><a name="p233996110456"></a><a name="p233996110456"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row2105965410456"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p2811042610456"><a name="p2811042610456"></a><a name="p2811042610456"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p6235199710456"><a name="p6235199710456"></a><a name="p6235199710456"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="row2429706910456"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p2190558110456"><a name="p2190558110456"></a><a name="p2190558110456"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p2952161710456"><a name="p2952161710456"></a><a name="p2952161710456"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row6436796410456"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p4642261010456"><a name="p4642261010456"></a><a name="p4642261010456"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p213507210456"><a name="p213507210456"></a><a name="p213507210456"></a>Internal service error.</p>
    </td>
    </tr>
    <tr id="row1921565610456"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p1296433510456"><a name="p1296433510456"></a><a name="p1296433510456"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p4347817710456"><a name="p4347817710456"></a><a name="p4347817710456"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


