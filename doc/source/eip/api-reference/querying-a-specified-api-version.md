# Querying a Specified API Version<a name="eip_openstackapi_0003"></a>

## Function<a name="en-us_topic_0201534145_section292172513710"></a>

This API is used to query the version of a specified API.

## URI<a name="en-us_topic_0201534145_section092618252375"></a>

GET /\{api\_version\}

[Table 1](#en-us_topic_0201534145_table8488410142319)  describes the parameters.

**Table  1**  Parameter description

<a name="en-us_topic_0201534145_table8488410142319"></a>
<table><thead align="left"><tr id="en-us_topic_0201534145_row9493141018236"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534145_p94981610102320"><a name="en-us_topic_0201534145_p94981610102320"></a><a name="en-us_topic_0201534145_p94981610102320"></a><strong id="en-us_topic_0201534145_b842352706193648"><a name="en-us_topic_0201534145_b842352706193648"></a><a name="en-us_topic_0201534145_b842352706193648"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534145_p12502171018236"><a name="en-us_topic_0201534145_p12502171018236"></a><a name="en-us_topic_0201534145_p12502171018236"></a><strong id="en-us_topic_0201534145_b842352706193653"><a name="en-us_topic_0201534145_b842352706193653"></a><a name="en-us_topic_0201534145_b842352706193653"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534145_p0503161052316"><a name="en-us_topic_0201534145_p0503161052316"></a><a name="en-us_topic_0201534145_p0503161052316"></a><strong id="en-us_topic_0201534145_b8423527061645"><a name="en-us_topic_0201534145_b8423527061645"></a><a name="en-us_topic_0201534145_b8423527061645"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0201534145_row050661014235"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534145_p5516910112316"><a name="en-us_topic_0201534145_p5516910112316"></a><a name="en-us_topic_0201534145_p5516910112316"></a>api_version</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534145_p1851919102230"><a name="en-us_topic_0201534145_p1851919102230"></a><a name="en-us_topic_0201534145_p1851919102230"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534145_p25212100235"><a name="en-us_topic_0201534145_p25212100235"></a><a name="en-us_topic_0201534145_p25212100235"></a>Specifies the version number, for example <strong id="en-us_topic_0201534145_b84235270685253"><a name="en-us_topic_0201534145_b84235270685253"></a><a name="en-us_topic_0201534145_b84235270685253"></a>v2.0</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="en-us_topic_0201534145_section159431125133719"></a>

-   Request parameter

    None


-   Example request

    ```
    GET https://{Endpoint}/v2.0
    ```


## Response Message<a name="en-us_topic_0201534145_section199536251373"></a>

-   Response parameter

    **Table  2**  Response parameter

    <a name="en-us_topic_0201534145_table1595322519378"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534145_row95291726133710"><th class="cellrowborder" valign="top" width="23.23%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534145_p1252992613712"><a name="en-us_topic_0201534145_p1252992613712"></a><a name="en-us_topic_0201534145_p1252992613712"></a><strong id="en-us_topic_0201534145_b22486247"><a name="en-us_topic_0201534145_b22486247"></a><a name="en-us_topic_0201534145_b22486247"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.25%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534145_p55291826163717"><a name="en-us_topic_0201534145_p55291826163717"></a><a name="en-us_topic_0201534145_p55291826163717"></a><strong id="en-us_topic_0201534145_b811117612"><a name="en-us_topic_0201534145_b811117612"></a><a name="en-us_topic_0201534145_b811117612"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="51.519999999999996%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534145_p1552913260373"><a name="en-us_topic_0201534145_p1552913260373"></a><a name="en-us_topic_0201534145_p1552913260373"></a><strong id="en-us_topic_0201534145_b535700571"><a name="en-us_topic_0201534145_b535700571"></a><a name="en-us_topic_0201534145_b535700571"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534145_row15529326203718"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534145_p8529826133712"><a name="en-us_topic_0201534145_p8529826133712"></a><a name="en-us_topic_0201534145_p8529826133712"></a>resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534145_p13529152643712"><a name="en-us_topic_0201534145_p13529152643712"></a><a name="en-us_topic_0201534145_p13529152643712"></a>Array of <a href="#en-us_topic_0201534145_table1195920258372">resource</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.519999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534145_p1852902653713"><a name="en-us_topic_0201534145_p1852902653713"></a><a name="en-us_topic_0201534145_p1852902653713"></a>Specifies the <strong id="en-us_topic_0201534145_b84235270685442"><a name="en-us_topic_0201534145_b84235270685442"></a><a name="en-us_topic_0201534145_b84235270685442"></a>resource</strong> object list.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **resource**  object

    <a name="en-us_topic_0201534145_table1195920258372"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534145_row5529132615373"><th class="cellrowborder" valign="top" width="23.23%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534145_p1252920262374"><a name="en-us_topic_0201534145_p1252920262374"></a><a name="en-us_topic_0201534145_p1252920262374"></a><strong id="en-us_topic_0201534145_b1084608877"><a name="en-us_topic_0201534145_b1084608877"></a><a name="en-us_topic_0201534145_b1084608877"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.25%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534145_p2529126123714"><a name="en-us_topic_0201534145_p2529126123714"></a><a name="en-us_topic_0201534145_p2529126123714"></a><strong id="en-us_topic_0201534145_b426919492"><a name="en-us_topic_0201534145_b426919492"></a><a name="en-us_topic_0201534145_b426919492"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="51.519999999999996%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534145_p105291226143715"><a name="en-us_topic_0201534145_p105291226143715"></a><a name="en-us_topic_0201534145_p105291226143715"></a><strong id="en-us_topic_0201534145_b1099241838"><a name="en-us_topic_0201534145_b1099241838"></a><a name="en-us_topic_0201534145_b1099241838"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534145_row1552919263377"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534145_p10529192611375"><a name="en-us_topic_0201534145_p10529192611375"></a><a name="en-us_topic_0201534145_p10529192611375"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534145_p352910264377"><a name="en-us_topic_0201534145_p352910264377"></a><a name="en-us_topic_0201534145_p352910264377"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.519999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534145_p052918269376"><a name="en-us_topic_0201534145_p052918269376"></a><a name="en-us_topic_0201534145_p052918269376"></a>Specifies the resource name.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534145_row852942611373"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534145_p1152902613374"><a name="en-us_topic_0201534145_p1152902613374"></a><a name="en-us_topic_0201534145_p1152902613374"></a>collection</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534145_p185293264370"><a name="en-us_topic_0201534145_p185293264370"></a><a name="en-us_topic_0201534145_p185293264370"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.519999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534145_p8529192614377"><a name="en-us_topic_0201534145_p8529192614377"></a><a name="en-us_topic_0201534145_p8529192614377"></a>Specifies the resource collection name.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534145_row6529726133710"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534145_p25291326103715"><a name="en-us_topic_0201534145_p25291326103715"></a><a name="en-us_topic_0201534145_p25291326103715"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534145_p2658122615326"><a name="en-us_topic_0201534145_p2658122615326"></a><a name="en-us_topic_0201534145_p2658122615326"></a>Array of <a href="#en-us_topic_0201534145_table4442151110172">link</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.519999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534145_p1252922613371"><a name="en-us_topic_0201534145_p1252922613371"></a><a name="en-us_topic_0201534145_p1252922613371"></a>Specifies the link list. For details, see <a href="#en-us_topic_0201534145_table4442151110172">Table 4</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **link**  objects

    <a name="en-us_topic_0201534145_table4442151110172"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534145_row12442181131712"><th class="cellrowborder" valign="top" width="23.23%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534145_p044251171713"><a name="en-us_topic_0201534145_p044251171713"></a><a name="en-us_topic_0201534145_p044251171713"></a><strong id="en-us_topic_0201534145_b220024813381"><a name="en-us_topic_0201534145_b220024813381"></a><a name="en-us_topic_0201534145_b220024813381"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.25%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534145_p4442411201715"><a name="en-us_topic_0201534145_p4442411201715"></a><a name="en-us_topic_0201534145_p4442411201715"></a><strong id="en-us_topic_0201534145_b1194978996"><a name="en-us_topic_0201534145_b1194978996"></a><a name="en-us_topic_0201534145_b1194978996"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="51.519999999999996%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534145_p124423117177"><a name="en-us_topic_0201534145_p124423117177"></a><a name="en-us_topic_0201534145_p124423117177"></a><strong id="en-us_topic_0201534145_b9873125010388"><a name="en-us_topic_0201534145_b9873125010388"></a><a name="en-us_topic_0201534145_b9873125010388"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534145_row1444331111711"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534145_p164432011131719"><a name="en-us_topic_0201534145_p164432011131719"></a><a name="en-us_topic_0201534145_p164432011131719"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534145_p444331114174"><a name="en-us_topic_0201534145_p444331114174"></a><a name="en-us_topic_0201534145_p444331114174"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.519999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534145_p17443151171713"><a name="en-us_topic_0201534145_p17443151171713"></a><a name="en-us_topic_0201534145_p17443151171713"></a>Specifies the API link.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534145_row174431411161711"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534145_p16443191131712"><a name="en-us_topic_0201534145_p16443191131712"></a><a name="en-us_topic_0201534145_p16443191131712"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534145_p2443111117171"><a name="en-us_topic_0201534145_p2443111117171"></a><a name="en-us_topic_0201534145_p2443111117171"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.519999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534145_p1944331171712"><a name="en-us_topic_0201534145_p1944331171712"></a><a name="en-us_topic_0201534145_p1944331171712"></a>Specifies the relationship between the API link and the API version.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "resources": [
            {
                "links": [
                    {
                        "href": "https://vpc.systems.com/v2.0/subnets",
                        "rel": "self"
                    }
                ],
                "name": "subnet",
                "collection": "subnets"
            },
            {
                "links": [
                    {
                        "href": "https://vpc.systems.com/v2.0/networks",
                        "rel": "self"
                    }
                ],
                "name": "network",
                "collection": "networks"
            },
            {
                "links": [
                    {
                        "href": "https://vpc.systems.com/v2.0/ports",
                        "rel": "self"
                    }
                ],
                "name": "port",
                "collection": "ports"
            }
        ]
    }
    ```


## Status Code<a name="en-us_topic_0201534145_section31981619"></a>

See  [Status Codes](status-codes.md#eip_api05_0001).

## Error Code<a name="en-us_topic_0201534145_section85821649202813"></a>

See  [Error Codes](error-codes.md#eip_api05_0002).

