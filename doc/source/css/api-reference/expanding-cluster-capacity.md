# Expanding Cluster Capacity<a name="css_03_0025"></a>

## Function<a name="section874853215915"></a>

This API is used to add instances to a cluster.

## URI<a name="section8763193210910"></a>

```
POST /v1.0/{project_id}/clusters/{cluster_id}/extend 
```

**Table  1**  Parameter description

<a name="table57631032695"></a>
<table><thead align="left"><tr id="row4445336913"><th class="cellrowborder" valign="top" width="15.75%" id="mcps1.2.5.1.1"><p id="p54417338910"><a name="p54417338910"></a><a name="p54417338910"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="24.060000000000002%" id="mcps1.2.5.1.2"><p id="p1644733693"><a name="p1644733693"></a><a name="p1644733693"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="19.46%" id="mcps1.2.5.1.3"><p id="p11441233696"><a name="p11441233696"></a><a name="p11441233696"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="40.73%" id="mcps1.2.5.1.4"><p id="p124403319916"><a name="p124403319916"></a><a name="p124403319916"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row94414331098"><td class="cellrowborder" valign="top" width="15.75%" headers="mcps1.2.5.1.1 "><p id="p0441331398"><a name="p0441331398"></a><a name="p0441331398"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="24.060000000000002%" headers="mcps1.2.5.1.2 "><p id="p9444331997"><a name="p9444331997"></a><a name="p9444331997"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="19.46%" headers="mcps1.2.5.1.3 "><p id="p144412334919"><a name="p144412334919"></a><a name="p144412334919"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.73%" headers="mcps1.2.5.1.4 "><p id="p18449331896"><a name="p18449331896"></a><a name="p18449331896"></a>Project ID.</p>
</td>
</tr>
<tr id="row14453320917"><td class="cellrowborder" valign="top" width="15.75%" headers="mcps1.2.5.1.1 "><p id="p2044193314920"><a name="p2044193314920"></a><a name="p2044193314920"></a>cluster_id</p>
</td>
<td class="cellrowborder" valign="top" width="24.060000000000002%" headers="mcps1.2.5.1.2 "><p id="p24410331398"><a name="p24410331398"></a><a name="p24410331398"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="19.46%" headers="mcps1.2.5.1.3 "><p id="p844133316918"><a name="p844133316918"></a><a name="p844133316918"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.73%" headers="mcps1.2.5.1.4 "><p id="p13441833493"><a name="p13441833493"></a><a name="p13441833493"></a>ID of the cluster where instances are to be added.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section1477913211910"></a>

