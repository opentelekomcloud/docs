# Expanding EVS Disks in a Replication Consistency Group \(Deprecated\)<a name="evs_01_0043"></a>

## Scenarios<a name="section21137677162916"></a>

Users can make an API call to expand the EVS disks in one or multiple EVS replication pairs of a replication consistency group. In such an expansion operation, two EVS disks in one EVS replication pair are expanded together.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>The  **status**  and  **replication\_status**  values of the replication consistency group remain unchanged before and after capacity expansion.  
>If the expansion fails, contact customer service to locate and rectify the fault. After the fault is rectified, expand the disks again.  
>EVS replication APIs have been deprecated. If you need to use the replication function, see  [Storage Disaster Recovery Service User Guide](https://docs.otc.t-systems.com/en-us/usermanual/sdrs/en-us_topic_0125068221.html)  and  [Storage Disaster Recovery Service API Reference](https://docs.otc.t-systems.com/en-us/api/sdrs/en-us_topic_0108184470.html).  

## Prerequisites<a name="section55795759162916"></a>

-   The  **status**  value of replication consistency group must be  **available**, which means that the group status is normal.
-   The  **replication\_status**  value of the replication consistency group is not  **error**.

## Procedure<a name="section24189094163418"></a>

1.  Make an API call to expand the EVS disks in one or multiple EVS replication pairs of the replication consistency group.

    For details, see  **Expanding EVS Disks a Replication Consistency Group**  in the  _Elastic Volume Service API Reference_.


