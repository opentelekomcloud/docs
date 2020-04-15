# Querying the Job Object List<a name="EN-US_TOPIC_0172486223"></a>

## Function<a name="section40666287163540"></a>

This API is used to query the job object list. This API is compatible with Sahara.

## URI<a name="section25682805163556"></a>

-   Format

    GET /v1.1/\{project\_id\}/jobs

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
    <p id="p45168427145211"><a name="p45168427145211"></a><a name="p45168427145211"></a>Value range: 1 to 1073741822</p>
    </td>
    </tr>
    <tr id="row6317415154849"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p41948639154849"><a name="p41948639154849"></a><a name="p41948639154849"></a>marker</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p42396583154849"><a name="p42396583154849"></a><a name="p42396583154849"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p11571175154849"><a name="p11571175154849"></a><a name="p11571175154849"></a>The ID is the ID of the last element in the list that will not be returned.</p>
    </td>
    </tr>
    <tr id="row25723845154843"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p3256680154843"><a name="p3256680154843"></a><a name="p3256680154843"></a>sort_by</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p62464499154843"><a name="p62464499154843"></a><a name="p62464499154843"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p191524715193"><a name="p191524715193"></a><a name="p191524715193"></a>Sort field. A hyphen (-) before the sort field indicates to sort in descending order. Examples:</p>
    <a name="ul5167941115195"></a><a name="ul5167941115195"></a><ul id="ul5167941115195"><li><strong id="b19392135162314"><a name="b19392135162314"></a><a name="b19392135162314"></a>sort_by=name</strong> indicates to sort by name in ascending order.</li><li><strong id="b5895360616342"><a name="b5895360616342"></a><a name="b5895360616342"></a>sort_by=-name</strong> indicates to sort by name in descending order.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section7976792193238"></a>

**Request parameters**

None

## Response<a name="section38599577193858"></a>

**Table  2**  Response parameter description

<a name="table60955430142546"></a>
<table><thead align="left"><tr id="row49351044142546"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p38011657142546"><a name="p38011657142546"></a><a name="p38011657142546"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="p17947989142546"><a name="p17947989142546"></a><a name="p17947989142546"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p44500971142546"><a name="p44500971142546"></a><a name="p44500971142546"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row47808898142546"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p63251747142556"><a name="p63251747142556"></a><a name="p63251747142556"></a>markers</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p39304444142556"><a name="p39304444142556"></a><a name="p39304444142556"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1657435617402"><a name="p1657435617402"></a><a name="p1657435617402"></a>Markers object</p>
<p id="p55104884142556"><a name="p55104884142556"></a><a name="p55104884142556"></a>For details, see <a href="#table35904709104244">Table 3</a>.</p>
</td>
</tr>
<tr id="row2052251142546"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p50715590142556"><a name="p50715590142556"></a><a name="p50715590142556"></a>jobs</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p20371352142556"><a name="p20371352142556"></a><a name="p20371352142556"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p3423101220415"><a name="p3423101220415"></a><a name="p3423101220415"></a>Job object list</p>
<p id="p1450079142556"><a name="p1450079142556"></a><a name="p1450079142556"></a>For details, see <a href="#table5154210817547">Table 4</a>.</p>
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

**Table  4** **jobs**  parameter description

