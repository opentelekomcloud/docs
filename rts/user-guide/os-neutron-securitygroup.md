# OS::Neutron::SecurityGroup<a name="EN-US_TOPIC_0088407166"></a>

A resource for managing Neutron security groups.

Security groups are sets of IP filter rules that are applied to an instances networking. They are project specific, and project members can edit the default rules for their group and add new rules sets. All projects have a "default" security group, which is applied to instances that have no other security group defined.

## Optional Properties<a name="section971064175514"></a>

<a name="table72146101563"></a>
<table><thead align="left"><tr id="row1688693814919"><th class="cellrowborder" valign="top" width="31%" id="mcps1.1.3.1.1"><p id="p9215410105619"><a name="p9215410105619"></a><a name="p9215410105619"></a><strong id="b99841417184712"><a name="b99841417184712"></a><a name="b99841417184712"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="69%" id="mcps1.1.3.1.2"><p id="p102152108569"><a name="p102152108569"></a><a name="p102152108569"></a><strong id="b14985111715471"><a name="b14985111715471"></a><a name="b14985111715471"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row788683818498"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p621513107562"><a name="p621513107562"></a><a name="p621513107562"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p9553281"><a name="p9553281"></a><a name="p9553281"></a>Description of the security group.</p>
<p id="p18870670"><a name="p18870670"></a><a name="p18870670"></a>String value expected.</p>
<p id="p35618305"><a name="p35618305"></a><a name="p35618305"></a>Can be updated without replacement.</p>
</td>
</tr>
<tr id="row988611382492"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p182152109562"><a name="p182152109562"></a><a name="p182152109562"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p66510437"><a name="p66510437"></a><a name="p66510437"></a>A string specifying a symbolic name for the security group, which is not required to be unique.</p>
<p id="p61723024"><a name="p61723024"></a><a name="p61723024"></a>String value expected.</p>
<p id="p18636310"><a name="p18636310"></a><a name="p18636310"></a>Can be updated without replacement.</p>
</td>
</tr>
<tr id="row188643813496"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p821551075611"><a name="p821551075611"></a><a name="p821551075611"></a>rules</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p33146107"><a name="p33146107"></a><a name="p33146107"></a>List of security group rules.</p>
<p id="p29879508"><a name="p29879508"></a><a name="p29879508"></a>List value expected.</p>
<p id="p480124"><a name="p480124"></a><a name="p480124"></a>Can be updated without replacement.</p>
<p id="p4321123"><a name="p4321123"></a><a name="p4321123"></a>Defaults to "[]".</p>
<p id="p38890115"><a name="p38890115"></a><a name="p38890115"></a><em id="i24500989"><a name="i24500989"></a><a name="i24500989"></a>List contents:</em></p>
<a name="ul63091573"></a><a name="ul63091573"></a><ul id="ul63091573"><li>*<p id="p10143804"><a name="p10143804"></a><a name="p10143804"></a>Map value expected.</p>
<p id="p24185379"><a name="p24185379"></a><a name="p24185379"></a>Can be updated without replacement.</p>
<p id="p16341824"><a name="p16341824"></a><a name="p16341824"></a><em id="i33206990"><a name="i33206990"></a><a name="i33206990"></a>Map properties:</em></p>
<a name="ul1036615160579"></a><a name="ul1036615160579"></a><ul id="ul1036615160579"><li>direction<p id="p12376122135818"><a name="p12376122135818"></a><a name="p12376122135818"></a>The direction in which the security group rule is applied. For a compute instance, an ingress security group rule matches traffic that is incoming (ingress) for that instance. An egress rule is applied to traffic leaving the instance.</p>
<p id="p13376521135815"><a name="p13376521135815"></a><a name="p13376521135815"></a>String value expected.</p>
<p id="p183771421125816"><a name="p183771421125816"></a><a name="p183771421125816"></a>Can be updated without replacement.</p>
<p id="p11377152175810"><a name="p11377152175810"></a><a name="p11377152175810"></a>Defaults to "ingress".</p>
<p id="p2378122185817"><a name="p2378122185817"></a><a name="p2378122185817"></a>Allowed values: ingress, egress</p>
</li><li>ethertype<p id="p10592200"><a name="p10592200"></a><a name="p10592200"></a>Ethertype of the traffic.</p>
<p id="p28220940"><a name="p28220940"></a><a name="p28220940"></a>String value expected.</p>
<p id="p52661876"><a name="p52661876"></a><a name="p52661876"></a>Can be updated without replacement.</p>
<p id="p4194840"><a name="p4194840"></a><a name="p4194840"></a>Defaults to "IPv4".</p>
<p id="p2722164035812"><a name="p2722164035812"></a><a name="p2722164035812"></a>Allowed values: IPv4, IPv6</p>
</li><li>port_range_max<p id="p7711627"><a name="p7711627"></a><a name="p7711627"></a>The maximum port number in the range that is matched by the security group rule. The port_range_min attribute constrains the port_range_max attribute. If the protocol is ICMP, this value must be an ICMP type.</p>
<p id="p2295787"><a name="p2295787"></a><a name="p2295787"></a>Integer value expected.</p>
<p id="p20662084"><a name="p20662084"></a><a name="p20662084"></a>Can be updated without replacement.</p>
<p id="p12100752155819"><a name="p12100752155819"></a><a name="p12100752155819"></a>The value must be in the range 0 to 65535, include 1 and 65535.</p>
</li><li>port_range_min<p id="p4031547"><a name="p4031547"></a><a name="p4031547"></a>The minimum port number in the range that is matched by the security group rule. If the protocol is TCP or UDP, this value must be less than or equal to the value of the port_range_max attribute. If the protocol is ICMP, this value must be an ICMP type.</p>
<p id="p36283926"><a name="p36283926"></a><a name="p36283926"></a>Integer value expected.</p>
<p id="p58119881"><a name="p58119881"></a><a name="p58119881"></a>Can be updated without replacement.</p>
<p id="p76831056599"><a name="p76831056599"></a><a name="p76831056599"></a>The value must be in the range 0 to 65535, include 1 and 65535.</p>
</li><li>protocol<p id="p11977491"><a name="p11977491"></a><a name="p11977491"></a>The protocol that is matched by the security group rule. Valid values include tcp, udp, and icmp.</p>
<p id="p40688558"><a name="p40688558"></a><a name="p40688558"></a>String value expected.</p>
<p id="p4741115155914"><a name="p4741115155914"></a><a name="p4741115155914"></a>Can be updated without replacement.</p>
</li><li>remote_group_id<p id="p65677640"><a name="p65677640"></a><a name="p65677640"></a>The remote group ID to be associated with this security group rule. If no value is specified then this rule will use this security group for the remote_group_id. The remote mode parameter must be set to "remote_group_id".</p>
<p id="p54227851"><a name="p54227851"></a><a name="p54227851"></a>String value expected.</p>
<p id="p3231525125915"><a name="p3231525125915"></a><a name="p3231525125915"></a>Can be updated without replacement.</p>
</li><li>remote_ip_prefix<p id="p44847690"><a name="p44847690"></a><a name="p44847690"></a>The remote IP prefix (CIDR) to be associated with this security group rule.</p>
<p id="p976031"><a name="p976031"></a><a name="p976031"></a>String value expected.</p>
<p id="p139361234125911"><a name="p139361234125911"></a><a name="p139361234125911"></a>Can be updated without replacement.</p>
</li><li>remote_mode<p id="p28401526"><a name="p28401526"></a><a name="p28401526"></a>Whether to specify a remote group or a remote IP prefix.</p>
<p id="p54287150"><a name="p54287150"></a><a name="p54287150"></a>String value expected.</p>
<p id="p18822307"><a name="p18822307"></a><a name="p18822307"></a>Can be updated without replacement.</p>
<p id="p35183038"><a name="p35183038"></a><a name="p35183038"></a>Defaults to "remote_ip_prefix".</p>
<p id="p688224417595"><a name="p688224417595"></a><a name="p688224417595"></a>Allowed values: remote_ip_prefix, remote_group_id</p>
</li></ul>
</li></ul>
</td>
</tr>
</tbody>
</table>

## HOT Syntax<a name="section4852135055518"></a>

```
heat_template_version: 2014-10-16
...
resources:
  ...
  the_resource:
    type: OS::Neutron::SecurityGroup
    properties:
      description: String
      name: String
      rules: [{"remote_group_id": String, "port_range_max": Integer, "remote_ip_prefix": String, "protocol": String, "port_range_min": Integer, "ethertype": String, "direction": String, "remote_mode": String}, {"remote_group_id": String, "port_range_max": Integer, "remote_ip_prefix": String, "protocol": String, "port_range_min": Integer, "ethertype": String, "direction": String, "remote_mode": String}, ...]
```

