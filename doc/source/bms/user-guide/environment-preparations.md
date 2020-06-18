# Environment Preparations<a name="EN-US_TOPIC_0159392251"></a>

## Software Environment<a name="section6649185522213"></a>

**Table  1**  Software versions

<a name="table50116845"></a>
<table><thead align="left"><tr id="row50454834"><th class="cellrowborder" valign="top" width="57.58%" id="mcps1.2.3.1.1"><p id="p60309786"><a name="p60309786"></a><a name="p60309786"></a>Component</p>
</th>
<th class="cellrowborder" valign="top" width="42.42%" id="mcps1.2.3.1.2"><p id="p9528291"><a name="p9528291"></a><a name="p9528291"></a>Version</p>
</th>
</tr>
</thead>
<tbody><tr id="row33911763"><td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.1 "><p id="p62498284"><a name="p62498284"></a><a name="p62498284"></a>VMware ESXi</p>
</td>
<td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.2 "><p id="p29196278"><a name="p29196278"></a><a name="p29196278"></a>6.5.0</p>
</td>
</tr>
<tr id="row61439917"><td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.1 "><p id="p10577379"><a name="p10577379"></a><a name="p10577379"></a>VMware vCenter Server Appliance</p>
</td>
<td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.2 "><p id="p51461341"><a name="p51461341"></a><a name="p51461341"></a>6.5.0</p>
</td>
</tr>
<tr id="row60498887"><td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.1 "><p id="p1462819"><a name="p1462819"></a><a name="p1462819"></a>VMware NSX Manager</p>
</td>
<td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.2 "><p id="p51379511"><a name="p51379511"></a><a name="p51379511"></a>6.4.3</p>
</td>
</tr>
<tr id="row59762422"><td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.1 "><p id="p8918034"><a name="p8918034"></a><a name="p8918034"></a>VMware vSphere Replication</p>
</td>
<td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.2 "><p id="p51272187"><a name="p51272187"></a><a name="p51272187"></a>6.5.1</p>
</td>
</tr>
<tr id="row58796504"><td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.1 "><p id="p64896350"><a name="p64896350"></a><a name="p64896350"></a>VMware vCenter Site Recovery Manager</p>
</td>
<td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.2 "><p id="p22112997"><a name="p22112997"></a><a name="p22112997"></a>6.5.1</p>
</td>
</tr>
</tbody>
</table>

## Network Environment<a name="section56651571236"></a>

>![](/images/icon-note.gif) **NOTE:**   
>The IP address segments are examples only. You need to obtain the information from the BMS metadata.  
>Eight network ports are configured for the provisioned BMS, two for accessing the VPC network and six for configuring the QinQ network. vmnic0 and vmnic1 in the example are two network ports for connecting to the VPC network. Different from two network ports connecting to the VPC network, these two ports become uplinks of vSwitch0 by default after provisioned and enabled on the BMS.  

The following example is a typical VMware architecture, which consists of three BMSs in cluster mode on which the management and service VMs are deployed. Each server has eight physical network ports configured and each BMS connects to a VPC subnet. You need to plan and configure the network planes used for management, vmotion, vSAN, and VXLAN on the NICs. The following method is for reference only.

**Table  2**  Network plane planning

