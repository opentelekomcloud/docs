# Tag Management<a name="dws_01_0105"></a>

This section describes how to search for clusters based on tags and how to add, modify, and delete tags for clusters.

## Searching for Clusters Based on Tags<a name="section887643535616"></a>

If tags have been added to a cluster, you can search for the cluster by setting tag filtering conditions to quickly find it.

1.  Log in to the management console at  [https://console.otc.t-systems.com/dws/](https://console.otc.t-systems.com/dws/).
2.  Click  **Cluster Management**.
3.  Click  **Search by Tag**  on the right of the current page to expand the tab page.

    **Figure  1**  Search by tag<a name="fig6194122616438"></a>  
    ![](figures/search-by-tag.png "search-by-tag")

4.  In the  **Search by Tag**  area, click the  **Tag Key**  text box to select a tag key from the drop-down list and then click the  **Tag Value**  text box to select the corresponding tag value.

    You can only enter a tag key or value that exists in the drop-down list. If no tag key or value is available, create a tag for the cluster. For details, see  [Adding a Tag to a Cluster](#section77515910494).

5.  Click  ![](figures/icon_dws_add_tag.png)  to add the selected tag to the area under the text boxes.
    -   Select another tag in the text boxes and click  ![](figures/icon_dws_add_tag.png)  to generate a tag combination for cluster search. You can add a maximum of 10 tags to search for data warehouse clusters. If you specify more than one tag, clusters containing all the specified tags will be displayed.
    -   To delete an existing tag, click  ![](figures/icon_dws_delete_tag.png)  next to the tag.
    -   You can click  **Reset**  to clear all added tags.

        **Figure  2**  Adding the tag key and value<a name="fig19996114485913"></a>  
        ![](figures/adding-the-tag-key-and-value.png "adding-the-tag-key-and-value")

6.  Click  **Search**. The target cluster will be displayed in the cluster list.

## Adding a Tag to a Cluster<a name="section77515910494"></a>

1.  On the  **Cluster Management**  page, click the name of the cluster to which a tag is to be added, and click the  **Tags**  tab.

    **Figure  3**  Tags page<a name="fig44818591213"></a>  
    ![](figures/tags-page.png "tags-page")

2.  Click  **Add Tag**. The  **Add Tag**  dialog box is displayed.
3.  Configure the tag parameters in the  **Add Tag**  dialog box.

    **Figure  4**  Adding a tag to a cluster<a name="fig1857218298273"></a>  
    ![](figures/adding-a-tag-to-a-cluster.png "adding-a-tag-to-a-cluster")

    **Table  1**  Tag parameters

    <a name="table12483201713111"></a>
    <table><thead align="left"><tr id="row17486121763113"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.4.1.1"><p id="p12486181715313"><a name="p12486181715313"></a><a name="p12486181715313"></a><strong id="b84235270617387"><a name="b84235270617387"></a><a name="b84235270617387"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="71%" id="mcps1.2.4.1.2"><p id="p1191704514113"><a name="p1191704514113"></a><a name="p1191704514113"></a><strong id="b842352706101627"><a name="b842352706101627"></a><a name="b842352706101627"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.4.1.3"><p id="p18486151713117"><a name="p18486151713117"></a><a name="p18486151713117"></a><strong id="b60793810112357"><a name="b60793810112357"></a><a name="b60793810112357"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row11486131733111"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="p1433134915503"><a name="p1433134915503"></a><a name="p1433134915503"></a>Tag key</p>
    </td>
    <td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.2 "><p id="p4183104918156"><a name="p4183104918156"></a><a name="p4183104918156"></a>You can:</p>
    <a name="ul149381653121514"></a><a name="ul149381653121514"></a><ul id="ul149381653121514"><li>Select a predefined tag key or an existing resource tag key from the drop-down list of the text box.<div class="note" id="note354311061312"><a name="note354311061312"></a><a name="note354311061312"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p19473813185311"><a name="p19473813185311"></a><a name="p19473813185311"></a>To add a predefined tag, you need to create one on TMS and select it from the drop-down list of <span class="parmname" id="parmname890218564101210"><a name="parmname890218564101210"></a><a name="parmname890218564101210"></a><b>Tag key</b></span>. You can click <span class="uicontrol" id="uicontrol941000013191930"><a name="uicontrol941000013191930"></a><a name="uicontrol941000013191930"></a><b>View predefined tags</b></span> to enter the <span class="wintitle" id="wintitle72946297619202"><a name="wintitle72946297619202"></a><a name="wintitle72946297619202"></a><b>Predefined Tag</b></span> page of TMS. Then, click <span class="uicontrol" id="uicontrol1385059717192149"><a name="uicontrol1385059717192149"></a><a name="uicontrol1385059717192149"></a><b>Create Tag</b></span> to create a predefined tag. For details, see section <span class="filepath" id="filepath79624027716543"><a name="filepath79624027716543"></a><a name="filepath79624027716543"></a><b>Creating Predefined Tags</b></span> in the <em id="i842352697104314"><a name="i842352697104314"></a><a name="i842352697104314"></a>Tag Management Service User Guide</em>.</p>
    </div></div>
    </li></ul>
    <a name="ul154819568159"></a><a name="ul154819568159"></a><ul id="ul154819568159"><li>Enter a tag key in the text box. A tag key can contain a maximum of 36 Unicode characters, which cannot be null. The first and last characters cannot be spaces.<p id="p1740919129378"><a name="p1740919129378"></a><a name="p1740919129378"></a>Contain only uppercase letters (A to Z), lowercase letters (a to z), digits (0-9), hyphens (-), and underscores (_).</p>
    <div class="p" id="p922511632019"><a name="p922511632019"></a><a name="p922511632019"></a><div class="note" id="note206991233134612"><a name="note206991233134612"></a><a name="note206991233134612"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p10699733104619"><a name="p10699733104619"></a><a name="p10699733104619"></a>The key name must be unique in the same cluster.</p>
    </div></div>
    </div>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.3 "><p id="p848641718314"><a name="p848641718314"></a><a name="p848641718314"></a>tagkey01</p>
    </td>
    </tr>
    <tr id="row19486151715318"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="p1548761710317"><a name="p1548761710317"></a><a name="p1548761710317"></a>Tag value</p>
    </td>
    <td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.2 "><p id="p34521618101419"><a name="p34521618101419"></a><a name="p34521618101419"></a>You can:</p>
    <a name="ul12885203215142"></a><a name="ul12885203215142"></a><ul id="ul12885203215142"><li>Select a predefined tag value or resource tag value from the drop-down list of the text box.</li><li>Enter a tag value in the text box. A tag key can contain a maximum of 43 Unicode characters, which can be null. The first and last characters cannot be spaces.<p id="p1110383711457"><a name="p1110383711457"></a><a name="p1110383711457"></a>Contain only uppercase letters (A to Z), lowercase letters (a to z), digits (0-9), hyphens (-), and underscores (_).</p>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.3 "><p id="p14487201712310"><a name="p14487201712310"></a><a name="p14487201712310"></a>value01</p>
    </td>
    </tr>
    </tbody>
    </table>

4.  Click  **OK**.

## Modifying a Tag<a name="section52819319499"></a>

1.  On the  **Cluster Management**  page, click the name of the cluster to which a tag is to be modified, and click the  **Tags**  tab.
2.  Locate the row that contains the tag to be modified, click  **Edit**  in the  **Operation**  column. The  **Edit Tag**  dialog box is displayed.

    **Figure  5**  Editing a tag<a name="fig4728182916311"></a>  
    ![](figures/editing-a-tag.png "editing-a-tag")

3.  Enter the new key value in the  **Value**  text box.
4.  Click  **OK**.

## Deleting a Tag<a name="section882014118493"></a>

1.  On the  **Cluster Management**  page, click the name of the cluster to which a tag is to be deleted, and click the  **Tags**  tab.
2.  Locate the row that contains the tag to be deleted, click  **Delete**  in the  **Operation**  column. The  **Delete Tag**  dialog box is displayed.

    **Figure  6**  Deleting a tag<a name="fig1994815502312"></a>  
    ![](figures/deleting-a-tag.png "deleting-a-tag")

3.  Click  **OK**  to delete the tag.

