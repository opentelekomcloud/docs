# Floating IP Address \(OpenStack Neutron API\)<a name="eip_apipermission_0006"></a>

<a name="en-us_topic_0201534306_table620116613438"></a>
<table><thead align="left"><tr id="en-us_topic_0201534306_row122422612431"><th class="cellrowborder" valign="top" width="47.368421052631575%" id="mcps1.1.4.1.1"><p id="en-us_topic_0201534306_p18242167434"><a name="en-us_topic_0201534306_p18242167434"></a><a name="en-us_topic_0201534306_p18242167434"></a>API</p>
</th>
<th class="cellrowborder" valign="top" width="21.052631578947363%" id="mcps1.1.4.1.2"><p id="en-us_topic_0201534306_p1742017470614"><a name="en-us_topic_0201534306_p1742017470614"></a><a name="en-us_topic_0201534306_p1742017470614"></a>API Function</p>
</th>
<th class="cellrowborder" valign="top" width="31.578947368421044%" id="mcps1.1.4.1.3"><p id="en-us_topic_0201534306_p132426674312"><a name="en-us_topic_0201534306_p132426674312"></a><a name="en-us_topic_0201534306_p132426674312"></a>Permissions</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0201534306_row11242186124315"><td class="cellrowborder" valign="top" width="47.368421052631575%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0201534306_p16242156154311"><a name="en-us_topic_0201534306_p16242156154311"></a><a name="en-us_topic_0201534306_p16242156154311"></a>GET /v2.0/floatingips</p>
</td>
<td class="cellrowborder" valign="top" width="21.052631578947363%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0201534306_p1942012471564"><a name="en-us_topic_0201534306_p1942012471564"></a><a name="en-us_topic_0201534306_p1942012471564"></a>Queries floating IP addresses.</p>
</td>
<td class="cellrowborder" valign="top" width="31.578947368421044%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0201534306_p5358141413439"><a name="en-us_topic_0201534306_p5358141413439"></a><a name="en-us_topic_0201534306_p5358141413439"></a>vpc:floatingIps:get</p>
</td>
</tr>
<tr id="en-us_topic_0201534306_row1424216134314"><td class="cellrowborder" valign="top" width="47.368421052631575%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0201534306_p1124219664317"><a name="en-us_topic_0201534306_p1124219664317"></a><a name="en-us_topic_0201534306_p1124219664317"></a>GET /v2.0/floatingips/{floatingip_id}</p>
</td>
<td class="cellrowborder" valign="top" width="21.052631578947363%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0201534306_p9420164712614"><a name="en-us_topic_0201534306_p9420164712614"></a><a name="en-us_topic_0201534306_p9420164712614"></a>Queries a floating IP address.</p>
</td>
<td class="cellrowborder" valign="top" width="31.578947368421044%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0201534306_p1818716161433"><a name="en-us_topic_0201534306_p1818716161433"></a><a name="en-us_topic_0201534306_p1818716161433"></a>vpc:floatingIps:get</p>
</td>
</tr>
<tr id="en-us_topic_0201534306_row192471262439"><td class="cellrowborder" valign="top" width="47.368421052631575%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0201534306_p92473619434"><a name="en-us_topic_0201534306_p92473619434"></a><a name="en-us_topic_0201534306_p92473619434"></a>POST /v2.0/floatingips</p>
</td>
<td class="cellrowborder" valign="top" width="21.052631578947363%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0201534306_p13420547366"><a name="en-us_topic_0201534306_p13420547366"></a><a name="en-us_topic_0201534306_p13420547366"></a>Creates a floating IP address.</p>
</td>
<td class="cellrowborder" valign="top" width="31.578947368421044%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0201534306_p142981517134319"><a name="en-us_topic_0201534306_p142981517134319"></a><a name="en-us_topic_0201534306_p142981517134319"></a>vpc:floatingIps:create</p>
</td>
</tr>
<tr id="en-us_topic_0201534306_row1724719674312"><td class="cellrowborder" valign="top" width="47.368421052631575%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0201534306_p1224756134320"><a name="en-us_topic_0201534306_p1224756134320"></a><a name="en-us_topic_0201534306_p1224756134320"></a>PUT /v2.0/floatingips/{floatingip_id}</p>
</td>
<td class="cellrowborder" valign="top" width="21.052631578947363%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0201534306_p16420347065"><a name="en-us_topic_0201534306_p16420347065"></a><a name="en-us_topic_0201534306_p16420347065"></a>Updates a floating IP address.</p>
</td>
<td class="cellrowborder" valign="top" width="31.578947368421044%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0201534306_p17326101812436"><a name="en-us_topic_0201534306_p17326101812436"></a><a name="en-us_topic_0201534306_p17326101812436"></a>vpc:floatingIps:update</p>
</td>
</tr>
<tr id="en-us_topic_0201534306_row102470615434"><td class="cellrowborder" valign="top" width="47.368421052631575%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0201534306_p9247126204318"><a name="en-us_topic_0201534306_p9247126204318"></a><a name="en-us_topic_0201534306_p9247126204318"></a>DELETE /v2.0/floatingips/{floatingip_id}</p>
</td>
<td class="cellrowborder" valign="top" width="21.052631578947363%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0201534306_p1542119471269"><a name="en-us_topic_0201534306_p1542119471269"></a><a name="en-us_topic_0201534306_p1542119471269"></a>Deletes a floating IP address.</p>
</td>
<td class="cellrowborder" valign="top" width="31.578947368421044%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0201534306_p64451919134314"><a name="en-us_topic_0201534306_p64451919134314"></a><a name="en-us_topic_0201534306_p64451919134314"></a>vpc:floatingIps:delete</p>
</td>
</tr>
</tbody>
</table>

