# Querying the Job Execution Object List<a name="EN-US_TOPIC_0172486209"></a>

## Function<a name="section5957478711297"></a>

This API is used to query the job execution object list. This API is compatible with Sahara.

## URI<a name="section9153250112933"></a>

-   Format

    GET /v1.1/\{project\_id\}/job-executions

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
    <p id="p8947859145519"><a name="p8947859145519"></a><a name="p8947859145519"></a>Value range: 1 to 1073741822</p>
    </td>
    </tr>
    <tr id="row6317415154849"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p41948639154849"><a name="p41948639154849"></a><a name="p41948639154849"></a>marker</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p42396583154849"><a name="p42396583154849"></a><a name="p42396583154849"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p12118708114324"><a name="p12118708114324"></a><a name="p12118708114324"></a>Job execution ID</p>
    <p id="p11571175154849"><a name="p11571175154849"></a><a name="p11571175154849"></a>Query the job execution list, and select one job execution ID as the marker. The ID is the ID of the last element in the list that will not be returned.</p>
    </td>
    </tr>
    <tr id="row25723845154843"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p3256680154843"><a name="p3256680154843"></a><a name="p3256680154843"></a>sort_by</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p62464499154843"><a name="p62464499154843"></a><a name="p62464499154843"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p47087808163520"><a name="p47087808163520"></a><a name="p47087808163520"></a>Sort field</p>
    <p id="p9590173213183"><a name="p9590173213183"></a><a name="p9590173213183"></a>A hyphen (-) before the sort field indicates to sort in descending order. Example:</p>
    <a name="ul5167941115195"></a><a name="ul5167941115195"></a><ul id="ul5167941115195"><li><strong id="b4347331193"><a name="b4347331193"></a><a name="b4347331193"></a>sort_by=name</strong> indicates to sort by name in ascending order.</li><li><strong id="b41191397198"><a name="b41191397198"></a><a name="b41191397198"></a>sort_by=-name</strong> indicates to sort by name in descending order.</li></ul>
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
<tbody><tr id="row6726034151222"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p42188054143821"><a name="p42188054143821"></a><a name="p42188054143821"></a>markers</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p25690466143952"><a name="p25690466143952"></a><a name="p25690466143952"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1424522572116"><a name="p1424522572116"></a><a name="p1424522572116"></a>Markers object</p>
<p id="p235089014404"><a name="p235089014404"></a><a name="p235089014404"></a>For details, see <a href="#table2264538214423">Table 3</a>.</p>
</td>
</tr>
<tr id="row5091669215512"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p3061139715512"><a name="p3061139715512"></a><a name="p3061139715512"></a>job_executions</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p5165802415512"><a name="p5165802415512"></a><a name="p5165802415512"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p17695163532112"><a name="p17695163532112"></a><a name="p17695163532112"></a>Job execution list</p>
<p id="p2355044315512"><a name="p2355044315512"></a><a name="p2355044315512"></a>For details, see <a href="#table2078214316114">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **markers**  parameter description

<a name="table2264538214423"></a>
<table><thead align="left"><tr id="row5998915014423"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p2728294714423"><a name="p2728294714423"></a><a name="p2728294714423"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="p2407642714423"><a name="p2407642714423"></a><a name="p2407642714423"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p403353314423"><a name="p403353314423"></a><a name="p403353314423"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row5828077214423"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p39683998144350"><a name="p39683998144350"></a><a name="p39683998144350"></a>prev</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p1249717914444"><a name="p1249717914444"></a><a name="p1249717914444"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p21181964144411"><a name="p21181964144411"></a><a name="p21181964144411"></a>Marker on the previous page</p>
</td>
</tr>
<tr id="row6471085014423"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p5714535144350"><a name="p5714535144350"></a><a name="p5714535144350"></a>next</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p5074755814444"><a name="p5074755814444"></a><a name="p5074755814444"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p6613652144411"><a name="p6613652144411"></a><a name="p6613652144411"></a>Marker on the next page</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **job\_executions**  parameter description

