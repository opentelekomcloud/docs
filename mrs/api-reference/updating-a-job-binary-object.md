# Updating a Job Binary Object<a name="EN-US_TOPIC_0172486219"></a>

## Function<a name="section13541137101416"></a>

This API is used to update a job binary object. This API is compatible with Sahara.

## URI<a name="section49980811101439"></a>

-   Format

    PUT /v1.1/\{project\_id\}/job-binaries/\{job\_binary\_id\}

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
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p39220083103051"><a name="p39220083103051"></a><a name="p39220083103051"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p22710132103051"><a name="p22710132103051"></a><a name="p22710132103051"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p27581435103051"><a name="p27581435103051"></a><a name="p27581435103051"></a>Binary object name</p>
<p id="p3904672811352"><a name="p3904672811352"></a><a name="p3904672811352"></a>Contains 1 to 80 characters and consists of letters, digits, hyphens (-), and underscores (_) only.</p>
</td>
</tr>
<tr id="row4719796510464"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p6521450910469"><a name="p6521450910469"></a><a name="p6521450910469"></a>url</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p4788387310469"><a name="p4788387310469"></a><a name="p4788387310469"></a>No</p>
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
<a name="ul6551573216658"></a><a name="ul6551573216658"></a><ul id="ul6551573216658"><li>true</li><li>false</li></ul>
<p id="p4656684916658"><a name="p4656684916658"></a><a name="p4656684916658"></a>The current version does not support this function.</p>
</td>
</tr>
<tr id="row1546567016045"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p2185314916152"><a name="p2185314916152"></a><a name="p2185314916152"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p79012551120"><a name="p79012551120"></a><a name="p79012551120"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p3397791716152"><a name="p3397791716152"></a><a name="p3397791716152"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p74792916152"><a name="p74792916152"></a><a name="p74792916152"></a>Binary object description</p>
<p id="p19803155762718"><a name="p19803155762718"></a><a name="p19803155762718"></a>Contains a maximum of 65535 characters.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section38599577193858"></a>

**Table  3**  Response parameter description

<a name="table65392315111353"></a>
<table><thead align="left"><tr id="row34315492111353"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p28091506111353"><a name="p28091506111353"></a><a name="p28091506111353"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="p27434435111353"><a name="p27434435111353"></a><a name="p27434435111353"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p7596758111353"><a name="p7596758111353"></a><a name="p7596758111353"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row11357670111353"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p47556058111353"><a name="p47556058111353"></a><a name="p47556058111353"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p26190480111353"><a name="p26190480111353"></a><a name="p26190480111353"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p41054113111353"><a name="p41054113111353"></a><a name="p41054113111353"></a>Binary object description</p>
</td>
</tr>
<tr id="row33942704111353"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p65004536111353"><a name="p65004536111353"></a><a name="p65004536111353"></a>url</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p17931936111353"><a name="p17931936111353"></a><a name="p17931936111353"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p43200721111353"><a name="p43200721111353"></a><a name="p43200721111353"></a>Binary object URL</p>
</td>
</tr>
<tr id="row53262173111353"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p19268770111353"><a name="p19268770111353"></a><a name="p19268770111353"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p56411121111353"><a name="p56411121111353"></a><a name="p56411121111353"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p7857191573713"><a name="p7857191573713"></a><a name="p7857191573713"></a>Project ID. For details on how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
</td>
</tr>
<tr id="row53082533111353"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p4717921111353"><a name="p4717921111353"></a><a name="p4717921111353"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p17096362111353"><a name="p17096362111353"></a><a name="p17096362111353"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p42628104111353"><a name="p42628104111353"></a><a name="p42628104111353"></a>Binary object creation time</p>
</td>
</tr>
<tr id="row65080540154130"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p37032416154130"><a name="p37032416154130"></a><a name="p37032416154130"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p35596989154130"><a name="p35596989154130"></a><a name="p35596989154130"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p64783846154130"><a name="p64783846154130"></a><a name="p64783846154130"></a>Binary object update time</p>
</td>
</tr>
<tr id="row48108617111353"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p4483910111353"><a name="p4483910111353"></a><a name="p4483910111353"></a>is_protected</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p25255806111353"><a name="p25255806111353"></a><a name="p25255806111353"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p32454409111353"><a name="p32454409111353"></a><a name="p32454409111353"></a>Whether a binary object is protected</p>
<a name="ul3762529416743"></a><a name="ul3762529416743"></a><ul id="ul3762529416743"><li>true</li><li>false</li></ul>
<p id="p4842317916743"><a name="p4842317916743"></a><a name="p4842317916743"></a>The current version does not support this function.</p>
</td>
</tr>
<tr id="row23654226111353"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p36944171111353"><a name="p36944171111353"></a><a name="p36944171111353"></a>is_public</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p60598757111353"><a name="p60598757111353"></a><a name="p60598757111353"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p9552279111353"><a name="p9552279111353"></a><a name="p9552279111353"></a>Whether a binary object is public</p>
<a name="ul6035424216746"></a><a name="ul6035424216746"></a><ul id="ul6035424216746"><li>true</li><li>false</li></ul>
<p id="p4193671516746"><a name="p4193671516746"></a><a name="p4193671516746"></a>The current version does not support this function.</p>
</td>
</tr>
<tr id="row18861649111353"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p51398639111353"><a name="p51398639111353"></a><a name="p51398639111353"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p4432992111353"><a name="p4432992111353"></a><a name="p4432992111353"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p23528067111353"><a name="p23528067111353"></a><a name="p23528067111353"></a>Binary object ID</p>
</td>
</tr>
<tr id="row10426016111353"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p39200957111353"><a name="p39200957111353"></a><a name="p39200957111353"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p36313784111353"><a name="p36313784111353"></a><a name="p36313784111353"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p55735398111353"><a name="p55735398111353"></a><a name="p55735398111353"></a>Binary object name</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section1210015461189"></a>

-   Example request

    ```
    { 
        "name": "my-job-binary-update",  
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
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p4613894216050"><a name="p4613894216050"></a><a name="p4613894216050"></a>The binary object has been updated successfully.</p>
</td>
</tr>
</tbody>
</table>

For the description about error status codes, see  [Status Codes](status-codes.md).

