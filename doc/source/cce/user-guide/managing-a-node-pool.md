# Managing a Node Pool<a name="cce_01_0222"></a>

## Editing a Node Pool<a name="section359343125016"></a>

1.  Log in to the CCE console. In the navigation pane, choose  **Resource Management**  \>  **Node Pool**.
2.  In the upper right corner of the displayed page, select a cluster to filter node pools by cluster.
3.  Click  **Edit**  next to the name of the node pool you will edit. In the  **Edit Node Pool**  dialog box, edit the following parameters:

    **Table  1**  Editing node pool parameters

    <a name="table16321825732"></a>
    <table><thead align="left"><tr id="row173212251235"><th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.2.3.1.1"><p id="p43211725338"><a name="p43211725338"></a><a name="p43211725338"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="72%" id="mcps1.2.3.1.2"><p id="p0322102516320"><a name="p0322102516320"></a><a name="p0322102516320"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row163229255313"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="p1232219251339"><a name="p1232219251339"></a><a name="p1232219251339"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="p129475498531"><a name="p129475498531"></a><a name="p129475498531"></a>Name of the node pool.</p>
    </td>
    </tr>
    <tr id="row6334727910"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="p233592498"><a name="p233592498"></a><a name="p233592498"></a>Nodes</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="p149431649155313"><a name="p149431649155313"></a><a name="p149431649155313"></a>Modify the number of nodes based on service requirements.</p>
    </td>
    </tr>
    <tr id="row111551253912"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="p51551451293"><a name="p51551451293"></a><a name="p51551451293"></a>Autoscaler</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="p20736112217461"><a name="p20736112217461"></a><a name="p20736112217461"></a>By default, autoscaler is disabled.</p>
    <p id="p1063941211266"><a name="p1063941211266"></a><a name="p1063941211266"></a>After you click <a name="en-us_topic_0107283640_image17351426631"></a><a name="en-us_topic_0107283640_image17351426631"></a><span><img id="en-us_topic_0107283640_image17351426631" src="figures/icon-autoscalerenable.png"></span> to enable autoscaler, nodes in the node pool will be automatically created or deleted to match the changeable cluster load. You can set <strong id="b10691164321810"><a name="b10691164321810"></a><a name="b10691164321810"></a>Maximum Nodes</strong> and <strong id="b1169234371818"><a name="b1169234371818"></a><a name="b1169234371818"></a>Minimum Nodes</strong> to ensure that the number of nodes will always fall within a specified range.</p>
    <p id="p12614171015488"><a name="p12614171015488"></a><a name="p12614171015488"></a>If the <strong id="b18191718101819"><a name="b18191718101819"></a><a name="b18191718101819"></a>Autoscaler</strong> field is set to on, install the <a href="autoscaler.md">autoscaler add-on</a> to use the autoscaler feature.</p>
    </td>
    </tr>
    </tbody>
    </table>

4.  After the configuration is complete, click  **Save**.

    In the node pool list, the node pool status is  **Scaling**. After the status changes to  **Complete**, the node pool parameters are edited successfully.


## Deleting a Node Pool<a name="section135941731115017"></a>

Deleting a node pool will delete nodes in the pool. Pods on these nodes will be automatically migrated to available nodes in other node pools. If pods in the node pool have a specific node selector and none of the other nodes in the cluster satisfies the node selector, the pods will become unschedulable.

1.  Log in to the CCE console. In the navigation pane, choose  **Resource Management**  \>  **Node Pool**.
2.  In the upper right corner of the displayed page, select a cluster to filter node pools by cluster.
3.  Choose  **Delete**  next to a node pool name to delete the node pool.
4.  Read the precautions in the  **Delete Node Pool**  dialog box.
5.  Enter  **DELETE**  in the text box and click  **Yes**  to confirm that you want to continue the deletion.

    **Figure  1**  Deleting a Node Pool<a name="fig12491145671314"></a>  
    ![](figures/deleting-a-node-pool.png "deleting-a-node-pool")


