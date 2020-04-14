# Bandwidth \(V2.0\)<a name="eip_apipermission_0004"></a>

<a name="en-us_topic_0201534017_table11714123643216"></a>
<table><thead align="left"><tr id="en-us_topic_0201534017_row1189103603211"><th class="cellrowborder" valign="top" width="54.794520547945204%" id="mcps1.1.4.1.1"><p id="en-us_topic_0201534017_p489173603213"><a name="en-us_topic_0201534017_p489173603213"></a><a name="en-us_topic_0201534017_p489173603213"></a>API</p>
</th>
<th class="cellrowborder" valign="top" width="23.28767123287671%" id="mcps1.1.4.1.2"><p id="en-us_topic_0201534017_p128919363322"><a name="en-us_topic_0201534017_p128919363322"></a><a name="en-us_topic_0201534017_p128919363322"></a>API Function</p>
</th>
<th class="cellrowborder" valign="top" width="21.91780821917808%" id="mcps1.1.4.1.3"><p id="en-us_topic_0201534017_p1789316368323"><a name="en-us_topic_0201534017_p1789316368323"></a><a name="en-us_topic_0201534017_p1789316368323"></a>Permissions</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0201534017_row2893836163216"><td class="cellrowborder" valign="top" width="54.794520547945204%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0201534017_p189363623210"><a name="en-us_topic_0201534017_p189363623210"></a><a name="en-us_topic_0201534017_p189363623210"></a>POST /v2.0/{project_id}/bandwidths</p>
</td>
<td class="cellrowborder" valign="top" width="23.28767123287671%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0201534017_p289363693211"><a name="en-us_topic_0201534017_p289363693211"></a><a name="en-us_topic_0201534017_p289363693211"></a>Allocates a shared bandwidth.</p>
</td>
<td class="cellrowborder" valign="top" width="21.91780821917808%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0201534017_p16893436153218"><a name="en-us_topic_0201534017_p16893436153218"></a><a name="en-us_topic_0201534017_p16893436153218"></a>vpc:bandwidths:create</p>
</td>
</tr>
<tr id="en-us_topic_0201534017_row198931336143219"><td class="cellrowborder" valign="top" width="54.794520547945204%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0201534017_p20893203693218"><a name="en-us_topic_0201534017_p20893203693218"></a><a name="en-us_topic_0201534017_p20893203693218"></a>DELETE /v2.0/{project_id}/bandwidths/{bandwidth_id}</p>
</td>
<td class="cellrowborder" valign="top" width="23.28767123287671%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0201534017_p19893536143218"><a name="en-us_topic_0201534017_p19893536143218"></a><a name="en-us_topic_0201534017_p19893536143218"></a>Deletes a shared bandwidth.</p>
</td>
<td class="cellrowborder" valign="top" width="21.91780821917808%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0201534017_p14893163623216"><a name="en-us_topic_0201534017_p14893163623216"></a><a name="en-us_topic_0201534017_p14893163623216"></a>vpc:bandwidths:delete</p>
</td>
</tr>
<tr id="en-us_topic_0201534017_row1389333616321"><td class="cellrowborder" valign="top" width="54.794520547945204%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0201534017_p1489311368324"><a name="en-us_topic_0201534017_p1489311368324"></a><a name="en-us_topic_0201534017_p1489311368324"></a>POST /v2.0/{project_id}/bandwidths/{bandwidth_id}/insert</p>
</td>
<td class="cellrowborder" valign="top" width="23.28767123287671%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0201534017_p98935364327"><a name="en-us_topic_0201534017_p98935364327"></a><a name="en-us_topic_0201534017_p98935364327"></a>Adds an EIP to a shared bandwidth.</p>
</td>
<td class="cellrowborder" valign="top" width="21.91780821917808%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0201534017_p589483603220"><a name="en-us_topic_0201534017_p589483603220"></a><a name="en-us_topic_0201534017_p589483603220"></a>vpc:publicIps:insert</p>
</td>
</tr>
<tr id="en-us_topic_0201534017_row289412363329"><td class="cellrowborder" valign="top" width="54.794520547945204%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0201534017_p6894836163215"><a name="en-us_topic_0201534017_p6894836163215"></a><a name="en-us_topic_0201534017_p6894836163215"></a>POST /v2.0/{project_id}/bandwidths/{bandwidth_id}/remove</p>
</td>
<td class="cellrowborder" valign="top" width="23.28767123287671%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0201534017_p1989463618324"><a name="en-us_topic_0201534017_p1989463618324"></a><a name="en-us_topic_0201534017_p1989463618324"></a>Removes an EIP from a shared bandwidth.</p>
</td>
<td class="cellrowborder" valign="top" width="21.91780821917808%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0201534017_p089443619327"><a name="en-us_topic_0201534017_p089443619327"></a><a name="en-us_topic_0201534017_p089443619327"></a>vpc:publicIps:remove</p>
</td>
</tr>
</tbody>
</table>

