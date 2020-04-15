# Submitting Storm Topologies on the Client<a name="EN-US_TOPIC_0125375477"></a>

## Scenario<a name="sf154793f16a84d6a840ec3e546d59de4"></a>

Users can submit Storm topologies on the MRS cluster client to continuously process stream data. For clusters with Kerberos authentication enabled, users who submit topologies must be members of the  **stormadmin**  or  **storm**  group.

## Prerequisites<a name="scd6d79e243e140a58560c94f542d2f1e"></a>

The client has been updated.

## Procedure<a name="s218c77151fa24a1586a68dbcbb4ca255"></a>

1.  Log in to the node where the client is installed.

    For example, if you have updated the client on the Master2 node, log in to the Master2 node to use the client. For details, see  [Client Management](client-management.md).

2.  Run the following command to switch the user:

    **sudo su - omm**

3.  Run the following command to switch to the client directory, for example,  **/opt/client**:

    **cd /opt/client**

4.  Run the following command to configure the environment variables:

    **source bigdata\_env**

5.  If Kerberos authentication is enabled, run the following command to authenticate the user. If Kerberos authentication is disabled, skip this step.

    **kinit** _**Storm username**_

    For example,  **kinit admin**

6.  Run the following command to submit the Storm topology:

    **storm jar** _**Topology package path Class name of the main topology method Topology name**_

    If the following information is displayed, the topology is submitted successfully.

    ```
    Finished submitting topology: topo1
    ```

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   To support sampling messages, add the  **topology.debug** and **topology.eventlogger.executors**  parameters. For example:  
    >    **_Topology package path Class name of the main topology method Topology name_storm jar -c topology.debug=true -c topology.eventlogger.executors=1**  
    >-   Data processing methods vary with topologies. The topology in the example generates characters randomly and separates character strings. To query the processing status, enable the sampling function and perform operations according to  [Querying Data Processing Logs of the Topology](querying-storm-topology-logs.md#sd672b6b4584f494aa21ff0012ba38709).  

7.  Run the following command to query Storm topologies. For clusters with Kerberos authentication enabled, only users in the  **stormadmin**  or  **storm**  group can query all topologies.

    **storm list**


