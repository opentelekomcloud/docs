# Querying the Data Source List<a name="EN-US_TOPIC_0172486214"></a>

## Function<a name="section11410068144834"></a>

This API is used to query the data source list. This API is compatible with Sahara.

## URI<a name="section4721807314497"></a>

-   Format

    GET /v1.1/\{project\_id\}/data-sources

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
    <p id="p39045553104130"><a name="p39045553104130"></a><a name="p39045553104130"></a>Value range: 1 to 1073741822</p>
    </td>
    </tr>
    <tr id="row6317415154849"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p41948639154849"><a name="p41948639154849"></a><a name="p41948639154849"></a>marker</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p42396583154849"><a name="p42396583154849"></a><a name="p42396583154849"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p3859954494718"><a name="p3859954494718"></a><a name="p3859954494718"></a>Data source ID</p>
    <p id="p11571175154849"><a name="p11571175154849"></a><a name="p11571175154849"></a>Query the data source list, and select one data source ID as the marker. The ID is the last element on the list that will not be returned.</p>
    </td>
    </tr>
    <tr id="row25723845154843"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p3256680154843"><a name="p3256680154843"></a><a name="p3256680154843"></a>sort_by</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p62464499154843"><a name="p62464499154843"></a><a name="p62464499154843"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p26459663154843"><a name="p26459663154843"></a><a name="p26459663154843"></a>Sort field</p>
    <p id="p1746233322911"><a name="p1746233322911"></a><a name="p1746233322911"></a>A hyphen (-) before the sort field indicates to sort in descending order. Example:</p>
    <a name="ul5167941115195"></a><a name="ul5167941115195"></a><ul id="ul5167941115195"><li><strong id="b6174964693835"><a name="b6174964693835"></a><a name="b6174964693835"></a>sort_by=name</strong> indicates to sort by name in ascending order.</li><li><strong id="b612896093841"><a name="b612896093841"></a><a name="b612896093841"></a>sort_by=-name</strong> indicates to sort by name in descending order.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section31697334144924"></a>

**Request parameters**

None.

## Response<a name="section10069032144933"></a>

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
<tbody><tr id="row6100194103515"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p24353731103515"><a name="p24353731103515"></a><a name="p24353731103515"></a>markers</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p65739139103515"><a name="p65739139103515"></a><a name="p65739139103515"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p23270066103515"><a name="p23270066103515"></a><a name="p23270066103515"></a>Marker object For more parameter description, see <a href="#table35904709104244">Table 3</a>.</p>
</td>
</tr>
<tr id="row12577217103942"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p12121637103942"><a name="p12121637103942"></a><a name="p12121637103942"></a>data_sources</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p6059195103942"><a name="p6059195103942"></a><a name="p6059195103942"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p21032764103942"><a name="p21032764103942"></a><a name="p21032764103942"></a>Data source list For more parameter description, see <a href="#table53055087104252">Table 4</a>.</p>
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

**Table  4** **data\_sources**  parameter description

