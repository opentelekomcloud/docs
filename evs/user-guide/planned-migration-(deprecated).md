# Planned Migration \(Deprecated\)<a name="evs_01_0030"></a>

## Scenarios<a name="section5572733817211"></a>

Production servers and production disks belong to the primary AZ, and DR servers and DR disks belong to the secondary AZ. Users can make API calls to perform a planned migration, for example, perform a primary/secondary AZ switchover for the replication consistency group and enable the servers and disks in the secondary AZ.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>EVS replication APIs have been deprecated. If you need to use the replication function, see  [Storage Disaster Recovery Service User Guide](https://docs.otc.t-systems.com/en-us/usermanual/sdrs/en-us_topic_0125068221.html)  and  [Storage Disaster Recovery Service API Reference](https://docs.otc.t-systems.com/en-us/api/sdrs/en-us_topic_0108184470.html).  

## Prerequisites<a name="section3033620895717"></a>

-   The production server status is normal, and the deployed services are running properly.
-   The target production servers have been temporarily stopped.
-   The replication status of the replication consistency group is  **active**, which means that data synchronization in all EVS replication pairs of the replication consistency group is complete.

## Procedure<a name="section55139435172113"></a>

1.  Perform a primary/secondary AZ switchover for the replication consistency group.

    For details, see  **Performing a Primary/Secondary Switchover for a Replication Consistency Group**  in the  _Elastic Volume Service API Reference_.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >Performing a primary/secondary switchover for a replication consistency group takes a relative long period of time, and it takes about 10 seconds for the system to respond the request.  

2.  If Elastic Load Balancing \(ELB\) or EIPs are used, unbind the ELB or EIPs with the production servers and bind them to the DR servers.
    -   For details about ELB, see  **Backend Server \(Enhanced Load Balancer\)**  in the  _Elastic Load Balancing User Guide_.
    -   For details about EIPs, see  **Elastic IP Address**  in the  _Virtual Private Cloud User Guide_.

3.  Verify that the DR server OSs can be normally started, deployed services are available, and the data is complete.

