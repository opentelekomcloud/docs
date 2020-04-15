# Updating a Replication Consistency Group \(Deprecated\)<a name="evs_01_0029"></a>

## Scenarios<a name="section41376901204426"></a>

Currently, EVS replication pairs can be added to or removed from replication consistency groups through APIs only. For details, see  **Updating a Replication Consistency Group**  in the  _Elastic Volume Service API Reference_.

If an EVS replication pair needs to be deleted after it has been added to a replication consistency group, remove this EVS replication pair from the group first, delete this EVS replication pair, and then delete the production disk and DR disk. For details, see  **Deleting an EVS Replication Pair**  and  **Deleting a Replication Consistency Group**  in the  _Elastic Volume Service API Reference_.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>EVS replication APIs have been deprecated. If you need to use the replication function, see  [Storage Disaster Recovery Service User Guide](https://docs.otc.t-systems.com/en-us/usermanual/sdrs/en-us_topic_0125068221.html)  and  [Storage Disaster Recovery Service API Reference](https://docs.otc.t-systems.com/en-us/api/sdrs/en-us_topic_0108184470.html).  

## Prerequisites<a name="section3033620895717"></a>

The replication consistency group status is  **available**.

## Procedure<a name="section18493003204426"></a>

1.  Pause the replication consistency group you need to update.

    For details, see  **Pausing a Replication Consistency Group**  in the  _Elastic Volume Service API Reference_.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >Pausing a replication consistency group means that the data synchronization within the group is paused. Therefore, the data between production disks and DR disks will be temporarily inconsistent and needs to be synchronized after the replication consistency group update is complete.  

2.  Update the replication consistency group, that is, add EVS replication pairs to or remove EVS replication pairs from the group.

    For details, see  **Updating a Replication Consistency Group**  in the  _Elastic Volume Service API Reference_.

3.  Synchronize the data of a replication consistency group, which means that the data of all EVS replication pairs within the group is synchronized.

    For details, see  **Synchronizing a Replication Consistency Group**  in the  _Elastic Volume Service API Reference_.

4.  Query the data synchronization status of the replication consistency group.

    For details, see  **Querying Details About a Replication Consistency Group**  in the  _Elastic Volume Service API Reference_.

    When the replication status of the replication consistency group changes to  **active**, the data in all EVS replication pairs of this group has been synchronized.


