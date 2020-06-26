# Querying the Target Flavors to Which an ECS Flavor Can Be Changed <a name="EN-US_TOPIC_0110472767"></a>

## Function<a name="section57769674"></a>

An ECS flavor cannot be changed to certain flavors. This API is used to query the target flavors to which a specified ECS flavor can be changed.

## URI<a name="section50165025"></a>

GET /v2.1/\{project\_id\}/resize\_flavors?\{instance\_uuid,source\_flavor\_id,source\_flavor\_name,sort\_key,sort\_dir,limit,marker\}

[Table 1](#table46110007)  describes the parameters in the URI.

**Table  1**  Path parameters

<a name="table46110007"></a>
<table><thead align="left"><tr id="row14148614"><th class="cellrowborder" valign="top" width="16.61%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.169999999999998%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="66.22%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row17201924"><td class="cellrowborder" valign="top" width="16.61%" headers="mcps1.2.4.1.1 "><p id="p51178607"><a name="p51178607"></a><a name="p51178607"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p51826478"><a name="p51826478"></a><a name="p51826478"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.22%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:**   
>One of the  **instance\_uuid**,  **source\_flavor\_id**, and  **source\_flavor\_name**  parameters must be configured. If multiple parameters are configured, the system processes the  **instance\_uuid**,  **source\_flavor\_id**, and  **source\_flavor\_name**  parameters in descending order by default.  

[Table 2](#table96861454162513)  describes the query parameters.

**Table  2**  Query parameters

<a name="table96861454162513"></a>
<table><thead align="left"><tr id="row4686754182515"><th class="cellrowborder" valign="top" width="18.408159184081594%" id="mcps1.2.5.1.1"><p id="p2686155416251"><a name="p2686155416251"></a><a name="p2686155416251"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.378262173782623%" id="mcps1.2.5.1.2"><p id="p11686854172518"><a name="p11686854172518"></a><a name="p11686854172518"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13.318668133186684%" id="mcps1.2.5.1.3"><p id="p1668645412516"><a name="p1668645412516"></a><a name="p1668645412516"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50.89491050894911%" id="mcps1.2.5.1.4"><p id="p1686154162510"><a name="p1686154162510"></a><a name="p1686154162510"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row156861454172514"><td class="cellrowborder" valign="top" width="18.408159184081594%" headers="mcps1.2.5.1.1 "><p id="p19686105415251"><a name="p19686105415251"></a><a name="p19686105415251"></a>instance_uuid</p>
</td>
<td class="cellrowborder" valign="top" width="17.378262173782623%" headers="mcps1.2.5.1.2 "><p id="p176861554112516"><a name="p176861554112516"></a><a name="p176861554112516"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.318668133186684%" headers="mcps1.2.5.1.3 "><p id="p176861154152518"><a name="p176861154152518"></a><a name="p176861154152518"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.89491050894911%" headers="mcps1.2.5.1.4 "><p id="p12686154172520"><a name="p12686154172520"></a><a name="p12686154172520"></a>Specifies the ID, in UUID format, of the target ECS.</p>
</td>
</tr>
<tr id="row7686175417253"><td class="cellrowborder" valign="top" width="18.408159184081594%" headers="mcps1.2.5.1.1 "><p id="p1668610545258"><a name="p1668610545258"></a><a name="p1668610545258"></a>source_flavor_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.378262173782623%" headers="mcps1.2.5.1.2 "><p id="p1768685417258"><a name="p1768685417258"></a><a name="p1768685417258"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.318668133186684%" headers="mcps1.2.5.1.3 "><p id="p1686145415256"><a name="p1686145415256"></a><a name="p1686145415256"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.89491050894911%" headers="mcps1.2.5.1.4 "><p id="p768685412514"><a name="p768685412514"></a><a name="p768685412514"></a>Specifies the source flavor ID.</p>
</td>
</tr>
<tr id="row168665411250"><td class="cellrowborder" valign="top" width="18.408159184081594%" headers="mcps1.2.5.1.1 "><p id="p1368635492517"><a name="p1368635492517"></a><a name="p1368635492517"></a>source_flavor_name</p>
</td>
<td class="cellrowborder" valign="top" width="17.378262173782623%" headers="mcps1.2.5.1.2 "><p id="p1568675462510"><a name="p1568675462510"></a><a name="p1568675462510"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.318668133186684%" headers="mcps1.2.5.1.3 "><p id="p126861554122516"><a name="p126861554122516"></a><a name="p126861554122516"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.89491050894911%" headers="mcps1.2.5.1.4 "><p id="p6686185411254"><a name="p6686185411254"></a><a name="p6686185411254"></a>Specifies the source flavor name.</p>
</td>
</tr>
<tr id="row1668613546250"><td class="cellrowborder" valign="top" width="18.408159184081594%" headers="mcps1.2.5.1.1 "><p id="p9686954172516"><a name="p9686954172516"></a><a name="p9686954172516"></a>sort_key</p>
</td>
<td class="cellrowborder" valign="top" width="17.378262173782623%" headers="mcps1.2.5.1.2 "><p id="p17686454182517"><a name="p17686454182517"></a><a name="p17686454182517"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.318668133186684%" headers="mcps1.2.5.1.3 "><p id="p1068616548253"><a name="p1068616548253"></a><a name="p1068616548253"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.89491050894911%" headers="mcps1.2.5.1.4 "><p id="p022328104313"><a name="p022328104313"></a><a name="p022328104313"></a>Indicates the field for sorting.</p>
<p id="p20288737204310"><a name="p20288737204310"></a><a name="p20288737204310"></a>Options:</p>
<a name="ul1373511215479"></a><a name="ul1373511215479"></a><ul id="ul1373511215479"><li><strong id="b84235270614334"><a name="b84235270614334"></a><a name="b84235270614334"></a>flavorid</strong>: indicates the flavor ID. The default value is <strong id="b842352706201611"><a name="b842352706201611"></a><a name="b842352706201611"></a>flavorid</strong>.</li><li><strong id="b842352706143324"><a name="b842352706143324"></a><a name="b842352706143324"></a>name</strong>: indicates the flavor name.</li><li><strong id="b842352706143338"><a name="b842352706143338"></a><a name="b842352706143338"></a>memory_mb</strong>: indicates the memory size.</li><li><strong id="b842352706143352"><a name="b842352706143352"></a><a name="b842352706143352"></a>vcpus</strong>: indicates the number of vCPUs.</li><li><strong id="b842352706143411"><a name="b842352706143411"></a><a name="b842352706143411"></a>root_gb</strong>: indicates the system disk size.</li></ul>
</td>
</tr>
<tr id="row11686654102510"><td class="cellrowborder" valign="top" width="18.408159184081594%" headers="mcps1.2.5.1.1 "><p id="p6686135416252"><a name="p6686135416252"></a><a name="p6686135416252"></a>sort_dir</p>
</td>
<td class="cellrowborder" valign="top" width="17.378262173782623%" headers="mcps1.2.5.1.2 "><p id="p2686135414252"><a name="p2686135414252"></a><a name="p2686135414252"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.318668133186684%" headers="mcps1.2.5.1.3 "><p id="p126861854152511"><a name="p126861854152511"></a><a name="p126861854152511"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.89491050894911%" headers="mcps1.2.5.1.4 "><p id="p1913719444471"><a name="p1913719444471"></a><a name="p1913719444471"></a>Specifies the ascending or descending sorting.</p>
<p id="p13472050164719"><a name="p13472050164719"></a><a name="p13472050164719"></a>Options:</p>
<a name="ul391512324817"></a><a name="ul391512324817"></a><ul id="ul391512324817"><li><strong id="b84235270614353"><a name="b84235270614353"></a><a name="b84235270614353"></a>asc</strong>: indicates the ascending order.</li><li><strong id="b842352706143516"><a name="b842352706143516"></a><a name="b842352706143516"></a>desc</strong>: indicates the descending order.</li></ul>
</td>
</tr>
<tr id="row156862545252"><td class="cellrowborder" valign="top" width="18.408159184081594%" headers="mcps1.2.5.1.1 "><p id="p8686185414256"><a name="p8686185414256"></a><a name="p8686185414256"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="17.378262173782623%" headers="mcps1.2.5.1.2 "><p id="p17686654172514"><a name="p17686654172514"></a><a name="p17686654172514"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.318668133186684%" headers="mcps1.2.5.1.3 "><p id="p16686175472510"><a name="p16686175472510"></a><a name="p16686175472510"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50.89491050894911%" headers="mcps1.2.5.1.4 "><p id="p5411239124919"><a name="p5411239124919"></a><a name="p5411239124919"></a>Specifies the maximum number of flavors that can be displayed on one page. The default value is <strong id="b842352706143626"><a name="b842352706143626"></a><a name="b842352706143626"></a>1000</strong>.</p>
</td>
</tr>
<tr id="row16861354102515"><td class="cellrowborder" valign="top" width="18.408159184081594%" headers="mcps1.2.5.1.1 "><p id="p768610546253"><a name="p768610546253"></a><a name="p768610546253"></a>marker</p>
</td>
<td class="cellrowborder" valign="top" width="17.378262173782623%" headers="mcps1.2.5.1.2 "><p id="p1668665492519"><a name="p1668665492519"></a><a name="p1668665492519"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.318668133186684%" headers="mcps1.2.5.1.3 "><p id="p76861154122518"><a name="p76861154122518"></a><a name="p76861154122518"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.89491050894911%" headers="mcps1.2.5.1.4 "><p id="p262162112515"><a name="p262162112515"></a><a name="p262162112515"></a>Uses the ID of the last flavor on one page as the paging marker.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section55841319144411"></a>

None

## Response<a name="section36835188"></a>

[Table 3](#table23477058)  describes the response parameters.

**Table  3**  Response parameters

<a name="table23477058"></a>
<table><thead align="left"><tr id="row2792905"><th class="cellrowborder" valign="top" width="18.060000000000002%" id="mcps1.2.5.1.1"><p id="p8834195805811"><a name="p8834195805811"></a><a name="p8834195805811"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.150000000000002%" id="mcps1.2.5.1.2"><p id="p14834258105810"><a name="p14834258105810"></a><a name="p14834258105810"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13.420000000000002%" id="mcps1.2.5.1.3"><p id="p284905812582"><a name="p284905812582"></a><a name="p284905812582"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.370000000000005%" id="mcps1.2.5.1.4"><p id="p28493585589"><a name="p28493585589"></a><a name="p28493585589"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row9994955"><td class="cellrowborder" valign="top" width="18.060000000000002%" headers="mcps1.2.5.1.1 "><p id="p4284989"><a name="p4284989"></a><a name="p4284989"></a>flavors</p>
</td>
<td class="cellrowborder" valign="top" width="17.150000000000002%" headers="mcps1.2.5.1.2 "><p id="p3812195916261"><a name="p3812195916261"></a><a name="p3812195916261"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.420000000000002%" headers="mcps1.2.5.1.3 "><p id="p62312200"><a name="p62312200"></a><a name="p62312200"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="51.370000000000005%" headers="mcps1.2.5.1.4 "><p id="p60002101"><a name="p60002101"></a><a name="p60002101"></a>Specifies ECS flavors.</p>
<p id="p49021850132819"><a name="p49021850132819"></a><a name="p49021850132819"></a>For details, see <a href="#table68941918122818">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **flavors**  field description

<a name="table68941918122818"></a>
<table><thead align="left"><tr id="row88943187284"><th class="cellrowborder" valign="top" width="18.15%" id="mcps1.2.5.1.1"><p id="p108926065917"><a name="p108926065917"></a><a name="p108926065917"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.1%" id="mcps1.2.5.1.2"><p id="p20892160115919"><a name="p20892160115919"></a><a name="p20892160115919"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13.51%" id="mcps1.2.5.1.3"><p id="p19909160135913"><a name="p19909160135913"></a><a name="p19909160135913"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.239999999999995%" id="mcps1.2.5.1.4"><p id="p199092009598"><a name="p199092009598"></a><a name="p199092009598"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1389441822812"><td class="cellrowborder" valign="top" width="18.15%" headers="mcps1.2.5.1.1 "><p id="p089461852819"><a name="p089461852819"></a><a name="p089461852819"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="17.1%" headers="mcps1.2.5.1.2 "><p id="p824744082716"><a name="p824744082716"></a><a name="p824744082716"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.51%" headers="mcps1.2.5.1.3 "><p id="p1789461852816"><a name="p1789461852816"></a><a name="p1789461852816"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.239999999999995%" headers="mcps1.2.5.1.4 "><p id="p19894121852814"><a name="p19894121852814"></a><a name="p19894121852814"></a>Specifies the ECS flavor ID.</p>
</td>
</tr>
<tr id="row1189421817287"><td class="cellrowborder" valign="top" width="18.15%" headers="mcps1.2.5.1.1 "><p id="p1289413188280"><a name="p1289413188280"></a><a name="p1289413188280"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="17.1%" headers="mcps1.2.5.1.2 "><p id="p192472404270"><a name="p192472404270"></a><a name="p192472404270"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.51%" headers="mcps1.2.5.1.3 "><p id="p9894151811283"><a name="p9894151811283"></a><a name="p9894151811283"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.239999999999995%" headers="mcps1.2.5.1.4 "><p id="p2894191811289"><a name="p2894191811289"></a><a name="p2894191811289"></a>Specifies the name of the ECS flavor.</p>
</td>
</tr>
<tr id="row18894161813288"><td class="cellrowborder" valign="top" width="18.15%" headers="mcps1.2.5.1.1 "><p id="p11894191811283"><a name="p11894191811283"></a><a name="p11894191811283"></a>vcpus</p>
</td>
<td class="cellrowborder" valign="top" width="17.1%" headers="mcps1.2.5.1.2 "><p id="p9247134022717"><a name="p9247134022717"></a><a name="p9247134022717"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.51%" headers="mcps1.2.5.1.3 "><p id="p889481852810"><a name="p889481852810"></a><a name="p889481852810"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="51.239999999999995%" headers="mcps1.2.5.1.4 "><p id="p10894181818285"><a name="p10894181818285"></a><a name="p10894181818285"></a>Specifies the number of vCPUs in the ECS flavor.</p>
</td>
</tr>
<tr id="row1589411184288"><td class="cellrowborder" valign="top" width="18.15%" headers="mcps1.2.5.1.1 "><p id="p188941182288"><a name="p188941182288"></a><a name="p188941182288"></a>ram</p>
</td>
<td class="cellrowborder" valign="top" width="17.1%" headers="mcps1.2.5.1.2 "><p id="p142471140142710"><a name="p142471140142710"></a><a name="p142471140142710"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.51%" headers="mcps1.2.5.1.3 "><p id="p489412187285"><a name="p489412187285"></a><a name="p489412187285"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="51.239999999999995%" headers="mcps1.2.5.1.4 "><p id="p108941182280"><a name="p108941182280"></a><a name="p108941182280"></a>Specifies the memory size (MB) in the ECS flavor.</p>
</td>
</tr>
<tr id="row1989491832819"><td class="cellrowborder" valign="top" width="18.15%" headers="mcps1.2.5.1.1 "><p id="p14894131892814"><a name="p14894131892814"></a><a name="p14894131892814"></a>disk</p>
</td>
<td class="cellrowborder" valign="top" width="17.1%" headers="mcps1.2.5.1.2 "><p id="p32471406274"><a name="p32471406274"></a><a name="p32471406274"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.51%" headers="mcps1.2.5.1.3 "><p id="p88942181287"><a name="p88942181287"></a><a name="p88942181287"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="51.239999999999995%" headers="mcps1.2.5.1.4 "><p id="p138941018162812"><a name="p138941018162812"></a><a name="p138941018162812"></a>Specifies the system disk size in the ECS flavor.</p>
<p id="p14894618102817"><a name="p14894618102817"></a><a name="p14894618102817"></a>This parameter has not been used. Its default value is <strong id="b84235270611135"><a name="b84235270611135"></a><a name="b84235270611135"></a>0</strong>.</p>
</td>
</tr>
<tr id="row589416182281"><td class="cellrowborder" valign="top" width="18.15%" headers="mcps1.2.5.1.1 "><p id="p2089421811281"><a name="p2089421811281"></a><a name="p2089421811281"></a>swap</p>
</td>
<td class="cellrowborder" valign="top" width="17.1%" headers="mcps1.2.5.1.2 "><p id="p172471640192716"><a name="p172471640192716"></a><a name="p172471640192716"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.51%" headers="mcps1.2.5.1.3 "><p id="p289411862819"><a name="p289411862819"></a><a name="p289411862819"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.239999999999995%" headers="mcps1.2.5.1.4 "><p id="p1699362755013"><a name="p1699362755013"></a><a name="p1699362755013"></a>Specifies the swap partition size required by the ECS flavor.</p>
<p id="p4563766173425"><a name="p4563766173425"></a><a name="p4563766173425"></a>This parameter has not been used. Its default value is <strong id="b84235270611135_1"><a name="b84235270611135_1"></a><a name="b84235270611135_1"></a>""</strong>.</p>
</td>
</tr>
<tr id="row158941218202818"><td class="cellrowborder" valign="top" width="18.15%" headers="mcps1.2.5.1.1 "><p id="p18894918132812"><a name="p18894918132812"></a><a name="p18894918132812"></a>OS-FLV-EXT-DATA:ephemeral</p>
</td>
<td class="cellrowborder" valign="top" width="17.1%" headers="mcps1.2.5.1.2 "><p id="p14339475447"><a name="p14339475447"></a><a name="p14339475447"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.51%" headers="mcps1.2.5.1.3 "><p id="p1894818152816"><a name="p1894818152816"></a><a name="p1894818152816"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="51.239999999999995%" headers="mcps1.2.5.1.4 "><p id="p16591226713"><a name="p16591226713"></a><a name="p16591226713"></a>Specifies the temporary disk size. This is an extended attribute.</p>
<p id="p073219456162"><a name="p073219456162"></a><a name="p073219456162"></a>This parameter has not been used. Its default value is <strong id="b84235270611135_2"><a name="b84235270611135_2"></a><a name="b84235270611135_2"></a>0</strong>.</p>
</td>
</tr>
<tr id="row18948183284"><td class="cellrowborder" valign="top" width="18.15%" headers="mcps1.2.5.1.1 "><p id="p88945189285"><a name="p88945189285"></a><a name="p88945189285"></a>OS-FLV-DISABLED:disabled</p>
</td>
<td class="cellrowborder" valign="top" width="17.1%" headers="mcps1.2.5.1.2 "><p id="p5247140122716"><a name="p5247140122716"></a><a name="p5247140122716"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.51%" headers="mcps1.2.5.1.3 "><p id="p208947181287"><a name="p208947181287"></a><a name="p208947181287"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="51.239999999999995%" headers="mcps1.2.5.1.4 "><p id="p1689471812814"><a name="p1689471812814"></a><a name="p1689471812814"></a>This is an extended attribute, specifying whether a flavor is available.</p>
<a name="ul29747184223"></a><a name="ul29747184223"></a><ul id="ul29747184223"><li><strong id="b842352706162411"><a name="b842352706162411"></a><a name="b842352706162411"></a>true</strong>: indicates that a flavor is available.</li><li><strong id="b842352706201847"><a name="b842352706201847"></a><a name="b842352706201847"></a>false</strong>: indicates that a flavor is unavailable.</li></ul>
<div class="note" id="note1057718393114"><a name="note1057718393114"></a><a name="note1057718393114"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p17577183913117"><a name="p17577183913117"></a><a name="p17577183913117"></a>This parameter is not used.</p>
</div></div>
</td>
</tr>
<tr id="row9894141812811"><td class="cellrowborder" valign="top" width="18.15%" headers="mcps1.2.5.1.1 "><p id="p989416188283"><a name="p989416188283"></a><a name="p989416188283"></a>rxtx_factor</p>
</td>
<td class="cellrowborder" valign="top" width="17.1%" headers="mcps1.2.5.1.2 "><p id="p624784010278"><a name="p624784010278"></a><a name="p624784010278"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.51%" headers="mcps1.2.5.1.3 "><p id="p1289431810285"><a name="p1289431810285"></a><a name="p1289431810285"></a>Float</p>
</td>
<td class="cellrowborder" valign="top" width="51.239999999999995%" headers="mcps1.2.5.1.4 "><p id="p1466112191228"><a name="p1466112191228"></a><a name="p1466112191228"></a>This is an extended attribute.</p>
<div class="note" id="note18501922021"><a name="note18501922021"></a><a name="note18501922021"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1350117223210"><a name="p1350117223210"></a><a name="p1350117223210"></a>This parameter is not used.</p>
</div></div>
</td>
</tr>
<tr id="row13357123218463"><td class="cellrowborder" valign="top" width="18.15%" headers="mcps1.2.5.1.1 "><p id="p21606246173425"><a name="p21606246173425"></a><a name="p21606246173425"></a>rxtx_quota</p>
</td>
<td class="cellrowborder" valign="top" width="17.1%" headers="mcps1.2.5.1.2 "><p id="p5275477173425"><a name="p5275477173425"></a><a name="p5275477173425"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.51%" headers="mcps1.2.5.1.3 "><p id="p391327154610"><a name="p391327154610"></a><a name="p391327154610"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.239999999999995%" headers="mcps1.2.5.1.4 "><p id="p3137170105719"><a name="p3137170105719"></a><a name="p3137170105719"></a>Specifies the software constraints of the network bandwidth that can be used by the ECS.</p>
<p id="p16913177154619"><a name="p16913177154619"></a><a name="p16913177154619"></a>This parameter has not been used. Its default value is <strong id="b84235270611135_3"><a name="b84235270611135_3"></a><a name="b84235270611135_3"></a>null</strong>.</p>
</td>
</tr>
<tr id="row7639734144610"><td class="cellrowborder" valign="top" width="18.15%" headers="mcps1.2.5.1.1 "><p id="p65053613173425"><a name="p65053613173425"></a><a name="p65053613173425"></a>rxtx_cap</p>
</td>
<td class="cellrowborder" valign="top" width="17.1%" headers="mcps1.2.5.1.2 "><p id="p34851326173425"><a name="p34851326173425"></a><a name="p34851326173425"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.51%" headers="mcps1.2.5.1.3 "><p id="p3914207184617"><a name="p3914207184617"></a><a name="p3914207184617"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.239999999999995%" headers="mcps1.2.5.1.4 "><p id="p12914778466"><a name="p12914778466"></a><a name="p12914778466"></a>Specifies the hardware constraints of the network bandwidth that can be used by the ECS.</p>
<p id="p1591467174617"><a name="p1591467174617"></a><a name="p1591467174617"></a>This parameter has not been used. Its default value is <strong id="b84235270611135_4"><a name="b84235270611135_4"></a><a name="b84235270611135_4"></a>null</strong>.</p>
</td>
</tr>
<tr id="row158941918102811"><td class="cellrowborder" valign="top" width="18.15%" headers="mcps1.2.5.1.1 "><p id="p18944183285"><a name="p18944183285"></a><a name="p18944183285"></a>os-flavor-access:is_public</p>
</td>
<td class="cellrowborder" valign="top" width="17.1%" headers="mcps1.2.5.1.2 "><p id="p2247124010273"><a name="p2247124010273"></a><a name="p2247124010273"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.51%" headers="mcps1.2.5.1.3 "><p id="p188942182287"><a name="p188942182287"></a><a name="p188942182287"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="51.239999999999995%" headers="mcps1.2.5.1.4 "><p id="p8894218182818"><a name="p8894218182818"></a><a name="p8894218182818"></a>Specifies whether a flavor is available to all tenants. This is an extended attribute.</p>
<a name="ul1474014143815"></a><a name="ul1474014143815"></a><ul id="ul1474014143815"><li><strong id="b84235270620200"><a name="b84235270620200"></a><a name="b84235270620200"></a>true</strong>: indicates that a flavor is available to all tenants.</li><li><strong id="b84235270620200_1"><a name="b84235270620200_1"></a><a name="b84235270620200_1"></a>false</strong>: indicates that a flavor is available only to certain tenants.</li></ul>
<p id="p35038271466"><a name="p35038271466"></a><a name="p35038271466"></a>Default value: <strong id="b842352706202049"><a name="b842352706202049"></a><a name="b842352706202049"></a>true</strong></p>
</td>
</tr>
<tr id="row13894418182817"><td class="cellrowborder" valign="top" width="18.15%" headers="mcps1.2.5.1.1 "><p id="p158941018122818"><a name="p158941018122818"></a><a name="p158941018122818"></a>links</p>
</td>
<td class="cellrowborder" valign="top" width="17.1%" headers="mcps1.2.5.1.2 "><p id="p724734016277"><a name="p724734016277"></a><a name="p724734016277"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.51%" headers="mcps1.2.5.1.3 "><p id="p1989491810284"><a name="p1989491810284"></a><a name="p1989491810284"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="51.239999999999995%" headers="mcps1.2.5.1.4 "><p id="p589411814280"><a name="p589411814280"></a><a name="p589411814280"></a>Specifies the shortcut link of the ECS flavor.</p>
<p id="p1020831644512"><a name="p1020831644512"></a><a name="p1020831644512"></a>For details, see <a href="#table15913898194628">Table 5</a>.</p>
</td>
</tr>
<tr id="row1989417182289"><td class="cellrowborder" valign="top" width="18.15%" headers="mcps1.2.5.1.1 "><p id="p14894151811285"><a name="p14894151811285"></a><a name="p14894151811285"></a>extra_specs</p>
</td>
<td class="cellrowborder" valign="top" width="17.1%" headers="mcps1.2.5.1.2 "><p id="p224784012712"><a name="p224784012712"></a><a name="p224784012712"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.51%" headers="mcps1.2.5.1.3 "><p id="p17894101822814"><a name="p17894101822814"></a><a name="p17894101822814"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="51.239999999999995%" headers="mcps1.2.5.1.4 "><p id="p1164601842410"><a name="p1164601842410"></a><a name="p1164601842410"></a>Specifies the extended field of the ECS specifications.</p>
<p id="p48941018132817"><a name="p48941018132817"></a><a name="p48941018132817"></a>For details, see <a href="querying-details-about-flavors-and-extended-flavor-information.md#table59078165">Table 6</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **links**  field description

<a name="table15913898194628"></a>
<table><thead align="left"><tr id="row37608132194628"><th class="cellrowborder" valign="top" width="18.060000000000002%" id="mcps1.2.5.1.1"><p id="p10572055596"><a name="p10572055596"></a><a name="p10572055596"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.119999999999997%" id="mcps1.2.5.1.2"><p id="p2572145145920"><a name="p2572145145920"></a><a name="p2572145145920"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13.469999999999999%" id="mcps1.2.5.1.3"><p id="p155721525912"><a name="p155721525912"></a><a name="p155721525912"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.349999999999994%" id="mcps1.2.5.1.4"><p id="p157216575917"><a name="p157216575917"></a><a name="p157216575917"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row17692319194628"><td class="cellrowborder" valign="top" width="18.060000000000002%" headers="mcps1.2.5.1.1 "><p id="p23791739194628"><a name="p23791739194628"></a><a name="p23791739194628"></a>rel</p>
</td>
<td class="cellrowborder" valign="top" width="17.119999999999997%" headers="mcps1.2.5.1.2 "><p id="p986727172810"><a name="p986727172810"></a><a name="p986727172810"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.469999999999999%" headers="mcps1.2.5.1.3 "><p id="p48082703194628"><a name="p48082703194628"></a><a name="p48082703194628"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.349999999999994%" headers="mcps1.2.5.1.4 "><p id="p2384900194628"><a name="p2384900194628"></a><a name="p2384900194628"></a>Specifies the shortcut link marker name.</p>
</td>
</tr>
<tr id="row21464106194628"><td class="cellrowborder" valign="top" width="18.060000000000002%" headers="mcps1.2.5.1.1 "><p id="p60871059194628"><a name="p60871059194628"></a><a name="p60871059194628"></a>href</p>
</td>
<td class="cellrowborder" valign="top" width="17.119999999999997%" headers="mcps1.2.5.1.2 "><p id="p208672782812"><a name="p208672782812"></a><a name="p208672782812"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.469999999999999%" headers="mcps1.2.5.1.3 "><p id="p31608752194628"><a name="p31608752194628"></a><a name="p31608752194628"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.349999999999994%" headers="mcps1.2.5.1.4 "><p id="p10172138194628"><a name="p10172138194628"></a><a name="p10172138194628"></a>Specifies the shortcut link.</p>
</td>
</tr>
<tr id="row0172619474"><td class="cellrowborder" valign="top" width="18.060000000000002%" headers="mcps1.2.5.1.1 "><p id="p16018444171451"><a name="p16018444171451"></a><a name="p16018444171451"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="17.119999999999997%" headers="mcps1.2.5.1.2 "><p id="p22425577171451"><a name="p22425577171451"></a><a name="p22425577171451"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.469999999999999%" headers="mcps1.2.5.1.3 "><p id="p838292134116"><a name="p838292134116"></a><a name="p838292134116"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.349999999999994%" headers="mcps1.2.5.1.4 "><p id="p10382152144115"><a name="p10382152144115"></a><a name="p10382152144115"></a>Specifies the shortcut link type. This parameter has not been used. Its default value is <strong id="b84235270611582"><a name="b84235270611582"></a><a name="b84235270611582"></a>null</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="section21941533132918"></a>

```
GET https://{endpoint}/v1/{project_id}/cloudservers/resize_flavors?source_flavor_id=c3.xlarge.2
```

## Example Response<a name="section025391883814"></a>

```
{
    "flavors": [
        {
            "id": "c3.15xlarge.2",
            "name": "c3.15xlarge.2",
            "vcpus": "60",
            "ram": 131072,
            "disk": "0",
            "swap": "",
            "links": [
                {
                    "rel": "self",
                    "href": "https://compute-ext.region.xxx.com/v1.0/743b4c0428d94531b9f2add666642e6b/flavors/c3.15xlarge.2",
                    "type": null
                },
                {
                    "rel": "bookmark",
                    "href": "https://compute-ext.region.xxx.com/743b4c0428d94531b9f2add666642e6b/flavors/c3.15xlarge.2",
                    "type": null
                }
            ],
            "OS-FLV-EXT-DATA:ephemeral": 0,
            "rxtx_factor": 1,
            "OS-FLV-DISABLED:disabled": false,
            "rxtx_quota": null,
            "rxtx_cap": null,
            "os-flavor-access:is_public": true,
            "extra_specs": {
                "ecs:virtualization_env_types": "CloudCompute",
                "ecs:generation": "c3",
                "ecs:performancetype": "computingv3",
                "resource_type": "IOoptimizedC3_2"
             }
        }
    ]
}
```

## Returned Values<a name="en-us_topic_0092803065_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

## Error Codes<a name="en-us_topic_0092803065_en-us_topic_0067161469_en-us_topic_0057973179_section23611955"></a>

See  [Error Code Description](error-code-description.md).