<a name="table2078214316114"></a>
<table><thead align="left"><tr id="row4842045416114"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p2974270116114"><a name="p2974270116114"></a><a name="p2974270116114"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="p5639618816114"><a name="p5639618816114"></a><a name="p5639618816114"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p468853316114"><a name="p468853316114"></a><a name="p468853316114"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row2404826816114"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p175270616114"><a name="p175270616114"></a><a name="p175270616114"></a>job_configs</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p2389212716114"><a name="p2389212716114"></a><a name="p2389212716114"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p5621416716114"><a name="p5621416716114"></a><a name="p5621416716114"></a>Key-value pair set for saving job running configurations For more parameter description, see <a href="#table30347504144155">Table 5</a>.</p>
</td>
</tr>
<tr id="row3616545716114"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p4372092016114"><a name="p4372092016114"></a><a name="p4372092016114"></a>is_protected</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p2967693216114"><a name="p2967693216114"></a><a name="p2967693216114"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p5502130516114"><a name="p5502130516114"></a><a name="p5502130516114"></a>Whether a job execution object is protected</p>
<a name="ul3813621916311"></a><a name="ul3813621916311"></a><ul id="ul3813621916311"><li>true</li><li>false</li></ul>
<p id="p1823422916311"><a name="p1823422916311"></a><a name="p1823422916311"></a>The current version does not support this function.</p>
</td>
</tr>
<tr id="row2542969916114"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p4653976616114"><a name="p4653976616114"></a><a name="p4653976616114"></a>input_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p207507616114"><a name="p207507616114"></a><a name="p207507616114"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p3386347216114"><a name="p3386347216114"></a><a name="p3386347216114"></a>Input data source ID of a job execution object</p>
</td>
</tr>
<tr id="row3633579616114"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p5751833116114"><a name="p5751833116114"></a><a name="p5751833116114"></a>job_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p2463235216114"><a name="p2463235216114"></a><a name="p2463235216114"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p4906350116114"><a name="p4906350116114"></a><a name="p4906350116114"></a>Job ID</p>
</td>
</tr>
<tr id="row3891833116114"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p6537710616114"><a name="p6537710616114"></a><a name="p6537710616114"></a>cluster_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p4644521716114"><a name="p4644521716114"></a><a name="p4644521716114"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p396625016114"><a name="p396625016114"></a><a name="p396625016114"></a>Cluster ID</p>
</td>
</tr>
<tr id="row3569625116114"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p571517916114"><a name="p571517916114"></a><a name="p571517916114"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p5054434416114"><a name="p5054434416114"></a><a name="p5054434416114"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p45123816114"><a name="p45123816114"></a><a name="p45123816114"></a>Job execution object creation time</p>
</td>
</tr>
<tr id="row406114716114"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p6051750316114"><a name="p6051750316114"></a><a name="p6051750316114"></a>end_time</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p3929807916114"><a name="p3929807916114"></a><a name="p3929807916114"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p2902782016114"><a name="p2902782016114"></a><a name="p2902782016114"></a>Job end time</p>
</td>
</tr>
<tr id="row5992379016114"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p2198881516114"><a name="p2198881516114"></a><a name="p2198881516114"></a>output_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p5166690116114"><a name="p5166690116114"></a><a name="p5166690116114"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p2426948416114"><a name="p2426948416114"></a><a name="p2426948416114"></a>Output data source ID of a job execution object</p>
</td>
</tr>
<tr id="row1709876416114"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p4282262816114"><a name="p4282262816114"></a><a name="p4282262816114"></a>is_public</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p4155894916114"><a name="p4155894916114"></a><a name="p4155894916114"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1083171016114"><a name="p1083171016114"></a><a name="p1083171016114"></a>Whether a job execution object is public</p>
<a name="ul3872134516111"></a><a name="ul3872134516111"></a><ul id="ul3872134516111"><li>true</li><li>false</li></ul>
<p id="p4213768316111"><a name="p4213768316111"></a><a name="p4213768316111"></a>The current version does not support this function.</p>
</td>
</tr>
<tr id="row3037653416114"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p4458017516114"><a name="p4458017516114"></a><a name="p4458017516114"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p3010195116114"><a name="p3010195116114"></a><a name="p3010195116114"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p2233894916114"><a name="p2233894916114"></a><a name="p2233894916114"></a>Job execution object update time</p>
</td>
</tr>
<tr id="row6683282116114"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p4474941716114"><a name="p4474941716114"></a><a name="p4474941716114"></a>return_code</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p6675945216114"><a name="p6675945216114"></a><a name="p6675945216114"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p3880650616114"><a name="p3880650616114"></a><a name="p3880650616114"></a>Response code after job execution</p>
</td>
</tr>
<tr id="row1371423416114"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p3711118816114"><a name="p3711118816114"></a><a name="p3711118816114"></a>data_source_urls</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p1554834916114"><a name="p1554834916114"></a><a name="p1554834916114"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p5145673216114"><a name="p5145673216114"></a><a name="p5145673216114"></a>Data source URL of a job execution object</p>
</td>
</tr>
<tr id="row6045740716114"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p6521176816114"><a name="p6521176816114"></a><a name="p6521176816114"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p3540196316114"><a name="p3540196316114"></a><a name="p3540196316114"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p78213424110"><a name="p78213424110"></a><a name="p78213424110"></a>Project ID. For details on how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
</td>
</tr>
<tr id="row3822749116114"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p941907716114"><a name="p941907716114"></a><a name="p941907716114"></a>start_time</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p5841445516114"><a name="p5841445516114"></a><a name="p5841445516114"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p3395042316114"><a name="p3395042316114"></a><a name="p3395042316114"></a>Job start time</p>
</td>
</tr>
<tr id="row3711835316114"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p5379659816114"><a name="p5379659816114"></a><a name="p5379659816114"></a>Id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p3396812216114"><a name="p3396812216114"></a><a name="p3396812216114"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p6706340116114"><a name="p6706340116114"></a><a name="p6706340116114"></a>Job execution object ID</p>
</td>
</tr>
<tr id="row4703004611458"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p5133741611458"><a name="p5133741611458"></a><a name="p5133741611458"></a>engine_job_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p540340611458"><a name="p540340611458"></a><a name="p540340611458"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p3502271311458"><a name="p3502271311458"></a><a name="p3502271311458"></a>Workflow ID of Oozie</p>
</td>
</tr>
<tr id="row6669970516114"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p3396698716114"><a name="p3396698716114"></a><a name="p3396698716114"></a>oozie_job_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p5597775016114"><a name="p5597775016114"></a><a name="p5597775016114"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p3790390216114"><a name="p3790390216114"></a><a name="p3790390216114"></a>Workflow ID returned by Oozie</p>
</td>
</tr>
<tr id="row559080316114"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p5020193316114"><a name="p5020193316114"></a><a name="p5020193316114"></a>info</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p458334716114"><a name="p458334716114"></a><a name="p458334716114"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p3570679816114"><a name="p3570679816114"></a><a name="p3570679816114"></a>Key-value pair set, containing job running information returned by Oozie</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **job\_configs**  parameter description

