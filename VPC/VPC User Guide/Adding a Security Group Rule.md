## Adding a Security Group Rule
#### Scenarios

The default security group rule allows all outgoing data packets. ECSs in a
security group can access each other without the need to add rules. After a
security group is created, you can create different access rules for the
security group to protect the ECSs that are added to this security group.

To access ECSs in a security group from external resources, create an inbound
rule for the security group, for example:

-   To access a remote Windows ECS using MSTSC, add an inbound rule in which
    **Protocol** is set to **TCP** and **Port Range** is set to **3389**.

-   To access a remote Linux ECS using SSH, add an inbound rule in which
    **Protocol** is set to **TCP** and **Port Range** is set to **22**.

-   Set **Source** to the IP address segment containing the IP address of the
    server accommodating the target ECS.

	Allocate ECSs that have different Internet access policies to different security groups.

	![](figure/NOTE.png)

	The default source IP address **0.0.0.0/0** indicates that all IP addresses can access ECSs in the security group.

#### Procedure

2.  Log in to the management console.

3.  On the console homepage, under **Network**, click **Virtual Private Cloud**.

4.  In the navigation pane on the left, click **Security Group**.

5.  On the **Security Group** page, click the security group name.

6.  On the displayed page showing security group details, click **Add Rule**.

	The **Add Rule** dialog box is displayed.

1.  On the page shown in <a href="#figure1">Figure 1</a>, add a security group rule.

    <a name="figure1">**Figure 1**</a> Add Rule

    ![](figure/2.2.5-Adding-a-Security-Group-Rule.png)


	 **Table 1** Parameter description

	<table>
      <tr>
         <th>Parameter</th>
         <th>Description</th>
         <th>Example Value</th>         
      
     </tr>
     <tr>
        <td>Protocol</td>
         <td>Specifies the network protocol for which the security group rule takes effect. The value can be TCP, UDP, ICMP, or ANY.</td>
         <td>TCP</td>
       
     </tr>
     <tr>
            <td>Transfer Direction</td>
         <td>Specifies the transfer direction of the traffic for which the security group rule takes effect. The value can be Inbound or Outbound.
		Inbound traffic flows to ECSs in a security group, and outbound traffic flows from ECSs in a security group.

		</td>
         <td>Inbound</td>
       
      
     </tr> 
     <tr>
           <td>Port Range</td>
         <td>Specifies the port or port range for which the security group rule takes effect. The value ranges from 1 to 65535.</td>
         <td>22 or 22-30</td>
       
       
        
     </tr> 
     <tr>
            <td>Source</td>
         <td>Specifies either the source IP address and subnet mask or the source security group for which the security group rule takes effect. This parameter is required when Transfer Direction is set to Inbound.
			For example:
			xxx.xxx.xxx.xxx/32 (IP address)
			xxx.xxx.xxx.0/24 (subnet)
			0.0.0.0/0 (any IP address)
</td>
         <td>0.0.0.0/0
		default
		</td>


	</table>
	Destination can be set to Security Group or IP Address. The details are as follows:

	- IP Address: This rule takes effect for the specified IP addresses. 0.0.0.0/0 indicates that this rule takes effect for all IP addresses.



	- Security Group: This rule takes effect for all ECSs in the selected security group.


1.  Click **OK**.
