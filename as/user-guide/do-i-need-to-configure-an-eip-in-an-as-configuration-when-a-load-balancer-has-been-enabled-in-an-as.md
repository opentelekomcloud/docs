# Do I Need to Configure an EIP in an AS Configuration When A Load Balancer Has Been Enabled in an AS Group?<a name="EN-US_TOPIC_0141570912"></a>

No. If you have enabled a load balancer in an AS group, you do not have to configure an EIP in the AS configuration. The system automatically adds instances in the AS group to the load balancer. These instances will provide services via the EIP bound to the load balancer.

