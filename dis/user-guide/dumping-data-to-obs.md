# Dumping Data to OBS<a name="dis_01_0078"></a>

## Dumping the JSON, BLOB, and CSV Data to the Text Data<a name="section5760185410392"></a>

**Table  1**  Parameters for configuring a Text dump file

<a name="table18468165816451"></a>
<table><thead align="left"><tr id="row15468165811456"><th class="cellrowborder" valign="top" width="21.08210821082108%" id="mcps1.2.4.1.1"><p id="p1746865813454"><a name="p1746865813454"></a><a name="p1746865813454"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="56.66566656665667%" id="mcps1.2.4.1.2"><p id="p1746811580453"><a name="p1746811580453"></a><a name="p1746811580453"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="22.252225222522252%" id="mcps1.2.4.1.3"><p id="p184682582458"><a name="p184682582458"></a><a name="p184682582458"></a>Value</p>
</th>
</tr>
</thead>
<tbody><tr id="row846805820453"><td class="cellrowborder" valign="top" width="21.08210821082108%" headers="mcps1.2.4.1.1 "><p id="p4468195810455"><a name="p4468195810455"></a><a name="p4468195810455"></a>Task Name</p>
</td>
<td class="cellrowborder" valign="top" width="56.66566656665667%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0120206045_p15371132211357"><a name="en-us_topic_0120206045_p15371132211357"></a><a name="en-us_topic_0120206045_p15371132211357"></a>Name of the dump task. The names of dump tasks created for the same stream must be unique. A dump task name is 1 to 64 characters long. Only letters, digits, hyphens (-), and underscores (_) are allowed.</p>
</td>
<td class="cellrowborder" valign="top" width="22.252225222522252%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0120206045_p9371522113518"><a name="en-us_topic_0120206045_p9371522113518"></a><a name="en-us_topic_0120206045_p9371522113518"></a>-</p>
</td>
</tr>
<tr id="row346865813454"><td class="cellrowborder" valign="top" width="21.08210821082108%" headers="mcps1.2.4.1.1 "><p id="p114692058184513"><a name="p114692058184513"></a><a name="p114692058184513"></a>Dump Bucket</p>
</td>
<td class="cellrowborder" valign="top" width="56.66566656665667%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0120206045_p737182214358"><a name="en-us_topic_0120206045_p737182214358"></a><a name="en-us_topic_0120206045_p737182214358"></a>Name of the OBS bucket used to store data from the DIS stream. The bucket name is created when you create a bucket in OBS.</p>
</td>
<td class="cellrowborder" valign="top" width="22.252225222522252%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0120206045_p93712225357"><a name="en-us_topic_0120206045_p93712225357"></a><a name="en-us_topic_0120206045_p93712225357"></a>-</p>
</td>
</tr>
<tr id="row174699584459"><td class="cellrowborder" valign="top" width="21.08210821082108%" headers="mcps1.2.4.1.1 "><p id="p1046914582454"><a name="p1046914582454"></a><a name="p1046914582454"></a>File Directory</p>
</td>
<td class="cellrowborder" valign="top" width="56.66566656665667%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0120206045_p73711822193518"><a name="en-us_topic_0120206045_p73711822193518"></a><a name="en-us_topic_0120206045_p73711822193518"></a>Directory created in OBS to store files from the DIS stream.</p>
<p id="en-us_topic_0120206045_p203713226352"><a name="en-us_topic_0120206045_p203713226352"></a><a name="en-us_topic_0120206045_p203713226352"></a>This directory name is 0 to 50 characters long.</p>
<p id="en-us_topic_0120206045_p437115221351"><a name="en-us_topic_0120206045_p437115221351"></a><a name="en-us_topic_0120206045_p437115221351"></a>By default, this parameter is left unspecified.</p>
</td>
<td class="cellrowborder" valign="top" width="22.252225222522252%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0120206045_p183712022113519"><a name="en-us_topic_0120206045_p183712022113519"></a><a name="en-us_topic_0120206045_p183712022113519"></a>-</p>
</td>
</tr>
<tr id="row446965814453"><td class="cellrowborder" valign="top" width="21.08210821082108%" headers="mcps1.2.4.1.1 "><p id="p17469058144516"><a name="p17469058144516"></a><a name="p17469058144516"></a>Time Directory Format</p>
</td>
<td class="cellrowborder" valign="top" width="56.66566656665667%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0120206045_p1643163722112"><a name="en-us_topic_0120206045_p1643163722112"></a><a name="en-us_topic_0120206045_p1643163722112"></a>Data will be saved according to the time format in the file directory of the OBS bucket.</p>
<p id="en-us_topic_0120206045_p11371122113511"><a name="en-us_topic_0120206045_p11371122113511"></a><a name="en-us_topic_0120206045_p11371122113511"></a>For example, if the time directory is accurate to day, the save path will be in the format of bucket name/file directory/year/month/day.</p>
<div class="p" id="en-us_topic_0120206045_p103711522163519"><a name="en-us_topic_0120206045_p103711522163519"></a><a name="en-us_topic_0120206045_p103711522163519"></a>Possible values are as follows:<a name="en-us_topic_0120206045_ul33711722133517"></a><a name="en-us_topic_0120206045_ul33711722133517"></a><ul id="en-us_topic_0120206045_ul33711722133517"><li>N/A: If this field is left unspecified, the time directory format will not be used.</li><li>yyyy: year.</li><li>yyyy/MM: year and month.</li><li>yyyy/MM/dd: year, month, and day.</li><li>yyyy/MM/dd/HH: year, month, day, and hour.</li><li>yyyy/MM/dd/HH/mm: year, month, day, hour, and minute.</li></ul>
</div>
<p id="en-us_topic_0120206045_p103719228358"><a name="en-us_topic_0120206045_p103719228358"></a><a name="en-us_topic_0120206045_p103719228358"></a>You can only select but not enter a value in this field.</p>
</td>
<td class="cellrowborder" valign="top" width="22.252225222522252%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0120206045_p1371322123511"><a name="en-us_topic_0120206045_p1371322123511"></a><a name="en-us_topic_0120206045_p1371322123511"></a>-</p>
</td>
</tr>
<tr id="row246955812451"><td class="cellrowborder" valign="top" width="21.08210821082108%" headers="mcps1.2.4.1.1 "><p id="p646917583450"><a name="p646917583450"></a><a name="p646917583450"></a>Record Delimiter</p>
</td>
<td class="cellrowborder" valign="top" width="56.66566656665667%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0120206045_p037115226353"><a name="en-us_topic_0120206045_p037115226353"></a><a name="en-us_topic_0120206045_p037115226353"></a>Delimiter used to separate different dump records.</p>
<div class="p" id="en-us_topic_0120206045_p538714226359"><a name="en-us_topic_0120206045_p538714226359"></a><a name="en-us_topic_0120206045_p538714226359"></a>Possible values are as follows:<a name="en-us_topic_0120206045_ul4387722103510"></a><a name="en-us_topic_0120206045_ul4387722103510"></a><ul id="en-us_topic_0120206045_ul4387722103510"><li>Comma (,)</li><li>Semicolon (;)</li><li>Vertical bar (|)</li><li>Newline (\n)</li><li>NULL</li></ul>
</div>
<p id="en-us_topic_0120206045_p103874223358"><a name="en-us_topic_0120206045_p103874223358"></a><a name="en-us_topic_0120206045_p103874223358"></a>You can only select but not enter a value in this field.</p>
</td>
<td class="cellrowborder" valign="top" width="22.252225222522252%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0120206045_p43872227359"><a name="en-us_topic_0120206045_p43872227359"></a><a name="en-us_topic_0120206045_p43872227359"></a>-</p>
</td>
</tr>
<tr id="row154692588456"><td class="cellrowborder" valign="top" width="21.08210821082108%" headers="mcps1.2.4.1.1 "><p id="p846916586453"><a name="p846916586453"></a><a name="p846916586453"></a>Offset</p>
</td>
<td class="cellrowborder" valign="top" width="56.66566656665667%" headers="mcps1.2.4.1.2 "><a name="en-us_topic_0120206045_ul19387202217353"></a><a name="en-us_topic_0120206045_ul19387202217353"></a><ul id="en-us_topic_0120206045_ul19387202217353"><li><strong id="b84235270616244"><a name="b84235270616244"></a><a name="b84235270616244"></a>Latest</strong>: Maximum offset, indicating that the latest data will be read.</li><li><strong id="b842352706162735"><a name="b842352706162735"></a><a name="b842352706162735"></a>Earliest</strong>: Minimum offset, indicating that the earliest data will be read.</li></ul>
</td>
<td class="cellrowborder" valign="top" width="22.252225222522252%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0120206045_p1838772218354"><a name="en-us_topic_0120206045_p1838772218354"></a><a name="en-us_topic_0120206045_p1838772218354"></a>Latest</p>
</td>
</tr>
<tr id="row14351951154713"><td class="cellrowborder" valign="top" width="21.08210821082108%" headers="mcps1.2.4.1.1 "><p id="p535285110473"><a name="p535285110473"></a><a name="p535285110473"></a>Dump Interval (s)</p>
</td>
<td class="cellrowborder" valign="top" width="56.66566656665667%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0120206045_p4387172214359"><a name="en-us_topic_0120206045_p4387172214359"></a><a name="en-us_topic_0120206045_p4387172214359"></a>Interval at which data from the DIS stream will be imported into dump destination, such as OBS, MRS, DLI, DWS, and CloudTable. If no data was pushed to the DIS stream during the time specified here, the dump file will not be generated.</p>
<p id="en-us_topic_0120206045_p1938732213352"><a name="en-us_topic_0120206045_p1938732213352"></a><a name="en-us_topic_0120206045_p1938732213352"></a>Value range: 30s to 900s</p>
<p id="en-us_topic_0120206045_p173876227356"><a name="en-us_topic_0120206045_p173876227356"></a><a name="en-us_topic_0120206045_p173876227356"></a>Unit: second</p>
<p id="en-us_topic_0120206045_p138716221355"><a name="en-us_topic_0120206045_p138716221355"></a><a name="en-us_topic_0120206045_p138716221355"></a>Default value: 300s</p>
</td>
<td class="cellrowborder" valign="top" width="22.252225222522252%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0120206045_p1338782293511"><a name="en-us_topic_0120206045_p1338782293511"></a><a name="en-us_topic_0120206045_p1338782293511"></a>-</p>
</td>
</tr>
</tbody>
</table>

