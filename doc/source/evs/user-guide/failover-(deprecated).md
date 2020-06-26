# Failover \(Deprecated\)<a name="evs_01_0031"></a>

## Scenarios<a name="section5572733817211"></a>

When the production servers and disks in the primary AZ become faulty due to force majeure, users can make API calls to perform a failover for the replication consistency group and enable the DR servers and disks in the secondary AZ to ensure the service continuity.

>![](/images/icon-note.gif) **NOTE:**   
>EVS replication APIs have been deprecated. If you need to use the replication function, see  [Storage Disaster Recovery Service User Guide](https://docs.otc.t-systems.com/en-us/usermanual/sdrs/en-us_topic_0125068221.html)  and  [Storage Disaster Recovery Service API Reference](https://docs.otc.t-systems.com/en-us/api/sdrs/en-us_topic_0108184470.html).  

## Prerequisites<a name="section3159922995753"></a>

Confirm with the customer service that servers and disks in the production AZ are faulty, and the deployed services are unavailable.

## Procedure<a name="section55139435172113"></a>

1.  Perform a failover for the replication consistency group.

    For details, see  **Performing a Failover for a Replication Consistency Group**  in the  _Elastic Volume Service API Reference_.

2.  If Elastic Load Balancing \(ELB\) or EIPs are used, unbind the ELB or EIPs with the production servers and bind them to the DR servers.
    -   For details about ELB, see  **Backend Server \(Enhanced Load Balancer\)**  in the  _Elastic Load Balancing User Guide_.
    -   For details about EIPs, see  **Elastic IP Address**  in the  _Virtual Private Cloud User Guide_.

3.  Verify that the DR server OSs can be normally started, deployed services are available, and the data is complete.

