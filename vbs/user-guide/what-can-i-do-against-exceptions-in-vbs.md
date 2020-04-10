# What Can I Do Against Exceptions in VBS?<a name="EN-US_TOPIC_0046276032"></a>

Exceptions in VBS mainly include abnormal states of VBS backups and backup jobs. Take the following measures to handle these exceptions.

**Table  1**  Measures against abnormal VBS backup states

<a name="table1547142735417"></a>
<table><thead align="left"><tr id="row15471227165418"><th class="cellrowborder" valign="top" width="15.409999999999998%" id="mcps1.2.3.1.1"><p id="p114711278542"><a name="p114711278542"></a><a name="p114711278542"></a>State</p>
</th>
<th class="cellrowborder" valign="top" width="84.59%" id="mcps1.2.3.1.2"><p id="p12475277546"><a name="p12475277546"></a><a name="p12475277546"></a>Handling Suggestion</p>
</th>
</tr>
</thead>
<tbody><tr id="row247152795416"><td class="cellrowborder" valign="top" width="15.409999999999998%" headers="mcps1.2.3.1.1 "><p id="p76341841072"><a name="p76341841072"></a><a name="p76341841072"></a>Error</p>
</td>
<td class="cellrowborder" valign="top" width="84.59%" headers="mcps1.2.3.1.2 "><p id="p268911541564"><a name="p268911541564"></a><a name="p268911541564"></a>Delete the VBS backups in the <strong id="b3561193864510"><a name="b3561193864510"></a><a name="b3561193864510"></a>Error</strong> state and re-create them.</p>
</td>
</tr>
<tr id="row1348182765414"><td class="cellrowborder" valign="top" width="15.409999999999998%" headers="mcps1.2.3.1.1 "><p id="p15634641974"><a name="p15634641974"></a><a name="p15634641974"></a>Deletion failed</p>
</td>
<td class="cellrowborder" valign="top" width="84.59%" headers="mcps1.2.3.1.2 "><p id="p1868917541162"><a name="p1868917541162"></a><a name="p1868917541162"></a>Contact the administrator and do not perform any operation on the backup data before related personnel respond. If you want a quick response, contact the administrator immediately upon discovering the problem.</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  Measures against abnormal VBS backup job states

