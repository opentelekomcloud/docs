# Modifying DCS Instance Specification<a name="EN-US_TOPIC_0237964723"></a>

## Scenario<a name="section28358649"></a>

On the DCS console, you can scale up DCS instances to desired specifications.

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>-   DCS instances in cluster mode do not support scale-up.  
>-   It takes 5 to 30 minutes to scale up a DCS instance. To minimize the impact of any unexpected results, we recommend scaling up your instance during off-peak periods.  
>-   During scale-up of single-node DCS instances, you cannot read from or write to DCS, but during scale-up of master/standby DCS instances, you can read from or write to DCS.  
>-   After successful scale-up, the scaled DCS instances are billed based on new specifications.  

## Prerequisites<a name="section53901255"></a>

The DCS instance you want to change the specification for is in the  **Running**  state.

## Procedure<a name="section15349251"></a>

1.  Log in to the management console.
2.  Click![](figures/icon-region.png)  in the upper left corner of the management console and select a region and a project.
3.  Click  **Service List**, and choose  **Database**  \>  **Distributed Cache Service**  to launch the DCS console.
4.  In the navigation pane, choose  **Cache Manager**.
5.  Choose  **More**  \>  **Modify Specification**  in the same row as the DCS instance.
6.  On the  **Modify Specification**  page, select the desired specification.

    The maximum storage space for both single-node and master/standby instances is 64 GB.

7.  Click  **Submit**.

    It takes 5 to 30 minutes to scale up a DCS instance. After scale-up is successful, the DCS instance enters the  **Running**  state.

    The  **Background Task Management**  page then appears. On this page, you can view the scale-up status. For more information, see  [Managing Background Tasks](managing-background-tasks.md).

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   If the specification modification of a single-node DCS instance fails, the instance is temporarily unavailable for use. The specification remains unchanged. Some management operations \(such as parameter configuration and specification modification\) are temporarily not supported. After the specification modification is completed in the backend, the instance changes to the new specification and becomes available for use again.  
    >-   If the specification modification of a master/standby or cluster DCS instance fails, the instance is still available for use with its original specifications. Some management operations \(such as parameter configuration, backup, restoration, and specification modification\) are temporarily not supported. Remember not to read or write more data than allowed by the original specifications; otherwise, data loss may occur.  
    >-   After the specification modification is successful, the new specification of the instance takes effect.  


