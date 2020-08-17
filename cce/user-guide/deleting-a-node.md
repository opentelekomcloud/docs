# Deleting a Node<a name="cce_01_0186"></a>

When a node in a CCE cluster is deleted, services running on the node will also be deleted. Exercise caution when performing this operation.

>![](public_sys-resources/icon-notice.gif) **NOTICE:** 
>After a CCE cluster is deleted, the ECS nodes in the cluster are also deleted.

## Background<a name="section83421713122615"></a>

-   Deleting a node will lead to pod migration, which may affect services. Perform this operation during off-peak hours.
-   Unexpected risks may occur during the operation. Back up related data in advance.
-   During the operation, the backend will set the node to the unschedulable state.
-   Only worker nodes can be deleted, and master nodes cannot.

## Procedure<a name="section727210277269"></a>

1.  Log in to the CCE console. In the navigation pane, choose  **Resource Management**  \>  **Nodes**. In the same row as the node you will delete, choose  **Operation**  \>  **More \> Delete**.
2.  In the  **Delete Node**  dialog box, enter  **DELETE**  and click  **Yes**.

    >![](public_sys-resources/icon-note.gif) **NOTE:** 
    >After the node is deleted, workload pods on the node are automatically migrated to other available nodes.


