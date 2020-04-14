# Firewall \(OpenStack Neutron API\)<a name="vpc_permission_0015"></a>

<a name="table138590164616"></a>
<table><thead align="left"><tr id="row2054710012466"><th class="cellrowborder" valign="top" width="49.382716049382715%" id="mcps1.1.4.1.1"><p id="p1754710018467"><a name="p1754710018467"></a><a name="p1754710018467"></a>API</p>
</th>
<th class="cellrowborder" valign="top" width="19.753086419753085%" id="mcps1.1.4.1.2"><p id="p1489614416718"><a name="p1489614416718"></a><a name="p1489614416718"></a>API Function</p>
</th>
<th class="cellrowborder" valign="top" width="30.864197530864196%" id="mcps1.1.4.1.3"><p id="p135474024612"><a name="p135474024612"></a><a name="p135474024612"></a>Permissions</p>
</th>
</tr>
</thead>
<tbody><tr id="row175475019467"><td class="cellrowborder" valign="top" width="49.382716049382715%" headers="mcps1.1.4.1.1 "><p id="p55474044610"><a name="p55474044610"></a><a name="p55474044610"></a>GET /v2.0/fwaas/firewall_rules</p>
</td>
<td class="cellrowborder" valign="top" width="19.753086419753085%" headers="mcps1.1.4.1.2 "><p id="p38962449710"><a name="p38962449710"></a><a name="p38962449710"></a>Queries all firewall rules.</p>
</td>
<td class="cellrowborder" valign="top" width="30.864197530864196%" headers="mcps1.1.4.1.3 "><p id="p87832010154620"><a name="p87832010154620"></a><a name="p87832010154620"></a>vpc:firewallRules:get</p>
</td>
</tr>
<tr id="row954717015469"><td class="cellrowborder" valign="top" width="49.382716049382715%" headers="mcps1.1.4.1.1 "><p id="p854711012462"><a name="p854711012462"></a><a name="p854711012462"></a>GET /v2.0/fwaas/firewall_rules/{firewall_rule_id}</p>
</td>
<td class="cellrowborder" valign="top" width="19.753086419753085%" headers="mcps1.1.4.1.2 "><p id="p68961644874"><a name="p68961644874"></a><a name="p68961644874"></a>Queries a firewall rule.</p>
</td>
<td class="cellrowborder" valign="top" width="30.864197530864196%" headers="mcps1.1.4.1.3 "><p id="p10249161204616"><a name="p10249161204616"></a><a name="p10249161204616"></a>vpc:firewallRules:get</p>
</td>
</tr>
<tr id="row754717018466"><td class="cellrowborder" valign="top" width="49.382716049382715%" headers="mcps1.1.4.1.1 "><p id="p25471074610"><a name="p25471074610"></a><a name="p25471074610"></a>POST /v2.0/fwaas/firewall_rules</p>
</td>
<td class="cellrowborder" valign="top" width="19.753086419753085%" headers="mcps1.1.4.1.2 "><p id="p989619441578"><a name="p989619441578"></a><a name="p989619441578"></a>Creates a firewall rule.</p>
</td>
<td class="cellrowborder" valign="top" width="30.864197530864196%" headers="mcps1.1.4.1.3 "><p id="p1642771311465"><a name="p1642771311465"></a><a name="p1642771311465"></a>vpc:firewallRules:create</p>
</td>
</tr>
<tr id="row25472014464"><td class="cellrowborder" valign="top" width="49.382716049382715%" headers="mcps1.1.4.1.1 "><p id="p15471304466"><a name="p15471304466"></a><a name="p15471304466"></a>PUT /v2.0/fwaas/firewall_rules/{firewall_rule_id}</p>
</td>
<td class="cellrowborder" valign="top" width="19.753086419753085%" headers="mcps1.1.4.1.2 "><p id="p10896844676"><a name="p10896844676"></a><a name="p10896844676"></a>Updates a firewall rule.</p>
</td>
<td class="cellrowborder" valign="top" width="30.864197530864196%" headers="mcps1.1.4.1.3 "><p id="p10998714144611"><a name="p10998714144611"></a><a name="p10998714144611"></a>vpc:firewallRules:update</p>
</td>
</tr>
<tr id="row2054713064610"><td class="cellrowborder" valign="top" width="49.382716049382715%" headers="mcps1.1.4.1.1 "><p id="p7547302464"><a name="p7547302464"></a><a name="p7547302464"></a>DELETE /v2.0/fwaas/firewall_rules/{firewall_rule_id}</p>
</td>
<td class="cellrowborder" valign="top" width="19.753086419753085%" headers="mcps1.1.4.1.2 "><p id="p128968441671"><a name="p128968441671"></a><a name="p128968441671"></a>Deletes a firewall rule.</p>
</td>
<td class="cellrowborder" valign="top" width="30.864197530864196%" headers="mcps1.1.4.1.3 "><p id="p0230316104616"><a name="p0230316104616"></a><a name="p0230316104616"></a>vpc:firewallRules:delete</p>
</td>
</tr>
<tr id="row17547110134614"><td class="cellrowborder" valign="top" width="49.382716049382715%" headers="mcps1.1.4.1.1 "><p id="p13547604464"><a name="p13547604464"></a><a name="p13547604464"></a>GET /v2.0/fwaas/firewall_policies</p>
</td>
<td class="cellrowborder" valign="top" width="19.753086419753085%" headers="mcps1.1.4.1.2 "><p id="p16896444478"><a name="p16896444478"></a><a name="p16896444478"></a>Queries all firewall policies.</p>
</td>
<td class="cellrowborder" valign="top" width="30.864197530864196%" headers="mcps1.1.4.1.3 "><p id="p1161211711468"><a name="p1161211711468"></a><a name="p1161211711468"></a>vpc:firewallPolicies:get</p>
</td>
</tr>
<tr id="row1554717012462"><td class="cellrowborder" valign="top" width="49.382716049382715%" headers="mcps1.1.4.1.1 "><p id="p1054790144617"><a name="p1054790144617"></a><a name="p1054790144617"></a>GET /v2.0/fwaas/firewall_policies/{firewall_policy_id}</p>
</td>
<td class="cellrowborder" valign="top" width="19.753086419753085%" headers="mcps1.1.4.1.2 "><p id="p68961448715"><a name="p68961448715"></a><a name="p68961448715"></a>Queries a firewall policy.</p>
</td>
<td class="cellrowborder" valign="top" width="30.864197530864196%" headers="mcps1.1.4.1.3 "><p id="p1018319193467"><a name="p1018319193467"></a><a name="p1018319193467"></a>vpc:firewallPolicies:get</p>
</td>
</tr>
<tr id="row9547170204610"><td class="cellrowborder" valign="top" width="49.382716049382715%" headers="mcps1.1.4.1.1 "><p id="p155471102460"><a name="p155471102460"></a><a name="p155471102460"></a>POST /v2.0/fwaas/firewall_policies</p>
</td>
<td class="cellrowborder" valign="top" width="19.753086419753085%" headers="mcps1.1.4.1.2 "><p id="p3896944179"><a name="p3896944179"></a><a name="p3896944179"></a>Creates a firewall policy.</p>
</td>
<td class="cellrowborder" valign="top" width="30.864197530864196%" headers="mcps1.1.4.1.3 "><p id="p1938032004613"><a name="p1938032004613"></a><a name="p1938032004613"></a>vpc:firewallPolicies:create</p>
</td>
</tr>
<tr id="row18547001460"><td class="cellrowborder" valign="top" width="49.382716049382715%" headers="mcps1.1.4.1.1 "><p id="p1254713011460"><a name="p1254713011460"></a><a name="p1254713011460"></a>PUT /v2.0/fwaas/firewall_policies/{firewall_policy_id}</p>
</td>
<td class="cellrowborder" valign="top" width="19.753086419753085%" headers="mcps1.1.4.1.2 "><p id="p889654416711"><a name="p889654416711"></a><a name="p889654416711"></a>Updates a firewall policy.</p>
</td>
<td class="cellrowborder" valign="top" width="30.864197530864196%" headers="mcps1.1.4.1.3 "><p id="p625182414611"><a name="p625182414611"></a><a name="p625182414611"></a>vpc:firewallPolicies:update</p>
</td>
</tr>
<tr id="row205476084614"><td class="cellrowborder" valign="top" width="49.382716049382715%" headers="mcps1.1.4.1.1 "><p id="p1454710013464"><a name="p1454710013464"></a><a name="p1454710013464"></a>DELETE /v2.0/fwaas/firewall_policies/{firewall_policy_id}</p>
</td>
<td class="cellrowborder" valign="top" width="19.753086419753085%" headers="mcps1.1.4.1.2 "><p id="p68974441376"><a name="p68974441376"></a><a name="p68974441376"></a>Deletes a firewall policy.</p>
</td>
<td class="cellrowborder" valign="top" width="30.864197530864196%" headers="mcps1.1.4.1.3 "><p id="p1761332616465"><a name="p1761332616465"></a><a name="p1761332616465"></a>vpc:firewallPolicies:delete</p>
</td>
</tr>
<tr id="row65472074610"><td class="cellrowborder" valign="top" width="49.382716049382715%" headers="mcps1.1.4.1.1 "><p id="p185471074618"><a name="p185471074618"></a><a name="p185471074618"></a>PUT /v2.0/fwaas/firewall_policies/{firewall_policy_id}/insert_rule</p>
</td>
<td class="cellrowborder" valign="top" width="19.753086419753085%" headers="mcps1.1.4.1.2 "><p id="p689710445712"><a name="p689710445712"></a><a name="p689710445712"></a>Inserts a firewall rule.</p>
</td>
<td class="cellrowborder" valign="top" width="30.864197530864196%" headers="mcps1.1.4.1.3 "><a name="ul194831710115410"></a><a name="ul194831710115410"></a><ul id="ul194831710115410"><li>vpc:firewallPolicies:addRule</li><li>vpc:firewallPolicies:get</li></ul>
</td>
</tr>
<tr id="row7547190114619"><td class="cellrowborder" valign="top" width="49.382716049382715%" headers="mcps1.1.4.1.1 "><p id="p0547130134614"><a name="p0547130134614"></a><a name="p0547130134614"></a>PUT /v2.0/fwaas/firewall_policies/{firewall_policy_id}/remove_rule</p>
</td>
<td class="cellrowborder" valign="top" width="19.753086419753085%" headers="mcps1.1.4.1.2 "><p id="p168971144178"><a name="p168971144178"></a><a name="p168971144178"></a>Removes a firewall rule.</p>
</td>
<td class="cellrowborder" valign="top" width="30.864197530864196%" headers="mcps1.1.4.1.3 "><a name="ul65475011468"></a><a name="ul65475011468"></a><ul id="ul65475011468"><li>vpc:firewallPolicies:removeRule</li><li>vpc:firewallPolicies:get</li></ul>
</td>
</tr>
<tr id="row1154718015467"><td class="cellrowborder" valign="top" width="49.382716049382715%" headers="mcps1.1.4.1.1 "><p id="p115477044612"><a name="p115477044612"></a><a name="p115477044612"></a>GET /v2.0/fwaas/firewall_groups</p>
</td>
<td class="cellrowborder" valign="top" width="19.753086419753085%" headers="mcps1.1.4.1.2 "><p id="p188978441979"><a name="p188978441979"></a><a name="p188978441979"></a>Queries all firewall groups.</p>
</td>
<td class="cellrowborder" valign="top" width="30.864197530864196%" headers="mcps1.1.4.1.3 "><p id="p153991240174616"><a name="p153991240174616"></a><a name="p153991240174616"></a>vpc:firewallGroups:get</p>
</td>
</tr>
<tr id="row165479014611"><td class="cellrowborder" valign="top" width="49.382716049382715%" headers="mcps1.1.4.1.1 "><p id="p95471309469"><a name="p95471309469"></a><a name="p95471309469"></a>GET /v2.0/fwaas/firewall_groups/{firewall_group_id}</p>
</td>
<td class="cellrowborder" valign="top" width="19.753086419753085%" headers="mcps1.1.4.1.2 "><p id="p10897164410715"><a name="p10897164410715"></a><a name="p10897164410715"></a>Queries a firewall group.</p>
</td>
<td class="cellrowborder" valign="top" width="30.864197530864196%" headers="mcps1.1.4.1.3 "><p id="p5766194114618"><a name="p5766194114618"></a><a name="p5766194114618"></a>vpc:firewallGroups:get</p>
</td>
</tr>
<tr id="row1154718013461"><td class="cellrowborder" valign="top" width="49.382716049382715%" headers="mcps1.1.4.1.1 "><p id="p254914014462"><a name="p254914014462"></a><a name="p254914014462"></a>POST /v2.0/fwaas/firewall_groups</p>
</td>
<td class="cellrowborder" valign="top" width="19.753086419753085%" headers="mcps1.1.4.1.2 "><p id="p88971344977"><a name="p88971344977"></a><a name="p88971344977"></a>Creates a firewall group.</p>
</td>
<td class="cellrowborder" valign="top" width="30.864197530864196%" headers="mcps1.1.4.1.3 "><p id="p17963425464"><a name="p17963425464"></a><a name="p17963425464"></a>vpc:firewallGroups:create</p>
</td>
</tr>
<tr id="row11549307461"><td class="cellrowborder" valign="top" width="49.382716049382715%" headers="mcps1.1.4.1.1 "><p id="p14549901464"><a name="p14549901464"></a><a name="p14549901464"></a>PUT /v2.0/fwaas/firewall_groups/{firewall_group_id}</p>
</td>
<td class="cellrowborder" valign="top" width="19.753086419753085%" headers="mcps1.1.4.1.2 "><p id="p389774420716"><a name="p389774420716"></a><a name="p389774420716"></a>Updates a firewall group.</p>
</td>
<td class="cellrowborder" valign="top" width="30.864197530864196%" headers="mcps1.1.4.1.3 "><p id="p1171664394618"><a name="p1171664394618"></a><a name="p1171664394618"></a>vpc:firewallGroups:update</p>
</td>
</tr>
<tr id="row15549309464"><td class="cellrowborder" valign="top" width="49.382716049382715%" headers="mcps1.1.4.1.1 "><p id="p1654911084613"><a name="p1654911084613"></a><a name="p1654911084613"></a>DELETE /v2.0/fwaas/firewall_groups/{firewall_group_id}</p>
</td>
<td class="cellrowborder" valign="top" width="19.753086419753085%" headers="mcps1.1.4.1.2 "><p id="p158974442715"><a name="p158974442715"></a><a name="p158974442715"></a>Deletes a firewall group.</p>
</td>
<td class="cellrowborder" valign="top" width="30.864197530864196%" headers="mcps1.1.4.1.3 "><p id="p182421245134619"><a name="p182421245134619"></a><a name="p182421245134619"></a>vpc:firewallGroups:delete</p>
</td>
</tr>
</tbody>
</table>

