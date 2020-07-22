# Reading Job Progress<a name="cce_02_0247"></a>

## Function<a name="section1686113493165"></a>

This API is used to query the progress of a job with a specified job ID returned after a job request is issued.

## URI<a name="section8403243161416"></a>

GET /api/v3/projects/\{project\_id\}/jobs/\{job\_id\}

[Table 1](#table2027961241820)  describes the parameters of the API.

**Table  1**  Parameter description

<a name="table2027961241820"></a>
<table><thead align="left"><tr id="row122809120186"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="p91421758131813"><a name="p91421758131813"></a><a name="p91421758131813"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.4.1.2"><p id="p101421758131816"><a name="p101421758131816"></a><a name="p101421758131816"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.2.4.1.3"><p id="p19143115818187"><a name="p19143115818187"></a><a name="p19143115818187"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row32801312121810"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p1714415589184"><a name="p1714415589184"></a><a name="p1714415589184"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p814518580186"><a name="p814518580186"></a><a name="p814518580186"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.4.1.3 "><p id="p5145175891811"><a name="p5145175891811"></a><a name="p5145175891811"></a>Project ID. For details about how to obtain the project ID, see <a href="how-to-obtain-parameters-in-the-api-uri.md">How to Obtain Parameters in the API URI</a>.</p>
</td>
</tr>
<tr id="row1649094164612"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p749015414462"><a name="p749015414462"></a><a name="p749015414462"></a>job_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p1849084134615"><a name="p1849084134615"></a><a name="p1849084134615"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.4.1.3 "><p id="p8491141114617"><a name="p8491141114617"></a><a name="p8491141114617"></a>Job ID. For details about how to obtain the job ID, see <a href="how-to-obtain-parameters-in-the-api-uri.md">How to Obtain Parameters in the API URI</a>.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section947084713911"></a>

**Request parameters**:

[Table 2](#table189325395020)  describes the request parameters.

**Table  2**  Parameters in the request header

<a name="table189325395020"></a>
<table><thead align="left"><tr id="en-us_topic_0102499074_row55001954122614"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="en-us_topic_0102499074_p115009545264"><a name="en-us_topic_0102499074_p115009545264"></a><a name="en-us_topic_0102499074_p115009545264"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18.95%" id="mcps1.2.4.1.2"><p id="en-us_topic_0102499074_p175001547265"><a name="en-us_topic_0102499074_p175001547265"></a><a name="en-us_topic_0102499074_p175001547265"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="61.050000000000004%" id="mcps1.2.4.1.3"><p id="en-us_topic_0102499074_p16500154162611"><a name="en-us_topic_0102499074_p16500154162611"></a><a name="en-us_topic_0102499074_p16500154162611"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0102499074_row199801811203412"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0102499074_p69808112344"><a name="en-us_topic_0102499074_p69808112344"></a><a name="en-us_topic_0102499074_p69808112344"></a>Content-Type</p>
</td>
<td class="cellrowborder" valign="top" width="18.95%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0102499074_p3980111103414"><a name="en-us_topic_0102499074_p3980111103414"></a><a name="en-us_topic_0102499074_p3980111103414"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="61.050000000000004%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0102499074_p169801011203416"><a name="en-us_topic_0102499074_p169801011203416"></a><a name="en-us_topic_0102499074_p169801011203416"></a>Message body type (format). Possible values:</p>
<a name="en-us_topic_0102499074_ul7385444163617"></a><a name="en-us_topic_0102499074_ul7385444163617"></a><ul id="en-us_topic_0102499074_ul7385444163617"><li>application/json;charset=utf-8</li><li>application/json</li></ul>
</td>
</tr>
<tr id="en-us_topic_0102499074_row3500125412260"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0102499074_p105001654202618"><a name="en-us_topic_0102499074_p105001654202618"></a><a name="en-us_topic_0102499074_p105001654202618"></a>X-Auth-Token</p>
</td>
<td class="cellrowborder" valign="top" width="18.95%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0102499074_p20500954182618"><a name="en-us_topic_0102499074_p20500954182618"></a><a name="en-us_topic_0102499074_p20500954182618"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="61.050000000000004%" headers="mcps1.2.4.1.3 "><p id="p18824197845"><a name="p18824197845"></a><a name="p18824197845"></a>Requests for calling an API can be authenticated using either a token or AK/SK. If token-based authentication is used, this parameter is mandatory and must be set to a user token. For details on how to obtain a user token, see <a href="api-usage-guidelines.md">API Usage Guidelines</a>.</p>
</td>
</tr>
</tbody>
</table>

**Example request**:

N/A

## Response<a name="section61819725020"></a>

**Response parameters**:

[Table 3](#en-us_topic_0079616779_en-us_topic_0079614912_ref458774242)  describes the response parameters.

**Table  3**  Response parameters

<a name="en-us_topic_0079616779_en-us_topic_0079614912_ref458774242"></a>
<table><thead align="left"><tr id="en-us_topic_0079616779_en-us_topic_0079614912_row38450714"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="en-us_topic_0079616779_en-us_topic_0079614912_p27500114"><a name="en-us_topic_0079616779_en-us_topic_0079614912_p27500114"></a><a name="en-us_topic_0079616779_en-us_topic_0079614912_p27500114"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="27%" id="mcps1.2.4.1.2"><p id="p1654581422214"><a name="p1654581422214"></a><a name="p1654581422214"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48%" id="mcps1.2.4.1.3"><p id="p125451914132219"><a name="p125451914132219"></a><a name="p125451914132219"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0079616779_en-us_topic_0079614912_row48220637"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p108391536181311"><a name="p108391536181311"></a><a name="p108391536181311"></a>kind</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.2 "><p id="p1056311621716"><a name="p1056311621716"></a><a name="p1056311621716"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p75781816181715"><a name="p75781816181715"></a><a name="p75781816181715"></a>API type. The value is fixed at <strong id="b1066504758171451"><a name="b1066504758171451"></a><a name="b1066504758171451"></a>Job</strong>.</p>
</td>
</tr>
<tr id="row1698782994313"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1785493610136"><a name="p1785493610136"></a><a name="p1785493610136"></a>apiVersion</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.2 "><p id="p757801610179"><a name="p757801610179"></a><a name="p757801610179"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p12578616151718"><a name="p12578616151718"></a><a name="p12578616151718"></a>API version. The value is fixed at <strong id="b1814506129171446"><a name="b1814506129171446"></a><a name="b1814506129171446"></a>v3</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0079616779_en-us_topic_0079614912_row28135397"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1185493615135"><a name="p1185493615135"></a><a name="p1185493615135"></a>metadata</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.2 "><p id="p734131363510"><a name="p734131363510"></a><a name="p734131363510"></a><a href="#table13456192212">metadata</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p10343195011177"><a name="p10343195011177"></a><a name="p10343195011177"></a>Node metadata.</p>
</td>
</tr>
<tr id="row12484123982118"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p6532732161518"><a name="p6532732161518"></a><a name="p6532732161518"></a>spec</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.2 "><p id="p5359350141715"><a name="p5359350141715"></a><a name="p5359350141715"></a><a href="#table620623542313">spec</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p173598507179"><a name="p173598507179"></a><a name="p173598507179"></a>Detailed node parameters.</p>
</td>
</tr>
<tr id="row1482918413216"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p15204203610152"><a name="p15204203610152"></a><a name="p15204203610152"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.2 "><p id="p1920413611513"><a name="p1920413611513"></a><a name="p1920413611513"></a><a href="#table5445161610255">status</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p9204133661512"><a name="p9204133661512"></a><a name="p9204133661512"></a>Node status.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  Data structure of the  **metadata**  field

<a name="table13456192212"></a>
<table><thead align="left"><tr id="row031056182217"><th class="cellrowborder" valign="top" width="25.252525252525253%" id="mcps1.2.4.1.1"><p id="p1225365992218"><a name="p1225365992218"></a><a name="p1225365992218"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="26.262626262626267%" id="mcps1.2.4.1.2"><p id="p1526815942214"><a name="p1526815942214"></a><a name="p1526815942214"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.484848484848484%" id="mcps1.2.4.1.3"><p id="p112681259142219"><a name="p112681259142219"></a><a name="p112681259142219"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row6345613224"><td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.2.4.1.1 "><p id="p103256202220"><a name="p103256202220"></a><a name="p103256202220"></a>uid</p>
</td>
<td class="cellrowborder" valign="top" width="26.262626262626267%" headers="mcps1.2.4.1.2 "><p id="p3305622213"><a name="p3305622213"></a><a name="p3305622213"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.4.1.3 "><p id="p73185662212"><a name="p73185662212"></a><a name="p73185662212"></a>Job ID.</p>
</td>
</tr>
<tr id="row10311567226"><td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.2.4.1.1 "><p id="p133756162217"><a name="p133756162217"></a><a name="p133756162217"></a>creationTimestamp</p>
</td>
<td class="cellrowborder" valign="top" width="26.262626262626267%" headers="mcps1.2.4.1.2 "><p id="p831856162219"><a name="p831856162219"></a><a name="p831856162219"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.4.1.3 "><p id="p173145615222"><a name="p173145615222"></a><a name="p173145615222"></a>Job creation time.</p>
</td>
</tr>
<tr id="row10365619222"><td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.2.4.1.1 "><p id="p1931356152218"><a name="p1931356152218"></a><a name="p1931356152218"></a>updateTimestamp</p>
</td>
<td class="cellrowborder" valign="top" width="26.262626262626267%" headers="mcps1.2.4.1.2 "><p id="p73356202217"><a name="p73356202217"></a><a name="p73356202217"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.4.1.3 "><p id="p1330568223"><a name="p1330568223"></a><a name="p1330568223"></a>Job update time.</p>
</td>
</tr>
</tbody>
</table>

**Table  5**  Data structure of the  **spec**  field

<a name="table620623542313"></a>
<table><thead align="left"><tr id="row520663552315"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p208332952414"><a name="p208332952414"></a><a name="p208332952414"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.2"><p id="p1184914917244"><a name="p1184914917244"></a><a name="p1184914917244"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49%" id="mcps1.2.4.1.3"><p id="p118491295245"><a name="p118491295245"></a><a name="p118491295245"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row12206153513232"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p6206135142317"><a name="p6206135142317"></a><a name="p6206135142317"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="p1320643516238"><a name="p1320643516238"></a><a name="p1320643516238"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.4.1.3 "><p id="p19206135162314"><a name="p19206135162314"></a><a name="p19206135162314"></a>Job type, for example, <strong id="b119911581564"><a name="b119911581564"></a><a name="b119911581564"></a>CreateCluster</strong>.</p>
</td>
</tr>
<tr id="row12206143515238"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p11206235122312"><a name="p11206235122312"></a><a name="p11206235122312"></a>clusterUID</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="p132061435132316"><a name="p132061435132316"></a><a name="p132061435132316"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.4.1.3 "><p id="p6206173582312"><a name="p6206173582312"></a><a name="p6206173582312"></a>ID of the cluster where the job runs.</p>
</td>
</tr>
<tr id="row9206123518238"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p12061135112315"><a name="p12061135112315"></a><a name="p12061135112315"></a>resourceID</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="p1920643502317"><a name="p1920643502317"></a><a name="p1920643502317"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.4.1.3 "><p id="p18206113582316"><a name="p18206113582316"></a><a name="p18206113582316"></a>ID of the resource on which a job is executed.</p>
</td>
</tr>
<tr id="row72396288246"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p823992812416"><a name="p823992812416"></a><a name="p823992812416"></a>resourceName</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="p023912892419"><a name="p023912892419"></a><a name="p023912892419"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.4.1.3 "><p id="p99811242122710"><a name="p99811242122710"></a><a name="p99811242122710"></a>Name of the resource on which a job is executed.</p>
</td>
</tr>
<tr id="row177561327249"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p175620323246"><a name="p175620323246"></a><a name="p175620323246"></a>extendParam</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="p4756193242414"><a name="p4756193242414"></a><a name="p4756193242414"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.4.1.3 "><p id="p1275643219249"><a name="p1275643219249"></a><a name="p1275643219249"></a>Extended parameter.</p>
</td>
</tr>
<tr id="row18896173620241"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1689693612416"><a name="p1689693612416"></a><a name="p1689693612416"></a>subJobs</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="p88941746133512"><a name="p88941746133512"></a><a name="p88941746133512"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.4.1.3 "><p id="p1089603642417"><a name="p1089603642417"></a><a name="p1089603642417"></a>List of sub-jobs. For details, see <a href="#en-us_topic_0079616779_en-us_topic_0079614912_ref458774242">Table 3</a>.</p>
<a name="ul725172425411"></a><a name="ul725172425411"></a><ul id="ul725172425411"><li>The sub-job list contains details about all sub-jobs.</li><li>Usually, a cluster/node creation job consists of multiple sub-jobs. The job is complete only after all sub-jobs are complete.</li></ul>
</td>
</tr>
</tbody>
</table>

**Table  6**  Data structure of the  **status**  field

<a name="table5445161610255"></a>
<table><thead align="left"><tr id="row184611916162519"><th class="cellrowborder" valign="top" width="25.47524752475247%" id="mcps1.2.4.1.1"><p id="p19320122372514"><a name="p19320122372514"></a><a name="p19320122372514"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="26.009900990099013%" id="mcps1.2.4.1.2"><p id="p103201823182517"><a name="p103201823182517"></a><a name="p103201823182517"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.51485148514851%" id="mcps1.2.4.1.3"><p id="p12336122362513"><a name="p12336122362513"></a><a name="p12336122362513"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row6461141613257"><td class="cellrowborder" valign="top" width="25.47524752475247%" headers="mcps1.2.4.1.1 "><p id="p6461916102517"><a name="p6461916102517"></a><a name="p6461916102517"></a>phase</p>
</td>
<td class="cellrowborder" valign="top" width="26.009900990099013%" headers="mcps1.2.4.1.2 "><p id="p11461131692514"><a name="p11461131692514"></a><a name="p11461131692514"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.2.4.1.3 "><p id="p1346114167250"><a name="p1346114167250"></a><a name="p1346114167250"></a>Job status. The options are as follows:</p>
<a name="ul51301755102811"></a><a name="ul51301755102811"></a><ul id="ul51301755102811"><li>JobPhaseInitializing JobPhase = "Initializing"</li><li>JobPhaseRunning JobPhase = "Running"</li><li>JobPhaseFailed JobPhase = "Failed"</li><li>JobPhaseSuccess JobPhase = "Success"</li></ul>
</td>
</tr>
<tr id="row1646161615257"><td class="cellrowborder" valign="top" width="25.47524752475247%" headers="mcps1.2.4.1.1 "><p id="p946118163258"><a name="p946118163258"></a><a name="p946118163258"></a>reason</p>
</td>
<td class="cellrowborder" valign="top" width="26.009900990099013%" headers="mcps1.2.4.1.2 "><p id="p1446161618259"><a name="p1446161618259"></a><a name="p1446161618259"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.2.4.1.3 "><p id="p15461171652519"><a name="p15461171652519"></a><a name="p15461171652519"></a>Reason why the job is in the current state.</p>
</td>
</tr>
</tbody>
</table>

**Example response**:

```
{
    "kind": "Job",
    "apiVersion": "v3",
    "metadata": {
        "uid": "354331b2c-229a-11e8-9c75-0255ac100ceb",
        "creationTimestamp": "2020-02-02 08:12:40.672772389 +0000 UTC",
        "updateTimestamp": "2020-02-02 08:21:50.478108569 +0000 UTC"
    },
    "spec": {
        "type": "CreateCluster",
        "clusterUID": "4d1ecb2c-229a-11e8-9c75-0255ac100ceb",
        "resourceID": "6f4dcb2c-229a-11e8-9c75-0255ac100ceb",
        "resourceName": "cluster-name",
        "extendParam": {
            "serverID": "bc467e3a-2338-11e8-825b-0255ac100c13"
        },
        "subJobs": [
            {
                "kind": "Job",
                "apiVersion": "v3",
                "metadata": {
                    "uid": "fd474fab-9606-11e8-baa9-0255ac10215d",
                    "creationTimestamp": "2020-02-02 03:52:34.615819618 +0000 UTC",
                    "updateTimestamp": "2020-02-02 04:05:29.196243031 +0000 UTC"
                },
                "spec": {
                    "type": "InstallMaster",
                    "clusterUID": "fcc72de0-9606-11e8-baa8-0255ac10215d",
                    "resourceID": "fd3b4ac0-9606-11e8-baa8-0255ac10215d",
                    "extendParam": {
                        "serverID": "fd3b4ac0-9606-11e8-baa8-0255ac10215d"
                    }
                },
                "status": {
                    "phase": "Success"
                }
            },
            {
                "kind": "Job",
                "apiVersion": "v3",
                "metadata": {
                    "uid": "fd474f82-9606-11e8-baa8-0255ac10215d",
                    "creationTimestamp": "2020-02-02 03:52:33.859150791 +0000 UTC",
                    "updateTimestamp": "2020-02-02 03:52:34.615655429 +0000 UTC"
                },
                "spec": {
                    "type": "CreatePSMCert",
                    "clusterUID": "fcc72de0-9606-11e8-baa8-0255ac10215d"
                },
                "status": {
                    "phase": "Success"
                }
            }
        ],       
    },
    "status": {
        "phase": "Running",
        "reason": ""        
    }
}
```

## Status Code<a name="s50f1049a6a4d404c895cf636eb8f3bf1"></a>

[Table 7](#en-us_topic_0079614900_table46761928)  describes the status code of this API.

**Table  7**  Status code

<a name="en-us_topic_0079614900_table46761928"></a>
<table><thead align="left"><tr id="en-us_topic_0079614900_row33254664"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p55616028205955"><a name="p55616028205955"></a><a name="p55616028205955"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p8604418205955"><a name="p8604418205955"></a><a name="p8604418205955"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0079614900_row41084259"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0079614900_p39490674"><a name="en-us_topic_0079614900_p39490674"></a><a name="en-us_topic_0079614900_p39490674"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0079614900_p44628050"><a name="en-us_topic_0079614900_p44628050"></a><a name="en-us_topic_0079614900_p44628050"></a>The progress of the specified job is successfully obtained.</p>
</td>
</tr>
</tbody>
</table>

For details about error status codes, see  [Status Code](status-code.md).

