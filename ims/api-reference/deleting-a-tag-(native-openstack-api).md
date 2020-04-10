# Deleting a Tag \(Native OpenStack API\)<a name="EN-US_TOPIC_0020091553"></a>

## Function<a name="section18389930"></a>

This API is used to delete a custom tag from a private image.

## URI<a name="section31291646"></a>

DELETE /v2/images/\{image\_id\}/tags/\{tag\}

[Table 1](#table25869170205722)  lists the parameters in the URI.

**Table  1**  Parameter description

<a name="table25869170205722"></a>
<table><thead align="left"><tr id="row8391193205722"><th class="cellrowborder" valign="top" width="21.43%" id="mcps1.2.5.1.1"><p id="p8598055205722"><a name="p8598055205722"></a><a name="p8598055205722"></a><strong id="b45514793161911"><a name="b45514793161911"></a><a name="b45514793161911"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="29.509999999999998%" id="mcps1.2.5.1.2"><p id="p25353829205722"><a name="p25353829205722"></a><a name="p25353829205722"></a><strong id="b26302767161914"><a name="b26302767161914"></a><a name="b26302767161914"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="18.23%" id="mcps1.2.5.1.3"><p id="p40394235205722"><a name="p40394235205722"></a><a name="p40394235205722"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="30.830000000000002%" id="mcps1.2.5.1.4"><p id="p50707602205722"><a name="p50707602205722"></a><a name="p50707602205722"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row13675089205722"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.5.1.1 "><p id="p33940449205722"><a name="p33940449205722"></a><a name="p33940449205722"></a>image_id</p>
</td>
<td class="cellrowborder" valign="top" width="29.509999999999998%" headers="mcps1.2.5.1.2 "><p id="p64821866205722"><a name="p64821866205722"></a><a name="p64821866205722"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.23%" headers="mcps1.2.5.1.3 "><p id="p16079763205722"><a name="p16079763205722"></a><a name="p16079763205722"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="30.830000000000002%" headers="mcps1.2.5.1.4 "><p id="p27392388205722"><a name="p27392388205722"></a><a name="p27392388205722"></a>Specifies the image ID.</p>
</td>
</tr>
<tr id="row45204903205722"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.5.1.1 "><p id="p37718552205722"><a name="p37718552205722"></a><a name="p37718552205722"></a>tag</p>
</td>
<td class="cellrowborder" valign="top" width="29.509999999999998%" headers="mcps1.2.5.1.2 "><p id="p35303910205722"><a name="p35303910205722"></a><a name="p35303910205722"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.23%" headers="mcps1.2.5.1.3 "><p id="p41044472205722"><a name="p41044472205722"></a><a name="p41044472205722"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="30.830000000000002%" headers="mcps1.2.5.1.4 "><p id="p36267959205722"><a name="p36267959205722"></a><a name="p36267959205722"></a>Specifies the image tag.</p>
<p id="p15777461117"><a name="p15777461117"></a><a name="p15777461117"></a>The tag can contain only digits, letters, underscores (_), and hyphens (-).</p>
<p id="p58738960"><a name="p58738960"></a><a name="p58738960"></a></p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section13189358"></a>

-   Request parameters

    None

-   Example request

    ```
    DELETE https://{Endpoint}/v2/images/4ca46bf1-5c61-48ff-b4f3-0ad4e5e3ba90/tags/aaaa
    ```


## Response<a name="section51595365"></a>

-   Response parameters

    None

-   Example response

    ```
    STATUS CODE 204
    ```


## Returned Values<a name="section61705107"></a>

-   Normal

    204

-   Abnormal

    <a name="table2557613417418"></a>
    <table><thead align="left"><tr id="row2726860617418"><th class="cellrowborder" valign="top" width="46.54%" id="mcps1.1.3.1.1"><p id="p6127347417418"><a name="p6127347417418"></a><a name="p6127347417418"></a><strong id="b24036155161927"><a name="b24036155161927"></a><a name="b24036155161927"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.459999999999994%" id="mcps1.1.3.1.2"><p id="p6420439117418"><a name="p6420439117418"></a><a name="p6420439117418"></a><strong id="b58806940161930"><a name="b58806940161930"></a><a name="b58806940161930"></a>Description</strong></p>
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


