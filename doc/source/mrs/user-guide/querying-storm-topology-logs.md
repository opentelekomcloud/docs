# Querying Storm Topology Logs<a name="EN-US_TOPIC_0125375996"></a>

## Scenario<a name="s9991ee397bad464ea623d33b0f621628"></a>

Users can query topology logs to check the execution of a Storm topology in a worker process. To query the data processing logs of a topology, users must enable the  **Debug** function when submitting the topology. Only streaming clusters with Kerberos authentication enabled support this function. In addition, the user who queries topology logs must be the one who submits the topology or a member of the  **stormadmin**  group.

## Prerequisites<a name="s4fa6cbab610d47ceb9a3af944b5d5c0c"></a>

-   The network of the work environment has been configured according to  [Related Operation](accessing-mrs-manager-supporting-kerberos-authentication.md#section5824002417933).
-   The sampling function has been enabled for the topology.

## Querying Worker Process Logs<a name="s965e2bb07dbc44a3b7429b49b49df832"></a>

1.  Access the Storm WebUI.
2.  In the  **Topology Summary**  area, click the desired topology to view details.
3.  Click the desired  **Spouts** or **Bolts** task. In the **Executors \(All time\)** area, click a port in **Port**  to view detailed logs.

## Querying Data Processing Logs of the Topology<a name="sd672b6b4584f494aa21ff0012ba38709"></a>

1.  Access the Storm WebUI.
2.  In the  **Topology Summary**  area, click the desired topology to view details.
3.  Click  **Debug**, specify the data sampling ratio, and click **OK**.
4.  Click the  **Spouts** or **Bolts** task. In **Component summary**, click **events**  to view data processing logs.

