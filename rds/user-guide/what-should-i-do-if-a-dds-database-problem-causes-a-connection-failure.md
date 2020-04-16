# What Should I Do If a DDS Database Problem Causes a Connection Failure?<a name="rds_faq_0022"></a>

Check in order whether the following problems are occurring on the RDS DB instance.

1.  The RDS DB instance is not properly connected.

    Solution: Check the connection mode. The RDS can be accessed only through an ECS in the same VPC.

2.  The maximum number of connections has been reached.

    Solution: Check whether the CPU usage and the number of current connections are normal by using the RDS resource monitoring function. If either of them reaches the maximum, then reboot, disconnect, or change the CPU and memory of the DB instance.

3.  DB instance is abnormal. For example, the RDS DB instance has failed to reboot, the RDS system has become faulty, or the RDS DB instance or table is locked.

    Solution: Reboot the RDS DB instance to see if the problem is resolved. If the problem persists, contact post-sales technical support.


