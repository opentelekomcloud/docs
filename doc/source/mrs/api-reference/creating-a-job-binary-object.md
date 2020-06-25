# Creating a Job Binary Object<a name="EN-US_TOPIC_0172486201"></a>

## Function<a name="section13541137101416"></a>

This API is used to create a job binary object. This API is compatible with Sahara.

## URI<a name="section49980811101439"></a>

-   Format

    POST /v1.1/\{project\_id\}/job-binaries

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
    </tbody>
    </table>


## Request<a name="section7976792193238"></a>

**Table  2**  Request parameter description

<a name="table51257841151049"></a>
<table><thead align="left"><tr id="row8480851151049"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p15860319151049"><a name="p15860319151049"></a><a name="p15860319151049"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p9617423151049"><a name="p9617423151049"></a><a name="p9617423151049"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p40813771151049"><a name="p40813771151049"></a><a name="p40813771151049"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="p17581180151049"><a name="p17581180151049"></a><a name="p17581180151049"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row33862023103039"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p66764558103051"><a name="p66764558103051"></a><a name="p66764558103051"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p39220083103051"><a name="p39220083103051"></a><a name="p39220083103051"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p22710132103051"><a name="p22710132103051"></a><a name="p22710132103051"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p27581435103051"><a name="p27581435103051"></a><a name="p27581435103051"></a>Binary object name</p>
<p id="p3904672811352"><a name="p3904672811352"></a><a name="p3904672811352"></a>Contains 1 to 80 characters and consists of letters, digits, hyphens (-), and underscores (_) only.</p>
</td>
</tr>
<tr id="row4719796510464"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p6521450910469"><a name="p6521450910469"></a><a name="p6521450910469"></a>url</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p4788387310469"><a name="p4788387310469"></a><a name="p4788387310469"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p5338853410469"><a name="p5338853410469"></a><a name="p5338853410469"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p2950402010469"><a name="p2950402010469"></a><a name="p2950402010469"></a>Binary object URL, which contains of 1 to 255 characters.</p>
<p id="p4805152516398"><a name="p4805152516398"></a><a name="p4805152516398"></a>The URL must start with <strong id="b1932717215405"><a name="b1932717215405"></a><a name="b1932717215405"></a>s3a://</strong> or <strong id="b1066213397426"><a name="b1066213397426"></a><a name="b1066213397426"></a>/</strong>.</p>
</td>
</tr>
<tr id="row60274821103112"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p16682465103121"><a name="p16682465103121"></a><a name="p16682465103121"></a>is_protected</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p653385121120"><a name="p653385121120"></a><a name="p653385121120"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p66208658103121"><a name="p66208658103121"></a><a name="p66208658103121"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p61301077103121"><a name="p61301077103121"></a><a name="p61301077103121"></a>Whether a binary object is protected</p>
<a name="ul24233663152954"></a><a name="ul24233663152954"></a><ul id="ul24233663152954"><li>true</li><li>false</li></ul>
<p id="p16709791152954"><a name="p16709791152954"></a><a name="p16709791152954"></a>The current version does not support this function.</p>
</td>
</tr>
<tr id="row6726034151222"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p20438892151640"><a name="p20438892151640"></a><a name="p20438892151640"></a>is_public</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p378209391120"><a name="p378209391120"></a><a name="p378209391120"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p16062920151640"><a name="p16062920151640"></a><a name="p16062920151640"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p26028163151640"><a name="p26028163151640"></a><a name="p26028163151640"></a>Whether a binary object is public</p>
<a name="ul2283053116435"></a><a name="ul2283053116435"></a><ul id="ul2283053116435"><li>true</li><li>false</li></ul>
<p id="p45929516435"><a name="p45929516435"></a><a name="p45929516435"></a>The current version does not support this function.</p>
</td>
</tr>
<tr id="row1546567016045"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p2185314916152"><a name="p2185314916152"></a><a name="p2185314916152"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p79012551120"><a name="p79012551120"></a><a name="p79012551120"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p3397791716152"><a name="p3397791716152"></a><a name="p3397791716152"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p74792916152"><a name="p74792916152"></a><a name="p74792916152"></a>Binary object description</p>
<p id="p163088710188"><a name="p163088710188"></a><a name="p163088710188"></a>Contains a maximum of 65535 characters.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section38599577193858"></a>

**Table  3**  Response parameter description

