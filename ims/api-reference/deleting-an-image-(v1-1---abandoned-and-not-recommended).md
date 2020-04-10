# Deleting an Image \(v1.1 - Abandoned and Not Recommended\)<a name="EN-US_TOPIC_0066978722"></a>

## Function<a name="section65883044152228"></a>

This API is used to delete an image. If you soft delete the image with a specified ID, the image persists in the database, but in the  **deleted **status.

This API has been discarded.  [Deleting an Image \(Native OpenStack API\)](deleting-an-image-(native-openstack-api).md)  is recommended.

## URI<a name="section45901761152228"></a>

DELETE /v1.1/images/\{image\_id\}

[Table 1](#table27262282)  lists the parameters in the URI.

**Table  1**  Parameter description

<a name="table27262282"></a>
<table><thead align="left"><tr id="row27551015"><th class="cellrowborder" valign="top" width="22.720000000000002%" id="mcps1.2.5.1.1"><p id="p17039762"><a name="p17039762"></a><a name="p17039762"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20.71%" id="mcps1.2.5.1.2"><p id="p38043494"><a name="p38043494"></a><a name="p38043494"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="20.49%" id="mcps1.2.5.1.3"><p id="p1119157921331"><a name="p1119157921331"></a><a name="p1119157921331"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="36.08%" id="mcps1.2.5.1.4"><p id="p61624137"><a name="p61624137"></a><a name="p61624137"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row25499238"><td class="cellrowborder" valign="top" width="22.720000000000002%" headers="mcps1.2.5.1.1 "><p id="p52172387"><a name="p52172387"></a><a name="p52172387"></a>image_id</p>
</td>
<td class="cellrowborder" valign="top" width="20.71%" headers="mcps1.2.5.1.2 "><p id="p65213800"><a name="p65213800"></a><a name="p65213800"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20.49%" headers="mcps1.2.5.1.3 "><p id="p3410274521331"><a name="p3410274521331"></a><a name="p3410274521331"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.08%" headers="mcps1.2.5.1.4 "><p id="p47826462"><a name="p47826462"></a><a name="p47826462"></a>Specifies the image ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section59210700152228"></a>

-   Request parameters

    None

-   Example request

    ```
    DELETE https://{Endpoint}/v1.1/images/3c3d1d01-b48a-4639-8a88-08be3b9b5d78
    ```


## Response<a name="section13601000152228"></a>

-   Response parameters

    None

-   Example response

    ```
    HTTP/1.1 200 OK
    ```

    ```
    Content-Type: text/html; charset=UTF-8
    Content-Length: 0
    X-Openstack-Request-Id: req-75e9edca-7b43-47da-bdc5-d39be469b72f
    Date: Mon, 23 May 2016 02:43:34 GMT
    ```


## Returned Values<a name="section47464039152228"></a>

-   Normal

    204

-   Abnormal

    <a name="table5314667917313"></a>
    <table><thead align="left"><tr id="row4648913117313"><th class="cellrowborder" valign="top" width="46.54%" id="mcps1.1.3.1.1"><p id="p752327917313"><a name="p752327917313"></a><a name="p752327917313"></a>Returned Values</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.459999999999994%" id="mcps1.1.3.1.2"><p id="p540582617313"><a name="p540582617313"></a><a name="p540582617313"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3521879917313"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p3415046017313"><a name="p3415046017313"></a><a name="p3415046017313"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p1472385717313"><a name="p1472385717313"></a><a name="p1472385717313"></a>Request error.</p>
    </td>
    </tr>
    <tr id="row5178178317313"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p3357490117313"><a name="p3357490117313"></a><a name="p3357490117313"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p3521250017313"><a name="p3521250017313"></a><a name="p3521250017313"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row4847705217313"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p3432710217313"><a name="p3432710217313"></a><a name="p3432710217313"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p2903189317313"><a name="p2903189317313"></a><a name="p2903189317313"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="row48061152191227"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p24571129191230"><a name="p24571129191230"></a><a name="p24571129191230"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p44104462191230"><a name="p44104462191230"></a><a name="p44104462191230"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row5996045217313"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p2495845317313"><a name="p2495845317313"></a><a name="p2495845317313"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p836881417313"><a name="p836881417313"></a><a name="p836881417313"></a>Internal service error.</p>
    </td>
    </tr>
    <tr id="row821047017313"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p6106831917313"><a name="p6106831917313"></a><a name="p6106831917313"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p4758680517313"><a name="p4758680517313"></a><a name="p4758680517313"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


