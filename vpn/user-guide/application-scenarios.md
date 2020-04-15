# Application Scenarios<a name="vpn_01_0003"></a>

With the VPN between the VPC and your traditional data center, you can easily use the ECSs and block storage resources provided by the cloud platform. Applications can be migrated to the cloud and additional web servers can be deployed to increase the computing capacity on a network. In this way, a hybrid cloud is built, which reduces IT O&M costs and protects enterprise core data from being leaked.

The VPN service allows you to set up site-to-site VPN connections or VPN connections from one site to multiple sites.

## Site-to-site VPN connection<a name="section14587411103213"></a>

You can set up a VPN to connect a local data center to a VPC, thus building a hybrid cloud.  [Figure 1](#fig234964913366)  shows a site-to-site VPN connection.

**Figure  1**  Site-to-site VPN connection<a name="fig234964913366"></a>  
![](figures/site-to-site-vpn-connection.png "site-to-site-vpn-connection")

## VPN connection from one site to multiple sites<a name="section6241644113713"></a>

You can also set up a VPN to connect multiple local data centers to a VPC, thus building a hybrid cloud.  [Figure 2](#fig8311841131918)  shows a VPN connection from one site to multiple sites.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>The subnet CIDR blocks of each site involved in the VPN connection cannot overlap.  

**Figure  2**  VPN connection from one site to multiple sites<a name="fig8311841131918"></a>  
![](figures/vpn-connection-from-one-site-to-multiple-sites.png "vpn-connection-from-one-site-to-multiple-sites")

