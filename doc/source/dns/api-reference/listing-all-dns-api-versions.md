# Listing All DNS API Versions<a name="dns_api_61001"></a>

## Function<a name="section3569153217343"></a>

List all DNS API versions.

To be interconnected with a third-party system, the current DNS version supports 1024- and 2048-bit DH key exchange algorithms, and the 2048-bit algorithm is recommended.

## URI<a name="section6163262617350"></a>

GET /

## Request<a name="section84941832125012"></a>

-   Request parameters

    None

-   Example request

    List all DNS API versions.

    ```
    GET https://{DNS_Endpoint}/
    ```


## Response<a name="section2142173017358"></a>

-   Parameter description

    **Table  1**  Parameter in the response

    <a name="table6255205892049"></a>
    <table><thead align="left"><tr id="row1727035092049"><th class="cellrowborder" valign="top" width="20.247975202479754%" id="mcps1.2.4.1.1"><p id="p5672109992049"><a name="p5672109992049"></a><a name="p5672109992049"></a><strong id="b162774213314533_1"><a name="b162774213314533_1"></a><a name="b162774213314533_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.568043195680435%" id="mcps1.2.4.1.2"><p id="p3100628892049"><a name="p3100628892049"></a><a name="p3100628892049"></a><strong id="b84235270619112_1"><a name="b84235270619112_1"></a><a name="b84235270619112_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="60.18398160183982%" id="mcps1.2.4.1.3"><p id="p2848141492049"><a name="p2848141492049"></a><a name="p2848141492049"></a><strong id="b842352706112423_1"><a name="b842352706112423_1"></a><a name="b842352706112423_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2529320492049"><td class="cellrowborder" valign="top" width="20.247975202479754%" headers="mcps1.2.4.1.1 "><p id="p3548368392049"><a name="p3548368392049"></a><a name="p3548368392049"></a>versions</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.568043195680435%" headers="mcps1.2.4.1.2 "><p id="p5560610792049"><a name="p5560610792049"></a><a name="p5560610792049"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.18398160183982%" headers="mcps1.2.4.1.3 "><p id="p780080392049"><a name="p780080392049"></a><a name="p780080392049"></a>Version object. For details, see <a href="#table2788528392049">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Description of the  **versions**  field

    <a name="table2788528392049"></a>
    <table><thead align="left"><tr id="row100602392049"><th class="cellrowborder" valign="top" width="20.437956204379564%" id="mcps1.2.4.1.1"><p id="p1437906692049"><a name="p1437906692049"></a><a name="p1437906692049"></a><strong id="b162774213314533_3"><a name="b162774213314533_3"></a><a name="b162774213314533_3"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.37806219378062%" id="mcps1.2.4.1.2"><p id="p2385367792049"><a name="p2385367792049"></a><a name="p2385367792049"></a><strong id="b84235270619112_3"><a name="b84235270619112_3"></a><a name="b84235270619112_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="60.18398160183982%" id="mcps1.2.4.1.3"><p id="p5309965692049"><a name="p5309965692049"></a><a name="p5309965692049"></a><strong id="b842352706112423_3"><a name="b842352706112423_3"></a><a name="b842352706112423_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row610488492049"><td class="cellrowborder" valign="top" width="20.437956204379564%" headers="mcps1.2.4.1.1 "><p id="p2473359292049"><a name="p2473359292049"></a><a name="p2473359292049"></a>values</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.37806219378062%" headers="mcps1.2.4.1.2 "><p id="p5726396592049"><a name="p5726396592049"></a><a name="p5726396592049"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.18398160183982%" headers="mcps1.2.4.1.3 "><p id="p786961192049"><a name="p786961192049"></a><a name="p786961192049"></a>Version list. For details, see <a href="#table3345872992049">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Description of the  **values**  field

    <a name="table3345872992049"></a>
    <table><thead align="left"><tr id="row4161787792049"><th class="cellrowborder" valign="top" width="18.18%" id="mcps1.2.4.1.1"><p id="p1560490192049"><a name="p1560490192049"></a><a name="p1560490192049"></a><strong id="b162774213314533_5"><a name="b162774213314533_5"></a><a name="b162774213314533_5"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.189999999999998%" id="mcps1.2.4.1.2"><p id="p5603748692049"><a name="p5603748692049"></a><a name="p5603748692049"></a><strong id="b84235270619112_5"><a name="b84235270619112_5"></a><a name="b84235270619112_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="62.629999999999995%" id="mcps1.2.4.1.3"><p id="p4274248792049"><a name="p4274248792049"></a><a name="p4274248792049"></a><strong id="b842352706112423_5"><a name="b842352706112423_5"></a><a name="b842352706112423_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3958938492049"><td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.1 "><p id="p5262353092049"><a name="p5262353092049"></a><a name="p5262353092049"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p3464752492049"><a name="p3464752492049"></a><a name="p3464752492049"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.629999999999995%" headers="mcps1.2.4.1.3 "><p id="p848217563142"><a name="p848217563142"></a><a name="p848217563142"></a>Version status, which can be:</p>
    <a name="ul19911143415371"></a><a name="ul19911143415371"></a><ul id="ul19911143415371"><li><strong id="b842352706115252"><a name="b842352706115252"></a><a name="b842352706115252"></a>CURRENT</strong>: widely used version</li><li><strong id="b965321614118"><a name="b965321614118"></a><a name="b965321614118"></a>SUPPORTED</strong>: earlier version which is still supported</li><li><strong id="b842352706115458"><a name="b842352706115458"></a><a name="b842352706115458"></a>DEPRECATED</strong>: deprecated version which may be deleted later</li></ul>
    </td>
    </tr>
    <tr id="row2511266892049"><td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.1 "><p id="p2086025192049"><a name="p2086025192049"></a><a name="p2086025192049"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p1195876692049"><a name="p1195876692049"></a><a name="p1195876692049"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.629999999999995%" headers="mcps1.2.4.1.3 "><p id="p2913599892049"><a name="p2913599892049"></a><a name="p2913599892049"></a>Version number</p>
    </td>
    </tr>
    <tr id="row6089739292049"><td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.1 "><p id="p3374170192049"><a name="p3374170192049"></a><a name="p3374170192049"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p4872327592049"><a name="p4872327592049"></a><a name="p4872327592049"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.629999999999995%" headers="mcps1.2.4.1.3 "><p id="p5427120992049"><a name="p5427120992049"></a><a name="p5427120992049"></a>URL of the current version. For details, see <a href="#table0172144213344">Table 4</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  Description of the  **links**  field

    <a name="table0172144213344"></a>
    <table><thead align="left"><tr id="row917304253418"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.1"><p id="p101731742153416"><a name="p101731742153416"></a><a name="p101731742153416"></a><strong id="b61661641440"><a name="b61661641440"></a><a name="b61661641440"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.25%" id="mcps1.2.4.1.2"><p id="p0174542163418"><a name="p0174542163418"></a><a name="p0174542163418"></a><strong id="b1744321241"><a name="b1744321241"></a><a name="b1744321241"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="62.74999999999999%" id="mcps1.2.4.1.3"><p id="p7174194243414"><a name="p7174194243414"></a><a name="p7174194243414"></a><strong id="b13281552192019"><a name="b13281552192019"></a><a name="b13281552192019"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1917494211345"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p13174134215348"><a name="p13174134215348"></a><a name="p13174134215348"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.25%" headers="mcps1.2.4.1.2 "><p id="p181741642173417"><a name="p181741642173417"></a><a name="p181741642173417"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.74999999999999%" headers="mcps1.2.4.1.3 "><p id="p1017434223419"><a name="p1017434223419"></a><a name="p1017434223419"></a>Link address</p>
    </td>
    </tr>
    <tr id="row455095771113"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p10551115771111"><a name="p10551115771111"></a><a name="p10551115771111"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.25%" headers="mcps1.2.4.1.2 "><p id="p17552957121114"><a name="p17552957121114"></a><a name="p17552957121114"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.74999999999999%" headers="mcps1.2.4.1.3 "><p id="p14552657201118"><a name="p14552657201118"></a><a name="p14552657201118"></a>Link marker name</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "versions": {
            "values": [
                {
                    "status": "CURRENT",
                    "id": "v2",
                    "links": [
                        {
                            "href": "https://Endpoint/v2",
                            "rel": "self"
                        }
                    ]
                }
            ]
        }
    }
    ```


## Returned Value<a name="section1917896317411"></a>

If the API call returns a code of 2_xx_, for example, 200, 202, or 204, the request is successful.

For details, see  [Status Code](status-code.md).

