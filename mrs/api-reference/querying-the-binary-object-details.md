# Querying the Binary Object Details<a name="EN-US_TOPIC_0172486100"></a>

## Function<a name="section13541137101416"></a>

This API is used to query detailed information about a binary object. This API is compatible with Sahara.

## URI<a name="section49980811101439"></a>

-   Format

    GET /v1.1/\{project\_id\}/job-binaries/\{job\_binary\_id\}

-   Parameter description

    **Table  1**  URI parameter description

    <a name="table49499141194754"></a>
    <table><thead align="left"><tr id="row33700024194754"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p16571835194812"><a name="p16571835194812"></a><a name="p16571835194812"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="p141410194812"><a name="p141410194812"></a><a name="p141410194812"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p11454278194812"><a name="p11454278194812"></a><a name="p11454278194812"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6505449415356"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p3492262515356"><a name="p3492262515356"></a><a name="p3492262515356"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p1016041415356"><a name="p1016041415356"></a><a name="p1016041415356"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1768719515356"><a name="p1768719515356"></a><a name="p1768719515356"></a>Project ID. For details on how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row61502886104852"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p15677856104852"><a name="p15677856104852"></a><a name="p15677856104852"></a>job_binary_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p61946843104852"><a name="p61946843104852"></a><a name="p61946843104852"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p51638399104852"><a name="p51638399104852"></a><a name="p51638399104852"></a>Binary object ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section7976792193238"></a>

**Request parameters**

None

## Response<a name="section38599577193858"></a>

**Table  2**  Response parameter description

<a name="table51257841151049"></a>
<table><thead align="left"><tr id="row8480851151049"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p15860319151049"><a name="p15860319151049"></a><a name="p15860319151049"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="p40813771151049"><a name="p40813771151049"></a><a name="p40813771151049"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p17581180151049"><a name="p17581180151049"></a><a name="p17581180151049"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row6726034151222"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p20438892151640"><a name="p20438892151640"></a><a name="p20438892151640"></a>is_public</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p16062920151640"><a name="p16062920151640"></a><a name="p16062920151640"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p26028163151640"><a name="p26028163151640"></a><a name="p26028163151640"></a>Whether a binary object is public</p>
<a name="ul24233663152954"></a><a name="ul24233663152954"></a><ul id="ul24233663152954"><li>true</li><li>false</li></ul>
<p id="p16709791152954"><a name="p16709791152954"></a><a name="p16709791152954"></a>The current version does not support this function.</p>
</td>
</tr>
<tr id="row35088736111441"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p2935166111454"><a name="p2935166111454"></a><a name="p2935166111454"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p64495288111454"><a name="p64495288111454"></a><a name="p64495288111454"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p56735821111454"><a name="p56735821111454"></a><a name="p56735821111454"></a>Binary object description</p>
</td>
</tr>
<tr id="row3560250611155"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p42933867111518"><a name="p42933867111518"></a><a name="p42933867111518"></a>url</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p33200524111518"><a name="p33200524111518"></a><a name="p33200524111518"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p4887925111518"><a name="p4887925111518"></a><a name="p4887925111518"></a>Binary object URL</p>
</td>
</tr>
<tr id="row1794513155918"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p25070059155926"><a name="p25070059155926"></a><a name="p25070059155926"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p835343155926"><a name="p835343155926"></a><a name="p835343155926"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1158920103815"><a name="p1158920103815"></a><a name="p1158920103815"></a>Project ID. For details on how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
</td>
</tr>
<tr id="row23363161601"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p6056003416010"><a name="p6056003416010"></a><a name="p6056003416010"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p4991056416010"><a name="p4991056416010"></a><a name="p4991056416010"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1622389816010"><a name="p1622389816010"></a><a name="p1622389816010"></a>Binary object creation time</p>
</td>
</tr>
<tr id="row15896716111552"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p12565602111552"><a name="p12565602111552"></a><a name="p12565602111552"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p33235893111552"><a name="p33235893111552"></a><a name="p33235893111552"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p7752833111552"><a name="p7752833111552"></a><a name="p7752833111552"></a>Binary object update time</p>
</td>
</tr>
<tr id="row8652083151249"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p29730140151249"><a name="p29730140151249"></a><a name="p29730140151249"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p17113312151828"><a name="p17113312151828"></a><a name="p17113312151828"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p39995064151249"><a name="p39995064151249"></a><a name="p39995064151249"></a>Binary object ID</p>
</td>
</tr>
<tr id="row12228393151256"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p50975775151256"><a name="p50975775151256"></a><a name="p50975775151256"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p21869845151828"><a name="p21869845151828"></a><a name="p21869845151828"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p43580859151256"><a name="p43580859151256"></a><a name="p43580859151256"></a>Binary object name</p>
</td>
</tr>
<tr id="row4419889616034"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p37826600111641"><a name="p37826600111641"></a><a name="p37826600111641"></a>is_protected</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p11748871111641"><a name="p11748871111641"></a><a name="p11748871111641"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p12134505111641"><a name="p12134505111641"></a><a name="p12134505111641"></a>Whether a binary object is protected</p>
<a name="ul3872134516111"></a><a name="ul3872134516111"></a><ul id="ul3872134516111"><li>true</li><li>false</li></ul>
<p id="p4213768316111"><a name="p4213768316111"></a><a name="p4213768316111"></a>The current version does not support this function.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section1210015461189"></a>

-   Example request

    None

-   Example response

    ```
    {
        "job_binary": {
            "name": "my-job-binary-update",
            "url": "/simple/mapreduce/program",
            "description": "this is the job binary template",
            "created_at": "2017-06-22T09:04:53",
            "updated_at": "2017-06-22T09:06:50",
            "id": "da37b581-042f-4d7a-9378-f628f32bd9ae",
            "tenant_id": "5a3314075bfa49b9ae360f4ecd333695",
            "is_public": false,
            "is_protected": false
        }
    }
    ```


## Status Code<a name="section19688788101519"></a>

[Table 3](#table1584477916050)  describes the status code of this API.

**Table  3**  Status code

<a name="table1584477916050"></a>
<table><thead align="left"><tr id="row1339492016050"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.3.1.1"><p id="p3411176516050"><a name="p3411176516050"></a><a name="p3411176516050"></a>Status code</p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.2.3.1.2"><p id="p1158961516050"><a name="p1158961516050"></a><a name="p1158961516050"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3719767816050"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p6022194016050"><a name="p6022194016050"></a><a name="p6022194016050"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p4613894216050"><a name="p4613894216050"></a><a name="p4613894216050"></a>The binary object details are queried successfully.</p>
</td>
</tr>
</tbody>
</table>

For the description about error status codes, see  [Status Codes](status-codes.md).

