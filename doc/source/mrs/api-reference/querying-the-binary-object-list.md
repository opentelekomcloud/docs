# Querying the Binary Object List<a name="EN-US_TOPIC_0172486189"></a>

## Function<a name="section13541137101416"></a>

This API is used to query the binary object list. This API is compatible with Sahara.

## URI<a name="section49980811101439"></a>

-   Format

    GET /v1.1/\{project\_id\}/job-binaries

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
    <tr id="row20659256153330"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p10159747154837"><a name="p10159747154837"></a><a name="p10159747154837"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p44704178154837"><a name="p44704178154837"></a><a name="p44704178154837"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p49662373154837"><a name="p49662373154837"></a><a name="p49662373154837"></a>Maximum number of objects in response data</p>
    <p id="p31788692155324"><a name="p31788692155324"></a><a name="p31788692155324"></a>Value range: 1 to 1073741822</p>
    </td>
    </tr>
    <tr id="row6317415154849"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p41948639154849"><a name="p41948639154849"></a><a name="p41948639154849"></a>marker</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p42396583154849"><a name="p42396583154849"></a><a name="p42396583154849"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p6627529811145"><a name="p6627529811145"></a><a name="p6627529811145"></a>Job binary object ID</p>
    <p id="p11571175154849"><a name="p11571175154849"></a><a name="p11571175154849"></a>Query the job binary object list, and select one job binary object ID as the marker. The ID is the ID of the last element in the list that will not be returned.</p>
    </td>
    </tr>
    <tr id="row36517032111447"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p5089576111447"><a name="p5089576111447"></a><a name="p5089576111447"></a>sort_by</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p9602484111447"><a name="p9602484111447"></a><a name="p9602484111447"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p4862929713590"><a name="p4862929713590"></a><a name="p4862929713590"></a>Sort field</p>
    <p id="p1758085093716"><a name="p1758085093716"></a><a name="p1758085093716"></a>A hyphen (-) before the sort field indicates to sort in descending order. Example:</p>
    <a name="ul5167941115195"></a><a name="ul5167941115195"></a><ul id="ul5167941115195"><li><strong id="b20718183818237"><a name="b20718183818237"></a><a name="b20718183818237"></a>sort_by=name</strong> indicates to sort by name in ascending order.</li><li><strong id="b13180444132316"><a name="b13180444132316"></a><a name="b13180444132316"></a>sort_by=-name</strong> indicates to sort by name in descending order.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section7976792193238"></a>

**Request parameters**

None.

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
<tbody><tr id="row16731987111557"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p13113722111557"><a name="p13113722111557"></a><a name="p13113722111557"></a>markers</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p5571942111557"><a name="p5571942111557"></a><a name="p5571942111557"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p48674171111557"><a name="p48674171111557"></a><a name="p48674171111557"></a>Markers object</p>
<p id="p16522192210405"><a name="p16522192210405"></a><a name="p16522192210405"></a>For details, see <a href="#table35904709104244">Table 3</a>.</p>
</td>
</tr>
<tr id="row64063916111610"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p21794736111610"><a name="p21794736111610"></a><a name="p21794736111610"></a>binaries</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p53385869111610"><a name="p53385869111610"></a><a name="p53385869111610"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p11305534104017"><a name="p11305534104017"></a><a name="p11305534104017"></a>Binary object list</p>
<p id="p29288118111610"><a name="p29288118111610"></a><a name="p29288118111610"></a>For details, see <a href="#table5646270112712">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **markers**  parameter description

<a name="table35904709104244"></a>
<table><thead align="left"><tr id="row49938240104244"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p18465671104244"><a name="p18465671104244"></a><a name="p18465671104244"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="p21768128104244"><a name="p21768128104244"></a><a name="p21768128104244"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p18387972104244"><a name="p18387972104244"></a><a name="p18387972104244"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row13030764104244"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p63118498104319"><a name="p63118498104319"></a><a name="p63118498104319"></a>prev</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p43381604104319"><a name="p43381604104319"></a><a name="p43381604104319"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p39594016104319"><a name="p39594016104319"></a><a name="p39594016104319"></a>Marker on the previous page</p>
</td>
</tr>
<tr id="row58460908104244"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p46558357104319"><a name="p46558357104319"></a><a name="p46558357104319"></a>next</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p66061904104319"><a name="p66061904104319"></a><a name="p66061904104319"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p53737691104319"><a name="p53737691104319"></a><a name="p53737691104319"></a>Marker on the next page</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **binaries**  parameter description

