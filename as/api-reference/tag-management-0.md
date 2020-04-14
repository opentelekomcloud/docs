# Tag Management<a name="EN-US_TOPIC_0120460581"></a>

<a name="table5773912426"></a>
<table><thead align="left"><tr id="row178123994218"><th class="cellrowborder" valign="top" width="19%" id="mcps1.1.5.1.1"><p id="p156502141495"><a name="p156502141495"></a><a name="p156502141495"></a><strong id="b472302141816"><a name="b472302141816"></a><a name="b472302141816"></a>Permission</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.2"><p id="p17522185717013"><a name="p17522185717013"></a><a name="p17522185717013"></a><strong id="b798115551813"><a name="b798115551813"></a><a name="b798115551813"></a>Actions</strong></p>
</th>
<th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.1.5.1.3"><p id="p1458713357289"><a name="p1458713357289"></a><a name="p1458713357289"></a><strong id="b629259111815"><a name="b629259111815"></a><a name="b629259111815"></a>Authorization Scope</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27%" id="mcps1.1.5.1.4"><p id="p151662411099"><a name="p151662411099"></a><a name="p151662411099"></a><strong id="b1044111211181"><a name="b1044111211181"></a><a name="b1044111211181"></a>APIs</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row288398427"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.5.1.1 "><p id="p11840203182819"><a name="p11840203182819"></a><a name="p11840203182819"></a>Querying tags</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="p48133974216"><a name="p48133974216"></a><a name="p48133974216"></a>as:tags:list</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.5.1.3 "><a name="ul6901191173020"></a><a name="ul6901191173020"></a><ul id="ul6901191173020"><li>Supported:<p id="p99014163020"><a name="p99014163020"></a><a name="p99014163020"></a>Project</p>
</li></ul>
<a name="ul29011117300"></a><a name="ul29011117300"></a><ul id="ul29011117300"><li>Unsupported:<p id="p169011918306"><a name="p169011918306"></a><a name="p169011918306"></a>Enterprise project</p>
</li></ul>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.5.1.4 "><p id="p10811393426"><a name="p10811393426"></a><a name="p10811393426"></a>GET /autoscaling-api/v1/{project_id}/{resource_type}/tags</p>
</td>
</tr>
<tr id="row28123911426"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.5.1.1 "><p id="p484011317284"><a name="p484011317284"></a><a name="p484011317284"></a>Querying tags of a resource</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="p138039124214"><a name="p138039124214"></a><a name="p138039124214"></a>as:tags:get</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.5.1.3 "><a name="ul7910191113016"></a><a name="ul7910191113016"></a><ul id="ul7910191113016"><li>Supported:<p id="p191012133015"><a name="p191012133015"></a><a name="p191012133015"></a>Project</p>
</li></ul>
<a name="ul3910141123017"></a><a name="ul3910141123017"></a><ul id="ul3910141123017"><li>Unsupported:<p id="p169101913307"><a name="p169101913307"></a><a name="p169101913307"></a>Enterprise project</p>
</li></ul>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.5.1.4 "><p id="p17813397424"><a name="p17813397424"></a><a name="p17813397424"></a>GET /autoscaling-api/v1/{project_id}/{resource_type}/{resource_id}/tags</p>
</td>
</tr>
<tr id="row188163984215"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.5.1.1 "><p id="p1584053115288"><a name="p1584053115288"></a><a name="p1584053115288"></a>Updating or deleting a tag</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="p118153920423"><a name="p118153920423"></a><a name="p118153920423"></a>as:tags:set</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.5.1.3 "><a name="ul2091613119305"></a><a name="ul2091613119305"></a><ul id="ul2091613119305"><li>Supported:<p id="p591611193014"><a name="p591611193014"></a><a name="p591611193014"></a>Project</p>
</li></ul>
<a name="ul1691671183015"></a><a name="ul1691671183015"></a><ul id="ul1691671183015"><li>Unsupported:<p id="p10916017309"><a name="p10916017309"></a><a name="p10916017309"></a>Enterprise project</p>
</li></ul>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.5.1.4 "><p id="p16883924218"><a name="p16883924218"></a><a name="p16883924218"></a>POST /autoscaling-api/v1/{project_id}/{resource_type}/{resource_id}/tags/action</p>
</td>
</tr>
<tr id="row3157175131516"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.5.1.1 "><p id="p1157135101510"><a name="p1157135101510"></a><a name="p1157135101510"></a>Querying resources</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="p815715161517"><a name="p815715161517"></a><a name="p815715161517"></a>as:tagResources:list</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.5.1.3 "><a name="ul10341132931516"></a><a name="ul10341132931516"></a><ul id="ul10341132931516"><li>Supported:<p id="p1934352918155"><a name="p1934352918155"></a><a name="p1934352918155"></a>Project</p>
</li></ul>
<a name="ul134332931515"></a><a name="ul134332931515"></a><ul id="ul134332931515"><li>Unsupported:<p id="p13344829191518"><a name="p13344829191518"></a><a name="p13344829191518"></a>Enterprise project</p>
</li></ul>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.5.1.4 "><p id="p11157125101515"><a name="p11157125101515"></a><a name="p11157125101515"></a>POST /autoscaling-api/v1/{project_id}/{resource_type}/resource_instances/action</p>
</td>
</tr>
</tbody>
</table>

