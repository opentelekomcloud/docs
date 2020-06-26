# Querying a List of Jobs<a name="EN-US_TOPIC_0177065249"></a>

## Function<a name="section4408504619327"></a>

This API is used to query the job list in an MRS cluster.

## URI<a name="section10186656193217"></a>

-   Format

    GET /v2/\{project\_id\}/clusters/\{cluster\_id\}/job-executions

-   Parameter description

    **Table  1**  URI parameter description

    <a name="table49499141194754"></a>
    <table><thead align="left"><tr id="en-us_topic_0176713997_row33700024194754"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="en-us_topic_0176713997_p16571835194812"><a name="en-us_topic_0176713997_p16571835194812"></a><a name="en-us_topic_0176713997_p16571835194812"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="en-us_topic_0176713997_p141410194812"><a name="en-us_topic_0176713997_p141410194812"></a><a name="en-us_topic_0176713997_p141410194812"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="en-us_topic_0176713997_p11454278194812"><a name="en-us_topic_0176713997_p11454278194812"></a><a name="en-us_topic_0176713997_p11454278194812"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0176713997_row39786771142917"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0176713997_p1503055142917"><a name="en-us_topic_0176713997_p1503055142917"></a><a name="en-us_topic_0176713997_p1503055142917"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0176713997_p54638598142917"><a name="en-us_topic_0176713997_p54638598142917"></a><a name="en-us_topic_0176713997_p54638598142917"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0176713997_p63650338142917"><a name="en-us_topic_0176713997_p63650338142917"></a><a name="en-us_topic_0176713997_p63650338142917"></a>Project ID. For details on how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0176713997_row3457216201210"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0176713997_p194589160122"><a name="en-us_topic_0176713997_p194589160122"></a><a name="en-us_topic_0176713997_p194589160122"></a>cluster_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0176713997_p045813165125"><a name="en-us_topic_0176713997_p045813165125"></a><a name="en-us_topic_0176713997_p045813165125"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0176713997_p1845891641218"><a name="en-us_topic_0176713997_p1845891641218"></a><a name="en-us_topic_0176713997_p1845891641218"></a>Cluster ID. For details on how to obtain the cluster ID, see <a href="obtain-mrs-cluster-information.md#section177891315153619">Obtaining a Cluster ID</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section673761354213"></a>

**Table  2**  Request parameter description

