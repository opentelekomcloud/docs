# Adding a Job and Executing the Job<a name="EN-US_TOPIC_0172486174"></a>

## Function<a name="section4408504619327"></a>

This API is used to add a job to an MRS cluster and execute the job. This API is incompatible with Sahara.

## URI<a name="section10186656193217"></a>

-   Format

    POST /v1.1/\{project\_id\}/jobs/submit-job

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
    <tbody><tr id="row39786771142917"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1503055142917"><a name="p1503055142917"></a><a name="p1503055142917"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p54638598142917"><a name="p54638598142917"></a><a name="p54638598142917"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p63650338142917"><a name="p63650338142917"></a><a name="p63650338142917"></a>Project ID. For details on how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
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
<tbody><tr id="row36582554193317"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p10396884193317"><a name="p10396884193317"></a><a name="p10396884193317"></a>job_type</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p36841295193317"><a name="p36841295193317"></a><a name="p36841295193317"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p346461129313"><a name="p346461129313"></a><a name="p346461129313"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p32476122205057"><a name="p32476122205057"></a><a name="p32476122205057"></a>Job type code</p>
<a name="ul5947149515590"></a><a name="ul5947149515590"></a><ul id="ul5947149515590"><li>1: MapReduce</li><li>2: Spark</li><li>3: Hive Script</li><li>4: HiveQL (not supported currently)</li><li>5: DistCp, importing and exporting data. For details, see <a href="#table3863810010324">Table 3</a>.</li><li>6: Spark Script</li><li>7: Spark SQL, submitting Spark SQL statements. For details, see <a href="#table63617887103233">Table 4</a>. (not supported in this API currently)<div class="note" id="note4514581911127"><a name="note4514581911127"></a><a name="note4514581911127"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p365918811127"><a name="p365918811127"></a><a name="p365918811127"></a>Spark and Hive jobs can be added to only clusters that include Spark and Hive components.</p>
</div></div>
</li></ul>
</td>
</tr>
<tr id="row57932449102743"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p62016791102743"><a name="p62016791102743"></a><a name="p62016791102743"></a>job_name</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p57304145102743"><a name="p57304145102743"></a><a name="p57304145102743"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p277864793547"><a name="p277864793547"></a><a name="p277864793547"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p1370122345910"><a name="p1370122345910"></a><a name="p1370122345910"></a>Job name</p>
<p id="p29070416105535"><a name="p29070416105535"></a><a name="p29070416105535"></a>Contains only 1 to 64 letters, digits, hyphens (-), and underscores (_).</p>
<div class="note" id="note60307154105535"><a name="note60307154105535"></a><a name="note60307154105535"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p5893482105535"><a name="p5893482105535"></a><a name="p5893482105535"></a>Identical job names are allowed but not recommended.</p>
</div></div>
</td>
</tr>
<tr id="row12562929114736"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p10964343114736"><a name="p10964343114736"></a><a name="p10964343114736"></a>cluster_id</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p15696597114736"><a name="p15696597114736"></a><a name="p15696597114736"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p63464884114736"><a name="p63464884114736"></a><a name="p63464884114736"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p40382012114736"><a name="p40382012114736"></a><a name="p40382012114736"></a>Cluster ID</p>
</td>
</tr>
<tr id="row8742005193317"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p4203226995210"><a name="p4203226995210"></a><a name="p4203226995210"></a>jar_path</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p4917062595210"><a name="p4917062595210"></a><a name="p4917062595210"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p154217579313"><a name="p154217579313"></a><a name="p154217579313"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p1712419591545"><a name="p1712419591545"></a><a name="p1712419591545"></a>Path of the JAR or SQL file for program execution</p>
<p id="p201991940546"><a name="p201991940546"></a><a name="p201991940546"></a>The parameter must meet the following requirements:</p>
<a name="ul28108739105445"></a><a name="ul28108739105445"></a><ul id="ul28108739105445"><li>Contains a maximum of 1023 characters, excluding special characters such as ;|&amp;&gt;&lt;'$. The address cannot be empty or full of spaces.</li><li>Starts with <span class="parmvalue" id="parmvalue1813934163"><a name="parmvalue1813934163"></a><a name="parmvalue1813934163"></a><b>/</b></span> or <span class="parmvalue" id="parmvalue13130347617"><a name="parmvalue13130347617"></a><a name="parmvalue13130347617"></a><b>s3a://</b></span>. The OBS path does not support files or programs encrypted by KMS.</li><li>Spark Script must end with <span class="parmvalue" id="parmvalue17976426105445"><a name="parmvalue17976426105445"></a><a name="parmvalue17976426105445"></a><b>.sql</b></span> while MapReduce and Spark Jar must end with <span class="parmvalue" id="parmvalue27570107105445"><a name="parmvalue27570107105445"></a><a name="parmvalue27570107105445"></a><b>.jar</b></span>.<strong id="b13627621162918"><a name="b13627621162918"></a><a name="b13627621162918"></a>sql</strong> and <strong id="b848112303292"><a name="b848112303292"></a><a name="b848112303292"></a>jar</strong> are case-insensitive.</li></ul>
</td>
</tr>
<tr id="row4788257010284"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p881779095210"><a name="p881779095210"></a><a name="p881779095210"></a>arguments</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p4315240795210"><a name="p4315240795210"></a><a name="p4315240795210"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p412027909313"><a name="p412027909313"></a><a name="p412027909313"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p568404895210"><a name="p568404895210"></a><a name="p568404895210"></a>Key parameter for program execution. The parameter is specified by the function of the user's program. MRS is only responsible for loading the parameter.</p>
<p id="p5115643295210"><a name="p5115643295210"></a><a name="p5115643295210"></a>The parameter contains a maximum of 2047 characters, excluding special characters such as ;|&amp;&gt;'&lt;$, and can be left blank.</p>
<div class="note" id="note62371709174814"><a name="note62371709174814"></a><a name="note62371709174814"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p20521095174814"><a name="p20521095174814"></a><a name="p20521095174814"></a>When entering a parameter containing sensitive information (for example, login password), you can add an at sign (@) before the parameter name to encrypt the parameter value. This prevents the sensitive information from being persisted in plaintext. Therefore, when you view job information on the MRS, sensitive information will be displayed as asterisks (*).</p>
<p id="p1265001117571"><a name="p1265001117571"></a><a name="p1265001117571"></a>For example, username=admin @password=admin_123.</p>
</div></div>
</td>
</tr>
<tr id="row22945661205631"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p4761952395210"><a name="p4761952395210"></a><a name="p4761952395210"></a>input</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p3197614195210"><a name="p3197614195210"></a><a name="p3197614195210"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p490916929313"><a name="p490916929313"></a><a name="p490916929313"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p3993064895210"><a name="p3993064895210"></a><a name="p3993064895210"></a>Path for inputting data, which must start with <span class="parmvalue" id="parmvalue178840111121"><a name="parmvalue178840111121"></a><a name="parmvalue178840111121"></a><b>/</b></span> or <span class="parmvalue" id="parmvalue888551101218"><a name="parmvalue888551101218"></a><a name="parmvalue888551101218"></a><b>s3a://</b></span>. Set this parameter to a correct OBS path. The OBS path does not support files or programs encrypted by KMS.</p>
<p id="p5908955195210"><a name="p5908955195210"></a><a name="p5908955195210"></a>The parameter contains a maximum of 1023 characters, excluding special characters such as ;|&amp;&gt;'&lt;$, and can be left blank.</p>
</td>
</tr>
<tr id="row4446769920575"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p2252515695210"><a name="p2252515695210"></a><a name="p2252515695210"></a>output</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p1259835495210"><a name="p1259835495210"></a><a name="p1259835495210"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p170040869313"><a name="p170040869313"></a><a name="p170040869313"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p1383379395210"><a name="p1383379395210"></a><a name="p1383379395210"></a>Path for outputting data, which must start with <span class="parmvalue" id="parmvalue14409181161310"><a name="parmvalue14409181161310"></a><a name="parmvalue14409181161310"></a><b>/</b></span> or <span class="parmvalue" id="parmvalue04101911161318"><a name="parmvalue04101911161318"></a><a name="parmvalue04101911161318"></a><b>s3a://</b></span>. A correct OBS path is required. If the path does not exist, the system automatically creates it.</p>
<p id="p3233760195210"><a name="p3233760195210"></a><a name="p3233760195210"></a>The parameter contains a maximum of 1023 characters, excluding special characters such as ;|&amp;&gt;'&lt;$, and can be left blank.</p>
</td>
</tr>
<tr id="row3637816111569"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p654800595210"><a name="p654800595210"></a><a name="p654800595210"></a>job_log</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p6062642495210"><a name="p6062642495210"></a><a name="p6062642495210"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p351537089313"><a name="p351537089313"></a><a name="p351537089313"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p1179329195210"><a name="p1179329195210"></a><a name="p1179329195210"></a>Path for storing job logs that record job running status. The path must start with <span class="parmvalue" id="parmvalue1863110314147"><a name="parmvalue1863110314147"></a><a name="parmvalue1863110314147"></a><b>/</b></span> or <span class="parmvalue" id="parmvalue363163119143"><a name="parmvalue363163119143"></a><a name="parmvalue363163119143"></a><b>s3a://</b></span>. A correct OBS path is required.</p>
<p id="p6637185895210"><a name="p6637185895210"></a><a name="p6637185895210"></a>The parameter contains a maximum of 1023 characters, excluding special characters such as ;|&amp;&gt;'&lt;$, and can be left blank.</p>
</td>
</tr>
<tr id="row14131383162346"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p59697381162356"><a name="p59697381162356"></a><a name="p59697381162356"></a>hive_script_path</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p3649694162356"><a name="p3649694162356"></a><a name="p3649694162356"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p211278519313"><a name="p211278519313"></a><a name="p211278519313"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p27189832162356"><a name="p27189832162356"></a><a name="p27189832162356"></a>SQL program path</p>
<p id="p111345215159"><a name="p111345215159"></a><a name="p111345215159"></a>This parameter is needed by Spark Script and Hive Script jobs only, and must meet the following requirements:</p>
<a name="ul43381903162356"></a><a name="ul43381903162356"></a><ul id="ul43381903162356"><li>Contains a maximum of 1023 characters, excluding special characters such as ;|&amp;&gt;&lt;'$. The address cannot be empty or full of spaces.</li><li>The path must start with <span class="parmvalue" id="parmvalue17132686162356"><a name="parmvalue17132686162356"></a><a name="parmvalue17132686162356"></a><b>/</b></span> or <span class="parmvalue" id="parmvalue48129207151559"><a name="parmvalue48129207151559"></a><a name="parmvalue48129207151559"></a><b>s3a://</b></span>. The OBS path does not support files or programs encrypted by KMS.</li><li>The path must end with <span class="parmvalue" id="parmvalue206581162356"><a name="parmvalue206581162356"></a><a name="parmvalue206581162356"></a><b>.sql</b></span>.<strong id="b1350611312346"><a name="b1350611312346"></a><a name="b1350611312346"></a>sql</strong> is case-insensitive.</li></ul>
</td>
</tr>
</tbody>
</table>