<a name="table30347504144155"></a>
<table><thead align="left"><tr id="row33053434144155"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p60082496144155"><a name="p60082496144155"></a><a name="p60082496144155"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="p3789952144155"><a name="p3789952144155"></a><a name="p3789952144155"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p38550732144155"><a name="p38550732144155"></a><a name="p38550732144155"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row35601555144155"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p24055588144213"><a name="p24055588144213"></a><a name="p24055588144213"></a>configs</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p6237746314436"><a name="p6237746314436"></a><a name="p6237746314436"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p7464973144313"><a name="p7464973144313"></a><a name="p7464973144313"></a>Key-value pair set configured for a job</p>
</td>
</tr>
<tr id="row63553962144155"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p21110331144213"><a name="p21110331144213"></a><a name="p21110331144213"></a>args</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p4046961114436"><a name="p4046961114436"></a><a name="p4046961114436"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p6148040144313"><a name="p6148040144313"></a><a name="p6148040144313"></a>List of arguments</p>
</td>
</tr>
<tr id="row9454595144155"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p21501934144213"><a name="p21501934144213"></a><a name="p21501934144213"></a>params</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p4155571614436"><a name="p4155571614436"></a><a name="p4155571614436"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p52736604144313"><a name="p52736604144313"></a><a name="p52736604144313"></a>Key-value pair set for running a job</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section1210015461189"></a>

-   Example request

    ```
    GET /v1.1/{project_id}/job-executions?limit=2&sort_by=id&marker=839244be-c471-469b-80c0-6f63e376bcbc
    ```

-   Example response

    ```
    {
        "markers": {
            "prev": "821c8924-5249-4dd8-8069-b8d425f3f54a",
            "next": null
        },
        "job_executions": [
            {
                "created_at": "2017-06-22T06:24:57",
                "updated_at": "2017-06-22T06:24:59",
                "id": "84900772-8807-4ddc-9484-f719fa43711f",
                "tenant_id": "5a3314075bfa49b9ae360f4ecd333695",
                "job_id": "",
                "start_time": "2017-06-22T06:24:49",
                "end_time": "2017-06-22T06:25:02",
                "cluster_id": "33dff020-7f96-4270-9c3a-88b99627f6e2",
                "oozie_job_id": null,
                "return_code": null,
                "input_id": null,
                "output_id": null,
                "is_protected": null,
                "is_public": null,
                "engine_job_id": null,
                "job_configs": null,
                "data_source_urls": null,
                "info": null
            },
            {
                "created_at": "2017-06-22T06:23:51",
                "updated_at": "2017-06-22T06:23:51",
                "id": "852042ea-a32c-424b-aacf-df2e6d6642b5",
                "tenant_id": "5a3314075bfa49b9ae360f4ecd333695",
                "job_id": "",
                "start_time": "2017-06-22T06:23:51",
                "end_time": null,
                "cluster_id": "33dff020-7f96-4270-9c3a-88b99627f6e2",
                "oozie_job_id": null,
                "return_code": null,
                "input_id": null,
                "output_id": null,
                "is_protected": null,
                "is_public": null,
                "engine_job_id": null,
                "job_configs": null,
                "data_source_urls": null,
                "info": null
            }
        ]
    }
    ```


## Status Code<a name="section25088328113020"></a>

[Table 6](#table1584477916050)  describes the status code of this API.

**Table  6**  Status code

<a name="table1584477916050"></a>
<table><thead align="left"><tr id="row1339492016050"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.3.1.1"><p id="p3411176516050"><a name="p3411176516050"></a><a name="p3411176516050"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.2.3.1.2"><p id="p1158961516050"><a name="p1158961516050"></a><a name="p1158961516050"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3719767816050"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p6022194016050"><a name="p6022194016050"></a><a name="p6022194016050"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p4613894216050"><a name="p4613894216050"></a><a name="p4613894216050"></a>The job execution object list is queried successfully.</p>
</td>
</tr>
</tbody>
</table>

For the description about error status codes, see  [Status Codes](status-codes.md).

