# Updating a Job Object<a name="EN-US_TOPIC_0172486196"></a>

## Function<a name="section40666287163540"></a>

This API is used to update a job object. This API is compatible with Sahara.

## URI<a name="section25682805163556"></a>

-   Format

    PATCH /v1.1/\{project\_id\}/jobs/\{job\_id\}

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
    <tr id="row46308375171554"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p59990891171554"><a name="p59990891171554"></a><a name="p59990891171554"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p27424032171554"><a name="p27424032171554"></a><a name="p27424032171554"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p6754142171554"><a name="p6754142171554"></a><a name="p6754142171554"></a>Job object ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section7976792193238"></a>

**Table  2**  Request parameter description

<a name="table64845902141414"></a>
<table><thead align="left"><tr id="row58897534141414"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p5970972141414"><a name="p5970972141414"></a><a name="p5970972141414"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p13886698141414"><a name="p13886698141414"></a><a name="p13886698141414"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p51080720141414"><a name="p51080720141414"></a><a name="p51080720141414"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="p43897655141414"><a name="p43897655141414"></a><a name="p43897655141414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row66049158141414"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p48381606141414"><a name="p48381606141414"></a><a name="p48381606141414"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p26596031141414"><a name="p26596031141414"></a><a name="p26596031141414"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p6794872141414"><a name="p6794872141414"></a><a name="p6794872141414"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p13513721141414"><a name="p13513721141414"></a><a name="p13513721141414"></a>Job object name</p>
<p id="p1603959314432"><a name="p1603959314432"></a><a name="p1603959314432"></a>Contains 1 to 64 characters and consists of letters, digits, hyphens (-), and underscores (_) only.</p>
</td>
</tr>
<tr id="row54514628141414"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p53608773141414"><a name="p53608773141414"></a><a name="p53608773141414"></a>mains</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p47343395141414"><a name="p47343395141414"></a><a name="p47343395141414"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p9609797141414"><a name="p9609797141414"></a><a name="p9609797141414"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p40196116141414"><a name="p40196116141414"></a><a name="p40196116141414"></a>Executable program set of a job object</p>
<p id="p21881168154"><a name="p21881168154"></a><a name="p21881168154"></a>The current version does not support update of the executable program set.</p>
</td>
</tr>
<tr id="row26220727141414"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p43504180141414"><a name="p43504180141414"></a><a name="p43504180141414"></a>libs</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p34177681141414"><a name="p34177681141414"></a><a name="p34177681141414"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p16928758141414"><a name="p16928758141414"></a><a name="p16928758141414"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p29052172141414"><a name="p29052172141414"></a><a name="p29052172141414"></a>Dependency package set of a job object</p>
<p id="p3961344111510"><a name="p3961344111510"></a><a name="p3961344111510"></a>The current version does not support update of the dependency package set.</p>
</td>
</tr>
<tr id="row60142961141414"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p39741650141414"><a name="p39741650141414"></a><a name="p39741650141414"></a>is_protected</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p64957113141414"><a name="p64957113141414"></a><a name="p64957113141414"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p27034763141414"><a name="p27034763141414"></a><a name="p27034763141414"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p42332210141414"><a name="p42332210141414"></a><a name="p42332210141414"></a>Whether a job object is protected</p>
<a name="ul45445577141414"></a><a name="ul45445577141414"></a><ul id="ul45445577141414"><li>true</li><li>false</li></ul>
<p id="p14310885151440"><a name="p14310885151440"></a><a name="p14310885151440"></a>The current version does not support this function.</p>
</td>
</tr>
<tr id="row45156126141414"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p33767603141414"><a name="p33767603141414"></a><a name="p33767603141414"></a>interface</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p50821308141414"><a name="p50821308141414"></a><a name="p50821308141414"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p22885282141414"><a name="p22885282141414"></a><a name="p22885282141414"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p51841380165956"><a name="p51841380165956"></a><a name="p51841380165956"></a>User-defined interface set</p>
<p id="p2086434116214"><a name="p2086434116214"></a><a name="p2086434116214"></a>The current version does not support this function.</p>
</td>
</tr>
<tr id="row40372398141414"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p48938810141414"><a name="p48938810141414"></a><a name="p48938810141414"></a>is_public</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p4620670141414"><a name="p4620670141414"></a><a name="p4620670141414"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p38730019141414"><a name="p38730019141414"></a><a name="p38730019141414"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p50123857141414"><a name="p50123857141414"></a><a name="p50123857141414"></a>Whether a job object is public</p>
<a name="ul48461530141414"></a><a name="ul48461530141414"></a><ul id="ul48461530141414"><li>true</li><li>false</li></ul>
<p id="p40851722151312"><a name="p40851722151312"></a><a name="p40851722151312"></a>The current version does not support this function.</p>
</td>
</tr>
<tr id="row29193317141414"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p15848476141414"><a name="p15848476141414"></a><a name="p15848476141414"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p8658171141414"><a name="p8658171141414"></a><a name="p8658171141414"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p30223275141414"><a name="p30223275141414"></a><a name="p30223275141414"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p32166228141414"><a name="p32166228141414"></a><a name="p32166228141414"></a>Job object type</p>
<a name="ul21060597141414"></a><a name="ul21060597141414"></a><ul id="ul21060597141414"><li>MapReduce</li><li>Spark</li><li>Hive</li><li>DistCp</li><li>SparkScript</li></ul>
</td>
</tr>
<tr id="row27550880141414"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p17028818141414"><a name="p17028818141414"></a><a name="p17028818141414"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p37157041141414"><a name="p37157041141414"></a><a name="p37157041141414"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p56930340141414"><a name="p56930340141414"></a><a name="p56930340141414"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p47954836141414"><a name="p47954836141414"></a><a name="p47954836141414"></a>Job object description</p>
<p id="p38071851191616"><a name="p38071851191616"></a><a name="p38071851191616"></a>Contains a maximum of 65535 characters.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section38599577193858"></a>