<a name="table9652104520446"></a>
<table><thead align="left"><tr id="row27857118"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.1"><p id="p41834070"><a name="p41834070"></a><a name="p41834070"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.2"><p id="p29612923"><a name="p29612923"></a><a name="p29612923"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.3"><p id="p45875888"><a name="p45875888"></a><a name="p45875888"></a>IP Address Segment</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.4"><p id="p23308753"><a name="p23308753"></a><a name="p23308753"></a>Gateway</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.5"><p id="p13538688"><a name="p13538688"></a><a name="p13538688"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row4700647"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.1 "><p id="p45208163"><a name="p45208163"></a><a name="p45208163"></a>VPC subnet</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="p37982554"><a name="p37982554"></a><a name="p37982554"></a>esx-primary</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.3 "><p id="p56688054"><a name="p56688054"></a><a name="p56688054"></a>192.168.0.0/24</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.4 "><p id="p28329695"><a name="p28329695"></a><a name="p28329695"></a>192.168.0.1</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p13003964"><a name="p13003964"></a><a name="p13003964"></a>BMS primary NIC</p>
</td>
</tr>
<tr id="row49926818"><td class="cellrowborder" rowspan="4" valign="top" width="20%" headers="mcps1.2.6.1.1 "><p id="p17540457"><a name="p17540457"></a><a name="p17540457"></a>User-planned VLAN</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="p11490904"><a name="p11490904"></a><a name="p11490904"></a>DPortGroup-mgmt</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.3 "><p id="p58348056"><a name="p58348056"></a><a name="p58348056"></a>11.11.11.0/24</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.4 "><p id="p28572113"><a name="p28572113"></a><a name="p28572113"></a>11.11.11.1</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p32639786"><a name="p32639786"></a><a name="p32639786"></a>Management and vMotion plane</p>
</td>
</tr>
<tr id="row25322618"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p37866150"><a name="p37866150"></a><a name="p37866150"></a>DPortGroup-vxlan</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p47259335"><a name="p47259335"></a><a name="p47259335"></a>11.11.13.0/24</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p2800965"><a name="p2800965"></a><a name="p2800965"></a>11.11.13.1</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p25551623"><a name="p25551623"></a><a name="p25551623"></a>vxlan</p>
</td>
</tr>
<tr id="row28638022"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p37978409"><a name="p37978409"></a><a name="p37978409"></a>DPortGroup-vsan</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p56352326"><a name="p56352326"></a><a name="p56352326"></a>11.11.12.0/24</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p1135683"><a name="p1135683"></a><a name="p1135683"></a>11.11.12.1</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p24881480"><a name="p24881480"></a><a name="p24881480"></a>vSAN plane</p>
</td>
</tr>
<tr id="row22606734"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p19206131"><a name="p19206131"></a><a name="p19206131"></a>hb-edge-internal</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p12192756"><a name="p12192756"></a><a name="p12192756"></a>11.11.8.0/24</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p48089211"><a name="p48089211"></a><a name="p48089211"></a>11.11.8.1</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p2911981"><a name="p2911981"></a><a name="p2911981"></a>Service plane</p>
</td>
</tr>
</tbody>
</table>

The following table lists the vNICs of the ESXi BMS.

**Table  3**  vNICs

<a name="table5655194511448"></a>
<table><thead align="left"><tr id="row10296933"><th class="cellrowborder" valign="top" width="34.03340334033403%" id="mcps1.2.4.1.1"><p id="p28745279"><a name="p28745279"></a><a name="p28745279"></a>Network</p>
</th>
<th class="cellrowborder" valign="top" width="31.873187318731873%" id="mcps1.2.4.1.2"><p id="p17343428"><a name="p17343428"></a><a name="p17343428"></a>IP Address</p>
</th>
<th class="cellrowborder" valign="top" width="34.09340934093409%" id="mcps1.2.4.1.3"><p id="p40707460"><a name="p40707460"></a><a name="p40707460"></a>vSwitch uplink</p>
</th>
</tr>
</thead>
<tbody><tr id="row13621136"><td class="cellrowborder" valign="top" width="34.03340334033403%" headers="mcps1.2.4.1.1 "><p id="p29570261"><a name="p29570261"></a><a name="p29570261"></a>esx-primary</p>
</td>
<td class="cellrowborder" valign="top" width="31.873187318731873%" headers="mcps1.2.4.1.2 "><p id="p46380963"><a name="p46380963"></a><a name="p46380963"></a>192.168.0.10</p>
</td>
<td class="cellrowborder" valign="top" width="34.09340934093409%" headers="mcps1.2.4.1.3 "><p id="p65870497"><a name="p65870497"></a><a name="p65870497"></a>vmnic0/vmnic1</p>
</td>
</tr>
<tr id="row55963561"><td class="cellrowborder" valign="top" width="34.03340334033403%" headers="mcps1.2.4.1.1 "><p id="p36754611"><a name="p36754611"></a><a name="p36754611"></a>DPortGroup-mgmt</p>
</td>
<td class="cellrowborder" valign="top" width="31.873187318731873%" headers="mcps1.2.4.1.2 "><p id="p24333505"><a name="p24333505"></a><a name="p24333505"></a>11.11.11.101</p>
</td>
<td class="cellrowborder" valign="top" width="34.09340934093409%" headers="mcps1.2.4.1.3 "><p id="p24856892"><a name="p24856892"></a><a name="p24856892"></a>vmnic2/vmnic3</p>
</td>
</tr>
<tr id="row22385437"><td class="cellrowborder" valign="top" width="34.03340334033403%" headers="mcps1.2.4.1.1 "><p id="p1281126"><a name="p1281126"></a><a name="p1281126"></a>DPortGroup-vxlan</p>
</td>
<td class="cellrowborder" valign="top" width="31.873187318731873%" headers="mcps1.2.4.1.2 "><p id="p36662351"><a name="p36662351"></a><a name="p36662351"></a>11.11.13.101</p>
</td>
<td class="cellrowborder" valign="top" width="34.09340934093409%" headers="mcps1.2.4.1.3 "><p id="p16860416"><a name="p16860416"></a><a name="p16860416"></a>vmnic4/vmnic5</p>
</td>
</tr>
<tr id="row17526019"><td class="cellrowborder" valign="top" width="34.03340334033403%" headers="mcps1.2.4.1.1 "><p id="p10321460"><a name="p10321460"></a><a name="p10321460"></a>DPortGroup-vsan</p>
</td>
<td class="cellrowborder" valign="top" width="31.873187318731873%" headers="mcps1.2.4.1.2 "><p id="p30731970"><a name="p30731970"></a><a name="p30731970"></a>11.11.12.101</p>
</td>
<td class="cellrowborder" valign="top" width="34.09340934093409%" headers="mcps1.2.4.1.3 "><p id="p6261652"><a name="p6261652"></a><a name="p6261652"></a>vmnic6/vmnic7</p>
</td>
</tr>
</tbody>
</table>

