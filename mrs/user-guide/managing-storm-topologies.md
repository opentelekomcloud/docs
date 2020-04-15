# Managing Storm Topologies<a name="EN-US_TOPIC_0125375807"></a>

## Scenario<a name="s7241a33714434c3c86a42d0b86202aa3"></a>

Users can manage Storm topologies on the Storm WebUI. Users in the  **storm**  group can manage only the topology tasks submitted by themselves, while users in the  **stormadmin**  group can manage all topology tasks.

## Procedure<a name="s302af2162d64497dbe5a25d453205456"></a>

1.  Access the Storm WebUI.
2.  In the  **Topology summary**  area, click the desired topology.
3.  Use options in  **Topology actions**  to manage the Storm topology.
    -   Activate the topology.

        Click  **Activate**  to activate the topology.

    -   Deactivate the topology.

        Click  **Deactivate**  to deactivate the topology.

    -   Re-deploy the topology.

        Click  **Rebalance**  and specify the wait time \(in seconds\) of re-deployment. Generally, if the number of nodes in a cluster changes, the topology can be re-deployed to maximize resource usage.

    -   Delete the topology.

        Click  **Kill**  and specify the wait time \(in seconds\) of the deletion.

    -   Start or stop sampling messages.

        Click  **Debug**. In the dialog box that is displayed, specify the percentage of the sampled data volume. For example, if the value is set to **10**, 10% of data is sampled.

        To stop sampling, click  **Stop Debug**.

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >This function is available only when the sampling function is enabled during topology submission. For details about querying data processing information, see  [Querying Data Processing Logs of the Topology](querying-storm-topology-logs.md#sd672b6b4584f494aa21ff0012ba38709).  

    -   Modify the topology log level.

        Click  **Change Log Level**  to specify the new log level.

4.  Display the topology.

    In the  **Topology Visualization** area, click **Show Visualization**  to visualize the topology.


