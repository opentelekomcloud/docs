## Overview

If your ECSs need to access the Internet, for example, the ECSs functioning as
the service nodes for deploying a website, you can follow the procedure shown in
<a href="#figure1">Figure 1</a> to bind EIPs to the ECSs.

<a name="figure1">**Figure 1**</a> Configuring the network

![](figure/f126be838da636cc4d5079aef48ac456.png)

**Table 1** Configuration process description
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
     
     <tr>
           <td>Create another subnet for the VPC.</td>
         <td>This task is optional.
	If you need another subnet besides the default one, you can create a subnet in the VPC.
	The new subnet is used to assign IP addresses to NICs added to the ECS.
	</td>
 
       
       
        
     </tr> 
     <tr>
            <td>Assign an EIP and bind it to an ECS.</td>
         <td>This task is mandatory.
		You can assign an EIP and bind it to an ECS to enable the ECS to access the Internet.
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

