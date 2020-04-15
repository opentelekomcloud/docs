# EVS Replication Operation Procedure \(Deprecated\)<a name="evs_01_0060"></a>

For the EVS replication concepts, see  [EVS Replication \(Deprecated\)](evs-replication-(deprecated).md). This chapter describes the basic functions and operations of EVS replication.  [Figure 1](#en-us_topic_0080271663_fig1868775620529)  shows the operation procedure.

1.  Performing pre-configuration operations before using EVS replication: Create DR servers, configure the virtual IP address for servers, and collect server information.
2.  Creating EVS replication pairs: Specify production disks in the primary AZ and DR disks in the secondary AZ to create EVS replication pairs.
3.  Creating replication consistency groups: Specify EVS replication pairs to create replication consistency groups.
4.  After EVS replication pairs and replication consistency groups are created, you can perform the following operations as required:

    -   Updating a replication consistency group:
        1.  Pause the replication consistency group if the group status is not paused.
        2.  Add or remove EVS replication pairs from the replication consistency group.
        3.  Synchronize the data in EVS replication pairs of the replication consistency group.

    -   Performing a planned migration: Switch the secondary AZ to the primary AZ and enable resources such as the DR servers and DR disks in the secondary AZ.
    -   Performing a failover:
        1.  If a fault occurred in the primary AZ, switch the secondary AZ to the primary AZ and enable the resources such as the DR servers and DR disks in the secondary AZ.
        2.  After the fault in the faulty AZ has been restored, reprotect the replication consistency group to enable the restored resources in the faulty AZ to function as DR servers and DR disks.

    -   Expanding EVS disks in a replication consistency group: Expand EVS disks in one or multiple EVS replication pairs of the replication consistency group.

    **Figure  1**  Operation procedure \(EVS replication\)<a name="en-us_topic_0080271663_fig1868775620529"></a>  
    ![](figures/operation-procedure-(evs-replication).png "operation-procedure-(evs-replication)")

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >EVS replication APIs have been deprecated. If you need to use the replication function, see  [Storage Disaster Recovery Service User Guide](https://docs.otc.t-systems.com/en-us/usermanual/sdrs/en-us_topic_0125068221.html)  and  [Storage Disaster Recovery Service API Reference](https://docs.otc.t-systems.com/en-us/api/sdrs/en-us_topic_0108184470.html).  


