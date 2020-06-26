# Are My RDS DB Instances Available When Scaling?<a name="rds_faq_0016"></a>

Currently, you can scale up storage space and change the CPU and memory of an RDS DB instance.

-   When scaling storage space, RDS DB instances are available and services are not affected. However, you cannot delete or reboot DB instances that are being scaled.
-   During the change of the CPU or memory, the network is intermittently disconnected for one or two times in seconds.

