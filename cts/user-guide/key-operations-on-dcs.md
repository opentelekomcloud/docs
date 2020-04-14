# Key Operations on DCS<a name="en-us_topic_0100363624"></a>

Distributed Cache Service \(DCS\) is an online distributed database service that is based on the cloud computing platform, available immediately after it is enabled, stable and reliable, scalable online, and easy to manage.

With CTS, you can record operations associated with DCS for future query, audit, and backtrack operations.

**Table  1**  DCS operations that can be recorded by CTS

<a name="table34008684164042"></a>
<table><thead align="left"><tr id="r3f382d867b4e45a4b4f35010ca1b2f74"><th class="cellrowborder" valign="top" width="34.42%" id="mcps1.2.4.1.1"><p id="a15f5dc2e89ab460a9c575077050730e5"><a name="a15f5dc2e89ab460a9c575077050730e5"></a><a name="a15f5dc2e89ab460a9c575077050730e5"></a>Operation</p>
</th>
<th class="cellrowborder" valign="top" width="23.369999999999997%" id="mcps1.2.4.1.2"><p id="af90a9c51331d4e01a95fbed054a5c871"><a name="af90a9c51331d4e01a95fbed054a5c871"></a><a name="af90a9c51331d4e01a95fbed054a5c871"></a>Resource Type</p>
</th>
<th class="cellrowborder" valign="top" width="42.21%" id="mcps1.2.4.1.3"><p id="a4de707691f4548b5aa6341022c01a2ad"><a name="a4de707691f4548b5aa6341022c01a2ad"></a><a name="a4de707691f4548b5aa6341022c01a2ad"></a>Trace Name</p>
</th>
</tr>
</thead>
<tbody><tr id="r0af60516fa0148a8b38dfe567c9baf64"><td class="cellrowborder" valign="top" width="34.42%" headers="mcps1.2.4.1.1 "><p id="p125551342960"><a name="p125551342960"></a><a name="p125551342960"></a>Creating a DCS instance</p>
</td>
<td class="cellrowborder" valign="top" width="23.369999999999997%" headers="mcps1.2.4.1.2 "><p id="a9a9321d74e6b47f8b0f805a4f273a3dc"><a name="a9a9321d74e6b47f8b0f805a4f273a3dc"></a><a name="a9a9321d74e6b47f8b0f805a4f273a3dc"></a>DCS</p>
</td>
<td class="cellrowborder" valign="top" width="42.21%" headers="mcps1.2.4.1.3 "><p id="p949073571"><a name="p949073571"></a><a name="p949073571"></a>createDCSInstanceSuccess/createDCSInstanceFailure createDCSInstanceTaskSuccess/createDCSInstanceTaskFailure</p>
</td>
</tr>
<tr id="r796843ecfd0e49189cf2739d10ff8fe4"><td class="cellrowborder" valign="top" width="34.42%" headers="mcps1.2.4.1.1 "><p id="p115556427616"><a name="p115556427616"></a><a name="p115556427616"></a>Modifying the information about a DCS instance</p>
</td>
<td class="cellrowborder" valign="top" width="23.369999999999997%" headers="mcps1.2.4.1.2 "><p id="ad53f3f3b00734a8da48cfbb67913ed8f"><a name="ad53f3f3b00734a8da48cfbb67913ed8f"></a><a name="ad53f3f3b00734a8da48cfbb67913ed8f"></a>DCS</p>
</td>
<td class="cellrowborder" valign="top" width="42.21%" headers="mcps1.2.4.1.3 "><p id="p44909314710"><a name="p44909314710"></a><a name="p44909314710"></a>modifyDCSInstanceInfoSuccess/modifyDCSInstanceInfoFailure</p>
</td>
</tr>
<tr id="r0679fff4fe8a42f1a0c2ad3c0a738d49"><td class="cellrowborder" valign="top" width="34.42%" headers="mcps1.2.4.1.1 "><p id="p85551421864"><a name="p85551421864"></a><a name="p85551421864"></a>Deleting a DCS instance</p>
</td>
<td class="cellrowborder" valign="top" width="23.369999999999997%" headers="mcps1.2.4.1.2 "><p id="a13ece91dcfe94fab80aac123ab351fa8"><a name="a13ece91dcfe94fab80aac123ab351fa8"></a><a name="a13ece91dcfe94fab80aac123ab351fa8"></a>DCS</p>
</td>
<td class="cellrowborder" valign="top" width="42.21%" headers="mcps1.2.4.1.3 "><p id="p5490103374"><a name="p5490103374"></a><a name="p5490103374"></a>deleteDCSInstanceSuccess/deleteDCSInstanceFailure</p>
<p id="p1549010312711"><a name="p1549010312711"></a><a name="p1549010312711"></a>batchDeleteDCSInstanceSuccess/batchDeleteDCSInstanceFailure</p>
<p id="p6490239710"><a name="p6490239710"></a><a name="p6490239710"></a>batchDeleteDCSInstanceTaskSuccess/batchDeleteDCSInstanceTaskFailure</p>
</td>
</tr>
<tr id="r277ddc0388804c77ac16f4b97410e2bd"><td class="cellrowborder" valign="top" width="34.42%" headers="mcps1.2.4.1.1 "><p id="p11555194220610"><a name="p11555194220610"></a><a name="p11555194220610"></a>Modifying the configurations of a DCS instance</p>
</td>
<td class="cellrowborder" valign="top" width="23.369999999999997%" headers="mcps1.2.4.1.2 "><p id="ae9228ec107404b68845aa892832c91ca"><a name="ae9228ec107404b68845aa892832c91ca"></a><a name="ae9228ec107404b68845aa892832c91ca"></a>DCS</p>
</td>
<td class="cellrowborder" valign="top" width="42.21%" headers="mcps1.2.4.1.3 "><p id="p1249063278"><a name="p1249063278"></a><a name="p1249063278"></a>modifyDCSInstanceConfigSuccess/modifyDCSInstanceConfigFailure</p>
</td>
</tr>
<tr id="red0b036583e5414a809cc7c5041138a9"><td class="cellrowborder" valign="top" width="34.42%" headers="mcps1.2.4.1.1 "><p id="p1955516421162"><a name="p1955516421162"></a><a name="p1955516421162"></a>Starting a DCS instance</p>
</td>
<td class="cellrowborder" valign="top" width="23.369999999999997%" headers="mcps1.2.4.1.2 "><p id="ab40e52635cbf49a2b7c380236b596a02"><a name="ab40e52635cbf49a2b7c380236b596a02"></a><a name="ab40e52635cbf49a2b7c380236b596a02"></a>DCS</p>
</td>
<td class="cellrowborder" valign="top" width="42.21%" headers="mcps1.2.4.1.3 "><p id="p134901235711"><a name="p134901235711"></a><a name="p134901235711"></a>startDCSInstanceSuccess/startDCSInstanceFailure</p>
<p id="p1549003279"><a name="p1549003279"></a><a name="p1549003279"></a>startDCSInstanceTaskSuccess/startDCSInstanceTaskFailure</p>
<p id="p349063775"><a name="p349063775"></a><a name="p349063775"></a>batchStartDCSInstanceSuccess/batchStartDCSInstanceFailure</p>
<p id="p249063172"><a name="p249063172"></a><a name="p249063172"></a>batchStartDCSInstanceTaskSuccess/batchStartDCSInstanceTaskFailure</p>
</td>
</tr>
<tr id="rb9e63c8d5df74efd84ad1e644bf73835"><td class="cellrowborder" valign="top" width="34.42%" headers="mcps1.2.4.1.1 "><p id="p20556742462"><a name="p20556742462"></a><a name="p20556742462"></a>Stopping a DCS instance</p>
</td>
<td class="cellrowborder" valign="top" width="23.369999999999997%" headers="mcps1.2.4.1.2 "><p id="a06b107a8127a433a86feb58894971786"><a name="a06b107a8127a433a86feb58894971786"></a><a name="a06b107a8127a433a86feb58894971786"></a>DCS</p>
</td>
<td class="cellrowborder" valign="top" width="42.21%" headers="mcps1.2.4.1.3 "><p id="p104901231877"><a name="p104901231877"></a><a name="p104901231877"></a>stopDCSInstanceSuccess/stopDCSInstanceFailure</p>
<p id="p12490131714"><a name="p12490131714"></a><a name="p12490131714"></a>stopDCSInstanceTaskSuccess/stopDCSInstanceTaskFailure</p>
<p id="p7490731372"><a name="p7490731372"></a><a name="p7490731372"></a>batchStopDCSInstanceSuccess/batchStopDCSInstanceFailure</p>
<p id="p17490431078"><a name="p17490431078"></a><a name="p17490431078"></a>batchStopDCSInstanceTaskSuccess/batchStopDCSInstanceTaskFailure</p>
</td>
</tr>
<tr id="re6bca835042949758fab006f0765b74a"><td class="cellrowborder" valign="top" width="34.42%" headers="mcps1.2.4.1.1 "><p id="p205567421762"><a name="p205567421762"></a><a name="p205567421762"></a>Restarting a DCS instance</p>
</td>
<td class="cellrowborder" valign="top" width="23.369999999999997%" headers="mcps1.2.4.1.2 "><p id="a0f87b04fdaad4305a2f2096bbe82167e"><a name="a0f87b04fdaad4305a2f2096bbe82167e"></a><a name="a0f87b04fdaad4305a2f2096bbe82167e"></a>DCS</p>
</td>
<td class="cellrowborder" valign="top" width="42.21%" headers="mcps1.2.4.1.3 "><p id="p7490234710"><a name="p7490234710"></a><a name="p7490234710"></a>restartDCSInstanceSuccess/restartDCSInstanceFailure</p>
<p id="p3490031715"><a name="p3490031715"></a><a name="p3490031715"></a>restartDCSInstanceTaskSuccess/restartDCSInstanceTaskFailure</p>
<p id="p104901539716"><a name="p104901539716"></a><a name="p104901539716"></a>batchRestartDCSInstanceSuccess/batchRestartDCSInstanceFailure</p>
<p id="p184902031079"><a name="p184902031079"></a><a name="p184902031079"></a>batchRestartDCSInstanceTaskSuccess/batchRestartDCSInstanceTaskFailure</p>
</td>
</tr>
<tr id="row161459511510"><td class="cellrowborder" valign="top" width="34.42%" headers="mcps1.2.4.1.1 "><p id="p55561942763"><a name="p55561942763"></a><a name="p55561942763"></a>Changing the password of a DCS instance</p>
</td>
<td class="cellrowborder" valign="top" width="23.369999999999997%" headers="mcps1.2.4.1.2 "><p id="p494116589514"><a name="p494116589514"></a><a name="p494116589514"></a>DCS</p>
</td>
<td class="cellrowborder" valign="top" width="42.21%" headers="mcps1.2.4.1.3 "><p id="p20490834712"><a name="p20490834712"></a><a name="p20490834712"></a>modifyDCSInstancePasswordSuccess/modifyDCSInstancePasswordFailure</p>
</td>
</tr>
<tr id="row17951242851"><td class="cellrowborder" valign="top" width="34.42%" headers="mcps1.2.4.1.1 "><p id="p195567420618"><a name="p195567420618"></a><a name="p195567420618"></a>Scaling up a DCS instance</p>
</td>
<td class="cellrowborder" valign="top" width="23.369999999999997%" headers="mcps1.2.4.1.2 "><p id="p6941125812519"><a name="p6941125812519"></a><a name="p6941125812519"></a>DCS</p>
</td>
<td class="cellrowborder" valign="top" width="42.21%" headers="mcps1.2.4.1.3 "><p id="p04907316713"><a name="p04907316713"></a><a name="p04907316713"></a>extendDCSInstanceSuccess/extendDCSInstanceFailure</p>
<p id="p134911933717"><a name="p134911933717"></a><a name="p134911933717"></a>extendDCSInstanceTaskSuccess/extendDCSInstanceTaskFailure</p>
</td>
</tr>
<tr id="row1398811481059"><td class="cellrowborder" valign="top" width="34.42%" headers="mcps1.2.4.1.1 "><p id="p555614216610"><a name="p555614216610"></a><a name="p555614216610"></a>Backing up a DCS instance</p>
</td>
<td class="cellrowborder" valign="top" width="23.369999999999997%" headers="mcps1.2.4.1.2 "><p id="p7942558553"><a name="p7942558553"></a><a name="p7942558553"></a>DCS</p>
</td>
<td class="cellrowborder" valign="top" width="42.21%" headers="mcps1.2.4.1.3 "><p id="p9491436713"><a name="p9491436713"></a><a name="p9491436713"></a>backupDCSInstanceStartSuccess/backupDCSInstanceStartFailure</p>
<p id="p204912314716"><a name="p204912314716"></a><a name="p204912314716"></a>backupDCSInstanceTaskSuccess/backupDCSInstanceTaskFailure</p>
</td>
</tr>
<tr id="row113815341657"><td class="cellrowborder" valign="top" width="34.42%" headers="mcps1.2.4.1.1 "><p id="p555644216611"><a name="p555644216611"></a><a name="p555644216611"></a>Restoring a DCS Instance</p>
</td>
<td class="cellrowborder" valign="top" width="23.369999999999997%" headers="mcps1.2.4.1.2 "><p id="p1494265814510"><a name="p1494265814510"></a><a name="p1494265814510"></a>DCS</p>
</td>
<td class="cellrowborder" valign="top" width="42.21%" headers="mcps1.2.4.1.3 "><p id="p134913312711"><a name="p134913312711"></a><a name="p134913312711"></a>restoreDCSInstanceStartSuccess/restoreDCSInstanceStartFailure</p>
<p id="p9491431075"><a name="p9491431075"></a><a name="p9491431075"></a>restoreDCSInstanceTaskSuccess/restoreDCSInstanceTaskFailure</p>
</td>
</tr>
</tbody>
</table>

