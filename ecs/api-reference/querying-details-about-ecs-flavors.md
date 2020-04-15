# Querying Details About ECS Flavors<a name="EN-US_TOPIC_0020212658"></a>

## Function<a name="section57769674"></a>

This API is used to query details about ECS flavors.

## URI<a name="section50165025"></a>

GET /v2/\{project\_id\}/flavors/detail\{?minDisk,minRam,sort\_key,sort\_dir\}

GET /v2.1/\{project\_id\}/flavors/detail\{?minDisk,minRam,sort\_key,sort\_dir\}

[Table 1](#table46110007)  describes the parameters in the URI.

**Table  1**  Path parameters

<a name="table46110007"></a>
<table><thead align="left"><tr id="row14148614"><th class="cellrowborder" valign="top" width="16.98%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.18%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.84%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row17201924"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.1 "><p id="p51178607"><a name="p51178607"></a><a name="p51178607"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.18%" headers="mcps1.2.4.1.2 "><p id="p51826478"><a name="p51826478"></a><a name="p51826478"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.84%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  Query parameters

<a name="table042719354613"></a>
<table><thead align="left"><tr id="row742718319462"><th class="cellrowborder" valign="top" width="16.919999999999998%" id="mcps1.2.5.1.1"><p id="en-us_topic_0057973030_p1494644"><a name="en-us_topic_0057973030_p1494644"></a><a name="en-us_topic_0057973030_p1494644"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.36%" id="mcps1.2.5.1.2"><p id="p1052214117427"><a name="p1052214117427"></a><a name="p1052214117427"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.24%" id="mcps1.2.5.1.3"><p id="en-us_topic_0057973030_p53957349"><a name="en-us_topic_0057973030_p53957349"></a><a name="en-us_topic_0057973030_p53957349"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.480000000000004%" id="mcps1.2.5.1.4"><p id="en-us_topic_0057973030_p14912584"><a name="en-us_topic_0057973030_p14912584"></a><a name="en-us_topic_0057973030_p14912584"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row144271334468"><td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.1 "><p id="p44273304617"><a name="p44273304617"></a><a name="p44273304617"></a>minDisk</p>
</td>
<td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.5.1.2 "><p id="p242715320466"><a name="p242715320466"></a><a name="p242715320466"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.24%" headers="mcps1.2.5.1.3 "><p id="p1742720324617"><a name="p1742720324617"></a><a name="p1742720324617"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.480000000000004%" headers="mcps1.2.5.1.4 "><p id="p14277313465"><a name="p14277313465"></a><a name="p14277313465"></a>Specifies the minimum disk specification in the unit of GB. Only the ECSs with the disk specification greater than or equal to the minimum specification can be queried.</p>
</td>
</tr>
<tr id="row942719310465"><td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.1 "><p id="p1542716374613"><a name="p1542716374613"></a><a name="p1542716374613"></a>minRam</p>
</td>
<td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.5.1.2 "><p id="p11427735469"><a name="p11427735469"></a><a name="p11427735469"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.24%" headers="mcps1.2.5.1.3 "><p id="p14273316463"><a name="p14273316463"></a><a name="p14273316463"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.480000000000004%" headers="mcps1.2.5.1.4 "><p id="p1842714344616"><a name="p1842714344616"></a><a name="p1842714344616"></a>Specifies the minimum RAM in the unit of MB. Only the ECSs with the RAM specification greater than or equal to the minimum specification can be queried.</p>
</td>
</tr>
<tr id="row6427173164613"><td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.1 "><p id="p942710364612"><a name="p942710364612"></a><a name="p942710364612"></a>sort_key</p>
</td>
<td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.5.1.2 "><p id="p16427433461"><a name="p16427433461"></a><a name="p16427433461"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.24%" headers="mcps1.2.5.1.3 "><p id="p104271333463"><a name="p104271333463"></a><a name="p104271333463"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.480000000000004%" headers="mcps1.2.5.1.4 "><p id="p1142783114612"><a name="p1142783114612"></a><a name="p1142783114612"></a>Indicates a sorting field, the default value of which is <strong id="b842352706101459"><a name="b842352706101459"></a><a name="b842352706101459"></a>flavorid</strong>. The value of this parameter can also be <strong id="b842352706101549"><a name="b842352706101549"></a><a name="b842352706101549"></a>name</strong>, <strong id="b842352706101555"><a name="b842352706101555"></a><a name="b842352706101555"></a>memory_mb</strong>, <strong id="b842352706101622"><a name="b842352706101622"></a><a name="b842352706101622"></a>vcpus</strong>, <strong id="b842352706101625"><a name="b842352706101625"></a><a name="b842352706101625"></a>root_gb</strong>, or <strong id="b842352706144441"><a name="b842352706144441"></a><a name="b842352706144441"></a>flavorid</strong>.</p>
</td>
</tr>
<tr id="row642717310465"><td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.1 "><p id="p642716364610"><a name="p642716364610"></a><a name="p642716364610"></a>sort_dir</p>
</td>
<td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.5.1.2 "><p id="p1342773174619"><a name="p1342773174619"></a><a name="p1342773174619"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.24%" headers="mcps1.2.5.1.3 "><p id="p15427035461"><a name="p15427035461"></a><a name="p15427035461"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.480000000000004%" headers="mcps1.2.5.1.4 "><p id="p134272310466"><a name="p134272310466"></a><a name="p134272310466"></a>Specifies the ascending (<strong id="b740796858102558"><a name="b740796858102558"></a><a name="b740796858102558"></a>asc</strong>) or descending (<strong id="b67906925910263"><a name="b67906925910263"></a><a name="b67906925910263"></a>desc</strong>) sorting. Options: <strong id="b274442023102145"><a name="b274442023102145"></a><a name="b274442023102145"></a>asc</strong> and <strong id="b308485864173554"><a name="b308485864173554"></a><a name="b308485864173554"></a>desc</strong></p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section136523104620"></a>

None

## Response<a name="section36835188"></a>

[Table 3](#table23477058)  describes the response parameters.

**Table  3**  Response parameters

<a name="table23477058"></a>
<table><thead align="left"><tr id="row2792905"><th class="cellrowborder" valign="top" width="17.16%" id="mcps1.2.4.1.1"><p id="p110452114597"><a name="p110452114597"></a><a name="p110452114597"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.23%" id="mcps1.2.4.1.2"><p id="p71044217595"><a name="p71044217595"></a><a name="p71044217595"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="66.61%" id="mcps1.2.4.1.3"><p id="p15104102175910"><a name="p15104102175910"></a><a name="p15104102175910"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row9994955"><td class="cellrowborder" valign="top" width="17.16%" headers="mcps1.2.4.1.1 "><p id="p4284989"><a name="p4284989"></a><a name="p4284989"></a>flavors</p>
</td>
<td class="cellrowborder" valign="top" width="16.23%" headers="mcps1.2.4.1.2 "><p id="p62312200"><a name="p62312200"></a><a name="p62312200"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="66.61%" headers="mcps1.2.4.1.3 "><p id="p127029403320"><a name="p127029403320"></a><a name="p127029403320"></a>Specifies ECS flavors. For details, see <a href="#table13194498">Table 4</a>.</p>
</td>
</tr>
<tr id="row19878185610436"><td class="cellrowborder" valign="top" width="17.16%" headers="mcps1.2.4.1.1 "><p id="p187945610434"><a name="p187945610434"></a><a name="p187945610434"></a>flavors_links</p>
</td>
<td class="cellrowborder" valign="top" width="16.23%" headers="mcps1.2.4.1.2 "><p id="p0953191316483"><a name="p0953191316483"></a><a name="p0953191316483"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="66.61%" headers="mcps1.2.4.1.3 "><p id="p5483191813483"><a name="p5483191813483"></a><a name="p5483191813483"></a>Specifies data links for querying the next pages in pagination query. For details, see <a href="#table15913898194628">Table 5</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **flavors**  field description

<a name="table13194498"></a>
<table><thead align="left"><tr id="row35873632"><th class="cellrowborder" valign="top" width="17.11%" id="mcps1.2.4.1.1"><p id="p8760175413114"><a name="p8760175413114"></a><a name="p8760175413114"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.38%" id="mcps1.2.4.1.2"><p id="p18760195414120"><a name="p18760195414120"></a><a name="p18760195414120"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="66.51%" id="mcps1.2.4.1.3"><p id="p1176095419111"><a name="p1176095419111"></a><a name="p1176095419111"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row15349251"><td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.2.4.1.1 "><p id="p35329809"><a name="p35329809"></a><a name="p35329809"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16.38%" headers="mcps1.2.4.1.2 "><p id="p24536113173145"><a name="p24536113173145"></a><a name="p24536113173145"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="66.51%" headers="mcps1.2.4.1.3 "><p id="p56261663"><a name="p56261663"></a><a name="p56261663"></a>Specifies the ECS flavor ID.</p>
</td>
</tr>
<tr id="row36592919"><td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.2.4.1.1 "><p id="p11236435"><a name="p11236435"></a><a name="p11236435"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.38%" headers="mcps1.2.4.1.2 "><p id="p54383891173145"><a name="p54383891173145"></a><a name="p54383891173145"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="66.51%" headers="mcps1.2.4.1.3 "><p id="p61525259"><a name="p61525259"></a><a name="p61525259"></a>Specifies the name of the ECS flavor.</p>
</td>
</tr>
<tr id="row126833218304"><td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.2.4.1.1 "><p id="p7268143212303"><a name="p7268143212303"></a><a name="p7268143212303"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="16.38%" headers="mcps1.2.4.1.2 "><p id="p5268193243011"><a name="p5268193243011"></a><a name="p5268193243011"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="66.51%" headers="mcps1.2.4.1.3 "><p id="p7268432113013"><a name="p7268432113013"></a><a name="p7268432113013"></a>Describes the ECS flavor.</p>
<p id="p18128110183110"><a name="p18128110183110"></a><a name="p18128110183110"></a>This field is supported in microversions later than 2.55.</p>
</td>
</tr>
<tr id="row16856419"><td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.2.4.1.1 "><p id="p23192694"><a name="p23192694"></a><a name="p23192694"></a>vcpus</p>
</td>
<td class="cellrowborder" valign="top" width="16.38%" headers="mcps1.2.4.1.2 "><p id="p61992247173145"><a name="p61992247173145"></a><a name="p61992247173145"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="66.51%" headers="mcps1.2.4.1.3 "><p id="p60827539"><a name="p60827539"></a><a name="p60827539"></a>Specifies the number of vCPUs in the ECS flavor.</p>
</td>
</tr>
<tr id="row3097644510336"><td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.2.4.1.1 "><p id="p3929432310349"><a name="p3929432310349"></a><a name="p3929432310349"></a>ram</p>
</td>
<td class="cellrowborder" valign="top" width="16.38%" headers="mcps1.2.4.1.2 "><p id="p51423198173145"><a name="p51423198173145"></a><a name="p51423198173145"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="66.51%" headers="mcps1.2.4.1.3 "><p id="p154673810349"><a name="p154673810349"></a><a name="p154673810349"></a>Specifies the memory size (MB) in the ECS flavor.</p>
</td>
</tr>
<tr id="row10576944"><td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.2.4.1.1 "><p id="p51426113"><a name="p51426113"></a><a name="p51426113"></a>disk</p>
</td>
<td class="cellrowborder" valign="top" width="16.38%" headers="mcps1.2.4.1.2 "><p id="p31344710173145"><a name="p31344710173145"></a><a name="p31344710173145"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="66.51%" headers="mcps1.2.4.1.3 "><p id="p19756352"><a name="p19756352"></a><a name="p19756352"></a>Specifies the system disk size in the ECS flavor.</p>
<p id="p43589445"><a name="p43589445"></a><a name="p43589445"></a>This parameter has not been used. Its default value is <strong id="b84235270611135"><a name="b84235270611135"></a><a name="b84235270611135"></a>0</strong>.</p>
</td>
</tr>
<tr id="row56760689"><td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.2.4.1.1 "><p id="p34213098"><a name="p34213098"></a><a name="p34213098"></a>swap</p>
</td>
<td class="cellrowborder" valign="top" width="16.38%" headers="mcps1.2.4.1.2 "><p id="p31087024173145"><a name="p31087024173145"></a><a name="p31087024173145"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="66.51%" headers="mcps1.2.4.1.3 "><p id="p1699362755013"><a name="p1699362755013"></a><a name="p1699362755013"></a>Specifies the swap partition size required by the ECS flavor.</p>
<p id="p4563766173425"><a name="p4563766173425"></a><a name="p4563766173425"></a>This parameter has not been used. Its default value is <strong id="b84235270611135_1"><a name="b84235270611135_1"></a><a name="b84235270611135_1"></a>""</strong>.</p>
</td>
</tr>
<tr id="row56925253"><td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.2.4.1.1 "><p id="p47542785"><a name="p47542785"></a><a name="p47542785"></a>OS-FLV-EXT-DATA:ephemeral</p>
</td>
<td class="cellrowborder" valign="top" width="16.38%" headers="mcps1.2.4.1.2 "><p id="p18132829173145"><a name="p18132829173145"></a><a name="p18132829173145"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="66.51%" headers="mcps1.2.4.1.3 "><p id="p16591226713"><a name="p16591226713"></a><a name="p16591226713"></a>Specifies the temporary disk size. This is an extended attribute.</p>
<p id="p1140814148017"><a name="p1140814148017"></a><a name="p1140814148017"></a>This parameter has not been used. Its default value is <strong id="b84235270611135_2"><a name="b84235270611135_2"></a><a name="b84235270611135_2"></a>0</strong>.</p>
</td>
</tr>
<tr id="row44806966"><td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.2.4.1.1 "><p id="p5485596"><a name="p5485596"></a><a name="p5485596"></a>OS-FLV-DISABLED:disabled</p>
</td>
<td class="cellrowborder" valign="top" width="16.38%" headers="mcps1.2.4.1.2 "><p id="p52585611173145"><a name="p52585611173145"></a><a name="p52585611173145"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="66.51%" headers="mcps1.2.4.1.3 "><p id="p32761310192019"><a name="p32761310192019"></a><a name="p32761310192019"></a>Specifies whether the ECS flavor has been disabled. This is an extended attribute.</p>
<p id="p182115151112"><a name="p182115151112"></a><a name="p182115151112"></a>This parameter has not been used. Its default value is <strong id="b84235270611135_3"><a name="b84235270611135_3"></a><a name="b84235270611135_3"></a>false</strong>.</p>
</td>
</tr>
<tr id="row42184651"><td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.2.4.1.1 "><p id="p61513540"><a name="p61513540"></a><a name="p61513540"></a>rxtx_factor</p>
</td>
<td class="cellrowborder" valign="top" width="16.38%" headers="mcps1.2.4.1.2 "><p id="p7527547173145"><a name="p7527547173145"></a><a name="p7527547173145"></a>Float</p>
</td>
<td class="cellrowborder" valign="top" width="66.51%" headers="mcps1.2.4.1.3 "><p id="p16772171313154"><a name="p16772171313154"></a><a name="p16772171313154"></a>Specifies the ratio of the available network bandwidth to the network hardware bandwidth of the ECS.</p>
<p id="p3711880173425"><a name="p3711880173425"></a><a name="p3711880173425"></a>This parameter has not been used. Its default value is <strong id="b84235270611135_4"><a name="b84235270611135_4"></a><a name="b84235270611135_4"></a>1.0</strong>.</p>
</td>
</tr>
<tr id="row51313205"><td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.2.4.1.1 "><p id="p62728917"><a name="p62728917"></a><a name="p62728917"></a>os-flavor-access:is_public</p>
</td>
<td class="cellrowborder" valign="top" width="16.38%" headers="mcps1.2.4.1.2 "><p id="p43117912173145"><a name="p43117912173145"></a><a name="p43117912173145"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="66.51%" headers="mcps1.2.4.1.3 "><p id="p8894218182818"><a name="p8894218182818"></a><a name="p8894218182818"></a>Specifies whether a flavor is available to all tenants. This is an extended attribute.</p>
<a name="ul1474014143815"></a><a name="ul1474014143815"></a><ul id="ul1474014143815"><li><strong id="b84235270620200"><a name="b84235270620200"></a><a name="b84235270620200"></a>true</strong>: indicates that a flavor is available to all tenants.</li><li><strong id="b84235270620200_1"><a name="b84235270620200_1"></a><a name="b84235270620200_1"></a>false</strong>: indicates that a flavor is available only to certain tenants.</li></ul>
<p id="p35038271466"><a name="p35038271466"></a><a name="p35038271466"></a>Default value: <strong id="b842352706115252"><a name="b842352706115252"></a><a name="b842352706115252"></a>true</strong></p>
</td>
</tr>
<tr id="row2047803919452"><td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.2.4.1.1 "><p id="p6509154919455"><a name="p6509154919455"></a><a name="p6509154919455"></a>links</p>
</td>
<td class="cellrowborder" valign="top" width="16.38%" headers="mcps1.2.4.1.2 "><p id="p3792414219455"><a name="p3792414219455"></a><a name="p3792414219455"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="66.51%" headers="mcps1.2.4.1.3 "><p id="p6495712119455"><a name="p6495712119455"></a><a name="p6495712119455"></a>Specifies shortcut links for ECS flavors. For details, see <a href="#table15913898194628">Table 5</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **links**  field description

<a name="table15913898194628"></a>
<table><thead align="left"><tr id="row37608132194628"><th class="cellrowborder" valign="top" width="17.23%" id="mcps1.2.4.1.1"><p id="p7144115819116"><a name="p7144115819116"></a><a name="p7144115819116"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.11%" id="mcps1.2.4.1.2"><p id="p19144558313"><a name="p19144558313"></a><a name="p19144558313"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="66.66%" id="mcps1.2.4.1.3"><p id="p14144358114"><a name="p14144358114"></a><a name="p14144358114"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row17692319194628"><td class="cellrowborder" valign="top" width="17.23%" headers="mcps1.2.4.1.1 "><p id="p23791739194628"><a name="p23791739194628"></a><a name="p23791739194628"></a>rel</p>
</td>
<td class="cellrowborder" valign="top" width="16.11%" headers="mcps1.2.4.1.2 "><p id="p48082703194628"><a name="p48082703194628"></a><a name="p48082703194628"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="66.66%" headers="mcps1.2.4.1.3 "><p id="p2384900194628"><a name="p2384900194628"></a><a name="p2384900194628"></a>Specifies the shortcut link marker name.</p>
</td>
</tr>
<tr id="row21464106194628"><td class="cellrowborder" valign="top" width="17.23%" headers="mcps1.2.4.1.1 "><p id="p60871059194628"><a name="p60871059194628"></a><a name="p60871059194628"></a>href</p>
</td>
<td class="cellrowborder" valign="top" width="16.11%" headers="mcps1.2.4.1.2 "><p id="p31608752194628"><a name="p31608752194628"></a><a name="p31608752194628"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="66.66%" headers="mcps1.2.4.1.3 "><p id="p10172138194628"><a name="p10172138194628"></a><a name="p10172138194628"></a>Provides the corresponding shortcut link.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="section1063811378466"></a>

```
GET https://{endpoint}/v2/743b4c0428d94531b9f2add666642e6b/flavors/detail
GET https://{endpoint}/v2.1/743b4c0428d94531b9f2add666642e6b/flavors/detail
```

## Example Response<a name="section10861115013317"></a>

```
{
    "flavors": [
        {
            "name": "c3.2xlarge.2",
            "links": [
                {
                    "href": "https://compute.region.xxx.com/v2.1/743b4c0428d94531b9f2add666642e6b/flavors/c3.2xlarge.2",
                    "rel": "self"
                },
                {
                    "href": "https://compute.region.xxx.com/743b4c0428d94531b9f2add666642e6b/flavors/c3.2xlarge.2",
                    "rel": "bookmark"
                }
            ],
            "ram": 16384,
            "OS-FLV-DISABLED:disabled": false,
            "vcpus": 8,
            "swap": "",
            "os-flavor-access:is_public": true,
            "rxtx_factor": 1,
            "OS-FLV-EXT-DATA:ephemeral": 0,
            "disk": 0,
            "id": "c3.2xlarge.2"
        },
        {
            "name": "c3.2xlarge.4",
            "links": [
                {
                    "href": "https://compute.region.xxx.com/v2.1/743b4c0428d94531b9f2add666642e6b/flavors/c3.2xlarge.4",
                    "rel": "self"
                },
                {
                    "href": "https://compute.region.xxx.com/743b4c0428d94531b9f2add666642e6b/flavors/c3.2xlarge.4",
                    "rel": "bookmark"
                }
            ],
            "ram": 32768,
            "OS-FLV-DISABLED:disabled": false,
            "vcpus": 8,
            "swap": "",
            "os-flavor-access:is_public": true,
            "rxtx_factor": 1,
            "OS-FLV-EXT-DATA:ephemeral": 0,
            "disk": 0,
            "id": "c3.2xlarge.4"
        }
    ]
                }
```

## Returned Values<a name="section63081244"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

