# Details of EVS Replication failure\_detail Values \(Deprecated\)<a name="evs_04_0044"></a>

## EVS Replication Pair<a name="section17414955102918"></a>

**Table  1**  Details of the failure\_detail values for EVS replication pairs

<a name="table23861215102932"></a>
<table><thead align="left"><tr id="row14036844102932"><th class="cellrowborder" valign="top" width="21.240000000000002%" id="mcps1.2.5.1.1"><p id="p40290869145455"><a name="p40290869145455"></a><a name="p40290869145455"></a>failure_detail Value</p>
</th>
<th class="cellrowborder" valign="top" width="27.82%" id="mcps1.2.5.1.2"><p id="p5805585814551"><a name="p5805585814551"></a><a name="p5805585814551"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="25.75%" id="mcps1.2.5.1.3"><p id="p5919455214551"><a name="p5919455214551"></a><a name="p5919455214551"></a>Cause</p>
</th>
<th class="cellrowborder" valign="top" width="25.19%" id="mcps1.2.5.1.4"><p id="p6517570414551"><a name="p6517570414551"></a><a name="p6517570414551"></a>Solution</p>
</th>
</tr>
</thead>
<tbody><tr id="row10217201102932"><td class="cellrowborder" valign="top" width="21.240000000000002%" headers="mcps1.2.5.1.1 "><p id="p40369378145532"><a name="p40369378145532"></a><a name="p40369378145532"></a>37100041</p>
</td>
<td class="cellrowborder" valign="top" width="27.82%" headers="mcps1.2.5.1.2 "><p id="p28042648145532"><a name="p28042648145532"></a><a name="p28042648145532"></a>Failed to create the EVS replication pair because the production disk capacity is inconsistent with the DR disk capacity.</p>
</td>
<td class="cellrowborder" valign="top" width="25.75%" headers="mcps1.2.5.1.3 "><p id="p45075634145532"><a name="p45075634145532"></a><a name="p45075634145532"></a>The production disk capacity is inconsistent with the DR disk capacity.</p>
</td>
<td class="cellrowborder" valign="top" width="25.19%" headers="mcps1.2.5.1.4 "><p id="p53724256145532"><a name="p53724256145532"></a><a name="p53724256145532"></a>Ensure that the capacities of the production and DR disks are consistent before you create the EVS replication pair.</p>
</td>
</tr>
<tr id="row55993359102932"><td class="cellrowborder" valign="top" width="21.240000000000002%" headers="mcps1.2.5.1.1 "><p id="p929784145532"><a name="p929784145532"></a><a name="p929784145532"></a>37100043</p>
<p id="p26799413145532"><a name="p26799413145532"></a><a name="p26799413145532"></a></p>
</td>
<td class="cellrowborder" valign="top" width="27.82%" headers="mcps1.2.5.1.2 "><p id="p46410217145532"><a name="p46410217145532"></a><a name="p46410217145532"></a>The operation fails because messages failed to be sent to the peer AZ.</p>
</td>
<td class="cellrowborder" valign="top" width="25.75%" headers="mcps1.2.5.1.3 "><p id="p44704294145532"><a name="p44704294145532"></a><a name="p44704294145532"></a>A communication error occurred.</p>
</td>
<td class="cellrowborder" valign="top" width="25.19%" headers="mcps1.2.5.1.4 "><p id="p23777953145532"><a name="p23777953145532"></a><a name="p23777953145532"></a>Contact technical support to check whether the link status is normal.</p>
</td>
</tr>
<tr id="row11603133102932"><td class="cellrowborder" valign="top" width="21.240000000000002%" headers="mcps1.2.5.1.1 "><p id="p23082629145532"><a name="p23082629145532"></a><a name="p23082629145532"></a>37100044</p>
</td>
<td class="cellrowborder" valign="top" width="27.82%" headers="mcps1.2.5.1.2 "><p id="p48003677145532"><a name="p48003677145532"></a><a name="p48003677145532"></a>Failed to create the EVS replication pair because the specified production disk is a lazyloading EVS disk.</p>
</td>
<td class="cellrowborder" valign="top" width="25.75%" headers="mcps1.2.5.1.3 "><p id="p59247376145532"><a name="p59247376145532"></a><a name="p59247376145532"></a>Lazyloading EVS disks cannot be used as member disks of EVS replication pairs.</p>
</td>
<td class="cellrowborder" valign="top" width="25.19%" headers="mcps1.2.5.1.4 "><p id="p55465145532"><a name="p55465145532"></a><a name="p55465145532"></a>Wait until the lazyloading process is complete and try again. If the fault persists, contact technical support.</p>
</td>
</tr>
<tr id="row60539153145510"><td class="cellrowborder" valign="top" width="21.240000000000002%" headers="mcps1.2.5.1.1 "><p id="p11763765145626"><a name="p11763765145626"></a><a name="p11763765145626"></a>37100045</p>
</td>
<td class="cellrowborder" valign="top" width="27.82%" headers="mcps1.2.5.1.2 "><p id="p11520644145626"><a name="p11520644145626"></a><a name="p11520644145626"></a>Failed to create the EVS replication pair because the specified DR disk is a lazyloading EVS disk.</p>
</td>
<td class="cellrowborder" valign="top" width="25.75%" headers="mcps1.2.5.1.3 "><p id="p14470972145626"><a name="p14470972145626"></a><a name="p14470972145626"></a>Lazyloading EVS disks cannot be used as member disks of EVS replication pairs.</p>
</td>
<td class="cellrowborder" valign="top" width="25.19%" headers="mcps1.2.5.1.4 "><p id="p45998059145626"><a name="p45998059145626"></a><a name="p45998059145626"></a>Wait until the lazyloading process is complete and try again. If the fault persists, contact technical support.</p>
</td>
</tr>
<tr id="row1115018145510"><td class="cellrowborder" valign="top" width="21.240000000000002%" headers="mcps1.2.5.1.1 "><p id="p17560533145626"><a name="p17560533145626"></a><a name="p17560533145626"></a>37100048</p>
</td>
<td class="cellrowborder" valign="top" width="27.82%" headers="mcps1.2.5.1.2 "><p id="p21442306145626"><a name="p21442306145626"></a><a name="p21442306145626"></a>Failed to create the EVS replication pair because the specified production disk does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="25.75%" headers="mcps1.2.5.1.3 "><p id="p25179875145626"><a name="p25179875145626"></a><a name="p25179875145626"></a>The specified production disk does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="25.19%" headers="mcps1.2.5.1.4 "><p id="p34289999145626"><a name="p34289999145626"></a><a name="p34289999145626"></a>Specify an existing production disk.</p>
</td>
</tr>
<tr id="row64755057145515"><td class="cellrowborder" valign="top" width="21.240000000000002%" headers="mcps1.2.5.1.1 "><p id="p46675664145716"><a name="p46675664145716"></a><a name="p46675664145716"></a>37100050</p>
</td>
<td class="cellrowborder" valign="top" width="27.82%" headers="mcps1.2.5.1.2 "><p id="p1059820145716"><a name="p1059820145716"></a><a name="p1059820145716"></a>Failed to create the EVS replication pair because the specified DR disk does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="25.75%" headers="mcps1.2.5.1.3 "><p id="p6697833145716"><a name="p6697833145716"></a><a name="p6697833145716"></a>The specified DR disk does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="25.19%" headers="mcps1.2.5.1.4 "><p id="p7774229145716"><a name="p7774229145716"></a><a name="p7774229145716"></a>Specify an existing DR disk.</p>
</td>
</tr>
<tr id="row6460838145515"><td class="cellrowborder" valign="top" width="21.240000000000002%" headers="mcps1.2.5.1.1 "><p id="p22006260145741"><a name="p22006260145741"></a><a name="p22006260145741"></a>37100053</p>
</td>
<td class="cellrowborder" valign="top" width="27.82%" headers="mcps1.2.5.1.2 "><p id="p6716788145741"><a name="p6716788145741"></a><a name="p6716788145741"></a>Failed to create the EVS replication pair because the specified production disk has been used in another EVS replication pair.</p>
</td>
<td class="cellrowborder" valign="top" width="25.75%" headers="mcps1.2.5.1.3 "><p id="p66920122145741"><a name="p66920122145741"></a><a name="p66920122145741"></a>The specified production disk is the member disk in another EVS replication pair.</p>
</td>
<td class="cellrowborder" valign="top" width="25.19%" headers="mcps1.2.5.1.4 "><p id="p20807885145741"><a name="p20807885145741"></a><a name="p20807885145741"></a>Specify a production disk that has not been used by another EVS replication pair.</p>
</td>
</tr>
<tr id="row34988264145515"><td class="cellrowborder" valign="top" width="21.240000000000002%" headers="mcps1.2.5.1.1 "><p id="p55594349145741"><a name="p55594349145741"></a><a name="p55594349145741"></a>37100054</p>
</td>
<td class="cellrowborder" valign="top" width="27.82%" headers="mcps1.2.5.1.2 "><p id="p48059566145741"><a name="p48059566145741"></a><a name="p48059566145741"></a>Failed to create the EVS replication pair because the specified DR disk has been used in another EVS replication pair.</p>
</td>
<td class="cellrowborder" valign="top" width="25.75%" headers="mcps1.2.5.1.3 "><p id="p25389695145741"><a name="p25389695145741"></a><a name="p25389695145741"></a>The specified DR disk is the member disk in another EVS replication pair.</p>
</td>
<td class="cellrowborder" valign="top" width="25.19%" headers="mcps1.2.5.1.4 "><p id="p27175549145741"><a name="p27175549145741"></a><a name="p27175549145741"></a>Specify a DR disk that has not been used by another EVS replication pair.</p>
</td>
</tr>
<tr id="row52601337105626"><td class="cellrowborder" valign="top" width="21.240000000000002%" headers="mcps1.2.5.1.1 "><p id="p1670396105633"><a name="p1670396105633"></a><a name="p1670396105633"></a>37100058</p>
</td>
<td class="cellrowborder" valign="top" width="27.82%" headers="mcps1.2.5.1.2 "><p id="p1084393105633"><a name="p1084393105633"></a><a name="p1084393105633"></a>Failed to create the EVS replication pair because the DR disk has been attached to a server and the server is in the <strong id="b842352706144538"><a name="b842352706144538"></a><a name="b842352706144538"></a>Running</strong> state.</p>
</td>
<td class="cellrowborder" valign="top" width="25.75%" headers="mcps1.2.5.1.3 "><p id="p20727027105633"><a name="p20727027105633"></a><a name="p20727027105633"></a>The specified DR disk has been attached to a server and the server is in the <strong id="b842352706144620"><a name="b842352706144620"></a><a name="b842352706144620"></a>Running</strong> state.</p>
</td>
<td class="cellrowborder" valign="top" width="25.19%" headers="mcps1.2.5.1.4 "><p id="p1167617105633"><a name="p1167617105633"></a><a name="p1167617105633"></a>Stop the server , or specify a DR disk that has not been attached to any server.</p>
</td>
</tr>
<tr id="row24248420145519"><td class="cellrowborder" valign="top" width="21.240000000000002%" headers="mcps1.2.5.1.1 "><p id="p4688985414592"><a name="p4688985414592"></a><a name="p4688985414592"></a>37100177</p>
</td>
<td class="cellrowborder" valign="top" width="27.82%" headers="mcps1.2.5.1.2 "><p id="p3853521514592"><a name="p3853521514592"></a><a name="p3853521514592"></a>Failed to create the EVS replication pair because the storage pool status of the primary AZ is abnormal.</p>
</td>
<td class="cellrowborder" valign="top" width="25.75%" headers="mcps1.2.5.1.3 "><p id="p4112101314592"><a name="p4112101314592"></a><a name="p4112101314592"></a>The storage pool status of the primary AZ is abnormal.</p>
</td>
<td class="cellrowborder" valign="top" width="25.19%" headers="mcps1.2.5.1.4 "><p id="p498969615361"><a name="p498969615361"></a><a name="p498969615361"></a>Create the EVS replication pair when the storage pool status is normal. If the fault persists, contact technical support.</p>
</td>
</tr>
<tr id="row37051972145519"><td class="cellrowborder" valign="top" width="21.240000000000002%" headers="mcps1.2.5.1.1 "><p id="p6298239314592"><a name="p6298239314592"></a><a name="p6298239314592"></a>37100178</p>
</td>
<td class="cellrowborder" valign="top" width="27.82%" headers="mcps1.2.5.1.2 "><p id="p5024054414592"><a name="p5024054414592"></a><a name="p5024054414592"></a>Failed to create the EVS replication pair because the storage pool status of the secondary AZ is abnormal.</p>
</td>
<td class="cellrowborder" valign="top" width="25.75%" headers="mcps1.2.5.1.3 "><p id="p6051324514592"><a name="p6051324514592"></a><a name="p6051324514592"></a>The storage pool status of the secondary AZ is abnormal.</p>
</td>
<td class="cellrowborder" valign="top" width="25.19%" headers="mcps1.2.5.1.4 "><p id="p2828770914592"><a name="p2828770914592"></a><a name="p2828770914592"></a>Create the EVS replication pair when the storage pool status is normal. If the fault persists, contact technical support.</p>
</td>
</tr>
<tr id="row22330620145519"><td class="cellrowborder" valign="top" width="21.240000000000002%" headers="mcps1.2.5.1.1 "><p id="p4857558515044"><a name="p4857558515044"></a><a name="p4857558515044"></a>37000212</p>
</td>
<td class="cellrowborder" valign="top" width="27.82%" headers="mcps1.2.5.1.2 "><p id="p5479967415044"><a name="p5479967415044"></a><a name="p5479967415044"></a>System internal processing failure.</p>
</td>
<td class="cellrowborder" valign="top" width="25.75%" headers="mcps1.2.5.1.3 "><p id="p6175227615044"><a name="p6175227615044"></a><a name="p6175227615044"></a>An internal system error occurred.</p>
</td>
<td class="cellrowborder" valign="top" width="25.19%" headers="mcps1.2.5.1.4 "><p id="p5117443615044"><a name="p5117443615044"></a><a name="p5117443615044"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row34244122145519"><td class="cellrowborder" valign="top" width="21.240000000000002%" headers="mcps1.2.5.1.1 "><p id="p5460704815044"><a name="p5460704815044"></a><a name="p5460704815044"></a>37000216</p>
</td>
<td class="cellrowborder" valign="top" width="27.82%" headers="mcps1.2.5.1.2 "><p id="p4292943415044"><a name="p4292943415044"></a><a name="p4292943415044"></a>The system is busy. Try again later.</p>
</td>
<td class="cellrowborder" valign="top" width="25.75%" headers="mcps1.2.5.1.3 "><p id="p3782230115044"><a name="p3782230115044"></a><a name="p3782230115044"></a>The system is busy. Try again later.</p>
</td>
<td class="cellrowborder" valign="top" width="25.19%" headers="mcps1.2.5.1.4 "><p id="p1643926415044"><a name="p1643926415044"></a><a name="p1643926415044"></a>Try again later. If the fault persists, contact technical support.</p>
</td>
</tr>
</tbody>
</table>

