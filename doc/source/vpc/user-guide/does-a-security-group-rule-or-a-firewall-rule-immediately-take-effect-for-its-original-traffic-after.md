# Does a Security Group Rule or a Firewall Rule Immediately Take Effect for Its Original Traffic After It Is Modified?<a name="vpc_faq_0074"></a>

No. After a security group rule or a firewall rule is modified, the new rule will not immediately take effect for its original traffic. You need to interrupt the original traffic for about 120 seconds for the new rule to take effect for the traffic.