**Table  3** **DistCp**  parameter description

<a name="table3863810010324"></a>
<table><thead align="left"><tr id="row4533068110324"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p54968585103616"><a name="p54968585103616"></a><a name="p54968585103616"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p23270363103616"><a name="p23270363103616"></a><a name="p23270363103616"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p21293140163428"><a name="p21293140163428"></a><a name="p21293140163428"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="p5851266103616"><a name="p5851266103616"></a><a name="p5851266103616"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row6178122510324"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p3822335110324"><a name="p3822335110324"></a><a name="p3822335110324"></a>job_name</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p908370110324"><a name="p908370110324"></a><a name="p908370110324"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p47022802163428"><a name="p47022802163428"></a><a name="p47022802163428"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p7709151120184"><a name="p7709151120184"></a><a name="p7709151120184"></a>Job name</p>
<p id="p3280503011050"><a name="p3280503011050"></a><a name="p3280503011050"></a>Contains only 1 to 64 letters, digits, hyphens (-), and underscores (_).</p>
<div class="note" id="note2680982011050"><a name="note2680982011050"></a><a name="note2680982011050"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p3996179411050"><a name="p3996179411050"></a><a name="p3996179411050"></a>Identical job names are allowed but not recommended.</p>
</div></div>
</td>
</tr>
<tr id="row4534941510324"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p4942398910324"><a name="p4942398910324"></a><a name="p4942398910324"></a>input</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p55067941103719"><a name="p55067941103719"></a><a name="p55067941103719"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p50750592163428"><a name="p50750592163428"></a><a name="p50750592163428"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p76447910324"><a name="p76447910324"></a><a name="p76447910324"></a>Data source path</p>
<a name="ul562023841145"></a><a name="ul562023841145"></a><ul id="ul562023841145"><li>When you import data, the parameter is set to an OBS path. Files or programs encrypted by KMS are not supported.</li><li>When you export data, the parameter is set to an HDFS path.</li></ul>
</td>
</tr>
<tr id="row688031410324"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p2043453110324"><a name="p2043453110324"></a><a name="p2043453110324"></a>output</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p62056516103719"><a name="p62056516103719"></a><a name="p62056516103719"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p17157254163428"><a name="p17157254163428"></a><a name="p17157254163428"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p5455659810324"><a name="p5455659810324"></a><a name="p5455659810324"></a>Data receiving path</p>
<a name="ul226832311445"></a><a name="ul226832311445"></a><ul id="ul226832311445"><li>When you import data, the parameter is set to an HDFS path.</li><li>When you export data, the parameter is set to an OBS path.</li></ul>
</td>
</tr>
<tr id="row2124733610324"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p4331269410324"><a name="p4331269410324"></a><a name="p4331269410324"></a>file_action</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p4838819103719"><a name="p4838819103719"></a><a name="p4838819103719"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p47560333163428"><a name="p47560333163428"></a><a name="p47560333163428"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p3565927110324"><a name="p3565927110324"></a><a name="p3565927110324"></a>Types of file operations, including:</p>
<a name="ul3995823810380"></a><a name="ul3995823810380"></a><ul id="ul3995823810380"><li>export: Export data from HDFS to OBS.</li><li>import: Import data from OBS to HDFS.</li></ul>
</td>
</tr>
</tbody>
</table>