## Dumping the JSON Data to the CSV Data<a name="section83387312148"></a>

**Table  2**  Parameters for configuring a CSV dump file

<a name="table6338163110141"></a>
<table><thead align="left"><tr id="row633823191412"><th class="cellrowborder" valign="top" width="21.08210821082108%" id="mcps1.2.4.1.1"><p id="p15338631141413"><a name="p15338631141413"></a><a name="p15338631141413"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="56.66566656665667%" id="mcps1.2.4.1.2"><p id="p20338203117141"><a name="p20338203117141"></a><a name="p20338203117141"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="22.252225222522252%" id="mcps1.2.4.1.3"><p id="p18338183111414"><a name="p18338183111414"></a><a name="p18338183111414"></a>Value</p>
</th>
</tr>
</thead>
<tbody><tr id="row2033833110142"><td class="cellrowborder" valign="top" width="21.08210821082108%" headers="mcps1.2.4.1.1 "><p id="p6339123161417"><a name="p6339123161417"></a><a name="p6339123161417"></a>Task Name</p>
</td>
<td class="cellrowborder" valign="top" width="56.66566656665667%" headers="mcps1.2.4.1.2 "><p id="p933910317145"><a name="p933910317145"></a><a name="p933910317145"></a>Name of the dump task. The names of dump tasks created for the same stream must be unique. A dump task name is 1 to 64 characters long. Only letters, digits, hyphens (-), and underscores (_) are allowed.</p>
</td>
<td class="cellrowborder" valign="top" width="22.252225222522252%" headers="mcps1.2.4.1.3 "><p id="p533953117146"><a name="p533953117146"></a><a name="p533953117146"></a>-</p>
</td>
</tr>
<tr id="row10339431111410"><td class="cellrowborder" valign="top" width="21.08210821082108%" headers="mcps1.2.4.1.1 "><p id="p12339431151416"><a name="p12339431151416"></a><a name="p12339431151416"></a>Dump Bucket</p>
</td>
<td class="cellrowborder" valign="top" width="56.66566656665667%" headers="mcps1.2.4.1.2 "><p id="p18339131201418"><a name="p18339131201418"></a><a name="p18339131201418"></a>Name of the OBS bucket used to store data from the DIS stream. The bucket name is created when you create a bucket in OBS.</p>
</td>
<td class="cellrowborder" valign="top" width="22.252225222522252%" headers="mcps1.2.4.1.3 "><p id="p73391831191417"><a name="p73391831191417"></a><a name="p73391831191417"></a>-</p>
</td>
</tr>
<tr id="row12339193115148"><td class="cellrowborder" valign="top" width="21.08210821082108%" headers="mcps1.2.4.1.1 "><p id="p14339133161412"><a name="p14339133161412"></a><a name="p14339133161412"></a>File Directory</p>
</td>
<td class="cellrowborder" valign="top" width="56.66566656665667%" headers="mcps1.2.4.1.2 "><p id="p19339173121416"><a name="p19339173121416"></a><a name="p19339173121416"></a>Directory created in OBS to store files from the DIS stream.</p>
<p id="p1133943116141"><a name="p1133943116141"></a><a name="p1133943116141"></a>This directory name is 0 to 50 characters long.</p>
<p id="p13391311141"><a name="p13391311141"></a><a name="p13391311141"></a>By default, this parameter is left unspecified.</p>
</td>
<td class="cellrowborder" valign="top" width="22.252225222522252%" headers="mcps1.2.4.1.3 "><p id="p633913114143"><a name="p633913114143"></a><a name="p633913114143"></a>-</p>
</td>
</tr>
<tr id="row1833918318144"><td class="cellrowborder" valign="top" width="21.08210821082108%" headers="mcps1.2.4.1.1 "><p id="p16339143191419"><a name="p16339143191419"></a><a name="p16339143191419"></a>Time Directory Format</p>
</td>
<td class="cellrowborder" valign="top" width="56.66566656665667%" headers="mcps1.2.4.1.2 "><p id="p6339931141412"><a name="p6339931141412"></a><a name="p6339931141412"></a>Data will be saved according to the time format in the file directory of the OBS bucket.</p>
<p id="p1733913316143"><a name="p1733913316143"></a><a name="p1733913316143"></a>For example, if the time directory is accurate to day, the save path will be in the format of bucket name/file directory/year/month/day.</p>
<div class="p" id="p1033914319144"><a name="p1033914319144"></a><a name="p1033914319144"></a>Possible values are as follows:<a name="ul1433915315140"></a><a name="ul1433915315140"></a><ul id="ul1433915315140"><li>N/A: If this field is left unspecified, the time directory format will not be used.</li><li>yyyy: year.</li><li>yyyy/MM: year and month.</li><li>yyyy/MM/dd: year, month, and day.</li><li>yyyy/MM/dd/HH: year, month, day, and hour.</li><li>yyyy/MM/dd/HH/mm: year, month, day, hour, and minute.</li></ul>
</div>
<p id="p133392031161414"><a name="p133392031161414"></a><a name="p133392031161414"></a>You can only select but not enter a value in this field.</p>
</td>
<td class="cellrowborder" valign="top" width="22.252225222522252%" headers="mcps1.2.4.1.3 "><p id="p333915314145"><a name="p333915314145"></a><a name="p333915314145"></a>-</p>
</td>
</tr>
<tr id="row19340103116141"><td class="cellrowborder" valign="top" width="21.08210821082108%" headers="mcps1.2.4.1.1 "><p id="p33401131171419"><a name="p33401131171419"></a><a name="p33401131171419"></a>Offset</p>
</td>
<td class="cellrowborder" valign="top" width="56.66566656665667%" headers="mcps1.2.4.1.2 "><a name="ul1634013121419"></a><a name="ul1634013121419"></a><ul id="ul1634013121419"><li><strong id="b1241631405"><a name="b1241631405"></a><a name="b1241631405"></a>Latest</strong>: Maximum offset, indicating that the latest data will be read.</li><li><strong id="b295773374"><a name="b295773374"></a><a name="b295773374"></a>Earliest</strong>: Minimum offset, indicating that the earliest data will be read.</li></ul>
</td>
<td class="cellrowborder" valign="top" width="22.252225222522252%" headers="mcps1.2.4.1.3 "><p id="p134018313147"><a name="p134018313147"></a><a name="p134018313147"></a>Latest</p>
</td>
</tr>
<tr id="row434073181418"><td class="cellrowborder" valign="top" width="21.08210821082108%" headers="mcps1.2.4.1.1 "><p id="p14340123116146"><a name="p14340123116146"></a><a name="p14340123116146"></a>Dump Interval (s)</p>
</td>
<td class="cellrowborder" valign="top" width="56.66566656665667%" headers="mcps1.2.4.1.2 "><p id="p6340123111418"><a name="p6340123111418"></a><a name="p6340123111418"></a>User-defined interval at which data is imported from the current DIS stream into the target place. If no data is pushed to the DIS stream during the current interval, no dump file package will be generated.</p>
<p id="p15340163115146"><a name="p15340163115146"></a><a name="p15340163115146"></a>Value range: 30s to 900s</p>
<p id="p03401631191415"><a name="p03401631191415"></a><a name="p03401631191415"></a>Unit: second</p>
<p id="p1134023101415"><a name="p1134023101415"></a><a name="p1134023101415"></a>Default value: 300s</p>
</td>
<td class="cellrowborder" valign="top" width="22.252225222522252%" headers="mcps1.2.4.1.3 "><p id="p12340173181414"><a name="p12340173181414"></a><a name="p12340173181414"></a>-</p>
</td>
</tr>
</tbody>
</table>