<a name="table46210785193317"></a>
<table><thead align="left"><tr id="row34262165193317"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p12621391193317"><a name="p12621391193317"></a><a name="p12621391193317"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p15699711193317"><a name="p15699711193317"></a><a name="p15699711193317"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p562413019313"><a name="p562413019313"></a><a name="p562413019313"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="p63717051193317"><a name="p63717051193317"></a><a name="p63717051193317"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row123786413298"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p62016791102743"><a name="p62016791102743"></a><a name="p62016791102743"></a>job_name</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p57304145102743"><a name="p57304145102743"></a><a name="p57304145102743"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p277864793547"><a name="p277864793547"></a><a name="p277864793547"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p29070416105535"><a name="p29070416105535"></a><a name="p29070416105535"></a>Job name. It contains 1 to 64 characters. Only letters, digits, hyphens (-), and underscores (_) are allowed.</p>
</td>
</tr>
<tr id="row36582554193317"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p10396884193317"><a name="p10396884193317"></a><a name="p10396884193317"></a>job_type</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p36841295193317"><a name="p36841295193317"></a><a name="p36841295193317"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p346461129313"><a name="p346461129313"></a><a name="p346461129313"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p32476122205057"><a name="p32476122205057"></a><a name="p32476122205057"></a>Type of a job.</p>
<a name="ul5947149515590"></a><a name="ul5947149515590"></a><ul id="ul5947149515590"><li>MapReduce</li><li>SparkSubmit</li><li>HiveScript</li><li>HiveSql</li><li>DistCp, importing and exporting data</li><li>SparkScript</li><li>SparkSql</li><li>Flink</li></ul>
</td>
</tr>
<tr id="row57932449102743"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p651819462374"><a name="p651819462374"></a><a name="p651819462374"></a>job_state</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p62009911389"><a name="p62009911389"></a><a name="p62009911389"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p55181346153710"><a name="p55181346153710"></a><a name="p55181346153710"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p19518746103716"><a name="p19518746103716"></a><a name="p19518746103716"></a>Execution status of a job.</p>
<a name="ul78901461383"></a><a name="ul78901461383"></a><ul id="ul78901461383"><li><strong id="b595914457375"><a name="b595914457375"></a><a name="b595914457375"></a>FAILED</strong>: indicates that the job fails to be executed.</li><li><strong id="b16527105443719"><a name="b16527105443719"></a><a name="b16527105443719"></a>KILLED</strong>: indicates that the job is terminated.</li><li><strong id="b164941157183711"><a name="b164941157183711"></a><a name="b164941157183711"></a>New</strong>: indicates that the job is created.</li><li><strong id="b9727551382"><a name="b9727551382"></a><a name="b9727551382"></a>NEW_SAVING</strong>: indicates that the job has been created and is being saved.</li><li><strong id="b12002317395"><a name="b12002317395"></a><a name="b12002317395"></a>SUBMITTED</strong>: indicates that the job is submitted.</li><li><strong id="b171161926113914"><a name="b171161926113914"></a><a name="b171161926113914"></a>ACCEPTED</strong>: indicates that the job is accepted.</li><li><strong id="b132630124316"><a name="b132630124316"></a><a name="b132630124316"></a>RUNNING</strong>: indicates that the job is running.</li><li><strong id="b510618694011"><a name="b510618694011"></a><a name="b510618694011"></a>FINISHED</strong>: indicates that the job is completed.</li></ul>
</td>
</tr>
<tr id="row029134321010"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p129174314106"><a name="p129174314106"></a><a name="p129174314106"></a>job_result</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p1829116436102"><a name="p1829116436102"></a><a name="p1829116436102"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p1829117436101"><a name="p1829117436101"></a><a name="p1829117436101"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p611416781112"><a name="p611416781112"></a><a name="p611416781112"></a>Execution result of a job.</p>
<a name="ul375917235111"></a><a name="ul375917235111"></a><ul id="ul375917235111"><li><strong id="b5962144484014"><a name="b5962144484014"></a><a name="b5962144484014"></a>FAILED</strong>: indicates that the job fails to be executed.</li><li><strong id="b220555515416"><a name="b220555515416"></a><a name="b220555515416"></a>KILLED</strong>: indicates that the job is manually terminated during execution.</li><li><strong id="b15303108425"><a name="b15303108425"></a><a name="b15303108425"></a>UNDEFINED</strong>: indicates that the job is being executed.</li><li><strong id="b5686110134310"><a name="b5686110134310"></a><a name="b5686110134310"></a>SUCCEEDED</strong>: indicates that the job has been successfully executed.</li></ul>
</td>
</tr>
<tr id="row430511374254"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p9518946143713"><a name="p9518946143713"></a><a name="p9518946143713"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p1655671116384"><a name="p1655671116384"></a><a name="p1655671116384"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p351964633713"><a name="p351964633713"></a><a name="p351964633713"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p125191146113712"><a name="p125191146113712"></a><a name="p125191146113712"></a>Number of records displayed on each page in the returned result. The default value is <strong id="b1297328164313"><a name="b1297328164313"></a><a name="b1297328164313"></a>10</strong>.</p>
</td>
</tr>
<tr id="row1688911377259"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p651934617378"><a name="p651934617378"></a><a name="p651934617378"></a>offset</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p299715158386"><a name="p299715158386"></a><a name="p299715158386"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p14519144612377"><a name="p14519144612377"></a><a name="p14519144612377"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p1451934616372"><a name="p1451934616372"></a><a name="p1451934616372"></a>Offset. The default value is <strong id="b84235270615612"><a name="b84235270615612"></a><a name="b84235270615612"></a>1</strong>.</p>
</td>
</tr>
<tr id="row4788257010284"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p17519144620374"><a name="p17519144620374"></a><a name="p17519144620374"></a>sort_by</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p538231823816"><a name="p538231823816"></a><a name="p538231823816"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p16519124612374"><a name="p16519124612374"></a><a name="p16519124612374"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p175272884110"><a name="p175272884110"></a><a name="p175272884110"></a>Ranking mode of returned results. The default value is <strong id="b10131195717437"><a name="b10131195717437"></a><a name="b10131195717437"></a>desc</strong>.</p>
<a name="ul74481310134119"></a><a name="ul74481310134119"></a><ul id="ul74481310134119"><li><strong id="b27942384416"><a name="b27942384416"></a><a name="b27942384416"></a>asc</strong>: indicates that the returned results are ranked in ascending order.</li><li><strong id="b3258634104416"><a name="b3258634104416"></a><a name="b3258634104416"></a>desc</strong>: indicates that the returned results are ranked in descending order.</li></ul>
</td>
</tr>
<tr id="row57271515193014"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p86221430133318"><a name="p86221430133318"></a><a name="p86221430133318"></a>submitted_time_begin</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p19601820113812"><a name="p19601820113812"></a><a name="p19601820113812"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p651914467376"><a name="p651914467376"></a><a name="p651914467376"></a>TimeStamp</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p051994616375"><a name="p051994616375"></a><a name="p051994616375"></a>UTC timestamp after which a job is submitted, in milliseconds. For example, 1562032041362.</p>
</td>
</tr>
<tr id="row22945661205631"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p8622830113313"><a name="p8622830113313"></a><a name="p8622830113313"></a>submitted_time_end</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p3207122223815"><a name="p3207122223815"></a><a name="p3207122223815"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p151954693715"><a name="p151954693715"></a><a name="p151954693715"></a>TimeStamp</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p5519346193718"><a name="p5519346193718"></a><a name="p5519346193718"></a>UTC timestamp before which a job is submitted, in milliseconds. For example, 1562032041362.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section775516131425"></a>