**Table  4** **Spark SQL**  parameter description

<a name="table63617887103233"></a>
<table><thead align="left"><tr id="row55179475103233"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p27628366103233"><a name="p27628366103233"></a><a name="p27628366103233"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p23305207103233"><a name="p23305207103233"></a><a name="p23305207103233"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p41131944163327"><a name="p41131944163327"></a><a name="p41131944163327"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="p8673620103233"><a name="p8673620103233"></a><a name="p8673620103233"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row10953722103233"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p14836289103233"><a name="p14836289103233"></a><a name="p14836289103233"></a>hql</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p60888752103233"><a name="p60888752103233"></a><a name="p60888752103233"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p43353145163327"><a name="p43353145163327"></a><a name="p43353145163327"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p50684616114137"><a name="p50684616114137"></a><a name="p50684616114137"></a>Spark SQL statement, which needs Base64 encoding and decoding. <span class="filepath" id="filepath4134175520335"><a name="filepath4134175520335"></a><a name="filepath4134175520335"></a><b>ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/</b></span> is a standard encoding table. MRS uses <span class="filepath" id="filepath35726041203311"><a name="filepath35726041203311"></a><a name="filepath35726041203311"></a><b>ABCDEFGHILKJMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/</b></span> for Base64 encoding. The value of the <strong id="b489803433714"><a name="b489803433714"></a><a name="b489803433714"></a>hql</strong> parameter is generated by adding any letter to the beginning of the encoded character string. The Spark SQL statement is generated by decoding the value in the background.</p>
<p id="p12634970201250"><a name="p12634970201250"></a><a name="p12634970201250"></a>Example:</p>
<a name="ol15229821202518"></a><a name="ol15229821202518"></a><ol id="ol15229821202518"><li>Obtain the Base64 encoding tool.</li><li>Enter the <span class="parmvalue" id="parmvalue2598081203133"><a name="parmvalue2598081203133"></a><a name="parmvalue2598081203133"></a><b>show tables;</b></span> Spark SQL statement in the encoding tool to perform Base64 encoding.</li><li>Obtain the encoded character string <span class="parmvalue" id="parmvalue43189727152156"><a name="parmvalue43189727152156"></a><a name="parmvalue43189727152156"></a><b>c2hvdyB0YWLsZXM7</b></span>.</li><li>At the beginning of <span class="parmvalue" id="parmvalue036417583374"><a name="parmvalue036417583374"></a><a name="parmvalue036417583374"></a><b>c2hvdyB0YWLsZXM7</b></span>, add any letter, for example, <strong id="b187691171554"><a name="b187691171554"></a><a name="b187691171554"></a>g</strong>. Then, the character string becomes <span class="parmname" id="parmname63642583378"><a name="parmname63642583378"></a><a name="parmname63642583378"></a><b>gc2hvdyB0YWLsZXM7</b></span>, that is, the value of the <strong id="b836455819376"><a name="b836455819376"></a><a name="b836455819376"></a>hql</strong> parameter.</li></ol>
</td>
</tr>
<tr id="row28941686103233"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p62575218103233"><a name="p62575218103233"></a><a name="p62575218103233"></a>job_name</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p35427858103233"><a name="p35427858103233"></a><a name="p35427858103233"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p21943888163327"><a name="p21943888163327"></a><a name="p21943888163327"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p1069874511615"><a name="p1069874511615"></a><a name="p1069874511615"></a>Job name. It contains 1 to 64 characters. Only letters, digits, hyphens (-), and underscores (_) are allowed.</p>
<div class="note" id="note2917984911615"><a name="note2917984911615"></a><a name="note2917984911615"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p6129204911615"><a name="p6129204911615"></a><a name="p6129204911615"></a>Identical job names are allowed but not recommended.</p>
</div></div>
</td>
</tr>
</tbody>
</table>

