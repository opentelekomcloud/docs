# Managing Cluster Tags<a name="EN-US_TOPIC_0125375579"></a>

Tags are used to identify clusters. Adding tags to clusters can help you identify and manage your cluster resources.

You can add a maximum of 10 tags to a cluster when creating the cluster or add them on the details page of the created cluster.

A tag consists of a tag key and a tag value.  [Table 1](#table16316649132010)  provides tag key and value requirements.

**Table  1**  Tag key and value requirements

<a name="table16316649132010"></a>
<table><thead align="left"><tr id="row63177491201"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p1861341272817"><a name="p1861341272817"></a><a name="p1861341272817"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p161321232818"><a name="p161321232818"></a><a name="p161321232818"></a>Requirement</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p4614131262812"><a name="p4614131262812"></a><a name="p4614131262812"></a>Example</p>
</th>
</tr>
</thead>
<tbody><tr id="row93171449162013"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p931774942019"><a name="p931774942019"></a><a name="p931774942019"></a>Key</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><a name="ul108861315388"></a><a name="ul108861315388"></a><ul id="ul108861315388"><li>This field cannot be left blank.</li><li>A tag key must be unique for a cluster.</li><li>A tag key contains a maximum of 36 characters.</li><li>Only digits, letters, underscores (_), hyphens (-) are allowed.</li></ul>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p2317144913209"><a name="p2317144913209"></a><a name="p2317144913209"></a>Organization</p>
</td>
</tr>
<tr id="row193176495203"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p931714916209"><a name="p931714916209"></a><a name="p931714916209"></a>Value</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><a name="ul1221649193817"></a><a name="ul1221649193817"></a><ul id="ul1221649193817"><li>A tag value contains a maximum of 64 characters.</li><li>Only digits, letters, underscores (_), hyphens (-) are allowed.</li></ul>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p431704919201"><a name="p431704919201"></a><a name="p431704919201"></a>Apache</p>
</td>
</tr>
</tbody>
</table>

You can perform the following operations on tags:

-   On the  **Create Cluster**  page, add tags to a cluster when creating the cluster. For details, see [Adding Tags to a Cluster](#section157211552192112).
-   On the  **Active Cluster** page, search for the target cluster by tag key or tag value. For details, see [Searching for the Target Cluster](#section17182338172517).
-   On the  **Tag** tab page of an existing cluster, view, add, modify, and delete tags. For details, see [Managing Tags](#section8744161572618).

## Adding Tags to a Cluster<a name="section157211552192112"></a>

You perform the following operations to add tags to a cluster when creating the cluster.

>![](/images/icon-note.gif) **NOTE:**   
>You can also add tags to an existing cluster. For details, see  [Managing Tags](#section8744161572618).  

1.  Log in to the management console.
2.  Click  **Create Cluster**  to go to the cluster creation page.
3.  In  **Advanced Settings**, select **Configure**.

    Enter the key and value of a tag to be added.

    You can add a maximum of 10 tags to a cluster and use intersections of tags to search for the target cluster.


## Searching for the Target Cluster<a name="section17182338172517"></a>

On the  **Active Cluster**  page, search for the target cluster by tag key or tag value.

1.  Log in to the management console.
2.  In the upper right corner of the  **Active Cluster** page, click **Search by Tag**  to access the search page.

    **Figure  1**  Searching by tag<a name="fig2631298318931"></a>  
    ![](figures/searching-by-tag.png "searching-by-tag")

3.  Enter the tag of the cluster to be searched.

    You can select a tag key or tag value from their drop-down lists. When the tag key or tag value is exactly matched, the system can automatically locate the target cluster. If you enter multiple tags, their intersections are used to search for the cluster.

4.  Click  **Search**.

    The system searches for the target cluster by tag key or value.


## Managing Tags<a name="section8744161572618"></a>

You can view, add, modify, and delete tags on the  **Tag**  tab page of the cluster.

1.  Log in to the management console.
2.  On the  **Active Cluster**  page, click the name of a cluster for which you want to manage tags.

    The cluster details page is displayed.

3.  Click the  **Tags**  tab and view, add, modify, and delete tags on the tab page.
    -   View

        On the  **Tags**  tab page, you can view details about tags of the cluster, including the number of tags and the key and value of each tag.

    -   Add

        Click  **Add Tag**  in the upper left corner. In the displayed **Add Tag** dialog box, enter the key and value of the tag to be added, and click **OK**.

    -   Modify

        In the  **Operation** column of the tag, click **Edit**. In the displayed **Edit Tag** page, enter new tag value and click **OK**.

    -   Delete

        In the  **Operation** column of the tag, click **Delete**. After confirmation, click **OK**  in the displayed **Delete Tag**  page.

        >![](/images/icon-note.gif) **NOTE:**   
        >MRS cluster tag updates will be synchronized to every ECS in the cluster. You are advised not to modify ECS tags on the ECS console to prevent inconsistency between ECS tags and MRS cluster tags. If the number of tags of an ECS in the MRS cluster reaches the upper limit, you cannot create any tag for the MRS cluster.  



