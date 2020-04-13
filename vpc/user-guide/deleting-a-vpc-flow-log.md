# Deleting a VPC Flow Log<a name="FlowLog_0005"></a>

## Scenarios<a name="section15598193716333"></a>

Delete a VPC flow log that is not required. Deleting a VPC flow log will not delete the existing flow log records in LTS.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>If related NIC \(ECS\) for a VPC flow log has been deleted, the flow log is automatically deleted. However, the flow log records are not deleted.  

## Procedure<a name="section7359352124511"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  On the console homepage, under  **Network**, click  **Virtual Private Cloud**.
4.  In the navigation pane on the left, choose  **VPC Flow Logs**.
5.  Locate the row that contains the VPC flow log to be deleted and click  **Delete**  in the  **Operation**  column.

    **Figure  1**  Deleting a VPC flow log<a name="fig11695911145"></a>  
    ![](figures/deleting-a-vpc-flow-log.png "deleting-a-vpc-flow-log")

6.  Click  **Yes**  in the displayed dialog box.

