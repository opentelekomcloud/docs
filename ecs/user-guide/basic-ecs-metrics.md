# Basic ECS Metrics<a name="EN-US_TOPIC_0030911465"></a>

## Description<a name="section25901060112133"></a>

This section describes monitoring metrics reported by ECS to Cloud Eye and their namespaces. You can use Cloud Eye to view these metrics and alarms generated for ECSs.

## Namespace<a name="section24282572112133"></a>

SYS.ECS

## ECS Metrics<a name="section1377504154"></a>

ECS metrics vary depending on ECS OSs and types. For details, see  [Table 1](#table11710814105256). √ indicates that the metric is supported, and x indicates that the metric is not supported.

**Table  1**  ECS metrics

<a name="table11710814105256"></a>
<table><thead align="left"><tr id="row43874561105256"><th class="cellrowborder" valign="top" id="mcps1.2.6.1.1"><p id="p31264332105312"><a name="p31264332105312"></a><a name="p31264332105312"></a>Metric</p>
</th>
<th class="cellrowborder" colspan="2" valign="top" id="mcps1.2.6.1.2"><p id="p11268033105256"><a name="p11268033105256"></a><a name="p11268033105256"></a>Windows</p>
</th>
<th class="cellrowborder" colspan="2" valign="top" id="mcps1.2.6.1.3"><p id="p42707722105256"><a name="p42707722105256"></a><a name="p42707722105256"></a>Linux</p>
</th>
</tr>
</thead>
<tbody><tr id="row5300934511122"><td class="cellrowborder" valign="top" width="21.802180218021803%" headers="mcps1.2.6.1.1 "><p id="p732206311122"><a name="p732206311122"></a><a name="p732206311122"></a>None</p>
</td>
<td class="cellrowborder" valign="top" width="18.98189818981898%" headers="mcps1.2.6.1.2 "><p id="p5621621911122"><a name="p5621621911122"></a><a name="p5621621911122"></a>Xen</p>
</td>
<td class="cellrowborder" valign="top" width="20.11201120112011%" headers="mcps1.2.6.1.2 "><p id="p5721985111122"><a name="p5721985111122"></a><a name="p5721985111122"></a>KVM</p>
</td>
<td class="cellrowborder" valign="top" width="19.55195519551955%" headers="mcps1.2.6.1.3 "><p id="p429632711122"><a name="p429632711122"></a><a name="p429632711122"></a>Xen</p>
</td>
<td class="cellrowborder" valign="top" width="19.55195519551955%" headers="mcps1.2.6.1.3 "><p id="p1245823211122"><a name="p1245823211122"></a><a name="p1245823211122"></a>KVM</p>
</td>
</tr>
<tr id="row48825179105256"><td class="cellrowborder" valign="top" width="21.802180218021803%" headers="mcps1.2.6.1.1 "><p id="p1841740511644"><a name="p1841740511644"></a><a name="p1841740511644"></a>CPU Usage</p>
</td>
<td class="cellrowborder" valign="top" width="18.98189818981898%" headers="mcps1.2.6.1.2 "><p id="p31396173105256"><a name="p31396173105256"></a><a name="p31396173105256"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="20.11201120112011%" headers="mcps1.2.6.1.2 "><p id="p48205138111156"><a name="p48205138111156"></a><a name="p48205138111156"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.55195519551955%" headers="mcps1.2.6.1.3 "><p id="p60062046105256"><a name="p60062046105256"></a><a name="p60062046105256"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.55195519551955%" headers="mcps1.2.6.1.3 "><p id="p33187552105256"><a name="p33187552105256"></a><a name="p33187552105256"></a>√</p>
</td>
</tr>
<tr id="row30252514105256"><td class="cellrowborder" valign="top" width="21.802180218021803%" headers="mcps1.2.6.1.1 "><p id="p451597011644"><a name="p451597011644"></a><a name="p451597011644"></a>Memory Usage</p>
</td>
<td class="cellrowborder" valign="top" width="18.98189818981898%" headers="mcps1.2.6.1.2 "><p id="p45839874105256"><a name="p45839874105256"></a><a name="p45839874105256"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="20.11201120112011%" headers="mcps1.2.6.1.2 "><p id="p12302135111156"><a name="p12302135111156"></a><a name="p12302135111156"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.55195519551955%" headers="mcps1.2.6.1.3 "><p id="p22042337105256"><a name="p22042337105256"></a><a name="p22042337105256"></a>√ (The OTC Tools must be installed on the image. Otherwise, this metric is unavailable.)</p>
</td>
<td class="cellrowborder" valign="top" width="19.55195519551955%" headers="mcps1.2.6.1.3 "><p id="p40598868105256"><a name="p40598868105256"></a><a name="p40598868105256"></a>x (Not supported)</p>
</td>
</tr>
<tr id="row29845497105256"><td class="cellrowborder" valign="top" width="21.802180218021803%" headers="mcps1.2.6.1.1 "><p id="p3427272111644"><a name="p3427272111644"></a><a name="p3427272111644"></a>Disk Usage</p>
</td>
<td class="cellrowborder" valign="top" width="18.98189818981898%" headers="mcps1.2.6.1.2 "><p id="p59751899105256"><a name="p59751899105256"></a><a name="p59751899105256"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="20.11201120112011%" headers="mcps1.2.6.1.2 "><p id="p56948901111156"><a name="p56948901111156"></a><a name="p56948901111156"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.55195519551955%" headers="mcps1.2.6.1.3 "><p id="p8065665105256"><a name="p8065665105256"></a><a name="p8065665105256"></a>√ (The OTC Tools must be installed on the image. Otherwise, this metric is unavailable.)</p>
</td>
<td class="cellrowborder" valign="top" width="19.55195519551955%" headers="mcps1.2.6.1.3 "><p id="p49339135105256"><a name="p49339135105256"></a><a name="p49339135105256"></a>x (Not supported)</p>
</td>
</tr>
<tr id="row41399039105256"><td class="cellrowborder" valign="top" width="21.802180218021803%" headers="mcps1.2.6.1.1 "><p id="p19600716418"><a name="p19600716418"></a><a name="p19600716418"></a>Disk Read Bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="18.98189818981898%" headers="mcps1.2.6.1.2 "><p id="p29528024105256"><a name="p29528024105256"></a><a name="p29528024105256"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="20.11201120112011%" headers="mcps1.2.6.1.2 "><p id="p49458243111156"><a name="p49458243111156"></a><a name="p49458243111156"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.55195519551955%" headers="mcps1.2.6.1.3 "><p id="p42959759105256"><a name="p42959759105256"></a><a name="p42959759105256"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.55195519551955%" headers="mcps1.2.6.1.3 "><p id="p57188483105256"><a name="p57188483105256"></a><a name="p57188483105256"></a>√</p>
</td>
</tr>
<tr id="row4688140611618"><td class="cellrowborder" valign="top" width="21.802180218021803%" headers="mcps1.2.6.1.1 "><p id="p1822812121446"><a name="p1822812121446"></a><a name="p1822812121446"></a>Disk Write Bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="18.98189818981898%" headers="mcps1.2.6.1.2 "><p id="p1813333611618"><a name="p1813333611618"></a><a name="p1813333611618"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="20.11201120112011%" headers="mcps1.2.6.1.2 "><p id="p46694713111156"><a name="p46694713111156"></a><a name="p46694713111156"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.55195519551955%" headers="mcps1.2.6.1.3 "><p id="p5951408111618"><a name="p5951408111618"></a><a name="p5951408111618"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.55195519551955%" headers="mcps1.2.6.1.3 "><p id="p5591121811618"><a name="p5591121811618"></a><a name="p5591121811618"></a>√</p>
</td>
</tr>
<tr id="row1132974911618"><td class="cellrowborder" valign="top" width="21.802180218021803%" headers="mcps1.2.6.1.1 "><p id="p1253012209414"><a name="p1253012209414"></a><a name="p1253012209414"></a>Disk Read IOPS</p>
</td>
<td class="cellrowborder" valign="top" width="18.98189818981898%" headers="mcps1.2.6.1.2 "><p id="p499687511618"><a name="p499687511618"></a><a name="p499687511618"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="20.11201120112011%" headers="mcps1.2.6.1.2 "><p id="p24175408111156"><a name="p24175408111156"></a><a name="p24175408111156"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.55195519551955%" headers="mcps1.2.6.1.3 "><p id="p209374911618"><a name="p209374911618"></a><a name="p209374911618"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.55195519551955%" headers="mcps1.2.6.1.3 "><p id="p3537597111618"><a name="p3537597111618"></a><a name="p3537597111618"></a>√</p>
</td>
</tr>
<tr id="row1115819211618"><td class="cellrowborder" valign="top" width="21.802180218021803%" headers="mcps1.2.6.1.1 "><p id="p1326013281743"><a name="p1326013281743"></a><a name="p1326013281743"></a>Disk Write IOPS</p>
</td>
<td class="cellrowborder" valign="top" width="18.98189818981898%" headers="mcps1.2.6.1.2 "><p id="p1414963011618"><a name="p1414963011618"></a><a name="p1414963011618"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="20.11201120112011%" headers="mcps1.2.6.1.2 "><p id="p12051023111156"><a name="p12051023111156"></a><a name="p12051023111156"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.55195519551955%" headers="mcps1.2.6.1.3 "><p id="p526937811618"><a name="p526937811618"></a><a name="p526937811618"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.55195519551955%" headers="mcps1.2.6.1.3 "><p id="p2416650311618"><a name="p2416650311618"></a><a name="p2416650311618"></a>√</p>
</td>
</tr>
<tr id="row456654211618"><td class="cellrowborder" valign="top" width="21.802180218021803%" headers="mcps1.2.6.1.1 "><p id="p2699216711644"><a name="p2699216711644"></a><a name="p2699216711644"></a>Inband Incoming Rate</p>
</td>
<td class="cellrowborder" valign="top" width="18.98189818981898%" headers="mcps1.2.6.1.2 "><p id="p4067515911618"><a name="p4067515911618"></a><a name="p4067515911618"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="20.11201120112011%" headers="mcps1.2.6.1.2 "><p id="p36608831111156"><a name="p36608831111156"></a><a name="p36608831111156"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.55195519551955%" headers="mcps1.2.6.1.3 "><p id="p635356811618"><a name="p635356811618"></a><a name="p635356811618"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.55195519551955%" headers="mcps1.2.6.1.3 "><p id="p4487699811618"><a name="p4487699811618"></a><a name="p4487699811618"></a>x (Not supported)</p>
</td>
</tr>
<tr id="row3462961611626"><td class="cellrowborder" valign="top" width="21.802180218021803%" headers="mcps1.2.6.1.1 "><p id="p1439291111644"><a name="p1439291111644"></a><a name="p1439291111644"></a>Inband Outgoing Rate</p>
</td>
<td class="cellrowborder" valign="top" width="18.98189818981898%" headers="mcps1.2.6.1.2 "><p id="p1205724611626"><a name="p1205724611626"></a><a name="p1205724611626"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="20.11201120112011%" headers="mcps1.2.6.1.2 "><p id="p12525352111156"><a name="p12525352111156"></a><a name="p12525352111156"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.55195519551955%" headers="mcps1.2.6.1.3 "><p id="p3711290911626"><a name="p3711290911626"></a><a name="p3711290911626"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.55195519551955%" headers="mcps1.2.6.1.3 "><p id="p5335568511626"><a name="p5335568511626"></a><a name="p5335568511626"></a>x (Not supported)</p>
</td>
</tr>
<tr id="row862172011626"><td class="cellrowborder" valign="top" width="21.802180218021803%" headers="mcps1.2.6.1.1 "><p id="p2344959811644"><a name="p2344959811644"></a><a name="p2344959811644"></a>Outband Incoming Rate</p>
</td>
<td class="cellrowborder" valign="top" width="18.98189818981898%" headers="mcps1.2.6.1.2 "><p id="p4410956311626"><a name="p4410956311626"></a><a name="p4410956311626"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="20.11201120112011%" headers="mcps1.2.6.1.2 "><p id="p7920561111156"><a name="p7920561111156"></a><a name="p7920561111156"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.55195519551955%" headers="mcps1.2.6.1.3 "><p id="p1610485911626"><a name="p1610485911626"></a><a name="p1610485911626"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.55195519551955%" headers="mcps1.2.6.1.3 "><p id="p2942518311626"><a name="p2942518311626"></a><a name="p2942518311626"></a>√</p>
</td>
</tr>
<tr id="row3742495611626"><td class="cellrowborder" valign="top" width="21.802180218021803%" headers="mcps1.2.6.1.1 "><p id="p4910578311644"><a name="p4910578311644"></a><a name="p4910578311644"></a>Outband Outgoing Rate</p>
</td>
<td class="cellrowborder" valign="top" width="18.98189818981898%" headers="mcps1.2.6.1.2 "><p id="p3659425511626"><a name="p3659425511626"></a><a name="p3659425511626"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="20.11201120112011%" headers="mcps1.2.6.1.2 "><p id="p37585666111156"><a name="p37585666111156"></a><a name="p37585666111156"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.55195519551955%" headers="mcps1.2.6.1.3 "><p id="p1134466511626"><a name="p1134466511626"></a><a name="p1134466511626"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.55195519551955%" headers="mcps1.2.6.1.3 "><p id="p4650269211626"><a name="p4650269211626"></a><a name="p4650269211626"></a>√</p>
</td>
</tr>
<tr id="row78415331170"><td class="cellrowborder" valign="top" width="21.802180218021803%" headers="mcps1.2.6.1.1 "><p id="p316336171174"><a name="p316336171174"></a><a name="p316336171174"></a>System Status Check Failed</p>
</td>
<td class="cellrowborder" valign="top" width="18.98189818981898%" headers="mcps1.2.6.1.2 "><p id="p122244601170"><a name="p122244601170"></a><a name="p122244601170"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="20.11201120112011%" headers="mcps1.2.6.1.2 "><p id="p24540100111156"><a name="p24540100111156"></a><a name="p24540100111156"></a>x</p>
</td>
<td class="cellrowborder" valign="top" width="19.55195519551955%" headers="mcps1.2.6.1.3 "><p id="p506571751170"><a name="p506571751170"></a><a name="p506571751170"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.55195519551955%" headers="mcps1.2.6.1.3 "><p id="p95905151170"><a name="p95905151170"></a><a name="p95905151170"></a>x</p>
</td>
</tr>
<tr id="row41528888111754"><td class="cellrowborder" valign="top" width="21.802180218021803%" headers="mcps1.2.6.1.1 "><p id="p38215678111754"><a name="p38215678111754"></a><a name="p38215678111754"></a>InfiniBand NIC status</p>
</td>
<td class="cellrowborder" valign="top" width="18.98189818981898%" headers="mcps1.2.6.1.2 "><p id="p8462202111754"><a name="p8462202111754"></a><a name="p8462202111754"></a>x</p>
</td>
<td class="cellrowborder" valign="top" width="20.11201120112011%" headers="mcps1.2.6.1.2 "><p id="p14349722111754"><a name="p14349722111754"></a><a name="p14349722111754"></a>√ (Only for H2 ECSs)</p>
</td>
<td class="cellrowborder" valign="top" width="19.55195519551955%" headers="mcps1.2.6.1.3 "><p id="p21476806111754"><a name="p21476806111754"></a><a name="p21476806111754"></a>x</p>
</td>
<td class="cellrowborder" valign="top" width="19.55195519551955%" headers="mcps1.2.6.1.3 "><p id="p61899751111754"><a name="p61899751111754"></a><a name="p61899751111754"></a>√ (Only for H2 ECSs)</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>The image based on which the target ECS is created must have OTC Tools installed \(OTC Tools has been installed for public images by default\). Otherwise, the  **Memory Usage**  and  **Disk Usage**  metrics are unavailable. For details about how to install the OTC Tools, visit  [https://github.com/UVP-Tools/UVP-Tools/](https://github.com/UVP-Tools/UVP-Tools/).  

[Table 2](#table64866324222846)  describes these ECS metrics.

The monitoring intervals for the following ECSs with raw monitoring metrics are as follows:

-   Xen ECSs: 4 minutes
-   KVM ECSs: 5 minutes

**Table  2**  Metric description

<a name="table64866324222846"></a>
<table><thead align="left"><tr id="row15175257222846"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.7.1.1"><p id="p55090151112133"><a name="p55090151112133"></a><a name="p55090151112133"></a>Metric</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.7.1.2"><p id="p21236279222846"><a name="p21236279222846"></a><a name="p21236279222846"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.2.7.1.3"><p id="p42417005222846"><a name="p42417005222846"></a><a name="p42417005222846"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="11%" id="mcps1.2.7.1.4"><p id="p64622851222846"><a name="p64622851222846"></a><a name="p64622851222846"></a>Value Range</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.7.1.5"><p id="p67068467222846"><a name="p67068467222846"></a><a name="p67068467222846"></a>Monitored Object</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.7.1.6"><p id="p92927044715"><a name="p92927044715"></a><a name="p92927044715"></a>Monitoring Interval (Raw Metrics and KVM Only)</p>
</th>
</tr>
</thead>
<tbody><tr id="row63836764222846"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.1 "><p id="p10069772112133"><a name="p10069772112133"></a><a name="p10069772112133"></a>cpu_util</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.2 "><p id="p3395365222846"><a name="p3395365222846"></a><a name="p3395365222846"></a>CPU Usage</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.7.1.3 "><p id="p6589110222846"><a name="p6589110222846"></a><a name="p6589110222846"></a>CPU usage of an ECS</p>
<p id="p370229193114"><a name="p370229193114"></a><a name="p370229193114"></a>Unit: Percent</p>
<p id="p11196181114376"><a name="p11196181114376"></a><a name="p11196181114376"></a>Formula: CPU usage of an ECS/Number of vCPUs in the ECS</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.4 "><p id="p13045074222846"><a name="p13045074222846"></a><a name="p13045074222846"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.5 "><p id="p18876142014717"><a name="p18876142014717"></a><a name="p18876142014717"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.7.1.6 "><p id="p162937034720"><a name="p162937034720"></a><a name="p162937034720"></a>5 minutes</p>
</td>
</tr>
<tr id="row47509658222846"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.1 "><p id="p124210503017"><a name="p124210503017"></a><a name="p124210503017"></a>mem_util</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.2 "><p id="p23077113222846"><a name="p23077113222846"></a><a name="p23077113222846"></a>Memory Usage</p>
<p id="p6367428222846"><a name="p6367428222846"></a><a name="p6367428222846"></a></p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.7.1.3 "><p id="p88761115174313"><a name="p88761115174313"></a><a name="p88761115174313"></a>Memory usage of an ECS</p>
<p id="p9514173893717"><a name="p9514173893717"></a><a name="p9514173893717"></a>This metric is unavailable if the image has no OTC Tools installed.</p>
<p id="p740255511317"><a name="p740255511317"></a><a name="p740255511317"></a>Unit: Percent</p>
<p id="p45999697222846"><a name="p45999697222846"></a><a name="p45999697222846"></a>Formula: Used memory of an ECS/Total memory of the ECS</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.4 "><p id="p15452979222846"><a name="p15452979222846"></a><a name="p15452979222846"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.5 "><p id="p43731801222846"><a name="p43731801222846"></a><a name="p43731801222846"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.7.1.6 "><p id="p1529314019473"><a name="p1529314019473"></a><a name="p1529314019473"></a>5 minutes</p>
</td>
</tr>
<tr id="row58041894222846"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.1 "><p id="p1924275153012"><a name="p1924275153012"></a><a name="p1924275153012"></a>disk_util_inband</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.2 "><p id="p3772951222846"><a name="p3772951222846"></a><a name="p3772951222846"></a>Disk Usage</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.7.1.3 "><p id="p661521494312"><a name="p661521494312"></a><a name="p661521494312"></a>Disk usage of an ECS</p>
<p id="p37173646222846"><a name="p37173646222846"></a><a name="p37173646222846"></a>This metric is unavailable if the image has no OTC Tools installed.</p>
<p id="p499211413328"><a name="p499211413328"></a><a name="p499211413328"></a>Unit: Percent</p>
<p id="p16310184093713"><a name="p16310184093713"></a><a name="p16310184093713"></a>Formula: Used capacity of an ECS disk/Total capacity of the ECS disk</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.4 "><p id="p22679847222846"><a name="p22679847222846"></a><a name="p22679847222846"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.5 "><p id="p25128347222846"><a name="p25128347222846"></a><a name="p25128347222846"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.7.1.6 "><p id="p72931703474"><a name="p72931703474"></a><a name="p72931703474"></a>5 minutes</p>
</td>
</tr>
<tr id="row24828535222846"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.1 "><p id="p15534971112133"><a name="p15534971112133"></a><a name="p15534971112133"></a>disk_read_bytes_rate</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.2 "><p id="p292712452495"><a name="p292712452495"></a><a name="p292712452495"></a>Disk Read Bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.7.1.3 "><p id="p26808602222846"><a name="p26808602222846"></a><a name="p26808602222846"></a>Number of bytes read from an ECS disk per second</p>
<p id="p1428281363215"><a name="p1428281363215"></a><a name="p1428281363215"></a>Unit: byte/s</p>
<p id="p139664438371"><a name="p139664438371"></a><a name="p139664438371"></a>Formula: Total number of bytes read from an ECS disk/Monitoring interval</p>
<p id="p13259851114311"><a name="p13259851114311"></a><a name="p13259851114311"></a>byte_out = (rd_bytes - last_rd_bytes)/Time difference</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.4 "><p id="p66019488222846"><a name="p66019488222846"></a><a name="p66019488222846"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.5 "><p id="p45978283222846"><a name="p45978283222846"></a><a name="p45978283222846"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.7.1.6 "><p id="p1929370154718"><a name="p1929370154718"></a><a name="p1929370154718"></a>5 minutes</p>
</td>
</tr>
<tr id="row11151367222846"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.1 "><p id="p17518185112133"><a name="p17518185112133"></a><a name="p17518185112133"></a>disk_write_bytes_rate</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.2 "><p id="p18939164514497"><a name="p18939164514497"></a><a name="p18939164514497"></a>Disk Write Bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.7.1.3 "><p id="p15463290222846"><a name="p15463290222846"></a><a name="p15463290222846"></a>Number of bytes written to an ECS disk per second</p>
<p id="p67319380323"><a name="p67319380323"></a><a name="p67319380323"></a>Unit: byte/s</p>
<p id="p13629649103720"><a name="p13629649103720"></a><a name="p13629649103720"></a>Formula: Total number of bytes written to an ECS disk/Monitoring interval</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.4 "><p id="p53157119222846"><a name="p53157119222846"></a><a name="p53157119222846"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.5 "><p id="p10759388222846"><a name="p10759388222846"></a><a name="p10759388222846"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.7.1.6 "><p id="p3293130104711"><a name="p3293130104711"></a><a name="p3293130104711"></a>5 minutes</p>
</td>
</tr>
<tr id="row29725634222846"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.1 "><p id="p18875184112133"><a name="p18875184112133"></a><a name="p18875184112133"></a>disk_read_requests_rate</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.2 "><p id="p59508458491"><a name="p59508458491"></a><a name="p59508458491"></a>Disk Read IOPS</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.7.1.3 "><p id="p11529080222846"><a name="p11529080222846"></a><a name="p11529080222846"></a>Number of read requests sent to an ECS disk per second</p>
<p id="p04261505333"><a name="p04261505333"></a><a name="p04261505333"></a>Unit: request/s</p>
<p id="p15021352143711"><a name="p15021352143711"></a><a name="p15021352143711"></a>Formula: Total number of read requests sent to an ECS disk/Monitoring interval</p>
<p id="p19923180174416"><a name="p19923180174416"></a><a name="p19923180174416"></a>req_out = (rd_req - last_rd_req)/Time difference</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.4 "><p id="p10609393222846"><a name="p10609393222846"></a><a name="p10609393222846"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.5 "><p id="p54054474222846"><a name="p54054474222846"></a><a name="p54054474222846"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.7.1.6 "><p id="p32931706476"><a name="p32931706476"></a><a name="p32931706476"></a>5 minutes</p>
</td>
</tr>
<tr id="row16728218222846"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.1 "><p id="p19979544112133"><a name="p19979544112133"></a><a name="p19979544112133"></a>disk_write_requests_rate</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.2 "><p id="p11969114513496"><a name="p11969114513496"></a><a name="p11969114513496"></a>Disk Write IOPS</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.7.1.3 "><p id="p30846695222846"><a name="p30846695222846"></a><a name="p30846695222846"></a>Number of write requests sent to an ECS disk per second</p>
<p id="p116931923173320"><a name="p116931923173320"></a><a name="p116931923173320"></a>Unit: request/s</p>
<p id="p21821655103712"><a name="p21821655103712"></a><a name="p21821655103712"></a>Formula: Total number of write requests sent to an ECS disk/Monitoring interval</p>
<p id="p1357557164413"><a name="p1357557164413"></a><a name="p1357557164413"></a>req_in = (wr_req - last_wr_req)/Time difference</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.4 "><p id="p51947303222846"><a name="p51947303222846"></a><a name="p51947303222846"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.5 "><p id="p46982038222846"><a name="p46982038222846"></a><a name="p46982038222846"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.7.1.6 "><p id="p18293105476"><a name="p18293105476"></a><a name="p18293105476"></a>5 minutes</p>
</td>
</tr>
<tr id="row20185161222846"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.1 "><p id="p34483231112133"><a name="p34483231112133"></a><a name="p34483231112133"></a>network_incoming_bytes_rate_inband</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.2 "><p id="p24385382222846"><a name="p24385382222846"></a><a name="p24385382222846"></a>Inband Incoming Rate</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.7.1.3 "><p id="p29058915222846"><a name="p29058915222846"></a><a name="p29058915222846"></a>Number of incoming bytes on an ECS per second</p>
<p id="p14765153917334"><a name="p14765153917334"></a><a name="p14765153917334"></a>Unit: byte/s</p>
<p id="p6126135893715"><a name="p6126135893715"></a><a name="p6126135893715"></a>Formula: Total number of inband incoming bytes on an ECS/Monitoring interval</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.4 "><p id="p66369310222846"><a name="p66369310222846"></a><a name="p66369310222846"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.5 "><p id="p7205036222846"><a name="p7205036222846"></a><a name="p7205036222846"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.7.1.6 "><p id="p82931008478"><a name="p82931008478"></a><a name="p82931008478"></a>5 minutes</p>
</td>
</tr>
<tr id="row64845332222846"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.1 "><p id="p7574877112133"><a name="p7574877112133"></a><a name="p7574877112133"></a>network_outgoing_bytes_rate_inband</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.2 "><p id="p17980571222846"><a name="p17980571222846"></a><a name="p17980571222846"></a>Inband Outgoing Rate</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.7.1.3 "><p id="p47140109222846"><a name="p47140109222846"></a><a name="p47140109222846"></a>Number of outgoing bytes on an ECS per second</p>
<p id="p372019126349"><a name="p372019126349"></a><a name="p372019126349"></a>Unit: byte/s</p>
<p id="p2336161163817"><a name="p2336161163817"></a><a name="p2336161163817"></a>Formula: Total number of inband outgoing bytes on an ECS/Monitoring interval</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.4 "><p id="p48614360222846"><a name="p48614360222846"></a><a name="p48614360222846"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.5 "><p id="p45449088222846"><a name="p45449088222846"></a><a name="p45449088222846"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.7.1.6 "><p id="p1429311044718"><a name="p1429311044718"></a><a name="p1429311044718"></a>5 minutes</p>
</td>
</tr>
<tr id="row22492419121215"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.1 "><p id="p31280203115945"><a name="p31280203115945"></a><a name="p31280203115945"></a>network_incoming_bytes_aggregate_rate</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.2 "><p id="p1105187121215"><a name="p1105187121215"></a><a name="p1105187121215"></a>Outband Incoming Rate</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.7.1.3 "><p id="p22411285121215"><a name="p22411285121215"></a><a name="p22411285121215"></a>Number of incoming bytes on an ECS per second on the hypervisor</p>
<p id="p727510295345"><a name="p727510295345"></a><a name="p727510295345"></a>Unit: byte/s</p>
<p id="p157791355389"><a name="p157791355389"></a><a name="p157791355389"></a>Formula: Total number of outband incoming bytes on an ECS/Monitoring interval</p>
<p id="p542192819444"><a name="p542192819444"></a><a name="p542192819444"></a>This metric is unavailable if SR-IOV is enabled.</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.4 "><p id="p4924384121215"><a name="p4924384121215"></a><a name="p4924384121215"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.5 "><p id="p63330824121215"><a name="p63330824121215"></a><a name="p63330824121215"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.7.1.6 "><p id="p132931016476"><a name="p132931016476"></a><a name="p132931016476"></a>5 minutes</p>
</td>
</tr>
<tr id="row62680097121215"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.1 "><p id="p27286742115945"><a name="p27286742115945"></a><a name="p27286742115945"></a>network_outgoing_bytes_ aggregate_rate</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.2 "><p id="p27249966121215"><a name="p27249966121215"></a><a name="p27249966121215"></a>Outband Outgoing Rate</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.7.1.3 "><p id="p59763627121215"><a name="p59763627121215"></a><a name="p59763627121215"></a>Number of outgoing bytes on an ECS per second on the hypervisor</p>
<p id="p10272498343"><a name="p10272498343"></a><a name="p10272498343"></a>Unit: byte/s</p>
<p id="p1112031083818"><a name="p1112031083818"></a><a name="p1112031083818"></a>Formula: Total number of outband outgoing bytes on an ECS/Monitoring interval</p>
<p id="p17183383445"><a name="p17183383445"></a><a name="p17183383445"></a>This metric is unavailable if SR-IOV is enabled.</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.4 "><p id="p59175014121215"><a name="p59175014121215"></a><a name="p59175014121215"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.5 "><p id="p28446836121215"><a name="p28446836121215"></a><a name="p28446836121215"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.7.1.6 "><p id="p182931501478"><a name="p182931501478"></a><a name="p182931501478"></a>5 minutes</p>
</td>
</tr>
<tr id="row2605901916337"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.1 "><p id="p324211523017"><a name="p324211523017"></a><a name="p324211523017"></a>inst_sys_status_error</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.2 "><p id="p3320458516337"><a name="p3320458516337"></a><a name="p3320458516337"></a>System Status Check Failed</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.7.1.3 "><p id="p521685316337"><a name="p521685316337"></a><a name="p521685316337"></a>Status of the cloud platform for running ECSs, which can be <strong id="b1565424293203310"><a name="b1565424293203310"></a><a name="b1565424293203310"></a>0</strong> or <strong id="b1229152802203310"><a name="b1229152802203310"></a><a name="b1229152802203310"></a>1</strong></p>
<a name="ul13348182820394"></a><a name="ul13348182820394"></a><ul id="ul13348182820394"><li><strong id="b171676334619247"><a name="b171676334619247"></a><a name="b171676334619247"></a>0</strong>: The system is running properly. All check items are normal.</li><li><strong id="b1087511831192613"><a name="b1087511831192613"></a><a name="b1087511831192613"></a>1</strong>: The system is not running properly. At least one check item failed. When the power source of the physical host fails or the hardware/software becomes faulty, the check result is <strong id="b842352706201616"><a name="b842352706201616"></a><a name="b842352706201616"></a>1</strong>.</li></ul>
<p id="p5086914416723"><a name="p5086914416723"></a><a name="p5086914416723"></a>The system periodically checks the status and returns check results using value <strong id="b842352706192323"><a name="b842352706192323"></a><a name="b842352706192323"></a>0</strong> or <strong id="b842352706192327"><a name="b842352706192327"></a><a name="b842352706192327"></a>1</strong>.</p>
<a name="ul3386195716122"></a><a name="ul3386195716122"></a><ul id="ul3386195716122"><li>If the detected fault does not affect ECS functions, certain management operations performed on the ECS, such as starting, stopping, or specifications modifications, may be affected.</li><li>If the detected fault affects ECS functions, such as a host power supply failure, the system will recover the ECS as soon as possible. </li></ul>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.4 "><p id="p72621040193911"><a name="p72621040193911"></a><a name="p72621040193911"></a><strong>0</strong> or <strong>1</strong></p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.5 "><p id="p225190516337"><a name="p225190516337"></a><a name="p225190516337"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.7.1.6 "><p id="p20293206479"><a name="p20293206479"></a><a name="p20293206479"></a>5 minutes</p>
</td>
</tr>
<tr id="row44572200141717"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.1 "><p id="p024210514305"><a name="p024210514305"></a><a name="p024210514305"></a>ib_card_state</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.2 "><p id="p65605483141717"><a name="p65605483141717"></a><a name="p65605483141717"></a>InfiniBand NIC status</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.7.1.3 "><p id="p12443932141717"><a name="p12443932141717"></a><a name="p12443932141717"></a>Status of an InfiniBand NIC on an H2 ECS</p>
<p id="p1325610141717"><a name="p1325610141717"></a><a name="p1325610141717"></a>The system periodically checks the status and returns check results using value <strong id="b1226863769"><a name="b1226863769"></a><a name="b1226863769"></a>0</strong> or <strong id="b686144398"><a name="b686144398"></a><a name="b686144398"></a>1</strong>.</p>
<a name="ul94245295397"></a><a name="ul94245295397"></a><ul id="ul94245295397"><li><strong id="b1295345995"><a name="b1295345995"></a><a name="b1295345995"></a>0</strong>: The system is running properly. That is, the InfiniBand NIC is functional.</li><li><strong id="b1157944315"><a name="b1157944315"></a><a name="b1157944315"></a>1</strong>: The system is not running properly. That is, the InfiniBand NIC malfunctions. When the physical NIC corresponding to a virtual NIC becomes faulty, for example, the network cable is not securely connected to the NIC, the switch or adapter is incompatible with the InfiniBand NIC, or the NIC is disabled, the returned value is <strong id="b842352706174428"><a name="b842352706174428"></a><a name="b842352706174428"></a>1</strong>.</li></ul>
<div class="note" id="note14324438161653"><a name="note14324438161653"></a><a name="note14324438161653"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p61811084161653"><a name="p61811084161653"></a><a name="p61811084161653"></a>Only Mellanox EDR 100 GB single-port InfiniBand NICs are supported.</p>
</div></div>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.4 "><p id="p1139153311398"><a name="p1139153311398"></a><a name="p1139153311398"></a><strong>0</strong> or <strong>1</strong></p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.5 "><p id="p40265596141717"><a name="p40265596141717"></a><a name="p40265596141717"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.7.1.6 "><p id="p1429319013473"><a name="p1429319013473"></a><a name="p1429319013473"></a>5 minutes</p>
</td>
</tr>
</tbody>
</table>

## Dimensions<a name="section36963297112133"></a>

<a name="table41237041112133"></a>
<table><thead align="left"><tr id="row28021974112133"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p55187441112133"><a name="p55187441112133"></a><a name="p55187441112133"></a>Key</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p40997749112133"><a name="p40997749112133"></a><a name="p40997749112133"></a>Value</p>
</th>
</tr>
</thead>
<tbody><tr id="row32483336112133"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p13904597112133"><a name="p13904597112133"></a><a name="p13904597112133"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p52530562112133"><a name="p52530562112133"></a><a name="p52530562112133"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

