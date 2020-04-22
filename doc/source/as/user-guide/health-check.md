# Health Check<a name="EN-US_TOPIC_0042018390"></a>

A health check removes abnormal instances from an AS group. Then, AS adds new instances to the AS group so that the number of instances is the same as the expected number. There are two types of AS group health check.

-   **ECS health check**: checks ECS running status. If an ECS is stopped or deleted, it is considered as abnormal.  **ECS health check**  is the default health check mode for an AS group. The AS group periodically uses the check result to determine the running status of every instance in the AS group. If the health check result shows that an ECS is faulty, AS removes the ECS from the AS group.
-   **ELB health check**: determines ECS running status using a load balancing listener. If the AS group uses load balancers, the health check method can also be  **ELB health check**. If you add multiple load balancers to an AS group, the ECS is considered normal only when all load balancers detect that the ECS status is normal. If any load balancer detects that the ECS is abnormal, the ECS will be removed from the AS group.

In both  **ECS health check**  and  **ELB health check**  modes, AS removes abnormal instances from AS groups. However, the removed instances are processed differently in the two modes:

For instances automatically added to an AS group during scaling actions, AS removes and deletes them. For instances manually added to an AS group, AS only removes them from the AS group.

When an AS group is disabled, checking instance health status continues. However, AS will not remove instances.

Generally, instances automatically added to an AS group in scaling actions require sufficient warm-up time \(grace period\) to pass the ELB health check. Therefore, if you add a load balancer to an AS group and set the health check method to ELB health check, the AS group will check the status of instances only after their grace periods end.

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>The grace period starts only after an instance is added to the AS group and enabled. The default grace period is 10 minutes.  

