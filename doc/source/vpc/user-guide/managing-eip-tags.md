# Managing EIP Tags<a name="en-us_topic_0068145818"></a>

## Scenarios<a name="section51463883214456"></a>

Tags can be added to EIPs to facilitate EIP identification and administration. You can add a tag to an EIP when assigning the EIP. Alternatively, you can add a tag to an assigned EIP on the EIP details page. A maximum of ten tags can be added to each EIP.

A tag consists of a key and value pair.  [Table 1](#ted9687ca14074ef785241145365a6175)  lists the tag key and value requirements.

**Table  1**  EIP tag requirements

<a name="ted9687ca14074ef785241145365a6175"></a>
<table><thead align="left"><tr id="rd57708e01e6443a9805ca72f554fae7f"><th class="cellrowborder" valign="top" width="18.54%" id="mcps1.2.4.1.1"><p id="abc7708d69440476086850b219c70efa8"><a name="abc7708d69440476086850b219c70efa8"></a><a name="abc7708d69440476086850b219c70efa8"></a><strong id="b842352706165123"><a name="b842352706165123"></a><a name="b842352706165123"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="53.39%" id="mcps1.2.4.1.2"><p id="a0df2f83c3277432ab05b525e4ffb1c2c"><a name="a0df2f83c3277432ab05b525e4ffb1c2c"></a><a name="a0df2f83c3277432ab05b525e4ffb1c2c"></a><strong id="b842352706174218"><a name="b842352706174218"></a><a name="b842352706174218"></a>Requirement</strong></p>
</th>
<th class="cellrowborder" valign="top" width="28.07%" id="mcps1.2.4.1.3"><p id="a902e732241f94e96b0b1b718cf7ed639"><a name="a902e732241f94e96b0b1b718cf7ed639"></a><a name="a902e732241f94e96b0b1b718cf7ed639"></a><strong id="b842352706174227"><a name="b842352706174227"></a><a name="b842352706174227"></a>Example Value</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r95612b479088487b99e620f90b71f798"><td class="cellrowborder" valign="top" width="18.54%" headers="mcps1.2.4.1.1 "><p id="a7694a48138124d1daf3804556a27bfd6"><a name="a7694a48138124d1daf3804556a27bfd6"></a><a name="a7694a48138124d1daf3804556a27bfd6"></a>Key</p>
</td>
<td class="cellrowborder" valign="top" width="53.39%" headers="mcps1.2.4.1.2 "><a name="uac40e19ce4ac49d0913d48b334564c45"></a><a name="uac40e19ce4ac49d0913d48b334564c45"></a><ul id="uac40e19ce4ac49d0913d48b334564c45"><li>Cannot be left blank.</li><li>Must be unique for each EIP.</li><li>Can contain a maximum of 36 characters.</li><li>Can contain only the following character types:<a name="uccb317c6616b4445aa84b125e5aa017f"></a><a name="uccb317c6616b4445aa84b125e5aa017f"></a><ul id="uccb317c6616b4445aa84b125e5aa017f"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
</li></ul>
</td>
<td class="cellrowborder" valign="top" width="28.07%" headers="mcps1.2.4.1.3 "><p id="a1a10de6d67c04555a3508a8cdc3500e7"><a name="a1a10de6d67c04555a3508a8cdc3500e7"></a><a name="a1a10de6d67c04555a3508a8cdc3500e7"></a>Ipv4_key1</p>
</td>
</tr>
<tr id="r32a79d8bde844fda8a6254383317e58f"><td class="cellrowborder" valign="top" width="18.54%" headers="mcps1.2.4.1.1 "><p id="a1ebd1dda592448d49631c7f099519113"><a name="a1ebd1dda592448d49631c7f099519113"></a><a name="a1ebd1dda592448d49631c7f099519113"></a>Value</p>
</td>
<td class="cellrowborder" valign="top" width="53.39%" headers="mcps1.2.4.1.2 "><a name="uaf17b1ea9b9a4e58b95cafefa2898283"></a><a name="uaf17b1ea9b9a4e58b95cafefa2898283"></a><ul id="uaf17b1ea9b9a4e58b95cafefa2898283"><li>Can contain a maximum of 43 characters.</li><li>Can contain only the following character types:<a name="ub74c759faad544c3b4428accc9c42b80"></a><a name="ub74c759faad544c3b4428accc9c42b80"></a><ul id="ub74c759faad544c3b4428accc9c42b80"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
</li></ul>
</td>
<td class="cellrowborder" valign="top" width="28.07%" headers="mcps1.2.4.1.3 "><p id="a21a035aeb72143f5ab0fd45a08248d08"><a name="a21a035aeb72143f5ab0fd45a08248d08"></a><a name="a21a035aeb72143f5ab0fd45a08248d08"></a>192.168.12.10</p>
</td>
</tr>
</tbody>
</table>

## Procedure<a name="section4374728222113"></a>

**Search for EIPs by Tag Key and Value on the Page Showing the EIP List.**

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  On the console homepage, under  **Network**, click  **Elastic IP**.
4.  In the upper right corner of the EIP list, click  **Search by Tag**.
5.  In the displayed area, enter the tag key and value of the EIP you are looking for.

    Both the tag key and value must be specified. The system automatically displays the EIPs you are looking for if both the tag key and value are matched.

6.  Click  **+**  to add the entered tag key and value.

    You can add multiple tag keys and values to refine your search results. If you add more than one tag to search for EIPs, the EIPs containing all specified tags will be displayed.

7.  Click  **Search**.

    The system displays the EIPs you are looking for based on the entered tag keys and values.


**Add, Delete, Edit, and View Tags on the Tags Tab of an EIP.**

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  On the console homepage, under  **Network**, click  **Elastic IP**.
4.  On the displayed page, locate the EIP whose tags are to be managed, and click the IP address.
5.  On the page showing EIP details, click the  **Tags**  tab and perform desired operations on tags.
    -   View tags.

        On the  **Tags**  tab, you can view details about tags added to the current EIP, including the number of tags and the key and value of each tag.

    -   Add a tag.

        Click  **Add Tag**  in the upper left corner. In the displayed  **Add Tag**  dialog box, enter the tag key and value, and click  **OK**.

    -   Edit a tag.

        Locate the row that contains the tag to be edited, and click  **Edit**  in the  **Operation**  column. Enter the new tag key and value, and click  **OK**.

    -   Delete a tag.

        Locate the row that contains the tag to be deleted, and click  **Delete**  in the  **Operation**  column. In the displayed  **Delete Tag**  dialog box, click  **Yes**.



