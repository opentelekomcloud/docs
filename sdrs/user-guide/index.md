# Storage Disaster Recovery Service User Guide

-   [Overview]
    -   [SDRS Introduction](sdrs-introduction.md)
    -   [Product Advantages](product-advantages.md)
    -   [Application Scenarios](application-scenarios.md)
    -   [Limitations](limitations.md)
    -   [Supported DR Scenarios](supported-dr-scenarios.md)
    -   [Compatible Applications and Versions](compatible-applications-and-versions.md)
    -   [Relationships with Other Services](relationships-with-other-services.md)
    -   [Basic Concepts]
        -   [SDRS Basic Concepts](sdrs-basic-concepts.md)
        -   [Region and AZ](region-and-az.md)


-   [Getting Started]
    -   [Configuring Cross-AZ DR for Servers]
        -   [Configuration Process](configuration-process.md)
        -   [Step 1: Create a Protection Group](step-1-create-a-protection-group.md)
        -   [Step 2: Create a Protected Instance](step-2-create-a-protected-instance.md)
        -   [Step 3: Enable Protection](step-3-enable-protection.md)

    -   [Performing a DR Drill](performing-a-dr-drill.md)

-   [Management]
    -   [Managing Protection Groups]
        -   [Disabling Protection](disabling-protection.md)
        -   [Performing a Planned Failover](performing-a-planned-failover.md)
        -   [Performing a Failover](performing-a-failover.md)
        -   [Performing Reprotection](performing-reprotection.md)
        -   [Deleting a Protection Group](deleting-a-protection-group.md)

    -   [Managing Protected Instances]
        -   [Modifying Specifications of a Protected Instance](modifying-specifications-of-a-protected-instance.md)
        -   [Deleting a Protected Instance](deleting-a-protected-instance.md)
        -   [Creating a Replication Pair](creating-a-replication-pair.md)
        -   [Attaching a Replication Pair](attaching-a-replication-pair.md)
        -   [Detaching a Replication Pair](detaching-a-replication-pair.md)
        -   [Adding a NIC](adding-a-nic.md)
        -   [Deleting a NIC](deleting-a-nic.md)
        -   [Managing Protected Instance Tags](managing-protected-instance-tags.md)

    -   [Managing Replication Pairs]
        -   [Creating a Replication Pair](creating-a-replication-pair-0.md)
        -   [Expanding Replication Pair Capacity](expanding-replication-pair-capacity.md)
        -   [Deleting a Replication Pair](deleting-a-replication-pair.md)

    -   [Managing DR Drills]
        -   [Performing a DR Drill](performing-a-dr-drill-1.md)
        -   [Deleting a DR Drill](deleting-a-dr-drill.md)

    -   [Interconnecting with CTS ]
        -   [Key SDRS Operations Recorded by CTS](key-sdrs-operations-recorded-by-cts.md)
        -   [Viewing Traces](viewing-traces.md)


-   [FAQs]
    -   [What Is DR?](what-is-dr.md)
    -   [What Are the Highlights of SDRS?](what-are-the-highlights-of-sdrs.md)
    -   [What Are RPO and RTO?](what-are-rpo-and-rto.md)
    -   [What Are the Differences Between DR and Backup?](what-are-the-differences-between-dr-and-backup.md)
    -   [What Can I Do When the EIP Cannot Be Pinged After I Perform a Planned Failover for a Protection Group Containing a SUSE Server?](what-can-i-do-when-the-eip-cannot-be-pinged-after-i-perform-a-planned-failover-for-a-protection-grou.md)
    -   [What Can I Do If the NIC Names of the DR Drill Server and Production Site Server Are Different?](what-can-i-do-if-the-nic-names-of-the-dr-drill-server-and-production-site-server-are-different.md)
    -   [What Can I Do If hostname of the Production Site Server and DR Site Server Are Different After a Planned Failover or Failover?](what-can-i-do-if-hostname-of-the-production-site-server-and-dr-site-server-are-different-after-a-pla.md)
    -   [Why NICs of DR Site Servers Are Not Displayed After I Perform a Failover?](why-nics-of-dr-site-servers-are-not-displayed-after-i-perform-a-failover.md)
    -   [What Are the Precautions If the Production Site Server Uses the Key Login Mode?](what-are-the-precautions-if-the-production-site-server-uses-the-key-login-mode.md)

-   [Glossary](glossary.md)

