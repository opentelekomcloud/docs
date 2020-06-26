# Creating One or More Software Configurations<a name="EN-US_TOPIC_0084581316"></a>

## Function<a name="en-us_topic_0057973155_section39327087"></a>

This API is used to create one or more software configurations.

## URI<a name="en-us_topic_0057973155_section18399466"></a>

POST /v1/\{project\_id\}/software\_configs

For details about the parameters, see  [Table 1](#table1759528275).

**Table  1**  Parameter description

<a name="table1759528275"></a>
<table><thead align="left"><tr id="row26011272716"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p17762534144716"><a name="p17762534144716"></a><a name="p17762534144716"></a><strong id="b6928202019284"><a name="b6928202019284"></a><a name="b6928202019284"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p376433420478"><a name="p376433420478"></a><a name="p376433420478"></a><strong id="b5926172118288"><a name="b5926172118288"></a><a name="b5926172118288"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p15766123474714"><a name="p15766123474714"></a><a name="p15766123474714"></a><strong id="b12908152211283"><a name="b12908152211283"></a><a name="b12908152211283"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p147683349474"><a name="p147683349474"></a><a name="p147683349474"></a><strong id="b15816152382815"><a name="b15816152382815"></a><a name="b15816152382815"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row10601725277"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1765464961019"><a name="p1765464961019"></a><a name="p1765464961019"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p0655184916104"><a name="p0655184916104"></a><a name="p0655184916104"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p865694971017"><a name="p865694971017"></a><a name="p865694971017"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p13658144921010"><a name="p13658144921010"></a><a name="p13658144921010"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Parameter<a name="en-us_topic_0057973155_section31377468"></a>

<a name="en-us_topic_0057973155_table65929779113135"></a>
<table><thead align="left"><tr id="en-us_topic_0057973155_row4303892113135"><th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.1.6.1.1"><p id="p13701251185014"><a name="p13701251185014"></a><a name="p13701251185014"></a><strong id="b1230411296284"><a name="b1230411296284"></a><a name="b1230411296284"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.1.6.1.2"><p id="p13704145119507"><a name="p13704145119507"></a><a name="p13704145119507"></a><strong id="b10409203319282"><a name="b10409203319282"></a><a name="b10409203319282"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.1.6.1.3"><p id="p3705151185017"><a name="p3705151185017"></a><a name="p3705151185017"></a><strong id="b13403234192818"><a name="b13403234192818"></a><a name="b13403234192818"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.1.6.1.4"><p id="p18709155145010"><a name="p18709155145010"></a><a name="p18709155145010"></a><strong id="b750218355280"><a name="b750218355280"></a><a name="b750218355280"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="41.584158415841586%" id="mcps1.1.6.1.5"><p id="p1371214511507"><a name="p1371214511507"></a><a name="p1371214511507"></a><strong id="b84961636152812"><a name="b84961636152812"></a><a name="b84961636152812"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row15808195064410"><td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0057973155_p329864113144"><a name="en-us_topic_0057973155_p329864113144"></a><a name="en-us_topic_0057973155_p329864113144"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.1.6.1.2 "><p id="p1033162910431"><a name="p1033162910431"></a><a name="p1033162910431"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0057973155_p26719017113144"><a name="en-us_topic_0057973155_p26719017113144"></a><a name="en-us_topic_0057973155_p26719017113144"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0057973155_p16756734113144"><a name="en-us_topic_0057973155_p16756734113144"></a><a name="en-us_topic_0057973155_p16756734113144"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="41.584158415841586%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0057973155_p15118191113144"><a name="en-us_topic_0057973155_p15118191113144"></a><a name="en-us_topic_0057973155_p15118191113144"></a>Specifies the name of the software configuration.</p>
</td>
</tr>
<tr id="en-us_topic_0057973155_row41540504113135"><td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0057973155_p61868181113144"><a name="en-us_topic_0057973155_p61868181113144"></a><a name="en-us_topic_0057973155_p61868181113144"></a>config</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.1.6.1.2 "><p id="p6333294432"><a name="p6333294432"></a><a name="p6333294432"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0057973155_p45266725113144"><a name="en-us_topic_0057973155_p45266725113144"></a><a name="en-us_topic_0057973155_p45266725113144"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0057973155_p42726081113144"><a name="en-us_topic_0057973155_p42726081113144"></a><a name="en-us_topic_0057973155_p42726081113144"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="41.584158415841586%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0057973155_p38260562113144"><a name="en-us_topic_0057973155_p38260562113144"></a><a name="en-us_topic_0057973155_p38260562113144"></a>Specifies the script used for defining the configuration.</p>
</td>
</tr>
<tr id="en-us_topic_0057973155_row24454548113135"><td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0057973155_p41771845113144"><a name="en-us_topic_0057973155_p41771845113144"></a><a name="en-us_topic_0057973155_p41771845113144"></a>group</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.1.6.1.2 "><p id="p1339291437"><a name="p1339291437"></a><a name="p1339291437"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0057973155_p28076297113144"><a name="en-us_topic_0057973155_p28076297113144"></a><a name="en-us_topic_0057973155_p28076297113144"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0057973155_p59587548113144"><a name="en-us_topic_0057973155_p59587548113144"></a><a name="en-us_topic_0057973155_p59587548113144"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="41.584158415841586%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0057973155_p61862121113144"><a name="en-us_topic_0057973155_p61862121113144"></a><a name="en-us_topic_0057973155_p61862121113144"></a>Specifies the name of the software configuration group.</p>
</td>
</tr>
<tr id="en-us_topic_0057973155_row38792844113135"><td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0057973155_p15308182113144"><a name="en-us_topic_0057973155_p15308182113144"></a><a name="en-us_topic_0057973155_p15308182113144"></a>inputs</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.1.6.1.2 "><p id="p1333142934318"><a name="p1333142934318"></a><a name="p1333142934318"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0057973155_p32003214113144"><a name="en-us_topic_0057973155_p32003214113144"></a><a name="en-us_topic_0057973155_p32003214113144"></a>List &lt;dict&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0057973155_p42123518113144"><a name="en-us_topic_0057973155_p42123518113144"></a><a name="en-us_topic_0057973155_p42123518113144"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="41.584158415841586%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0057973155_p56561807113144"><a name="en-us_topic_0057973155_p56561807113144"></a><a name="en-us_topic_0057973155_p56561807113144"></a>Specifies the software configuration input.</p>
</td>
</tr>
<tr id="en-us_topic_0057973155_row65450611113135"><td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0057973155_p28715184113144"><a name="en-us_topic_0057973155_p28715184113144"></a><a name="en-us_topic_0057973155_p28715184113144"></a>outputs</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.1.6.1.2 "><p id="p173312944313"><a name="p173312944313"></a><a name="p173312944313"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0057973155_p44228553113144"><a name="en-us_topic_0057973155_p44228553113144"></a><a name="en-us_topic_0057973155_p44228553113144"></a>List &lt;dict&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0057973155_p25743039113144"><a name="en-us_topic_0057973155_p25743039113144"></a><a name="en-us_topic_0057973155_p25743039113144"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="41.584158415841586%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0057973155_p4811385113144"><a name="en-us_topic_0057973155_p4811385113144"></a><a name="en-us_topic_0057973155_p4811385113144"></a>Specifies the software configuration output.</p>
</td>
</tr>
<tr id="en-us_topic_0057973155_row25758153113135"><td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0057973155_p17838943113144"><a name="en-us_topic_0057973155_p17838943113144"></a><a name="en-us_topic_0057973155_p17838943113144"></a>options</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.1.6.1.2 "><p id="p0337295430"><a name="p0337295430"></a><a name="p0337295430"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0057973155_p35668275113144"><a name="en-us_topic_0057973155_p35668275113144"></a><a name="en-us_topic_0057973155_p35668275113144"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0057973155_p3449192113144"><a name="en-us_topic_0057973155_p3449192113144"></a><a name="en-us_topic_0057973155_p3449192113144"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="41.584158415841586%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0057973155_p10949158113144"><a name="en-us_topic_0057973155_p10949158113144"></a><a name="en-us_topic_0057973155_p10949158113144"></a>Specifies options used by a software configuration management tool.</p>
</td>
</tr>
</tbody>
</table>

## Response Parameter<a name="en-us_topic_0057973155_section13961758"></a>

<a name="table534093217106"></a>
<table><thead align="left"><tr id="row19342113221011"><th class="cellrowborder" valign="top" width="16.470000000000002%" id="mcps1.1.5.1.1"><p id="p10524141715571"><a name="p10524141715571"></a><a name="p10524141715571"></a><strong id="b09061987291"><a name="b09061987291"></a><a name="b09061987291"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.470000000000002%" id="mcps1.1.5.1.2"><p id="p13528131714576"><a name="p13528131714576"></a><a name="p13528131714576"></a><strong id="b496510912296"><a name="b496510912296"></a><a name="b496510912296"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.65%" id="mcps1.1.5.1.3"><p id="p8531141795714"><a name="p8531141795714"></a><a name="p8531141795714"></a><strong id="b0993210202918"><a name="b0993210202918"></a><a name="b0993210202918"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="49.41%" id="mcps1.1.5.1.4"><p id="p4535181705714"><a name="p4535181705714"></a><a name="p4535181705714"></a><strong id="b2964711152913"><a name="b2964711152913"></a><a name="b2964711152913"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row334213329108"><td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.1 "><p id="p12342732111015"><a name="p12342732111015"></a><a name="p12342732111015"></a>software_config</p>
</td>
<td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.2 "><p id="p154421347134514"><a name="p154421347134514"></a><a name="p154421347134514"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.65%" headers="mcps1.1.5.1.3 "><p id="p123421332141018"><a name="p123421332141018"></a><a name="p123421332141018"></a>Dict</p>
</td>
<td class="cellrowborder" valign="top" width="49.41%" headers="mcps1.1.5.1.4 "><p id="p0342183218106"><a name="p0342183218106"></a><a name="p0342183218106"></a>Specifies the software configuration information.</p>
</td>
</tr>
</tbody>
</table>

**software\_config**  structure information

<a name="en-us_topic_0057973155_table66276559"></a>
<table><thead align="left"><tr id="en-us_topic_0057973155_row11349229"><th class="cellrowborder" valign="top" width="16.470000000000002%" id="mcps1.1.5.1.1"><p id="p16504720125711"><a name="p16504720125711"></a><a name="p16504720125711"></a><strong id="b66260425294"><a name="b66260425294"></a><a name="b66260425294"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.470000000000002%" id="mcps1.1.5.1.2"><p id="p17508192095710"><a name="p17508192095710"></a><a name="p17508192095710"></a><strong id="b23351463301"><a name="b23351463301"></a><a name="b23351463301"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.65%" id="mcps1.1.5.1.3"><p id="p16512220165714"><a name="p16512220165714"></a><a name="p16512220165714"></a><strong id="b668414143011"><a name="b668414143011"></a><a name="b668414143011"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="49.41%" id="mcps1.1.5.1.4"><p id="p175201820165714"><a name="p175201820165714"></a><a name="p175201820165714"></a><strong id="b128601911203013"><a name="b128601911203013"></a><a name="b128601911203013"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973155_row12495801"><td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973155_p5526924"><a name="en-us_topic_0057973155_p5526924"></a><a name="en-us_topic_0057973155_p5526924"></a>inputs</p>
</td>
<td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.2 "><p id="p16884141154310"><a name="p16884141154310"></a><a name="p16884141154310"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.65%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973155_p45027737"><a name="en-us_topic_0057973155_p45027737"></a><a name="en-us_topic_0057973155_p45027737"></a>List &lt;dict&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="49.41%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973155_p13765499"><a name="en-us_topic_0057973155_p13765499"></a><a name="en-us_topic_0057973155_p13765499"></a>Specifies the software configuration input.</p>
</td>
</tr>
<tr id="en-us_topic_0057973155_row56780633"><td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973155_p35828526"><a name="en-us_topic_0057973155_p35828526"></a><a name="en-us_topic_0057973155_p35828526"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.2 "><p id="p488412412433"><a name="p488412412433"></a><a name="p488412412433"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.65%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973155_p16429471"><a name="en-us_topic_0057973155_p16429471"></a><a name="en-us_topic_0057973155_p16429471"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.41%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973155_p16929400"><a name="en-us_topic_0057973155_p16929400"></a><a name="en-us_topic_0057973155_p16929400"></a>Specifies the name of the software configuration.</p>
</td>
</tr>
<tr id="en-us_topic_0057973155_row18146878"><td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973155_p60610990"><a name="en-us_topic_0057973155_p60610990"></a><a name="en-us_topic_0057973155_p60610990"></a>outputs</p>
</td>
<td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.2 "><p id="p16884741124310"><a name="p16884741124310"></a><a name="p16884741124310"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.65%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973155_p10543167"><a name="en-us_topic_0057973155_p10543167"></a><a name="en-us_topic_0057973155_p10543167"></a>List &lt;dict&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="49.41%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973155_p51592162"><a name="en-us_topic_0057973155_p51592162"></a><a name="en-us_topic_0057973155_p51592162"></a>Specifies the software configuration output.</p>
</td>
</tr>
<tr id="en-us_topic_0057973155_row61676281"><td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973155_p29722863"><a name="en-us_topic_0057973155_p29722863"></a><a name="en-us_topic_0057973155_p29722863"></a>creation_time</p>
</td>
<td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.2 "><p id="p13884184104320"><a name="p13884184104320"></a><a name="p13884184104320"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.65%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973155_p58741673"><a name="en-us_topic_0057973155_p58741673"></a><a name="en-us_topic_0057973155_p58741673"></a>Date Time</p>
</td>
<td class="cellrowborder" valign="top" width="49.41%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973155_p65021323"><a name="en-us_topic_0057973155_p65021323"></a><a name="en-us_topic_0057973155_p65021323"></a>Specifies the time when the configuration was created.</p>
</td>
</tr>
<tr id="en-us_topic_0057973155_row48320995"><td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973155_p21686552"><a name="en-us_topic_0057973155_p21686552"></a><a name="en-us_topic_0057973155_p21686552"></a>group</p>
</td>
<td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.2 "><p id="p17884154115433"><a name="p17884154115433"></a><a name="p17884154115433"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.65%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973155_p11780310"><a name="en-us_topic_0057973155_p11780310"></a><a name="en-us_topic_0057973155_p11780310"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.41%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973155_p48312586"><a name="en-us_topic_0057973155_p48312586"></a><a name="en-us_topic_0057973155_p48312586"></a>Specifies the name of the software configuration group.</p>
</td>
</tr>
<tr id="en-us_topic_0057973155_row32160094"><td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973155_p54830812"><a name="en-us_topic_0057973155_p54830812"></a><a name="en-us_topic_0057973155_p54830812"></a>config</p>
</td>
<td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.2 "><p id="p88841341204318"><a name="p88841341204318"></a><a name="p88841341204318"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.65%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973155_p12110791"><a name="en-us_topic_0057973155_p12110791"></a><a name="en-us_topic_0057973155_p12110791"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.41%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973155_p2006018"><a name="en-us_topic_0057973155_p2006018"></a><a name="en-us_topic_0057973155_p2006018"></a>Specifies the software configuration code.</p>
</td>
</tr>
<tr id="en-us_topic_0057973155_row18054162"><td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973155_p53100979"><a name="en-us_topic_0057973155_p53100979"></a><a name="en-us_topic_0057973155_p53100979"></a>options</p>
</td>
<td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.2 "><p id="p688454116436"><a name="p688454116436"></a><a name="p688454116436"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.65%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973155_p6212037"><a name="en-us_topic_0057973155_p6212037"></a><a name="en-us_topic_0057973155_p6212037"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.41%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973155_p22096474"><a name="en-us_topic_0057973155_p22096474"></a><a name="en-us_topic_0057973155_p22096474"></a>Specifies the software configuration options.</p>
</td>
</tr>
<tr id="row137462219123"><td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.1 "><p id="p177414227124"><a name="p177414227124"></a><a name="p177414227124"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.2 "><p id="p6884174174320"><a name="p6884174174320"></a><a name="p6884174174320"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.65%" headers="mcps1.1.5.1.3 "><p id="p18741222131217"><a name="p18741222131217"></a><a name="p18741222131217"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.41%" headers="mcps1.1.5.1.4 "><p id="p17741222151220"><a name="p17741222151220"></a><a name="p17741222151220"></a>Specifies the software configuration UUID.</p>
</td>
</tr>
</tbody>
</table>

## Request Example<a name="en-us_topic_0057973155_section58546961"></a>

```
POST /v1/95d02433133a4c0a87ba6967474a2ad3/software_configs
{
    "inputs": [
        {
            "default": null,
            "type": "String",
            "name": "foo",
            "description": null
        },
        {
            "default": null,
            "type": "String",
            "name": "bar",
            "description": null
        }
    ],
    "group": "script",
    "name": "a-config-we5zpvyu7b5o",
    "outputs": [
        {
            "type": "String",
            "name": "result",
            "error_output": false,
            "description": null
        }
    ],
    "config": "#!/bin/sh -x\necho \"Writing to /tmp/$bar\"\necho $foo > /tmp/$bar\necho -n \"The file /tmp/$bar contains `cat /tmp/$bar` for server $deploy_server_id during $deploy_action\" > $heat_outputs_path.result\necho \"Written to /tmp/$bar\"\necho \"Output to stderr\" 1>&2",
    "options": null
}
```

## Response Example<a name="en-us_topic_0057973155_section57160607"></a>

```
{
    "software_config": {
        "creation_time": "2015-01-31T15:12:36Z",
        "inputs": [
            {
                "default": null,
                "type": "String",
                "name": "foo",
                "description": null
            },
            {
                "default": null,
                "type": "String",
                "name": "bar",
                "description": null
            }
        ],
        "group": "script",
        "name": "a-config-we5zpvyu7b5o",
        "outputs": [
            {
                "type": "String",
                "name": "result",
                "error_output": false,
                "description": null
            }
        ],
        "options": null,
        "config": "#!/bin/sh -x\necho \"Writing to /tmp/$bar\"\necho $foo > /tmp/$bar\necho -n \"The file /tmp/$bar contains `cat /tmp/$bar` for server $deploy_server_id during $deploy_action\" > $heat_outputs_path.result\necho \"Written to /tmp/$bar\"\necho \"Output to stderr\" 1>&2",
        "id": "ddee7aca-aa32-4335-8265-d436b20db4f1"
    }
}
```

## Return Code<a name="en-us_topic_0057973155_section44683415"></a>

**Table  2**  Normal return code

<a name="table01411862119"></a>
<table><thead align="left"><tr id="en-us_topic_0084581285_en-us_topic_0057973117_row42419326194057"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="en-us_topic_0084581285_en-us_topic_0057973117_p13413377194057"><a name="en-us_topic_0084581285_en-us_topic_0057973117_p13413377194057"></a><a name="en-us_topic_0084581285_en-us_topic_0057973117_p13413377194057"></a><strong id="en-us_topic_0084581285_b14910172512114"><a name="en-us_topic_0084581285_b14910172512114"></a><a name="en-us_topic_0084581285_b14910172512114"></a>Return Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.2"><p id="en-us_topic_0084581285_en-us_topic_0057973117_p12741761194057"><a name="en-us_topic_0084581285_en-us_topic_0057973117_p12741761194057"></a><a name="en-us_topic_0084581285_en-us_topic_0057973117_p12741761194057"></a><strong id="en-us_topic_0084581285_en-us_topic_0057973140_b84235270615814_1"><a name="en-us_topic_0084581285_en-us_topic_0057973140_b84235270615814_1"></a><a name="en-us_topic_0084581285_en-us_topic_0057973140_b84235270615814_1"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.3"><p id="en-us_topic_0084581285_en-us_topic_0057973117_p25449701194057"><a name="en-us_topic_0084581285_en-us_topic_0057973117_p25449701194057"></a><a name="en-us_topic_0084581285_en-us_topic_0057973117_p25449701194057"></a><strong id="en-us_topic_0084581285_en-us_topic_0057973140_b842352706193020"><a name="en-us_topic_0084581285_en-us_topic_0057973140_b842352706193020"></a><a name="en-us_topic_0084581285_en-us_topic_0057973140_b842352706193020"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0084581285_en-us_topic_0057973117_row48159894194057"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0084581285_en-us_topic_0057973117_p8637307194057"><a name="en-us_topic_0084581285_en-us_topic_0057973117_p8637307194057"></a><a name="en-us_topic_0084581285_en-us_topic_0057973117_p8637307194057"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0084581285_en-us_topic_0057973117_p28533244194057"><a name="en-us_topic_0084581285_en-us_topic_0057973117_p28533244194057"></a><a name="en-us_topic_0084581285_en-us_topic_0057973117_p28533244194057"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0084581285_en-us_topic_0057973117_p29491459194057"><a name="en-us_topic_0084581285_en-us_topic_0057973117_p29491459194057"></a><a name="en-us_topic_0084581285_en-us_topic_0057973117_p29491459194057"></a>Request was successful.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Error return code

<a name="table8571828153012"></a>
<table><thead align="left"><tr id="en-us_topic_0084581294_row16955110342"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="en-us_topic_0084581294_p129561510144"><a name="en-us_topic_0084581294_p129561510144"></a><a name="en-us_topic_0084581294_p129561510144"></a><strong id="en-us_topic_0084581294_b1235759101013"><a name="en-us_topic_0084581294_b1235759101013"></a><a name="en-us_topic_0084581294_b1235759101013"></a>Return Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.2"><p id="en-us_topic_0084581294_p4959810444"><a name="en-us_topic_0084581294_p4959810444"></a><a name="en-us_topic_0084581294_p4959810444"></a><strong id="en-us_topic_0084581294_en-us_topic_0057973140_b84235270615814_1"><a name="en-us_topic_0084581294_en-us_topic_0057973140_b84235270615814_1"></a><a name="en-us_topic_0084581294_en-us_topic_0057973140_b84235270615814_1"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.3"><p id="en-us_topic_0084581294_p9959161020418"><a name="en-us_topic_0084581294_p9959161020418"></a><a name="en-us_topic_0084581294_p9959161020418"></a><strong id="en-us_topic_0084581294_en-us_topic_0057973140_b842352706193020"><a name="en-us_topic_0084581294_en-us_topic_0057973140_b842352706193020"></a><a name="en-us_topic_0084581294_en-us_topic_0057973140_b842352706193020"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0084581294_row179609103411"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0084581294_p896118101840"><a name="en-us_topic_0084581294_p896118101840"></a><a name="en-us_topic_0084581294_p896118101840"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0084581294_p1296211015416"><a name="en-us_topic_0084581294_p1296211015416"></a><a name="en-us_topic_0084581294_p1296211015416"></a>Bad Request</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0084581294_p9963110146"><a name="en-us_topic_0084581294_p9963110146"></a><a name="en-us_topic_0084581294_p9963110146"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="en-us_topic_0084581294_row181330274199"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0084581294_p18134027201912"><a name="en-us_topic_0084581294_p18134027201912"></a><a name="en-us_topic_0084581294_p18134027201912"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0084581294_p1713419274191"><a name="en-us_topic_0084581294_p1713419274191"></a><a name="en-us_topic_0084581294_p1713419274191"></a>Unauthorized</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0084581294_p11134162718196"><a name="en-us_topic_0084581294_p11134162718196"></a><a name="en-us_topic_0084581294_p11134162718196"></a>Authorization failed.</p>
</td>
</tr>
<tr id="en-us_topic_0084581294_row16531631121913"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0084581294_en-us_topic_0057973122_p5338333194217"><a name="en-us_topic_0084581294_en-us_topic_0057973122_p5338333194217"></a><a name="en-us_topic_0084581294_en-us_topic_0057973122_p5338333194217"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0084581294_p125520290312"><a name="en-us_topic_0084581294_p125520290312"></a><a name="en-us_topic_0084581294_p125520290312"></a>Not found</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0084581294_en-us_topic_0057973122_p29751790194217"><a name="en-us_topic_0084581294_en-us_topic_0057973122_p29751790194217"></a><a name="en-us_topic_0084581294_en-us_topic_0057973122_p29751790194217"></a>The requested resources are not found.</p>
</td>
</tr>
</tbody>
</table>

