# Step 3: Access OBS<a name="vpcep_02_0304"></a>

## Scenarios<a name="section336734914324"></a>

This section describes how to access OBS using a VPN connection or a direct connection.

## Procedure<a name="section372772717323"></a>

1.  <a name="li146041853163516"></a>In the VPC endpoint list, locate the VPC endpoint for connecting to DNS and click its ID to view the private IP address.

    **Figure  1**  Summary of the VPC endpoint<a name="fig1234818262310"></a>  
    ![](figures/summary-of-the-vpc-endpoint-6.png "summary-of-the-vpc-endpoint-6")

2.  Add DNS records on the DNS server at your local data center to forward requests for resolving OBS domain names to the VPC endpoint for accessing DNS.

    The methods of configuring DNS forwarding rules vary depending on operating systems. For details, see the DNS software operation documents.

    This step uses the common DNS software Bind as an example to configure forwarding rules in the UNIX operating system as follows:

    In file  **/etc/named.conf**, add the DNS forwarder configuration and set  **forwarders**  to the private IP address of the VPC endpoint for accessing DNS.

    **options \{**

    **forward only;**

    **forwarders\{ **_xx.xx.xx.xx_**;\};**

    **\};**

    >![](public_sys-resources/icon-note.gif) **NOTE:** 
    >-   If no DNS server is available at your local data center, add the private IP address of the VPC endpoint in file  **/etc/resolv.conf**.
    >-   _xx.xx.xx.xx_  is the private IP address described in step  [1](#li146041853163516).

3.  Configure a DNS route from your local data center to the VPN gateway or Direct Connect gateway.

    _xx.xx.xx.xx_  indicates the private IP address of the VPC endpoint. To access DNS using a VPN connection or a direct connection, you need to ensure that traffic from your local data center to DNS is directed to the VPN gateway or Direct Connect gateway.

    Configure a permanent route at your local data center and specify the Direct Connect or VPN gateway as the next hop for accessing DNS.

    **route -p add xx.xx.xx.xx mask 255.255.255.255 xxx.xxx.xxx.xxx**

    >![](public_sys-resources/icon-note.gif) **NOTE:** 
    >-   _xx.xx.xx.xx_  is the private IP address described in step  [1](step-3-access-obs.md#li146041853163516).
    >-   _xxx.xxx.xxx.xxx_  indicates the IP address of the Direct Connect or VPN gateway created at your local data center.

4.  Configure an OBS route from the local data center to the VPN or Direct Connect gateway.

    The CIDR block of the VPC endpoint for accessing OBS is 100.125.0.0/16. To access OBS using a VPN connection or direct connection, you need to ensure that traffic from your local data center to OBS is directed to the VPN gateway or Direct Connect gateway.

    Configure a permanent route at your local data center and specify the Direct Connect or VPN gateway as the next hop for accessing OBS.

    **route -p add 100.125.0.0 mask 255.255.0.0 xxx.xxx.xxx.xxx**

    >![](public_sys-resources/icon-note.gif) **NOTE:** 
    >_xxx.xxx.xxx.xxx_  indicates the IP address of the Direct Connect or VPN gateway created at your local data center.

5.  At the local data center, run the following command to verify the connectivity with OBS:

    **telnet xx.xx.xx.xx**

    >![](public_sys-resources/icon-note.gif) **NOTE:** 
    >_xx.xx.xx.xx_  indicates the private IP address described in  [1](#li146041853163516).


