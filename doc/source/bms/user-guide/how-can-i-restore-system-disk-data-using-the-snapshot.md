# How Can I Restore System Disk Data Using the Snapshot?<a name="EN-US_TOPIC_0078771807"></a>

You can create snapshots of the BMS system disk on the EVS console periodically. To restore the system disk data, mount the target system disk to the  **sda**  mount point.

1.  Power off the BMS.
    1.  Log in to the management console.
    2.  Under  **Computing**, click  **Bare Metal Server**.

        The BMS console is displayed.

    3.  Locate the target BMS and click  **Stop**.

2.  Detach the system disk.
    1.  Click the BMS after it is powered off.

        The page showing details of the BMS is displayed.

    2.  Locate the target system disk and click  **Detach**.

        In the displayed dialog box, click  **OK**.

3.  Attach the system disk.
    1.  On the page showing the BMS details, click  **Attach Disk**.

        The  **Attach Disk**  page is displayed.

    2.  Select the system disk and mount point  **/dev/sda**, and click  **Attach Disk**.

        In the displayed dialog box, click  **OK**.



