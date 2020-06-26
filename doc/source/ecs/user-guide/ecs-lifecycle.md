# ECS Lifecycle<a name="EN-US_TOPIC_0140323150"></a>

A lifecycle indicates the ECS statuses recorded from the time when the ECS is created through the time when the ECS is deleted or released.

**Table  1**  ECS statuses

<a name="table198821178160"></a>
<table><thead align="left"><tr id="row31891630195029"><th class="cellrowborder" valign="top" width="20.669135149431366%" id="mcps1.2.4.1.1"><p id="p33085243195029"><a name="p33085243195029"></a><a name="p33085243195029"></a>Status</p>
</th>
<th class="cellrowborder" valign="top" width="22.322137000793443%" id="mcps1.2.4.1.2"><p id="p62659045195029"><a name="p62659045195029"></a><a name="p62659045195029"></a>Status Attribute</p>
</th>
<th class="cellrowborder" valign="top" width="57.008727849775184%" id="mcps1.2.4.1.3"><p id="p42217875195029"><a name="p42217875195029"></a><a name="p42217875195029"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row64204718195029"><td class="cellrowborder" valign="top" width="20.669135149431366%" headers="mcps1.2.4.1.1 "><p id="p33199645195029"><a name="p33199645195029"></a><a name="p33199645195029"></a>Creating</p>
</td>
<td class="cellrowborder" valign="top" width="22.322137000793443%" headers="mcps1.2.4.1.2 "><p id="p4816713195029"><a name="p4816713195029"></a><a name="p4816713195029"></a>Intermediate</p>
</td>
<td class="cellrowborder" valign="top" width="57.008727849775184%" headers="mcps1.2.4.1.3 "><p id="p11928492203457"><a name="p11928492203457"></a><a name="p11928492203457"></a>The ECS has been created but is not running.</p>
</td>
</tr>
<tr id="row47440894105334"><td class="cellrowborder" valign="top" width="20.669135149431366%" headers="mcps1.2.4.1.1 "><p id="p19016076105357"><a name="p19016076105357"></a><a name="p19016076105357"></a>Starting</p>
</td>
<td class="cellrowborder" valign="top" width="22.322137000793443%" headers="mcps1.2.4.1.2 "><p id="p63907192105357"><a name="p63907192105357"></a><a name="p63907192105357"></a>Intermediate</p>
</td>
<td class="cellrowborder" valign="top" width="57.008727849775184%" headers="mcps1.2.4.1.3 "><p id="p9100060105357"><a name="p9100060105357"></a><a name="p9100060105357"></a>The ECS is between the <strong id="b842352706103424"><a name="b842352706103424"></a><a name="b842352706103424"></a>Stopped</strong> and <strong id="b842352706103427"><a name="b842352706103427"></a><a name="b842352706103427"></a>Running</strong> states.</p>
</td>
</tr>
<tr id="row32093542195029"><td class="cellrowborder" valign="top" width="20.669135149431366%" headers="mcps1.2.4.1.1 "><p id="p49440133195029"><a name="p49440133195029"></a><a name="p49440133195029"></a>Running</p>
</td>
<td class="cellrowborder" valign="top" width="22.322137000793443%" headers="mcps1.2.4.1.2 "><p id="p45227832195029"><a name="p45227832195029"></a><a name="p45227832195029"></a>Stable</p>
</td>
<td class="cellrowborder" valign="top" width="57.008727849775184%" headers="mcps1.2.4.1.3 "><p id="p57478049203527"><a name="p57478049203527"></a><a name="p57478049203527"></a>The ECS is running properly.</p>
<p id="p39575784195029"><a name="p39575784195029"></a><a name="p39575784195029"></a>An ECS in this state can provide services.</p>
</td>
</tr>
<tr id="row21015765105421"><td class="cellrowborder" valign="top" width="20.669135149431366%" headers="mcps1.2.4.1.1 "><p id="p2951922105435"><a name="p2951922105435"></a><a name="p2951922105435"></a>Stopping</p>
</td>
<td class="cellrowborder" valign="top" width="22.322137000793443%" headers="mcps1.2.4.1.2 "><p id="p37779111105435"><a name="p37779111105435"></a><a name="p37779111105435"></a>Intermediate</p>
</td>
<td class="cellrowborder" valign="top" width="57.008727849775184%" headers="mcps1.2.4.1.3 "><p id="p40209165105435"><a name="p40209165105435"></a><a name="p40209165105435"></a>The ECS is between the <strong id="b857403626"><a name="b857403626"></a><a name="b857403626"></a>Running</strong> and <strong id="b1245309347"><a name="b1245309347"></a><a name="b1245309347"></a>Stopped</strong> states.</p>
</td>
</tr>
<tr id="row20637738195029"><td class="cellrowborder" valign="top" width="20.669135149431366%" headers="mcps1.2.4.1.1 "><p id="p61044063195029"><a name="p61044063195029"></a><a name="p61044063195029"></a>Stopped</p>
</td>
<td class="cellrowborder" valign="top" width="22.322137000793443%" headers="mcps1.2.4.1.2 "><p id="p45622085195029"><a name="p45622085195029"></a><a name="p45622085195029"></a>Stable</p>
</td>
<td class="cellrowborder" valign="top" width="57.008727849775184%" headers="mcps1.2.4.1.3 "><p id="p19889388203530"><a name="p19889388203530"></a><a name="p19889388203530"></a>The ECS has been properly stopped.</p>
<p id="p4401411195029"><a name="p4401411195029"></a><a name="p4401411195029"></a>An ECS in this state cannot provide services.</p>
</td>
</tr>
<tr id="row39612707195029"><td class="cellrowborder" valign="top" width="20.669135149431366%" headers="mcps1.2.4.1.1 "><p id="p54512730195029"><a name="p54512730195029"></a><a name="p54512730195029"></a>Restarting</p>
</td>
<td class="cellrowborder" valign="top" width="22.322137000793443%" headers="mcps1.2.4.1.2 "><p id="p53454972195029"><a name="p53454972195029"></a><a name="p53454972195029"></a>Intermediate</p>
</td>
<td class="cellrowborder" valign="top" width="57.008727849775184%" headers="mcps1.2.4.1.3 "><p id="p52330452203536"><a name="p52330452203536"></a><a name="p52330452203536"></a>The ECS is being restarted.</p>
</td>
</tr>
<tr id="row45533970195029"><td class="cellrowborder" valign="top" width="20.669135149431366%" headers="mcps1.2.4.1.1 "><p id="p64372963195029"><a name="p64372963195029"></a><a name="p64372963195029"></a>Resizing</p>
</td>
<td class="cellrowborder" valign="top" width="22.322137000793443%" headers="mcps1.2.4.1.2 "><p id="p46827516195029"><a name="p46827516195029"></a><a name="p46827516195029"></a>Intermediate</p>
</td>
<td class="cellrowborder" valign="top" width="57.008727849775184%" headers="mcps1.2.4.1.3 "><p id="p18520823203547"><a name="p18520823203547"></a><a name="p18520823203547"></a>The ECS has received a resizing request and has started to resize.</p>
</td>
</tr>
<tr id="row45956925195029"><td class="cellrowborder" valign="top" width="20.669135149431366%" headers="mcps1.2.4.1.1 "><p id="p31523443195029"><a name="p31523443195029"></a><a name="p31523443195029"></a>Verifying resizing</p>
</td>
<td class="cellrowborder" valign="top" width="22.322137000793443%" headers="mcps1.2.4.1.2 "><p id="p3262061195029"><a name="p3262061195029"></a><a name="p3262061195029"></a>Intermediate</p>
</td>
<td class="cellrowborder" valign="top" width="57.008727849775184%" headers="mcps1.2.4.1.3 "><p id="p13207388203629"><a name="p13207388203629"></a><a name="p13207388203629"></a>The ECS is verifying the modified configuration.</p>
</td>
</tr>
<tr id="row39752192105447"><td class="cellrowborder" valign="top" width="20.669135149431366%" headers="mcps1.2.4.1.1 "><p id="p3921202210551"><a name="p3921202210551"></a><a name="p3921202210551"></a>Deleting</p>
</td>
<td class="cellrowborder" valign="top" width="22.322137000793443%" headers="mcps1.2.4.1.2 "><p id="p2205719010551"><a name="p2205719010551"></a><a name="p2205719010551"></a>Intermediate</p>
</td>
<td class="cellrowborder" valign="top" width="57.008727849775184%" headers="mcps1.2.4.1.3 "><p id="p4180197510551"><a name="p4180197510551"></a><a name="p4180197510551"></a>The ECS is being deleted.</p>
<p id="p4067345910551"><a name="p4067345910551"></a><a name="p4067345910551"></a>If the ECS remains in this state for a long time, exceptions may have occurred. In such an event, contact the administrator.</p>
</td>
</tr>
<tr id="row29232435195029"><td class="cellrowborder" valign="top" width="20.669135149431366%" headers="mcps1.2.4.1.1 "><p id="p19017031195029"><a name="p19017031195029"></a><a name="p19017031195029"></a>Deleted</p>
</td>
<td class="cellrowborder" valign="top" width="22.322137000793443%" headers="mcps1.2.4.1.2 "><p id="p63984572195029"><a name="p63984572195029"></a><a name="p63984572195029"></a>Intermediate</p>
</td>
<td class="cellrowborder" valign="top" width="57.008727849775184%" headers="mcps1.2.4.1.3 "><p id="p15367866195029"><a name="p15367866195029"></a><a name="p15367866195029"></a>The ECS has been deleted. An ECS in this state cannot provide services and will be promptly cleared from the system.</p>
</td>
</tr>
<tr id="row4093067195029"><td class="cellrowborder" valign="top" width="20.669135149431366%" headers="mcps1.2.4.1.1 "><p id="p63103016195029"><a name="p63103016195029"></a><a name="p63103016195029"></a>Faulty</p>
</td>
<td class="cellrowborder" valign="top" width="22.322137000793443%" headers="mcps1.2.4.1.2 "><p id="p11070690195029"><a name="p11070690195029"></a><a name="p11070690195029"></a>Stable</p>
</td>
<td class="cellrowborder" valign="top" width="57.008727849775184%" headers="mcps1.2.4.1.3 "><p id="p52961886203752"><a name="p52961886203752"></a><a name="p52961886203752"></a>An exception has occurred on the ECS.</p>
<p id="p24310688195029"><a name="p24310688195029"></a><a name="p24310688195029"></a>An ECS in this state cannot provide services. Contact the administrator.</p>
</td>
</tr>
<tr id="row2110602622730"><td class="cellrowborder" valign="top" width="20.669135149431366%" headers="mcps1.2.4.1.1 "><p id="p5573650922730"><a name="p5573650922730"></a><a name="p5573650922730"></a>Reinstalling OS</p>
</td>
<td class="cellrowborder" valign="top" width="22.322137000793443%" headers="mcps1.2.4.1.2 "><p id="p1836339522730"><a name="p1836339522730"></a><a name="p1836339522730"></a>Intermediate</p>
</td>
<td class="cellrowborder" valign="top" width="57.008727849775184%" headers="mcps1.2.4.1.3 "><p id="p4576066522929"><a name="p4576066522929"></a><a name="p4576066522929"></a>The ECS has received a request to reinstall the OS and has begun the reinstallation.</p>
</td>
</tr>
<tr id="row2185704722730"><td class="cellrowborder" valign="top" width="20.669135149431366%" headers="mcps1.2.4.1.1 "><p id="p6249570022730"><a name="p6249570022730"></a><a name="p6249570022730"></a>Reinstalling OS failed</p>
</td>
<td class="cellrowborder" valign="top" width="22.322137000793443%" headers="mcps1.2.4.1.2 "><p id="p2898696322730"><a name="p2898696322730"></a><a name="p2898696322730"></a>Stable</p>
</td>
<td class="cellrowborder" valign="top" width="57.008727849775184%" headers="mcps1.2.4.1.3 "><p id="p6164988522950"><a name="p6164988522950"></a><a name="p6164988522950"></a>The ECS received a request to reinstall the OS, but due to exceptions, the reinstallation failed.</p>
<p id="p1797806122950"><a name="p1797806122950"></a><a name="p1797806122950"></a>An ECS in this state cannot provide services. Contact the administrator.</p>
</td>
</tr>
<tr id="row54080092153753"><td class="cellrowborder" valign="top" width="20.669135149431366%" headers="mcps1.2.4.1.1 "><p id="p16958788153753"><a name="p16958788153753"></a><a name="p16958788153753"></a>Changing OS</p>
</td>
<td class="cellrowborder" valign="top" width="22.322137000793443%" headers="mcps1.2.4.1.2 "><p id="p31484596153753"><a name="p31484596153753"></a><a name="p31484596153753"></a>Intermediate</p>
</td>
<td class="cellrowborder" valign="top" width="57.008727849775184%" headers="mcps1.2.4.1.3 "><p id="p3579210015402"><a name="p3579210015402"></a><a name="p3579210015402"></a>The ECS received a request to change the OS and has begun implementing the changes.</p>
</td>
</tr>
<tr id="row33994049153753"><td class="cellrowborder" valign="top" width="20.669135149431366%" headers="mcps1.2.4.1.1 "><p id="p37510992153753"><a name="p37510992153753"></a><a name="p37510992153753"></a>OS Change failed</p>
</td>
<td class="cellrowborder" valign="top" width="22.322137000793443%" headers="mcps1.2.4.1.2 "><p id="p18491498153753"><a name="p18491498153753"></a><a name="p18491498153753"></a>Stable</p>
</td>
<td class="cellrowborder" valign="top" width="57.008727849775184%" headers="mcps1.2.4.1.3 "><p id="p51539590154026"><a name="p51539590154026"></a><a name="p51539590154026"></a>The ECS has received a request to change the OS, but due to exceptions, the changes failed to be implemented.</p>
<p id="p61203130154026"><a name="p61203130154026"></a><a name="p61203130154026"></a>An ECS in this state cannot provide services. Contact the administrator.</p>
</td>
</tr>
<tr id="row5468053522730"><td class="cellrowborder" valign="top" width="20.669135149431366%" headers="mcps1.2.4.1.1 "><p id="p2236276722730"><a name="p2236276722730"></a><a name="p2236276722730"></a>Forcibly restarting</p>
</td>
<td class="cellrowborder" valign="top" width="22.322137000793443%" headers="mcps1.2.4.1.2 "><p id="p6655366422730"><a name="p6655366422730"></a><a name="p6655366422730"></a>Intermediate</p>
</td>
<td class="cellrowborder" valign="top" width="57.008727849775184%" headers="mcps1.2.4.1.3 "><p id="p4698147522103"><a name="p4698147522103"></a><a name="p4698147522103"></a>The ECS is being forcibly restarted.</p>
</td>
</tr>
<tr id="row397906322730"><td class="cellrowborder" valign="top" width="20.669135149431366%" headers="mcps1.2.4.1.1 "><p id="p3581157122730"><a name="p3581157122730"></a><a name="p3581157122730"></a>Rolling back resizing</p>
</td>
<td class="cellrowborder" valign="top" width="22.322137000793443%" headers="mcps1.2.4.1.2 "><p id="p1505612922730"><a name="p1505612922730"></a><a name="p1505612922730"></a>Intermediate</p>
</td>
<td class="cellrowborder" valign="top" width="57.008727849775184%" headers="mcps1.2.4.1.3 "><p id="p23060354221011"><a name="p23060354221011"></a><a name="p23060354221011"></a>The ECS is rolling back resizing.</p>
</td>
</tr>
</tbody>
</table>

