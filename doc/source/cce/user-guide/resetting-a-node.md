# Resetting a Node<a name="cce_01_0003"></a>

Resetting a node in the cluster will delete the node itself and the services running on it. Exercise caution when performing this operation.

## Context<a name="section83421713122615"></a>

-   Resetting a node will lead to pod migration, which may affect services. Therefore, delete nodes during off-peak hours.
-   Unexpected risks may occur during node deletion. Back up related data in advance.
-   While the node is being reset, the backend will set the node to the unschedulable state.
-   Only worker nodes can be reset.

## Procedure<a name="section2360193212113"></a>

1.  Log in to the CCE console. In the navigation pane, choose  **Resource Management**  \>  **Nodes**. In the same row as the node you will reset, choose  **Operation**  \>  **More \> Reset**.
2.  In the  **Reset**  dialog box displayed, enter  **RESET**  and set  **Key pair**.

    **Figure  1**  Resetting the selected node<a name="fig10143855684"></a>  
    ![](figures/resetting-the-selected-node.png "resetting-the-selected-node")

3.  Set parameters as required and click  **Yes**.

    After the node is reset, workload pods on the node are automatically migrated to other available nodes.


