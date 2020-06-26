# Do Applications Need to Support Reconnecting to the RDS DB Instance Automatically?<a name="rds_faq_0024"></a>

It is recommended that your applications support automatic reconnections to the database. After a database reboot, your applications will automatically reconnect to the database to increase service availability and continuity.

In addition, you are advised to set your applications to connect to the database using a long connection to reduce resource consumption and improve performance.

