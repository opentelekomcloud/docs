# Deleting an Image Member \(Native OpenStack API\)<a name="EN-US_TOPIC_0036994321"></a>

## Function<a name="section29995926"></a>

This API is used to stop image sharing by deleting the tenant with whom the image is shared.

## URI<a name="section1527883"></a>

DELETE /v2/images/\{image\_id\}/members/\{member\_id\}

[Table 1](#table6209770492526)  lists the parameters in the URI.

**Table  1**  Parameter description

<a name="table6209770492526"></a>
<table><thead align="left"><tr id="row4392035892526"><th class="cellrowborder" valign="top" width="19.73802619738026%" id="mcps1.2.5.1.1"><p id="p77928492526"><a name="p77928492526"></a><a name="p77928492526"></a><strong id="b16263767162443"><a name="b16263767162443"></a><a name="b16263767162443"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19.358064193580642%" id="mcps1.2.5.1.2"><p id="p6312205492526"><a name="p6312205492526"></a><a name="p6312205492526"></a><strong id="b31986159162448"><a name="b31986159162448"></a><a name="b31986159162448"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="18.418158184181582%" id="mcps1.2.5.1.3"><p id="p1261277392526"><a name="p1261277392526"></a><a name="p1261277392526"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="42.48575142485752%" id="mcps1.2.5.1.4"><p id="p1500168892526"><a name="p1500168892526"></a><a name="p1500168892526"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row717722492526"><td class="cellrowborder" valign="top" width="19.73802619738026%" headers="mcps1.2.5.1.1 "><p id="p4448425292526"><a name="p4448425292526"></a><a name="p4448425292526"></a>image_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.358064193580642%" headers="mcps1.2.5.1.2 "><p id="p4645465392526"><a name="p4645465392526"></a><a name="p4645465392526"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.418158184181582%" headers="mcps1.2.5.1.3 "><p id="p473051492526"><a name="p473051492526"></a><a name="p473051492526"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.48575142485752%" headers="mcps1.2.5.1.4 "><p id="p4762733192526"><a name="p4762733192526"></a><a name="p4762733192526"></a>Specifies the image ID.</p>
</td>
</tr>
<tr id="row2599280292526"><td class="cellrowborder" valign="top" width="19.73802619738026%" headers="mcps1.2.5.1.1 "><p id="p2504225092526"><a name="p2504225092526"></a><a name="p2504225092526"></a>member_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.358064193580642%" headers="mcps1.2.5.1.2 "><p id="p1515635492526"><a name="p1515635492526"></a><a name="p1515635492526"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.418158184181582%" headers="mcps1.2.5.1.3 "><p id="p1970513892526"><a name="p1970513892526"></a><a name="p1970513892526"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.48575142485752%" headers="mcps1.2.5.1.4 "><p id="p5261235592526"><a name="p5261235592526"></a><a name="p5261235592526"></a>Specifies the member ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section13750947"></a>

-   Request parameters

    None

-   Example request

    ```
    DELETE https://{Endpoint}/v2/images/d164b5df-1bc3-4c3f-893e-3e471fd16e64/members/edc89b490d7d4392898e19b2deb34797
    ```


## Response<a name="section56649665"></a>

-   Response parameters

    None

-   Example response

    ```
    204 No Content
    ```


## Returned Values<a name="section61705107"></a>

-   Normal

    204

-   Abnormal

    <a name="table2557613417418"></a>
    <table><thead align="left"><tr id="row2726860617418"><th class="cellrowborder" valign="top" width="46.54%" id="mcps1.1.3.1.1"><p id="p6127347417418"><a name="p6127347417418"></a><a name="p6127347417418"></a><strong id="b41488565204450"><a name="b41488565204450"></a><a name="b41488565204450"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.459999999999994%" id="mcps1.1.3.1.2"><p id="p6420439117418"><a name="p6420439117418"></a><a name="p6420439117418"></a><strong id="b84235270616929"><a name="b84235270616929"></a><a name="b84235270616929"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3317320517418"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p267505917418"><a name="p267505917418"></a><a name="p267505917418"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p1535319317418"><a name="p1535319317418"></a><a name="p1535319317418"></a>Request error.</p>
    </td>
    </tr>
    <tr id="row396101317418"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p5240662717418"><a name="p5240662717418"></a><a name="p5240662717418"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p1707839817418"><a name="p1707839817418"></a><a name="p1707839817418"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row1948785517418"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p3501244017418"><a name="p3501244017418"></a><a name="p3501244017418"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p1743536117418"><a name="p1743536117418"></a><a name="p1743536117418"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="row66661301191255"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p26317130191257"><a name="p26317130191257"></a><a name="p26317130191257"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p51312824191257"><a name="p51312824191257"></a><a name="p51312824191257"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row2270052117418"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p2680288517418"><a name="p2680288517418"></a><a name="p2680288517418"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p2355010217418"><a name="p2355010217418"></a><a name="p2355010217418"></a>Internal service error.</p>
    </td>
    </tr>
    <tr id="row1062433417418"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p5526474517418"><a name="p5526474517418"></a><a name="p5526474517418"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p4725937317418"><a name="p4725937317418"></a><a name="p4725937317418"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


