# VPC Peering Connection<a name="vpc_permission_0005"></a>

<a name="table967413133817"></a>
<table><thead align="left"><tr id="row9708231163820"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.4.1.1"><p id="p1970823143813"><a name="p1970823143813"></a><a name="p1970823143813"></a>API</p>
</th>
<th class="cellrowborder" valign="top" width="29.72972972972973%" id="mcps1.1.4.1.2"><p id="p12638211185918"><a name="p12638211185918"></a><a name="p12638211185918"></a>API Function</p>
</th>
<th class="cellrowborder" valign="top" width="20.27027027027027%" id="mcps1.1.4.1.3"><p id="p137081931143810"><a name="p137081931143810"></a><a name="p137081931143810"></a>Permissions</p>
</th>
</tr>
</thead>
<tbody><tr id="row197081331113817"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.4.1.1 "><p id="p143974820139"><a name="p143974820139"></a><a name="p143974820139"></a>GET /v2.0/vpc/peerings</p>
</td>
<td class="cellrowborder" valign="top" width="29.72972972972973%" headers="mcps1.1.4.1.2 "><p id="p7482131816133"><a name="p7482131816133"></a><a name="p7482131816133"></a>Querying VPC peering connections</p>
</td>
<td class="cellrowborder" valign="top" width="20.27027027027027%" headers="mcps1.1.4.1.3 "><p id="p13892440173820"><a name="p13892440173820"></a><a name="p13892440173820"></a>vpc:peerings:get</p>
</td>
</tr>
<tr id="row15709203163811"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.4.1.1 "><p id="p17649343101319"><a name="p17649343101319"></a><a name="p17649343101319"></a>GET /v2.0/vpc/peerings/{peering_id}</p>
</td>
<td class="cellrowborder" valign="top" width="29.72972972972973%" headers="mcps1.1.4.1.2 "><p id="p1549015468132"><a name="p1549015468132"></a><a name="p1549015468132"></a>Querying a VPC peering connection</p>
</td>
<td class="cellrowborder" valign="top" width="20.27027027027027%" headers="mcps1.1.4.1.3 "><p id="p1940834512014"><a name="p1940834512014"></a><a name="p1940834512014"></a>vpc:peerings:get</p>
</td>
</tr>
<tr id="row1670914317388"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.4.1.1 "><p id="p181448651411"><a name="p181448651411"></a><a name="p181448651411"></a>POST /v2.0/vpc/peerings</p>
</td>
<td class="cellrowborder" valign="top" width="29.72972972972973%" headers="mcps1.1.4.1.2 "><p id="p8638811165911"><a name="p8638811165911"></a><a name="p8638811165911"></a>Creating a VPC peering connection</p>
</td>
<td class="cellrowborder" valign="top" width="20.27027027027027%" headers="mcps1.1.4.1.3 "><p id="p1724712431387"><a name="p1724712431387"></a><a name="p1724712431387"></a>vpc:peerings:create</p>
</td>
</tr>
<tr id="row6709163118385"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.4.1.1 "><p id="p206275422143"><a name="p206275422143"></a><a name="p206275422143"></a>PUT /v2.0/vpc/peerings/{peering_id}/accept</p>
</td>
<td class="cellrowborder" valign="top" width="29.72972972972973%" headers="mcps1.1.4.1.2 "><p id="p135991634111413"><a name="p135991634111413"></a><a name="p135991634111413"></a>Accepting a VPC peering connection</p>
</td>
<td class="cellrowborder" valign="top" width="20.27027027027027%" headers="mcps1.1.4.1.3 "><p id="p383524711173"><a name="p383524711173"></a><a name="p383524711173"></a>vpc:peerings:accept</p>
</td>
</tr>
<tr id="row1821415719143"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.4.1.1 "><p id="p11214957111419"><a name="p11214957111419"></a><a name="p11214957111419"></a>PUT /v2.0/vpc/peerings/{peering_id}/reject</p>
</td>
<td class="cellrowborder" valign="top" width="29.72972972972973%" headers="mcps1.1.4.1.2 "><p id="p1921455713144"><a name="p1921455713144"></a><a name="p1921455713144"></a>Refusing a VPC peering connection</p>
</td>
<td class="cellrowborder" valign="top" width="20.27027027027027%" headers="mcps1.1.4.1.3 "><p id="p02142057171419"><a name="p02142057171419"></a><a name="p02142057171419"></a>vpc:peerings:reject</p>
</td>
</tr>
<tr id="row134257015151"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.4.1.1 "><p id="p13307113415152"><a name="p13307113415152"></a><a name="p13307113415152"></a>PUT /v2.0/vpc/peerings/{peering_id}</p>
</td>
<td class="cellrowborder" valign="top" width="29.72972972972973%" headers="mcps1.1.4.1.2 "><p id="p74251013151"><a name="p74251013151"></a><a name="p74251013151"></a>Updating a VPC peering connection</p>
</td>
<td class="cellrowborder" valign="top" width="20.27027027027027%" headers="mcps1.1.4.1.3 "><p id="p2720085191"><a name="p2720085191"></a><a name="p2720085191"></a>vpc:peerings:update</p>
</td>
</tr>
<tr id="row629817252151"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.4.1.1 "><p id="p1629862511519"><a name="p1629862511519"></a><a name="p1629862511519"></a>DELETE /v2.0/vpc/peerings/{peering_id}</p>
</td>
<td class="cellrowborder" valign="top" width="29.72972972972973%" headers="mcps1.1.4.1.2 "><p id="p1129816255153"><a name="p1129816255153"></a><a name="p1129816255153"></a>Deleting a VPC peering connection</p>
</td>
<td class="cellrowborder" valign="top" width="20.27027027027027%" headers="mcps1.1.4.1.3 "><p id="p1381162919184"><a name="p1381162919184"></a><a name="p1381162919184"></a>vpc:peerings:delete</p>
</td>
</tr>
</tbody>
</table>

