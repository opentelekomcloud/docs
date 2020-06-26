# Managing Protected Instance Tags<a name="sdrs_ug_pi_0008"></a>

## Scenarios<a name="section8725118105318"></a>

Tags are identifiers of protected instances. You can add tags for protected instances, and classify and search the protected instances based on these tags.

You can add a maximum of 10 tags for each protected instance when creating the protected instance or add them on the details page of the created protected instance.

## **Context**<a name="section14453133119534"></a>

A tag consists of a tag key and a tag value.  [Table 1](#en-us_topic_0092499768_table197401426182516)  lists the tag key and value requirements.

**Table  1**  Tag key and value requirements

<a name="en-us_topic_0092499768_table197401426182516"></a>
<table><thead align="left"><tr id="en-us_topic_0092499768_row374112610252"><th class="cellrowborder" valign="top" width="18.54%" id="mcps1.2.4.1.1"><p id="en-us_topic_0092499768_p674122692511"><a name="en-us_topic_0092499768_p674122692511"></a><a name="en-us_topic_0092499768_p674122692511"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="55.65%" id="mcps1.2.4.1.2"><p id="en-us_topic_0092499768_p47412026172519"><a name="en-us_topic_0092499768_p47412026172519"></a><a name="en-us_topic_0092499768_p47412026172519"></a>Requirement</p>
</th>
<th class="cellrowborder" valign="top" width="25.81%" id="mcps1.2.4.1.3"><p id="en-us_topic_0092499768_p074152682511"><a name="en-us_topic_0092499768_p074152682511"></a><a name="en-us_topic_0092499768_p074152682511"></a>Example</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0092499768_row77477265250"><td class="cellrowborder" valign="top" width="18.54%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0092499768_p37471326142512"><a name="en-us_topic_0092499768_p37471326142512"></a><a name="en-us_topic_0092499768_p37471326142512"></a>Tag key </p>
</td>
<td class="cellrowborder" valign="top" width="55.65%" headers="mcps1.2.4.1.2 "><a name="en-us_topic_0092499768_ul207505264257"></a><a name="en-us_topic_0092499768_ul207505264257"></a><ul id="en-us_topic_0092499768_ul207505264257"><li>Cannot be left blank.</li><li>Must be unique.</li><li>Can contain a maximum of 36 characters.</li><li>Can only consist of digits, letters, hyphens (-), and underscores (_).</li></ul>
</td>
<td class="cellrowborder" valign="top" width="25.81%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0092499768_p157536266259"><a name="en-us_topic_0092499768_p157536266259"></a><a name="en-us_topic_0092499768_p157536266259"></a>Organization</p>
</td>
</tr>
<tr id="en-us_topic_0092499768_row4754926182519"><td class="cellrowborder" valign="top" width="18.54%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0092499768_p37542260253"><a name="en-us_topic_0092499768_p37542260253"></a><a name="en-us_topic_0092499768_p37542260253"></a>Tag value</p>
</td>
<td class="cellrowborder" valign="top" width="55.65%" headers="mcps1.2.4.1.2 "><a name="en-us_topic_0092499768_ul107561326102518"></a><a name="en-us_topic_0092499768_ul107561326102518"></a><ul id="en-us_topic_0092499768_ul107561326102518"><li>Can contain a maximum of 43 characters.</li><li>Can only consist of digits, letters, hyphens (-), and underscores (_).</li></ul>
</td>
<td class="cellrowborder" valign="top" width="25.81%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0092499768_p47581826192520"><a name="en-us_topic_0092499768_p47581826192520"></a><a name="en-us_topic_0092499768_p47581826192520"></a>Marketing</p>
</td>
</tr>
</tbody>
</table>

## Procedure<a name="section1420165135416"></a>

You can perform the following operations based on tags:

-   Adding tags for a protected instance when you create the protected instance

    For details, see  [Step 2: Create a Protected Instance](step-2-create-a-protected-instance.md).

-   Searching for protected instances by tag on the protected instance list page
    1.  Log in to the management console.
    2.  Choose  **Storage**  \>  **Storage Disaster Recovery Service**.
    3.  In the pane of the protection group, click  **Protected Instances**.
    4.  On the  **Protected Instances**  tab, click  **Search by Tag**  in the upper right corner of the protected instance list to expand the search area.
    5.  Enter the tag of the protected instance to be searched.

        Both the tag key and tag value must be specified. When the tag key or tag value is matched, the system automatically shows the target protected instances.

    6.  Click  ![](figures/instance-tags-0.png)  to add a tag.

        The system supports multiple tags and uses the intersection set of all tags to search for protected instances.

    7.  Click  **Search**.

        The system searches for protection instances by tags.


-   Adding, deleting, modifying, and searching for tags on the  **Protected Instance Details**  page
    1.  Log in to the management console.
    2.  Choose  **Storage**  \>  **Storage Disaster Recovery Service**.
    3.  In the pane of the protection group, click  **Protected Instances**.
    4.  Click the  **Protected Instances**  tab and click the name of the specified protected instance.

        The  **Protected Instance Details**  page is displayed.

    5.  Click the  **Tags**  tab and perform desired operations.
        -   View tags.

            You can view details of protected instance tags, including the number of tags and the key and value of each tag.

        -   Add a tag.

            Click  **Add Tag**  in the upper left corner. In the displayed dialog box, enter the key and value of the tag to be added, and click  **OK**.

        -   Modify a tag.

            Locate the row containing the tag to be edited and click  **Edit**  in the  **Operation**  column. In the  **Edit Tag**  dialog box, change the key and value of the tag and click  **OK**.

        -   Delete a tag.

            Locate the row containing the tag to be deleted and click  **Delete**  in the  **Operation**  column. In the  **Delete Tag**  dialog box, click  **OK**.