## Dumping the JSON and CSV Data to the Parquet Data<a name="section51282162613"></a>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>[Table 3](#table1068705245510)  lists the differentiated parameters that need to be set when the source data type is JSON or CSV, the dump destination is OBS, and the dump file format is Parquet. For details about how to configure other common parameters, see  [Table 1](#table18468165816451).  

**Table  3**  Parameters for configuring a Parquet dump file

<a name="table1068705245510"></a>
<table><thead align="left"><tr id="row1668710524553"><th class="cellrowborder" valign="top" width="23.262326232623263%" id="mcps1.2.4.1.1"><p id="p0305164555620"><a name="p0305164555620"></a><a name="p0305164555620"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="43.404340434043405%" id="mcps1.2.4.1.2"><p id="p13051045165612"><a name="p13051045165612"></a><a name="p13051045165612"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p1230517459563"><a name="p1230517459563"></a><a name="p1230517459563"></a>Value</p>
</th>
</tr>
</thead>
<tbody><tr id="row2097131155910"><td class="cellrowborder" valign="top" width="23.262326232623263%" headers="mcps1.2.4.1.1 "><p id="p11971131155914"><a name="p11971131155914"></a><a name="p11971131155914"></a>Source Data Schema</p>
</td>
<td class="cellrowborder" valign="top" width="43.404340434043405%" headers="mcps1.2.4.1.2 "><p id="p5969122711441"><a name="p5969122711441"></a><a name="p5969122711441"></a>JSON or CSV data example, used to describe the JSON or CSV data format. DIS can generate an Avro schema based on the JSON or CSV data sample and convert the uploaded JSON or CSV data to the Parquet format.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p20976314593"><a name="p20976314593"></a><a name="p20976314593"></a>-</p>
</td>
</tr>
<tr id="row201713565599"><td class="cellrowborder" valign="top" width="23.262326232623263%" headers="mcps1.2.4.1.1 "><p id="p8171135618592"><a name="p8171135618592"></a><a name="p8171135618592"></a>Custom Time Directory</p>
</td>
<td class="cellrowborder" valign="top" width="43.404340434043405%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0120206045_p109384485447"><a name="en-us_topic_0120206045_p109384485447"></a><a name="en-us_topic_0120206045_p109384485447"></a>You can click <a name="en-us_topic_0120206045_image4750163771713"></a><a name="en-us_topic_0120206045_image4750163771713"></a><span><img id="en-us_topic_0120206045_image4750163771713" src="figures/wwx437827-中软基础平台部-datasight-image-2684cf81-d351-4504-ae1a-2fb70826e877.png"></span> or <a name="en-us_topic_0120206045_image87501237191719"></a><a name="en-us_topic_0120206045_image87501237191719"></a><span><img id="en-us_topic_0120206045_image87501237191719" src="figures/wwx437827-中软基础平台部-datasight-image-2737afc7-0c6b-4cf7-b8ea-fead261a6098.png"></span> to disable or enable the custom time directory.</p>
<a name="en-us_topic_0120206045_ul758115401126"></a><a name="en-us_topic_0120206045_ul758115401126"></a><ul id="en-us_topic_0120206045_ul758115401126"><li>If the custom timestamp is disabled, the directory where the object file written to OBS resides is named after the creation time of the dump file.<p id="en-us_topic_0120206045_p183381534162120"><a name="en-us_topic_0120206045_p183381534162120"></a><a name="en-us_topic_0120206045_p183381534162120"></a>For example, if a dump file was created on October 16, 2018 and the time directory format is accurate to day, the file will be saved in <em id="i14311645102414"><a name="i14311645102414"></a><a name="i14311645102414"></a>OBS bucket name</em>/<em id="i10568134842419"><a name="i10568134842419"></a><a name="i10568134842419"></a>dump file directory</em>/<strong id="b137811635274"><a name="b137811635274"></a><a name="b137811635274"></a>2018</strong>/<strong id="b13283131012279"><a name="b13283131012279"></a><a name="b13283131012279"></a>10</strong>/<strong id="b61781112132715"><a name="b61781112132715"></a><a name="b61781112132715"></a>16</strong>.</p>
</li><li>If the custom timestamp is disabled, the directory where the object file written to OBS resides is named in the time format specified in the source data.<p id="en-us_topic_0120206045_p1181145635618"><a name="en-us_topic_0120206045_p1181145635618"></a><a name="en-us_topic_0120206045_p1181145635618"></a>For example, if a dump file was created on October 16, 2018, the time directory format is accurate to day, and the time format specified in the data source is 2017/09/08 11:01:01, the file will be saved in <em id="i69388509306"><a name="i69388509306"></a><a name="i69388509306"></a>OBS bucket name</em>/<em id="i176553591309"><a name="i176553591309"></a><a name="i176553591309"></a>dump file directory</em>/<strong id="b139127183112"><a name="b139127183112"></a><a name="b139127183112"></a>2017</strong>/<strong id="b460113114317"><a name="b460113114317"></a><a name="b460113114317"></a>09</strong>/<strong id="b1674143173117"><a name="b1674143173117"></a><a name="b1674143173117"></a>08</strong>. The storage directory is defined based on the time format defined in the source data instead of the time when the dump file is created.</p>
</li></ul>
</td>
<td class="cellrowborder" rowspan="2" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0120206045_ul242514794915"></a><a name="en-us_topic_0120206045_ul242514794915"></a><ul id="en-us_topic_0120206045_ul242514794915"><li>Example 1: Dump simple JSON data.</li></ul>
<p id="en-us_topic_0120206045_p13799581689"><a name="en-us_topic_0120206045_p13799581689"></a><a name="en-us_topic_0120206045_p13799581689"></a>Source data:</p>
<p id="en-us_topic_0120206045_p246581516453"><a name="en-us_topic_0120206045_p246581516453"></a><a name="en-us_topic_0120206045_p246581516453"></a>{    "id":"1",    "date":"2018/10/16 11:00:05"}</p>
<p id="en-us_topic_0120206045_p1697333419410"><a name="en-us_topic_0120206045_p1697333419410"></a><a name="en-us_topic_0120206045_p1697333419410"></a>The configuration is as follows:</p>
<p id="en-us_topic_0120206045_p8515191715313"><a name="en-us_topic_0120206045_p8515191715313"></a><a name="en-us_topic_0120206045_p8515191715313"></a>Set the timestamp attribute name to <span class="parmvalue" id="parmvalue3567143616569"><a name="parmvalue3567143616569"></a><a name="parmvalue3567143616569"></a><b>date</b></span>, data type to <span class="parmvalue" id="parmvalue151311555155611"><a name="parmvalue151311555155611"></a><a name="parmvalue151311555155611"></a><b>String</b></span>, and timestamp format to <span class="parmvalue" id="parmvalue0100137105712"><a name="parmvalue0100137105712"></a><a name="parmvalue0100137105712"></a><b>yyyy/MM/dd HH:mm:ss</b></span> based on the source data type of the data to be dumped.</p>
<p id="en-us_topic_0120206045_p185217221581"><a name="en-us_topic_0120206045_p185217221581"></a><a name="en-us_topic_0120206045_p185217221581"></a>After the data is dumped successfully, the storage directory structure depends on the source data timestamp and the time directory format. In this example, the time directory format is accurate to day. Therefore, the final data storage directory is <em id="i886074121010"><a name="i886074121010"></a><a name="i886074121010"></a>OBS bucket name</em>/<em id="i1680801313102"><a name="i1680801313102"></a><a name="i1680801313102"></a>dump file directory</em>/<strong id="b137881720171018"><a name="b137881720171018"></a><a name="b137881720171018"></a>2018</strong>/<strong id="b144911223181012"><a name="b144911223181012"></a><a name="b144911223181012"></a>10</strong>/<strong id="b5266172591017"><a name="b5266172591017"></a><a name="b5266172591017"></a>16</strong>.</p>
<a name="en-us_topic_0120206045_ul8297195613349"></a><a name="en-us_topic_0120206045_ul8297195613349"></a><ul id="en-us_topic_0120206045_ul8297195613349"><li>Example 2: Dump multiply layers of nested JSON data.<p id="en-us_topic_0120206045_p49712221082"><a name="en-us_topic_0120206045_p49712221082"></a><a name="en-us_topic_0120206045_p49712221082"></a>Source data:</p>
<p id="en-us_topic_0120206045_p1047182223517"><a name="en-us_topic_0120206045_p1047182223517"></a><a name="en-us_topic_0120206045_p1047182223517"></a>{    "id":"1",    "detail":{        "detID":"05790110000000000103#567fd3cb13a4493eaa43076953253eed",        "endTime":"2018/10/07 13:26:35"    }}</p>
</li></ul>
<p id="en-us_topic_0120206045_p23133562349"><a name="en-us_topic_0120206045_p23133562349"></a><a name="en-us_topic_0120206045_p23133562349"></a>The configuration is as follows:</p>
<p id="en-us_topic_0120206045_p14329756133413"><a name="en-us_topic_0120206045_p14329756133413"></a><a name="en-us_topic_0120206045_p14329756133413"></a>Set the timestamp attribute name to <span class="parmvalue" id="parmvalue123291567342"><a name="parmvalue123291567342"></a><a name="parmvalue123291567342"></a><b>detail.endTime</b></span>, data type to <span class="parmvalue" id="parmvalue15730194014182"><a name="parmvalue15730194014182"></a><a name="parmvalue15730194014182"></a><b>String</b></span>, and timestamp format to <span class="parmvalue" id="parmvalue4343125633414"><a name="parmvalue4343125633414"></a><a name="parmvalue4343125633414"></a><b>yyyy/MM/dd HH:mm:ss</b></span> based on the source data type of the data to be dumped.</p>
<p id="en-us_topic_0120206045_p163435562349"><a name="en-us_topic_0120206045_p163435562349"></a><a name="en-us_topic_0120206045_p163435562349"></a>After the data is dumped successfully, the storage directory structure depends on the source data timestamp and the time directory format. In this example, the time directory format is accurate to day. Therefore, the final data storage directory is <em id="i14934234171911"><a name="i14934234171911"></a><a name="i14934234171911"></a>OBS bucket name</em>/<em id="i1793513411916"><a name="i1793513411916"></a><a name="i1793513411916"></a>dump file directory</em>/<strong id="b293613431915"><a name="b293613431915"></a><a name="b293613431915"></a>2018</strong>/<strong id="b89369348198"><a name="b89369348198"></a><a name="b89369348198"></a>10</strong>/<strong id="b293733412199"><a name="b293733412199"></a><a name="b293733412199"></a>07</strong>.</p>
<a name="en-us_topic_0120206045_ul9507111915371"></a><a name="en-us_topic_0120206045_ul9507111915371"></a><ul id="en-us_topic_0120206045_ul9507111915371"><li>Example 3: Dump CSV data.</li></ul>
<p id="en-us_topic_0120206045_p1744223114816"><a name="en-us_topic_0120206045_p1744223114816"></a><a name="en-us_topic_0120206045_p1744223114816"></a>Source data:</p>
<p id="en-us_topic_0120206045_p18531396133"><a name="en-us_topic_0120206045_p18531396133"></a><a name="en-us_topic_0120206045_p18531396133"></a>a,2010-10-12 11:00:00,b,2011-10-12 11:00:10</p>
<p id="en-us_topic_0120206045_p5441125010817"><a name="en-us_topic_0120206045_p5441125010817"></a><a name="en-us_topic_0120206045_p5441125010817"></a>The configuration is as follows:</p>
<p id="en-us_topic_0120206045_p144412050281"><a name="en-us_topic_0120206045_p144412050281"></a><a name="en-us_topic_0120206045_p144412050281"></a>Select timestamp <strong id="b14261226232"><a name="b14261226232"></a><a name="b14261226232"></a>2010-10-12 11:00:00</strong> based on the source data to be dumped. After data is converted to the Parquet format, the corresponding attribute field name is <strong id="b52624268317"><a name="b52624268317"></a><a name="b52624268317"></a>field_1</strong>. When creating a dump task, set the timestamp attribute to <span class="parmvalue" id="parmvalue11457195016819"><a name="parmvalue11457195016819"></a><a name="parmvalue11457195016819"></a><b>field_1</b></span>, data type to <span class="parmvalue" id="parmvalue2457250584"><a name="parmvalue2457250584"></a><a name="parmvalue2457250584"></a><b>String</b></span>, and timestamp format to <span class="parmvalue" id="parmvalue94574501286"><a name="parmvalue94574501286"></a><a name="parmvalue94574501286"></a><b>yyyy/MM/dd HH:mm:ss</b></span>.</p>
<p id="en-us_topic_0120206045_p1045714501089"><a name="en-us_topic_0120206045_p1045714501089"></a><a name="en-us_topic_0120206045_p1045714501089"></a>After the data is dumped successfully, the storage directory structure depends on the source data timestamp and the time directory format. In this example, the time directory format is accurate to day. Therefore, the final data storage directory is <em id="i8747171553616"><a name="i8747171553616"></a><a name="i8747171553616"></a>OBS bucket name</em>/<em id="i13747915163614"><a name="i13747915163614"></a><a name="i13747915163614"></a>dump file directory</em>/<strong id="b77482015113619"><a name="b77482015113619"></a><a name="b77482015113619"></a>2010</strong>/<strong id="b87481215173613"><a name="b87481215173613"></a><a name="b87481215173613"></a>10</strong>/<strong id="b974861563617"><a name="b974861563617"></a><a name="b974861563617"></a>12</strong>.</p>
</td>
</tr>
<tr id="row1390112278010"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p69021327305"><a name="p69021327305"></a><a name="p69021327305"></a>Source Data Timestamp</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><a name="en-us_topic_0120206045_ul2686128153"></a><a name="en-us_topic_0120206045_ul2686128153"></a><ul id="en-us_topic_0120206045_ul2686128153"><li>Attribute name of the timestamp.<div class="note" id="en-us_topic_0120206045_note847092512169"><a name="en-us_topic_0120206045_note847092512169"></a><a name="en-us_topic_0120206045_note847092512169"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0120206045_p747012513166"><a name="en-us_topic_0120206045_p747012513166"></a><a name="en-us_topic_0120206045_p747012513166"></a>Enter the field name corresponding to the timestamp defined in the source data to be uploaded.</p>
</div></div>
</li><li>Timestamp format. Possible values can be:<p id="en-us_topic_0120206045_p770215219156"><a name="en-us_topic_0120206045_p770215219156"></a><a name="en-us_topic_0120206045_p770215219156"></a>yyyy/MM/dd HH:mm:ss</p>
<p id="en-us_topic_0120206045_p07177218156"><a name="en-us_topic_0120206045_p07177218156"></a><a name="en-us_topic_0120206045_p07177218156"></a>MM/dd/yyyy HH:mm:ss</p>
<p id="en-us_topic_0120206045_p171718291517"><a name="en-us_topic_0120206045_p171718291517"></a><a name="en-us_topic_0120206045_p171718291517"></a>dd/MM/yyyy HH:mm:ss</p>
<p id="en-us_topic_0120206045_p9717625156"><a name="en-us_topic_0120206045_p9717625156"></a><a name="en-us_topic_0120206045_p9717625156"></a>yyyy-MM-dd HH:mm:ss</p>
<p id="en-us_topic_0120206045_p147171261517"><a name="en-us_topic_0120206045_p147171261517"></a><a name="en-us_topic_0120206045_p147171261517"></a>MM-dd-yyyy HH:mm:ss</p>
<p id="en-us_topic_0120206045_p5733529159"><a name="en-us_topic_0120206045_p5733529159"></a><a name="en-us_topic_0120206045_p5733529159"></a>dd-MM-yyyy HH:mm:ss</p>
</li><li>Data type. Possible values can be:<a name="en-us_topic_0120206045_ul274962171520"></a><a name="en-us_topic_0120206045_ul274962171520"></a><ul id="en-us_topic_0120206045_ul274962171520"><li>String</li><li>Timestamp<div class="note" id="en-us_topic_0120206045_note1624112537265"><a name="en-us_topic_0120206045_note1624112537265"></a><a name="en-us_topic_0120206045_note1624112537265"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0120206045_p18241185310265"><a name="en-us_topic_0120206045_p18241185310265"></a><a name="en-us_topic_0120206045_p18241185310265"></a>If the type of the source data to be uploaded is <strong id="b912711101447"><a name="b912711101447"></a><a name="b912711101447"></a>Timestamp</strong>, the value must be accurate to milliseconds.</p>
</div></div>
</li></ul>
</li></ul>
</td>
</tr>
</tbody>
</table>