**Table  3**  Response parameter description

<a name="table12040613193927"></a>
<table><thead align="left"><tr id="row8843854193927"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p45263556193927"><a name="p45263556193927"></a><a name="p45263556193927"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="p1907984993927"><a name="p1907984993927"></a><a name="p1907984993927"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p17473879193927"><a name="p17473879193927"></a><a name="p17473879193927"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row8387056194027"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p14121183010424"><a name="p14121183010424"></a><a name="p14121183010424"></a>total_record</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p1812143074216"><a name="p1812143074216"></a><a name="p1812143074216"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p112123064210"><a name="p112123064210"></a><a name="p112123064210"></a>Total number of jobs</p>
</td>
</tr>
<tr id="row19100834201113"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1612153074218"><a name="p1612153074218"></a><a name="p1612153074218"></a>job_list</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p121445122811"><a name="p121445122811"></a><a name="p121445122811"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p14121203094215"><a name="p14121203094215"></a><a name="p14121203094215"></a>Job list. For details about the parameter, see <a href="#table9145123857">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  Job parameter description

<a name="table9145123857"></a>
<table><thead align="left"><tr id="en-us_topic_0176790808_row8843854193927"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="en-us_topic_0176790808_p45263556193927"><a name="en-us_topic_0176790808_p45263556193927"></a><a name="en-us_topic_0176790808_p45263556193927"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="en-us_topic_0176790808_p1907984993927"><a name="en-us_topic_0176790808_p1907984993927"></a><a name="en-us_topic_0176790808_p1907984993927"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="en-us_topic_0176790808_p17473879193927"><a name="en-us_topic_0176790808_p17473879193927"></a><a name="en-us_topic_0176790808_p17473879193927"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0176790808_row8387056194027"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0176790808_p52943541117"><a name="en-us_topic_0176790808_p52943541117"></a><a name="en-us_topic_0176790808_p52943541117"></a>job_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0176790808_p12125168101212"><a name="en-us_topic_0176790808_p12125168101212"></a><a name="en-us_topic_0176790808_p12125168101212"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0176790808_p6329191671215"><a name="en-us_topic_0176790808_p6329191671215"></a><a name="en-us_topic_0176790808_p6329191671215"></a>Job ID.</p>
</td>
</tr>
<tr id="en-us_topic_0176790808_row19100834201113"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0176790808_p1029418549112"><a name="en-us_topic_0176790808_p1029418549112"></a><a name="en-us_topic_0176790808_p1029418549112"></a>user</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0176790808_p512508201214"><a name="en-us_topic_0176790808_p512508201214"></a><a name="en-us_topic_0176790808_p512508201214"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0176790808_p183294166123"><a name="en-us_topic_0176790808_p183294166123"></a><a name="en-us_topic_0176790808_p183294166123"></a>Name of the user who submits a job.</p>
</td>
</tr>
<tr id="en-us_topic_0176790808_row1850318495114"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0176790808_p12294125416119"><a name="en-us_topic_0176790808_p12294125416119"></a><a name="en-us_topic_0176790808_p12294125416119"></a>job_name</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0176790808_p191251789127"><a name="en-us_topic_0176790808_p191251789127"></a><a name="en-us_topic_0176790808_p191251789127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0176790808_p153291516111218"><a name="en-us_topic_0176790808_p153291516111218"></a><a name="en-us_topic_0176790808_p153291516111218"></a>Job name. It contains 1 to 64 characters. Only letters, digits, hyphens (-), and underscores (_) are allowed.</p>
</td>
</tr>
<tr id="en-us_topic_0176790808_row1910618551609"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0176790808_p1341817597018"><a name="en-us_topic_0176790808_p1341817597018"></a><a name="en-us_topic_0176790808_p1341817597018"></a>job_result</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0176790808_p12418185915018"><a name="en-us_topic_0176790808_p12418185915018"></a><a name="en-us_topic_0176790808_p12418185915018"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0176790808_p741885912014"><a name="en-us_topic_0176790808_p741885912014"></a><a name="en-us_topic_0176790808_p741885912014"></a>Final result of a job.</p>
<a name="en-us_topic_0176790808_ul141131420762"></a><a name="en-us_topic_0176790808_ul141131420762"></a><ul id="en-us_topic_0176790808_ul141131420762"><li><strong id="en-us_topic_0176790808_en-us_topic_0177065249_b5962144484014"><a name="en-us_topic_0176790808_en-us_topic_0177065249_b5962144484014"></a><a name="en-us_topic_0176790808_en-us_topic_0177065249_b5962144484014"></a>FAILED</strong>: indicates that the job fails to be executed.</li><li><strong id="en-us_topic_0176790808_en-us_topic_0177065249_b220555515416"><a name="en-us_topic_0176790808_en-us_topic_0177065249_b220555515416"></a><a name="en-us_topic_0176790808_en-us_topic_0177065249_b220555515416"></a>KILLED</strong>: indicates that the job is manually terminated during execution.</li><li><strong id="en-us_topic_0176790808_en-us_topic_0177065249_b15303108425"><a name="en-us_topic_0176790808_en-us_topic_0177065249_b15303108425"></a><a name="en-us_topic_0176790808_en-us_topic_0177065249_b15303108425"></a>UNDEFINED</strong>: indicates that the job is being executed.</li><li><strong id="en-us_topic_0176790808_en-us_topic_0177065249_b5686110134310"><a name="en-us_topic_0176790808_en-us_topic_0177065249_b5686110134310"></a><a name="en-us_topic_0176790808_en-us_topic_0177065249_b5686110134310"></a>SUCCEEDED</strong>: indicates that the job has been successfully executed.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0176790808_row128711949131111"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0176790808_p16294105413112"><a name="en-us_topic_0176790808_p16294105413112"></a><a name="en-us_topic_0176790808_p16294105413112"></a>job_state</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0176790808_p11261885121"><a name="en-us_topic_0176790808_p11261885121"></a><a name="en-us_topic_0176790808_p11261885121"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0176790808_p232941614125"><a name="en-us_topic_0176790808_p232941614125"></a><a name="en-us_topic_0176790808_p232941614125"></a>Execution status of a job.</p>
<a name="en-us_topic_0176790808_ul83814473515"></a><a name="en-us_topic_0176790808_ul83814473515"></a><ul id="en-us_topic_0176790808_ul83814473515"><li><strong id="en-us_topic_0176790808_en-us_topic_0177065249_b595914457375"><a name="en-us_topic_0176790808_en-us_topic_0177065249_b595914457375"></a><a name="en-us_topic_0176790808_en-us_topic_0177065249_b595914457375"></a>FAILED</strong>: indicates that the job fails to be executed.</li><li><strong id="en-us_topic_0176790808_en-us_topic_0177065249_b16527105443719"><a name="en-us_topic_0176790808_en-us_topic_0177065249_b16527105443719"></a><a name="en-us_topic_0176790808_en-us_topic_0177065249_b16527105443719"></a>KILLED</strong>: indicates that the job is terminated.</li><li><strong id="en-us_topic_0176790808_en-us_topic_0177065249_b164941157183711"><a name="en-us_topic_0176790808_en-us_topic_0177065249_b164941157183711"></a><a name="en-us_topic_0176790808_en-us_topic_0177065249_b164941157183711"></a>New</strong>: indicates that the job is created.</li><li><strong id="en-us_topic_0176790808_en-us_topic_0177065249_b9727551382"><a name="en-us_topic_0176790808_en-us_topic_0177065249_b9727551382"></a><a name="en-us_topic_0176790808_en-us_topic_0177065249_b9727551382"></a>NEW_SAVING</strong>: indicates that the job has been created and is being saved.</li><li><strong id="en-us_topic_0176790808_en-us_topic_0177065249_b12002317395"><a name="en-us_topic_0176790808_en-us_topic_0177065249_b12002317395"></a><a name="en-us_topic_0176790808_en-us_topic_0177065249_b12002317395"></a>SUBMITTED</strong>: indicates that the job is submitted.</li><li><strong id="en-us_topic_0176790808_en-us_topic_0177065249_b171161926113914"><a name="en-us_topic_0176790808_en-us_topic_0177065249_b171161926113914"></a><a name="en-us_topic_0176790808_en-us_topic_0177065249_b171161926113914"></a>ACCEPTED</strong>: indicates that the job is accepted.</li><li><strong id="en-us_topic_0176790808_en-us_topic_0177065249_b132630124316"><a name="en-us_topic_0176790808_en-us_topic_0177065249_b132630124316"></a><a name="en-us_topic_0176790808_en-us_topic_0177065249_b132630124316"></a>RUNNING</strong>: indicates that the job is running.</li><li><strong id="en-us_topic_0176790808_en-us_topic_0177065249_b510618694011"><a name="en-us_topic_0176790808_en-us_topic_0177065249_b510618694011"></a><a name="en-us_topic_0176790808_en-us_topic_0177065249_b510618694011"></a>FINISHED</strong>: indicates that the job is completed.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0176790808_row11227205011116"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0176790808_p16294105418112"><a name="en-us_topic_0176790808_p16294105418112"></a><a name="en-us_topic_0176790808_p16294105418112"></a>job_progress</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0176790808_p612614821210"><a name="en-us_topic_0176790808_p612614821210"></a><a name="en-us_topic_0176790808_p612614821210"></a>Float</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0176790808_p832915169122"><a name="en-us_topic_0176790808_p832915169122"></a><a name="en-us_topic_0176790808_p832915169122"></a>Job execution progress.</p>
</td>
</tr>
<tr id="en-us_topic_0176790808_row11400175061120"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0176790808_p729415401114"><a name="en-us_topic_0176790808_p729415401114"></a><a name="en-us_topic_0176790808_p729415401114"></a>job_type</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0176790808_p13126198181216"><a name="en-us_topic_0176790808_p13126198181216"></a><a name="en-us_topic_0176790808_p13126198181216"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0176790808_p532941620128"><a name="en-us_topic_0176790808_p532941620128"></a><a name="en-us_topic_0176790808_p532941620128"></a>Type of a job.</p>
<a name="en-us_topic_0176790808_ul58695132184"></a><a name="en-us_topic_0176790808_ul58695132184"></a><ul id="en-us_topic_0176790808_ul58695132184"><li>MapReduce</li><li>SparkSubmit</li><li>HiveScript</li><li>HiveSql</li><li>DistCp, importing and exporting data</li><li>SparkScript</li><li>SparkSql</li><li>Flink</li></ul>
</td>
</tr>
<tr id="en-us_topic_0176790808_row12272193451118"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0176790808_p1629585451114"><a name="en-us_topic_0176790808_p1629585451114"></a><a name="en-us_topic_0176790808_p1629585451114"></a>started_time</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0176790808_p1612698121215"><a name="en-us_topic_0176790808_p1612698121215"></a><a name="en-us_topic_0176790808_p1612698121215"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0176790808_p1433061611218"><a name="en-us_topic_0176790808_p1433061611218"></a><a name="en-us_topic_0176790808_p1433061611218"></a>Start time to run a job. Unit: ms.</p>
</td>
</tr>
<tr id="en-us_topic_0176790808_row139751543313"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0176790808_p169751343516"><a name="en-us_topic_0176790808_p169751343516"></a><a name="en-us_topic_0176790808_p169751343516"></a>submitted_time</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0176790808_p1497516434114"><a name="en-us_topic_0176790808_p1497516434114"></a><a name="en-us_topic_0176790808_p1497516434114"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0176790808_p169754431714"><a name="en-us_topic_0176790808_p169754431714"></a><a name="en-us_topic_0176790808_p169754431714"></a>Time when a job is submitted. Unit: ms.</p>
</td>
</tr>
<tr id="en-us_topic_0176790808_row24471734181115"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0176790808_p13295554131120"><a name="en-us_topic_0176790808_p13295554131120"></a><a name="en-us_topic_0176790808_p13295554131120"></a>finished_time</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0176790808_p1012618817121"><a name="en-us_topic_0176790808_p1012618817121"></a><a name="en-us_topic_0176790808_p1012618817121"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0176790808_p1333011651212"><a name="en-us_topic_0176790808_p1333011651212"></a><a name="en-us_topic_0176790808_p1333011651212"></a>End time to run a job. Unit: ms.</p>
</td>
</tr>
<tr id="en-us_topic_0176790808_row186142034131118"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0176790808_p8295135413112"><a name="en-us_topic_0176790808_p8295135413112"></a><a name="en-us_topic_0176790808_p8295135413112"></a>elapsed_time</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0176790808_p1612617841214"><a name="en-us_topic_0176790808_p1612617841214"></a><a name="en-us_topic_0176790808_p1612617841214"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0176790808_p733061610128"><a name="en-us_topic_0176790808_p733061610128"></a><a name="en-us_topic_0176790808_p733061610128"></a>Running duration of a job. Unit: ms.</p>
</td>
</tr>
<tr id="en-us_topic_0176790808_row6780123481117"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0176790808_p62951654141119"><a name="en-us_topic_0176790808_p62951654141119"></a><a name="en-us_topic_0176790808_p62951654141119"></a>arguments</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0176790808_p51269812128"><a name="en-us_topic_0176790808_p51269812128"></a><a name="en-us_topic_0176790808_p51269812128"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0176790808_p93301716191220"><a name="en-us_topic_0176790808_p93301716191220"></a><a name="en-us_topic_0176790808_p93301716191220"></a>Running parameter. The parameter contains a maximum of 4,096 characters, excluding special characters such as ;|&amp;&gt;'&lt;$, and can be left blank.</p>
</td>
</tr>
<tr id="en-us_topic_0176790808_row4950134131116"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0176790808_p18295154101116"><a name="en-us_topic_0176790808_p18295154101116"></a><a name="en-us_topic_0176790808_p18295154101116"></a>properties</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0176790808_p181261986126"><a name="en-us_topic_0176790808_p181261986126"></a><a name="en-us_topic_0176790808_p181261986126"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0176790808_p1133020163121"><a name="en-us_topic_0176790808_p1133020163121"></a><a name="en-us_topic_0176790808_p1133020163121"></a>Configuration parameter, which is used to configure <strong id="en-us_topic_0176790808_b4449156204014"><a name="en-us_topic_0176790808_b4449156204014"></a><a name="en-us_topic_0176790808_b4449156204014"></a>-d</strong> parameters. The parameter contains a maximum of 2,048 characters, excluding special characters such as &gt;&lt;|'`&amp;!\, and can be left blank.</p>
</td>
</tr>
<tr id="en-us_topic_0176790808_row34573461227"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0176790808_p103136481121"><a name="en-us_topic_0176790808_p103136481121"></a><a name="en-us_topic_0176790808_p103136481121"></a>launcher_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0176790808_p139311522020"><a name="en-us_topic_0176790808_p139311522020"></a><a name="en-us_topic_0176790808_p139311522020"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0176790808_p20244195418212"><a name="en-us_topic_0176790808_p20244195418212"></a><a name="en-us_topic_0176790808_p20244195418212"></a>Launcher job ID</p>
</td>
</tr>
<tr id="en-us_topic_0176790808_row1687919461120"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0176790808_p031334815212"><a name="en-us_topic_0176790808_p031334815212"></a><a name="en-us_topic_0176790808_p031334815212"></a>app_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0176790808_p149310528220"><a name="en-us_topic_0176790808_p149310528220"></a><a name="en-us_topic_0176790808_p149310528220"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0176790808_p1624412541822"><a name="en-us_topic_0176790808_p1624412541822"></a><a name="en-us_topic_0176790808_p1624412541822"></a>Actual job ID.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section1210015461189"></a>

