# Typical Application Scenarios<a name="vpc_qs_0002"></a>

A VPC provides an isolated virtual network for ECSs. You can configure and manage the network as required.

-   If your ECSs do not need to access the Internet or need to access the Internet using a specified IP address with limited bandwidth on the default network segment, for example, the ECSs functioning as the database or server nodes for deploying a website, you can configure a VPC for the ECSs by following the instructions described in  [Configuring a VPC for ECSs That Do Not Require Internet Access](configuring-a-vpc-for-ecss-that-do-not-require-internet-access.md).
-   If your ECSs need to access the Internet, you can configure EIPs for them. For example, the ECSs functioning as the service nodes for deploying a website need to be accessed by users over the Internet. Then, you can configure a VPC for these ECSs by following the instructions provided in  [Configuring a VPC for ECSs That Access the Internet Using EIPs](configuring-a-vpc-for-ecss-that-access-the-internet-using-eips.md).

