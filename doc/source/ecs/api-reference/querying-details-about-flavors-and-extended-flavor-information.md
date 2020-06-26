# Querying Details About Flavors and Extended Flavor Information<a name="EN-US_TOPIC_0020212656"></a>

## Function<a name="section19330484"></a>

This API is used to query details about ECS flavors and extended flavor information. 

## URI<a name="section39756633"></a>

GET /v1/\{project\_id\}/cloudservers/flavors\{?availability\_zone\}

[Table 1](#table50905282)  describes the parameters in the URI.

**Table  1**  Path parameters

<a name="table50905282"></a>
<table><thead align="left"><tr id="row27788708"><th class="cellrowborder" valign="top" width="16.61%" id="mcps1.2.4.1.1"><p id="p36292894"><a name="p36292894"></a><a name="p36292894"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.54%" id="mcps1.2.4.1.2"><p id="p54043292"><a name="p54043292"></a><a name="p54043292"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.85%" id="mcps1.2.4.1.3"><p id="p15430535"><a name="p15430535"></a><a name="p15430535"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row41913798"><td class="cellrowborder" valign="top" width="16.61%" headers="mcps1.2.4.1.1 "><p id="p39574466"><a name="p39574466"></a><a name="p39574466"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.54%" headers="mcps1.2.4.1.2 "><p id="p51415138"><a name="p51415138"></a><a name="p51415138"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.85%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  Query parameters

<a name="table49939793"></a>
<table><thead align="left"><tr id="row40936054"><th class="cellrowborder" valign="top" width="16.521652165216523%" id="mcps1.2.5.1.1"><p id="p27486043"><a name="p27486043"></a><a name="p27486043"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.731773177317734%" id="mcps1.2.5.1.2"><p id="p11776988"><a name="p11776988"></a><a name="p11776988"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13.381338133813381%" id="mcps1.2.5.1.3"><p id="p14412003"><a name="p14412003"></a><a name="p14412003"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="52.36523652365236%" id="mcps1.2.5.1.4"><p id="p37367427"><a name="p37367427"></a><a name="p37367427"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row762524"><td class="cellrowborder" valign="top" width="16.521652165216523%" headers="mcps1.2.5.1.1 "><p id="p157004471157"><a name="p157004471157"></a><a name="p157004471157"></a>availability_zone</p>
</td>
<td class="cellrowborder" valign="top" width="17.731773177317734%" headers="mcps1.2.5.1.2 "><p id="p36869576"><a name="p36869576"></a><a name="p36869576"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.381338133813381%" headers="mcps1.2.5.1.3 "><p id="p33645693"><a name="p33645693"></a><a name="p33645693"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.36523652365236%" headers="mcps1.2.5.1.4 "><p id="p32975066"><a name="p32975066"></a><a name="p32975066"></a>Specifies the AZ name, ID, or code.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section1132155716387"></a>

None

## Response<a name="section66170694"></a>

[Table 3](#table17679057)  describes the response parameters.

**Table  3**  Response parameters

<a name="table17679057"></a>
<table><thead align="left"><tr id="row9548790"><th class="cellrowborder" valign="top" width="20.05%" id="mcps1.2.4.1.1"><p id="p35254491"><a name="p35254491"></a><a name="p35254491"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15.909999999999998%" id="mcps1.2.4.1.2"><p id="p47571555"><a name="p47571555"></a><a name="p47571555"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.03999999999999%" id="mcps1.2.4.1.3"><p id="p28090709"><a name="p28090709"></a><a name="p28090709"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row60754972"><td class="cellrowborder" valign="top" width="20.05%" headers="mcps1.2.4.1.1 "><p id="p22205728"><a name="p22205728"></a><a name="p22205728"></a>flavors</p>
</td>
<td class="cellrowborder" valign="top" width="15.909999999999998%" headers="mcps1.2.4.1.2 "><p id="p65549821"><a name="p65549821"></a><a name="p65549821"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="64.03999999999999%" headers="mcps1.2.4.1.3 "><p id="p4308570"><a name="p4308570"></a><a name="p4308570"></a>Specifies ECS flavors. For details, see <a href="#table15697576">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **flavors**  field description

<a name="table15697576"></a>
<table><thead align="left"><tr id="row27618155"><th class="cellrowborder" valign="top" width="19.918008199180083%" id="mcps1.2.4.1.1"><p id="p1836575115412"><a name="p1836575115412"></a><a name="p1836575115412"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.008399160083993%" id="mcps1.2.4.1.2"><p id="p16365253545"><a name="p16365253545"></a><a name="p16365253545"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.07359264073594%" id="mcps1.2.4.1.3"><p id="p73815535419"><a name="p73815535419"></a><a name="p73815535419"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row56771492"><td class="cellrowborder" valign="top" width="19.918008199180083%" headers="mcps1.2.4.1.1 "><p id="p2508360173425"><a name="p2508360173425"></a><a name="p2508360173425"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16.008399160083993%" headers="mcps1.2.4.1.2 "><p id="p1850582173425"><a name="p1850582173425"></a><a name="p1850582173425"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.07359264073594%" headers="mcps1.2.4.1.3 "><p id="p6897056173425"><a name="p6897056173425"></a><a name="p6897056173425"></a>Specifies the ID of the ECS flavor.</p>
</td>
</tr>
<tr id="row49957660"><td class="cellrowborder" valign="top" width="19.918008199180083%" headers="mcps1.2.4.1.1 "><p id="p61898162173425"><a name="p61898162173425"></a><a name="p61898162173425"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.008399160083993%" headers="mcps1.2.4.1.2 "><p id="p47695250173425"><a name="p47695250173425"></a><a name="p47695250173425"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.07359264073594%" headers="mcps1.2.4.1.3 "><p id="p7446212173425"><a name="p7446212173425"></a><a name="p7446212173425"></a>Specifies the name of the ECS flavor.</p>
</td>
</tr>
<tr id="row43901854"><td class="cellrowborder" valign="top" width="19.918008199180083%" headers="mcps1.2.4.1.1 "><p id="p59579429173425"><a name="p59579429173425"></a><a name="p59579429173425"></a>vcpus</p>
</td>
<td class="cellrowborder" valign="top" width="16.008399160083993%" headers="mcps1.2.4.1.2 "><p id="p61204439173425"><a name="p61204439173425"></a><a name="p61204439173425"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.07359264073594%" headers="mcps1.2.4.1.3 "><p id="p57750575173425"><a name="p57750575173425"></a><a name="p57750575173425"></a>Specifies the number of vCPUs in the ECS flavor.</p>
</td>
</tr>
<tr id="row3995878295757"><td class="cellrowborder" valign="top" width="19.918008199180083%" headers="mcps1.2.4.1.1 "><p id="p22911904173425"><a name="p22911904173425"></a><a name="p22911904173425"></a>ram</p>
</td>
<td class="cellrowborder" valign="top" width="16.008399160083993%" headers="mcps1.2.4.1.2 "><p id="p43924899173425"><a name="p43924899173425"></a><a name="p43924899173425"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="64.07359264073594%" headers="mcps1.2.4.1.3 "><p id="p10323939173425"><a name="p10323939173425"></a><a name="p10323939173425"></a>Specifies the memory size (MB) in the ECS flavor.</p>
</td>
</tr>
<tr id="row61114224"><td class="cellrowborder" valign="top" width="19.918008199180083%" headers="mcps1.2.4.1.1 "><p id="p9958946173425"><a name="p9958946173425"></a><a name="p9958946173425"></a>disk</p>
</td>
<td class="cellrowborder" valign="top" width="16.008399160083993%" headers="mcps1.2.4.1.2 "><p id="p1368312173425"><a name="p1368312173425"></a><a name="p1368312173425"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.07359264073594%" headers="mcps1.2.4.1.3 "><p id="p57975774173425"><a name="p57975774173425"></a><a name="p57975774173425"></a>Specifies the system disk size in the ECS flavor.</p>
<p id="p52019925173425"><a name="p52019925173425"></a><a name="p52019925173425"></a>This parameter has not been used. Its default value is <strong id="b84235270611135"><a name="b84235270611135"></a><a name="b84235270611135"></a>0</strong>.</p>
</td>
</tr>
<tr id="row5177538310057"><td class="cellrowborder" valign="top" width="19.918008199180083%" headers="mcps1.2.4.1.1 "><p id="p6017815173425"><a name="p6017815173425"></a><a name="p6017815173425"></a>swap</p>
</td>
<td class="cellrowborder" valign="top" width="16.008399160083993%" headers="mcps1.2.4.1.2 "><p id="p17681022173425"><a name="p17681022173425"></a><a name="p17681022173425"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.07359264073594%" headers="mcps1.2.4.1.3 "><p id="p1699362755013"><a name="p1699362755013"></a><a name="p1699362755013"></a>Specifies the swap partition size required by the ECS flavor.</p>
<p id="p4563766173425"><a name="p4563766173425"></a><a name="p4563766173425"></a>This parameter has not been used. Its default value is <strong id="b358926685"><a name="b358926685"></a><a name="b358926685"></a>""</strong>.</p>
</td>
</tr>
<tr id="row3524039010057"><td class="cellrowborder" valign="top" width="19.918008199180083%" headers="mcps1.2.4.1.1 "><p id="p38651455173425"><a name="p38651455173425"></a><a name="p38651455173425"></a>OS-FLV-EXT-DATA:ephemeral</p>
</td>
<td class="cellrowborder" valign="top" width="16.008399160083993%" headers="mcps1.2.4.1.2 "><p id="p43760136173425"><a name="p43760136173425"></a><a name="p43760136173425"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="64.07359264073594%" headers="mcps1.2.4.1.3 "><p id="p16591226713"><a name="p16591226713"></a><a name="p16591226713"></a>Specifies the temporary disk size. This is an extended attribute.</p>
<p id="p1140814148017"><a name="p1140814148017"></a><a name="p1140814148017"></a>This parameter has not been used. Its default value is <strong id="b377842783"><a name="b377842783"></a><a name="b377842783"></a>0</strong>.</p>
</td>
</tr>
<tr id="row4118343910057"><td class="cellrowborder" valign="top" width="19.918008199180083%" headers="mcps1.2.4.1.1 "><p id="p24955566173425"><a name="p24955566173425"></a><a name="p24955566173425"></a>OS-FLV-DISABLED:disabled</p>
</td>
<td class="cellrowborder" valign="top" width="16.008399160083993%" headers="mcps1.2.4.1.2 "><p id="p8135002173425"><a name="p8135002173425"></a><a name="p8135002173425"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="64.07359264073594%" headers="mcps1.2.4.1.3 "><p id="p32761310192019"><a name="p32761310192019"></a><a name="p32761310192019"></a>Specifies whether the ECS flavor has been disabled. This is an extended attribute.</p>
<p id="p182115151112"><a name="p182115151112"></a><a name="p182115151112"></a>This parameter has not been used. Its default value is <strong id="b676206732"><a name="b676206732"></a><a name="b676206732"></a>false</strong>.</p>
</td>
</tr>
<tr id="row5681826310045"><td class="cellrowborder" valign="top" width="19.918008199180083%" headers="mcps1.2.4.1.1 "><p id="p53520998173425"><a name="p53520998173425"></a><a name="p53520998173425"></a>rxtx_factor</p>
</td>
<td class="cellrowborder" valign="top" width="16.008399160083993%" headers="mcps1.2.4.1.2 "><p id="p40233587173425"><a name="p40233587173425"></a><a name="p40233587173425"></a>Float</p>
</td>
<td class="cellrowborder" valign="top" width="64.07359264073594%" headers="mcps1.2.4.1.3 "><p id="p16772171313154"><a name="p16772171313154"></a><a name="p16772171313154"></a>Specifies the ratio of the available network bandwidth to the network hardware bandwidth of the ECS.</p>
<p id="p3711880173425"><a name="p3711880173425"></a><a name="p3711880173425"></a>This parameter has not been used. Its default value is <strong id="b2098547183"><a name="b2098547183"></a><a name="b2098547183"></a>1.0</strong>.</p>
</td>
</tr>
<tr id="row4759361810041"><td class="cellrowborder" valign="top" width="19.918008199180083%" headers="mcps1.2.4.1.1 "><p id="p21606246173425"><a name="p21606246173425"></a><a name="p21606246173425"></a>rxtx_quota</p>
</td>
<td class="cellrowborder" valign="top" width="16.008399160083993%" headers="mcps1.2.4.1.2 "><p id="p5275477173425"><a name="p5275477173425"></a><a name="p5275477173425"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.07359264073594%" headers="mcps1.2.4.1.3 "><p id="p3137170105719"><a name="p3137170105719"></a><a name="p3137170105719"></a>Specifies the software constraints of the network bandwidth that can be used by the ECS.</p>
<p id="p20617737173425"><a name="p20617737173425"></a><a name="p20617737173425"></a>This parameter has not been used. Its default value is <strong id="b169907274"><a name="b169907274"></a><a name="b169907274"></a>null</strong>.</p>
</td>
</tr>
<tr id="row310961201014"><td class="cellrowborder" valign="top" width="19.918008199180083%" headers="mcps1.2.4.1.1 "><p id="p65053613173425"><a name="p65053613173425"></a><a name="p65053613173425"></a>rxtx_cap</p>
</td>
<td class="cellrowborder" valign="top" width="16.008399160083993%" headers="mcps1.2.4.1.2 "><p id="p34851326173425"><a name="p34851326173425"></a><a name="p34851326173425"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.07359264073594%" headers="mcps1.2.4.1.3 "><p id="p928015325585"><a name="p928015325585"></a><a name="p928015325585"></a>Specifies the hardware constraints of the network bandwidth that can be used by the ECS.</p>
<p id="p39466769173425"><a name="p39466769173425"></a><a name="p39466769173425"></a>This parameter has not been used. Its default value is <strong id="b1238015247"><a name="b1238015247"></a><a name="b1238015247"></a>null</strong>.</p>
</td>
</tr>
<tr id="row2314399310037"><td class="cellrowborder" valign="top" width="19.918008199180083%" headers="mcps1.2.4.1.1 "><p id="p48681277173425"><a name="p48681277173425"></a><a name="p48681277173425"></a>os-flavor-access:is_public</p>
</td>
<td class="cellrowborder" valign="top" width="16.008399160083993%" headers="mcps1.2.4.1.2 "><p id="p50869360173425"><a name="p50869360173425"></a><a name="p50869360173425"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="64.07359264073594%" headers="mcps1.2.4.1.3 "><p id="p8894218182818"><a name="p8894218182818"></a><a name="p8894218182818"></a>Specifies whether a flavor is available to all tenants. This is an extended attribute.</p>
<a name="ul1474014143815"></a><a name="ul1474014143815"></a><ul id="ul1474014143815"><li><strong id="b84235270620200"><a name="b84235270620200"></a><a name="b84235270620200"></a>true</strong>: indicates that a flavor is available to all tenants.</li><li><strong id="b1256067637"><a name="b1256067637"></a><a name="b1256067637"></a>false</strong>: indicates that a flavor is available only to certain tenants.</li></ul>
<p id="p35038271466"><a name="p35038271466"></a><a name="p35038271466"></a>Default value: <strong id="b842352706115252"><a name="b842352706115252"></a><a name="b842352706115252"></a>true</strong></p>
</td>
</tr>
<tr id="row4704833194529"><td class="cellrowborder" valign="top" width="19.918008199180083%" headers="mcps1.2.4.1.1 "><p id="p44974357194532"><a name="p44974357194532"></a><a name="p44974357194532"></a>links</p>
</td>
<td class="cellrowborder" valign="top" width="16.008399160083993%" headers="mcps1.2.4.1.2 "><p id="p19044305194532"><a name="p19044305194532"></a><a name="p19044305194532"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="64.07359264073594%" headers="mcps1.2.4.1.3 "><p id="p58872692194532"><a name="p58872692194532"></a><a name="p58872692194532"></a>Specifies shortcut links for ECS flavors. For details, see <a href="#table35958848194647">Table 5</a>.</p>
</td>
</tr>
<tr id="row3802258"><td class="cellrowborder" valign="top" width="19.918008199180083%" headers="mcps1.2.4.1.1 "><p id="p39547486"><a name="p39547486"></a><a name="p39547486"></a>os_extra_specs</p>
</td>
<td class="cellrowborder" valign="top" width="16.008399160083993%" headers="mcps1.2.4.1.2 "><p id="p28190407"><a name="p28190407"></a><a name="p28190407"></a>Objects</p>
</td>
<td class="cellrowborder" valign="top" width="64.07359264073594%" headers="mcps1.2.4.1.3 "><p id="p15494878"><a name="p15494878"></a><a name="p15494878"></a>Specifies extended ECS specifications. For details, see <a href="#table59078165">Table 6</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **links**  field description

<a name="table35958848194647"></a>
<table><thead align="left"><tr id="row19152007194647"><th class="cellrowborder" valign="top" width="19.869999999999997%" id="mcps1.2.4.1.1"><p id="p7605141111549"><a name="p7605141111549"></a><a name="p7605141111549"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.11%" id="mcps1.2.4.1.2"><p id="p660511110547"><a name="p660511110547"></a><a name="p660511110547"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.02%" id="mcps1.2.4.1.3"><p id="p1762111111546"><a name="p1762111111546"></a><a name="p1762111111546"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row319269194647"><td class="cellrowborder" valign="top" width="19.869999999999997%" headers="mcps1.2.4.1.1 "><p id="p25860791194647"><a name="p25860791194647"></a><a name="p25860791194647"></a>rel</p>
</td>
<td class="cellrowborder" valign="top" width="16.11%" headers="mcps1.2.4.1.2 "><p id="p14349342194647"><a name="p14349342194647"></a><a name="p14349342194647"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.02%" headers="mcps1.2.4.1.3 "><p id="p21446082194647"><a name="p21446082194647"></a><a name="p21446082194647"></a>Specifies the shortcut link marker name.</p>
</td>
</tr>
<tr id="row58797014194647"><td class="cellrowborder" valign="top" width="19.869999999999997%" headers="mcps1.2.4.1.1 "><p id="p64937695194647"><a name="p64937695194647"></a><a name="p64937695194647"></a>href</p>
</td>
<td class="cellrowborder" valign="top" width="16.11%" headers="mcps1.2.4.1.2 "><p id="p25461977194647"><a name="p25461977194647"></a><a name="p25461977194647"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.02%" headers="mcps1.2.4.1.3 "><p id="p49154284194647"><a name="p49154284194647"></a><a name="p49154284194647"></a>Provides the corresponding shortcut link.</p>
</td>
</tr>
<tr id="row15939343171451"><td class="cellrowborder" valign="top" width="19.869999999999997%" headers="mcps1.2.4.1.1 "><p id="p16018444171451"><a name="p16018444171451"></a><a name="p16018444171451"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="16.11%" headers="mcps1.2.4.1.2 "><p id="p22425577171451"><a name="p22425577171451"></a><a name="p22425577171451"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.02%" headers="mcps1.2.4.1.3 "><p id="p4532430171451"><a name="p4532430171451"></a><a name="p4532430171451"></a>Specifies the shortcut link type. This parameter has not been used. Its default value is <strong id="b84235270611582"><a name="b84235270611582"></a><a name="b84235270611582"></a>null</strong>.</p>
</td>
</tr>
</tbody>
</table>

**Table  6** **os\_extra\_specs**  field description

<a name="table59078165"></a>
<table><thead align="left"><tr id="row48163256"><th class="cellrowborder" valign="top" width="22.597740225977404%" id="mcps1.2.4.1.1"><p id="p2179014175417"><a name="p2179014175417"></a><a name="p2179014175417"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.538646135386461%" id="mcps1.2.4.1.2"><p id="p1717918144547"><a name="p1717918144547"></a><a name="p1717918144547"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="63.86361363863614%" id="mcps1.2.4.1.3"><p id="p101791614155416"><a name="p101791614155416"></a><a name="p101791614155416"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row40625737"><td class="cellrowborder" valign="top" width="22.597740225977404%" headers="mcps1.2.4.1.1 "><p id="p2350413"><a name="p2350413"></a><a name="p2350413"></a>ecs:performancetype</p>
</td>
<td class="cellrowborder" valign="top" width="13.538646135386461%" headers="mcps1.2.4.1.2 "><p id="p53130157"><a name="p53130157"></a><a name="p53130157"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63.86361363863614%" headers="mcps1.2.4.1.3 "><p id="p10070188"><a name="p10070188"></a><a name="p10070188"></a>Specifies the ECS flavor type:</p>
<a name="ul30830313154217"></a><a name="ul30830313154217"></a><ul id="ul30830313154217"><li><strong id="b18933105864811"><a name="b18933105864811"></a><a name="b18933105864811"></a>normal</strong>: general computing</li><li><strong id="b64942601153937"><a name="b64942601153937"></a><a name="b64942601153937"></a>cpuv1</strong>: computing I</li><li><strong id="b42292462153937"><a name="b42292462153937"></a><a name="b42292462153937"></a>cpuv2</strong>: computing II</li><li><strong id="b84235270619150"><a name="b84235270619150"></a><a name="b84235270619150"></a>computingv3</strong>: general computing-plus</li><li><strong id="b24328905153937"><a name="b24328905153937"></a><a name="b24328905153937"></a>highmem</strong>: memory-optimized</li><li><strong id="b842352706182019"><a name="b842352706182019"></a><a name="b842352706182019"></a>saphana</strong>: large-memory</li><li><strong id="b946848659"><a name="b946848659"></a><a name="b946848659"></a>saphana</strong>: large-memory HANA ECS</li><li><strong id="b8423527068463"><a name="b8423527068463"></a><a name="b8423527068463"></a>diskintensive</strong>: disk-intensive</li><li><strong id="b84235270618537"><a name="b84235270618537"></a><a name="b84235270618537"></a>highcpu</strong>: high-performance computing</li><li><strong id="b84235270692455"><a name="b84235270692455"></a><a name="b84235270692455"></a>gpu</strong>: GPU-accelerated</li><li><strong id="b84235270693231"><a name="b84235270693231"></a><a name="b84235270693231"></a>fpga</strong>: FPGA-accelerated</li></ul>
</td>
</tr>
<tr id="row1765536610939"><td class="cellrowborder" valign="top" width="22.597740225977404%" headers="mcps1.2.4.1.1 "><p id="p148927910953"><a name="p148927910953"></a><a name="p148927910953"></a>resource_type</p>
</td>
<td class="cellrowborder" valign="top" width="13.538646135386461%" headers="mcps1.2.4.1.2 "><p id="p5352275710953"><a name="p5352275710953"></a><a name="p5352275710953"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63.86361363863614%" headers="mcps1.2.4.1.3 "><p id="p2784055310953"><a name="p2784055310953"></a><a name="p2784055310953"></a>Specifies the resource type. <strong id="b84235270693618"><a name="b84235270693618"></a><a name="b84235270693618"></a>resource_type</strong> is used to differentiate between the types of the physical servers accommodating ECSs.</p>
</td>
</tr>
<tr id="row3298094311027"><td class="cellrowborder" valign="top" width="22.597740225977404%" headers="mcps1.2.4.1.1 "><p id="p4603650011047"><a name="p4603650011047"></a><a name="p4603650011047"></a>instance_vnic:type</p>
</td>
<td class="cellrowborder" valign="top" width="13.538646135386461%" headers="mcps1.2.4.1.2 "><p id="p2899031911027"><a name="p2899031911027"></a><a name="p2899031911027"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63.86361363863614%" headers="mcps1.2.4.1.3 "><p id="p6651453911027"><a name="p6651453911027"></a><a name="p6651453911027"></a>Specifies the NIC type. The value of this parameter is consistently <strong id="b84235270693818"><a name="b84235270693818"></a><a name="b84235270693818"></a>enhanced</strong>, indicating that network enhancement ECSs are to be created.</p>
</td>
</tr>
<tr id="row4401335711029"><td class="cellrowborder" valign="top" width="22.597740225977404%" headers="mcps1.2.4.1.1 "><p id="p642956911055"><a name="p642956911055"></a><a name="p642956911055"></a>instance_vnic:instance_bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="13.538646135386461%" headers="mcps1.2.4.1.2 "><p id="p219411211029"><a name="p219411211029"></a><a name="p219411211029"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="63.86361363863614%" headers="mcps1.2.4.1.3 "><p id="p3733921611317"><a name="p3733921611317"></a><a name="p3733921611317"></a>Specifies the maximum bandwidth in the unit of Mbit/s. The maximum value of this parameter is <strong id="b84235270620405"><a name="b84235270620405"></a><a name="b84235270620405"></a>10000</strong>.</p>
</td>
</tr>
<tr id="row210633411030"><td class="cellrowborder" valign="top" width="22.597740225977404%" headers="mcps1.2.4.1.1 "><p id="p4719080011112"><a name="p4719080011112"></a><a name="p4719080011112"></a>instance_vnic:max_count</p>
</td>
<td class="cellrowborder" valign="top" width="13.538646135386461%" headers="mcps1.2.4.1.2 "><p id="p6234262411030"><a name="p6234262411030"></a><a name="p6234262411030"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="63.86361363863614%" headers="mcps1.2.4.1.3 "><p id="p3214052511338"><a name="p3214052511338"></a><a name="p3214052511338"></a>Specifies the maximum number of NICs. The maximum value of this parameter is 4.</p>
</td>
</tr>
<tr id="row2048185111032"><td class="cellrowborder" valign="top" width="22.597740225977404%" headers="mcps1.2.4.1.1 "><p id="p71867811120"><a name="p71867811120"></a><a name="p71867811120"></a>quota:local_disk</p>
</td>
<td class="cellrowborder" valign="top" width="13.538646135386461%" headers="mcps1.2.4.1.2 "><p id="p2948474411032"><a name="p2948474411032"></a><a name="p2948474411032"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63.86361363863614%" headers="mcps1.2.4.1.3 "><p id="p18886502171752"><a name="p18886502171752"></a><a name="p18886502171752"></a>The value of this parameter is in format of "{type}:{count}:{size}:{safeFormat}", where,</p>
<a name="ul5014974617193"></a><a name="ul5014974617193"></a><ul id="ul5014974617193"><li><strong id="b8423527068536"><a name="b8423527068536"></a><a name="b8423527068536"></a>type</strong> specifies the disk type, which can only be HDD.</li><li><strong id="b842352706204211"><a name="b842352706204211"></a><a name="b842352706204211"></a>count</strong> specifies the number of local disks. Its value can be 3/6/12/24 for d1 type of disks, 2/4/8/12/16/24 for d2 type of disks, or 2/4/8/12/16/24/28 for d3 type of disks.</li><li><strong id="b84235270620446"><a name="b84235270620446"></a><a name="b84235270620446"></a>size</strong> specifies the capacity of a single disk, in GB. Currently, only <strong id="b842352706204418"><a name="b842352706204418"></a><a name="b842352706204418"></a>1675</strong> is supported. The actual disk size is <strong id="b842352706204424"><a name="b842352706204424"></a><a name="b842352706204424"></a>1800</strong>, and the available size after formatting is <strong id="b842352706204431"><a name="b842352706204431"></a><a name="b842352706204431"></a>1675</strong>.</li><li><strong id="b84235270685445"><a name="b84235270685445"></a><a name="b84235270685445"></a>safeFormat</strong> specifies whether the local disks of an ECS have been securely formatted. The value of this parameter can only be <strong id="b84235270685819"><a name="b84235270685819"></a><a name="b84235270685819"></a>FALSE</strong> for D1 ECSs or <strong id="b84235270691030"><a name="b84235270691030"></a><a name="b84235270691030"></a>True</strong> for D2 and D3 ECSs.</li></ul>
<div class="note" id="note19568384171814"><a name="note19568384171814"></a><a name="note19568384171814"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p41897735171814"><a name="p41897735171814"></a><a name="p41897735171814"></a>This field is dedicated for disk-intensive ECSs.</p>
</div></div>
</td>
</tr>
<tr id="row79844161301"><td class="cellrowborder" valign="top" width="22.597740225977404%" headers="mcps1.2.4.1.1 "><p id="p179851516123013"><a name="p179851516123013"></a><a name="p179851516123013"></a>quota:nvme_ssd</p>
</td>
<td class="cellrowborder" valign="top" width="13.538646135386461%" headers="mcps1.2.4.1.2 "><p id="p14675332203217"><a name="p14675332203217"></a><a name="p14675332203217"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63.86361363863614%" headers="mcps1.2.4.1.3 "><p id="p1636010426325"><a name="p1636010426325"></a><a name="p1636010426325"></a>The value of this parameter is in format of "{type}:{spec}:{size}:{safeFormat}".</p>
<a name="ul14360154253214"></a><a name="ul14360154253214"></a><ul id="ul14360154253214"><li><strong id="b842352706122129"><a name="b842352706122129"></a><a name="b842352706122129"></a>type</strong>: indicates the capacity of a single NVME SSD disk attached to the ECS, which can only be 1.6 TB or 3.2 TB.</li><li><strong id="b84235270615818"><a name="b84235270615818"></a><a name="b84235270615818"></a>spec</strong>: indicates the specifications of the NVME SSD disk, which can be large or small. Only I3 ECSs with large specifications are supported.</li><li><strong id="b842352706153758"><a name="b842352706153758"></a><a name="b842352706153758"></a>size</strong>: indicates the capacity, in the unit of GB, of the disk used by the guest user. If the <strong id="b842352706153855"><a name="b842352706153855"></a><a name="b842352706153855"></a>spec</strong> value is <strong id="b84235270615398"><a name="b84235270615398"></a><a name="b84235270615398"></a>large</strong>, the value of this parameter is the size of a single disk attached to the ECS. If the <strong id="b1709825260153941"><a name="b1709825260153941"></a><a name="b1709825260153941"></a>spec</strong> value is <strong id="b762663279153941"><a name="b762663279153941"></a><a name="b762663279153941"></a>small</strong>, the value of this parameter is 1/4 or 1/2 of the specification.</li><li><strong id="b1435226326"><a name="b1435226326"></a><a name="b1435226326"></a>safeFormat</strong>: indicates whether the local disks of the ECS are securely formatted. The value of this parameter can only be <strong id="b1584208235"><a name="b1584208235"></a><a name="b1584208235"></a>True</strong> for I3 ECSs.</li></ul>
<div class="note" id="note14360144233213"><a name="note14360144233213"></a><a name="note14360144233213"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p23611542193210"><a name="p23611542193210"></a><a name="p23611542193210"></a>This field is dedicated for ultra-high I/O ECSs.</p>
</div></div>
</td>
</tr>
<tr id="row3607774511039"><td class="cellrowborder" valign="top" width="22.597740225977404%" headers="mcps1.2.4.1.1 "><p id="p036915215368"><a name="p036915215368"></a><a name="p036915215368"></a>extra_spec:io:persistent_grant</p>
</td>
<td class="cellrowborder" valign="top" width="13.538646135386461%" headers="mcps1.2.4.1.2 "><p id="p1312224411039"><a name="p1312224411039"></a><a name="p1312224411039"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="63.86361363863614%" headers="mcps1.2.4.1.3 "><p id="p5626887711039"><a name="p5626887711039"></a><a name="p5626887711039"></a>Specifies whether persistence is supported. The value of this parameter is <strong id="b8423527068598"><a name="b8423527068598"></a><a name="b8423527068598"></a>true</strong>.</p>
<p id="p154651097561"><a name="p154651097561"></a><a name="p154651097561"></a>This parameter indicates that the ECS is persistently authorized to access the storage.</p>
<div class="note" id="note16119794171837"><a name="note16119794171837"></a><a name="note16119794171837"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p10860420171837"><a name="p10860420171837"></a><a name="p10860420171837"></a>This field is dedicated for disk-intensive D1 ECSs.</p>
</div></div>
</td>
</tr>
<tr id="row32430052103752"><td class="cellrowborder" valign="top" width="22.597740225977404%" headers="mcps1.2.4.1.1 "><p id="p9588565103752"><a name="p9588565103752"></a><a name="p9588565103752"></a>ecs:generation</p>
</td>
<td class="cellrowborder" valign="top" width="13.538646135386461%" headers="mcps1.2.4.1.2 "><p id="p38476302103752"><a name="p38476302103752"></a><a name="p38476302103752"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63.86361363863614%" headers="mcps1.2.4.1.3 "><p id="p39563409104048"><a name="p39563409104048"></a><a name="p39563409104048"></a>Specifies the generation of an ECS type.</p>
<a name="ul41452807105213"></a><a name="ul41452807105213"></a><ul id="ul41452807105213"><li><strong id="b842352706173240"><a name="b842352706173240"></a><a name="b842352706173240"></a>s1</strong>: general-purpose first-generation</li><li><strong id="b1623687517173313"><a name="b1623687517173313"></a><a name="b1623687517173313"></a>s2</strong>: general-purpose second-generation</li><li><strong id="b480152783"><a name="b480152783"></a><a name="b480152783"></a>s3</strong>: general-purpose third-generation</li><li><strong id="b35643547153937"><a name="b35643547153937"></a><a name="b35643547153937"></a>s6</strong>: general-purpose</li><li><strong id="b2032219541912"><a name="b2032219541912"></a><a name="b2032219541912"></a>sn3</strong>: general network-optimized</li><li><strong id="b1921697480"><a name="b1921697480"></a><a name="b1921697480"></a>c3</strong>: general computing-plus</li><li><strong id="b916893070"><a name="b916893070"></a><a name="b916893070"></a>c6</strong>: general computing-plus</li><li><strong id="b195954361197"><a name="b195954361197"></a><a name="b195954361197"></a>c3ne</strong>: general network enhancement</li><li><strong id="b1230349247173332"><a name="b1230349247173332"></a><a name="b1230349247173332"></a>m1</strong>: memory-optimized first-generation</li><li><strong id="b14662750817340"><a name="b14662750817340"></a><a name="b14662750817340"></a>m2</strong>: memory-optimized second-generation</li><li><strong id="b739732950"><a name="b739732950"></a><a name="b739732950"></a>m3</strong>: memory-optimized third-generation</li><li><strong id="b1753307529"><a name="b1753307529"></a><a name="b1753307529"></a>m6</strong>: memory-optimized</li><li><strong id="b1274319619215"><a name="b1274319619215"></a><a name="b1274319619215"></a>m3ne</strong>: memory network enhancement</li><li><strong id="b1339968966173414"><a name="b1339968966173414"></a><a name="b1339968966173414"></a>h1</strong>: high-performance computing first-generation</li><li><strong id="b1058770675173431"><a name="b1058770675173431"></a><a name="b1058770675173431"></a>h2</strong>: high-performance computing second-generation</li><li><strong id="b528779505193223"><a name="b528779505193223"></a><a name="b528779505193223"></a>hc2</strong>: high-performance computing</li><li><strong id="b1041233995"><a name="b1041233995"></a><a name="b1041233995"></a>h3</strong>: high-performance computing</li><li><strong id="b1721516585"><a name="b1721516585"></a><a name="b1721516585"></a>hi3</strong>: ultra-high performance computing</li><li><strong id="b2104194860173444"><a name="b2104194860173444"></a><a name="b2104194860173444"></a>d1</strong>: Disk-intensive first-generation ECSs</li><li><strong id="b175683645317352"><a name="b175683645317352"></a><a name="b175683645317352"></a>d2</strong>: disk-intensive second-generation</li><li><strong id="b726593318"><a name="b726593318"></a><a name="b726593318"></a>d3</strong>: disk-intensive</li><li><strong id="b53278115"><a name="b53278115"></a><a name="b53278115"></a>kc1</strong>: Kunpeng general computing-plus</li><li><strong id="b1193860365"><a name="b1193860365"></a><a name="b1193860365"></a>km1</strong>: Kunpeng memory-optimized</li><li><strong id="b842352706204532"><a name="b842352706204532"></a><a name="b842352706204532"></a>g1</strong>: GPU-optimized first-generation</li><li><strong id="b84235270620470"><a name="b84235270620470"></a><a name="b84235270620470"></a>g2</strong>: GPU-optimized second-generation</li><li><strong id="b1883664023"><a name="b1883664023"></a><a name="b1883664023"></a>e3</strong>: large-memory</li><li><strong id="b1172002785"><a name="b1172002785"></a><a name="b1172002785"></a>i3</strong>: ultra-high I/O</li></ul>
<div class="note" id="note4393341105446"><a name="note4393341105446"></a><a name="note4393341105446"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p39540072105446"><a name="p39540072105446"></a><a name="p39540072105446"></a>This field is optional.</p>
</div></div>
</td>
</tr>
<tr id="row38665273103753"><td class="cellrowborder" valign="top" width="22.597740225977404%" headers="mcps1.2.4.1.1 "><p id="p44879434103753"><a name="p44879434103753"></a><a name="p44879434103753"></a>ecs:virtualization_env_types</p>
</td>
<td class="cellrowborder" valign="top" width="13.538646135386461%" headers="mcps1.2.4.1.2 "><p id="p11355576103753"><a name="p11355576103753"></a><a name="p11355576103753"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63.86361363863614%" headers="mcps1.2.4.1.3 "><p id="p47386474103753"><a name="p47386474103753"></a><a name="p47386474103753"></a>Specifies a virtualization type.</p>
<a name="ul58866534105220"></a><a name="ul58866534105220"></a><ul id="ul58866534105220"><li>If the parameter value is <strong id="b842352706201341"><a name="b842352706201341"></a><a name="b842352706201341"></a>FusionCompute</strong>, the ECS uses Xen virtualization.</li><li>If the parameter value is <strong id="b5532434820147"><a name="b5532434820147"></a><a name="b5532434820147"></a>CloudCompute</strong>, the ECS uses KVM virtualization.</li></ul>
<div class="note" id="note16372434105451"><a name="note16372434105451"></a><a name="note16372434105451"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p13134186105451"><a name="p13134186105451"></a><a name="p13134186105451"></a>This field is optional.</p>
</div></div>
</td>
</tr>
<tr id="row40633323112531"><td class="cellrowborder" valign="top" width="22.597740225977404%" headers="mcps1.2.4.1.1 "><p id="p30155595112531"><a name="p30155595112531"></a><a name="p30155595112531"></a>pci_passthrough:enable_gpu</p>
</td>
<td class="cellrowborder" valign="top" width="13.538646135386461%" headers="mcps1.2.4.1.2 "><p id="p26684139112531"><a name="p26684139112531"></a><a name="p26684139112531"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="63.86361363863614%" headers="mcps1.2.4.1.3 "><p id="p5109464911323"><a name="p5109464911323"></a><a name="p5109464911323"></a>Indicates whether the GPU is passthrough.</p>
<p id="p13931631112531"><a name="p13931631112531"></a><a name="p13931631112531"></a>If the value is <strong id="b842352706204429"><a name="b842352706204429"></a><a name="b842352706204429"></a>true</strong>, the GPU is passthrough.</p>
</td>
</tr>
<tr id="row15025433112531"><td class="cellrowborder" valign="top" width="22.597740225977404%" headers="mcps1.2.4.1.1 "><p id="p1011177112531"><a name="p1011177112531"></a><a name="p1011177112531"></a>pci_passthrough:gpu_specs</p>
</td>
<td class="cellrowborder" valign="top" width="13.538646135386461%" headers="mcps1.2.4.1.2 "><p id="p14796532112531"><a name="p14796532112531"></a><a name="p14796532112531"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63.86361363863614%" headers="mcps1.2.4.1.3 "><p id="p2591674143711"><a name="p2591674143711"></a><a name="p2591674143711"></a>Indicates the technology used on the G1 and G2 ECSs, including GPU virtualization and GPU passthrough.</p>
<a name="ul3341661143849"></a><a name="ul3341661143849"></a><ul id="ul3341661143849"><li>If the ECS with specified specifications uses GPU virtualization and the GPU model is M60-1Q, the parameter value can be <strong id="b842352706204624"><a name="b842352706204624"></a><a name="b842352706204624"></a>m60_1q:virt:1</strong>.</li><li>If the ECS with specified specifications uses GPU passthrough and the GPU model is M60, the parameter value can be <strong id="b648177307204633"><a name="b648177307204633"></a><a name="b648177307204633"></a>m60:direct_graphics:1</strong>.</li></ul>
</td>
</tr>
<tr id="row1587411238210"><td class="cellrowborder" valign="top" width="22.597740225977404%" headers="mcps1.2.4.1.1 "><p id="p1787514232218"><a name="p1787514232218"></a><a name="p1787514232218"></a>pci_passthrough:alias</p>
</td>
<td class="cellrowborder" valign="top" width="13.538646135386461%" headers="mcps1.2.4.1.2 "><p id="p5875823928"><a name="p5875823928"></a><a name="p5875823928"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63.86361363863614%" headers="mcps1.2.4.1.3 "><p id="p1487514231826"><a name="p1487514231826"></a><a name="p1487514231826"></a>Indicates the model and quantity of passthrough-enabled GPUs on P1 ECSs. The parameter value can be set to <strong id="b842352706163914"><a name="b842352706163914"></a><a name="b842352706163914"></a>nvidia-p100:1</strong>, indicating that the ECS using this specification will occupy one NVIDIA P100 GPU.</p>
</td>
</tr>
<tr id="row169423685915"><td class="cellrowborder" valign="top" width="22.597740225977404%" headers="mcps1.2.4.1.1 "><p id="p395203616590"><a name="p395203616590"></a><a name="p395203616590"></a>cond:operation:status</p>
</td>
<td class="cellrowborder" valign="top" width="13.538646135386461%" headers="mcps1.2.4.1.2 "><p id="p29512361595"><a name="p29512361595"></a><a name="p29512361595"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63.86361363863614%" headers="mcps1.2.4.1.3 "><p id="p108052518111"><a name="p108052518111"></a><a name="p108052518111"></a>This parameter takes effect region-wide. If an AZ is not configured in the <strong id="b84235270617842"><a name="b84235270617842"></a><a name="b84235270617842"></a>cond:operation:az</strong> parameter, the value of this parameter is used by default. If this parameter is not set or used, the meaning of <strong id="b842352706171020"><a name="b842352706171020"></a><a name="b842352706171020"></a>normal</strong> applies. Options:</p>
<a name="ul14280914915"></a><a name="ul14280914915"></a><ul id="ul14280914915"><li><strong id="b84235270615416"><a name="b84235270615416"></a><a name="b84235270615416"></a>normal</strong>: indicates normal commercial use of the flavor.</li><li><strong id="b842352706152617"><a name="b842352706152617"></a><a name="b842352706152617"></a>abandon</strong>: indicates that the flavor has been canceled (not displayed).</li><li><strong id="b842352706154546"><a name="b842352706154546"></a><a name="b842352706154546"></a>sellout</strong>: indicates that the flavor has been sold out.</li><li><strong id="b84235270615467"><a name="b84235270615467"></a><a name="b84235270615467"></a>obt</strong>: indicates that the flavor is under open beta testing (OBT).</li><li><strong id="b162074261262"><a name="b162074261262"></a><a name="b162074261262"></a>obt_sellout</strong>: indicates that the OBT resources are sold out.</li><li><strong id="b842352706152917"><a name="b842352706152917"></a><a name="b842352706152917"></a>promotion</strong>: indicates the recommended flavor (commercial use, which is similar to <strong id="b84235270615300"><a name="b84235270615300"></a><a name="b84235270615300"></a>normal</strong>).</li></ul>
</td>
</tr>
<tr id="row1347820527114"><td class="cellrowborder" valign="top" width="22.597740225977404%" headers="mcps1.2.4.1.1 "><p id="p54798521311"><a name="p54798521311"></a><a name="p54798521311"></a>cond:operation:az</p>
</td>
<td class="cellrowborder" valign="top" width="13.538646135386461%" headers="mcps1.2.4.1.2 "><p id="p12479205214119"><a name="p12479205214119"></a><a name="p12479205214119"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63.86361363863614%" headers="mcps1.2.4.1.3 "><p id="p118175714108"><a name="p118175714108"></a><a name="p118175714108"></a>This parameter takes effect AZ-wide. If an AZ is not configured in this parameter, the value of the <strong id="b842352706171317"><a name="b842352706171317"></a><a name="b842352706171317"></a>cond:operation:status</strong> parameter is used by default. This parameter is in the format of "az(xx)". The value in parentheses is the flavor status in an AZ. If the parentheses are left blank, the configuration is invalid. The <strong id="b1479429540172238"><a name="b1479429540172238"></a><a name="b1479429540172238"></a>cond:operation:az</strong> options are the same as the <strong id="b734926429172243"><a name="b734926429172243"></a><a name="b734926429172243"></a>cond:operation:status</strong> options.</p>
<p id="p994816551996"><a name="p994816551996"></a><a name="p994816551996"></a>For example, a flavor is for commercial use in AZs 0 and 3, sold out in AZ 1, for OBT in AZ 2, and is canceled in other AZs. Then, set parameters as follows:</p>
<a name="ul18538152311016"></a><a name="ul18538152311016"></a><ul id="ul18538152311016"><li><span class="parmname" id="parmname88521131611218"><a name="parmname88521131611218"></a><a name="parmname88521131611218"></a><b>cond:operation:status</b></span>: <span class="parmvalue" id="parmvalue696784524112116"><a name="parmvalue696784524112116"></a><a name="parmvalue696784524112116"></a><b>abandon</b></span></li><li><span class="parmname" id="parmname124225164154437"><a name="parmname124225164154437"></a><a name="parmname124225164154437"></a><b>cond:operation:az</b></span>: <span class="parmvalue" id="parmvalue1340869142154443"><a name="parmvalue1340869142154443"></a><a name="parmvalue1340869142154443"></a><b>az0(normal), az1(sellout), az2(obt), az3(normal)</b></span></li></ul>
<div class="note" id="note1837362942612"><a name="note1837362942612"></a><a name="note1837362942612"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p103771029162615"><a name="p103771029162615"></a><a name="p103771029162615"></a>Configure this parameter if the flavor status in an AZ is different from the <strong id="b842352706102514"><a name="b842352706102514"></a><a name="b842352706102514"></a>cond:operation:status</strong> value.</p>
</div></div>
</td>
</tr>
<tr id="row7391144881019"><td class="cellrowborder" valign="top" width="22.597740225977404%" headers="mcps1.2.4.1.1 "><p id="p17438195812103"><a name="p17438195812103"></a><a name="p17438195812103"></a>quota:max_rate</p>
</td>
<td class="cellrowborder" valign="top" width="13.538646135386461%" headers="mcps1.2.4.1.2 "><p id="p14391184819100"><a name="p14391184819100"></a><a name="p14391184819100"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63.86361363863614%" headers="mcps1.2.4.1.3 "><p id="p1767118159115"><a name="p1767118159115"></a><a name="p1767118159115"></a>Specifies the maximum bandwidth.</p>
<a name="ul572353916149"></a><a name="ul572353916149"></a><ul id="ul572353916149"><li>Unit: Mbit/s. If a bandwidth is in the unit of Gbit/s, it must be divided by 1000.</li></ul>
</td>
</tr>
<tr id="row1879715571010"><td class="cellrowborder" valign="top" width="22.597740225977404%" headers="mcps1.2.4.1.1 "><p id="p11438958121015"><a name="p11438958121015"></a><a name="p11438958121015"></a>quota:min_rate</p>
</td>
<td class="cellrowborder" valign="top" width="13.538646135386461%" headers="mcps1.2.4.1.2 "><p id="p9543182031515"><a name="p9543182031515"></a><a name="p9543182031515"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63.86361363863614%" headers="mcps1.2.4.1.3 "><p id="p567181510118"><a name="p567181510118"></a><a name="p567181510118"></a>Specified the assured bandwidth.</p>
<a name="ul1173092731517"></a><a name="ul1173092731517"></a><ul id="ul1173092731517"><li>Unit: Mbit/s. If a bandwidth is in the unit of Gbit/s, it must be divided by 1000.</li></ul>
</td>
</tr>
<tr id="row1628165141013"><td class="cellrowborder" valign="top" width="22.597740225977404%" headers="mcps1.2.4.1.1 "><p id="p13438358171015"><a name="p13438358171015"></a><a name="p13438358171015"></a>quota:max_pps</p>
</td>
<td class="cellrowborder" valign="top" width="13.538646135386461%" headers="mcps1.2.4.1.2 "><p id="p627754891516"><a name="p627754891516"></a><a name="p627754891516"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63.86361363863614%" headers="mcps1.2.4.1.3 "><p id="p166719153116"><a name="p166719153116"></a><a name="p166719153116"></a>Specifies the maximum intranet PPS.</p>
<a name="ul991890151616"></a><a name="ul991890151616"></a><ul id="ul991890151616"><li>Unit: number. If a value is in the unit of 10000, it must be divided by 10000.</li></ul>
</td>
</tr>
<tr id="row121692012201"><td class="cellrowborder" valign="top" width="22.597740225977404%" headers="mcps1.2.4.1.1 "><p id="p1216152092019"><a name="p1216152092019"></a><a name="p1216152092019"></a>cond:operation:charge</p>
</td>
<td class="cellrowborder" valign="top" width="13.538646135386461%" headers="mcps1.2.4.1.2 "><p id="p18216620192017"><a name="p18216620192017"></a><a name="p18216620192017"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63.86361363863614%" headers="mcps1.2.4.1.3 "><p id="p621662082017"><a name="p621662082017"></a><a name="p621662082017"></a>Specifies a billing type.</p>
<a name="ul1499718472209"></a><a name="ul1499718472209"></a><ul id="ul1499718472209"><li>Both billing types are supported if this parameter is not set.</li><li>Pay-per-use</li></ul>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:**   
>For ECS specifications, see "Instances and Application Scenarios" in  _Elastic Cloud Server User Guide_.  

## Example Request<a name="section11327529135420"></a>

```
GET https://{endpoint}/v1/{project_id}/cloudservers/flavors?availability_zone=availability_value
```

## Example Response<a name="section437243975713"></a>

```
{
    "flavors": [
        {
            "id": "c3.2xlarge.2",
            "name": "c3.2xlarge.2",
            "vcpus": "8",
            "ram": 16384,
            "disk": "0",
            "swap": "",
            "links": [
                {
                    "rel": "self",
                    "href": "https://compute-ext.region.xxx.com/v1.0/743b4c0428d94531b9f2add666642e6b/flavors/c3.2xlarge.2",
                    "type": null
                },
                {
                    "rel": "bookmark",
                    "href": "https://compute-ext.region.xxx.com/743b4c0428d94531b9f2add666642e6b/flavors/c3.2xlarge.2",
                    "type": null
                }
            ],
            "OS-FLV-EXT-DATA:ephemeral": 0,
            "rxtx_factor": 1,
            "OS-FLV-DISABLED:disabled": false,
            "rxtx_quota": null,
            "rxtx_cap": null,
            "os-flavor-access:is_public": true,
            "os_extra_specs": {
                "ecs:virtualization_env_types": "CloudCompute",
                "ecs:generation": "c3",
                "ecs:performancetype": "computingv3",
                "resource_type": "IOoptimizedC3_2"
            }
        }
    ]
}
```

## Returned Values<a name="section58665336"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

## Error Codes<a name="section85821649202813"></a>

See  [Error Code Description](error-code-description.md).

