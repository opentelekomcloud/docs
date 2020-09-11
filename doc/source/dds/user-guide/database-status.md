# Database Status<a name="en-us_topic_0044018318"></a>

## DB Instance Status<a name="section66452380182814"></a>

**Table  1**  Status and description

<a name="table3431324515552"></a>
<table><thead align="left"><tr id="row4108828815552"><th class="cellrowborder" valign="top" width="22.56%" id="mcps1.2.3.1.1"><p id="p3561062515552"><a name="p3561062515552"></a><a name="p3561062515552"></a><strong id="b84235270615330"><a name="b84235270615330"></a><a name="b84235270615330"></a>Status</strong></p>
</th>
<th class="cellrowborder" valign="top" width="77.44%" id="mcps1.2.3.1.2"><p id="p62334861173026"><a name="p62334861173026"></a><a name="p62334861173026"></a><strong id="b32665571155026"><a name="b32665571155026"></a><a name="b32665571155026"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row5206017615552"><td class="cellrowborder" valign="top" width="22.56%" headers="mcps1.2.3.1.1 "><p id="p4980985015552"><a name="p4980985015552"></a><a name="p4980985015552"></a>Available</p>
</td>
<td class="cellrowborder" valign="top" width="77.44%" headers="mcps1.2.3.1.2 "><p id="p15958982173026"><a name="p15958982173026"></a><a name="p15958982173026"></a>A DB instance is running properly.</p>
</td>
</tr>
<tr id="row3979773815552"><td class="cellrowborder" valign="top" width="22.56%" headers="mcps1.2.3.1.1 "><p id="p5947899315552"><a name="p5947899315552"></a><a name="p5947899315552"></a>Abnormal</p>
</td>
<td class="cellrowborder" valign="top" width="77.44%" headers="mcps1.2.3.1.2 "><p id="p17059123173026"><a name="p17059123173026"></a><a name="p17059123173026"></a>A DB instance is faulty.</p>
</td>
</tr>
<tr id="row163765563364"><td class="cellrowborder" valign="top" width="22.56%" headers="mcps1.2.3.1.1 "><p id="p195281216378"><a name="p195281216378"></a><a name="p195281216378"></a>Creating</p>
</td>
<td class="cellrowborder" valign="top" width="77.44%" headers="mcps1.2.3.1.2 "><p id="p1153116263714"><a name="p1153116263714"></a><a name="p1153116263714"></a>A DB instance is being created.</p>
</td>
</tr>
<tr id="row95881945153619"><td class="cellrowborder" valign="top" width="22.56%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0086557181_p36127048165022"><a name="en-us_topic_0086557181_p36127048165022"></a><a name="en-us_topic_0086557181_p36127048165022"></a>Creation failed</p>
</td>
<td class="cellrowborder" valign="top" width="77.44%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0086557181_p40609790165022"><a name="en-us_topic_0086557181_p40609790165022"></a><a name="en-us_topic_0086557181_p40609790165022"></a>A DB instance fails to be created.</p>
</td>
</tr>
<tr id="row257957321645"><td class="cellrowborder" valign="top" width="22.56%" headers="mcps1.2.3.1.1 "><p id="p2552515716418"><a name="p2552515716418"></a><a name="p2552515716418"></a>Restarting</p>
</td>
<td class="cellrowborder" valign="top" width="77.44%" headers="mcps1.2.3.1.2 "><p id="p5427184316418"><a name="p5427184316418"></a><a name="p5427184316418"></a>A DB instance is being restarted because of a customer request or a modification that requires restarting it for the modification to take effect.</p>
</td>
</tr>
<tr id="row163371537142018"><td class="cellrowborder" valign="top" width="22.56%" headers="mcps1.2.3.1.1 "><p id="p183371837102012"><a name="p183371837102012"></a><a name="p183371837102012"></a>Switchover in progress</p>
</td>
<td class="cellrowborder" valign="top" width="77.44%" headers="mcps1.2.3.1.2 "><p id="p11337537192016"><a name="p11337537192016"></a><a name="p11337537192016"></a>The primary and secondary nodes of a replica set instance are being switched.</p>
</td>
</tr>
<tr id="row288815261649"><td class="cellrowborder" valign="top" width="22.56%" headers="mcps1.2.3.1.1 "><p id="p3705337016418"><a name="p3705337016418"></a><a name="p3705337016418"></a>Adding node</p>
</td>
<td class="cellrowborder" valign="top" width="77.44%" headers="mcps1.2.3.1.2 "><p id="p4853295616418"><a name="p4853295616418"></a><a name="p4853295616418"></a>shards or mongos are being added to a DDS cluster instance.</p>
</td>
</tr>
<tr id="row94605376467"><td class="cellrowborder" valign="top" width="22.56%" headers="mcps1.2.3.1.1 "><p id="p8941164220460"><a name="p8941164220460"></a><a name="p8941164220460"></a>Deleting node</p>
</td>
<td class="cellrowborder" valign="top" width="77.44%" headers="mcps1.2.3.1.2 "><p id="p4943342164611"><a name="p4943342164611"></a><a name="p4943342164611"></a>The node that failed to be added is being deleted.</p>
</td>
</tr>
<tr id="row3852395216416"><td class="cellrowborder" valign="top" width="22.56%" headers="mcps1.2.3.1.1 "><p id="p1415409816418"><a name="p1415409816418"></a><a name="p1415409816418"></a>Scaling up</p>
</td>
<td class="cellrowborder" valign="top" width="77.44%" headers="mcps1.2.3.1.2 "><p id="p563129916418"><a name="p563129916418"></a><a name="p563129916418"></a>The storage space of instance nodes is being expanded.</p>
</td>
</tr>
<tr id="row12762730145350"><td class="cellrowborder" valign="top" width="22.56%" headers="mcps1.2.3.1.1 "><p id="p27148218145350"><a name="p27148218145350"></a><a name="p27148218145350"></a>Changing instance class</p>
</td>
<td class="cellrowborder" valign="top" width="77.44%" headers="mcps1.2.3.1.2 "><p id="p51522030145350"><a name="p51522030145350"></a><a name="p51522030145350"></a>The CPU or memory of a DB instance is being changed.</p>
</td>
</tr>
<tr id="row1403128316412"><td class="cellrowborder" valign="top" width="22.56%" headers="mcps1.2.3.1.1 "><p id="p1157664416418"><a name="p1157664416418"></a><a name="p1157664416418"></a>Backing up</p>
</td>
<td class="cellrowborder" valign="top" width="77.44%" headers="mcps1.2.3.1.2 "><p id="p6529295716418"><a name="p6529295716418"></a><a name="p6529295716418"></a>A backup file is being created.</p>
</td>
</tr>
<tr id="row4589286816712"><td class="cellrowborder" valign="top" width="22.56%" headers="mcps1.2.3.1.1 "><p id="p2633482216712"><a name="p2633482216712"></a><a name="p2633482216712"></a>Checking restoration</p>
</td>
<td class="cellrowborder" valign="top" width="77.44%" headers="mcps1.2.3.1.2 "><p id="p5274582416712"><a name="p5274582416712"></a><a name="p5274582416712"></a>The backup of the current DB instance is being restored to a new DB instance.</p>
</td>
</tr>
<tr id="row29249273161157"><td class="cellrowborder" valign="top" width="22.56%" headers="mcps1.2.3.1.1 "><p id="p20380874161157"><a name="p20380874161157"></a><a name="p20380874161157"></a>Switching SSL</p>
</td>
<td class="cellrowborder" valign="top" width="77.44%" headers="mcps1.2.3.1.2 "><p id="p40238092161157"><a name="p40238092161157"></a><a name="p40238092161157"></a>The SSL channel is being enabled or disabled.</p>
</td>
</tr>
<tr id="row2292112131110"><td class="cellrowborder" valign="top" width="22.56%" headers="mcps1.2.3.1.1 "><p id="p1629441251115"><a name="p1629441251115"></a><a name="p1629441251115"></a>Changing private IP address</p>
</td>
<td class="cellrowborder" valign="top" width="77.44%" headers="mcps1.2.3.1.2 "><p id="p66926164155046"><a name="p66926164155046"></a><a name="p66926164155046"></a>The private IP address of a node is being changed.</p>
</td>
</tr>
<tr id="row18876115161233"><td class="cellrowborder" valign="top" width="22.56%" headers="mcps1.2.3.1.1 "><p id="p52570329161233"><a name="p52570329161233"></a><a name="p52570329161233"></a>Changing port</p>
</td>
<td class="cellrowborder" valign="top" width="77.44%" headers="mcps1.2.3.1.2 "><p id="p6472021161358"><a name="p6472021161358"></a><a name="p6472021161358"></a>The DB instance port is being changed.</p>
</td>
</tr>
<tr id="row4632247104013"><td class="cellrowborder" valign="top" width="22.56%" headers="mcps1.2.3.1.1 "><p id="p56321147194018"><a name="p56321147194018"></a><a name="p56321147194018"></a>Changing a security group</p>
</td>
<td class="cellrowborder" valign="top" width="77.44%" headers="mcps1.2.3.1.2 "><p id="p763234754019"><a name="p763234754019"></a><a name="p763234754019"></a>The security group is being changed.</p>
</td>
</tr>
</tbody>
</table>

