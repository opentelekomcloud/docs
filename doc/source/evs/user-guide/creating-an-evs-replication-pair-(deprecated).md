# Creating an EVS Replication Pair \(Deprecated\)<a name="evs_01_0027"></a>

## Scenarios<a name="section5572733817211"></a>

Currently, users need to make API calls to create EVS replication pairs. Each server can have multiple EVS replication pairs. For details, see  **EVS Replication Pair**  in the  _Elastic Volume Service API Reference_.

If a production disk needs to be deleted after it has been used together with its DR disk to create an EVS replication pair, delete the EVS replication pair first and then delete the production disk and DR disk. For details, see  **Deleting an EVS Replication Pair**  in the  _Elastic Volume Service API Reference_.

>![](/images/icon-note.gif) **NOTE:**   
>EVS replication APIs have been deprecated. If you need to use the replication function, see  [Storage Disaster Recovery Service User Guide](https://docs.otc.t-systems.com/en-us/usermanual/sdrs/en-us_topic_0125068221.html)  and  [Storage Disaster Recovery Service API Reference](https://docs.otc.t-systems.com/en-us/api/sdrs/en-us_topic_0108184470.html).  

## Procedure<a name="section55139435172113"></a>

1.  Create an EVS replication pair using the production disk and DR disk.

    For details, see  **Creating an EVS Replication Pair**  in the  _Elastic Volume Service API Reference_.

2.  Query the details about the EVS replication pair.

    For details, see  **Querying Details About an EVS Replication Pair**  in the  _Elastic Volume Service API Reference_.

    If the EVS replication pair status changes to  **available**, the creation is successful.

3.  Take note of the production disk ID, DR disk ID, EVS replication pair ID, and the primary site of the EVS replication pair, which is the AZ containing the production disk.

    >![](/images/icon-note.gif) **NOTE:**   
    >Two EVS disks form an EVS replication pair. Therefore, the production disk ID, DR disk ID, and EVS replication pair ID can be used to identify disks and the EVS replication pair.  