<a name="table5646270112712"></a>
<table><thead align="left"><tr id="row41235644112712"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p51752871112712"><a name="p51752871112712"></a><a name="p51752871112712"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="p46844898112712"><a name="p46844898112712"></a><a name="p46844898112712"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p36340354112712"><a name="p36340354112712"></a><a name="p36340354112712"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row16789243112712"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p17751420112712"><a name="p17751420112712"></a><a name="p17751420112712"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p33193333112712"><a name="p33193333112712"></a><a name="p33193333112712"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p4305468112712"><a name="p4305468112712"></a><a name="p4305468112712"></a>Binary object name</p>
</td>
</tr>
<tr id="row38749219112712"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p51679044112712"><a name="p51679044112712"></a><a name="p51679044112712"></a>url</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p32230151112712"><a name="p32230151112712"></a><a name="p32230151112712"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p60505466112712"><a name="p60505466112712"></a><a name="p60505466112712"></a>Binary object URL</p>
</td>
</tr>
<tr id="row7678284112712"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p17961238112712"><a name="p17961238112712"></a><a name="p17961238112712"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p519192112712"><a name="p519192112712"></a><a name="p519192112712"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p42054559112712"><a name="p42054559112712"></a><a name="p42054559112712"></a>Binary object description</p>
</td>
</tr>
<tr id="row42946717112712"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p56132075112712"><a name="p56132075112712"></a><a name="p56132075112712"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p56208447112712"><a name="p56208447112712"></a><a name="p56208447112712"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p56590358112712"><a name="p56590358112712"></a><a name="p56590358112712"></a>Binary object creation time</p>
</td>
</tr>
<tr id="row39551177112712"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p49528772112712"><a name="p49528772112712"></a><a name="p49528772112712"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p17154847112712"><a name="p17154847112712"></a><a name="p17154847112712"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p47365327112712"><a name="p47365327112712"></a><a name="p47365327112712"></a>Binary object update time</p>
</td>
</tr>
<tr id="row23634760112712"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p35367402112712"><a name="p35367402112712"></a><a name="p35367402112712"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p50183839112712"><a name="p50183839112712"></a><a name="p50183839112712"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p38359171112712"><a name="p38359171112712"></a><a name="p38359171112712"></a>Binary object ID</p>
</td>
</tr>
<tr id="row9688219112712"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p46548270112712"><a name="p46548270112712"></a><a name="p46548270112712"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p57872178112712"><a name="p57872178112712"></a><a name="p57872178112712"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p98891143183718"><a name="p98891143183718"></a><a name="p98891143183718"></a>Project ID. For details on how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
</td>
</tr>
<tr id="row44451467112712"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p43799081112712"><a name="p43799081112712"></a><a name="p43799081112712"></a>is_public</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p5621264112712"><a name="p5621264112712"></a><a name="p5621264112712"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p52669224112712"><a name="p52669224112712"></a><a name="p52669224112712"></a>Whether a binary object is public</p>
<a name="ul24233663152954"></a><a name="ul24233663152954"></a><ul id="ul24233663152954"><li>true</li><li>false</li></ul>
<p id="p16709791152954"><a name="p16709791152954"></a><a name="p16709791152954"></a>The current version does not support this function.</p>
</td>
</tr>
<tr id="row4260969112712"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p9594237112712"><a name="p9594237112712"></a><a name="p9594237112712"></a>is_protected</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p66786682112712"><a name="p66786682112712"></a><a name="p66786682112712"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p41012147112712"><a name="p41012147112712"></a><a name="p41012147112712"></a>Whether a binary object is protected</p>
<a name="ul5782838616950"></a><a name="ul5782838616950"></a><ul id="ul5782838616950"><li>true</li><li>false</li></ul>
<p id="p1252713316950"><a name="p1252713316950"></a><a name="p1252713316950"></a>The current version does not support this function.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section1210015461189"></a>

-   Example request

    ```
    GET /v1.1/{project_id}/job-binaries?limit=1&sort_by=name&marker= eadfb8ec-760b-499f-b8df-00a6def854f8
    ```

-   Example response

    ```
    {
        "markers": {
            "prev": "ddf13f9d-93e8-4999-b860-0dc0c01c517d",
            "next": null
        },
        "binaries": [
            {
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
        ]
    }
    ```


## Status Code<a name="section19688788101519"></a>

[Table 5](#table1584477916050)  describes the status code of this API.

**Table  5**  Status code

<a name="table1584477916050"></a>
<table><thead align="left"><tr id="row1339492016050"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.3.1.1"><p id="p3411176516050"><a name="p3411176516050"></a><a name="p3411176516050"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.2.3.1.2"><p id="p1158961516050"><a name="p1158961516050"></a><a name="p1158961516050"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3719767816050"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p6022194016050"><a name="p6022194016050"></a><a name="p6022194016050"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p4613894216050"><a name="p4613894216050"></a><a name="p4613894216050"></a>The binary object list is queried successfully.</p>
</td>
</tr>
</tbody>
</table>

For the description about error status codes, see  [Status Codes](status-codes.md).

