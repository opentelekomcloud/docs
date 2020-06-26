# How Can I Identify Data Corruption?<a name="rds_faq_0011"></a>

-   Data tempering

    Lots of security measures are provided to ensure that only authenticated users have permissions to perform operations on database table records. The SSH protocol is inaccessible to users. Database tables can be accessed only through the specified database service port.

    Verifying package during primary/standby synchronization can prevent data tampering. MySQL uses the InnoDB storage engine to prevent data damage.

-   DB instance servers may be powered off suddenly, causing database page corruption and database rebooting failures.

    If the primary DB instance is faulty, RDS switches to the standby DB instance within 1 to 5 minutes to provide services for you. Databases cannot be accessed during failover. You must set automatic reconnections between the applications and RDS to prevent the applications from becoming unavailable due to the failover.