## Response<a name="section775516131425"></a>

**Table  5**  Response parameter description

<a name="table12040613193927"></a>
<table><thead align="left"><tr id="row8843854193927"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p45263556193927"><a name="p45263556193927"></a><a name="p45263556193927"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="p1907984993927"><a name="p1907984993927"></a><a name="p1907984993927"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p17473879193927"><a name="p17473879193927"></a><a name="p17473879193927"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row8387056194027"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p20048170121940"><a name="p20048170121940"></a><a name="p20048170121940"></a>templated</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p5273559121940"><a name="p5273559121940"></a><a name="p5273559121940"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p27667593121940"><a name="p27667593121940"></a><a name="p27667593121940"></a>Whether job execution objects are generated by job templates</p>
</td>
</tr>
<tr id="row21668190121640"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p10292970121640"><a name="p10292970121640"></a><a name="p10292970121640"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p20661971121640"><a name="p20661971121640"></a><a name="p20661971121640"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p63006977121640"><a name="p63006977121640"></a><a name="p63006977121640"></a>Creation time, which is a 10-bit timestamp.</p>
</td>
</tr>
<tr id="row42904543121649"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p52715992121649"><a name="p52715992121649"></a><a name="p52715992121649"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p57651023121649"><a name="p57651023121649"></a><a name="p57651023121649"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p39221277121649"><a name="p39221277121649"></a><a name="p39221277121649"></a>Update time, which is a 10-bit timestamp.</p>
</td>
</tr>
<tr id="row22471936121656"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p8287516121656"><a name="p8287516121656"></a><a name="p8287516121656"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p16212648121656"><a name="p16212648121656"></a><a name="p16212648121656"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p38156137121656"><a name="p38156137121656"></a><a name="p38156137121656"></a>Job ID</p>
</td>
</tr>
<tr id="row24499372121723"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p38292125121723"><a name="p38292125121723"></a><a name="p38292125121723"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p18955520141536"><a name="p18955520141536"></a><a name="p18955520141536"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1768719515356"><a name="p1768719515356"></a><a name="p1768719515356"></a>Project ID. For details on how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
</td>
</tr>
<tr id="row2857708612175"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p3304262412175"><a name="p3304262412175"></a><a name="p3304262412175"></a>job_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p53035375141554"><a name="p53035375141554"></a><a name="p53035375141554"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p898100141554"><a name="p898100141554"></a><a name="p898100141554"></a>Job application ID</p>
</td>
</tr>
<tr id="row32761734121731"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p36454768121731"><a name="p36454768121731"></a><a name="p36454768121731"></a>job_name</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p5357472814169"><a name="p5357472814169"></a><a name="p5357472814169"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p4458571514169"><a name="p4458571514169"></a><a name="p4458571514169"></a>Job name</p>
</td>
</tr>
<tr id="row34637547121713"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p54177922121713"><a name="p54177922121713"></a><a name="p54177922121713"></a>input_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p58298059142036"><a name="p58298059142036"></a><a name="p58298059142036"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p24522334142036"><a name="p24522334142036"></a><a name="p24522334142036"></a>Data input ID</p>
</td>
</tr>
<tr id="row52362323121740"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p13489802121740"><a name="p13489802121740"></a><a name="p13489802121740"></a>output_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p25824096142036"><a name="p25824096142036"></a><a name="p25824096142036"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p11377013142036"><a name="p11377013142036"></a><a name="p11377013142036"></a>Data output ID</p>
</td>
</tr>
<tr id="row23099520121823"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p59121852121823"><a name="p59121852121823"></a><a name="p59121852121823"></a>start_time</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p1602626141644"><a name="p1602626141644"></a><a name="p1602626141644"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p62703864141644"><a name="p62703864141644"></a><a name="p62703864141644"></a>Start time of job execution, which is a 10-bit timestamp.</p>
</td>
</tr>
<tr id="row44209130121746"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p24169774121746"><a name="p24169774121746"></a><a name="p24169774121746"></a>end_time</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p9981156141644"><a name="p9981156141644"></a><a name="p9981156141644"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p3167337141644"><a name="p3167337141644"></a><a name="p3167337141644"></a>End time of job execution, which is a 10-bit timestamp.</p>
</td>
</tr>
<tr id="row19333868121844"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p22539448121844"><a name="p22539448121844"></a><a name="p22539448121844"></a>cluster_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p40496279121844"><a name="p40496279121844"></a><a name="p40496279121844"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p58973177121844"><a name="p58973177121844"></a><a name="p58973177121844"></a>Cluster ID</p>
</td>
</tr>
<tr id="row64101544121932"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p24842601121932"><a name="p24842601121932"></a><a name="p24842601121932"></a>engine_job_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p51989737121932"><a name="p51989737121932"></a><a name="p51989737121932"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p50419192121932"><a name="p50419192121932"></a><a name="p50419192121932"></a>Workflow ID of Oozie</p>
</td>
</tr>
<tr id="row40913530121914"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p25661615121914"><a name="p25661615121914"></a><a name="p25661615121914"></a>return_code</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p56829523121914"><a name="p56829523121914"></a><a name="p56829523121914"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p39788690121914"><a name="p39788690121914"></a><a name="p39788690121914"></a>Returned code for an execution result</p>
</td>
</tr>
<tr id="row42426498121924"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p13994348121924"><a name="p13994348121924"></a><a name="p13994348121924"></a>is_public</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p11996722121924"><a name="p11996722121924"></a><a name="p11996722121924"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p32210397121924"><a name="p32210397121924"></a><a name="p32210397121924"></a>Whether a job is public</p>
<a name="ul30570541161523"></a><a name="ul30570541161523"></a><ul id="ul30570541161523"><li>true</li><li>false</li></ul>
<p id="p5781975161523"><a name="p5781975161523"></a><a name="p5781975161523"></a>The current version does not support this function.</p>
</td>
</tr>
<tr id="row64146966121851"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p28521772121851"><a name="p28521772121851"></a><a name="p28521772121851"></a>is_protected</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p31837065121851"><a name="p31837065121851"></a><a name="p31837065121851"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p28665505121851"><a name="p28665505121851"></a><a name="p28665505121851"></a>Whether a job is protected</p>
<a name="ul34999201161533"></a><a name="ul34999201161533"></a><ul id="ul34999201161533"><li>true</li><li>false</li></ul>
<p id="p13049358161533"><a name="p13049358161533"></a><a name="p13049358161533"></a>The current version does not support this function.</p>
</td>
</tr>
<tr id="row2588379712190"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1621284512190"><a name="p1621284512190"></a><a name="p1621284512190"></a>group_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p63148421141951"><a name="p63148421141951"></a><a name="p63148421141951"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p14748509141951"><a name="p14748509141951"></a><a name="p14748509141951"></a>Group ID of a job</p>
</td>
</tr>
<tr id="row2381680812197"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p5011328212197"><a name="p5011328212197"></a><a name="p5011328212197"></a>jar_path</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p5429436914200"><a name="p5429436914200"></a><a name="p5429436914200"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p3576773514200"><a name="p3576773514200"></a><a name="p3576773514200"></a>Path of the <strong id="b177514235467"><a name="b177514235467"></a><a name="b177514235467"></a>.jar</strong> file for program execution</p>
</td>
</tr>
<tr id="row1756817121813"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p8084509121813"><a name="p8084509121813"></a><a name="p8084509121813"></a>input</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p61444593142016"><a name="p61444593142016"></a><a name="p61444593142016"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p10956159142016"><a name="p10956159142016"></a><a name="p10956159142016"></a>Address for inputting data</p>
</td>
</tr>
<tr id="row1372989312184"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p3837955812184"><a name="p3837955812184"></a><a name="p3837955812184"></a>output</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p1085221142016"><a name="p1085221142016"></a><a name="p1085221142016"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p20794095142016"><a name="p20794095142016"></a><a name="p20794095142016"></a>Address for outputting data</p>
</td>
</tr>
<tr id="row34000642121755"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p2588600121755"><a name="p2588600121755"></a><a name="p2588600121755"></a>job_log</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p41520902142110"><a name="p41520902142110"></a><a name="p41520902142110"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p7749910142110"><a name="p7749910142110"></a><a name="p7749910142110"></a>Address for storing job logs</p>
</td>
</tr>
<tr id="row2501321914242"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1280482614242"><a name="p1280482614242"></a><a name="p1280482614242"></a>job_type</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p12539997142110"><a name="p12539997142110"></a><a name="p12539997142110"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p9106851142110"><a name="p9106851142110"></a><a name="p9106851142110"></a>Job type code</p>
<a name="ul14852800142110"></a><a name="ul14852800142110"></a><ul id="ul14852800142110"><li>1: MapReduce</li><li>2: Spark</li><li>3: Hive Script</li><li>4: HiveQL (not supported currently)</li><li>5: DistCp</li><li>6: Spark Script</li><li>7: Spark SQL (not supported in this API currently)</li></ul>
</td>
</tr>
<tr id="row5695735714252"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p5014324414252"><a name="p5014324414252"></a><a name="p5014324414252"></a>file_action</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p31897142128"><a name="p31897142128"></a><a name="p31897142128"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p2583722142128"><a name="p2583722142128"></a><a name="p2583722142128"></a>Data import and export</p>
</td>
</tr>
<tr id="row2097336914259"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p2112133014259"><a name="p2112133014259"></a><a name="p2112133014259"></a>arguments</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p26217341142148"><a name="p26217341142148"></a><a name="p26217341142148"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p43229902142148"><a name="p43229902142148"></a><a name="p43229902142148"></a>Key parameter for program execution. The parameter is specified by the function of the user's internal program. MRS is only responsible for loading the parameter. This parameter can be empty.</p>
</td>
</tr>
<tr id="row624173961439"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p226442851439"><a name="p226442851439"></a><a name="p226442851439"></a>job_state</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p6666243914228"><a name="p6666243914228"></a><a name="p6666243914228"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p3094845114228"><a name="p3094845114228"></a><a name="p3094845114228"></a>Job status code</p>
<a name="ul13080661695"></a><a name="ul13080661695"></a><ul id="ul13080661695"><li>-1: Terminated</li><li>1: Starting</li><li>2: Running</li><li>3: Completed</li><li>4: Abnormal</li><li>5: Error</li></ul>
</td>
</tr>
<tr id="row4846002714355"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p3294814314355"><a name="p3294814314355"></a><a name="p3294814314355"></a>job_final_status</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p2627918214228"><a name="p2627918214228"></a><a name="p2627918214228"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p25388152145857"><a name="p25388152145857"></a><a name="p25388152145857"></a>Final job status</p>
<a name="ul27166780145857"></a><a name="ul27166780145857"></a><ul id="ul27166780145857"><li>0: unfinished</li><li>1: terminated due to an execution error</li><li>2: executed successfully</li><li>3: canceled</li></ul>
</td>
</tr>
<tr id="row371401061445"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p555586001445"><a name="p555586001445"></a><a name="p555586001445"></a>hive_script_path</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p55880059142240"><a name="p55880059142240"></a><a name="p55880059142240"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p29990897142240"><a name="p29990897142240"></a><a name="p29990897142240"></a>Address of the Hive script</p>
</td>
</tr>
<tr id="row1977685014520"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p5842105014520"><a name="p5842105014520"></a><a name="p5842105014520"></a>create_by</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p52983467142240"><a name="p52983467142240"></a><a name="p52983467142240"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p63802438142240"><a name="p63802438142240"></a><a name="p63802438142240"></a>User ID for creating jobs</p>
<p id="p5897187514510"><a name="p5897187514510"></a><a name="p5897187514510"></a>This parameter is not used in the current version, but is retained for compatibility with earlier versions.</p>
</td>
</tr>
<tr id="row65069714440"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p5270649514440"><a name="p5270649514440"></a><a name="p5270649514440"></a>finished_step</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p5534688142240"><a name="p5534688142240"></a><a name="p5534688142240"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p45656553142240"><a name="p45656553142240"></a><a name="p45656553142240"></a>Number of completed steps</p>
<p id="p2504751814513"><a name="p2504751814513"></a><a name="p2504751814513"></a>This parameter is not used in the current version, but is retained for compatibility with earlier versions.</p>
</td>
</tr>
<tr id="row5260952714511"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p3351325814511"><a name="p3351325814511"></a><a name="p3351325814511"></a>job_main_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p6044962714230"><a name="p6044962714230"></a><a name="p6044962714230"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p6458165214230"><a name="p6458165214230"></a><a name="p6458165214230"></a>Main ID of a job</p>
<p id="p4059885114508"><a name="p4059885114508"></a><a name="p4059885114508"></a>This parameter is not used in the current version, but is retained for compatibility with earlier versions.</p>
</td>
</tr>
<tr id="row96030801453"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p396520331453"><a name="p396520331453"></a><a name="p396520331453"></a>job_step_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p3671105514230"><a name="p3671105514230"></a><a name="p3671105514230"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p2080547814230"><a name="p2080547814230"></a><a name="p2080547814230"></a>Step ID of a job</p>
<p id="p30405496145012"><a name="p30405496145012"></a><a name="p30405496145012"></a>This parameter is not used in the current version, but is retained for compatibility with earlier versions.</p>
</td>
</tr>
<tr id="row1130301914455"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p4312932914455"><a name="p4312932914455"></a><a name="p4312932914455"></a>postpone_at</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p59048414230"><a name="p59048414230"></a><a name="p59048414230"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p4782921914230"><a name="p4782921914230"></a><a name="p4782921914230"></a>Delay time, which is a 10-bit timestamp.</p>
<p id="p15159739144955"><a name="p15159739144955"></a><a name="p15159739144955"></a>This parameter is not used in the current version, but is retained for compatibility with earlier versions.</p>
</td>
</tr>
<tr id="row581419814447"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p118804214447"><a name="p118804214447"></a><a name="p118804214447"></a>step_name</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p3800048714230"><a name="p3800048714230"></a><a name="p3800048714230"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p5814056814230"><a name="p5814056814230"></a><a name="p5814056814230"></a>Step name of a job</p>
<p id="p32873352145019"><a name="p32873352145019"></a><a name="p32873352145019"></a>This parameter is not used in the current version, but is retained for compatibility with earlier versions.</p>
</td>
</tr>
<tr id="row507987314414"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p881657214414"><a name="p881657214414"></a><a name="p881657214414"></a>step_num</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p65588007142319"><a name="p65588007142319"></a><a name="p65588007142319"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p4812513145022"><a name="p4812513145022"></a><a name="p4812513145022"></a>Number of steps</p>
<p id="p11028364142319"><a name="p11028364142319"></a><a name="p11028364142319"></a>This parameter is not used in the current version, but is retained for compatibility with earlier versions.</p>
</td>
</tr>
<tr id="row132578714422"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p4027988414422"><a name="p4027988414422"></a><a name="p4027988414422"></a>task_num</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p53722769142319"><a name="p53722769142319"></a><a name="p53722769142319"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p56577012142319"><a name="p56577012142319"></a><a name="p56577012142319"></a>Number of tasks</p>
<p id="p50694354145030"><a name="p50694354145030"></a><a name="p50694354145030"></a>This parameter is not used in the current version, but is retained for compatibility with earlier versions.</p>
</td>
</tr>
<tr id="row5130719714431"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p6224232214431"><a name="p6224232214431"></a><a name="p6224232214431"></a>update_by</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p39799355142319"><a name="p39799355142319"></a><a name="p39799355142319"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p2522359142319"><a name="p2522359142319"></a><a name="p2522359142319"></a>User ID for updating jobs</p>
</td>
</tr>
<tr id="row473298451470"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p85122171470"><a name="p85122171470"></a><a name="p85122171470"></a>credentials</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p25066895142337"><a name="p25066895142337"></a><a name="p25066895142337"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p17152630142337"><a name="p17152630142337"></a><a name="p17152630142337"></a>Token</p>
<p id="p197619271524"><a name="p197619271524"></a><a name="p197619271524"></a>The current version does not support this function.</p>
</td>
</tr>
<tr id="row5423502514712"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p3096092314712"><a name="p3096092314712"></a><a name="p3096092314712"></a>user_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p6319581214712"><a name="p6319581214712"></a><a name="p6319581214712"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1858712314712"><a name="p1858712314712"></a><a name="p1858712314712"></a>User ID for creating jobs</p>
<p id="p44645113144925"><a name="p44645113144925"></a><a name="p44645113144925"></a>This parameter is not used in the current version, but is retained for compatibility with earlier versions.</p>
</td>
</tr>
<tr id="row4512948014720"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p3160926714720"><a name="p3160926714720"></a><a name="p3160926714720"></a>job_configs</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p33219872143521"><a name="p33219872143521"></a><a name="p33219872143521"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p6455092143521"><a name="p6455092143521"></a><a name="p6455092143521"></a>Key-value pair set for saving job running configurations</p>
</td>
</tr>
<tr id="row4615599914728"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p4764841414728"><a name="p4764841414728"></a><a name="p4764841414728"></a>extra</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p8141885143521"><a name="p8141885143521"></a><a name="p8141885143521"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p10345716105310"><a name="p10345716105310"></a><a name="p10345716105310"></a>Authentication information</p>
<p id="p55512955143521"><a name="p55512955143521"></a><a name="p55512955143521"></a>The current version does not support this function.</p>
</td>
</tr>
<tr id="row3766101214740"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p3064311414740"><a name="p3064311414740"></a><a name="p3064311414740"></a>data_source_urls</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p2299922143521"><a name="p2299922143521"></a><a name="p2299922143521"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p52075956143521"><a name="p52075956143521"></a><a name="p52075956143521"></a>Data source URL</p>
</td>
</tr>
<tr id="row6023152714753"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p4691550114753"><a name="p4691550114753"></a><a name="p4691550114753"></a>info</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p46864266143521"><a name="p46864266143521"></a><a name="p46864266143521"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p37909211143521"><a name="p37909211143521"></a><a name="p37909211143521"></a>Key-value pair set, containing job running information returned by Oozie</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section1210015461189"></a>

