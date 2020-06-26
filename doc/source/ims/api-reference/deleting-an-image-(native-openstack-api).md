# Deleting an Image \(Native OpenStack API\)<a name="EN-US_TOPIC_0020092108"></a>

## Function<a name="section24723024"></a>

This API is used to delete a private image. You can only delete your own private images.

## URI<a name="section21180630"></a>

DELETE /v2/images/\{image\_id\}

[Table 1](#table27262282)  lists the parameters in the URI.

**Table  1**  Parameter description

<a name="table27262282"></a>
<table><thead align="left"><tr id="row27551015"><th class="cellrowborder" valign="top" width="25.75%" id="mcps1.2.5.1.1"><p id="p17039762"><a name="p17039762"></a><a name="p17039762"></a><strong id="b1415227516105"><a name="b1415227516105"></a><a name="b1415227516105"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="24.81%" id="mcps1.2.5.1.2"><p id="p38043494"><a name="p38043494"></a><a name="p38043494"></a><strong id="b3505224916109"><a name="b3505224916109"></a><a name="b3505224916109"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="18.61%" id="mcps1.2.5.1.3"><p id="p1119157921331"><a name="p1119157921331"></a><a name="p1119157921331"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="30.830000000000002%" id="mcps1.2.5.1.4"><p id="p61624137"><a name="p61624137"></a><a name="p61624137"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row25499238"><td class="cellrowborder" valign="top" width="25.75%" headers="mcps1.2.5.1.1 "><p id="p52172387"><a name="p52172387"></a><a name="p52172387"></a>image_id</p>
</td>
<td class="cellrowborder" valign="top" width="24.81%" headers="mcps1.2.5.1.2 "><p id="p65213800"><a name="p65213800"></a><a name="p65213800"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.5.1.3 "><p id="p3410274521331"><a name="p3410274521331"></a><a name="p3410274521331"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="30.830000000000002%" headers="mcps1.2.5.1.4 "><p id="p47826462"><a name="p47826462"></a><a name="p47826462"></a>Specifies the image ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section56407950"></a>

-   Request parameters

    <a name="table53011268153646"></a>
    <table><thead align="left"><tr id="row8255548153646"><th class="cellrowborder" valign="top" width="24%" id="mcps1.1.5.1.1"><p id="p64719651153646"><a name="p64719651153646"></a><a name="p64719651153646"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.35%" id="mcps1.1.5.1.2"><p id="p7800370153646"><a name="p7800370153646"></a><a name="p7800370153646"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.709999999999999%" id="mcps1.1.5.1.3"><p id="p27850258153646"><a name="p27850258153646"></a><a name="p27850258153646"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="43.94%" id="mcps1.1.5.1.4"><p id="p41278443153646"><a name="p41278443153646"></a><a name="p41278443153646"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row55219556153646"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.5.1.1 "><p id="p43599013153646"><a name="p43599013153646"></a><a name="p43599013153646"></a>delete_backup</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.35%" headers="mcps1.1.5.1.2 "><p id="p41859159153646"><a name="p41859159153646"></a><a name="p41859159153646"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.709999999999999%" headers="mcps1.1.5.1.3 "><p id="p35148705153646"><a name="p35148705153646"></a><a name="p35148705153646"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.94%" headers="mcps1.1.5.1.4 "><p id="p19281151510248"><a name="p19281151510248"></a><a name="p19281151510248"></a>Specifies whether to delete the CSBS backups associated with a full-ECS image when the image is deleted. The value can be <strong id="b62101047165618"><a name="b62101047165618"></a><a name="b62101047165618"></a>true</strong> or <strong id="b2210194705616"><a name="b2210194705616"></a><a name="b2210194705616"></a>false</strong>.</p>
    <a name="ul832061319479"></a><a name="ul832061319479"></a><ul id="ul832061319479"><li><strong id="b1252813912105"><a name="b1252813912105"></a><a name="b1252813912105"></a>true</strong>: When a full-ECS image is deleted, its CSBS backups are also deleted.</li><li><strong id="b419911110596"><a name="b419911110596"></a><a name="b419911110596"></a>false</strong>: When a full-ECS image is deleted, its CSBS backups are not deleted.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    DELETE https://{Endpoint}/v2/images/4ca46bf1-5c61-48ff-b4f3-0ad4e5e3ba90
    ```

    ```
    {
        "delete_backup": true
    }
    ```


## Response<a name="section37909503"></a>

-   Response parameters

    None

-   Example response

    ```
    STATUS CODE 204
    ```


## Returned Values<a name="section5641212"></a>

-   Normal

    204

-   Abnormal

    <a name="table5314667917313"></a>
    <table><thead align="left"><tr id="row4648913117313"><th class="cellrowborder" valign="top" width="46.54%" id="mcps1.1.3.1.1"><p id="p752327917313"><a name="p752327917313"></a><a name="p752327917313"></a><strong id="b23710173161024"><a name="b23710173161024"></a><a name="b23710173161024"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.459999999999994%" id="mcps1.1.3.1.2"><p id="p540582617313"><a name="p540582617313"></a><a name="p540582617313"></a><strong id="b49381322161029"><a name="b49381322161029"></a><a name="b49381322161029"></a>Description</strong></p>
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


