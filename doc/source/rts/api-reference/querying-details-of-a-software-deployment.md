# Querying Details of a Software Deployment<a name="EN-US_TOPIC_0085277560"></a>

## Function<a name="en-us_topic_0085081137_section5314816"></a>

This API is used to query details of a software deployment.

## URI<a name="en-us_topic_0085081137_section47833347"></a>

GET /v1/\{project\_id\}/software\_deployments/\{deployment\_id\}

For details about the parameters, see  [Table 1](#table1759528275).

**Table  1**  Parameter description

<a name="table1759528275"></a>
<table><thead align="left"><tr id="row26011272716"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p17762534144716"><a name="p17762534144716"></a><a name="p17762534144716"></a><strong id="b148911851154417"><a name="b148911851154417"></a><a name="b148911851154417"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p376433420478"><a name="p376433420478"></a><a name="p376433420478"></a><strong id="b3241653144417"><a name="b3241653144417"></a><a name="b3241653144417"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p15766123474714"><a name="p15766123474714"></a><a name="p15766123474714"></a><strong id="b923495494418"><a name="b923495494418"></a><a name="b923495494418"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p147683349474"><a name="p147683349474"></a><a name="p147683349474"></a><strong id="b15169855134415"><a name="b15169855134415"></a><a name="b15169855134415"></a>Description</strong></p>
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
<tr id="row205605355223"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1874564042214"><a name="p1874564042214"></a><a name="p1874564042214"></a>deployment_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p17747124020225"><a name="p17747124020225"></a><a name="p17747124020225"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p157491540122216"><a name="p157491540122216"></a><a name="p157491540122216"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p197517404224"><a name="p197517404224"></a><a name="p197517404224"></a>Specifies the software deployment UUID.</p>
</td>
</tr>
</tbody>
</table>

## Request Parameter<a name="en-us_topic_0085081137_section27846943"></a>

N/A

## Response Parameter<a name="en-us_topic_0085081137_section49295902"></a>

<a name="table78931944326"></a>
<table><thead align="left"><tr id="row158936453217"><th class="cellrowborder" valign="top" width="18.6%" id="mcps1.1.5.1.1"><p id="p13701251185014"><a name="p13701251185014"></a><a name="p13701251185014"></a><strong id="b186129221451"><a name="b186129221451"></a><a name="b186129221451"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.120000000000001%" id="mcps1.1.5.1.2"><p id="p13704145119507"><a name="p13704145119507"></a><a name="p13704145119507"></a><strong id="b13788623114516"><a name="b13788623114516"></a><a name="b13788623114516"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.120000000000001%" id="mcps1.1.5.1.3"><p id="p3705151185017"><a name="p3705151185017"></a><a name="p3705151185017"></a><strong id="b410842594515"><a name="b410842594515"></a><a name="b410842594515"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51.160000000000004%" id="mcps1.1.5.1.4"><p id="p1371214511507"><a name="p1371214511507"></a><a name="p1371214511507"></a><strong id="b14591267452"><a name="b14591267452"></a><a name="b14591267452"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row18893847322"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="p1789310463210"><a name="p1789310463210"></a><a name="p1789310463210"></a>software_deployment</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.2 "><p id="p352864913122"><a name="p352864913122"></a><a name="p352864913122"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.3 "><p id="p1289317417323"><a name="p1289317417323"></a><a name="p1289317417323"></a>List &lt;dict&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="51.160000000000004%" headers="mcps1.1.5.1.4 "><p id="p88941549323"><a name="p88941549323"></a><a name="p88941549323"></a>Specifies the software deployment objects.</p>
</td>
</tr>
</tbody>
</table>

**software\_deployment**  structure information

<a name="en-us_topic_0085081137_table58541283"></a>
<table><thead align="left"><tr id="en-us_topic_0085081137_row14014710"><th class="cellrowborder" valign="top" width="18.821882188218822%" id="mcps1.1.5.1.1"><p id="p3499759596"><a name="p3499759596"></a><a name="p3499759596"></a><strong id="b1586914178466"><a name="b1586914178466"></a><a name="b1586914178466"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.291529152915292%" id="mcps1.1.5.1.2"><p id="p1050010595917"><a name="p1050010595917"></a><a name="p1050010595917"></a><strong id="b82722074613"><a name="b82722074613"></a><a name="b82722074613"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.291529152915292%" id="mcps1.1.5.1.3"><p id="p105026513591"><a name="p105026513591"></a><a name="p105026513591"></a><strong id="b12216221124613"><a name="b12216221124613"></a><a name="b12216221124613"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50.5950595059506%" id="mcps1.1.5.1.4"><p id="p195054515597"><a name="p195054515597"></a><a name="p195054515597"></a><strong id="b315372274616"><a name="b315372274616"></a><a name="b315372274616"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0085081137_row20801079"><td class="cellrowborder" valign="top" width="18.821882188218822%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081137_p970153811317"><a name="en-us_topic_0085081137_p970153811317"></a><a name="en-us_topic_0085081137_p970153811317"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.2 "><p id="p1165152711816"><a name="p1165152711816"></a><a name="p1165152711816"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081137_p167118383136"><a name="en-us_topic_0085081137_p167118383136"></a><a name="en-us_topic_0085081137_p167118383136"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.5950595059506%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0085081137_p7718387138"><a name="en-us_topic_0085081137_p7718387138"></a><a name="en-us_topic_0085081137_p7718387138"></a>Specifies the stack action that triggers the software deployment.</p>
</td>
</tr>
<tr id="en-us_topic_0085081137_row20715858"><td class="cellrowborder" valign="top" width="18.821882188218822%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081137_p14711038141317"><a name="en-us_topic_0085081137_p14711038141317"></a><a name="en-us_topic_0085081137_p14711038141317"></a>config_id</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.2 "><p id="p10651327386"><a name="p10651327386"></a><a name="p10651327386"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081137_p2071238141312"><a name="en-us_topic_0085081137_p2071238141312"></a><a name="en-us_topic_0085081137_p2071238141312"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.5950595059506%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0085081137_p77111384136"><a name="en-us_topic_0085081137_p77111384136"></a><a name="en-us_topic_0085081137_p77111384136"></a>Specifies the ID of the software configuration running on a server.</p>
</td>
</tr>
<tr id="en-us_topic_0085081137_row26021030"><td class="cellrowborder" valign="top" width="18.821882188218822%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081137_p1971138131311"><a name="en-us_topic_0085081137_p1971138131311"></a><a name="en-us_topic_0085081137_p1971138131311"></a>creation_time</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.2 "><p id="p11651527181"><a name="p11651527181"></a><a name="p11651527181"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081137_p97112386131"><a name="en-us_topic_0085081137_p97112386131"></a><a name="en-us_topic_0085081137_p97112386131"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.5950595059506%" headers="mcps1.1.5.1.4 "><p id="p46091151173019"><a name="p46091151173019"></a><a name="p46091151173019"></a>Specifies the creation time. The timestamp uses the ISO 8601 format:</p>
<pre class="screen" id="screen152761357123016"><a name="screen152761357123016"></a><a name="screen152761357123016"></a>CCYY-MM-DDThh:mm:ss&plusmn;hh:mm</pre>
</td>
</tr>
<tr id="en-us_topic_0085081137_row45386595"><td class="cellrowborder" valign="top" width="18.821882188218822%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081137_p77143812131"><a name="en-us_topic_0085081137_p77143812131"></a><a name="en-us_topic_0085081137_p77143812131"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.2 "><p id="p56517271281"><a name="p56517271281"></a><a name="p56517271281"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081137_p1671938101313"><a name="en-us_topic_0085081137_p1671938101313"></a><a name="en-us_topic_0085081137_p1671938101313"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.5950595059506%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0085081137_p1371113816138"><a name="en-us_topic_0085081137_p1371113816138"></a><a name="en-us_topic_0085081137_p1371113816138"></a>Specifies the software deployment UUID.</p>
</td>
</tr>
<tr id="en-us_topic_0085081137_row23709572"><td class="cellrowborder" valign="top" width="18.821882188218822%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081137_p207113817136"><a name="en-us_topic_0085081137_p207113817136"></a><a name="en-us_topic_0085081137_p207113817136"></a>input_values</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.2 "><p id="p13654271382"><a name="p13654271382"></a><a name="p13654271382"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081137_p1671193818134"><a name="en-us_topic_0085081137_p1671193818134"></a><a name="en-us_topic_0085081137_p1671193818134"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="50.5950595059506%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0085081137_p147118380132"><a name="en-us_topic_0085081137_p147118380132"></a><a name="en-us_topic_0085081137_p147118380132"></a>Specifies input data stored in the form of a key-value pair.</p>
</td>
</tr>
<tr id="en-us_topic_0085081137_row1676488279"><td class="cellrowborder" valign="top" width="18.821882188218822%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081137_p37193817135"><a name="en-us_topic_0085081137_p37193817135"></a><a name="en-us_topic_0085081137_p37193817135"></a>output_values</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.2 "><p id="p8651427080"><a name="p8651427080"></a><a name="p8651427080"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081137_p47115382137"><a name="en-us_topic_0085081137_p47115382137"></a><a name="en-us_topic_0085081137_p47115382137"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="50.5950595059506%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0085081137_p671153819133"><a name="en-us_topic_0085081137_p671153819133"></a><a name="en-us_topic_0085081137_p671153819133"></a>Specifies output data stored in the form of a key-value pair.</p>
</td>
</tr>
<tr id="en-us_topic_0085081137_row876414818717"><td class="cellrowborder" valign="top" width="18.821882188218822%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081137_p20716383130"><a name="en-us_topic_0085081137_p20716383130"></a><a name="en-us_topic_0085081137_p20716383130"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.2 "><p id="p146542716812"><a name="p146542716812"></a><a name="p146542716812"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081137_p1971173813133"><a name="en-us_topic_0085081137_p1971173813133"></a><a name="en-us_topic_0085081137_p1971173813133"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.5950595059506%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0085081137_p137115382136"><a name="en-us_topic_0085081137_p137115382136"></a><a name="en-us_topic_0085081137_p137115382136"></a>Specifies the server ID.</p>
</td>
</tr>
<tr id="en-us_topic_0085081137_row576428579"><td class="cellrowborder" valign="top" width="18.821882188218822%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081137_p11728383139"><a name="en-us_topic_0085081137_p11728383139"></a><a name="en-us_topic_0085081137_p11728383139"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.2 "><p id="p46510271782"><a name="p46510271782"></a><a name="p46510271782"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081137_p117293816130"><a name="en-us_topic_0085081137_p117293816130"></a><a name="en-us_topic_0085081137_p117293816130"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.5950595059506%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0085081137_p1672163851310"><a name="en-us_topic_0085081137_p1672163851310"></a><a name="en-us_topic_0085081137_p1672163851310"></a>Specifies the current status of software deployments. Valid values include <strong id="b199125715557"><a name="b199125715557"></a><a name="b199125715557"></a>COMPLETE</strong>, <strong id="b1391219716557"><a name="b1391219716557"></a><a name="b1391219716557"></a>IN_PROGRESS</strong>, and <strong id="b89131373553"><a name="b89131373553"></a><a name="b89131373553"></a>FAILED</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0085081137_row17648812714"><td class="cellrowborder" valign="top" width="18.821882188218822%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081137_p11724384138"><a name="en-us_topic_0085081137_p11724384138"></a><a name="en-us_topic_0085081137_p11724384138"></a>status_reason</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.2 "><p id="p16651327689"><a name="p16651327689"></a><a name="p16651327689"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081137_p1272133815132"><a name="en-us_topic_0085081137_p1272133815132"></a><a name="en-us_topic_0085081137_p1272133815132"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.5950595059506%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0085081137_p172938101310"><a name="en-us_topic_0085081137_p172938101310"></a><a name="en-us_topic_0085081137_p172938101310"></a>Specifies the cause of the software deployment status.</p>
</td>
</tr>
<tr id="en-us_topic_0085081137_row196812121172"><td class="cellrowborder" valign="top" width="18.821882188218822%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081137_p17217383134"><a name="en-us_topic_0085081137_p17217383134"></a><a name="en-us_topic_0085081137_p17217383134"></a>updated_time</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.2 "><p id="p2658271381"><a name="p2658271381"></a><a name="p2658271381"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081137_p772143861317"><a name="en-us_topic_0085081137_p772143861317"></a><a name="en-us_topic_0085081137_p772143861317"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.5950595059506%" headers="mcps1.1.5.1.4 "><p id="p1433450143111"><a name="p1433450143111"></a><a name="p1433450143111"></a>Specifies the update time. The timestamp uses the ISO 8601 format:</p>
<pre class="screen" id="screen3724154153114"><a name="screen3724154153114"></a><a name="screen3724154153114"></a>CCYY-MM-DDThh:mm:ss&plusmn;hh:mm</pre>
</td>
</tr>
</tbody>
</table>

## Request Example<a name="en-us_topic_0085081137_section41009935"></a>

```
GET /v1/95d02433133a4c0a87ba6967474a2ad3/software_deployments/3d5ec2a8-7004-43b6-a7f6-542bdbe9d434
```

## Response Example<a name="en-us_topic_0085081137_section33545101"></a>

```
{
    "software_deployment": {
        "action": "CREATE",
        "config_id": "619d6e53-e14b-497f-8852-9c2671b07d79",
        "creation_time": "2018-05-15T08:48:23.500895",
        "id": "bb51252e-3e80-4be9-8c06-c52a88e87ec8",
        "input_values": {},
        "output_values": null,
        "server_id": "ca839c6d-c038-46b6-b0b8-8ce78e715639",
        "status": "IN_PROGRESS",
        "status_reason": "Deploy data available"
    }
}
```

## Return Code<a name="en-us_topic_0085081137_section33470456"></a>

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

<a name="table3304326164315"></a>
<table><thead align="left"><tr id="en-us_topic_0084581290_row16955110342"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="en-us_topic_0084581290_p129561510144"><a name="en-us_topic_0084581290_p129561510144"></a><a name="en-us_topic_0084581290_p129561510144"></a><strong id="en-us_topic_0084581290_b1552942884813"><a name="en-us_topic_0084581290_b1552942884813"></a><a name="en-us_topic_0084581290_b1552942884813"></a>Return Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.2"><p id="en-us_topic_0084581290_p4959810444"><a name="en-us_topic_0084581290_p4959810444"></a><a name="en-us_topic_0084581290_p4959810444"></a><strong id="en-us_topic_0084581290_b956007905"><a name="en-us_topic_0084581290_b956007905"></a><a name="en-us_topic_0084581290_b956007905"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.3"><p id="en-us_topic_0084581290_p9959161020418"><a name="en-us_topic_0084581290_p9959161020418"></a><a name="en-us_topic_0084581290_p9959161020418"></a><strong id="en-us_topic_0084581290_b359171417"><a name="en-us_topic_0084581290_b359171417"></a><a name="en-us_topic_0084581290_b359171417"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0084581290_row179609103411"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0084581290_p896118101840"><a name="en-us_topic_0084581290_p896118101840"></a><a name="en-us_topic_0084581290_p896118101840"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0084581290_p1296211015416"><a name="en-us_topic_0084581290_p1296211015416"></a><a name="en-us_topic_0084581290_p1296211015416"></a>Bad Request</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0084581290_p9963110146"><a name="en-us_topic_0084581290_p9963110146"></a><a name="en-us_topic_0084581290_p9963110146"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="en-us_topic_0084581290_row181330274199"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0084581290_p18134027201912"><a name="en-us_topic_0084581290_p18134027201912"></a><a name="en-us_topic_0084581290_p18134027201912"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0084581290_p1713419274191"><a name="en-us_topic_0084581290_p1713419274191"></a><a name="en-us_topic_0084581290_p1713419274191"></a>Unauthorized</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0084581290_p11134162718196"><a name="en-us_topic_0084581290_p11134162718196"></a><a name="en-us_topic_0084581290_p11134162718196"></a>Authorization failed.</p>
</td>
</tr>
<tr id="en-us_topic_0084581290_row16531631121913"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0084581290_en-us_topic_0057973122_p5338333194217"><a name="en-us_topic_0084581290_en-us_topic_0057973122_p5338333194217"></a><a name="en-us_topic_0084581290_en-us_topic_0057973122_p5338333194217"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0084581290_p125520290312"><a name="en-us_topic_0084581290_p125520290312"></a><a name="en-us_topic_0084581290_p125520290312"></a>Not found</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0084581290_en-us_topic_0057973122_p29751790194217"><a name="en-us_topic_0084581290_en-us_topic_0057973122_p29751790194217"></a><a name="en-us_topic_0084581290_en-us_topic_0057973122_p29751790194217"></a>The requested resources are not found.</p>
</td>
</tr>
<tr id="en-us_topic_0084581290_row196097477276"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0084581290_p19789174972712"><a name="en-us_topic_0084581290_p19789174972712"></a><a name="en-us_topic_0084581290_p19789174972712"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0084581290_p779364918272"><a name="en-us_topic_0084581290_p779364918272"></a><a name="en-us_topic_0084581290_p779364918272"></a>Internal Server Error</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0084581290_p196546319198"><a name="en-us_topic_0084581290_p196546319198"></a><a name="en-us_topic_0084581290_p196546319198"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
</tbody>
</table>