## Replication Consistency Group<a name="section27959400102950"></a>

**Table  2**  Details of the failure\_detail values for replication consistency groups

<a name="table12187075103114"></a>
<table><thead align="left"><tr id="row45300301103114"><th class="cellrowborder" valign="top" width="21.240000000000002%" id="mcps1.2.5.1.1"><p id="p133014131513"><a name="p133014131513"></a><a name="p133014131513"></a>failure_detail Value</p>
</th>
<th class="cellrowborder" valign="top" width="28.01%" id="mcps1.2.5.1.2"><p id="p607028991513"><a name="p607028991513"></a><a name="p607028991513"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="25.75%" id="mcps1.2.5.1.3"><p id="p167847311513"><a name="p167847311513"></a><a name="p167847311513"></a>Cause</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p263389101513"><a name="p263389101513"></a><a name="p263389101513"></a>Solution</p>
</th>
</tr>
</thead>
<tbody><tr id="row55752712103114"><td class="cellrowborder" valign="top" width="21.240000000000002%" headers="mcps1.2.5.1.1 "><p id="p3017795615128"><a name="p3017795615128"></a><a name="p3017795615128"></a>37100017</p>
</td>
<td class="cellrowborder" valign="top" width="28.01%" headers="mcps1.2.5.1.2 "><p id="p14667222181243"><a name="p14667222181243"></a><a name="p14667222181243"></a>Failed to create the replication consistency group because the number of replication consistency groups in the primary AZ has reached the upper limit.</p>
<p id="p64896139181243"><a name="p64896139181243"></a><a name="p64896139181243"></a></p>
</td>
<td class="cellrowborder" valign="top" width="25.75%" headers="mcps1.2.5.1.3 "><p id="p22095930181243"><a name="p22095930181243"></a><a name="p22095930181243"></a>The number of replication consistency groups in the primary AZ has reached the upper limit.</p>
<p id="p64645645181243"><a name="p64645645181243"></a><a name="p64645645181243"></a></p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p1805930181243"><a name="p1805930181243"></a><a name="p1805930181243"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row17237398103114"><td class="cellrowborder" valign="top" width="21.240000000000002%" headers="mcps1.2.5.1.1 "><p id="p5903457615128"><a name="p5903457615128"></a><a name="p5903457615128"></a>37100043</p>
<p id="p5691220715128"><a name="p5691220715128"></a><a name="p5691220715128"></a></p>
</td>
<td class="cellrowborder" valign="top" width="28.01%" headers="mcps1.2.5.1.2 "><p id="p264257915128"><a name="p264257915128"></a><a name="p264257915128"></a>The operation fails because messages failed to be sent to the peer AZ.</p>
</td>
<td class="cellrowborder" valign="top" width="25.75%" headers="mcps1.2.5.1.3 "><p id="p4629503215128"><a name="p4629503215128"></a><a name="p4629503215128"></a>The communication between the primary AZ and secondary AZ fails.</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p5879713215128"><a name="p5879713215128"></a><a name="p5879713215128"></a>Contact technical support to check whether the link status is normal.</p>
</td>
</tr>
<tr id="row3420472103114"><td class="cellrowborder" valign="top" width="21.240000000000002%" headers="mcps1.2.5.1.1 "><p id="p1635565715128"><a name="p1635565715128"></a><a name="p1635565715128"></a>37100159</p>
<p id="p4130864715128"><a name="p4130864715128"></a><a name="p4130864715128"></a></p>
</td>
<td class="cellrowborder" valign="top" width="28.01%" headers="mcps1.2.5.1.2 "><p id="p1295959915128"><a name="p1295959915128"></a><a name="p1295959915128"></a>Failed to create the replication consistency group because the number of replication consistency groups in the secondary AZ has reached the upper limit.</p>
<p id="p6352319715128"><a name="p6352319715128"></a><a name="p6352319715128"></a></p>
</td>
<td class="cellrowborder" valign="top" width="25.75%" headers="mcps1.2.5.1.3 "><p id="p6405864815128"><a name="p6405864815128"></a><a name="p6405864815128"></a>The number of replication consistency groups in the secondary AZ has reached the upper limit.</p>
<p id="p2326075615128"><a name="p2326075615128"></a><a name="p2326075615128"></a></p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p5314504915128"><a name="p5314504915128"></a><a name="p5314504915128"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row1805546315134"><td class="cellrowborder" valign="top" width="21.240000000000002%" headers="mcps1.2.5.1.1 "><p id="p37322115150"><a name="p37322115150"></a><a name="p37322115150"></a>37000212</p>
</td>
<td class="cellrowborder" valign="top" width="28.01%" headers="mcps1.2.5.1.2 "><p id="p4913789215150"><a name="p4913789215150"></a><a name="p4913789215150"></a>System internal processing failure.</p>
</td>
<td class="cellrowborder" valign="top" width="25.75%" headers="mcps1.2.5.1.3 "><p id="p1953506215150"><a name="p1953506215150"></a><a name="p1953506215150"></a>An internal system error occurred.</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p3095391315150"><a name="p3095391315150"></a><a name="p3095391315150"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row5388191515134"><td class="cellrowborder" valign="top" width="21.240000000000002%" headers="mcps1.2.5.1.1 "><p id="p3821921615150"><a name="p3821921615150"></a><a name="p3821921615150"></a>37000216</p>
</td>
<td class="cellrowborder" valign="top" width="28.01%" headers="mcps1.2.5.1.2 "><p id="p3883909215150"><a name="p3883909215150"></a><a name="p3883909215150"></a>The system is busy. Try again later.</p>
</td>
<td class="cellrowborder" valign="top" width="25.75%" headers="mcps1.2.5.1.3 "><p id="p5395680815150"><a name="p5395680815150"></a><a name="p5395680815150"></a>The system is busy. Try again later.</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p5360665815150"><a name="p5360665815150"></a><a name="p5360665815150"></a>Try again later. If the fault persists, contact technical support.</p>
</td>
</tr>
</tbody>
</table>

