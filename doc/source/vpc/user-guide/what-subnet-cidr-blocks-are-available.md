# What Subnet CIDR Blocks Are Available?<a name="vpc_faq_0006"></a>

The subnet CIDR blocks must be included in the VPC CIDR blocks. The VPC CIDR blocks are  **10.0.0.0/8–24**,  **172.16.0.0/12–24**, and  **192.168.0.0/16–24**. The subnet CIDR blocks must be within these CIDR blocks, and the allowed block size of a subnet is between the netmask of its VPC CIDR block and /29 netmask.

