# Querying a Specified API Version<a name="vpc_version_0002"></a>

## Function<a name="section292172513710"></a>

This API is used to query the version of a specified API.

## URI<a name="section092618252375"></a>

GET /\{api\_version\}

[Table 1](#table8488410142319)  describes the parameters.

**Table  1**  Parameter description

<a name="table8488410142319"></a>
<table><thead align="left"><tr id="row9493141018236"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p94981610102320"><a name="p94981610102320"></a><a name="p94981610102320"></a><strong id="b842352706193648"><a name="b842352706193648"></a><a name="b842352706193648"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p12502171018236"><a name="p12502171018236"></a><a name="p12502171018236"></a><strong id="b842352706193653"><a name="b842352706193653"></a><a name="b842352706193653"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p0503161052316"><a name="p0503161052316"></a><a name="p0503161052316"></a><strong id="b8423527061645"><a name="b8423527061645"></a><a name="b8423527061645"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row050661014235"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p5516910112316"><a name="p5516910112316"></a><a name="p5516910112316"></a>api_version</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1851919102230"><a name="p1851919102230"></a><a name="p1851919102230"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p25212100235"><a name="p25212100235"></a><a name="p25212100235"></a>Specifies the version number, for example <strong id="b84235270685253"><a name="b84235270685253"></a><a name="b84235270685253"></a>v2.0</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section159431125133719"></a>

-   Request parameter

    None


-   Example request

    ```
    GET https://{Endpoint}/v2.0
    ```


## Response Message<a name="section199536251373"></a>

-   Response parameter

    **Table  2**  Response parameter

    <a name="table1595322519378"></a>
    <table><thead align="left"><tr id="row95291726133710"><th class="cellrowborder" valign="top" width="23.23%" id="mcps1.2.4.1.1"><p id="p1252992613712"><a name="p1252992613712"></a><a name="p1252992613712"></a><strong id="b22486247"><a name="b22486247"></a><a name="b22486247"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.25%" id="mcps1.2.4.1.2"><p id="p55291826163717"><a name="p55291826163717"></a><a name="p55291826163717"></a><strong id="b811117612"><a name="b811117612"></a><a name="b811117612"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="51.519999999999996%" id="mcps1.2.4.1.3"><p id="p1552913260373"><a name="p1552913260373"></a><a name="p1552913260373"></a><strong id="b535700571"><a name="b535700571"></a><a name="b535700571"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15529326203718"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p8529826133712"><a name="p8529826133712"></a><a name="p8529826133712"></a>resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p13529152643712"><a name="p13529152643712"></a><a name="p13529152643712"></a>Array of <a href="#table1195920258372">resource</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.519999999999996%" headers="mcps1.2.4.1.3 "><p id="p1852902653713"><a name="p1852902653713"></a><a name="p1852902653713"></a>Specifies the <strong id="b84235270685442"><a name="b84235270685442"></a><a name="b84235270685442"></a>resource</strong> object list.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **resource**  object

    <a name="table1195920258372"></a>
    <table><thead align="left"><tr id="row5529132615373"><th class="cellrowborder" valign="top" width="23.23%" id="mcps1.2.4.1.1"><p id="p1252920262374"><a name="p1252920262374"></a><a name="p1252920262374"></a><strong id="b1084608877"><a name="b1084608877"></a><a name="b1084608877"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.25%" id="mcps1.2.4.1.2"><p id="p2529126123714"><a name="p2529126123714"></a><a name="p2529126123714"></a><strong id="b426919492"><a name="b426919492"></a><a name="b426919492"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="51.519999999999996%" id="mcps1.2.4.1.3"><p id="p105291226143715"><a name="p105291226143715"></a><a name="p105291226143715"></a><strong id="b1099241838"><a name="b1099241838"></a><a name="b1099241838"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1552919263377"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p10529192611375"><a name="p10529192611375"></a><a name="p10529192611375"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p352910264377"><a name="p352910264377"></a><a name="p352910264377"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.519999999999996%" headers="mcps1.2.4.1.3 "><p id="p052918269376"><a name="p052918269376"></a><a name="p052918269376"></a>Specifies the resource name.</p>
    </td>
    </tr>
    <tr id="row852942611373"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p1152902613374"><a name="p1152902613374"></a><a name="p1152902613374"></a>collection</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p185293264370"><a name="p185293264370"></a><a name="p185293264370"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.519999999999996%" headers="mcps1.2.4.1.3 "><p id="p8529192614377"><a name="p8529192614377"></a><a name="p8529192614377"></a>Specifies the resource collection name.</p>
    </td>
    </tr>
    <tr id="row6529726133710"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p25291326103715"><a name="p25291326103715"></a><a name="p25291326103715"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p2658122615326"><a name="p2658122615326"></a><a name="p2658122615326"></a>Array of <a href="#table4442151110172">link</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.519999999999996%" headers="mcps1.2.4.1.3 "><p id="p1252922613371"><a name="p1252922613371"></a><a name="p1252922613371"></a>Specifies the link list. For details, see <a href="#table4442151110172">Table 4</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **link**  objects

    <a name="table4442151110172"></a>
    <table><thead align="left"><tr id="row12442181131712"><th class="cellrowborder" valign="top" width="23.23%" id="mcps1.2.4.1.1"><p id="p044251171713"><a name="p044251171713"></a><a name="p044251171713"></a><strong id="b220024813381"><a name="b220024813381"></a><a name="b220024813381"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.25%" id="mcps1.2.4.1.2"><p id="p4442411201715"><a name="p4442411201715"></a><a name="p4442411201715"></a><strong id="b1194978996"><a name="b1194978996"></a><a name="b1194978996"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="51.519999999999996%" id="mcps1.2.4.1.3"><p id="p124423117177"><a name="p124423117177"></a><a name="p124423117177"></a><strong id="b9873125010388"><a name="b9873125010388"></a><a name="b9873125010388"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1444331111711"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p164432011131719"><a name="p164432011131719"></a><a name="p164432011131719"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p444331114174"><a name="p444331114174"></a><a name="p444331114174"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.519999999999996%" headers="mcps1.2.4.1.3 "><p id="p17443151171713"><a name="p17443151171713"></a><a name="p17443151171713"></a>Specifies the API link.</p>
    </td>
    </tr>
    <tr id="row174431411161711"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p16443191131712"><a name="p16443191131712"></a><a name="p16443191131712"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p2443111117171"><a name="p2443111117171"></a><a name="p2443111117171"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.519999999999996%" headers="mcps1.2.4.1.3 "><p id="p1944331171712"><a name="p1944331171712"></a><a name="p1944331171712"></a>Specifies the relationship between the API link and the API version.</p>
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


## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

