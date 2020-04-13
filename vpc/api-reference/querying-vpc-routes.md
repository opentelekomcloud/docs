# Querying VPC Routes<a name="vpc_route_0001"></a>

## Function<a name="section162841743131116"></a>

This API is used to query all routes of the tenant submitting the request. The routes are filtered based on the filtering condition. For details about the response format of pagination query, see section  [Pagination](pagination.md).

## URI<a name="section1828464319118"></a>

GET /v2.0/vpc/routes

Example:

```
Example:
GET https://{Endpoint}/v2.0/vpc/routes?id={id}&vpc_id={vpc_id}&tenant_id={tenant_id}&destination={destination}&type={type}&limit={limit}&marker={marker}
```

[Table 1](#table1256815152114)  describes the parameters.

**Table  1**  Parameter description

<a name="table1256815152114"></a>
<table><thead align="left"><tr id="row2066671591116"><th class="cellrowborder" valign="top" width="22.222222222222225%" id="mcps1.2.5.1.1"><p id="p1466620159113"><a name="p1466620159113"></a><a name="p1466620159113"></a><strong id="b3371155162638"><a name="b3371155162638"></a><a name="b3371155162638"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.14141414141414%" id="mcps1.2.5.1.2"><p id="p0666015121119"><a name="p0666015121119"></a><a name="p0666015121119"></a><strong id="b842352706145619"><a name="b842352706145619"></a><a name="b842352706145619"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.27272727272727%" id="mcps1.2.5.1.3"><p id="p966631501115"><a name="p966631501115"></a><a name="p966631501115"></a><strong id="b842352706145623"><a name="b842352706145623"></a><a name="b842352706145623"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="36.36363636363636%" id="mcps1.2.5.1.4"><p id="p14666615171112"><a name="p14666615171112"></a><a name="p14666615171112"></a><strong id="b8423527061645"><a name="b8423527061645"></a><a name="b8423527061645"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row06661515151115"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p1666681551120"><a name="p1666681551120"></a><a name="p1666681551120"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p12666151515113"><a name="p12666151515113"></a><a name="p12666151515113"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.5.1.3 "><p id="p66664158117"><a name="p66664158117"></a><a name="p66664158117"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.5.1.4 "><p id="p16661715101119"><a name="p16661715101119"></a><a name="p16661715101119"></a>Specifies that the route ID is used as the filtering condition.</p>
</td>
</tr>
<tr id="row10666515101113"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p5482113610377"><a name="p5482113610377"></a><a name="p5482113610377"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p11666815111120"><a name="p11666815111120"></a><a name="p11666815111120"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.5.1.3 "><p id="p146661615161112"><a name="p146661615161112"></a><a name="p146661615161112"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.5.1.4 "><p id="p1066641513118"><a name="p1066641513118"></a><a name="p1066641513118"></a>Specifies that the tenant ID is used as the filtering condition.</p>
</td>
</tr>
<tr id="row19666101515116"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p866631561113"><a name="p866631561113"></a><a name="p866631561113"></a>vpc_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p1666616153117"><a name="p1666616153117"></a><a name="p1666616153117"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.5.1.3 "><p id="p18666215201119"><a name="p18666215201119"></a><a name="p18666215201119"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.5.1.4 "><p id="p466651510117"><a name="p466651510117"></a><a name="p466651510117"></a>Specifies that the VPC ID is used as the filtering condition.</p>
</td>
</tr>
<tr id="row14666415101111"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p1066681561114"><a name="p1066681561114"></a><a name="p1066681561114"></a>destination</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p166671571112"><a name="p166671571112"></a><a name="p166671571112"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.5.1.3 "><p id="p1266681521114"><a name="p1266681521114"></a><a name="p1266681521114"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.5.1.4 "><p id="p466671561110"><a name="p466671561110"></a><a name="p466671561110"></a>Specifies that the route destination address (CIDR) is used as the filtering condition.</p>
</td>
</tr>
<tr id="row186663151117"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p56661015111110"><a name="p56661015111110"></a><a name="p56661015111110"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p17666151515114"><a name="p17666151515114"></a><a name="p17666151515114"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.5.1.3 "><p id="p1566641571117"><a name="p1566641571117"></a><a name="p1566641571117"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.5.1.4 "><p id="p1666610159113"><a name="p1666610159113"></a><a name="p1666610159113"></a>Specifies that the type is used as the filtering condition. Currently, the value can only be <strong id="b115817011124"><a name="b115817011124"></a><a name="b115817011124"></a>peering</strong>.</p>
</td>
</tr>
<tr id="row12666615181111"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p17666191551117"><a name="p17666191551117"></a><a name="p17666191551117"></a>marker</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p2666131513115"><a name="p2666131513115"></a><a name="p2666131513115"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.5.1.3 "><p id="p15666715171118"><a name="p15666715171118"></a><a name="p15666715171118"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.5.1.4 "><p id="p3666191521119"><a name="p3666191521119"></a><a name="p3666191521119"></a>Specifies the start resource ID of pagination query. If the parameter is left blank, only resources on the first page are queried.</p>
</td>
</tr>
<tr id="row1666661561117"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p1666121531117"><a name="p1666121531117"></a><a name="p1666121531117"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p66667156117"><a name="p66667156117"></a><a name="p66667156117"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.5.1.3 "><p id="p12666111514118"><a name="p12666111514118"></a><a name="p12666111514118"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.5.1.4 "><a name="ul79502025143815"></a><a name="ul79502025143815"></a><ul id="ul79502025143815"><li>Specifies the number of records returned on each page.</li><li>The value ranges from 0 to intmax.</li><li>The default value is <strong id="b1051016316122"><a name="b1051016316122"></a><a name="b1051016316122"></a>2000</strong>.</li></ul>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section229194351110"></a>

-   Request parameter

    None


-   Example request

    ```
    GET https://{Endpoint}/v2.0/vpc/routes?vpc_id=ab78be2d-782f-42a5-aa72-35879f6890ff
    ```


## Response Message<a name="section12916437119"></a>

-   Response parameter

    **Table  2**  Response parameter

    <a name="table10292143181119"></a>
    <table><thead align="left"><tr id="row5437104312112"><th class="cellrowborder" valign="top" width="18.82%" id="mcps1.2.4.1.1"><p id="p19437124311115"><a name="p19437124311115"></a><a name="p19437124311115"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.709999999999997%" id="mcps1.2.4.1.2"><p id="p3437243191113"><a name="p3437243191113"></a><a name="p3437243191113"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.47%" id="mcps1.2.4.1.3"><p id="p8437174311112"><a name="p8437174311112"></a><a name="p8437174311112"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1443754317116"><td class="cellrowborder" valign="top" width="18.82%" headers="mcps1.2.4.1.1 "><p id="p8437643101115"><a name="p8437643101115"></a><a name="p8437643101115"></a>routes</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.709999999999997%" headers="mcps1.2.4.1.2 "><p id="p20437343121112"><a name="p20437343121112"></a><a name="p20437343121112"></a>Array of <a href="#table05001250111">route</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.2.4.1.3 "><p id="p16438204318114"><a name="p16438204318114"></a><a name="p16438204318114"></a>Specifies the route object list. For details, see <a href="#table05001250111">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **route**  objects

    <a name="table05001250111"></a>
    <table><thead align="left"><tr id="row1604152531116"><th class="cellrowborder" valign="top" width="19.321932193219325%" id="mcps1.2.4.1.1"><p id="p19605525151115"><a name="p19605525151115"></a><a name="p19605525151115"></a><strong id="b84235270610290"><a name="b84235270610290"></a><a name="b84235270610290"></a>Attribute</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24.172417241724172%" id="mcps1.2.4.1.2"><p id="p2060572511111"><a name="p2060572511111"></a><a name="p2060572511111"></a><strong id="b84235270610297"><a name="b84235270610297"></a><a name="b84235270610297"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="56.5056505650565%" id="mcps1.2.4.1.3"><p id="p11605425111120"><a name="p11605425111120"></a><a name="p11605425111120"></a><strong id="b4752179111911"><a name="b4752179111911"></a><a name="b4752179111911"></a>Description</strong></p>
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
    <td class="cellrowborder" valign="top" width="56.5056505650565%" headers="mcps1.2.4.1.3 "><p id="p487414894012"><a name="p487414894012"></a><a name="p487414894012"></a>Specifies the next hop. If the route type is <strong id="b842352706105350"><a name="b842352706105350"></a><a name="b842352706105350"></a>peering</strong>, enter the VPC peering connection ID.</p>
    </td>
    </tr>
    <tr id="row26061325191110"><td class="cellrowborder" valign="top" width="19.321932193219325%" headers="mcps1.2.4.1.1 "><p id="p86067257112"><a name="p86067257112"></a><a name="p86067257112"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.172417241724172%" headers="mcps1.2.4.1.2 "><p id="p260619251118"><a name="p260619251118"></a><a name="p260619251118"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.5056505650565%" headers="mcps1.2.4.1.3 "><p id="p9916134014397"><a name="p9916134014397"></a><a name="p9916134014397"></a>Specifies the route type. Currently, the value can only be <strong id="b842352706105424"><a name="b842352706105424"></a><a name="b842352706105424"></a>peering</strong>.</p>
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
      "routes": [ 
        { 
          "type": "peering",  
          "nexthop": "60c809cb-6731-45d0-ace8-3bf5626421a9",  
          "destination": "192.168.200.0/24",  
          "vpc_id": "ab78be2d-782f-42a5-aa72-35879f6890ff",  
          "tenant_id": "6fbe9263116a4b68818cf1edce16bc4f",
          "id": "3d42a0d4-a980-4613-ae76-a2cddecff054" 
        }
      ] 
    }
    ```


## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

