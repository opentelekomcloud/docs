# Querying Operation Logs<a name="EN-US_TOPIC_0125375892"></a>

The  **Operation Logs**  page records cluster and job operations. Logs are typically used to quickly locate faults in case of cluster exceptions, helping you resolve problems.

## Operation Types<a name="section42049383165922"></a>

Currently, only after Kerberos authentication is disabled, two types of operations are recorded in the logs. You can filter and search for a desired type of operations.

-   Cluster: Creating, terminating, shrinking, and expanding a cluster
-   Job: Creating, stopping, and deleting a job

## Log Parameters<a name="section57726380165938"></a>

Logs are listed in chronological order by default in the log list, with the most recent logs displayed at the top.

[Table 1](#table5924273517010)  describes parameters in logs.

**Table  1**  Description of parameters in logs

<a name="table5924273517010"></a>
<table><thead align="left"><tr id="row2217974117010"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.3.1.1"><p id="p37124417010"><a name="p37124417010"></a><a name="p37124417010"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="80%" id="mcps1.2.3.1.2"><p id="p5559965417010"><a name="p5559965417010"></a><a name="p5559965417010"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row595250417010"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p6693723117010"><a name="p6693723117010"></a><a name="p6693723117010"></a>Operation Type</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p234869017010"><a name="p234869017010"></a><a name="p234869017010"></a>Operation type</p>
<p id="p50755714446"><a name="p50755714446"></a><a name="p50755714446"></a>Possible types include:</p>
<a name="ul2977561517418"></a><a name="ul2977561517418"></a><ul id="ul2977561517418"><li>Cluster</li><li>Job</li></ul>
</td>
</tr>
<tr id="row431321819572"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p1382637719572"><a name="p1382637719572"></a><a name="p1382637719572"></a>IP Address</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p4619474419572"><a name="p4619474419572"></a><a name="p4619474419572"></a>IP address where an operation is executed</p>
<div class="note" id="note48964576112218"><a name="note48964576112218"></a><a name="note48964576112218"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p38028006112218"><a name="p38028006112218"></a><a name="p38028006112218"></a>If MRS cluster deployment fails, the cluster is automatically terminated, and the operation log of the terminated cluster does not contain the user's <span class="parmname" id="parmname3839760101855"><a name="parmname3839760101855"></a><a name="parmname3839760101855"></a><b>IP Address</b></span> information.</p>
</div></div>
</td>
</tr>
<tr id="row1556529017010"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p459724117010"><a name="p459724117010"></a><a name="p459724117010"></a>Operation Details</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p37625132141041"><a name="p37625132141041"></a><a name="p37625132141041"></a>Operation content</p>
<p id="p4481421617010"><a name="p4481421617010"></a><a name="p4481421617010"></a>The content can contain a maximum of 2048 characters.</p>
</td>
</tr>
<tr id="row3264057817010"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p4623164717010"><a name="p4623164717010"></a><a name="p4623164717010"></a>Operation Time</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p4405646714114"><a name="p4405646714114"></a><a name="p4405646714114"></a>Operation time</p>
<p id="p5272923141210"><a name="p5272923141210"></a><a name="p5272923141210"></a>For terminated clusters, only those terminated within the last six months are displayed. If you want to view clusters terminated six months ago, contact technical support engineers.</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  Button description

<a name="table3011042510139"></a>
<table><thead align="left"><tr id="row708755810139"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.3.1.1"><p id="p6655665410139"><a name="p6655665410139"></a><a name="p6655665410139"></a>Button</p>
</th>
<th class="cellrowborder" valign="top" width="80%" id="mcps1.2.3.1.2"><p id="p2237991710139"><a name="p2237991710139"></a><a name="p2237991710139"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row9266410139"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p750586110139"><a name="p750586110139"></a><a name="p750586110139"></a><a name="image6147517310551"></a><a name="image6147517310551"></a><span><img id="image6147517310551" src="figures/icon_mrs_cluster_state.jpg"></span></p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p5344702710412"><a name="p5344702710412"></a><a name="p5344702710412"></a>In the drop-down list, select an operation type to filter logs.</p>
<a name="ul1294383513519"></a><a name="ul1294383513519"></a><ul id="ul1294383513519"><li>All: displays all logs.</li><li>Cluster: displays logs of <span class="parmname" id="parmname38069190102037"><a name="parmname38069190102037"></a><a name="parmname38069190102037"></a><b>Clusters</b></span>.</li><li>Job: displays logs of <span class="parmname" id="parmname13142044102056"><a name="parmname13142044102056"></a><a name="parmname13142044102056"></a><b>Jobs</b></span>.</li></ul>
</td>
</tr>
<tr id="row63630108154320"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p53765115154320"><a name="p53765115154320"></a><a name="p53765115154320"></a><a name="image53709734154348"></a><a name="image53709734154348"></a><span><img id="image53709734154348" src="figures/icon_mrs_time-dt.jpg"></span></p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p60007083154320"><a name="p60007083154320"></a><a name="p60007083154320"></a>Filter logs by time.</p>
<a name="ol2595430715486"></a><a name="ol2595430715486"></a><ol id="ol2595430715486"><li>Click the button.</li><li>Specify the date and time.</li><li>Click <span class="uicontrol" id="uicontrol44366937155920"><a name="uicontrol44366937155920"></a><a name="uicontrol44366937155920"></a><b>OK</b></span>.</li></ol>
<p id="p57734443154828"><a name="p57734443154828"></a><a name="p57734443154828"></a>Enter the query start time in the left box and end time in the right box. The end time must be later than the start time. Otherwise, logs cannot be filtered by time.</p>
</td>
</tr>
<tr id="row3595494810139"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p2666966910139"><a name="p2666966910139"></a><a name="p2666966910139"></a><a name="image63573541154216"></a><a name="image63573541154216"></a><span><img id="image63573541154216" src="figures/icon_mrs_search_l.png"></span></p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p1275954610139"><a name="p1275954610139"></a><a name="p1275954610139"></a>Enter key words in <span class="parmname" id="parmname10790254155939"><a name="parmname10790254155939"></a><a name="parmname10790254155939"></a><b>Operation Details</b></span>&nbsp;and click&nbsp;<a name="image20607779154221"></a><a name="image20607779154221"></a><span><img id="image20607779154221" src="figures/icon_mrs_search_l.png"></span> to search for logs.</p>
</td>
</tr>
<tr id="row4772705110139"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p4068596210139"><a name="p4068596210139"></a><a name="p4068596210139"></a><a name="image2384057154134"></a><a name="image2384057154134"></a><span><img id="image2384057154134" src="figures/icon_mrs_fresh_r.png"></span></p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p722865810139"><a name="p722865810139"></a><a name="p722865810139"></a>Click <a name="image46828546154136"></a><a name="image46828546154136"></a><span><img id="image46828546154136" src="figures/icon_mrs_fresh_r.png"></span> to manually refresh the log list.</p>
</td>
</tr>
</tbody>
</table>