## Dumping the JSON and CSV Data to the CarbonData Data<a name="section167738422917"></a>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>[Table 4](#table1977324211913)  lists the differentiated parameters that need to be set when the source data type is JSON or CSV, the dump destination is OBS, and the dump file format is CarbonData. For details about how to configure other common parameters, see  [Table 1](#table18468165816451).  

**Table  4**  Parameters for configuring a CarbonData dump file

<a name="table1977324211913"></a>
<table><thead align="left"><tr id="row157732421993"><th class="cellrowborder" valign="top" width="23.262326232623263%" id="mcps1.2.4.1.1"><p id="p3773114212919"><a name="p3773114212919"></a><a name="p3773114212919"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="43.404340434043405%" id="mcps1.2.4.1.2"><p id="p10773164215912"><a name="p10773164215912"></a><a name="p10773164215912"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p1577311424915"><a name="p1577311424915"></a><a name="p1577311424915"></a>Value</p>
</th>
</tr>
</thead>
<tbody><tr id="row17775184215917"><td class="cellrowborder" valign="top" width="23.262326232623263%" headers="mcps1.2.4.1.1 "><p id="p1277511423913"><a name="p1277511423913"></a><a name="p1277511423913"></a>Source Data Schema</p>
</td>
<td class="cellrowborder" valign="top" width="43.404340434043405%" headers="mcps1.2.4.1.2 "><p id="p14317210417"><a name="p14317210417"></a><a name="p14317210417"></a>JSON or CSV data sample, used to describe the JSON or CSV data format. DIS can generate an Avro schema based on the JSON or CSV data sample and convert the uploaded JSON or CSV data to the CarbonData format.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p877511422092"><a name="p877511422092"></a><a name="p877511422092"></a>-</p>
</td>
</tr>
<tr id="row7775842990"><td class="cellrowborder" valign="top" width="23.262326232623263%" headers="mcps1.2.4.1.1 "><p id="p6159105319119"><a name="p6159105319119"></a><a name="p6159105319119"></a>CarbonData Retrieval Attribute</p>
</td>
<td class="cellrowborder" valign="top" width="43.404340434043405%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0120206045_p19391102713416"><a name="en-us_topic_0120206045_p19391102713416"></a><a name="en-us_topic_0120206045_p19391102713416"></a>Attribute of the carbon table, used to create a carbon writer.</p>
<p id="en-us_topic_0120206045_p19478201112210"><a name="en-us_topic_0120206045_p19478201112210"></a><a name="en-us_topic_0120206045_p19478201112210"></a>The following keys are supported:</p>
<a name="en-us_topic_0120206045_ul126024616213"></a><a name="en-us_topic_0120206045_ul126024616213"></a><ul id="en-us_topic_0120206045_ul126024616213"><li><strong id="b13379104212612"><a name="b13379104212612"></a><a name="b13379104212612"></a>table_blocksize</strong>: Size of a table block. The value ranges from 1 MB to 2048 MB. The default value is 1024 MB.</li><li><strong id="b43747457617"><a name="b43747457617"></a><a name="b43747457617"></a>table_blocklet_size</strong>: Size of the blocklet in a file. The default value is 64 MB.</li><li>local_dictionary_threshold</li><li><strong id="b156827313713"><a name="b156827313713"></a><a name="b156827313713"></a>local_dictionary_enable</strong>: Possible values can be <strong id="b1769734295414"><a name="b1769734295414"></a><a name="b1769734295414"></a>true</strong> or <strong id="b776984675415"><a name="b776984675415"></a><a name="b776984675415"></a>false</strong>. The default value is <strong id="b067505815547"><a name="b067505815547"></a><a name="b067505815547"></a>false</strong>.</li><li><strong id="b177681812972"><a name="b177681812972"></a><a name="b177681812972"></a>sort_columns</strong>: Specifies the index column. Multi-level index columns are separated by commas (,).</li><li><strong id="b16771031572"><a name="b16771031572"></a><a name="b16771031572"></a>sort_scope</strong>: Specifies the scope where data is sorted during loading. Currently, the following types are supported:<a name="en-us_topic_0120206045_ul19249218407"></a><a name="en-us_topic_0120206045_ul19249218407"></a><ul id="en-us_topic_0120206045_ul19249218407"><li><strong id="b265534294"><a name="b265534294"></a><a name="b265534294"></a>local_sort</strong>: Default value, indicating that data is sorted in a node.</li><li><strong id="b1475714441597"><a name="b1475714441597"></a><a name="b1475714441597"></a>no_sort</strong>: Data is not sorted. It is used when data needs to be saved to a database quickly. After the data is saved to the database, you can use the <strong id="b103971925165911"><a name="b103971925165911"></a><a name="b103971925165911"></a>Compaction</strong> command to create an index when the system is idle.</li><li><strong id="b1211614581015"><a name="b1211614581015"></a><a name="b1211614581015"></a>batch_sort</strong>: A CarbonData file is generated after the memory is sorted in a node and no full sorting is performed on the node. This configuration improves the loading speed, but the query performance is inferior to that of <strong id="b195212396107"><a name="b195212396107"></a><a name="b195212396107"></a>LOCAL_SORT</strong>.</li></ul>
</li><li>long_string_columns</li></ul>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0120206045_p42571613476"><a name="en-us_topic_0120206045_p42571613476"></a><a name="en-us_topic_0120206045_p42571613476"></a>-</p>
</td>
</tr>
</tbody>
</table>

