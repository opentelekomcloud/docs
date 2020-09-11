# EVS Replication \(Deprecated\)<a name="evs_01_0020"></a>

## What Is EVS Replication<a name="section29902489215657"></a>

If your services or disk data demands high reliability, you can use the cross-AZ replication feature provided by EVS. You can create a disaster recovery \(DR\) disk for a production disk in another AZ and use the production disk and DR disk to create an EVS replication pair. The data on these two disks will be consistent in real time. If a large number of physical resources in the primary AZ are faulty due to force majeure, you can use the DR disks in the secondary AZ to ensure the service availability and continuity.

-   The server with the production disk attached is referred to as the production server, and the AZ containing the production server is the primary AZ.
-   The server with the DR disk attached is referred to as the DR server, and the AZ containing the DR server is the secondary AZ.

## Application Scenarios<a name="section8885956105220"></a>

The replication function helps address your following needs:

-   Data in DR disks is consistent with that in production disks in real time. You can perform a planned migration based on your service needs, that is, migrate the services from the primary AZ to the secondary AZ without data loss.
-   If large-scale physical resources in the primary AZ become faulty due to force majeure, you can use DR disks in the secondary AZ to lower the impact exerted on services.

## Usage Instructions<a name="section30695838172854"></a>

For more use methods of EVS replication, see  [Managing EVS Replication \(Deprecated\)](managing_evs_replication).

>![](/images/icon-note.gif) **NOTE:**   
>EVS replication APIs have been deprecated. If you need to use the replication function, see  [Storage Disaster Recovery Service User Guide](https://docs.otc.t-systems.com/en-us/usermanual/sdrs/en-us_topic_0125068221.html)  and  [Storage Disaster Recovery Service API Reference](https://docs.otc.t-systems.com/en-us/api/sdrs/en-us_topic_0108184470.html).  

