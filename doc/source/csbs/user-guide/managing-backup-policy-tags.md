# Managing Backup Policy Tags<a name="EN-US_TOPIC_0103696542"></a>

You can add tags to a backup policy as well as edit and delete these tags. These tags are used to filter and manage backup resources only.

## Procedure<a name="section102885314254"></a>

1.  Log in to the CSBS management console.
    1.  Log in to the management console.
    2.  Click  ![](figures/icon-region.png)  in the upper left corner of the management console and select a region and a project.
    3.  Click  ![](figures/icon-servicelist.png). Under  **Storage**, click  **Cloud Server Backup Service**.

2.  Click the  **Policies**  tab.
3.  Select a backup policy and click  ![](figures/icon-down.png). The  **Tags**  tab page displays existing tags of the backup policy.
    -   Adding a tag
        1.  In the upper left corner of the  **Tags**  panel, click  **Add Tag**.
        2.  In the dialog box that is displayed, set the key and value of the new tag.

            A tag is represented in the form of a key-value pair. Tags are used to identify, classify, and search for cloud resources.

            Tags added in a backup policy apply to all backups generated using the backup policy. These tags are used to filter and manage backup resources only. A backup policy can have a maximum of 10 tags.

            [Table 1](#table1499463312)  describes parameters of a tag.

            **Table  1**  Parameter description

            <a name="table1499463312"></a>
            <table><thead align="left"><tr id="row7997693112"><th class="cellrowborder" valign="top" width="10%" id="mcps1.2.4.1.1"><p id="p610096163114"><a name="p610096163114"></a><a name="p610096163114"></a>Parameter</p>
            </th>
            <th class="cellrowborder" valign="top" width="72%" id="mcps1.2.4.1.2"><p id="p111001683118"><a name="p111001683118"></a><a name="p111001683118"></a>Description</p>
            </th>
            <th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.3"><p id="p13176100134"><a name="p13176100134"></a><a name="p13176100134"></a>Example Value</p>
            </th>
            </tr>
            </thead>
            <tbody><tr id="row41005620310"><td class="cellrowborder" valign="top" width="10%" headers="mcps1.2.4.1.1 "><p id="p51007653114"><a name="p51007653114"></a><a name="p51007653114"></a>Key</p>
            </td>
            <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.2 "><p id="p1100765311"><a name="p1100765311"></a><a name="p1100765311"></a>Tag key. Each tag of a backup policy has a unique key. The key of a tag is user-definable or is selected from those of existing tags in TMS.</p>
            <p id="p1310012619313"><a name="p1310012619313"></a><a name="p1310012619313"></a>The naming rule of a tag key is as follows:</p>
            <a name="ul20115438812"></a><a name="ul20115438812"></a><ul id="ul20115438812"><li>It ranges from 1 to 36 Unicode characters.</li><li>It can contain only uppercase letters, lowercase letters, digits, hyphens (-), and underscores (_).</li></ul>
            </td>
            <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.3 "><p id="p1617616012310"><a name="p1617616012310"></a><a name="p1617616012310"></a>Key_0001</p>
            </td>
            </tr>
            <tr id="row1310014614314"><td class="cellrowborder" valign="top" width="10%" headers="mcps1.2.4.1.1 "><p id="p141001968315"><a name="p141001968315"></a><a name="p141001968315"></a>Value</p>
            </td>
            <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.2 "><p id="p1510056203114"><a name="p1510056203114"></a><a name="p1510056203114"></a>Tag value. Tag values can be repetitive or null.</p>
            <p id="p2100186133115"><a name="p2100186133115"></a><a name="p2100186133115"></a>The naming rule of a tag value is as follows:</p>
            <a name="ul211610318811"></a><a name="ul211610318811"></a><ul id="ul211610318811"><li>It ranges from 0 to 43 Unicode characters.</li><li>It can contain only uppercase letters, lowercase letters, digits, hyphens (-), and underscores (_).</li></ul>
            </td>
            <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.3 "><p id="p19176601033"><a name="p19176601033"></a><a name="p19176601033"></a>Value_0001</p>
            </td>
            </tr>
            </tbody>
            </table>

        3.  Click  **OK**.

    -   Editing a tag
        1.  In the  **Operation**  column of the tag that you want to edit, click  **Edit**.
        2.  In the  **Edit Tag**  dialog box that is displayed, modify the tag value.  [Table 1](#table1499463312)  describes the parameters.
        3.  Click  **OK**.

    -   Deleting a tag
        1.  In the  **Operation**  column of the tag that you want to delete, click  **Delete**.
        2.  In the dialog box that is displayed, confirm the deletion information.
        3.  Click  **OK**.



