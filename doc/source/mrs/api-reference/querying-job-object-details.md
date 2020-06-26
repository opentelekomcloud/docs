# Querying Job Object Details<a name="EN-US_TOPIC_0172486208"></a>

## Function<a name="section40666287163540"></a>

This API is used to query detailed information about a job object. This API is compatible with Sahara.

## URI<a name="section25682805163556"></a>

-   Format

    GET /v1.1/\{project\_id\}/jobs/\{job\_id\}

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
    <tbody><tr id="row12931900144556"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p40851019144556"><a name="p40851019144556"></a><a name="p40851019144556"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p20598275144556"><a name="p20598275144556"></a><a name="p20598275144556"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p57847563144556"><a name="p57847563144556"></a><a name="p57847563144556"></a>Project ID. For details on how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row5348473617029"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p3729636117029"><a name="p3729636117029"></a><a name="p3729636117029"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p110643517029"><a name="p110643517029"></a><a name="p110643517029"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p2251243817029"><a name="p2251243817029"></a><a name="p2251243817029"></a>Job object ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section7976792193238"></a>

**Request parameters**

None

## Response<a name="section38599577193858"></a>

**Table  2**  Response parameter description

<a name="table5154210817547"></a>
<table><thead align="left"><tr id="row5182537317547"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p3710571317547"><a name="p3710571317547"></a><a name="p3710571317547"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="p4673655817547"><a name="p4673655817547"></a><a name="p4673655817547"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p2756483917547"><a name="p2756483917547"></a><a name="p2756483917547"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row2282909519515"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p511042419522"><a name="p511042419522"></a><a name="p511042419522"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p4216874019522"><a name="p4216874019522"></a><a name="p4216874019522"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1768719515356"><a name="p1768719515356"></a><a name="p1768719515356"></a>Project ID. For details on how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
</td>
</tr>
<tr id="row4628798119532"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p4662995419539"><a name="p4662995419539"></a><a name="p4662995419539"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p5692937519539"><a name="p5692937519539"></a><a name="p5692937519539"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p4787664819539"><a name="p4787664819539"></a><a name="p4787664819539"></a>Job object creation time</p>
</td>
</tr>
<tr id="row3275478619555"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p277685231966"><a name="p277685231966"></a><a name="p277685231966"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p558238521966"><a name="p558238521966"></a><a name="p558238521966"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p254381651966"><a name="p254381651966"></a><a name="p254381651966"></a>Job object ID</p>
</td>
</tr>
<tr id="row394775811961"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p223764941966"><a name="p223764941966"></a><a name="p223764941966"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p450946541966"><a name="p450946541966"></a><a name="p450946541966"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p287883401966"><a name="p287883401966"></a><a name="p287883401966"></a>Job object name</p>
</td>
</tr>
<tr id="row539121719625"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p3343201519749"><a name="p3343201519749"></a><a name="p3343201519749"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p3568595119749"><a name="p3568595119749"></a><a name="p3568595119749"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p488090119749"><a name="p488090119749"></a><a name="p488090119749"></a>Job object update time</p>
</td>
</tr>
<tr id="row134024519637"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p6560074719645"><a name="p6560074719645"></a><a name="p6560074719645"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p3735645219645"><a name="p3735645219645"></a><a name="p3735645219645"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p597380019645"><a name="p597380019645"></a><a name="p597380019645"></a>Job object description</p>
</td>
</tr>
<tr id="row2196179617822"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p342696619659"><a name="p342696619659"></a><a name="p342696619659"></a>interface</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p285542119659"><a name="p285542119659"></a><a name="p285542119659"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p2996254519659"><a name="p2996254519659"></a><a name="p2996254519659"></a>User-defined interface set</p>
</td>
</tr>
<tr id="row2742286517547"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p10630271977"><a name="p10630271977"></a><a name="p10630271977"></a>libs</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p623086031977"><a name="p623086031977"></a><a name="p623086031977"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p138320451977"><a name="p138320451977"></a><a name="p138320451977"></a>Dependency package set of a job object</p>
</td>
</tr>
<tr id="row3736230917853"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p293931571964"><a name="p293931571964"></a><a name="p293931571964"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p77970001964"><a name="p77970001964"></a><a name="p77970001964"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p397013291964"><a name="p397013291964"></a><a name="p397013291964"></a>Job object type</p>
</td>
</tr>
<tr id="row1786102519722"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p787637119758"><a name="p787637119758"></a><a name="p787637119758"></a>mains</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p305111719758"><a name="p305111719758"></a><a name="p305111719758"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p4581390619758"><a name="p4581390619758"></a><a name="p4581390619758"></a>Executable program set of a job object</p>
</td>
</tr>
<tr id="row1938744719726"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p4919799719740"><a name="p4919799719740"></a><a name="p4919799719740"></a>is_protected</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p6153381419740"><a name="p6153381419740"></a><a name="p6153381419740"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1818301319740"><a name="p1818301319740"></a><a name="p1818301319740"></a>Whether a job object is protected</p>
<a name="ul27945944162458"></a><a name="ul27945944162458"></a><ul id="ul27945944162458"><li>true</li><li>false</li></ul>
<p id="p38608103162458"><a name="p38608103162458"></a><a name="p38608103162458"></a>The current version does not support this function.</p>
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
        "job": {
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
        }
    }
    ```


## Status Code<a name="section7365446163631"></a>

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
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p4613894216050"><a name="p4613894216050"></a><a name="p4613894216050"></a>The job object details are queried successfully.</p>
</td>
</tr>
</tbody>
</table>

For the description about error status codes, see  [Status Codes](status-codes.md).