-   Example request

    The following is an example of an MapReduce job request:

    ```
    {
        "job_type": 1, 
        "job_name": "mrs_test_jobone_20170602_141106", 
        "cluster_id": "e955a7a3-d334-4943-a39a-994976900d56", 
        "jar_path": "s3a://mrs-opsadm/jarpath/hadoop-mapreduce-examples-2.7.2.jar", 
        "arguments": "wordcount", 
        "input": "s3a://mrs-opsadm/input/", 
        "output": "s3a://mrs-opsadm/output/", 
        "job_log": "s3a://mrs-opsadm/log/", 
        "file_action": "", 
        "hql": "", 
        "hive_script_path": ""
    }
    ```

    The request example of Spark job:

    ```
    {
        "job_type": 2, 
        "job_name": "mrs_test_sparkjob_20170602_141106", 
        "cluster_id": "e955a7a3-d334-4943-a39a-994976900d56", 
        "jar_path": "s3a://mrs-opsadm/jarpath/spark-test.jar", 
        "arguments": "org.apache.spark.examples.SparkPi 10", 
        "input": "", 
        "output": "s3a://mrs-opsadm/output/", 
        "job_log": "s3a://mrs-opsadm/log/", 
        "file_action": "", 
        "hql": "", 
        "hive_script_path": ""
    }
    ```

    The request example of Hive Script job:

    ```
    {
        "job_type": 3, 
        "job_name": "mrs_test_SparkScriptJob_20170602_141106", 
        "cluster_id": "e955a7a3-d334-4943-a39a-994976900d56", 
        "jar_path": "s3a://mrs-opsadm/jarpath/Hivescript.sql", 
        "arguments": "", 
        "input": "s3a://mrs-opsadm/input/", 
        "output": "s3a://mrs-opsadm/output/", 
        "job_log": "s3a://mrs-opsadm/log/", 
        "file_action": "", 
        "hql": "", 
        "hive_script_path": "s3a://mrs-opsadm/jarpath/Hivescript.sql"
    }
    ```

    The request example of DistCp job for import:

    ```
    {
        "job_type": 5, 
        "job_name": "mrs_test_importjob_20170602_141106", 
        "cluster_id": "e955a7a3-d334-4943-a39a-994976900d56", 
        "input": "s3a://mrs-opsadm/jarpath/hadoop-mapreduce-examples-2.7.2.jar", 
        "output": "/user", 
        "file_action": "import"
    }
    ```

    The request example of DistCp job for export:

    ```
    {
        "job_type": 5, 
        "job_name": "mrs_test_exportjob_20170602_141106", 
        "cluster_id": "e955a7a3-d334-4943-a39a-994976900d56", 
        "input": "/user/hadoop-mapreduce-examples-2.7.2.jar", 
        "output": "s3a://mrs-opsadm/jarpath/", 
        "file_action": "export"
    }
    ```

    The request example of Spark Script job:

    ```
    {
        "job_type": 6, 
        "job_name": "mrs_test_sparkscriptjob_20170602_141106", 
        "cluster_id": "e955a7a3-d334-4943-a39a-994976900d56", 
        "jar_path": "s3a://mrs-opsadm/jarpath/sparkscript.sql", 
        "arguments": "", 
        "input": "s3a://mrs-opsadm/input/", 
        "output": "s3a://mrs-opsadm/output/", 
        "job_log": "s3a://mrs-opsadm/log/", 
        "file_action": "", 
        "hql": "", 
        "hive_script_path": "s3a://mrs-opsadm/jarpath/sparkscript.sql"
    }
    ```