<a name="table5154210817547"></a>
<table><thead align="left"><tr id="row5182537317547"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p3710571317547"><a name="p3710571317547"></a><a name="p3710571317547"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="p4673655817547"><a name="p4673655817547"></a><a name="p4673655817547"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p2756483917547"><a name="p2756483917547"></a><a name="p2756483917547"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row6552698617547"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p38654942173327"><a name="p38654942173327"></a><a name="p38654942173327"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p45958699173327"><a name="p45958699173327"></a><a name="p45958699173327"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p65699732173327"><a name="p65699732173327"></a><a name="p65699732173327"></a>Job object description</p>
</td>
</tr>
<tr id="row4779481717637"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p42808336173327"><a name="p42808336173327"></a><a name="p42808336173327"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p55508321174021"><a name="p55508321174021"></a><a name="p55508321174021"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1024215139405"><a name="p1024215139405"></a><a name="p1024215139405"></a>Project ID. For details on how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
</td>
</tr>
<tr id="row1495495217648"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p61232516173327"><a name="p61232516173327"></a><a name="p61232516173327"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p9124128174021"><a name="p9124128174021"></a><a name="p9124128174021"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p8513737173327"><a name="p8513737173327"></a><a name="p8513737173327"></a>Job object creation time</p>
</td>
</tr>
<tr id="row2384662617658"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p12110587173327"><a name="p12110587173327"></a><a name="p12110587173327"></a>mains</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p17782978173327"><a name="p17782978173327"></a><a name="p17782978173327"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p43671551173327"><a name="p43671551173327"></a><a name="p43671551173327"></a>Executable program set of a job object</p>
</td>
</tr>
<tr id="row305452361779"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p24571699173327"><a name="p24571699173327"></a><a name="p24571699173327"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p35399396173327"><a name="p35399396173327"></a><a name="p35399396173327"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p54671175173327"><a name="p54671175173327"></a><a name="p54671175173327"></a>Job object update time</p>
</td>
</tr>
<tr id="row5615267117721"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p5825773173327"><a name="p5825773173327"></a><a name="p5825773173327"></a>libs</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p45331175173327"><a name="p45331175173327"></a><a name="p45331175173327"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p16981856173327"><a name="p16981856173327"></a><a name="p16981856173327"></a>Dependency package set of a job object</p>
</td>
</tr>
<tr id="row4660982117733"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p49256169173327"><a name="p49256169173327"></a><a name="p49256169173327"></a>is_protected</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p38038412173327"><a name="p38038412173327"></a><a name="p38038412173327"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p59429132173327"><a name="p59429132173327"></a><a name="p59429132173327"></a>Whether a job object is protected</p>
<a name="ul45445577141414"></a><a name="ul45445577141414"></a><ul id="ul45445577141414"><li>true</li><li>false</li></ul>
<p id="p14310885151440"><a name="p14310885151440"></a><a name="p14310885151440"></a>The current version does not support this function.</p>
</td>
</tr>
<tr id="row2048741417746"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p5748711173327"><a name="p5748711173327"></a><a name="p5748711173327"></a>interface</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p34473875173327"><a name="p34473875173327"></a><a name="p34473875173327"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p9833738173327"><a name="p9833738173327"></a><a name="p9833738173327"></a>User-defined interface set</p>
</td>
</tr>
<tr id="row36805501785"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p30196392173327"><a name="p30196392173327"></a><a name="p30196392173327"></a>is_public</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p54822332173327"><a name="p54822332173327"></a><a name="p54822332173327"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p66821146173327"><a name="p66821146173327"></a><a name="p66821146173327"></a>Whether a job object is public</p>
<a name="ul16102444162419"></a><a name="ul16102444162419"></a><ul id="ul16102444162419"><li>true</li><li>false</li></ul>
<p id="p61739489162419"><a name="p61739489162419"></a><a name="p61739489162419"></a>The current version does not support this function.</p>
</td>
</tr>
<tr id="row2196179617822"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p22804970173327"><a name="p22804970173327"></a><a name="p22804970173327"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p2469217174057"><a name="p2469217174057"></a><a name="p2469217174057"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p47664891173327"><a name="p47664891173327"></a><a name="p47664891173327"></a>Job object type</p>
</td>
</tr>
<tr id="row2742286517547"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p45574254173327"><a name="p45574254173327"></a><a name="p45574254173327"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p66698908174057"><a name="p66698908174057"></a><a name="p66698908174057"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p30735983173327"><a name="p30735983173327"></a><a name="p30735983173327"></a>Job object ID</p>
</td>
</tr>
<tr id="row3736230917853"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p36233460173327"><a name="p36233460173327"></a><a name="p36233460173327"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p7478336174057"><a name="p7478336174057"></a><a name="p7478336174057"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p43748149173327"><a name="p43748149173327"></a><a name="p43748149173327"></a>Job object name</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section1210015461189"></a>

-   Example request

    ```
    GET /v1.1/{project_id}/jobs?limit=2&sort_by=name&marker=4f59aa66-bf38-402c-9b6f-320e77219b9b
    ```

-   Example response

    ```
    {
        "markers": {
            "prev": "62a287e9-76c3-458d-a2f8-56e2d824a9ee",
            "next": null
        },
        "jobs": [
            {
                "name": "my-mapreduce-job",
                "type": "MapReduce",
                "description": "This is the Map Reduce job template",
                "mains": [],
                "libs": [
                    {
                        "name": "my-job-binary-666",
                        "url": "/simple/mapreduce/program",
                        "description": "this is the job binary template",
                        "id": "2628d0e4-6109-4a09-a338-c4ee1b0963ed",
                        "tenant_id": "5a3314075bfa49b9ae360f4ecd333695",
                        "is_public": false,
                        "is_protected": null,
                        "extra": null
                    }
                ],
                "created_at": "2017-06-22T09:39:13",
                "updated_at": "2017-06-22T09:39:13",
                "id": "38a04cba-c113-4868-b11f-f50e8b1bf252",
                "tenant_id": "5a3314075bfa49b9ae360f4ecd333695",
                "is_public": false,
                "is_protected": false,
                "interface": []
            },
            {
                "name": "my-mapreduce-job-update",
                "type": "MapReduce",
                "description": "This is the Map Reduce job template",
                "mains": [],
                "libs": [
                    {
                        "name": "my-job-binary-666",
                        "url": "/simple/mapreduce/program",
                        "description": "this is the job binary template",
                        "id": "2628d0e4-6109-4a09-a338-c4ee1b0963ed",
                        "tenant_id": "5a3314075bfa49b9ae360f4ecd333695",
                        "is_public": false,
                        "is_protected": null,
                        "extra": null
                    }
                ],
                "created_at": "2017-06-22T12:05:58",
                "updated_at": "2017-06-22T12:05:58",
                "id": "b8ea4daa-0042-45e0-a522-e8b714e74760",
                "tenant_id": "5a3314075bfa49b9ae360f4ecd333695",
                "is_public": false,
                "is_protected": false,
                "interface": []
            }
        ]
    }
    ```


## Status Code<a name="section7365446163631"></a>

[Table 5](#table1584477916050)  describes the status code of this API.

**Table  5**  Status code

<a name="table1584477916050"></a>
<table><thead align="left"><tr id="row1339492016050"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.3.1.1"><p id="p3411176516050"><a name="p3411176516050"></a><a name="p3411176516050"></a>Status code</p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.2.3.1.2"><p id="p1158961516050"><a name="p1158961516050"></a><a name="p1158961516050"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3719767816050"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p6022194016050"><a name="p6022194016050"></a><a name="p6022194016050"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p4613894216050"><a name="p4613894216050"></a><a name="p4613894216050"></a>The job object list is queried successfully.</p>
</td>
</tr>
</tbody>
</table>

For the description about error status codes, see  [Status Codes](status-codes.md).