-   Example request

    None

-   Example response
    -   Example of a successful response

        ```
        {
        	"total_record": 2,
        	"job_list": [{
        			"job_id": "981374c1-85da-44ee-be32-edfb4fba776c",
        			"user": "xxxx",
        			"job_name": "SparkSubmitTset",
        			"job_result": "UNDEFINED",
        			"job_state": "ACCEPTED",
        			"job_progress": 0,
        			"job_type": "SparkSubmit",
        			"started_time": 0,
        			"submitted_time": 1564714763119,
        			"finished_time": 0,
        			"elapsed_time": 0,
        			"queue": "default",
        			"arguments": "[--class, --driver-memory, --executor-cores, --master, yarn-cluster, s3a://obs-test/hadoop-mapreduce-examples-3.1.1.jar, dddd]",
        			"launcher_id": "application_1564622673393_0613",
        			"properties": "{}"
        		},
        		{
        			"job_id": "c54c8aa0-c277-4f83-8acc-521d85cfa32b",
        			"user": "xxxx",
        			"job_name": "SparkSubmitTset2",
        			"job_result": "UNDEFINED",
        			"job_state": "ACCEPTED",
        			"job_progress": 0,
        			"job_type": "SparkSubmit",
        			"started_time": 0,
        			"submitted_time": 1564714020099,
        			"finished_time": 0,
        			"elapsed_time": 0,
        			"queue": "default",
        			"arguments": "[--conf, yujjsjhe, --driver-memory, yueujdjjd, --master, yarn-cluster, s3a://obs-test/hadoop-mapreduce-examples-3.1.1.jar]",
        			"launcher_id": "application_1564622673393_0611",
        			"properties": "{}"
        		}
        	]
        }
        ```

    -   Example of a failed response

        ```
        {
        "error_msg": "Failed to query the job list."
        "error_code":"0166"
        }
        ```



## Status Code<a name="section4391766619434"></a>

For details about status codes, see  [Status Codes](status-codes.md).

