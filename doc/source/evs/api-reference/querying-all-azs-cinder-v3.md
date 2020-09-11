# Querying All AZs<a name="evs_04_3045"></a>

## Function<a name="section54465313"></a>

This API is used to query all AZs.

## URI<a name="section20425774"></a>

-   URI format

    GET /v3/\{project\_id\}/os-availability-zone

-   Parameter description

    <a name="table34934986"></a>
    <table><thead align="left"><tr id="row15816986"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="p6107499"><a name="p6107499"></a><a name="p6107499"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.362036203620363%" id="mcps1.1.4.1.2"><p id="p24945412"><a name="p24945412"></a><a name="p24945412"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.30463046304631%" id="mcps1.1.4.1.3"><p id="p7312526"><a name="p7312526"></a><a name="p7312526"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row55443761"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p61759636"><a name="p61759636"></a><a name="p61759636"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.362036203620363%" headers="mcps1.1.4.1.2 "><p id="p36474591"><a name="p36474591"></a><a name="p36474591"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.30463046304631%" headers="mcps1.1.4.1.3 "><p id="p1651899"><a name="p1651899"></a><a name="p1651899"></a>Specifies the project ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section49614245"></a>

-   Example request

    ```
    GET https://{endpoint}/v3/{project_id}/os-availability-zone
    ```


## Response<a name="section43875021"></a>

