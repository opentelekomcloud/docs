# Stopping BMSs<a name="EN-US_TOPIC_0140740387"></a>

## Scenarios<a name="section89140121163"></a>

You can stop BMSs in  **Running**  state.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>If you choose to forcibly stop a BMS, services running on the BMS will be stopped. Before performing this operation, ensure that you have saved files on the BMS.  

## Procedure<a name="section1534145814619"></a>

1.  Log in to the management console. 
2.  Under  **Computing**, click  **Bare Metal Server**.

    The BMS console is displayed.

3.  Locate the row that contains the target BMS, click  **More**  in the  **Operation**  column, and select  **Stop**  from the drop-down list. To stop multiple BMSs, select them and click  **Stop**  at the top of the BMS list.
4.  In the displayed dialog box, click  **Yes**.

After a BMS is stopped, its status becomes  **Stopped**.

You can perform the following operations only when the BMS is stopped:

-   [Detaching the System Disk](detaching-a-disk.md)
-   [Creating an Image](creating-a-private-image-from-a-bms.md)
-   [Rebuilding a BMS](rebuilding-a-bms.md)

