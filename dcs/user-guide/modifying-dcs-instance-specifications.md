# Modifying DCS Instance Specifications<a name="en-us_topic_0063519673"></a>

## Scenario<a name="section8135151"></a>

On the DCS console, you can modify a DCS Redis instance to the desired specifications.

>![](public_sys-resources/icon-notice.gif) **NOTICE:** 
>-   After you change the specifications of a Proxy Cluster DCS instance, you cannot restore the files backed up before the modification. You are advised to back up your data as soon as possible after changing the specifications.
>-   It takes 5 to 30 minutes to change the specifications of single-node or master/standby DCS instances. Changing the specifications of a Proxy Cluster DCS instance takes a longer time because data must be redistributed in the cluster. During the specification modification, services are interrupted for seconds. You are advised to modify the specifications during off-peak hours.
>-   Normally during the specification modification, single-node, master/standby, and Proxy Cluster DCS instances can be read from and written into. However, writing data into single-node or master/standby instances may be temporarily unsupported until the specification modification is completed.

## Prerequisites<a name="section6107499"></a>

The DCS instance you want to change the specification for is in the  **Running**  state.

## Procedure<a name="section28432151594"></a>

1.  Log in to the management console.
2.  Click  ![](figures/project.png) in the upper left corner of the management console and select a region and a project.
3.  Click  **Service List**, and choose **Database** \> **Distributed Cache Service**  to launch the DCS console.
4.  In the navigation pane, choose  **Cache Manager**.
5.  Choose  **More**  \>  **Modify Specifications**  in the same row as the DCS instance.
6.  On the  **Modify Specifications**  page, select the desired specification.

    The maximum storage space is 64 GB for single-node and master/standby instances, and 512 GB for Proxy Cluster instances.

7.  Click  **Next**.
8.  Click  **Submit**.

    It takes 5 to 30 minutes to scale up a DCS instance. After scale-up is successful, the DCS instance enters the  **Running**  state.

    The  **Background Tasks **page then appears. On this page, you can view the scale-up status. For more information, see [Managing Background Tasks](managing-background-tasks.md).

    >![](public_sys-resources/icon-note.gif) **NOTE:** 
    >-   If the specification modification of a single-node DCS instance fails, the instance is temporarily unavailable for use. The specification remains unchanged. Some management operations \(such as parameter configuration and specification modification\) are temporarily not supported. After the specification modification is completed in the backend, the instance changes to the new specification and becomes available for use again.
    >-   If the specification modification of a master/standby or Proxy Cluster DCS instance fails, the instance is still available for use with its original specifications. Some management operations \(such as parameter configuration, backup, restoration, and specification modification\) are temporarily not supported. Remember not to read or write more data than allowed by the original specifications; otherwise, data loss may occur.
    >-   After the specification modification is successful, the new specification of the instance takes effect.


