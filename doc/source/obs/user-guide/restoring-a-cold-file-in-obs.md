# Restoring a Cold File in OBS<a name="obs_03_0418"></a>

## Background Information<a name="sc77505e4e8f54d77be74167432ce207f"></a>

The Cold storage class is applicable to archiving rarely-accessed \(such as once a year\) data. The application scenarios include data archiving and long-term data retention for backup, allowing users to safely store data at a low price. However, it can take up to hours to restore data from the Cold storage class.

If an object in the Cold storage class is being restored, you cannot suspend or delete the restoration task.

You cannot restore an object that is in the  **Restoring**  state.

## Procedure<a name="s2d1f733f72264226ae6c4e207a585caf"></a>

1.  Log in to OBS Browser.
2.  Click the bucket in which the file that you want to restore resides. The object list is displayed.
3.  Click the restore icon next to the object that you want to restore. Alternatively, you can select an object and click the restore icon on the top of the object list.

    **Table  1**  Parameters for restoring objects

    <a name="t11e13a9301aa4729b85b9e6a3f461360"></a>
    <table><thead align="left"><tr id="obs_03_0320_row20202933164622"><th class="cellrowborder" valign="top" width="23.68%" id="mcps1.2.3.1.1"><p id="obs_03_0320_p25824852164622"><a name="obs_03_0320_p25824852164622"></a><a name="obs_03_0320_p25824852164622"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="76.32%" id="mcps1.2.3.1.2"><p id="obs_03_0320_p11438256164622"><a name="obs_03_0320_p11438256164622"></a><a name="obs_03_0320_p11438256164622"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="obs_03_0320_row63287564164622"><td class="cellrowborder" valign="top" width="23.68%" headers="mcps1.2.3.1.1 "><p id="obs_03_0320_p26019055164622"><a name="obs_03_0320_p26019055164622"></a><a name="obs_03_0320_p26019055164622"></a>Validity Period</p>
    </td>
    <td class="cellrowborder" valign="top" width="76.32%" headers="mcps1.2.3.1.2 "><p id="obs_03_0320_p27168719164622"><a name="obs_03_0320_p27168719164622"></a><a name="obs_03_0320_p27168719164622"></a>Time duration when an object remains in the <strong id="obs_03_0320_b105713101419"><a name="obs_03_0320_b105713101419"></a><a name="obs_03_0320_b105713101419"></a>Restored</strong> state after being restored. The timing starts as the object restoration is completed. The value is an integer ranging from 1 to 30 (days). The default value is 30.</p>
    <p id="obs_03_0320_p43191881164622"><a name="obs_03_0320_p43191881164622"></a><a name="obs_03_0320_p43191881164622"></a>For example, you set <strong id="obs_03_0320_b39195835171853"><a name="obs_03_0320_b39195835171853"></a><a name="obs_03_0320_b39195835171853"></a>Validity Period</strong> to <strong id="obs_03_0320_b17218197171853"><a name="obs_03_0320_b17218197171853"></a><a name="obs_03_0320_b17218197171853"></a>20</strong> when restoring an object. After 20 days starting from the time when the object is successfully restored, the object's status will change from <strong id="obs_03_0320_b34084818146"><a name="obs_03_0320_b34084818146"></a><a name="obs_03_0320_b34084818146"></a>Restored</strong> to <strong id="obs_03_0320_b193925342113658"><a name="obs_03_0320_b193925342113658"></a><a name="obs_03_0320_b193925342113658"></a>Unrestored</strong>.</p>
    </td>
    </tr>
    <tr id="obs_03_0320_row53182611164622"><td class="cellrowborder" valign="top" width="23.68%" headers="mcps1.2.3.1.1 "><p id="obs_03_0320_p12824228164622"><a name="obs_03_0320_p12824228164622"></a><a name="obs_03_0320_p12824228164622"></a>Speed</p>
    </td>
    <td class="cellrowborder" valign="top" width="76.32%" headers="mcps1.2.3.1.2 "><p id="obs_03_0320_p32129513164622"><a name="obs_03_0320_p32129513164622"></a><a name="obs_03_0320_p32129513164622"></a>Restoration speed of an object.</p>
    <a name="obs_03_0320_ul20730162164622"></a><a name="obs_03_0320_ul20730162164622"></a><ul id="obs_03_0320_ul20730162164622"><li><strong id="obs_03_0320_b1582157145911"><a name="obs_03_0320_b1582157145911"></a><a name="obs_03_0320_b1582157145911"></a>Expedited</strong>: Allows you to restore the Cold objects within 1 to 5 minutes.</li><li><strong id="obs_03_0320_b0591717204614"><a name="obs_03_0320_b0591717204614"></a><a name="obs_03_0320_b0591717204614"></a>Standard</strong>: Allows you to restore your cold objects within 3 to 5 hours.</li><li><strong id="obs_03_0320_b1759418742113726"><a name="obs_03_0320_b1759418742113726"></a><a name="obs_03_0320_b1759418742113726"></a>Bulk</strong>: Bulk retrievals are the lowest-cost retrieval option of OBS, enabling you to retrieve large amounts, even petabytes, of data in a day at a low cost. Bulk retrievals typically complete within 5 to 12 hours.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

4.  Click  **OK**.

    Click  ![](figures/icon-attributes.png)  and the  **Properties**  dialog box is displayed. For details, see  [Figure 1](#fe014653c9d364bf3999772d96d998638). You can view the restoration status.

    **Figure  1**  Properties of the restored object<a name="fe014653c9d364bf3999772d96d998638"></a>  
    ![](figures/properties-of-the-restored-object.png "properties-of-the-restored-object")

    You can download the file only after its status changes to  **Restored**. You can click the  **Refresh**  button in the upper right corner to refresh the restoration tasks and to view the restoration progress. The system also automatically refreshes the restoration tasks every 5 minutes.

    >![](/images/icon-note.gif) **NOTE:**   
    >The system checks the file restoration status once a day at UTC 00:00. The expiration time is counted starting from the time when the last check is complete.  


## Follow-up Procedure<a name="s62e59e087d6c49fb99d881ecaa584564"></a>

Within the validity period of an object, you can repeatedly restore the object. The validity period of the object is counted starting from the time when the latest restoration is completed. By doing so, you can prolong the validity period of an object.

>![](/images/icon-note.gif) **NOTE:**   
>If an object is to be restored for a second time, the expiration time set for the second restoration must be later than that set for the first restoration.  