-   Parameter description

    <a name="evs_04_2081_table201437992512"></a>
    <table><thead align="left"><tr id="evs_04_2081_row1414420917255"><th class="cellrowborder" valign="top" width="21.18%" id="mcps1.1.4.1.1"><p id="evs_04_2081_p11144139152511"><a name="evs_04_2081_p11144139152511"></a><a name="evs_04_2081_p11144139152511"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.35%" id="mcps1.1.4.1.2"><p id="evs_04_2081_p1014419152512"><a name="evs_04_2081_p1014419152512"></a><a name="evs_04_2081_p1014419152512"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.47%" id="mcps1.1.4.1.3"><p id="evs_04_2081_p16144994250"><a name="evs_04_2081_p16144994250"></a><a name="evs_04_2081_p16144994250"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2081_row181446912510"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="evs_04_2081_p13144119162511"><a name="evs_04_2081_p13144119162511"></a><a name="evs_04_2081_p13144119162511"></a>availabilityZoneInfo</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="evs_04_2081_p214416911255"><a name="evs_04_2081_p214416911255"></a><a name="evs_04_2081_p214416911255"></a>list</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="evs_04_2081_p01441910254"><a name="evs_04_2081_p01441910254"></a><a name="evs_04_2081_p01441910254"></a>Specifies the list of queried AZs. For details, see <a href="#evs_04_2081_li19751007201910">Parameters in the availabilityZoneInfo field</a>.</p>
    </td>
    </tr>
    <tr id="evs_04_2081_row6109186192812"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="evs_04_2081_p129522216412"><a name="evs_04_2081_p129522216412"></a><a name="evs_04_2081_p129522216412"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="evs_04_2081_p1595262111415"><a name="evs_04_2081_p1595262111415"></a><a name="evs_04_2081_p1595262111415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="evs_04_2081_p109527215417"><a name="evs_04_2081_p109527215417"></a><a name="evs_04_2081_p109527215417"></a>Specifies the error message returned when an error occurs. For details, see <a href="#evs_04_2081_li0419202382514">Parameters in the error field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="evs_04_2081_li19751007201910"></a>Parameters in the  **availabilityZoneInfo**  field

    <a name="evs_04_2081_table43541335201910"></a>
    <table><thead align="left"><tr id="evs_04_2081_row45002232201910"><th class="cellrowborder" valign="top" width="21.18%" id="mcps1.1.4.1.1"><p id="evs_04_2081_p21302142201910"><a name="evs_04_2081_p21302142201910"></a><a name="evs_04_2081_p21302142201910"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.35%" id="mcps1.1.4.1.2"><p id="evs_04_2081_p523569515640"><a name="evs_04_2081_p523569515640"></a><a name="evs_04_2081_p523569515640"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.47%" id="mcps1.1.4.1.3"><p id="evs_04_2081_p42702004201910"><a name="evs_04_2081_p42702004201910"></a><a name="evs_04_2081_p42702004201910"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2081_row36310324201910"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="evs_04_2081_p55455149201910"><a name="evs_04_2081_p55455149201910"></a><a name="evs_04_2081_p55455149201910"></a>zoneState</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="evs_04_2081_p2143812515640"><a name="evs_04_2081_p2143812515640"></a><a name="evs_04_2081_p2143812515640"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="evs_04_2081_p44081575201910"><a name="evs_04_2081_p44081575201910"></a><a name="evs_04_2081_p44081575201910"></a>Specifies the status of the AZ. For details, see <a href="#evs_04_2081_li11149334112511">Parameter in the zoneState field</a>.</p>
    </td>
    </tr>
    <tr id="evs_04_2081_row61189858201910"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="evs_04_2081_p57431491201910"><a name="evs_04_2081_p57431491201910"></a><a name="evs_04_2081_p57431491201910"></a>zoneName</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="evs_04_2081_p5876653115640"><a name="evs_04_2081_p5876653115640"></a><a name="evs_04_2081_p5876653115640"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="evs_04_2081_p58856323201910"><a name="evs_04_2081_p58856323201910"></a><a name="evs_04_2081_p58856323201910"></a>Specifies the AZ name.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="evs_04_2081_li11149334112511"></a>Parameter in the  **zoneState**  field

    <a name="evs_04_2081_table915023482516"></a>
    <table><thead align="left"><tr id="evs_04_2081_row4150434152517"><th class="cellrowborder" valign="top" width="21.18%" id="mcps1.1.4.1.1"><p id="evs_04_2081_p1215093419253"><a name="evs_04_2081_p1215093419253"></a><a name="evs_04_2081_p1215093419253"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.35%" id="mcps1.1.4.1.2"><p id="evs_04_2081_p3150193412259"><a name="evs_04_2081_p3150193412259"></a><a name="evs_04_2081_p3150193412259"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.47%" id="mcps1.1.4.1.3"><p id="evs_04_2081_p1215014346259"><a name="evs_04_2081_p1215014346259"></a><a name="evs_04_2081_p1215014346259"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2081_row2150534192516"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="evs_04_2081_p115073413258"><a name="evs_04_2081_p115073413258"></a><a name="evs_04_2081_p115073413258"></a>available</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="evs_04_2081_p915013462516"><a name="evs_04_2081_p915013462516"></a><a name="evs_04_2081_p915013462516"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><div class="p" id="evs_04_2081_p171501234112510"><a name="evs_04_2081_p171501234112510"></a><a name="evs_04_2081_p171501234112510"></a>Specifies whether the AZ is available.<a name="evs_04_2081_ul315013410258"></a><a name="evs_04_2081_ul315013410258"></a><ul id="evs_04_2081_ul315013410258"><li><strong id="evs_04_2081_b43493744616"><a name="evs_04_2081_b43493744616"></a><a name="evs_04_2081_b43493744616"></a>true</strong>: available</li><li><strong id="evs_04_2081_b643617390464"><a name="evs_04_2081_b643617390464"></a><a name="evs_04_2081_b643617390464"></a>false</strong>: unavailable</li></ul>
    </div>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="evs_04_2081_li0419202382514"></a>Parameters in the  **error**  field

    <a name="evs_04_2081_evs_04_2013_table15441099103019"></a>
    <table><thead align="left"><tr id="evs_04_2081_evs_04_2013_row54094047103019"><th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.1"><p id="evs_04_2081_evs_04_2013_p19541716103019"><a name="evs_04_2081_evs_04_2013_p19541716103019"></a><a name="evs_04_2081_evs_04_2013_p19541716103019"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.2"><p id="evs_04_2081_evs_04_2013_p39375186103019"><a name="evs_04_2081_evs_04_2013_p39375186103019"></a><a name="evs_04_2081_evs_04_2013_p39375186103019"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.64423557644236%" id="mcps1.1.4.1.3"><p id="evs_04_2081_evs_04_2013_p38578950103019"><a name="evs_04_2081_evs_04_2013_p38578950103019"></a><a name="evs_04_2081_evs_04_2013_p38578950103019"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2081_evs_04_2013_row59401790103019"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="evs_04_2081_evs_04_2013_p46815658103019"><a name="evs_04_2081_evs_04_2013_p46815658103019"></a><a name="evs_04_2081_evs_04_2013_p46815658103019"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="evs_04_2081_evs_04_2013_p33971979103019"><a name="evs_04_2081_evs_04_2013_p33971979103019"></a><a name="evs_04_2081_evs_04_2013_p33971979103019"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="evs_04_2081_evs_04_2013_p21623243103019"><a name="evs_04_2081_evs_04_2013_p21623243103019"></a><a name="evs_04_2081_evs_04_2013_p21623243103019"></a>Specifies the error message returned when an error occurs.</p>
    </td>
    </tr>
    <tr id="evs_04_2081_evs_04_2013_row60391466103019"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="evs_04_2081_evs_04_2013_p59870541103019"><a name="evs_04_2081_evs_04_2013_p59870541103019"></a><a name="evs_04_2081_evs_04_2013_p59870541103019"></a>code</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="evs_04_2081_evs_04_2013_p17675690103019"><a name="evs_04_2081_evs_04_2013_p17675690103019"></a><a name="evs_04_2081_evs_04_2013_p17675690103019"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="evs_04_2081_evs_04_2013_p6087468103019"><a name="evs_04_2081_evs_04_2013_p6087468103019"></a><a name="evs_04_2081_evs_04_2013_p6087468103019"></a>Specifies the error code returned when an error occurs.</p>
    <p id="evs_04_2081_evs_04_2013_p54787218103019"><a name="evs_04_2081_evs_04_2013_p54787218103019"></a><a name="evs_04_2081_evs_04_2013_p54787218103019"></a>For details about the error code, see <a href="error-codes.md">Error Codes</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "availabilityZoneInfo": [
            {
                "zoneState": {
                    "available": true
                }, 
                "zoneName": "az-dc-1"
            }
        ]
    }
    ```

    or

    ```
    {
        "error": {
            "message": "XXXX", 
            "code": "XXX"
        }
    }
    ```


## Status Codes<a name="section59330872"></a>

-   Normal

    200


## Error Codes<a name="section431317151242"></a>

For details, see  [Error Codes](error-codes.md).

