# Querying a VPC Route<a name="vpc_route_0002"></a>

## Function<a name="section854682151220"></a>

This API is used to query details about a route.

## URI<a name="section3547821101219"></a>

GET /v2.0/vpc/routes/\{route\_id\}

[Table 1](#table18880184689)  describes the parameters.

**Table  1**  Parameter description

<a name="table18880184689"></a>
<table><thead align="left"><tr id="row13968641385"><th class="cellrowborder" valign="top" width="22.222222222222225%" id="mcps1.2.5.1.1"><p id="p209684410817"><a name="p209684410817"></a><a name="p209684410817"></a><strong id="b842352706195711"><a name="b842352706195711"></a><a name="b842352706195711"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.14141414141414%" id="mcps1.2.5.1.2"><p id="p69681441386"><a name="p69681441386"></a><a name="p69681441386"></a><strong id="b84235270615219"><a name="b84235270615219"></a><a name="b84235270615219"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.27272727272727%" id="mcps1.2.5.1.3"><p id="p1096813412811"><a name="p1096813412811"></a><a name="p1096813412811"></a><strong id="b842352706145623"><a name="b842352706145623"></a><a name="b842352706145623"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="36.36363636363636%" id="mcps1.2.5.1.4"><p id="p139686416813"><a name="p139686416813"></a><a name="p139686416813"></a><strong id="b8423527061645"><a name="b8423527061645"></a><a name="b8423527061645"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row19681041189"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p1013244217196"><a name="p1013244217196"></a><a name="p1013244217196"></a>route_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p1797015416817"><a name="p1797015416817"></a><a name="p1797015416817"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.5.1.3 "><p id="p19701411813"><a name="p19701411813"></a><a name="p19701411813"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.5.1.4 "><p id="p123881427145"><a name="p123881427145"></a><a name="p123881427145"></a>Specifies the route ID, which uniquely identifies the route.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section11553182191214"></a>

-   Request parameter

    None


-   Example request

    ```
    GET https://{Endpoint}/v2.0/vpc/routes/60c809cb-6731-45d0-ace8-3bf5626421a9
    ```


## Response Message<a name="section6554102119123"></a>

-   Response parameter

    **Table  2**  Response parameter

    <a name="table355410218123"></a>
    <table><thead align="left"><tr id="row1168714210128"><th class="cellrowborder" valign="top" width="21.349999999999998%" id="mcps1.2.4.1.1"><p id="p5687821191213"><a name="p5687821191213"></a><a name="p5687821191213"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.48%" id="mcps1.2.4.1.2"><p id="p20687202118122"><a name="p20687202118122"></a><a name="p20687202118122"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="65.16999999999999%" id="mcps1.2.4.1.3"><p id="p4687102113129"><a name="p4687102113129"></a><a name="p4687102113129"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2068712111129"><td class="cellrowborder" valign="top" width="21.349999999999998%" headers="mcps1.2.4.1.1 "><p id="p176872021121212"><a name="p176872021121212"></a><a name="p176872021121212"></a>route</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.48%" headers="mcps1.2.4.1.2 "><p id="p1368732191211"><a name="p1368732191211"></a><a name="p1368732191211"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.16999999999999%" headers="mcps1.2.4.1.3 "><p id="p16438204318114"><a name="p16438204318114"></a><a name="p16438204318114"></a>Specifies the route object list. For details, see <a href="#table05001250111">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **route**  objects

    <a name="table05001250111"></a>
    <table><thead align="left"><tr id="row1604152531116"><th class="cellrowborder" valign="top" width="19.321932193219325%" id="mcps1.2.4.1.1"><p id="p19605525151115"><a name="p19605525151115"></a><a name="p19605525151115"></a><strong id="b127281319183"><a name="b127281319183"></a><a name="b127281319183"></a>Attribute</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24.172417241724172%" id="mcps1.2.4.1.2"><p id="p2060572511111"><a name="p2060572511111"></a><a name="p2060572511111"></a><strong id="b17283814101819"><a name="b17283814101819"></a><a name="b17283814101819"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="56.5056505650565%" id="mcps1.2.4.1.3"><p id="p11605425111120"><a name="p11605425111120"></a><a name="p11605425111120"></a><strong id="b1966810394191"><a name="b1966810394191"></a><a name="b1966810394191"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row19605172516117"><td class="cellrowborder" valign="top" width="19.321932193219325%" headers="mcps1.2.4.1.1 "><p id="p4605625141117"><a name="p4605625141117"></a><a name="p4605625141117"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.172417241724172%" headers="mcps1.2.4.1.2 "><p id="p4605425191116"><a name="p4605425191116"></a><a name="p4605425191116"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.5056505650565%" headers="mcps1.2.4.1.3 "><p id="p136051025171110"><a name="p136051025171110"></a><a name="p136051025171110"></a>Specifies the route ID.</p>
    </td>
    </tr>
    <tr id="row19605192511115"><td class="cellrowborder" valign="top" width="19.321932193219325%" headers="mcps1.2.4.1.1 "><p id="p1160582510117"><a name="p1160582510117"></a><a name="p1160582510117"></a>destination</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.172417241724172%" headers="mcps1.2.4.1.2 "><p id="p186051725131113"><a name="p186051725131113"></a><a name="p186051725131113"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.5056505650565%" headers="mcps1.2.4.1.3 "><p id="p20605425121118"><a name="p20605425121118"></a><a name="p20605425121118"></a>Specifies the destination address in the CIDR notation format, for example, 192.168.200.0/24.</p>
    </td>
    </tr>
    <tr id="row160513252111"><td class="cellrowborder" valign="top" width="19.321932193219325%" headers="mcps1.2.4.1.1 "><p id="p76051225121114"><a name="p76051225121114"></a><a name="p76051225121114"></a>nexthop</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.172417241724172%" headers="mcps1.2.4.1.2 "><p id="p1460592591111"><a name="p1460592591111"></a><a name="p1460592591111"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.5056505650565%" headers="mcps1.2.4.1.3 "><p id="p487414894012"><a name="p487414894012"></a><a name="p487414894012"></a>Specifies the next hop. If the route type is <strong id="b1665776122017"><a name="b1665776122017"></a><a name="b1665776122017"></a>peering</strong>, enter the VPC peering connection ID.</p>
    </td>
    </tr>
    <tr id="row26061325191110"><td class="cellrowborder" valign="top" width="19.321932193219325%" headers="mcps1.2.4.1.1 "><p id="p86067257112"><a name="p86067257112"></a><a name="p86067257112"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.172417241724172%" headers="mcps1.2.4.1.2 "><p id="p260619251118"><a name="p260619251118"></a><a name="p260619251118"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.5056505650565%" headers="mcps1.2.4.1.3 "><p id="p9916134014397"><a name="p9916134014397"></a><a name="p9916134014397"></a>Specifies the route type. Currently, the value can only be <strong id="b1198002102012"><a name="b1198002102012"></a><a name="b1198002102012"></a>peering</strong>.</p>
    </td>
    </tr>
    <tr id="row11606125111110"><td class="cellrowborder" valign="top" width="19.321932193219325%" headers="mcps1.2.4.1.1 "><p id="p12606162501119"><a name="p12606162501119"></a><a name="p12606162501119"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.172417241724172%" headers="mcps1.2.4.1.2 "><p id="p06061925181119"><a name="p06061925181119"></a><a name="p06061925181119"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.5056505650565%" headers="mcps1.2.4.1.3 "><p id="p9606112519111"><a name="p9606112519111"></a><a name="p9606112519111"></a>Specifies the VPC of the route. Set this parameter to the existing VPC ID.</p>
    </td>
    </tr>
    <tr id="row56067256117"><td class="cellrowborder" valign="top" width="19.321932193219325%" headers="mcps1.2.4.1.1 "><p id="p196065257115"><a name="p196065257115"></a><a name="p196065257115"></a>tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.172417241724172%" headers="mcps1.2.4.1.2 "><p id="p10606182591115"><a name="p10606182591115"></a><a name="p10606182591115"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.5056505650565%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "route": { 
            "type": "peering",  
            "nexthop": "60c809cb-6731-45d0-ace8-3bf5626421a9",  
            "destination": "192.168.200.0/24",  
            "vpc_id": "ab78be2d-782f-42a5-aa72-35879f6890ff",  
            "tenant_id": "6fbe9263116a4b68818cf1edce16bc4f",
            "id": "3d42a0d4-a980-4613-ae76-a2cddecff054" 
        }
    }
    ```


## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