<a name="table16354846105411"></a>
<table><thead align="left"><tr id="row1335417464549"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.3.1.1"><p id="p17452205113540"><a name="p17452205113540"></a><a name="p17452205113540"></a>State</p>
</th>
<th class="cellrowborder" valign="top" width="85%" id="mcps1.2.3.1.2"><p id="p7452451165410"><a name="p7452451165410"></a><a name="p7452451165410"></a>Handling Suggestion</p>
</th>
</tr>
</thead>
<tbody><tr id="row1435410460546"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.3.1.1 "><p id="p17336181195511"><a name="p17336181195511"></a><a name="p17336181195511"></a>Timed out</p>
</td>
<td class="cellrowborder" valign="top" width="85%" headers="mcps1.2.3.1.2 "><a name="ol159291363911"></a><a name="ol159291363911"></a><ol id="ol159291363911"><li>In the <strong id="b7141457185218"><a name="b7141457185218"></a><a name="b7141457185218"></a>Backup Name</strong> column of the backup job list, check whether the backup name is displayed.<a name="ul811204919404"></a><a name="ul811204919404"></a><ul id="ul811204919404"><li>If yes, locate the backup on the VBS backup list according to the backup name. Check whether the backup is in the <strong id="b7141857105215"><a name="b7141857105215"></a><a name="b7141857105215"></a>Available</strong> state. If it is in the <strong id="b911924818282"><a name="b911924818282"></a><a name="b911924818282"></a>Available</strong> state, the backup job is successful and no further actions are required. If no, click <strong id="b158795276217915"><a name="b158795276217915"></a><a name="b158795276217915"></a>Back Up Again</strong> in the <strong id="b69673741817915"><a name="b69673741817915"></a><a name="b69673741817915"></a>Operation</strong> column to perform a manual backup operation.</li><li>If no, click <strong id="b152364406817941"><a name="b152364406817941"></a><a name="b152364406817941"></a>Back Up Again</strong> in the <strong id="b120961540817941"><a name="b120961540817941"></a><a name="b120961540817941"></a>Operation</strong> column to perform a manual backup operation.</li></ul>
</li><li>If the problem persists, contact the administrator and and do not perform any operation on the backup data before related personnel respond. If you want a quick response, contact the administrator immediately upon discovering the problem.</li></ol>
</td>
</tr>
<tr id="row5354246175413"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.3.1.1 "><p id="p1133711119551"><a name="p1133711119551"></a><a name="p1133711119551"></a>Failed</p>
</td>
<td class="cellrowborder" valign="top" width="85%" headers="mcps1.2.3.1.2 "><a name="ol16604721173518"></a><a name="ol16604721173518"></a><ol id="ol16604721173518"><li>Above the VBS backup list, you can see messages indicating the backup usage. If the backup quantity quota is not sufficient to support your new backups, contact the administrator to apply for a higher quota. Then click <strong id="b1214956129171039"><a name="b1214956129171039"></a><a name="b1214956129171039"></a>Back Up Again</strong> in the <strong id="b1112087523171039"><a name="b1112087523171039"></a><a name="b1112087523171039"></a>Operation</strong> column of the <strong id="b48792272171039"><a name="b48792272171039"></a><a name="b48792272171039"></a>Backup Jobs</strong> list to perform a manual backup operation.</li><li>In the EVS list, check whether the EVS disk to be backed up is in the <strong id="b1907207836171056"><a name="b1907207836171056"></a><a name="b1907207836171056"></a>Available</strong> or <strong id="b54318086171056"><a name="b54318086171056"></a><a name="b54318086171056"></a>In-use</strong> state. If no, after the EVS disk restores to the <strong id="b2102072989171243"><a name="b2102072989171243"></a><a name="b2102072989171243"></a>Available</strong> or <strong id="b1594024754171243"><a name="b1594024754171243"></a><a name="b1594024754171243"></a>In-use</strong> state, click <strong id="b1179018228171243"><a name="b1179018228171243"></a><a name="b1179018228171243"></a>Back Up Again</strong> in the <strong id="b225006912171243"><a name="b225006912171243"></a><a name="b225006912171243"></a>Operation</strong> column of the <strong id="b1386574471171243"><a name="b1386574471171243"></a><a name="b1386574471171243"></a>Backup Jobs</strong> list to perform a manual backup operation.</li><li>In the VBS backup list, check whether the EVS disk is in the <strong id="b112587592479"><a name="b112587592479"></a><a name="b112587592479"></a>Disk Name</strong> column and the backup state is <strong id="b132581859104718"><a name="b132581859104718"></a><a name="b132581859104718"></a>Creating</strong>. If yes, after the backup restores to the <strong id="b22583590471"><a name="b22583590471"></a><a name="b22583590471"></a>Available</strong> state, click <strong id="b325918599473"><a name="b325918599473"></a><a name="b325918599473"></a>Back Up Again</strong> in the <strong id="b5259105924714"><a name="b5259105924714"></a><a name="b5259105924714"></a>Operation</strong> column of the <strong id="b72591359104711"><a name="b72591359104711"></a><a name="b72591359104711"></a>Backup Jobs</strong> list to perform a manual backup operation.</li><li>For other circumstances, click <strong id="b0141457145212"><a name="b0141457145212"></a><a name="b0141457145212"></a>Back Up Again</strong> in the <strong id="b414115755215"><a name="b414115755215"></a><a name="b414115755215"></a>Operation</strong> column of the <strong id="b13715169144016"><a name="b13715169144016"></a><a name="b13715169144016"></a>Backup Jobs</strong> list to perform a manual backup operation. If the backup job state is still abnormal, contact the administrator, and do not perform any operation on the backup data before related personnel respond. If you want a quick response, contact the administrator immediately upon discovering the problem.</li></ol>
</td>
</tr>
</tbody>
</table>

