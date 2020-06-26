# Is an SSL Connection to a DB Instance Interrupted After a Primary/Standby Switchover or Failover Occurs?<a name="rds_faq_0111"></a>

For DB instances connected through SSL, a primary/standby switchover or failover does not interrupt the connection because the SSL certificate is still valid for both the primary and standby DB instances.