-   Example response

    ```
    {
      "job_execution": {
        "templated": false,
        "created_at": 1496387588,
        "updated_at": 1496387588,
        "id": "12ee9ae4-6ee1-48c6-bb84-fb0b4f76cf03",
        "tenant_id": "c71ad83a66c5470496c2ed6e982621cc",
        "job_id": "",
        "job_name": "mrs_test_jobone_20170602_141106",
        "input_id": null,
        "output_id": null,
        "start_time": 1496387588,
        "end_time": null,
        "cluster_id": "e955a7a3-d334-4943-a39a-994976900d56",
        "engine_job_id": null,
        "return_code": null,
        "is_public": null,
        "is_protected": null,
        "group_id": "12ee9ae4-6ee1-48c6-bb84-fb0b4f76cf03",
        "jar_path": "s3a://mrs-opsadm/jarpath/hadoop-mapreduce-examples-2.7.2.jar",
        "input": "s3a://mrs-opsadm/input/",
        "output": "s3a://mrs-opsadm/output/",
        "job_log": "s3a://mrs-opsadm/log/",
        "job_type": 1,
        "file_action": "",
        "arguments": "wordcount",
        "hql": "",
        "job_state": 2,
        "job_final_status": 0,
        "hive_script_path": "",
        "create_by": "b67132be2f054a45b247365647e05af0",
        "finished_step": 0,
        "job_main_id": "",
        "job_step_id": "",
        "postpone_at": 1496387588,
        "step_name": "",
        "step_num": 0,
        "task_num": 0,
        "update_by": "b67132be2f054a45b247365647e05af0",
        "credentials": "",
        "user_id": "b67132be2f054a45b247365647e05af0",
        "job_configs": null,
        "extra": null,
        "data_source_urls": null,
        "info": null
      }
    }
    ```


## Status Code<a name="section4391766619434"></a>

[Table 6](#table1584477916050)  describes the status code of this API.

**Table  6**  Status Code

<a name="table1584477916050"></a>
<table><thead align="left"><tr id="row1339492016050"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.3.1.1"><p id="p3411176516050"><a name="p3411176516050"></a><a name="p3411176516050"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.2.3.1.2"><p id="p1158961516050"><a name="p1158961516050"></a><a name="p1158961516050"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3719767816050"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p6022194016050"><a name="p6022194016050"></a><a name="p6022194016050"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p4613894216050"><a name="p4613894216050"></a><a name="p4613894216050"></a>The job has been successfully added.</p>
</td>
</tr>
</tbody>
</table>

For the description about error status codes, see  [Status Codes](status-codes.md).

