# Why Does Not the ELB Health Check Used by an AS Group Take Effect Immediately?<a name="EN-US_TOPIC_0113772108"></a>

Generally, instances automatically added to an AS group in scaling actions require sufficient warm-up time \(grace period\) to pass the ELB health check. Therefore, if you add a load balancer to an AS group and set the health check method to ELB health check, the AS group will check the status of instances only after their grace periods end.

The grace period starts only after an instance is added to the AS group and enabled. The default grace period is 10 minutes.

