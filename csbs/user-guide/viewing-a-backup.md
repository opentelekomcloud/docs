# Viewing a Backup<a name="EN-US_TOPIC_0056584642"></a>

After a backup job is delivered or completed, you can set search criteria to filter backups from the backup list and view backup details.

## Prerequisites<a name="section451227271115"></a>

A backup job has been created.

## View Backup Details<a name="section20267152222857"></a>

1.  Log in to the CSBS management console.
    1.  Log in to the management console.
    2.  Click  ![](figures/icon-region.png)  in the upper left corner of the management console and select a region and a project.
    3.  Click  ![](figures/icon-servicelist.png). Under  **Storage**, click  **Cloud Server Backup Service**.

2.  Click the  **Backups**  tab. Search for backups by filtering conditions.
    -   You can search for backups by selecting a status displayed in the upper right corner of the backup list.

        [Table 1](#table27644511104124)  describes each state.

        **Table  1**  State description

        <a name="table27644511104124"></a>
        <table><thead align="left"><tr id="row60378258104124"><th class="cellrowborder" valign="top" width="15.1%" id="mcps1.2.4.1.1"><p id="p58800757104124"><a name="p58800757104124"></a><a name="p58800757104124"></a>State</p>
        </th>
        <th class="cellrowborder" valign="top" width="16.79%" id="mcps1.2.4.1.2"><p id="p65240856104124"><a name="p65240856104124"></a><a name="p65240856104124"></a>State Attribute</p>
        </th>
        <th class="cellrowborder" valign="top" width="68.11%" id="mcps1.2.4.1.3"><p id="p50017955104124"><a name="p50017955104124"></a><a name="p50017955104124"></a>Description</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row3808446420388"><td class="cellrowborder" valign="top" width="15.1%" headers="mcps1.2.4.1.1 "><p id="p721585820388"><a name="p721585820388"></a><a name="p721585820388"></a>All statuses</p>
        </td>
        <td class="cellrowborder" valign="top" width="16.79%" headers="mcps1.2.4.1.2 "><p id="p4761360720388"><a name="p4761360720388"></a><a name="p4761360720388"></a>--</p>
        </td>
        <td class="cellrowborder" valign="top" width="68.11%" headers="mcps1.2.4.1.3 "><p id="p3149697320388"><a name="p3149697320388"></a><a name="p3149697320388"></a>All statuses of backups.</p>
        </td>
        </tr>
        <tr id="row24922559104124"><td class="cellrowborder" valign="top" width="15.1%" headers="mcps1.2.4.1.1 "><p id="p5461395104124"><a name="p5461395104124"></a><a name="p5461395104124"></a>Available</p>
        </td>
        <td class="cellrowborder" valign="top" width="16.79%" headers="mcps1.2.4.1.2 "><p id="p39719880104124"><a name="p39719880104124"></a><a name="p39719880104124"></a>A stable state</p>
        </td>
        <td class="cellrowborder" valign="top" width="68.11%" headers="mcps1.2.4.1.3 "><p id="p63193734104124"><a name="p63193734104124"></a><a name="p63193734104124"></a>A stable state of a backup after the backup is created</p>
        <p id="p31872695104124"><a name="p31872695104124"></a><a name="p31872695104124"></a>This state allows various operations.</p>
        </td>
        </tr>
        <tr id="row18418804104124"><td class="cellrowborder" valign="top" width="15.1%" headers="mcps1.2.4.1.1 "><p id="p15528122104124"><a name="p15528122104124"></a><a name="p15528122104124"></a>Creating</p>
        </td>
        <td class="cellrowborder" valign="top" width="16.79%" headers="mcps1.2.4.1.2 "><p id="p49818369104124"><a name="p49818369104124"></a><a name="p49818369104124"></a>An intermediate state</p>
        </td>
        <td class="cellrowborder" valign="top" width="68.11%" headers="mcps1.2.4.1.3 "><p id="p8756080104124"><a name="p8756080104124"></a><a name="p8756080104124"></a>An intermediate state of a backup from the start of a backup job to the completion of the backup job.</p>
        <p id="p11695863104124"><a name="p11695863104124"></a><a name="p11695863104124"></a>In this state, a progress bar is displayed indicating the backup progress. If the progress bar remains unchanged for a long time, an exception has occurred. Contact the administrator for support.</p>
        </td>
        </tr>
        <tr id="row38153904104124"><td class="cellrowborder" valign="top" width="15.1%" headers="mcps1.2.4.1.1 "><p id="p3458537104124"><a name="p3458537104124"></a><a name="p3458537104124"></a>Restoring</p>
        </td>
        <td class="cellrowborder" valign="top" width="16.79%" headers="mcps1.2.4.1.2 "><p id="p11706050104124"><a name="p11706050104124"></a><a name="p11706050104124"></a>An intermediate state</p>
        </td>
        <td class="cellrowborder" valign="top" width="68.11%" headers="mcps1.2.4.1.3 "><p id="p8665955104124"><a name="p8665955104124"></a><a name="p8665955104124"></a>An intermediate state when using the backup to restore data.</p>
        <p id="p10884734104124"><a name="p10884734104124"></a><a name="p10884734104124"></a>In this state, a progress bar is displayed indicating the restoration progress. If the progress bar remains unchanged for a long time, an exception has occurred. Contact the administrator for support.</p>
        </td>
        </tr>
        <tr id="row30853749104124"><td class="cellrowborder" valign="top" width="15.1%" headers="mcps1.2.4.1.1 "><p id="p16125727104124"><a name="p16125727104124"></a><a name="p16125727104124"></a>Deleting</p>
        </td>
        <td class="cellrowborder" valign="top" width="16.79%" headers="mcps1.2.4.1.2 "><p id="p31115530104124"><a name="p31115530104124"></a><a name="p31115530104124"></a>An intermediate state</p>
        </td>
        <td class="cellrowborder" valign="top" width="68.11%" headers="mcps1.2.4.1.3 "><p id="p37330014104124"><a name="p37330014104124"></a><a name="p37330014104124"></a>An intermediate state from the start of deleting the backup to the completion of deleting the backup.</p>
        <p id="p425806104124"><a name="p425806104124"></a><a name="p425806104124"></a>In this state, a progress bar is displayed indicating the deletion progress. If the progress bar remains unchanged for a long time, an exception has occurred. Contact the administrator for support.</p>
        </td>
        </tr>
        <tr id="row3832257104124"><td class="cellrowborder" valign="top" width="15.1%" headers="mcps1.2.4.1.1 "><p id="p41977438104124"><a name="p41977438104124"></a><a name="p41977438104124"></a>Error</p>
        </td>
        <td class="cellrowborder" valign="top" width="16.79%" headers="mcps1.2.4.1.2 "><p id="p44729307104124"><a name="p44729307104124"></a><a name="p44729307104124"></a>A stable state</p>
        </td>
        <td class="cellrowborder" valign="top" width="68.11%" headers="mcps1.2.4.1.3 "><p id="p66304096104124"><a name="p66304096104124"></a><a name="p66304096104124"></a>A backup enters the <strong id="b84235270692120"><a name="b84235270692120"></a><a name="b84235270692120"></a>Error</strong> state when an exception occurs when the backup is being used.</p>
        <p id="p59865958104124"><a name="p59865958104124"></a><a name="p59865958104124"></a>A backup in this state cannot be used for backup or restoration, and must be deleted manually. If manual deletion fails, contact the administrator for support.</p>
        </td>
        </tr>
        </tbody>
        </table>

    -   You can search for backups by selecting a time segment displayed in the upper right corner of the backup list.
    -   You can search for backups by server name, server ID, backup name, or backup ID. Click  ![](figures/icon-check.png)  to search for target backups.
    -   You can click  **Search by Tag**  in the upper right corner to search for backups by tag.

        -   On the  **Search by Tag**  tab page that is displayed, enter a tag key and a tag value \(must be among existing keys and values\) and click  ![](figures/icon-addtag.png). The added tag search criteria are displayed under the text boxes. Click  **Search**  in the lower right corner.
        -   You can use more than one tag for a combination search. Each time after a key and a value are entered, click  ![](figures/icon-addtag.png). The added tag search criteria are displayed under the text boxes. When more than one tag is added, they will be applied together for a combination search. A maximum of 10 tags can be added at the same time.
        -   You can click  **Reset**  in the upper right corner to reset the search criteria.

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >Backups whose backup type is  **Enhanced backup**  support Instant Restore. Backups whose backup type is  **Enhanced backup**  support Instant Restore. For details, see  [Instant Restore](basic-concepts.md#section181448505477).  


3.  Click  ![](figures/icon-down.png)  on the left of a backup name to view details about the backup.

## View Backup Space Usage<a name="section68951030125110"></a>

1.  Log in to the CSBS management console.
    1.  Log in to the management console.
    2.  Click  ![](figures/icon-region.png)  in the upper left corner of the management console and select a region and a project.
    3.  Click  ![](figures/icon-servicelist.png). Under  **Storage**, click  **Cloud Server Backup Service**.

2.  Click the  **Backups**  tab and then the number indicating the used storage space can be viewed in the backup overview.  [Figure 1](#fig635912816013)  provides an example.

    **Figure  1**  Backup overview<a name="fig635912816013"></a>  
    ![](figures/backup-overview.png "backup-overview")

3.  In the displayed dialog box, view the storage space usage.

    Each record indicates an ECS. In the displayed dialog box,  **Backups**  specifies the number of backups created for an ECS and  **Total Backup Capacity \(GB\)**  specifies the capacity used by the ECS's backups in total.

    **Figure  2**  Storage space usage<a name="fig12592151016138"></a>  
    ![](figures/storage-space-usage.png "storage-space-usage")


