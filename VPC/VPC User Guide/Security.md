## Overview


The public cloud system provides firewalls and security groups to monitor and
improve VPC security. The differences between firewalls and security groups are
as follows.

Differences between security groups and firewalls

**Table 1** Differences between security groups and firewalls

<table>
      <tr>
         <th>Security Group</th>
         <th>Firewall</th>
        
      
     </tr>
     <tr>
        <td>Operates at the ECS level (first layer of defense).</td>
         <td>Operates at the subnet level (second layer of defense).</td>
     
     </tr>
   	 <tr>
        <td>Only supports allow rules.</td>
         <td>Supports allow rules, deny rules, and reject rules.</td>
       
     </tr>

	<tr>
        <td>If multiple security group rules conflict, the overlapping part of these rules takes effect.</td>
         <td>If multiple firewall rules conflict, the rule with the smallest index value takes effect.</td>
      
       
     </tr>
	<tr>
        <td>By default, you must select a security group when creating an ECS. The selected security group takes effect for that ECS.</td>
         <td>You cannot select a firewall when creating a subnet. You must create a firewall, associate subnets with the firewall, add inbound and outbound network rules, and enable the firewall. Then, the firewall takes effect for the associated subnets and ECSs in the subnets.</td>
       
       
     </tr>
	<tr>
        <td>Only supports packet filtering based on the 3-tuple (protocol, port, and peer IP address).</td>
         <td>Only supports packet filtering based on the 5-tuple (protocol, source port, destination port, source IP address, and destination IP address).
		</td>
       
	</table>
