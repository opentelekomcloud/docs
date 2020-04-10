# Managing VPN Tags<a name="vpn_04_0800"></a>

## Application Scenarios<a name="section51463883214456"></a>

A VPN tag identifies a VPN. Tags can be added to VPNs to facilitate VPN identification and administration. You can add a tag to a VPN when creating the VPN. Alternatively, you can add a tag to a created VPN on the VPN details page. A maximum of ten tags can be added to each VPN.

A tag consists of a key and value pair.  [Table 1](#en-us_topic_0013859511_table1794599823119)  lists the tag key and value requirements.

**Table  1**  VPN tag key and value requirements

<a name="en-us_topic_0013859511_table1794599823119"></a>
<table><thead align="left"><tr id="en-us_topic_0013859511_row2997812223119"><th class="cellrowborder" valign="top" width="18.54%" id="mcps1.2.4.1.1"><p id="en-us_topic_0013859511_p4367076523119"><a name="en-us_topic_0013859511_p4367076523119"></a><a name="en-us_topic_0013859511_p4367076523119"></a><strong id="b842352706184931"><a name="b842352706184931"></a><a name="b842352706184931"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="53.39%" id="mcps1.2.4.1.2"><p id="en-us_topic_0013859511_p4767111023119"><a name="en-us_topic_0013859511_p4767111023119"></a><a name="en-us_topic_0013859511_p4767111023119"></a><strong id="b842352706171418"><a name="b842352706171418"></a><a name="b842352706171418"></a>Requirement</strong></p>
</th>
<th class="cellrowborder" valign="top" width="28.07%" id="mcps1.2.4.1.3"><p id="en-us_topic_0013859511_p3615470723119"><a name="en-us_topic_0013859511_p3615470723119"></a><a name="en-us_topic_0013859511_p3615470723119"></a><strong id="b84235270610336"><a name="b84235270610336"></a><a name="b84235270610336"></a>Example Value</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0013859511_row5695691323119"><td class="cellrowborder" valign="top" width="18.54%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0013859511_p5010724023119"><a name="en-us_topic_0013859511_p5010724023119"></a><a name="en-us_topic_0013859511_p5010724023119"></a>Key</p>
</td>
<td class="cellrowborder" valign="top" width="53.39%" headers="mcps1.2.4.1.2 "><a name="ub2cf5f68e02742d49e3f8d80289eab77"></a><a name="ub2cf5f68e02742d49e3f8d80289eab77"></a><ul id="ub2cf5f68e02742d49e3f8d80289eab77"><li>Cannot be left blank.</li><li>Must be unique for the same VPN and can be the same for different VPNs.</li><li>Contains a maximum of 36 characters.</li><li>Can contain only the following character types:<a name="uccb317c6616b4445aa84b125e5aa017f"></a><a name="uccb317c6616b4445aa84b125e5aa017f"></a><ul id="uccb317c6616b4445aa84b125e5aa017f"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
</li></ul>
</td>
<td class="cellrowborder" valign="top" width="28.07%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0013859511_p5438834323119"><a name="en-us_topic_0013859511_p5438834323119"></a><a name="en-us_topic_0013859511_p5438834323119"></a>vpn_key1</p>
</td>
</tr>
<tr id="en-us_topic_0013859511_row1973304523119"><td class="cellrowborder" valign="top" width="18.54%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0013859511_p5487280123119"><a name="en-us_topic_0013859511_p5487280123119"></a><a name="en-us_topic_0013859511_p5487280123119"></a>Value</p>
</td>
<td class="cellrowborder" valign="top" width="53.39%" headers="mcps1.2.4.1.2 "><a name="u463eb9034f3d456b81073b15ba62f102"></a><a name="u463eb9034f3d456b81073b15ba62f102"></a><ul id="u463eb9034f3d456b81073b15ba62f102"><li>Can contain a maximum of 43 characters.</li><li>Can contain only the following character types:<a name="ub74c759faad544c3b4428accc9c42b80"></a><a name="ub74c759faad544c3b4428accc9c42b80"></a><ul id="ub74c759faad544c3b4428accc9c42b80"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
</li></ul>
</td>
<td class="cellrowborder" valign="top" width="28.07%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0013859511_p4850087723119"><a name="en-us_topic_0013859511_p4850087723119"></a><a name="en-us_topic_0013859511_p4850087723119"></a>vpn-01</p>
</td>
</tr>
</tbody>
</table>

## **Procedure**<a name="section4374728222113"></a>

**Search for VPNs by Tag Key and Value on the Page Showing the VPN List.**

1.  Log in to the management console.
2.  Click  ![](figures/d00356819-云计算开发部-公有云_iaas-image-f1cac6ef-c4f7-462b-a7f1-85e988937e64-6.png)  in the upper left corner and select the desired region and project.
3.  On the console homepage, under  **Network**, click  **Virtual Private Network**.
4.  In the upper right corner of the VPN list, click  **Search by Tag**.
5.  In the displayed area, enter the tag key and value of the VPN you are looking for.

    Both the tag key and value must be specified.

6.  Click  **+**  to add the entered tag key and value.

    You can add multiple tag keys and values to refine your search results. If you add more than one tag to search for VPCs, the VPCs containing all specified tags will be displayed.

7.  Click  **Search**.

    The system displays the VPNs you are looking for based on the entered tag keys and values. 


**Add, Delete, Edit, and View Tags on the Tags Tab of a VPN.**

1.  Log in to the management console.
2.  Click  ![](figures/d00356819-云计算开发部-公有云_iaas-image-f1cac6ef-c4f7-462b-a7f1-85e988937e64-6.png)  in the upper left corner and select the desired region and project.
3.  On the console homepage, under  **Network**, click  **Virtual Private Network**.
4.  On the  **Virtual Private Network**  page, locate the VPN whose tags are to be managed and click the VPN name.

    The page showing details about the particular VPN is displayed.

5.  Click the  **Tags**  tab and perform desired operations on tags.
    -   View tags.

        On the  **Tags**  tab, you can view details about tags added to the current VPN, including the number of tags and the key and value of each tag.

    -   Add a tag.

        Click  **Add Tag**  in the upper left corner. In the displayed dialog box, enter the key and value of the tag to be added, and click  **OK**.

    -   Edit a tag.

        Locate the row that contains the tag to be edited and click  **Edit**  in the  **Operation**  column. In the  **Edit Tag**  dialog box, change the tag value and click  **OK**.

    -   Delete a tag.

        Locate the row that contains the tag to be deleted, and click  **Delete**  in the  **Operation**  column. In the displayed  **Delete Tag**  dialog box, click  **Yes**.