**Table  3**  Response parameter description

<a name="table59661002165457"></a>
<table><thead align="left"><tr id="row10519102165457"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p46740914165457"><a name="p46740914165457"></a><a name="p46740914165457"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="p46739816165457"><a name="p46739816165457"></a><a name="p46739816165457"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p27828729165457"><a name="p27828729165457"></a><a name="p27828729165457"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row39534608165457"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p63009778165556"><a name="p63009778165556"></a><a name="p63009778165556"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p16556971165556"><a name="p16556971165556"></a><a name="p16556971165556"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p66046290165556"><a name="p66046290165556"></a><a name="p66046290165556"></a>Job object description</p>
</td>
</tr>
<tr id="row25337058165457"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p3995095165523"><a name="p3995095165523"></a><a name="p3995095165523"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p5010671716586"><a name="p5010671716586"></a><a name="p5010671716586"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1768719515356"><a name="p1768719515356"></a><a name="p1768719515356"></a>Project ID. For details on how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
</td>
</tr>
<tr id="row12452905165457"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p9142694165522"><a name="p9142694165522"></a><a name="p9142694165522"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p5818509216586"><a name="p5818509216586"></a><a name="p5818509216586"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p43099508165522"><a name="p43099508165522"></a><a name="p43099508165522"></a>Job object creation time</p>
</td>
</tr>
<tr id="row5765868144424"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p64382198144424"><a name="p64382198144424"></a><a name="p64382198144424"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p28416508144424"><a name="p28416508144424"></a><a name="p28416508144424"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p20035783144424"><a name="p20035783144424"></a><a name="p20035783144424"></a>Job object update time</p>
</td>
</tr>
<tr id="row45726010165636"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p15790016165745"><a name="p15790016165745"></a><a name="p15790016165745"></a>mains</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p49320399165745"><a name="p49320399165745"></a><a name="p49320399165745"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p35529400165745"><a name="p35529400165745"></a><a name="p35529400165745"></a>Executable program set of a job object</p>
</td>
</tr>
<tr id="row52234583165644"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p64020041165745"><a name="p64020041165745"></a><a name="p64020041165745"></a>libs</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p1110262165745"><a name="p1110262165745"></a><a name="p1110262165745"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p22822436165745"><a name="p22822436165745"></a><a name="p22822436165745"></a>Dependency package set of a job object</p>
</td>
</tr>
<tr id="row48958638165457"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p6226708165457"><a name="p6226708165457"></a><a name="p6226708165457"></a>is_protected</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p51245066165457"><a name="p51245066165457"></a><a name="p51245066165457"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p57209706165457"><a name="p57209706165457"></a><a name="p57209706165457"></a>Whether a job object is protected</p>
<a name="ul27883211162228"></a><a name="ul27883211162228"></a><ul id="ul27883211162228"><li>true</li><li>false</li></ul>
<p id="p59984291162228"><a name="p59984291162228"></a><a name="p59984291162228"></a>The current version does not support this function.</p>
</td>
</tr>
<tr id="row13009340165457"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p47123581165457"><a name="p47123581165457"></a><a name="p47123581165457"></a>interface</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p7281273165457"><a name="p7281273165457"></a><a name="p7281273165457"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p52912260165457"><a name="p52912260165457"></a><a name="p52912260165457"></a>User-defined interface set</p>
</td>
</tr>
<tr id="row6448297165457"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p52550072165457"><a name="p52550072165457"></a><a name="p52550072165457"></a>is_public</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p42790907165457"><a name="p42790907165457"></a><a name="p42790907165457"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p43511423165457"><a name="p43511423165457"></a><a name="p43511423165457"></a>Whether a job object is public</p>
<a name="ul34382005162224"></a><a name="ul34382005162224"></a><ul id="ul34382005162224"><li>true</li><li>false</li></ul>
<p id="p32875830162224"><a name="p32875830162224"></a><a name="p32875830162224"></a>The current version does not support this function.</p>
</td>
</tr>
<tr id="row64450389165457"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p53098998165457"><a name="p53098998165457"></a><a name="p53098998165457"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p20418607165457"><a name="p20418607165457"></a><a name="p20418607165457"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p43294486165457"><a name="p43294486165457"></a><a name="p43294486165457"></a>Job object type</p>
</td>
</tr>
<tr id="row20514830165457"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p43131972165659"><a name="p43131972165659"></a><a name="p43131972165659"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p15928073165725"><a name="p15928073165725"></a><a name="p15928073165725"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p34994329165659"><a name="p34994329165659"></a><a name="p34994329165659"></a>Job object ID</p>
</td>
</tr>
<tr id="row2613903516576"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p3688706316576"><a name="p3688706316576"></a><a name="p3688706316576"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p19040333165725"><a name="p19040333165725"></a><a name="p19040333165725"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p6070871216576"><a name="p6070871216576"></a><a name="p6070871216576"></a>Job object name</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section1210015461189"></a>

