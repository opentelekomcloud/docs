# Creating a Job Object<a name="EN-US_TOPIC_0172486197"></a>

## Function<a name="section40666287163540"></a>

This API is used to create a job object. This API is compatible with Sahara.

## URI<a name="section25682805163556"></a>

-   Format

    POST /v1.1/\{project\_id\}/jobs

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
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p207690014257"><a name="p207690014257"></a><a name="p207690014257"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p22710132103051"><a name="p22710132103051"></a><a name="p22710132103051"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p27581435103051"><a name="p27581435103051"></a><a name="p27581435103051"></a>Job object name</p>
<p id="p24316035143322"><a name="p24316035143322"></a><a name="p24316035143322"></a>Contains 1 to 80 characters and consists of letters, digits, hyphens (-), and underscores (_) only.</p>
</td>
</tr>
<tr id="row22681519104555"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p62177253104629"><a name="p62177253104629"></a><a name="p62177253104629"></a>mains</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p3476698514319"><a name="p3476698514319"></a><a name="p3476698514319"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p57283501104629"><a name="p57283501104629"></a><a name="p57283501104629"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p9452014104629"><a name="p9452014104629"></a><a name="p9452014104629"></a>Executable program set of a job object</p>
<p id="p4353308112728"><a name="p4353308112728"></a><a name="p4353308112728"></a>If the job type is Hive or Spark Script, the value of <strong id="b1689470184713"><a name="b1689470184713"></a><a name="b1689470184713"></a>mains</strong> must not be empty.</p>
<p id="p46902461112746"><a name="p46902461112746"></a><a name="p46902461112746"></a>For details on how to obtain the executable program, see <a href="creating-a-job-binary-object.md">Creating a Job Binary Object</a>.</p>
</td>
</tr>
<tr id="row4719796510464"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p6521450910469"><a name="p6521450910469"></a><a name="p6521450910469"></a>libs</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p633981614319"><a name="p633981614319"></a><a name="p633981614319"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p5338853410469"><a name="p5338853410469"></a><a name="p5338853410469"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p5409080711259"><a name="p5409080711259"></a><a name="p5409080711259"></a>Dependency package set of a job object</p>
<p id="p19928586112535"><a name="p19928586112535"></a><a name="p19928586112535"></a>If the job type is MapReduce or Spark, the value of <strong id="b775065414712"><a name="b775065414712"></a><a name="b775065414712"></a>libs</strong> must not be empty.</p>
<p id="p2950402010469"><a name="p2950402010469"></a><a name="p2950402010469"></a>For details on how to obtain the dependency package, see <a href="creating-a-job-binary-object.md">Creating a Job Binary Object</a>.</p>
</td>
</tr>
<tr id="row60274821103112"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p16682465103121"><a name="p16682465103121"></a><a name="p16682465103121"></a>is_protected</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p2616717514319"><a name="p2616717514319"></a><a name="p2616717514319"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p66208658103121"><a name="p66208658103121"></a><a name="p66208658103121"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p61301077103121"><a name="p61301077103121"></a><a name="p61301077103121"></a>Whether a job object is protected</p>
<a name="ul14838786103121"></a><a name="ul14838786103121"></a><ul id="ul14838786103121"><li>true</li><li>false</li></ul>
<p id="p60751061161756"><a name="p60751061161756"></a><a name="p60751061161756"></a>The current version does not support this function.</p>
</td>
</tr>
<tr id="row7283691165011"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p53108105165011"><a name="p53108105165011"></a><a name="p53108105165011"></a>interface</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p708398414319"><a name="p708398414319"></a><a name="p708398414319"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p13061488165011"><a name="p13061488165011"></a><a name="p13061488165011"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p51347592165011"><a name="p51347592165011"></a><a name="p51347592165011"></a>User-defined interface set</p>
<p id="p937511912139"><a name="p937511912139"></a><a name="p937511912139"></a>The current version does not support this function.</p>
</td>
</tr>
<tr id="row6726034151222"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p20438892151640"><a name="p20438892151640"></a><a name="p20438892151640"></a>is_public</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p3988522414319"><a name="p3988522414319"></a><a name="p3988522414319"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p16062920151640"><a name="p16062920151640"></a><a name="p16062920151640"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p26028163151640"><a name="p26028163151640"></a><a name="p26028163151640"></a>Whether a job object is public</p>
<a name="ul32926880151640"></a><a name="ul32926880151640"></a><ul id="ul32926880151640"><li>true</li><li>false</li></ul>
<p id="p30840219161910"><a name="p30840219161910"></a><a name="p30840219161910"></a>The current version does not support this function.</p>
</td>
</tr>
<tr id="row32868124165025"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p45072358165025"><a name="p45072358165025"></a><a name="p45072358165025"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p26982364165025"><a name="p26982364165025"></a><a name="p26982364165025"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p38087912165025"><a name="p38087912165025"></a><a name="p38087912165025"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p65221999165025"><a name="p65221999165025"></a><a name="p65221999165025"></a>Job object type</p>
<a name="ul41980356165224"></a><a name="ul41980356165224"></a><ul id="ul41980356165224"><li>MapReduce</li><li>Spark</li><li>Hive (not supported currently)</li><li>hql</li><li>DistCp</li><li>SparkScript</li><li>SparkSql (not supported in this API currently)</li></ul>
</td>
</tr>
<tr id="row1546567016045"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p2185314916152"><a name="p2185314916152"></a><a name="p2185314916152"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p2527461516152"><a name="p2527461516152"></a><a name="p2527461516152"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p3397791716152"><a name="p3397791716152"></a><a name="p3397791716152"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p74792916152"><a name="p74792916152"></a><a name="p74792916152"></a>Job object description</p>
<p id="p1211513514815"><a name="p1211513514815"></a><a name="p1211513514815"></a>Contains a maximum of 65535 characters.</p>
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
<tr id="row6430303593958"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p4116333193958"><a name="p4116333193958"></a><a name="p4116333193958"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p2654730093958"><a name="p2654730093958"></a><a name="p2654730093958"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p284769393958"><a name="p284769393958"></a><a name="p284769393958"></a>Job object update time</p>
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
<a name="ul35340370162024"></a><a name="ul35340370162024"></a><ul id="ul35340370162024"><li>true</li><li>false</li></ul>
<p id="p60435047162024"><a name="p60435047162024"></a><a name="p60435047162024"></a>The current version does not support this function.</p>
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
<a name="ul5045624162013"></a><a name="ul5045624162013"></a><ul id="ul5045624162013"><li>true</li><li>false</li></ul>
<p id="p54381902162013"><a name="p54381902162013"></a><a name="p54381902162013"></a>The current version does not support this function.</p>
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
    The request example of MapReduce job: 
    {    
        "name": "my-mapreduce-job",         
        "mains": [ ],         
        "libs": [                 
        "092b628b-26a3-4571-9ba4-f8d000df8877"        
        ],         
        "is_protected": false,         
        "interface": [ ],         
        "is_public": false,         
        "type": "MapReduce",         
        "description": "This is the Map Reduce job template"    
    } 
     
    The request example of Spark job: 
    { 
        "name": "my-spark-job",  
        "type": "Spark",  
        "description": "This is the Spark job template",  
        "mains": [ ],  
        "libs": [ 
            "ed2ffd92-6308-44cb-b930-e10b6d65d3aa" 
        ],  
        "is_public": false,  
        "is_protected": false,  
        "interface": [ ] 
    }
    
    The request example of DistCp job: 
    { 
        "name": "my-distcp-job",  
        "type": "DistCp",  
        "description": "This is the DistCp job template",  
        "mains": [ ],  
        "libs": [ ],  
        "is_public": false,  
        "is_protected": false,  
        "interface": [ ] 
    }
    
    The request example of Hive job:
    { 
        "name": "my-hive-job",  
        "type": "Hive",  
        "description": "This is the Hive job template",  
    "mains": [
        "0d58a7e1-3ea7-413e-9a94-7702f99a9fa2"
    ],  
        "libs": [ ],  
        "is_public": false,  
        "is_protected": false,  
        "interface": [ ] 
    }
    
    The request example of SparkScript job:
    { 
        "name": "my-sparkscript-job",  
        "type": "SparkScript",  
        "description": "This is the SparkScript job template",  
        "mains": [
        "89e6a8bc-dde1-4053-97c1-72504f630dbf"
        ],  
        "libs": [ ],  
        "is_public": false,  
        "is_protected": false,  
        "interface": [ ] 
    }
    ```

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
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p4613894216050"><a name="p4613894216050"></a><a name="p4613894216050"></a>The job object has been successfully created.</p>
</td>
</tr>
</tbody>
</table>

For the description about error status codes, see  [Status Codes](status-codes.md).

