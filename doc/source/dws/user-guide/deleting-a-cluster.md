# Deleting a Cluster<a name="dws_01_0025"></a>

## Scenario<a name="section43782126162722"></a>

You can delete and redundant or unwanted clusters from your DWS.

## Impact on the System<a name="section6977716114930"></a>

You cannot restore any clusters that you have deleted. Additionally, you cannot access user data in the deleted cluster because the data is automatically deleted.

## Procedure<a name="section13594386114220"></a>

1.  Log in to the management console at  [https://console.otc.t-systems.com/dws/](https://console.otc.t-systems.com/dws/).
2.  Click  **Cluster Management**.

    All clusters are displayed by default.

3.  In the cluster list, locate the row containing the cluster to be deleted, and choose  **More**  \>  **Delete**  in the  **Operation**  column.
4.  \(Optional\) If the cluster status is in the normal state, click  **Create Cluster Snapshot**  on the pop-up window to create a new snapshot for the cluster that you want to delete.

    For details about how to create a cluster snapshot, see  [Manually Creating a Snapshot](manually-creating-a-snapshot.md).

5.  \(Optional\) If the cluster is bound with an EIP, you can click  **Release the EIP bound with the cluster**  to release the EIP of the cluster to be deleted.
6.  Click  **OK**.

    If the cluster to be deleted uses an automatically created security group that is not used by other clusters, the security group is automatically deleted when the cluster is deleted.


