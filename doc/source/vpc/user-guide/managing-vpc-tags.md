# Managing VPC Tags<a name="vpc_vpc_0004"></a>

## Scenarios<a name="section51463883214456"></a>

A VPC tag identifies a VPC. Tags can be added to VPCs to facilitate VPC identification and administration. You can add a tag to a VPC when creating the VPC. Alternatively, you can add a tag to a created VPC on the VPC details page. A maximum of ten tags can be added to each VPC.

A tag consists of a key and value pair.  [Table 1](#ted9687ca14074ef785241145365a6175)  lists the tag key and value requirements.

**Table  1**  VPC tag key and value requirements

<a name="ted9687ca14074ef785241145365a6175"></a>
<table><thead align="left"><tr id="r8f725dd873f74d5689a397a96364525f"><th class="cellrowborder" valign="top" width="17.71%" id="mcps1.2.4.1.1"><p id="ae7200181216040679ba0b08613e317f0"><a name="ae7200181216040679ba0b08613e317f0"></a><a name="ae7200181216040679ba0b08613e317f0"></a><strong id="b84235270618434"><a name="b84235270618434"></a><a name="b84235270618434"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="65.29%" id="mcps1.2.4.1.2"><p id="a30f1778a977845c0a6948f77fd9efada"><a name="a30f1778a977845c0a6948f77fd9efada"></a><a name="a30f1778a977845c0a6948f77fd9efada"></a><strong id="b842352706174218"><a name="b842352706174218"></a><a name="b842352706174218"></a>Requirements</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.4.1.3"><p id="a34827669831a48ec96262bfcabc61519"><a name="a34827669831a48ec96262bfcabc61519"></a><a name="a34827669831a48ec96262bfcabc61519"></a><strong id="b842352706174227"><a name="b842352706174227"></a><a name="b842352706174227"></a>Example Value</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="ra6c6dfb7a5c344f1af2c7664d34e7d80"><td class="cellrowborder" valign="top" width="17.71%" headers="mcps1.2.4.1.1 "><p id="a45a01bdce58d410d8ee06b6f374e401b"><a name="a45a01bdce58d410d8ee06b6f374e401b"></a><a name="a45a01bdce58d410d8ee06b6f374e401b"></a>Key</p>
</td>
<td class="cellrowborder" valign="top" width="65.29%" headers="mcps1.2.4.1.2 "><a name="ub2cf5f68e02742d49e3f8d80289eab77"></a><a name="ub2cf5f68e02742d49e3f8d80289eab77"></a><ul id="ub2cf5f68e02742d49e3f8d80289eab77"><li>Cannot be left blank.</li><li>Must be unique for the same VPC and can be the same for different VPCs.</li><li>Can contain a maximum of 36 characters.</li><li>Can contain only the following character types:<a name="uccb317c6616b4445aa84b125e5aa017f"></a><a name="uccb317c6616b4445aa84b125e5aa017f"></a><ul id="uccb317c6616b4445aa84b125e5aa017f"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
</li></ul>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.3 "><p id="a735c9e74ec274598ac7051f7d65e7bce"><a name="a735c9e74ec274598ac7051f7d65e7bce"></a><a name="a735c9e74ec274598ac7051f7d65e7bce"></a>vpc_key1</p>
</td>
</tr>
<tr id="rcabbd61ffcd048ec8408a15332fde94d"><td class="cellrowborder" valign="top" width="17.71%" headers="mcps1.2.4.1.1 "><p id="a5f7f1bb378214abcaf0c661567a47535"><a name="a5f7f1bb378214abcaf0c661567a47535"></a><a name="a5f7f1bb378214abcaf0c661567a47535"></a>Value</p>
</td>
<td class="cellrowborder" valign="top" width="65.29%" headers="mcps1.2.4.1.2 "><a name="u463eb9034f3d456b81073b15ba62f102"></a><a name="u463eb9034f3d456b81073b15ba62f102"></a><ul id="u463eb9034f3d456b81073b15ba62f102"><li>Can contain a maximum of 43 characters.</li><li>Can contain only the following character types:<a name="ub74c759faad544c3b4428accc9c42b80"></a><a name="ub74c759faad544c3b4428accc9c42b80"></a><ul id="ub74c759faad544c3b4428accc9c42b80"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
</li></ul>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.3 "><p id="a3ac5d865f6a848458eb5fae95f81fee0"><a name="a3ac5d865f6a848458eb5fae95f81fee0"></a><a name="a3ac5d865f6a848458eb5fae95f81fee0"></a>vpc-01</p>
</td>
</tr>
</tbody>
</table>

## Procedure<a name="section4374728222113"></a>

**Search for VPCs by Tag Key and Value on the Page Showing the VPC List.**

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  Under  **Network**, click  **Virtual Private Cloud**.
4.  In the navigation pane on the left, click  **Virtual Private Cloud**.
5.  In the upper right corner of the VPC list, click  **Search by Tag**.
6.  In the displayed area, enter the tag key and value of the VPC you are looking for.

    Both the tag key and value must be specified. The system automatically displays the VPCs you are looking for if both the tag key and value are matched.

7.  Click  **+**  to add the entered tag key and value.

    You can add multiple tag keys and values to refine your search results. If you add more than one tag to search for VPCs, the VPCs containing all specified tags will be displayed.

8.  Click  **Search**.

    The system displays the VPCs you are looking for based on the entered tag keys and values. 


**Add, Delete, Edit, and View Tags on the Tags Tab of a VPC.**

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  Under  **Network**, click  **Virtual Private Cloud**.
4.  In the navigation pane on the left, click  **Virtual Private Cloud**.
5.  On the  **Virtual Private Cloud**  page, locate the VPC whose tags are to be managed and click the VPC name.

    The page showing details about the particular VPC is displayed.

6.  Click the  **Tags**  tab and perform desired operations on tags.
    -   View tags.

        On the  **Tags**  tab, you can view details about tags added to the current VPC, including the number of tags and the key and value of each tag.

    -   Add a tag.

        Click  **Add Tag**  in the upper left corner. In the displayed  **Add Tag**  dialog box, enter the tag key and value, and click  **OK**.

    -   Edit a tag.

        Locate the row that contains the tag to be edited, and click  **Edit**  in the  **Operation**  column. Enter the new tag key and value, and click  **OK**.

    -   Delete a tag.

        Locate the row that contains the tag to be deleted, and click  **Delete**  in the  **Operation**  column. In the displayed  **Delete Tag**  dialog box, click  **Yes**.



