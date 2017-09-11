## Overview

If you need to access ECSs in a VPC over the Internet to perform maintenance
operations on the ECSs, you can follow the procedure shown in <a href="#figure1">Figure 1</a> to configure a VPN. For example, you can configure a VPN to enable a website administrator to access ECSs functioning as service nodes in the VPC over the Internet.

<a name="figure1">**Figure 1**</a>  Configuring the network

![](figure/906db686e07c9743b936ef116ad13046.png)

**Table 1** shows the procedure for configuring the network.

<table>
      <tr>
         <th>Task</th>
         <th>Description</th>
         
      
     </tr>
     <tr>
        <td>Create a VPC.</td>
         <td>This task is mandatory.
	You must configure required parameters to create a VPC. The created VPC comes with a default subnet you specified.
	After the VPC is created, you can create other required network resources in the VPC based on your service requirements.
  </td>
         
       
     </tr>
    
           <td>Create another subnet for the VPC.</td>
         <td>This task is optional.
	If you need another subnet besides the default one, you can create a subnet in the VPC.
	The new subnet is used to assign IP addresses to NICs added to the ECS.
	</td>
 
       
       
        
     </tr> 
     <tr>
            <td>Create a VPN.</td>
         <td>his task is mandatory.
	You can create an IPsec VPN to set up a secure and isolated communication tunnel between your data center and cloud services.

	</td>
      
       
  
     </tr>
    <tr>
            <td>Create a security group.</td>
         <td>This task is mandatory.
		You can create a security group and add ECSs in the VPC to the security group to improve ECS access security.
		After a security group is created, it has a default rule. The default security group rule allows all outgoing data packets. ECSs in a security group can access each other without the need to add rules. If the default rule meets your service requirements, you do not need to add rules to the security group.
		</td>

       
  
     </tr>

	<tr>
            <td>Add a security group rule.</td>
         <td>This task is optional.
		After a security group is created, it has a default rule. The default security group rule allows all outgoing data packets. ECSs in a security group can access each other without the need to add rules. If the default rule cannot meet your service requirements, you can add a security group rule.
	</td>
       
  
     </tr>



	</table>