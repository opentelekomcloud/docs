# Querying the DNS API Version<a name="dns_api_61002"></a>

## Function<a name="section3569153217343"></a>

Query a specified DNS API version.

To be interconnected with a third-party system, the current DNS version supports 1024- and 2048-bit DH key exchange algorithms, and the 2048-bit algorithm is recommended.

## URI<a name="section6163262617350"></a>

GET /\{version\}

For details, see  [Table 1](#table14024165).

**Table  1**  Parameter in the URI

<a name="table14024165"></a>
<table><thead align="left"><tr id="row26592044"><th class="cellrowborder" valign="top" width="15.459999999999999%" id="mcps1.2.5.1.1"><p id="p6471942"><a name="p6471942"></a><a name="p6471942"></a><strong id="b162774213314533_1"><a name="b162774213314533_1"></a><a name="b162774213314533_1"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.459999999999999%" id="mcps1.2.5.1.2"><p id="p54465313"><a name="p54465313"></a><a name="p54465313"></a><strong id="b593421527191713"><a name="b593421527191713"></a><a name="b593421527191713"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.53%" id="mcps1.2.5.1.3"><p id="p49614245"><a name="p49614245"></a><a name="p49614245"></a><strong id="b7804141120356_1"><a name="b7804141120356_1"></a><a name="b7804141120356_1"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51.55%" id="mcps1.2.5.1.4"><p id="p59330872"><a name="p59330872"></a><a name="p59330872"></a><strong id="b842352706112423_1"><a name="b842352706112423_1"></a><a name="b842352706112423_1"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row41071365"><td class="cellrowborder" valign="top" width="15.459999999999999%" headers="mcps1.2.5.1.1 "><p id="p38446258"><a name="p38446258"></a><a name="p38446258"></a>version</p>
</td>
<td class="cellrowborder" valign="top" width="15.459999999999999%" headers="mcps1.2.5.1.2 "><p id="p27139175"><a name="p27139175"></a><a name="p27139175"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.53%" headers="mcps1.2.5.1.3 "><p id="p50789581"><a name="p50789581"></a><a name="p50789581"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.55%" headers="mcps1.2.5.1.4 "><p id="p20315403"><a name="p20315403"></a><a name="p20315403"></a>Version to be queried, which starts with <strong id="b842352706141446"><a name="b842352706141446"></a><a name="b842352706141446"></a>v</strong>, for example, <strong id="b842352706141516"><a name="b842352706141516"></a><a name="b842352706141516"></a>v2</strong></p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section4207148117353"></a>

-   Request parameters

    None

-   Example request

    Query information about the v2 API version.

    ```
    GET https://{DNS_Endpoint}/v2
    ```


## Response<a name="section01535143610"></a>

-   Parameter description

    **Table  2**  Parameter in the response

    <a name="table6255205892049"></a>
    <table><thead align="left"><tr id="row1727035092049"><th class="cellrowborder" valign="top" width="18.18%" id="mcps1.2.4.1.1"><p id="p5672109992049"><a name="p5672109992049"></a><a name="p5672109992049"></a><strong id="b162774213314533_3"><a name="b162774213314533_3"></a><a name="b162774213314533_3"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.189999999999998%" id="mcps1.2.4.1.2"><p id="p3100628892049"><a name="p3100628892049"></a><a name="p3100628892049"></a><strong id="b7804141120356_3"><a name="b7804141120356_3"></a><a name="b7804141120356_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="62.629999999999995%" id="mcps1.2.4.1.3"><p id="p2848141492049"><a name="p2848141492049"></a><a name="p2848141492049"></a><strong id="b842352706112423_3"><a name="b842352706112423_3"></a><a name="b842352706112423_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2529320492049"><td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.1 "><p id="p3548368392049"><a name="p3548368392049"></a><a name="p3548368392049"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p5560610792049"><a name="p5560610792049"></a><a name="p5560610792049"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.629999999999995%" headers="mcps1.2.4.1.3 "><p id="p780080392049"><a name="p780080392049"></a><a name="p780080392049"></a>Version object. For details, see <a href="#table3345872992049">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Description of the  **version**  field

    <a name="table3345872992049"></a>
    <table><thead align="left"><tr id="row4161787792049"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.1"><p id="p1560490192049"><a name="p1560490192049"></a><a name="p1560490192049"></a><strong id="b162774213314533_5"><a name="b162774213314533_5"></a><a name="b162774213314533_5"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.2"><p id="p5603748692049"><a name="p5603748692049"></a><a name="p5603748692049"></a><strong id="b7804141120356_5"><a name="b7804141120356_5"></a><a name="b7804141120356_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="63%" id="mcps1.2.4.1.3"><p id="p4274248792049"><a name="p4274248792049"></a><a name="p4274248792049"></a><strong id="b842352706112423_5"><a name="b842352706112423_5"></a><a name="b842352706112423_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3958938492049"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p5262353092049"><a name="p5262353092049"></a><a name="p5262353092049"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p3464752492049"><a name="p3464752492049"></a><a name="p3464752492049"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p848217563142"><a name="p848217563142"></a><a name="p848217563142"></a>Version status, which can be:</p>
    <a name="ul1897113391488"></a><a name="ul1897113391488"></a><ul id="ul1897113391488"><li><strong id="b04019265257"><a name="b04019265257"></a><a name="b04019265257"></a>CURRENT</strong>: widely used version</li><li><strong id="b176585275259"><a name="b176585275259"></a><a name="b176585275259"></a>SUPPORTED</strong>: earlier version which is still supported</li><li><strong id="b16212132942515"><a name="b16212132942515"></a><a name="b16212132942515"></a>DEPRECATED</strong>: deprecated version which may be deleted later</li></ul>
    </td>
    </tr>
    <tr id="row2511266892049"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p2086025192049"><a name="p2086025192049"></a><a name="p2086025192049"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p1195876692049"><a name="p1195876692049"></a><a name="p1195876692049"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p2913599892049"><a name="p2913599892049"></a><a name="p2913599892049"></a>Version number, for example, <strong id="b84235270614227"><a name="b84235270614227"></a><a name="b84235270614227"></a>v2</strong></p>
    </td>
    </tr>
    <tr id="row15102829192914"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p5102192912291"><a name="p5102192912291"></a><a name="p5102192912291"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p1710232902916"><a name="p1710232902916"></a><a name="p1710232902916"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p1410222992917"><a name="p1410222992917"></a><a name="p1410222992917"></a>Time when the API version was released</p>
    <p id="p1481431019435"><a name="p1481431019435"></a><a name="p1481431019435"></a>The UTC time format is used: YYYY-MM-DDTHH:MM:SSZ.</p>
    </td>
    </tr>
    <tr id="row6155145713164"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p81562578165"><a name="p81562578165"></a><a name="p81562578165"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p161560570169"><a name="p161560570169"></a><a name="p161560570169"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p138029367173"><a name="p138029367173"></a><a name="p138029367173"></a>Maximum micro-version number. If the APIs do not support micro-versions, the value is left blank.</p>
    </td>
    </tr>
    <tr id="row5867187131816"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p586811716185"><a name="p586811716185"></a><a name="p586811716185"></a>min_version</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p1686820701814"><a name="p1686820701814"></a><a name="p1686820701814"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p8453122951815"><a name="p8453122951815"></a><a name="p8453122951815"></a>Minimum micro-version number. If the APIs do not support micro-versions, the value is left blank.</p>
    </td>
    </tr>
    <tr id="row6089739292049"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p3374170192049"><a name="p3374170192049"></a><a name="p3374170192049"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p4872327592049"><a name="p4872327592049"></a><a name="p4872327592049"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p5427120992049"><a name="p5427120992049"></a><a name="p5427120992049"></a>URL of the current version. For details, see <a href="#table0172144213344">Table 4</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  Description of the  **links**  field

    <a name="table0172144213344"></a>
    <table><thead align="left"><tr id="row917304253418"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.1"><p id="p101731742153416"><a name="p101731742153416"></a><a name="p101731742153416"></a><strong id="b72591837112616"><a name="b72591837112616"></a><a name="b72591837112616"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.25%" id="mcps1.2.4.1.2"><p id="p0174542163418"><a name="p0174542163418"></a><a name="p0174542163418"></a><strong id="b1837055"><a name="b1837055"></a><a name="b1837055"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="62.74999999999999%" id="mcps1.2.4.1.3"><p id="p7174194243414"><a name="p7174194243414"></a><a name="p7174194243414"></a><strong id="b116191914172617"><a name="b116191914172617"></a><a name="b116191914172617"></a>Description</strong></p>
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
            "version": 
                {
                    "status": "CURRENT",
                    "id": "v2",
                    "links": [
                        {
                            "href": "https://Endpoint/v2/",
                            "rel": "self"
                        }
                    ],
                "min_version": "",
                "updated": "2018-09-18T00:00:00Z",
                "version": ""
                }
    }
    ```


## Returned Value<a name="section9249181042119"></a>

If the API call returns a code of 2_xx_, for example, 200, 202, or 204, the request is successful.

For details, see  [Status Code](status-code.md).

