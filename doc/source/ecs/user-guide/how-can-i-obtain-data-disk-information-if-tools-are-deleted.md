# How Can I Obtain Data Disk Information If Tools Are Deleted?<a name="EN-US_TOPIC_0029806525"></a>

If Tools are uninstalled from a Linux ECS in a non-PVOPS system, data disks cannot be identified. In such a case, you can obtain information about these data disks by creating a new ECS and attaching the data disks of the original ECS to the new ECS. The procedure is as follows:

1.  Log in to the management console and create a new ECS.

    >![](/images/icon-note.gif) **NOTE:**   
    >The new ECS must be located in the same AZ and have the same parameter settings as the original ECS.  

2.  \(Optional\) On the  **Elastic Cloud Server**  page, locate the row containing the original ECS, click  **More**  in the  **Operation**  column, and select  **Stop**. On the  **Stop ECS**  page, select  **Forcibly stop the preceding ECSs**  and  **Yes**  and click  **OK**  to forcibly stop the original ECS.

    Manually refresh the  **Elastic Cloud Server**  page. The original ECS is stopped once the  **Status**  changes to  **Stopped**.

    >![](/images/icon-note.gif) **NOTE:**   
    >The ECSs running certain OSs support online data disk detaching. If your OS supports this feature, you can detach data disks from the running ECS.  

3.  Click  ![](figures/icon-unfold.png)  to view information about the data disks attached to the original ECS.

    >![](/images/icon-note.gif) **NOTE:**   
    >If the original ECS has multiple data disks attached, repeat steps  [4](#li3454282161441)  to  [6](#li3628995162045)  to attach each data disk to the new ECS.  

4.  <a name="li3454282161441"></a>Click a data disk.

    The  **Elastic Volume Service**  page is displayed.

5.  Select the data disk to be detached and click  **Detach**  in the  **Operation**  column. On the  **Detach Disk**  page, select the original ECS and click  **OK**  to detach the data disk from the original ECS.

    Manually refresh the  **Elastic Volume Service**  page. The data disk is detached from the original ECS once the  **Status**  changes to  **Available**.

6.  <a name="li3628995162045"></a>Select the detached data disk and click  **Attach**  in the  **Operation**  column. On the  **Attach Disk**  page, click the new ECS, select a device name, and click  **OK**  to attach the data disk to the new ECS.

    Manually refresh the EVS list. The data disk is attached to the new ECS once the  **Status**  value changes to  **In-use**. You can then log in to the management console and view information about the data disk of the new ECS.


