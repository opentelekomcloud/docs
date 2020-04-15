# EVS Disk Status<a name="evs_01_0040"></a>

An EVS disk has several statuses.  [Table 1](#evs_faq_0013_table64552624191747)  lists the EVS disk statuses, the meaning of each status, and the operations a disk in each status allows.

**Table  1**  Disk status details

<a name="evs_faq_0013_table64552624191747"></a>
<table><thead align="left"><tr id="evs_faq_0013_row53790844191747"><th class="cellrowborder" valign="top" width="18.67%" id="mcps1.2.4.1.1"><p id="evs_faq_0013_p4696184819180"><a name="evs_faq_0013_p4696184819180"></a><a name="evs_faq_0013_p4696184819180"></a>EVS Disk Status</p>
</th>
<th class="cellrowborder" valign="top" width="52.129999999999995%" id="mcps1.2.4.1.2"><p id="evs_faq_0013_p16533784191747"><a name="evs_faq_0013_p16533784191747"></a><a name="evs_faq_0013_p16533784191747"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="29.2%" id="mcps1.2.4.1.3"><p id="evs_faq_0013_p44528397191747"><a name="evs_faq_0013_p44528397191747"></a><a name="evs_faq_0013_p44528397191747"></a>Allowed Operation</p>
</th>
</tr>
</thead>
<tbody><tr id="evs_faq_0013_row35291149191747"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="evs_faq_0013_p52928025191747"><a name="evs_faq_0013_p52928025191747"></a><a name="evs_faq_0013_p52928025191747"></a>In-use</p>
</td>
<td class="cellrowborder" valign="top" width="52.129999999999995%" headers="mcps1.2.4.1.2 "><p id="evs_faq_0013_p8182837191747"><a name="evs_faq_0013_p8182837191747"></a><a name="evs_faq_0013_p8182837191747"></a>The EVS disk is attached to <span id="evs_faq_0013_text996094623144624"><a name="evs_faq_0013_text996094623144624"></a><a name="evs_faq_0013_text996094623144624"></a>a server</span> and is in use.</p>
</td>
<td class="cellrowborder" valign="top" width="29.2%" headers="mcps1.2.4.1.3 "><a name="evs_faq_0013_ul6530119818278"></a><a name="evs_faq_0013_ul6530119818278"></a><ul id="evs_faq_0013_ul6530119818278"><li>Detaching</li><li>Creating VBS backups</li><li>Expanding<div class="note" id="evs_faq_0013_note22611728203940"><a name="evs_faq_0013_note22611728203940"></a><a name="evs_faq_0013_note22611728203940"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="evs_faq_0013_p2178963203940"><a name="evs_faq_0013_p2178963203940"></a><a name="evs_faq_0013_p2178963203940"></a>If a shared EVS disk is in the <span class="parmname" id="evs_faq_0013_parmname16804863221452"><a name="evs_faq_0013_parmname16804863221452"></a><a name="evs_faq_0013_parmname16804863221452"></a><b>In-use</b></span> state, the disk can be attached.</p>
<p id="evs_faq_0013_p4050480162040"><a name="evs_faq_0013_p4050480162040"></a><a name="evs_faq_0013_p4050480162040"></a>If a shared EVS disk is in the <span class="parmname" id="evs_faq_0013_parmname16804863221452_1"><a name="evs_faq_0013_parmname16804863221452_1"></a><a name="evs_faq_0013_parmname16804863221452_1"></a><b>In-use</b></span> state, the disk cannot be expanded.</p>
</div></div>
</li></ul>
</td>
</tr>
<tr id="evs_faq_0013_row12893053191747"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="evs_faq_0013_p2259935191846"><a name="evs_faq_0013_p2259935191846"></a><a name="evs_faq_0013_p2259935191846"></a>Available</p>
</td>
<td class="cellrowborder" valign="top" width="52.129999999999995%" headers="mcps1.2.4.1.2 "><p id="evs_faq_0013_p16383851191846"><a name="evs_faq_0013_p16383851191846"></a><a name="evs_faq_0013_p16383851191846"></a>The EVS disk has not been attached to any <span id="evs_faq_0013_text1896822207144644"><a name="evs_faq_0013_text1896822207144644"></a><a name="evs_faq_0013_text1896822207144644"></a>server</span> and can be attached.</p>
</td>
<td class="cellrowborder" valign="top" width="29.2%" headers="mcps1.2.4.1.3 "><a name="evs_faq_0013_ul62104117182653"></a><a name="evs_faq_0013_ul62104117182653"></a><ul id="evs_faq_0013_ul62104117182653"><li>Attaching</li><li>Expanding</li><li>Deleting</li><li>Creating VBS backups</li><li>Rolling back snapshots to EVS disks</li></ul>
</td>
</tr>
<tr id="evs_faq_0013_row3465059312446"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="evs_faq_0013_p2028928412455"><a name="evs_faq_0013_p2028928412455"></a><a name="evs_faq_0013_p2028928412455"></a>Creating</p>
</td>
<td class="cellrowborder" valign="top" width="52.129999999999995%" headers="mcps1.2.4.1.2 "><p id="evs_faq_0013_p5713908012455"><a name="evs_faq_0013_p5713908012455"></a><a name="evs_faq_0013_p5713908012455"></a>The EVS disk is being created.</p>
</td>
<td class="cellrowborder" valign="top" width="29.2%" headers="mcps1.2.4.1.3 "><p id="evs_faq_0013_p4503759612455"><a name="evs_faq_0013_p4503759612455"></a><a name="evs_faq_0013_p4503759612455"></a>None</p>
</td>
</tr>
<tr id="evs_faq_0013_row618886912446"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="evs_faq_0013_p1654812012455"><a name="evs_faq_0013_p1654812012455"></a><a name="evs_faq_0013_p1654812012455"></a>Attaching</p>
</td>
<td class="cellrowborder" valign="top" width="52.129999999999995%" headers="mcps1.2.4.1.2 "><p id="evs_faq_0013_p5184251612455"><a name="evs_faq_0013_p5184251612455"></a><a name="evs_faq_0013_p5184251612455"></a>The EVS disk is being attached to <span id="evs_faq_0013_text1268840253185355"><a name="evs_faq_0013_text1268840253185355"></a><a name="evs_faq_0013_text1268840253185355"></a>a server</span>.</p>
</td>
<td class="cellrowborder" valign="top" width="29.2%" headers="mcps1.2.4.1.3 "><p id="evs_faq_0013_p5079721612455"><a name="evs_faq_0013_p5079721612455"></a><a name="evs_faq_0013_p5079721612455"></a>None</p>
</td>
</tr>
<tr id="evs_faq_0013_row4740542112446"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="evs_faq_0013_p1076529612455"><a name="evs_faq_0013_p1076529612455"></a><a name="evs_faq_0013_p1076529612455"></a>Detaching</p>
</td>
<td class="cellrowborder" valign="top" width="52.129999999999995%" headers="mcps1.2.4.1.2 "><p id="evs_faq_0013_p1865238812455"><a name="evs_faq_0013_p1865238812455"></a><a name="evs_faq_0013_p1865238812455"></a>The EVS disk is being detached from <span id="evs_faq_0013_text1535283816185410"><a name="evs_faq_0013_text1535283816185410"></a><a name="evs_faq_0013_text1535283816185410"></a>a server</span>.</p>
</td>
<td class="cellrowborder" valign="top" width="29.2%" headers="mcps1.2.4.1.3 "><p id="evs_faq_0013_p5419159212455"><a name="evs_faq_0013_p5419159212455"></a><a name="evs_faq_0013_p5419159212455"></a>None</p>
</td>
</tr>
<tr id="evs_faq_0013_row721621712446"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="evs_faq_0013_p3658433212455"><a name="evs_faq_0013_p3658433212455"></a><a name="evs_faq_0013_p3658433212455"></a>Deleting</p>
</td>
<td class="cellrowborder" valign="top" width="52.129999999999995%" headers="mcps1.2.4.1.2 "><p id="evs_faq_0013_p3682527212455"><a name="evs_faq_0013_p3682527212455"></a><a name="evs_faq_0013_p3682527212455"></a>The EVS disk is being deleted.</p>
</td>
<td class="cellrowborder" valign="top" width="29.2%" headers="mcps1.2.4.1.3 "><p id="evs_faq_0013_p4587262812455"><a name="evs_faq_0013_p4587262812455"></a><a name="evs_faq_0013_p4587262812455"></a>None</p>
</td>
</tr>
<tr id="evs_faq_0013_row1073062112446"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="evs_faq_0013_p4208872012455"><a name="evs_faq_0013_p4208872012455"></a><a name="evs_faq_0013_p4208872012455"></a>Restoring</p>
</td>
<td class="cellrowborder" valign="top" width="52.129999999999995%" headers="mcps1.2.4.1.2 "><p id="evs_faq_0013_p33758012455"><a name="evs_faq_0013_p33758012455"></a><a name="evs_faq_0013_p33758012455"></a>A VBS backup is being used to restore the EVS disk.</p>
</td>
<td class="cellrowborder" valign="top" width="29.2%" headers="mcps1.2.4.1.3 "><p id="evs_faq_0013_p1673327212455"><a name="evs_faq_0013_p1673327212455"></a><a name="evs_faq_0013_p1673327212455"></a>None</p>
</td>
</tr>
<tr id="evs_faq_0013_row1362373212446"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="evs_faq_0013_p1487436012455"><a name="evs_faq_0013_p1487436012455"></a><a name="evs_faq_0013_p1487436012455"></a>Expanding</p>
</td>
<td class="cellrowborder" valign="top" width="52.129999999999995%" headers="mcps1.2.4.1.2 "><p id="evs_faq_0013_p3000340412455"><a name="evs_faq_0013_p3000340412455"></a><a name="evs_faq_0013_p3000340412455"></a>The capacity of the EVS disk is being expanded.</p>
</td>
<td class="cellrowborder" valign="top" width="29.2%" headers="mcps1.2.4.1.3 "><p id="evs_faq_0013_p3724766412455"><a name="evs_faq_0013_p3724766412455"></a><a name="evs_faq_0013_p3724766412455"></a>None</p>
</td>
</tr>
<tr id="evs_faq_0013_row655296691252"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="evs_faq_0013_p111354991259"><a name="evs_faq_0013_p111354991259"></a><a name="evs_faq_0013_p111354991259"></a>Uploading</p>
</td>
<td class="cellrowborder" valign="top" width="52.129999999999995%" headers="mcps1.2.4.1.2 "><p id="evs_faq_0013_p425803511259"><a name="evs_faq_0013_p425803511259"></a><a name="evs_faq_0013_p425803511259"></a>Data on the EVS disk is being uploaded to an image. This state occurs when you create an image from <span id="evs_faq_0013_text53826504414471"><a name="evs_faq_0013_text53826504414471"></a><a name="evs_faq_0013_text53826504414471"></a>a server</span>.</p>
</td>
<td class="cellrowborder" valign="top" width="29.2%" headers="mcps1.2.4.1.3 "><p id="evs_faq_0013_p584890911259"><a name="evs_faq_0013_p584890911259"></a><a name="evs_faq_0013_p584890911259"></a>None</p>
</td>
</tr>
<tr id="evs_faq_0013_row324318491252"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="evs_faq_0013_p625787911259"><a name="evs_faq_0013_p625787911259"></a><a name="evs_faq_0013_p625787911259"></a>Downloading</p>
</td>
<td class="cellrowborder" valign="top" width="52.129999999999995%" headers="mcps1.2.4.1.2 "><p id="evs_faq_0013_p316876991259"><a name="evs_faq_0013_p316876991259"></a><a name="evs_faq_0013_p316876991259"></a>Data is being downloaded from an image to the EVS disk. This state occurs when you create <span id="evs_faq_0013_text345568229144754"><a name="evs_faq_0013_text345568229144754"></a><a name="evs_faq_0013_text345568229144754"></a>a server</span>.</p>
</td>
<td class="cellrowborder" valign="top" width="29.2%" headers="mcps1.2.4.1.3 "><p id="evs_faq_0013_p167464471259"><a name="evs_faq_0013_p167464471259"></a><a name="evs_faq_0013_p167464471259"></a>None</p>
</td>
</tr>
<tr id="evs_faq_0013_row57957852194514"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="evs_faq_0013_p7460362194521"><a name="evs_faq_0013_p7460362194521"></a><a name="evs_faq_0013_p7460362194521"></a>Error</p>
</td>
<td class="cellrowborder" valign="top" width="52.129999999999995%" headers="mcps1.2.4.1.2 "><p id="evs_faq_0013_p526628519467"><a name="evs_faq_0013_p526628519467"></a><a name="evs_faq_0013_p526628519467"></a>An error occurs when you try to create an EVS disk.</p>
</td>
<td class="cellrowborder" valign="top" width="29.2%" headers="mcps1.2.4.1.3 "><p id="evs_faq_0013_p2242870194521"><a name="evs_faq_0013_p2242870194521"></a><a name="evs_faq_0013_p2242870194521"></a>Deleting</p>
</td>
</tr>
<tr id="evs_faq_0013_row51729329191747"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="evs_faq_0013_p23982637191747"><a name="evs_faq_0013_p23982637191747"></a><a name="evs_faq_0013_p23982637191747"></a>Deletion failed</p>
</td>
<td class="cellrowborder" valign="top" width="52.129999999999995%" headers="mcps1.2.4.1.2 "><p id="evs_faq_0013_p5387879619469"><a name="evs_faq_0013_p5387879619469"></a><a name="evs_faq_0013_p5387879619469"></a>An error occurs when you try to delete the EVS disk.</p>
</td>
<td class="cellrowborder" valign="top" width="29.2%" headers="mcps1.2.4.1.3 "><p id="evs_faq_0013_p56250197191747"><a name="evs_faq_0013_p56250197191747"></a><a name="evs_faq_0013_p56250197191747"></a>None</p>
</td>
</tr>
<tr id="evs_faq_0013_row27894953191747"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="evs_faq_0013_p19344120194636"><a name="evs_faq_0013_p19344120194636"></a><a name="evs_faq_0013_p19344120194636"></a>Expansion failed</p>
</td>
<td class="cellrowborder" valign="top" width="52.129999999999995%" headers="mcps1.2.4.1.2 "><p id="evs_faq_0013_p35675803115140"><a name="evs_faq_0013_p35675803115140"></a><a name="evs_faq_0013_p35675803115140"></a>An error occurs when you try to expand the capacity of the EVS disk.</p>
</td>
<td class="cellrowborder" valign="top" width="29.2%" headers="mcps1.2.4.1.3 "><p id="evs_faq_0013_p35751628194636"><a name="evs_faq_0013_p35751628194636"></a><a name="evs_faq_0013_p35751628194636"></a>Deleting</p>
</td>
</tr>
<tr id="evs_faq_0013_row44239461191747"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="evs_faq_0013_p58879407194641"><a name="evs_faq_0013_p58879407194641"></a><a name="evs_faq_0013_p58879407194641"></a>Restoration failed</p>
</td>
<td class="cellrowborder" valign="top" width="52.129999999999995%" headers="mcps1.2.4.1.2 "><p id="evs_faq_0013_p359073115142"><a name="evs_faq_0013_p359073115142"></a><a name="evs_faq_0013_p359073115142"></a>An error occurs when you try to restore the EVS disk from a backup.</p>
</td>
<td class="cellrowborder" valign="top" width="29.2%" headers="mcps1.2.4.1.3 "><p id="evs_faq_0013_p7528903194641"><a name="evs_faq_0013_p7528903194641"></a><a name="evs_faq_0013_p7528903194641"></a>Deleting</p>
</td>
</tr>
<tr id="evs_faq_0013_row57899957175726"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="evs_faq_0013_p51337573175726"><a name="evs_faq_0013_p51337573175726"></a><a name="evs_faq_0013_p51337573175726"></a>Rolling back</p>
</td>
<td class="cellrowborder" valign="top" width="52.129999999999995%" headers="mcps1.2.4.1.2 "><p id="evs_faq_0013_p3842076519239"><a name="evs_faq_0013_p3842076519239"></a><a name="evs_faq_0013_p3842076519239"></a>Data on the EVS disk is being restored from a snapshot.</p>
<div class="note" id="evs_faq_0013_note1024257119239"><a name="evs_faq_0013_note1024257119239"></a><a name="evs_faq_0013_note1024257119239"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="evs_faq_0013_ul2507428319239"></a><a name="evs_faq_0013_ul2507428319239"></a><ul id="evs_faq_0013_ul2507428319239"><li>When you roll back a snapshot to an EVS disk, you can only roll back the snapshot to the source EVS disk. Rollback to a specified disk is not supported.</li><li>You can roll back an EVS disk from a snapshot only when the disk is in the <span class="wintitle" id="evs_faq_0013_wintitle355923761181956"><a name="evs_faq_0013_wintitle355923761181956"></a><a name="evs_faq_0013_wintitle355923761181956"></a><b>Available</b></span> or <span class="wintitle" id="evs_faq_0013_wintitle698955377181956"><a name="evs_faq_0013_wintitle698955377181956"></a><a name="evs_faq_0013_wintitle698955377181956"></a><b>Rollback failed</b></span> state.</li></ul>
</div></div>
</td>
<td class="cellrowborder" valign="top" width="29.2%" headers="mcps1.2.4.1.3 "><p id="evs_faq_0013_p6428254175726"><a name="evs_faq_0013_p6428254175726"></a><a name="evs_faq_0013_p6428254175726"></a>None</p>
</td>
</tr>
<tr id="evs_faq_0013_row53629027175738"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="evs_faq_0013_p12899196175738"><a name="evs_faq_0013_p12899196175738"></a><a name="evs_faq_0013_p12899196175738"></a>Rollback failed</p>
</td>
<td class="cellrowborder" valign="top" width="52.129999999999995%" headers="mcps1.2.4.1.2 "><p id="evs_faq_0013_p38201995175738"><a name="evs_faq_0013_p38201995175738"></a><a name="evs_faq_0013_p38201995175738"></a>An error occurs when the EVS disk is rolled back from a snapshot.</p>
</td>
<td class="cellrowborder" valign="top" width="29.2%" headers="mcps1.2.4.1.3 "><a name="evs_faq_0013_ul63969149183234"></a><a name="evs_faq_0013_ul63969149183234"></a><ul id="evs_faq_0013_ul63969149183234"><li>Deleting</li><li>Rolling back snapshots to EVS disks</li></ul>
</td>
</tr>
<tr id="evs_faq_0013_row3874810143339"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="evs_faq_0013_p45424225143339"><a name="evs_faq_0013_p45424225143339"></a><a name="evs_faq_0013_p45424225143339"></a>Awaiting transfer</p>
</td>
<td class="cellrowborder" valign="top" width="52.129999999999995%" headers="mcps1.2.4.1.2 "><p id="evs_faq_0013_p55483571143339"><a name="evs_faq_0013_p55483571143339"></a><a name="evs_faq_0013_p55483571143339"></a>The EVS disk is awaiting for a transfer.</p>
</td>
<td class="cellrowborder" valign="top" width="29.2%" headers="mcps1.2.4.1.3 "><p id="evs_faq_0013_p64984282143339"><a name="evs_faq_0013_p64984282143339"></a><a name="evs_faq_0013_p64984282143339"></a>None</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>If an EVS disk status is  **Error**,  **Deletion failed**,  **Expansion failed**,  **Restoration failed**, or  **Rollback failed**, you can rectify the error by following the steps provided in  [What Should I Do If an Error Occurs on My EVS Disk?](what-should-i-do-if-an-error-occurs-on-my-evs-disk.md).  

