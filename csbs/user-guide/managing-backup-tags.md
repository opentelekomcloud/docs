# Managing Backup Tags<a name="EN-US_TOPIC_0103696541"></a>

You can add tags to a backup as well as edit and delete these tags. These tags are used to filter and manage backup resources only.

## Procedure<a name="section6750171261513"></a>

1.  Log in to the CSBS management console.
    1.  Log in to the management console.
    2.  Click  ![](figures/icon-region.png)  in the upper left corner of the management console and select a region and a project.
    3.  Click  ![](figures/icon-servicelist.png). Under  **Storage**, click  **Cloud Server Backup Service**.

2.  Click the  **Backups**  tab. Locate the backup for the ECS. For details, see  [Viewing a Backup](viewing-a-backup.md).
3.  Click  ![](figures/icon-down.png)  on the left of a backup name to view details about the backup.
4.  Click  **Tags**  in the details area to expand the tag management panel.

    The panel displays all tags of the backup.

    -   Adding a tag
        1.  Click  **Add Tag**  in the upper left corner.
        2.  In the dialog box that is displayed, set the key and value of the new tag.

            A tag is represented in the form of a key-value pair. Tags are used to identify, classify, and search for cloud resources. These tags are used to filter and manage backup resources only. A backup can have a maximum of 10 tags.

            [Table 1](#table191162312815)  describes parameters of a tag.

            **Table  1**  Parameter description

            <a name="table191162312815"></a>
            <table><thead align="left"><tr id="row41151331884"><th class="cellrowborder" valign="top" width="9.900990099009901%" id="mcps1.2.4.1.1"><p id="p311514319817"><a name="p311514319817"></a><a name="p311514319817"></a>Parameter</p>
            </th>
            <th class="cellrowborder" valign="top" width="71.28712871287128%" id="mcps1.2.4.1.2"><p id="p3115234819"><a name="p3115234819"></a><a name="p3115234819"></a>Description</p>
            </th>
            <th class="cellrowborder" valign="top" width="18.81188118811881%" id="mcps1.2.4.1.3"><p id="p19990164015312"><a name="p19990164015312"></a><a name="p19990164015312"></a>Example Value</p>
            </th>
            </tr>
            </thead>
            <tbody><tr id="row51153313816"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.2.4.1.1 "><p id="p14115183385"><a name="p14115183385"></a><a name="p14115183385"></a>Key</p>
            </td>
            <td class="cellrowborder" valign="top" width="71.28712871287128%" headers="mcps1.2.4.1.2 "><p id="p611511310819"><a name="p611511310819"></a><a name="p611511310819"></a>Tag key. Each tag of a backup has a unique key. The key of a tag is user-definable or is selected from those of existing tags in TMS.</p>
            <p id="p191158314810"><a name="p191158314810"></a><a name="p191158314810"></a>The naming rule of a tag key is as follows:</p>
            <a name="ul1375384515178"></a><a name="ul1375384515178"></a><ul id="ul1375384515178"><li>It ranges from 1 to 36 Unicode characters.</li></ul>
            <a name="ul20115438812"></a><a name="ul20115438812"></a><ul id="ul20115438812"><li>It can contain only uppercase letters, lowercase letters, digits, hyphens (-), and underscores (_).</li></ul>
            </td>
            <td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.4.1.3 "><p id="p1499017405316"><a name="p1499017405316"></a><a name="p1499017405316"></a>Key_0001</p>
            </td>
            </tr>
            <tr id="row21161531187"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.2.4.1.1 "><p id="p101151731081"><a name="p101151731081"></a><a name="p101151731081"></a>Value</p>
            </td>
            <td class="cellrowborder" valign="top" width="71.28712871287128%" headers="mcps1.2.4.1.2 "><p id="p1911693486"><a name="p1911693486"></a><a name="p1911693486"></a>Tag value. Tag values can be repetitive or null.</p>
            <p id="p21161131085"><a name="p21161131085"></a><a name="p21161131085"></a>The naming rule of a tag value is as follows:</p>
            <a name="ul1369633817171"></a><a name="ul1369633817171"></a><ul id="ul1369633817171"><li>It ranges from 0 to 43 Unicode characters.</li></ul>
            <a name="ul211610318811"></a><a name="ul211610318811"></a><ul id="ul211610318811"><li>It can contain only uppercase letters, lowercase letters, digits, hyphens (-), and underscores (_).</li></ul>
            </td>
            <td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.4.1.3 "><p id="p129902040143116"><a name="p129902040143116"></a><a name="p129902040143116"></a>Value_0001</p>
            </td>
            </tr>
            </tbody>
            </table>

        3.  Click  **OK**.

    -   Editing a tag
        1.  In the  **Operation**  column of the tag that you want to edit, click  **Edit**.
        2.  In the  **Edit Tag**  dialog box that is displayed, modify the tag value.  [Table 1](#table191162312815)  describes the parameters.

            If the updated tag is identical to an existing one, only one is retained.

        3.  Click  **OK**.

    -   Deleting a tag
        1.  In the  **Operation**  column of the tag that you want to delete, click  **Delete**.
        2.  In the dialog box that is displayed, confirm the deletion information.
        3.  Click  **OK**.

    -   Searching for backups by tag

        For details, see  [View Backup Details](viewing-a-backup.md#section20267152222857).



