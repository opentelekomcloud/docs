# Supported DR Scenarios<a name="sdrs_pro_0008"></a>

## Production Site Is Faulty<a name="section387518476565"></a>

-   Description

    The production site has a fault. Services at the production site are affected and cannot be restored using the failover function. 

    **Figure  1**  Production site being faulty<a name="fig16793129143812"></a>  
    ![](figures/production-site-being-faulty.png "production-site-being-faulty")


-   Solution

    You can use the DR drill function to create DR drill servers at the DR site to resume the services.

    For more information about the DR drill function, see  [Performing a DR Drill](performing-a-dr-drill.md).


## DR Site Is Faulty<a name="section8466142612574"></a>

-   Description

    The DR site has a fault. Services at the production site are not affected, but the planned failover cannot be performed. 

    **Figure  2**  DR site being faulty<a name="fig12161743402"></a>  
    ![](figures/dr-site-being-faulty.png "dr-site-being-faulty")

-   Solution

    Contact the customer service to obtain technical support.


## Replication Link Is Faulty<a name="section107495164323"></a>

-   Description

    The replication link between the production site and DR site becomes faulty. Services at the production site are not affected, but the planned failover cannot be performed. 

    **Figure  3**  Replication link being faulty<a name="fig14944168432"></a>  
    ![](figures/replication-link-being-faulty.png "replication-link-being-faulty")

-   Solution

    You do not need to perform any operations. The DR protection will automatically restore once the replication link fault is rectified.


## Storage Resource at the Production Site Is Faulty<a name="section199475412343"></a>

-   Description

    Services at the production site are affected because the storage resource at the production site has a fault.

    **Figure  4**  Storage resource at the production site is faulty<a name="fig1743420214458"></a>  
    ![](figures/storage-resource-at-the-production-site-is-faulty.png "storage-resource-at-the-production-site-is-faulty")

-   Solution

    Use the failover function to start resources such as servers and disks at the DR site to resume the services.

    For more information about the failover function, see  [Performing a Failover](performing-a-failover.md).


## Storage Resource at the DR Site Is Faulty <a name="section1518717206394"></a>

-   Description

    The storage resource at the DR site has a fault. Services at the production site are not affected, but the planned failover or failover cannot be performed. 

    **Figure  5**  Storage resource at the DR site being faulty <a name="fig756316184494"></a>  
    ![](figures/storage-resource-at-the-dr-site-being-faulty.png "storage-resource-at-the-dr-site-being-faulty")

-   Solution

    Contact the customer service to obtain technical support.


