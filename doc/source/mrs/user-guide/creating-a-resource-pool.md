# Creating a Resource Pool<a name="EN-US_TOPIC_0125375451"></a>

## Scenario<a name="section25729969195856"></a>

On the MRS cluster, users can logically divide Yarn cluster nodes to combine multiple NodeManagers into a Yarn resource pool. Each NodeManager belongs to one resource pool only. The system contains a  **Default** resource pool by default. All NodeManagers that are not added to customized resource pools belong to this default resource pool.

You can create a customized resource pool on MRS Manager and add hosts that have not been added to other customized resource pools to it.

## Procedure<a name="section59066814195916"></a>

1.  On MRS Manager, click  **Tenant**.
2.  Click the  **Resource Pool**  tab.
3.  Click  **Create Resource Pool**.
4.  In  **Create Resource Pool**, set the attributes of the resource pool.
    -   **Name**:

        Enter a name for the resource pool. The name cannot be  **Default**.

        The name contains 1 to 20 characters and can consist of digits, letters, and underscores \(\_\). However, it must not start with underscores.

    -   **Available Hosts**:

        In the host list on the left, select the name of a specified host and click  ![](figures/icon_mrs_addhost.jpg)  to add the selected host to the resource pool. Only hosts in the cluster can be selected. The host list of a resource pool can be left blank.

5.  Click  **OK**  to save the settings.
6.  After the resource pool is created, users can view the  **Name**, **Members**, **Association Mode**, **vCore**, and **Memory** in the resource pool list. Hosts that have been added to the customized resource pool are no longer members of the **Default**  resource pool.