The following table lists the IP addresses of the management components connected to the DPortGroup-mgmt network.

**Table  4**  IP addresses of components

<a name="table76701445114412"></a>
<table><thead align="left"><tr id="row14433768"><th class="cellrowborder" valign="top" width="34%" id="mcps1.2.4.1.1"><p id="p28284541"><a name="p28284541"></a><a name="p28284541"></a>Component</p>
</th>
<th class="cellrowborder" valign="top" width="32%" id="mcps1.2.4.1.2"><p id="p17009632"><a name="p17009632"></a><a name="p17009632"></a>IP Address</p>
</th>
<th class="cellrowborder" valign="top" width="34%" id="mcps1.2.4.1.3"><p id="p65265032"><a name="p65265032"></a><a name="p65265032"></a>Domain Name</p>
</th>
</tr>
</thead>
<tbody><tr id="row49322849"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="p35727861"><a name="p35727861"></a><a name="p35727861"></a>vCenter Server</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="p8275629"><a name="p8275629"></a><a name="p8275629"></a>11.11.11.3</p>
</td>
<td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.3 "><p id="p66346226"><a name="p66346226"></a><a name="p66346226"></a>Optional</p>
</td>
</tr>
<tr id="row60245124"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="p48016903"><a name="p48016903"></a><a name="p48016903"></a>NSX manager</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="p64163914"><a name="p64163914"></a><a name="p64163914"></a>11.11.11.4</p>
</td>
<td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.3 "><p id="p29894517"><a name="p29894517"></a><a name="p29894517"></a>-</p>
</td>
</tr>
<tr id="row615201"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="p49831357"><a name="p49831357"></a><a name="p49831357"></a>NSX controller</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="p9808084"><a name="p9808084"></a><a name="p9808084"></a>11.11.11.200</p>
<p id="p21163898"><a name="p21163898"></a><a name="p21163898"></a>11.11.11.201</p>
<p id="p56257360"><a name="p56257360"></a><a name="p56257360"></a>11.11.11.202</p>
</td>
<td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.3 "><p id="p60552345"><a name="p60552345"></a><a name="p60552345"></a>-</p>
</td>
</tr>
<tr id="row8100198"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="p52136268"><a name="p52136268"></a><a name="p52136268"></a>DNS/NTP</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="p62288179"><a name="p62288179"></a><a name="p62288179"></a>11.11.11.6</p>
</td>
<td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.3 "><p id="p12177730"><a name="p12177730"></a><a name="p12177730"></a>-</p>
</td>
</tr>
<tr id="row42490713"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="p19195704"><a name="p19195704"></a><a name="p19195704"></a>Nsx-edge</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="p11348180"><a name="p11348180"></a><a name="p11348180"></a>11.11.11.30</p>
</td>
<td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.3 "><p id="p46787348"><a name="p46787348"></a><a name="p46787348"></a>-</p>
</td>
</tr>
<tr id="row18432949"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="p16673895"><a name="p16673895"></a><a name="p16673895"></a>Jump VM</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="p8408241"><a name="p8408241"></a><a name="p8408241"></a>11.11.11.2</p>
</td>
<td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.3 "><p id="p9978940"><a name="p9978940"></a><a name="p9978940"></a>-</p>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:**   
>-   The VPC name, subnet, and gateway in  [Table 2](#table9652104520446)  are defined and input on the console by the tenant during VM creation.  
>-   You can plan the IP addresses of the vNICs in  [Table 3](#table5655194511448).  
>-   You can plan and allocate the IP addresses in  [Table 4](#table76701445114412).  

