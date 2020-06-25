# Why NICs of DR Site Servers Are Not Displayed After I Perform a Failover?<a name="sdrs_faq_0004"></a>

SDRS performs planned failovers or failovers for protection groups. After a planned failover or failover, the production site and DR site exchange. When the production site is functional, users can perform a planned failover according to plans. When a fault occurs at the production site, users need to perform a failover.

-   During a planned failover, NICs of the production site servers and DR site servers will exchange. In this way, servers can be accessed using the same IP addresses and MAC addresses after the planned failover.
-   During a failover, production site servers do not work properly, NICs of the production site servers will be migrated to the DR site servers. The primary NICs of the DR site servers will enter the to-be-used state. Therefore, after a failover, the original production site servers will not have NICs. When users perform reprotection for the protection group after the original production site servers restore, the primary NICs in the to-be-used state detached from the original DR site servers will be attached to the original production site servers. Then, the NICs of the production site servers and DR site servers are exchanged.