## Parameter Group Status<a name="section3874184714358"></a>

**Table  2**  Status and description

<a name="table6382756214358"></a>
<table><thead align="left"><tr id="row2110192914358"><th class="cellrowborder" valign="top" width="23.49%" id="mcps1.2.3.1.1"><p id="p5678134514358"><a name="p5678134514358"></a><a name="p5678134514358"></a><strong id="b84235270620453"><a name="b84235270620453"></a><a name="b84235270620453"></a>Status</strong></p>
</th>
<th class="cellrowborder" valign="top" width="76.51%" id="mcps1.2.3.1.2"><p id="p3588621014358"><a name="p3588621014358"></a><a name="p3588621014358"></a><strong id="b33255568155026"><a name="b33255568155026"></a><a name="b33255568155026"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row222202214358"><td class="cellrowborder" valign="top" width="23.49%" headers="mcps1.2.3.1.1 "><p id="p3153465114358"><a name="p3153465114358"></a><a name="p3153465114358"></a>In-Sync</p>
</td>
<td class="cellrowborder" valign="top" width="76.51%" headers="mcps1.2.3.1.2 "><p id="p416995414358"><a name="p416995414358"></a><a name="p416995414358"></a>A database parameter change has taken effect.</p>
</td>
</tr>
<tr id="row1573708414358"><td class="cellrowborder" valign="top" width="23.49%" headers="mcps1.2.3.1.1 "><p id="p2628951614358"><a name="p2628951614358"></a><a name="p2628951614358"></a>Pending restart</p>
</td>
<td class="cellrowborder" valign="top" width="76.51%" headers="mcps1.2.3.1.2 "><p id="p4907605014358"><a name="p4907605014358"></a><a name="p4907605014358"></a>A database parameter is waiting for the DB instance to be restarted before its modification takes effect.</p>
</td>
</tr>
</tbody>
</table>

