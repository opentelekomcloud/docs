# Modifying Specifications of a Protected Instance<a name="EN-US_TOPIC_0110273585"></a>

## Scenarios<a name="section1484312317349"></a>

If the specifications of an existing protected instance cannot meet the service requirements, you can perform steps provided in this section to modify the server specifications, including the vCPU and memory. 

The following scenarios may involve:

-   Modifying the specifications of both the production and DR site servers
-   Modifying the specifications of the production site server only
-   Modifying the specifications of the DR site server only

## **Prerequisites**<a name="section8218163017179"></a>

-   The protection group is in the  **Available**  or  **Protecting state**.
-   The protected instance is in the  **Available**,  **Protecting**, or  **Modifying specifications failed**.
-   Servers of which the specifications to be modified are stopped.

## Procedure<a name="section12404242193417"></a>

1.  Log in to the management console.
2.  Click  **Service List**  and choose  **Storage**  \>  **Storage Disaster Recovery Service**.

    The  **Storage Disaster Recovery Service**  page is displayed.

3.  In the pane of the protection group for which the protected instance specifications are to be modified, click  **Protected Instances**.

    The operation page for the protection group is displayed.

4.  On the  **Protected Instances**  tab, locate the row containing the target protected instance, click  **More**  in the  **Operation**  column, and choose  **Modify Specifications of the Production Site Server**  or  **Modify Specifications of the DR Site Server**  from the drop-down list. 

    **Figure  1**  Modifying specifications<a name="fig18486161131816"></a>  
    ![](figures/modifying-specifications.png "modifying-specifications")

5.  In the  **Modify Specifications**  dialog box, select new server type, vCPU, and memory specifications.
6.  \(Optional\) If you need to modify the specifications of both the production site server and DR site server, select  **Modify the specifications of both the production and DR site servers**. After you select this item, the system will modify the specifications of both the production site server and DR site server to the same specifications.

    **Figure  2**  Modifying the specifications of both the production site server and DR site server<a name="fig9965423103213"></a>  
    ![](figures/modifying-the-specifications-of-both-the-production-site-server-and-dr-site-server.png "modifying-the-specifications-of-both-the-production-site-server-and-dr-site-server")

    >![](/images/icon-note.gif) **NOTE:**   
    >This item is deselected by default, indicating that the system modifies the specifications of only the production site server or DR site server.  

7.  Click  **OK**.

    To ensure proper server running, do not perform any operations to the servers during specification modifications. 