<a name="table2520777103924"></a>
<table><thead align="left"><tr id="row18797656103924"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p46215177103924"><a name="p46215177103924"></a><a name="p46215177103924"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="p19932140103924"><a name="p19932140103924"></a><a name="p19932140103924"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p3890671103924"><a name="p3890671103924"></a><a name="p3890671103924"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row55511969104214"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p47996474104221"><a name="p47996474104221"></a><a name="p47996474104221"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p30078601104221"><a name="p30078601104221"></a><a name="p30078601104221"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p20447634104221"><a name="p20447634104221"></a><a name="p20447634104221"></a>Binary object description</p>
</td>
</tr>
<tr id="row46708914103924"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p25325661103924"><a name="p25325661103924"></a><a name="p25325661103924"></a>url</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p118157103924"><a name="p118157103924"></a><a name="p118157103924"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p9570786103924"><a name="p9570786103924"></a><a name="p9570786103924"></a>Binary object URL</p>
</td>
</tr>
<tr id="row6386960010401"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p605514510401"><a name="p605514510401"></a><a name="p605514510401"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p18350161104059"><a name="p18350161104059"></a><a name="p18350161104059"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p657412272348"><a name="p657412272348"></a><a name="p657412272348"></a>Project ID. For details on how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
</td>
</tr>
<tr id="row25442097104010"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p47543995104010"><a name="p47543995104010"></a><a name="p47543995104010"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p16046984104059"><a name="p16046984104059"></a><a name="p16046984104059"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p5606803104010"><a name="p5606803104010"></a><a name="p5606803104010"></a>Binary object creation time</p>
</td>
</tr>
<tr id="row35926613153722"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p24374572153722"><a name="p24374572153722"></a><a name="p24374572153722"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p1144197153722"><a name="p1144197153722"></a><a name="p1144197153722"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p25571161153722"><a name="p25571161153722"></a><a name="p25571161153722"></a>Binary object update time</p>
</td>
</tr>
<tr id="row40943146103924"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p28060554103924"><a name="p28060554103924"></a><a name="p28060554103924"></a>is_protected</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p25685468103924"><a name="p25685468103924"></a><a name="p25685468103924"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p148125103924"><a name="p148125103924"></a><a name="p148125103924"></a>Whether a binary object is protected</p>
<a name="ul230560601655"></a><a name="ul230560601655"></a><ul id="ul230560601655"><li>true</li><li>false</li></ul>
<p id="p306523561655"><a name="p306523561655"></a><a name="p306523561655"></a>The current version does not support this function.</p>
</td>
</tr>
<tr id="row32326809103924"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1225892103924"><a name="p1225892103924"></a><a name="p1225892103924"></a>is_public</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p57126811103924"><a name="p57126811103924"></a><a name="p57126811103924"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p63869016103924"><a name="p63869016103924"></a><a name="p63869016103924"></a>Whether a binary object is public</p>
<a name="ul393051701659"></a><a name="ul393051701659"></a><ul id="ul393051701659"><li>true</li><li>false</li></ul>
<p id="p650933911659"><a name="p650933911659"></a><a name="p650933911659"></a>The current version does not support this function.</p>
</td>
</tr>
<tr id="row16869530103924"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p18189813104253"><a name="p18189813104253"></a><a name="p18189813104253"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p56316713104253"><a name="p56316713104253"></a><a name="p56316713104253"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p2201971104253"><a name="p2201971104253"></a><a name="p2201971104253"></a>Binary object ID</p>
</td>
</tr>
<tr id="row17526607103924"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p45390223104325"><a name="p45390223104325"></a><a name="p45390223104325"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p43225188104325"><a name="p43225188104325"></a><a name="p43225188104325"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p11579305104325"><a name="p11579305104325"></a><a name="p11579305104325"></a>Binary object name</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section1210015461189"></a>

-   Example request

    ```
    { 
        "name": "my-job-binary",  
        "url": "/simple/mapreduce/program",  
        "is_protected": false,  
        "is_public": false,  
        "description": "this is the job binary template" 
    }
    ```

-   Example response

    ```
    {
        "job_binary": {
            "name": "my-job-binary",
            "url": "/simple/mapreduce/program",
            "description": "this is the job binary template",
            "created_at": "2017-06-22T09:04:53",
            "updated_at": null,
            "id": "da37b581-042f-4d7a-9378-f628f32bd9ae",
            "tenant_id": "5a3314075bfa49b9ae360f4ecd333695",
            "is_public": false,
            "is_protected": false
        }
    }
    ```


## Status Code<a name="section19688788101519"></a>

[Table 4](#table1584477916050)  describes the status code of this API.

**Table  4**  Status code

<a name="table1584477916050"></a>
<table><thead align="left"><tr id="row1339492016050"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.3.1.1"><p id="p3411176516050"><a name="p3411176516050"></a><a name="p3411176516050"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.2.3.1.2"><p id="p1158961516050"><a name="p1158961516050"></a><a name="p1158961516050"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3719767816050"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p6022194016050"><a name="p6022194016050"></a><a name="p6022194016050"></a>202</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p4613894216050"><a name="p4613894216050"></a><a name="p4613894216050"></a>The job binary object has been successfully created.</p>
</td>
</tr>
</tbody>
</table>

For the description about error status codes, see  [Status Codes](status-codes.md).

