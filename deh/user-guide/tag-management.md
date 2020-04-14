# Tag Management<a name="EN-US_TOPIC_0152893947"></a>

Tags are identifiers of DeHs. Adding tags to DeHs can help you identify and manage your DeHs.

You can add a tag to a DeH during the DeH creation. Alternatively, you can add a tag to a DeH on the  **Tags**  tab of the DeH details page. A maximum of 10 tags can be added to a DeH.

A tag consists of a tag key and a tag value.  [Table 1](#table204442131366)  lists the naming requirements for keys and values.

**Table  1**  Tag naming requirements

<a name="table204442131366"></a>
<table><thead align="left"><tr id="row44447138369"><th class="cellrowborder" valign="top" width="19.101910191019105%" id="mcps1.2.4.1.1"><p id="p470292918368"><a name="p470292918368"></a><a name="p470292918368"></a><strong id="b842352706184931"><a name="b842352706184931"></a><a name="b842352706184931"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="47.56475647564757%" id="mcps1.2.4.1.2"><p id="p370219293361"><a name="p370219293361"></a><a name="p370219293361"></a><strong id="b39731356112712"><a name="b39731356112712"></a><a name="b39731356112712"></a>Requirement</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p1870319292364"><a name="p1870319292364"></a><a name="p1870319292364"></a><strong id="b842352706194150"><a name="b842352706194150"></a><a name="b842352706194150"></a>Example Value</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row0444913183616"><td class="cellrowborder" valign="top" width="19.101910191019105%" headers="mcps1.2.4.1.1 "><p id="p1270320293365"><a name="p1270320293365"></a><a name="p1270320293365"></a>Tag key</p>
</td>
<td class="cellrowborder" valign="top" width="47.56475647564757%" headers="mcps1.2.4.1.2 "><a name="ul970319290363"></a><a name="ul970319290363"></a><ul id="ul970319290363"><li>Cannot be left blank.</li><li>Must be unique for a specific DeH.</li><li>Contains a maximum of 36 characters.</li><li>Contains only digits, letters, hyphens (-), and underscores (_).</li></ul>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p13703122912362"><a name="p13703122912362"></a><a name="p13703122912362"></a>Organization</p>
</td>
</tr>
<tr id="row194446132361"><td class="cellrowborder" valign="top" width="19.101910191019105%" headers="mcps1.2.4.1.1 "><p id="p1370314293368"><a name="p1370314293368"></a><a name="p1370314293368"></a>Tag value</p>
</td>
<td class="cellrowborder" valign="top" width="47.56475647564757%" headers="mcps1.2.4.1.2 "><a name="ul97031229203620"></a><a name="ul97031229203620"></a><ul id="ul97031229203620"><li>Contains a maximum of 43 characters.</li><li>Contains only digits, letters, hyphens (-), and underscores (_).</li></ul>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p11704122943610"><a name="p11704122943610"></a><a name="p11704122943610"></a>Apache</p>
</td>
</tr>
</tbody>
</table>

## Searching for DeHs<a name="section2682195644817"></a>

On the  **Dedicated Host**  page, you can search for the desired DeHs based on the tag keys and tag values.

1.  Log in to the management console.
2.  Under  **Computing**, click  **Dedicated Host**.
3.  In the upper right corner of the DeH list, click  **Search by Tag**  to expand the search page.

    **Figure  1**  Searching for DeHs by tag<a name="fig1051216257312"></a>  
    ![](figures/searching-for-dehs-by-tag.png "searching-for-dehs-by-tag")

4.  Enter the tag of the DeH to be searched.

    Neither the tag key nor tag value can be empty. When the tag key and tag value are matched, the system automatically shows your desired DeHs.

5.  Click  ![](figures/6.png)  to add a tag.

    You can add multiple tags to DeHs. The system will display DeHs that match all tags.

6.  Click  **Search**.

    The system searches for DeHs based on tag keys or tag values.