<a name="table53055087104252"></a>
<table><thead align="left"><tr id="row35892073104252"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p21576778104252"><a name="p21576778104252"></a><a name="p21576778104252"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="p32652035104252"><a name="p32652035104252"></a><a name="p32652035104252"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p27569194104252"><a name="p27569194104252"></a><a name="p27569194104252"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row18726201104252"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p40427346104252"><a name="p40427346104252"></a><a name="p40427346104252"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p29590281104252"><a name="p29590281104252"></a><a name="p29590281104252"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p48002551104252"><a name="p48002551104252"></a><a name="p48002551104252"></a>Data source name</p>
</td>
</tr>
<tr id="row29369779104252"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p30141923104252"><a name="p30141923104252"></a><a name="p30141923104252"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p58448085104252"><a name="p58448085104252"></a><a name="p58448085104252"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p36674406104252"><a name="p36674406104252"></a><a name="p36674406104252"></a>Data source type</p>
</td>
</tr>
<tr id="row61634201104252"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p26314410104252"><a name="p26314410104252"></a><a name="p26314410104252"></a>url</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p44852170104252"><a name="p44852170104252"></a><a name="p44852170104252"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p9147177104252"><a name="p9147177104252"></a><a name="p9147177104252"></a>Data source URL</p>
</td>
</tr>
<tr id="row15215732104252"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p24514817104252"><a name="p24514817104252"></a><a name="p24514817104252"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p48878563104252"><a name="p48878563104252"></a><a name="p48878563104252"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p66849545104252"><a name="p66849545104252"></a><a name="p66849545104252"></a>Data source description</p>
</td>
</tr>
<tr id="row64774998104252"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p12283463104252"><a name="p12283463104252"></a><a name="p12283463104252"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p61169696104252"><a name="p61169696104252"></a><a name="p61169696104252"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p55798359104252"><a name="p55798359104252"></a><a name="p55798359104252"></a>Data source creation time</p>
</td>
</tr>
<tr id="row33701760152359"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p45488048152359"><a name="p45488048152359"></a><a name="p45488048152359"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p13966373152359"><a name="p13966373152359"></a><a name="p13966373152359"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p57534394152359"><a name="p57534394152359"></a><a name="p57534394152359"></a>Data source update time</p>
</td>
</tr>
<tr id="row32423190104252"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p9032743104252"><a name="p9032743104252"></a><a name="p9032743104252"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p6703306104252"><a name="p6703306104252"></a><a name="p6703306104252"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p6096941104252"><a name="p6096941104252"></a><a name="p6096941104252"></a>Data source ID</p>
</td>
</tr>
<tr id="row54872471104252"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p15485137104252"><a name="p15485137104252"></a><a name="p15485137104252"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p62274483104252"><a name="p62274483104252"></a><a name="p62274483104252"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p13745886363"><a name="p13745886363"></a><a name="p13745886363"></a>Project ID. For details on how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
</td>
</tr>
<tr id="row32506112104252"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p15749438104252"><a name="p15749438104252"></a><a name="p15749438104252"></a>is_public</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p51522162104252"><a name="p51522162104252"></a><a name="p51522162104252"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p12545593104252"><a name="p12545593104252"></a><a name="p12545593104252"></a>Whether the data source is public</p>
<a name="ul35290564102533"></a><a name="ul35290564102533"></a><ul id="ul35290564102533"><li>true</li><li>false</li></ul>
<p id="p24126416102533"><a name="p24126416102533"></a><a name="p24126416102533"></a>The current version does not support this function.</p>
</td>
</tr>
<tr id="row45801476104252"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p18932079104252"><a name="p18932079104252"></a><a name="p18932079104252"></a>is_protected</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p61973162104252"><a name="p61973162104252"></a><a name="p61973162104252"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p53770186104252"><a name="p53770186104252"></a><a name="p53770186104252"></a>Whether the data source is protected</p>
<a name="ul46267294153233"></a><a name="ul46267294153233"></a><ul id="ul46267294153233"><li>true</li><li>false</li></ul>
<p id="p40207906153233"><a name="p40207906153233"></a><a name="p40207906153233"></a>The current version does not support this function.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section13287161117450"></a>

-   Example request

    ```
    GET /v1.1/{project_id}/data-sources?sort_by=name&limit=2&marker=81a2d48b-029a-4160-830b-2d0ac51fa3ba
    ```


-   Example response

    ```
    {
        "markers": {
            "prev": "948b92e5-8213-4f5d-975a-435a67c6b93d",
            "next": null
        },
        "data_sources": [
            {
                "name": "my-data-source-update",
                "type": "hdfs",
                "url": "/simple/mapreduce/input",
                "description": "this is the data source template",
                "created_at": "2017-06-22T08:28:57",
                "updated_at": "2017-06-22T08:30:08",
                "id": "e275a927-fe72-4b8b-a634-e47a11dca181",
                "tenant_id": "5a3314075bfa49b9ae360f4ecd333695",
                "is_public": false,
                "is_protected": false
            },
            {
                "name": "my-datasource",
                "type": "hdfs",
                "url": "/simple/mapreduce/input",
                "description": "this is the data source template",
                "created_at": "2017-06-22T08:22:06",
                "updated_at": null,
                "id": "e68164d5-5897-41a7-a550-5de635fffe20",
                "tenant_id": "5a3314075bfa49b9ae360f4ecd333695",
                "is_public": false,
                "is_protected": false
            }
        ]
    }
    ```


## Status Code<a name="section13299747144948"></a>

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
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p4613894216050"><a name="p4613894216050"></a><a name="p4613894216050"></a>The data source list is queried successfully.</p>
</td>
</tr>
</tbody>
</table>

For the description about error status codes, see  [Status Codes](status-codes.md).

