## Creating a VPC
### Scenarios

A VPC provides an isolated virtual network for ECSs. You can configure and
manage the network as required.

To use a VPC, first create it by following the steps provided in this section.
Then, create subnets, security groups, and VPNs, and assign EIPs by following
the steps provided in subsequent sections based on your actual network
requirements.

#### Procedure

2.  Log in to the management console.

3.  On the console homepage, under **Network**, click **Virtual Private Cloud**.

4.  On the **Dashboard** page, click **Create VPC**.

	On the displayed **Create VPC** page shown in <a href="#figure1">Figure 1</a>, set the parameters as prompted.

	<a name="figure1">**Figure 1**</a> Create VPC

	![](figure/2.2.2Creating_a_vpc-01.png)

	 **Table 1**  Parameter description

	<table>
      <tr>
         <th>Parameter</th>
         <th>Description</th>
         <th>Example Value</th>         
      
     </tr>
     <tr>
        <td>Name</td>
         <td>Specifies the VPC name.</td>
         <td>VPC-001</td>
       
     </tr>
     <tr>
            <td>VPC CIDR</td>
         <td>Specifies the Classless Inter-Domain Routing (CIDR) block for the VPC. The CIDR block of a subnet can be the same as the CIDR block for the VPC (for a single subnet in the VPC) or a subset (for multiple subnets in the VPC).
		The following CIDR blocks are supported:
		10.0.0.0/8–24
		172.16.0.0/12–24
		192.168.0.0/16–24
		</td>
         <td>192.168.0.0/16</td>
       
      
     </tr> 
     <tr>
           <td>Name</td>
         <td>Specifies the subnet name.</td>
         <td>Subnet</td>
       
       
        
     </tr> 
     <tr>
            <td>CIDR</td>
         <td>Specifies the CIDR block for the subnet. This value must be within the VPC CIDR range.</td>
         <td>192.168.0.0/24</td>
       
  
     </tr>
    <tr>
            <td>Gateway</td>
         <td>Specifies the gateway address of the subnet.</td>
         <td>192.168.0.1</td>
       
  
     </tr>


	</table>



1. The external DNS server address is used by default. If you need to change the DNS server address, click **Show Advanced Settings** and configure the DNS server addresses. You must ensure that the configured DNS server addresses are available.

3.  Click **Create Now**.
