# Suggestions on Container Performance Tuning<a name="obs_03_0005"></a>

OBS \(compatible with OpenStack Swift\) updates the same metadata when processing concurrent PUT or DELETE operations on objects in a container. Performance of these operations is compromised due to metadata conflicts. For concurrent GET operations on objects in a container, however, performance is not compromised. For concurrent PUT or DELETE object operations per container, the Transactions Per Second \(TPS\) supported by OBS \(compatible with OpenStack Swift\) is 15. However, the performance of PUT an object is constrained by the TPS only when the object size is small. When the object size is relatively large, container performance has nothing to do with the TPS because PUT operations in this case mainly process object data and seldom update metadata. In general, container performance is inversely proportional to the object size in PUT operations. According to test results, when the average size of concurrently uploaded objects exceeds 10 MB, the impact of concurrent metadata updates on operation performance can be ignored. For DELETE operations on objects, the performance of the container is constrained regardless of object sizes.

>![](/images/icon-note.gif) **NOTE:**   
>The preceding PUT, DELETE, and GET operations refer to those performed on different objects in a container. If concurrent operations are performed on the same object, container performance is determined by processing capabilities of one or several specific disks.  

## Performance Tuning for Intensive PUT or DELETE Operations<a name="section19704042175710"></a>

In typical application scenarios of OBS \(compatible with OpenStack Swift\), such as archive and backup, there are a large number of concurrent PUT operations. To tune container performance, particularly in scenarios with small objects, the following methods are recommended:

1.  Balancing loads among multiple containers

    Upload backup data to different containers in OBS \(compatible with OpenStack Swift\) to eliminate data hotspots caused by concurrent PUT operations on the same container. As independent logical entities in OBS \(compatible with OpenStack Swift\), containers maintain their own metadata. Therefore, performance of one container is not affected by concurrent operations performed on other containers. In addition, data uploaded to different containers can be logically separated, which improves data listing and query performance.

2.  Controlling the number of concurrent operations on a container

    The performance of a container does not necessarily increase with the concurrent processing capability of that container. In contrast, when the concurrent processing capability of a container is excessively high, the performance of that container may deteriorate because OBS \(compatible with OpenStack Swift\) is busy handling conflicts in concurrent operations. In OBS \(compatible with OpenStack Swift\), you are advised to set the concurrency number of a container to 15. This value has been proved by tests of uploading small objects concurrently to a container. If the object size is large, you can increase this value to a larger one based on the container's TPS to achieve optimal container performance.

3.  Uploading small objects after packaging them

    In scenarios with a large number of small objects, to improve container performance and storage space utilization, upload small objects after packaging them.

4.  Using random object names

    You can use random object names to reduce the impact of concurrency conflicts on a single node. For example, in a typical scenario of log archiving, the names of objects to be uploaded may be as follows:

    ```
    yourcontainer/obslog/20140610-01.log.tar.gz
    yourcontainer/obslog/20140610-02.log.tar.gz
    yourcontainer/obslog/20140610-03.log.tar.gz
    yourcontainer/obslog/20140610-04.log.tar.gz
    ...
    yourcontainer/obslog/20140611-01.log.tar.gz
    yourcontainer/obslog/20140611-02.log.tar.gz
    yourcontainer/obslog/20140611-03.log.tar.gz
    yourcontainer/obslog/20140611-04.log.tar.gz
    ```

    The names of these objects have the same prefix. When being uploaded concurrently, these objects are likely to be routed to the same node. To eliminate data hotspots and improve container performance, add random prefixes to object names. For example, a 6-digit hexadecimal string is added to each of the following object names:

    ```
    yourcontainer/6ac3e2-obslog/20140610-01.log.tar.gz
    yourcontainer/b425da-obslog/20140610-02.log.tar.gz
    yourcontainer/17fe36obslog/20140610-03.log.tar.gz
    yourcontainer/ac96b4-obslog/20140610-04.log.tar.gz
    ...
    yourcontainer/95d36e-obslog/20140611-01.log.tar.gz
    yourcontainer/45c2d-obslog/20140611-02.log.tar.gz
    yourcontainer/ea2cfe-obslog/20140611-03.log.tar.gz
    yourcontainer/ba36c2-obslog/20140611-04.log.tar.gz
    ```

    >![](/images/icon-note.gif) **NOTE:**   
    >This method is applicable only when the number of objects in a container is large enough.  


