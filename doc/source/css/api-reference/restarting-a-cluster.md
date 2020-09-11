# Restarting a Cluster<a name="css_03_0021"></a>

## Function<a name="section16607137567"></a>

This API is used to restart a cluster. Restarting the cluster will interrupt ongoing services.

## URI<a name="section1566021345618"></a>

```
POST /v1.0/{project_id}/clusters/{cluster_id}/restart
```

**Table  1**  Parameter description

<a name="table5660213195614"></a>
<table><thead align="left"><tr id="row1114111425612"><th class="cellrowborder" valign="top" width="25.742574257425744%" id="mcps1.2.5.1.1"><p id="p0114121417563"><a name="p0114121417563"></a><a name="p0114121417563"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="24.752475247524753%" id="mcps1.2.5.1.2"><p id="p51141140563"><a name="p51141140563"></a><a name="p51141140563"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="18.81188118811881%" id="mcps1.2.5.1.3"><p id="p911411143567"><a name="p911411143567"></a><a name="p911411143567"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="30.693069306930692%" id="mcps1.2.5.1.4"><p id="p511417145568"><a name="p511417145568"></a><a name="p511417145568"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row4114314185617"><td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.5.1.1 "><p id="p411491414569"><a name="p411491414569"></a><a name="p411491414569"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="24.752475247524753%" headers="mcps1.2.5.1.2 "><p id="p11141814195617"><a name="p11141814195617"></a><a name="p11141814195617"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.5.1.3 "><p id="p151147141568"><a name="p151147141568"></a><a name="p151147141568"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="30.693069306930692%" headers="mcps1.2.5.1.4 "><p id="p181147147563"><a name="p181147147563"></a><a name="p181147147563"></a>Project ID.</p>
</td>
</tr>
<tr id="row121141814115618"><td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.5.1.1 "><p id="p1011491416566"><a name="p1011491416566"></a><a name="p1011491416566"></a>cluster_id</p>
</td>
<td class="cellrowborder" valign="top" width="24.752475247524753%" headers="mcps1.2.5.1.2 "><p id="p511441415614"><a name="p511441415614"></a><a name="p511441415614"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.5.1.3 "><p id="p9114814125614"><a name="p9114814125614"></a><a name="p9114814125614"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="30.693069306930692%" headers="mcps1.2.5.1.4 "><p id="p211461445611"><a name="p211461445611"></a><a name="p211461445611"></a>ID of the cluster to be restarted.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section16676613185611"></a>

None

## Response<a name="section567618138567"></a>

**Table  2**  Parameter description

<a name="table134134101673"></a>
<table><thead align="left"><tr id="row34302108710"><th class="cellrowborder" valign="top" width="20.73%" id="mcps1.2.4.1.1"><p id="p144309102719"><a name="p144309102719"></a><a name="p144309102719"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21.95%" id="mcps1.2.4.1.2"><p id="p24306101877"><a name="p24306101877"></a><a name="p24306101877"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="57.32000000000001%" id="mcps1.2.4.1.3"><p id="p743071010717"><a name="p743071010717"></a><a name="p743071010717"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row164441710172"><td class="cellrowborder" valign="top" width="20.73%" headers="mcps1.2.4.1.1 "><p id="p11444191010712"><a name="p11444191010712"></a><a name="p11444191010712"></a>jobId</p>
</td>
<td class="cellrowborder" valign="top" width="21.95%" headers="mcps1.2.4.1.2 "><p id="p94447103718"><a name="p94447103718"></a><a name="p94447103718"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.32000000000001%" headers="mcps1.2.4.1.3 "><p id="p1644420107711"><a name="p1644420107711"></a><a name="p1644420107711"></a>ID of the restart task.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section02195263215"></a>

Example request

```
POST /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/47e49a5e-8ced-4d0d-ae15-2af62ac468e3/restart
```

Example response

```
{ 
 "jobId": [  
"ff8080815fa0fa5e015fa365b6300007" 
 ]
 }
```

## Status Code<a name="section87962546391"></a>

[Table 3](#table12321369178)  describes the status code.

**Table  3**  Status code

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

