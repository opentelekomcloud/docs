# What Is Health Check Grace Period?<a name="EN-US_TOPIC_0141570909"></a>

Generally, instances automatically added to an AS group in scaling actions require sufficient warm-up time \(grace period\) to pass the ELB health check. Therefore, if you add a load balancer to an AS group and set the health check method to ELB health check, once instances are added to the AS group and become enabled, the AS group will check the status of instances after the grace period. The health check grace period is 600s by default.