-   Example request

    ```
    {    
        "name": "my-mapreduce-job-update",         
        "mains": [ ],         
        "libs": [                 
        "2628d0e4-6109-4a09-a338-c4ee1b0963ed"        
        ],         
        "is_protected": false,         
        "interface": [ ],         
        "is_public": false,         
        "type": "MapReduce",         
        "description": "This is the Map Reduce job template"    
    }
    ```

-   Example response

    ```
    {
        "job": {
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
    }
    ```


## Status Code<a name="section7365446163631"></a>

[Table 4](#table1584477916050)  describes the status code of this API.

**Table  4**  Status code

<a name="table1584477916050"></a>
<table><thead align="left"><tr id="row1339492016050"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.3.1.1"><p id="p3411176516050"><a name="p3411176516050"></a><a name="p3411176516050"></a>Status code</p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.2.3.1.2"><p id="p1158961516050"><a name="p1158961516050"></a><a name="p1158961516050"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3719767816050"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p6022194016050"><a name="p6022194016050"></a><a name="p6022194016050"></a>202</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p4613894216050"><a name="p4613894216050"></a><a name="p4613894216050"></a>The job object has been successfully updated.</p>
</td>
</tr>
</tbody>
</table>

For the description about error status codes, see  [Status Codes](status-codes.md).