[Table 2](#table82481020121413)  describes the request parameters.

**Table  2**  Parameter description

<a name="table82481020121413"></a>
<table><thead align="left"><tr id="row18248112010149"><th class="cellrowborder" valign="top" width="19.2%" id="mcps1.2.5.1.1"><p id="p10441033494"><a name="p10441033494"></a><a name="p10441033494"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.08%" id="mcps1.2.5.1.2"><p id="p74493316910"><a name="p74493316910"></a><a name="p74493316910"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17.49%" id="mcps1.2.5.1.3"><p id="p1044533896"><a name="p1044533896"></a><a name="p1044533896"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="47.23%" id="mcps1.2.5.1.4"><p id="p154413335917"><a name="p154413335917"></a><a name="p154413335917"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row18248182013148"><td class="cellrowborder" valign="top" width="19.2%" headers="mcps1.2.5.1.1 "><p id="p11441933698"><a name="p11441933698"></a><a name="p11441933698"></a>grow</p>
</td>
<td class="cellrowborder" valign="top" width="16.08%" headers="mcps1.2.5.1.2 "><p id="p4441233891"><a name="p4441233891"></a><a name="p4441233891"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.2.5.1.3 "><p id="p1344203319917"><a name="p1344203319917"></a><a name="p1344203319917"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="47.23%" headers="mcps1.2.5.1.4 "><p id="p9448924192218"><a name="p9448924192218"></a><a name="p9448924192218"></a>Detailed description about the cluster capacity expansion request. For details, see <a href="#table198051725112115">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **grow**  field description

<a name="table198051725112115"></a>
<table><thead align="left"><tr id="row38051625132113"><th class="cellrowborder" valign="top" width="19.689999999999998%" id="mcps1.2.5.1.1"><p id="p14183513162314"><a name="p14183513162314"></a><a name="p14183513162314"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15.52%" id="mcps1.2.5.1.2"><p id="p14183813172311"><a name="p14183813172311"></a><a name="p14183813172311"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15.52%" id="mcps1.2.5.1.3"><p id="p12183151313234"><a name="p12183151313234"></a><a name="p12183151313234"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.27%" id="mcps1.2.5.1.4"><p id="p12183131319238"><a name="p12183131319238"></a><a name="p12183131319238"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1380519259210"><td class="cellrowborder" valign="top" width="19.689999999999998%" headers="mcps1.2.5.1.1 "><p id="p161839139239"><a name="p161839139239"></a><a name="p161839139239"></a>modifySize</p>
</td>
<td class="cellrowborder" valign="top" width="15.52%" headers="mcps1.2.5.1.2 "><p id="p121831413142310"><a name="p121831413142310"></a><a name="p121831413142310"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.52%" headers="mcps1.2.5.1.3 "><p id="p17183013172315"><a name="p17183013172315"></a><a name="p17183013172315"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="49.27%" headers="mcps1.2.5.1.4 "><p id="p318341317238"><a name="p318341317238"></a><a name="p318341317238"></a>Number of instances to be added.</p>
<div class="note" id="note17398115110518"><a name="note17398115110518"></a><a name="note17398115110518"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1639820519513"><a name="p1639820519513"></a><a name="p1639820519513"></a>The total number of existing instances and newly added instances in a cluster cannot exceed 32.</p>
</div></div>
</td>
</tr>
</tbody>
</table>

## Response<a name="section19810103220915"></a>

[Table 4](#table2282125191510)  describes the response parameters.

**Table  4**  Parameter description

<a name="table2282125191510"></a>
<table><thead align="left"><tr id="row16282195131515"><th class="cellrowborder" valign="top" width="23.13231323132313%" id="mcps1.2.4.1.1"><p id="p4446331696"><a name="p4446331696"></a><a name="p4446331696"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="30.213021302130212%" id="mcps1.2.4.1.2"><p id="p7440338917"><a name="p7440338917"></a><a name="p7440338917"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="46.65466546654666%" id="mcps1.2.4.1.3"><p id="p184453317918"><a name="p184453317918"></a><a name="p184453317918"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1728235121514"><td class="cellrowborder" valign="top" width="23.13231323132313%" headers="mcps1.2.4.1.1 "><p id="p204483311913"><a name="p204483311913"></a><a name="p204483311913"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="30.213021302130212%" headers="mcps1.2.4.1.2 "><p id="p1944203310919"><a name="p1944203310919"></a><a name="p1944203310919"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.65466546654666%" headers="mcps1.2.4.1.3 "><p id="p11443334918"><a name="p11443334918"></a><a name="p11443334918"></a>Cluster ID.</p>
</td>
</tr>
<tr id="row142821951181515"><td class="cellrowborder" valign="top" width="23.13231323132313%" headers="mcps1.2.4.1.1 "><p id="p12440330917"><a name="p12440330917"></a><a name="p12440330917"></a>instances</p>
</td>
<td class="cellrowborder" valign="top" width="30.213021302130212%" headers="mcps1.2.4.1.2 "><p id="p154412330917"><a name="p154412330917"></a><a name="p154412330917"></a>Array of instance objects</p>
</td>
<td class="cellrowborder" valign="top" width="46.65466546654666%" headers="mcps1.2.4.1.3 "><p id="p24412332916"><a name="p24412332916"></a><a name="p24412332916"></a>List of instances to be added. For details, see <a href="#table16533171913167">Table 5</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **instances**  field data structure description

<a name="table16533171913167"></a>
<table><thead align="left"><tr id="row18533191901611"><th class="cellrowborder" valign="top" width="24.062406240624064%" id="mcps1.2.4.1.1"><p id="p1215823519164"><a name="p1215823519164"></a><a name="p1215823519164"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="29.792979297929794%" id="mcps1.2.4.1.2"><p id="p171581935141610"><a name="p171581935141610"></a><a name="p171581935141610"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="46.144614461446146%" id="mcps1.2.4.1.3"><p id="p615853591618"><a name="p615853591618"></a><a name="p615853591618"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row5533519101617"><td class="cellrowborder" valign="top" width="24.062406240624064%" headers="mcps1.2.4.1.1 "><p id="p11158135171617"><a name="p11158135171617"></a><a name="p11158135171617"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="29.792979297929794%" headers="mcps1.2.4.1.2 "><p id="p1115863511162"><a name="p1115863511162"></a><a name="p1115863511162"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.144614461446146%" headers="mcps1.2.4.1.3 "><p id="p191588352163"><a name="p191588352163"></a><a name="p191588352163"></a>Instance ID.</p>
</td>
</tr>
<tr id="row175339191169"><td class="cellrowborder" valign="top" width="24.062406240624064%" headers="mcps1.2.4.1.1 "><p id="p7158173521617"><a name="p7158173521617"></a><a name="p7158173521617"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="29.792979297929794%" headers="mcps1.2.4.1.2 "><p id="p815820350165"><a name="p815820350165"></a><a name="p815820350165"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.144614461446146%" headers="mcps1.2.4.1.3 "><p id="p161586358162"><a name="p161586358162"></a><a name="p161586358162"></a>Instance name.</p>
</td>
</tr>
<tr id="row208820351219"><td class="cellrowborder" valign="top" width="24.062406240624064%" headers="mcps1.2.4.1.1 "><p id="p388183515212"><a name="p388183515212"></a><a name="p388183515212"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="29.792979297929794%" headers="mcps1.2.4.1.2 "><p id="p208814351622"><a name="p208814351622"></a><a name="p208814351622"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.144614461446146%" headers="mcps1.2.4.1.3 "><p id="p198812351923"><a name="p198812351923"></a><a name="p198812351923"></a>Instance type.</p>
</td>
</tr>
<tr id="row075349031"><td class="cellrowborder" valign="top" width="24.062406240624064%" headers="mcps1.2.4.1.1 "><p id="p1475249139"><a name="p1475249139"></a><a name="p1475249139"></a>shard_id</p>
</td>
<td class="cellrowborder" valign="top" width="29.792979297929794%" headers="mcps1.2.4.1.2 "><p id="p1775249733"><a name="p1775249733"></a><a name="p1775249733"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.144614461446146%" headers="mcps1.2.4.1.3 "><p id="p2757492312"><a name="p2757492312"></a><a name="p2757492312"></a>Instance group name.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section3958181015348"></a>

Example request

```
POST /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/extend
{
    "grow": 
        {
            "modifySize": 4
        }
}
```

Example response

```
{
  "id": "4b0fae9f-e3fb-4581-872b-330cdd09a3d5",
  "instances": [
    {
      "id": "2c47ec92-337b-4f22-8337-e342eb315063",
      "name": "Es-c1a2-ess-esn-4-1",
      "type": "ess",
      "shard_id": "esn-4"
    },
    {
      "id": "311077f8-debb-4350-97d5-9eafd2b438f2",
      "name": "Es-c1a2-ess-esn-5-1",
      "type": "ess",
      "shard_id": "esn-5"
    },
    {
      "id": "fcc3c59e-9420-4fd8-a8ad-836c45b6813e",
      "name": "Es-c1a2-ess-esn-6-1",
      "type": "ess",
      "shard_id": "esn-6"
    },
    {
      "id": "dd64e308-3799-4f2a-a57e-9b92e9f3ce45",
      "name": "Es-c1a2-ess-esn-7-1",
      "type": "ess",
      "shard_id": "esn-7"
    }
  ]
}
```

## Status Code<a name="section87962546391"></a>

[Table 6](#table12321369178)  describes the status code.

**Table  6**  Status code

<a name="table12321369178"></a>
<table><thead align="left"><tr id="css_03_0018_row1972183521418"><th class="cellrowborder" valign="top" width="15.939999999999998%" id="mcps1.2.4.1.1"><p id="css_03_0018_p14560134151414"><a name="css_03_0018_p14560134151414"></a><a name="css_03_0018_p14560134151414"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="31.04%" id="mcps1.2.4.1.2"><p id="css_03_0018_p5563194141411"><a name="css_03_0018_p5563194141411"></a><a name="css_03_0018_p5563194141411"></a>Code</p>
</th>
<th class="cellrowborder" valign="top" width="53.02%" id="mcps1.2.4.1.3"><p id="css_03_0018_p256616411143"><a name="css_03_0018_p256616411143"></a><a name="css_03_0018_p256616411143"></a>Status Code Description</p>
</th>
</tr>
</thead>
<tbody><tr id="css_03_0018_row129720356144"><td class="cellrowborder" valign="top" width="15.939999999999998%" headers="mcps1.2.4.1.1 "><p id="css_03_0018_p1957004131410"><a name="css_03_0018_p1957004131410"></a><a name="css_03_0018_p1957004131410"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="31.04%" headers="mcps1.2.4.1.2 "><p id="css_03_0018_p165731141171419"><a name="css_03_0018_p165731141171419"></a><a name="css_03_0018_p165731141171419"></a>BadRequest</p>
</td>
<td class="cellrowborder" valign="top" width="53.02%" headers="mcps1.2.4.1.3 "><p id="css_03_0018_p65778413148"><a name="css_03_0018_p65778413148"></a><a name="css_03_0018_p65778413148"></a>Invalid request.</p>
<p id="css_03_0018_p1557974171415"><a name="css_03_0018_p1557974171415"></a><a name="css_03_0018_p1557974171415"></a>The client should not repeat the request without modifications.</p>
</td>
</tr>
<tr id="css_03_0018_row8972103517147"><td class="cellrowborder" valign="top" width="15.939999999999998%" headers="mcps1.2.4.1.1 "><p id="css_03_0018_p75841441191410"><a name="css_03_0018_p75841441191410"></a><a name="css_03_0018_p75841441191410"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="31.04%" headers="mcps1.2.4.1.2 "><p id="css_03_0018_p258716416142"><a name="css_03_0018_p258716416142"></a><a name="css_03_0018_p258716416142"></a>NotFound</p>
</td>
<td class="cellrowborder" valign="top" width="53.02%" headers="mcps1.2.4.1.3 "><p id="css_03_0018_p15589154118141"><a name="css_03_0018_p15589154118141"></a><a name="css_03_0018_p15589154118141"></a>The requested resource cannot be found.</p>
<p id="css_03_0018_p14590164151410"><a name="css_03_0018_p14590164151410"></a><a name="css_03_0018_p14590164151410"></a>The client should not repeat the request without modifications.</p>
</td>
</tr>
<tr id="css_03_0018_row297223511416"><td class="cellrowborder" valign="top" width="15.939999999999998%" headers="mcps1.2.4.1.1 "><p id="css_03_0018_p13595164131416"><a name="css_03_0018_p13595164131416"></a><a name="css_03_0018_p13595164131416"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="31.04%" headers="mcps1.2.4.1.2 "><p id="css_03_0018_p9598741131416"><a name="css_03_0018_p9598741131416"></a><a name="css_03_0018_p9598741131416"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="53.02%" headers="mcps1.2.4.1.3 "><p id="css_03_0018_p659994115146"><a name="css_03_0018_p659994115146"></a><a name="css_03_0018_p659994115146"></a>The request is processed successfully.</p>
</td>
</tr>
</tbody>
</table>

