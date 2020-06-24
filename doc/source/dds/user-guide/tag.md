# Tag<a name="dds_03_0023"></a>

## **Scenarios**<a name="section7898787175059"></a>

Tag Management Service \(TMS\) enables you to use tags on the management console to manage resources. TMS works with other cloud services to manage tags. TMS manages tags globally and other cloud services manage their own tags.

Adding tags to DDS DB instances helps you better identify and manage them. A DB instance can be tagged during or after it is created.

-   You are advised to set predefined tags on the TMS console.
-   A tag consists of a key and value. You can add only one value for each key. For details about the naming rules of tag keys and tag values, see  [Table 1](#table197401426182516).
-   A maximum of 10 tags can be added for a DB instance.

**Table  1**  Naming rules

<a name="table197401426182516"></a>
<table><thead align="left"><tr id="row374112610252"><th class="cellrowborder" valign="top" width="18.54%" id="mcps1.2.4.1.1"><p id="p674122692511"><a name="p674122692511"></a><a name="p674122692511"></a><strong id="b053013532341"><a name="b053013532341"></a><a name="b053013532341"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="53.39%" id="mcps1.2.4.1.2"><p id="p47412026172519"><a name="p47412026172519"></a><a name="p47412026172519"></a><strong id="b121465516343"><a name="b121465516343"></a><a name="b121465516343"></a>Requirement</strong></p>
</th>
<th class="cellrowborder" valign="top" width="28.07%" id="mcps1.2.4.1.3"><p id="p074152682511"><a name="p074152682511"></a><a name="p074152682511"></a><strong id="b84235270685752"><a name="b84235270685752"></a><a name="b84235270685752"></a>Example</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row77477265250"><td class="cellrowborder" valign="top" width="18.54%" headers="mcps1.2.4.1.1 "><p id="p37471326142512"><a name="p37471326142512"></a><a name="p37471326142512"></a>Tag key</p>
</td>
<td class="cellrowborder" valign="top" width="53.39%" headers="mcps1.2.4.1.2 "><a name="ul207505264257"></a><a name="ul207505264257"></a><ul id="ul207505264257"><li>Cannot be left blank.</li><li>For each DB instance, each tag key is unique.</li><li>Consists of a maximum of 36 characters.</li><li>Can only consist of digits, letters, underscores (_), and hyphens (-).</li></ul>
</td>
<td class="cellrowborder" valign="top" width="28.07%" headers="mcps1.2.4.1.3 "><p id="p157536266259"><a name="p157536266259"></a><a name="p157536266259"></a>Organization</p>
</td>
</tr>
<tr id="row4754926182519"><td class="cellrowborder" valign="top" width="18.54%" headers="mcps1.2.4.1.1 "><p id="p37542260253"><a name="p37542260253"></a><a name="p37542260253"></a>Tag value</p>
</td>
<td class="cellrowborder" valign="top" width="53.39%" headers="mcps1.2.4.1.2 "><a name="ul107561326102518"></a><a name="ul107561326102518"></a><ul id="ul107561326102518"><li>Can be empty.</li><li>Consists of a maximum of 43 characters.</li><li>Can only consist of digits, letters, underscores (_), and hyphens (-).</li></ul>
</td>
<td class="cellrowborder" valign="top" width="28.07%" headers="mcps1.2.4.1.3 "><p id="p47581826192520"><a name="p47581826192520"></a><a name="p47581826192520"></a>dds_01</p>
</td>
</tr>
</tbody>
</table>

## Adding a Tag<a name="section57172399175119"></a>

1.  [Log in to the DDS console.](logging-in-to-the-dds-console.md)
2.  On the  **Instance Management**  page, click the target DB instance.
3.  In the navigation pane on the left, click  **Tags**.
4.  On the  **Tags**  page, click  **Add Tag**. In the displayed dialog box, enter a tag key and value, and click  **OK**.
5.  View and manage tags on the  **Tags**  page.

## Editing a Tag<a name="section38640924175719"></a>

1.  [Log in to the DDS console.](logging-in-to-the-dds-console.md)
2.  On the  **Instance Management**  page, click the target DB instance.
3.  In the navigation pane on the left, click  **Tags**.
4.  On the  **Tags**  page, locate the tag to be edited and click  **Edit**  in the  **Operation**  column. In the displayed dialog box, change the tag value and click  **OK**.

    Only the tag value can be edited when editing a tag.

5.  View and manage tags on the  **Tags**  page.

## Deleting a Tag<a name="section51403672175725"></a>

1.  [Log in to the DDS console.](logging-in-to-the-dds-console.md)
2.  On the  **Instance Management**  page, click the target DB instance.
3.  In the navigation pane on the left, click  **Tags**.
4.  On the  **Tags**  page, locate the tag to be deleted and click  **Delete**  in the  **Operation**  column. In the displayed dialog box, click  **Yes**.
5.  After a tag has been deleted, it will not be displayed on the  **Tags**  page.

