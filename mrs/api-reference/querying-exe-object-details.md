# Querying exe Object Details<a name="EN-US_TOPIC_0172486198"></a>

## Function<a name="section40666287163540"></a>

This API is used to query detailed information about the exe object of a job. This API is incompatible with Sahara.

## URI<a name="section25682805163556"></a>

-   Format

    GET /v1.1/\{project\_id\}/job-exes/\{job\_exe\_id\}

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
    <tr id="row37407495194754"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p12883183194310"><a name="p12883183194310"></a><a name="p12883183194310"></a>job_exe_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p19030045194310"><a name="p19030045194310"></a><a name="p19030045194310"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p51134712194310"><a name="p51134712194310"></a><a name="p51134712194310"></a>Job ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section7976792193238"></a>

**Request parameters**

None

## Response<a name="section38599577193858"></a>

**Table  2**  Response parameter description

<a name="table3315199519550"></a>
<table><thead align="left"><tr id="row578377519550"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p38420820195833"><a name="p38420820195833"></a><a name="p38420820195833"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="p18107258195833"><a name="p18107258195833"></a><a name="p18107258195833"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p57401825195833"><a name="p57401825195833"></a><a name="p57401825195833"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row4877039619550"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1036349219556"><a name="p1036349219556"></a><a name="p1036349219556"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p3507660919556"><a name="p3507660919556"></a><a name="p3507660919556"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p3191186819556"><a name="p3191186819556"></a><a name="p3191186819556"></a>Job ID</p>
</td>
</tr>
<tr id="row5452608519550"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p492591519556"><a name="p492591519556"></a><a name="p492591519556"></a>create_at</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p65547675193741"><a name="p65547675193741"></a><a name="p65547675193741"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p46076642191954"><a name="p46076642191954"></a><a name="p46076642191954"></a>Creation time, which is a 13-bit timestamp.</p>
</td>
</tr>
<tr id="row90837019550"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p646916119550"><a name="p646916119550"></a><a name="p646916119550"></a>update_at</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p31855594195115"><a name="p31855594195115"></a><a name="p31855594195115"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p9461207191918"><a name="p9461207191918"></a><a name="p9461207191918"></a>Update time, which is a 13-bit timestamp.</p>
</td>
</tr>
<tr id="row5085722819550"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p2579483119550"><a name="p2579483119550"></a><a name="p2579483119550"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p5844159719550"><a name="p5844159719550"></a><a name="p5844159719550"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1768719515356"><a name="p1768719515356"></a><a name="p1768719515356"></a>Project ID. For details on how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
</td>
</tr>
<tr id="row5690483719550"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p4588905219550"><a name="p4588905219550"></a><a name="p4588905219550"></a>job_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p44975318193910"><a name="p44975318193910"></a><a name="p44975318193910"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p3001481419550"><a name="p3001481419550"></a><a name="p3001481419550"></a>Job ID</p>
</td>
</tr>
<tr id="row169787619550"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p331026719550"><a name="p331026719550"></a><a name="p331026719550"></a>job_name</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p42427159193910"><a name="p42427159193910"></a><a name="p42427159193910"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p2005248319550"><a name="p2005248319550"></a><a name="p2005248319550"></a>Job name</p>
</td>
</tr>
<tr id="row4625462019550"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p5563670019550"><a name="p5563670019550"></a><a name="p5563670019550"></a>start_time</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p29918955193921"><a name="p29918955193921"></a><a name="p29918955193921"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p2026254620146"><a name="p2026254620146"></a><a name="p2026254620146"></a>Start time of job execution, which is a 13-bit timestamp.</p>
</td>
</tr>
<tr id="row2176045219550"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1776620019550"><a name="p1776620019550"></a><a name="p1776620019550"></a>end_time</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p37327910193921"><a name="p37327910193921"></a><a name="p37327910193921"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p5041299620146"><a name="p5041299620146"></a><a name="p5041299620146"></a>End time of job execution, which is a 13-bit timestamp.</p>
</td>
</tr>
<tr id="row6143635119550"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1028852819550"><a name="p1028852819550"></a><a name="p1028852819550"></a>cluster_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p5862431019550"><a name="p5862431019550"></a><a name="p5862431019550"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p2281683220216"><a name="p2281683220216"></a><a name="p2281683220216"></a>Cluster ID of a job</p>
</td>
</tr>
<tr id="row5588512519550"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p3040126119550"><a name="p3040126119550"></a><a name="p3040126119550"></a>group_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p1380124819410"><a name="p1380124819410"></a><a name="p1380124819410"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1891440820216"><a name="p1891440820216"></a><a name="p1891440820216"></a>Group ID of a job</p>
</td>
</tr>
<tr id="row2461506319550"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p4766307219550"><a name="p4766307219550"></a><a name="p4766307219550"></a>jar_path</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p1405183219410"><a name="p1405183219410"></a><a name="p1405183219410"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p34979288192243"><a name="p34979288192243"></a><a name="p34979288192243"></a>Path of the <strong id="b15121162817710"><a name="b15121162817710"></a><a name="b15121162817710"></a>.jar</strong> file or <strong id="b20127132262011"><a name="b20127132262011"></a><a name="b20127132262011"></a>.sql</strong> file for program execution</p>
</td>
</tr>
<tr id="row3958047819550"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p5190214619550"><a name="p5190214619550"></a><a name="p5190214619550"></a>input</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p1627104919410"><a name="p1627104919410"></a><a name="p1627104919410"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p4996084420258"><a name="p4996084420258"></a><a name="p4996084420258"></a>Address for inputting data</p>
</td>
</tr>
<tr id="row1217098519727"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p4632576819727"><a name="p4632576819727"></a><a name="p4632576819727"></a>output</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p989452319410"><a name="p989452319410"></a><a name="p989452319410"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p852868320258"><a name="p852868320258"></a><a name="p852868320258"></a>Address for outputting data</p>
</td>
</tr>
<tr id="row3799281119842"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p5751881819842"><a name="p5751881819842"></a><a name="p5751881819842"></a>job_log</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p3324274119410"><a name="p3324274119410"></a><a name="p3324274119410"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p4477291020258"><a name="p4477291020258"></a><a name="p4477291020258"></a>Address for storing job logs</p>
</td>
</tr>
<tr id="row399573611990"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p153208431990"><a name="p153208431990"></a><a name="p153208431990"></a>job_type</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p580869611990"><a name="p580869611990"></a><a name="p580869611990"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p74233721990"><a name="p74233721990"></a><a name="p74233721990"></a>Job type code</p>
<a name="ul52805946192537"></a><a name="ul52805946192537"></a><ul id="ul52805946192537"><li>1: MapReduce</li><li>2: Spark</li><li>3: Hive Script</li><li>4: HiveQL (not supported currently)</li><li>5: DistCp</li><li>6: Spark Script</li><li>7: Spark SQL (not supported in this API currently)</li></ul>
</td>
</tr>
<tr id="row4199685319913"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p4630192719913"><a name="p4630192719913"></a><a name="p4630192719913"></a>file_action</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p5222674819913"><a name="p5222674819913"></a><a name="p5222674819913"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p250820819913"><a name="p250820819913"></a><a name="p250820819913"></a>Data import and export</p>
</td>
</tr>
<tr id="row4714693819921"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p6080567119921"><a name="p6080567119921"></a><a name="p6080567119921"></a>arguments</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p5092218519921"><a name="p5092218519921"></a><a name="p5092218519921"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p10094543192658"><a name="p10094543192658"></a><a name="p10094543192658"></a>Key parameter for program execution. The parameter is specified by the function of the user's program. MRS is only responsible for loading the parameter. This parameter can be empty.</p>
</td>
</tr>
<tr id="row6009214319943"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p3562540819943"><a name="p3562540819943"></a><a name="p3562540819943"></a>hql</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p6523786219943"><a name="p6523786219943"></a><a name="p6523786219943"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p4977550119943"><a name="p4977550119943"></a><a name="p4977550119943"></a>HiveQL statement</p>
</td>
</tr>
<tr id="row1859114019956"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p2948735219956"><a name="p2948735219956"></a><a name="p2948735219956"></a>job_state</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p5877310219956"><a name="p5877310219956"></a><a name="p5877310219956"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p57659102193943"><a name="p57659102193943"></a><a name="p57659102193943"></a>Job status code</p>
<a name="ul29263952193948"></a><a name="ul29263952193948"></a><ul id="ul29263952193948"><li>-1: Terminated</li><li>1: Starting</li><li>2: Running</li><li>3: Completed</li><li>4: Abnormal</li><li>5: Error</li></ul>
</td>
</tr>
<tr id="row51998636191052"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p51139963191052"><a name="p51139963191052"></a><a name="p51139963191052"></a>job_final_status</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p52088375191052"><a name="p52088375191052"></a><a name="p52088375191052"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p25388152145857"><a name="p25388152145857"></a><a name="p25388152145857"></a>Final job status</p>
<a name="ul27166780145857"></a><a name="ul27166780145857"></a><ul id="ul27166780145857"><li>0: unfinished</li><li>1: terminated due to an execution error</li><li>2: executed successfully</li><li>3: canceled</li></ul>
</td>
</tr>
<tr id="row4584195819116"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p2221115219116"><a name="p2221115219116"></a><a name="p2221115219116"></a>hive_script_path</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p3402997419116"><a name="p3402997419116"></a><a name="p3402997419116"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p496448119116"><a name="p496448119116"></a><a name="p496448119116"></a>Address of the Hive script</p>
</td>
</tr>
<tr id="row7998612191113"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p43907848191113"><a name="p43907848191113"></a><a name="p43907848191113"></a>create_by</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p48146760191113"><a name="p48146760191113"></a><a name="p48146760191113"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p7573477191113"><a name="p7573477191113"></a><a name="p7573477191113"></a>User ID for creating jobs</p>
</td>
</tr>
<tr id="row46507344191132"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p8998499191132"><a name="p8998499191132"></a><a name="p8998499191132"></a>finished_step</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p50461418191132"><a name="p50461418191132"></a><a name="p50461418191132"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p60843054191132"><a name="p60843054191132"></a><a name="p60843054191132"></a>Number of completed steps</p>
</td>
</tr>
<tr id="row63007578191145"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p3340165191145"><a name="p3340165191145"></a><a name="p3340165191145"></a>job_main_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p4495656219439"><a name="p4495656219439"></a><a name="p4495656219439"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1759059320856"><a name="p1759059320856"></a><a name="p1759059320856"></a>Main ID of a job</p>
</td>
</tr>
<tr id="row10088168191225"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p11835266191225"><a name="p11835266191225"></a><a name="p11835266191225"></a>job_step_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p1667749119439"><a name="p1667749119439"></a><a name="p1667749119439"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1438564520856"><a name="p1438564520856"></a><a name="p1438564520856"></a>Step ID of a job</p>
</td>
</tr>
<tr id="row54963709191240"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p22875416191240"><a name="p22875416191240"></a><a name="p22875416191240"></a>postpone_at</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p30188072191240"><a name="p30188072191240"></a><a name="p30188072191240"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p4057938120917"><a name="p4057938120917"></a><a name="p4057938120917"></a>Delay time, which is a 13-bit timestamp.</p>
</td>
</tr>
<tr id="row20295505191252"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p33323170191252"><a name="p33323170191252"></a><a name="p33323170191252"></a>step_name</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p59751102191252"><a name="p59751102191252"></a><a name="p59751102191252"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p8001113191252"><a name="p8001113191252"></a><a name="p8001113191252"></a>Step name of a job</p>
</td>
</tr>
<tr id="row31355889191259"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p56799042191259"><a name="p56799042191259"></a><a name="p56799042191259"></a>step_num</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p2995550191259"><a name="p2995550191259"></a><a name="p2995550191259"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p51527704201027"><a name="p51527704201027"></a><a name="p51527704201027"></a>Number of steps</p>
</td>
</tr>
<tr id="row3898483219138"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p365478919138"><a name="p365478919138"></a><a name="p365478919138"></a>task_num</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p2120762919138"><a name="p2120762919138"></a><a name="p2120762919138"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p34076263201027"><a name="p34076263201027"></a><a name="p34076263201027"></a>Number of tasks</p>
</td>
</tr>
<tr id="row16929053191331"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p29076056191331"><a name="p29076056191331"></a><a name="p29076056191331"></a>update_by</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p44613171191331"><a name="p44613171191331"></a><a name="p44613171191331"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p56897059191331"><a name="p56897059191331"></a><a name="p56897059191331"></a>User ID for updating jobs</p>
</td>
</tr>
<tr id="row60220269191339"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p46003592191339"><a name="p46003592191339"></a><a name="p46003592191339"></a>spend_time</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p41009304191339"><a name="p41009304191339"></a><a name="p41009304191339"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p33419357191339"><a name="p33419357191339"></a><a name="p33419357191339"></a>Duration of job execution (unit: s)</p>
</td>
</tr>
<tr id="row25391145191345"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p43416868191345"><a name="p43416868191345"></a><a name="p43416868191345"></a>step_seq</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p48053375191345"><a name="p48053375191345"></a><a name="p48053375191345"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p9263191345"><a name="p9263191345"></a><a name="p9263191345"></a>Step sequence of a job</p>
</td>
</tr>
<tr id="row12938423191358"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p41379368191358"><a name="p41379368191358"></a><a name="p41379368191358"></a>progress</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p34684936191358"><a name="p34684936191358"></a><a name="p34684936191358"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p58016455191358"><a name="p58016455191358"></a><a name="p58016455191358"></a>Job execution progress</p>
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
        "job_execution": {
            "id": "632863d5-15d4-4691-9dc1-1a72340cb097", 
            "create_at": 1484240559176, 
            "update_at": 1484240559176, 
            "tenant_id": "3f99e3319a8943ceb15c584f3325d064", 
            "job_id": "632863d5-15d4-4691-9dc1-1a72340cb097", 
            "job_name": "hive_script", 
            "start_time": 1484240559176, 
            "end_time": null, 
            "cluster_id": "8b1d55f6-150e-45e2-8347-b2ca608d366b", 
            "group_id": "632863d5-15d4-4691-9dc1-1a72340cb097", 
            "jar_path": "s3a://jp-test1/program/Hivescript.sql", 
            "input": "s3a://jp-test1/input/", 
            "output": "s3a://jp-test1/output/", 
            "job_log": "s3a://jp-test1/joblogs/", 
            "job_type": 3, 
            "file_action": "", 
            "arguments": "wordcount", 
            "hql": null, 
            "job_state": 3, 
            "job_final_status": 1, 
            "hive_script_path": "s3a://jp-test1/program/Hivescript.sql", 
            "create_by": "3f99e3319a8943ceb15c584f3325d064", 
            "finished_step": 0, 
            "job_main_id": "", 
            "job_step_id": "", 
            "postpone_at": 1484240558705, 
            "step_name": "", 
            "step_num": 0, 
            "task_num": 0, 
            "update_by": "3f99e3319a8943ceb15c584f3325d064", 
            "spend_time": null, 
            "step_seq": 222, 
            "progress": "first progress"
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
<tbody><tr id="row3719767816050"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p27524314194358"><a name="p27524314194358"></a><a name="p27524314194358"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p1477641194358"><a name="p1477641194358"></a><a name="p1477641194358"></a>The exe object details are queried successfully.</p>
</td>
</tr>
</tbody>
</table>

For the description about error status codes, see  [Status Codes](status-codes.md).
