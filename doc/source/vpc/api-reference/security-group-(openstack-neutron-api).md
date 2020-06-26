# Security Group \(OpenStack Neutron API\)<a name="vpc_permission_0016"></a>

<a name="table111868166448"></a>
<table><thead align="left"><tr id="row202761516194420"><th class="cellrowborder" valign="top" width="52.63157894736842%" id="mcps1.1.4.1.1"><p id="p11276201616440"><a name="p11276201616440"></a><a name="p11276201616440"></a>API</p>
</th>
<th class="cellrowborder" valign="top" width="19.736842105263158%" id="mcps1.1.4.1.2"><p id="p1014003731317"><a name="p1014003731317"></a><a name="p1014003731317"></a>API Function</p>
</th>
<th class="cellrowborder" valign="top" width="27.631578947368418%" id="mcps1.1.4.1.3"><p id="p6276816124418"><a name="p6276816124418"></a><a name="p6276816124418"></a>Permissions</p>
</th>
</tr>
</thead>
<tbody><tr id="row1327615166444"><td class="cellrowborder" valign="top" width="52.63157894736842%" headers="mcps1.1.4.1.1 "><p id="p527614163445"><a name="p527614163445"></a><a name="p527614163445"></a>GET /v2.0/security-groups</p>
</td>
<td class="cellrowborder" valign="top" width="19.736842105263158%" headers="mcps1.1.4.1.2 "><p id="p121401137121311"><a name="p121401137121311"></a><a name="p121401137121311"></a>Queries a security group.</p>
</td>
<td class="cellrowborder" valign="top" width="27.631578947368418%" headers="mcps1.1.4.1.3 "><p id="p98711213440"><a name="p98711213440"></a><a name="p98711213440"></a>vpc:securityGroups:get</p>
</td>
</tr>
<tr id="row1276141614415"><td class="cellrowborder" valign="top" width="52.63157894736842%" headers="mcps1.1.4.1.1 "><p id="p7277416144413"><a name="p7277416144413"></a><a name="p7277416144413"></a>GET /v2.0/security-groups/{security_group_id}</p>
</td>
<td class="cellrowborder" valign="top" width="19.736842105263158%" headers="mcps1.1.4.1.2 "><p id="p31401537101319"><a name="p31401537101319"></a><a name="p31401537101319"></a>Queries details about a security group.</p>
</td>
<td class="cellrowborder" valign="top" width="27.631578947368418%" headers="mcps1.1.4.1.3 "><p id="p10403422194410"><a name="p10403422194410"></a><a name="p10403422194410"></a>vpc:securityGroups:get</p>
</td>
</tr>
<tr id="row8277141624413"><td class="cellrowborder" valign="top" width="52.63157894736842%" headers="mcps1.1.4.1.1 "><p id="p1827717168446"><a name="p1827717168446"></a><a name="p1827717168446"></a>POST /v2.0/security-groups</p>
</td>
<td class="cellrowborder" valign="top" width="19.736842105263158%" headers="mcps1.1.4.1.2 "><p id="p1114023711130"><a name="p1114023711130"></a><a name="p1114023711130"></a>Creates a security group.</p>
</td>
<td class="cellrowborder" valign="top" width="27.631578947368418%" headers="mcps1.1.4.1.3 "><p id="p1849202313448"><a name="p1849202313448"></a><a name="p1849202313448"></a>vpc:securityGroups:create</p>
</td>
</tr>
<tr id="row6277111674416"><td class="cellrowborder" valign="top" width="52.63157894736842%" headers="mcps1.1.4.1.1 "><p id="p3277616144414"><a name="p3277616144414"></a><a name="p3277616144414"></a>PUT /v2.0/security-groups/{security_group_id}</p>
</td>
<td class="cellrowborder" valign="top" width="19.736842105263158%" headers="mcps1.1.4.1.2 "><p id="p14140113791317"><a name="p14140113791317"></a><a name="p14140113791317"></a>Updates a security group.</p>
</td>
<td class="cellrowborder" valign="top" width="27.631578947368418%" headers="mcps1.1.4.1.3 "><p id="p138071424124410"><a name="p138071424124410"></a><a name="p138071424124410"></a>vpc:securityGroups:update</p>
</td>
</tr>
<tr id="row13278116104413"><td class="cellrowborder" valign="top" width="52.63157894736842%" headers="mcps1.1.4.1.1 "><p id="p1927814164440"><a name="p1927814164440"></a><a name="p1927814164440"></a>DELETE /v2.0/security-groups/{security_group_id}</p>
</td>
<td class="cellrowborder" valign="top" width="19.736842105263158%" headers="mcps1.1.4.1.2 "><p id="p1141133731317"><a name="p1141133731317"></a><a name="p1141133731317"></a>Deletes a security group.</p>
</td>
<td class="cellrowborder" valign="top" width="27.631578947368418%" headers="mcps1.1.4.1.3 "><p id="p893572614442"><a name="p893572614442"></a><a name="p893572614442"></a>vpc:securityGroups:delete</p>
</td>
</tr>
<tr id="row627815168444"><td class="cellrowborder" valign="top" width="52.63157894736842%" headers="mcps1.1.4.1.1 "><p id="p10278116124410"><a name="p10278116124410"></a><a name="p10278116124410"></a>GET /v2.0/security-group-rules</p>
</td>
<td class="cellrowborder" valign="top" width="19.736842105263158%" headers="mcps1.1.4.1.2 "><p id="p2014111373133"><a name="p2014111373133"></a><a name="p2014111373133"></a>Queries a security group rule.</p>
</td>
<td class="cellrowborder" valign="top" width="27.631578947368418%" headers="mcps1.1.4.1.3 "><p id="p1358653024420"><a name="p1358653024420"></a><a name="p1358653024420"></a>vpc:securityGroupRules:get</p>
</td>
</tr>
<tr id="row13278171615443"><td class="cellrowborder" valign="top" width="52.63157894736842%" headers="mcps1.1.4.1.1 "><p id="p827816164443"><a name="p827816164443"></a><a name="p827816164443"></a>GET /v2.0/security-group-rules/{rules_security_groups_id}</p>
</td>
<td class="cellrowborder" valign="top" width="19.736842105263158%" headers="mcps1.1.4.1.2 "><p id="p414183714131"><a name="p414183714131"></a><a name="p414183714131"></a>Queries details about a security group rule.</p>
</td>
<td class="cellrowborder" valign="top" width="27.631578947368418%" headers="mcps1.1.4.1.3 "><p id="p134853214444"><a name="p134853214444"></a><a name="p134853214444"></a>vpc:securityGroupRules:get</p>
</td>
</tr>
<tr id="row1427916168445"><td class="cellrowborder" valign="top" width="52.63157894736842%" headers="mcps1.1.4.1.1 "><p id="p1627917161448"><a name="p1627917161448"></a><a name="p1627917161448"></a>POST /v2.0/security-group-rules</p>
</td>
<td class="cellrowborder" valign="top" width="19.736842105263158%" headers="mcps1.1.4.1.2 "><p id="p114120374136"><a name="p114120374136"></a><a name="p114120374136"></a>Creates a security group rule.</p>
</td>
<td class="cellrowborder" valign="top" width="27.631578947368418%" headers="mcps1.1.4.1.3 "><p id="p327293419443"><a name="p327293419443"></a><a name="p327293419443"></a>vpc:securityGroupRules:create</p>
</td>
</tr>
<tr id="row1927921619447"><td class="cellrowborder" valign="top" width="52.63157894736842%" headers="mcps1.1.4.1.1 "><p id="p19279141614412"><a name="p19279141614412"></a><a name="p19279141614412"></a>DELETE /v2.0/security-group-rules/{rules_security_groups_id}</p>
</td>
<td class="cellrowborder" valign="top" width="19.736842105263158%" headers="mcps1.1.4.1.2 "><p id="p014143715135"><a name="p014143715135"></a><a name="p014143715135"></a>Deletes a security group rule.</p>
</td>
<td class="cellrowborder" valign="top" width="27.631578947368418%" headers="mcps1.1.4.1.3 "><p id="p18887113614448"><a name="p18887113614448"></a><a name="p18887113614448"></a>vpc:securityGroupRules:delete</p>
</td>
</tr>
</tbody>
</table>

