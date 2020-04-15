# Scaling Up Master Node Specifications<a name="EN-US_TOPIC_0221415041"></a>

As users' increasing services lead to Core node scale-out and high CPU usage, Master node specifications cannot meet user requirements and need to be scaled up. This section describes how to scale up Master node specifications. Note that Master node specifications can be scaled up only for clusters with the cluster HA function enabled.

## Procedure \(for Versions Later Than MRS 1.7.2\)<a name="section9102175113472"></a>

1.  Log in to the MRS management console.
2.  In the left navigation pane, choose  **Clusters**  \>  **Active Clusters**, select the cluster for which you want to scale up Master node specifications, and click its name to switch to the cluster details page.
3.  On the  **Nodes**  tab page, select  **Scale Up Specifications**  in the  **Operation**  column of the Master node group. The  **Scale Up Master Node Specifications**  page is displayed.
4.  Select the target specifications and click  **Submit Order**. The order has been submitted successfully.

    The node specifications scale-up takes some time. After the scale-up is successful, the cluster status changes to  **Running**.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >The VM to be scaled up is automatically stopped during the scale-up and started after the scale-up is complete.  


## Procedure \(for MRS 1.7.2 or Earlier\)<a name="section43251723164812"></a>

**Preparing for Scaling Up Master Node Specifications**

1.  <a name="li487181481727"></a>Log in to the MRS management console.
2.  In the left navigation pane, choose  **Clusters**  \>  **Active Clusters**, select the cluster for which you want to scale up Master node specifications, and click its name to switch to the cluster details page.
3.  Ensure that the cluster status is  **Running**.
4.  On the  **Nodes**  tab page, ensure that all nodes in the cluster are in the  **Running**  state.
5.  Log in to MRS Manager and go to the cluster management page. For details, see  [Accessing MRS Manager](accessing-mrs-manager.md)  or  [Accessing MRS Manager Supporting Kerberos Authentication](accessing-mrs-manager-supporting-kerberos-authentication.md).
6.  Choose  **Services**  \>  **ZooKeeper**  \>  **Service Status**  and ensure that  **Health Status**  of the ZooKeeper service is  **Good**.
7.  Update service parameter settings as required. For details, see  [Configuring Service Parameters](configuring-service-parameters.md).

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >You need to perform this step only once before scaling up the standby Master node.  

8.  <a name="li36491855204611"></a>Choose  **Services**  \>  **HDFS**  \>  **Instance**.
9.  <a name="li3448141413114"></a>Record the business IP address of  **NameNode \(Standby\)**. When scaling up the specifications of the active Master node, record the business IP address of  **NameNode \(Active\)**. 

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >Only when the cluster is an analysis cluster, you can perform  [8](#li36491855204611)  to  [9](#li3448141413114)  to record the IP addresses of the active and standby nodes.  

10. On the upper right of the MRS Manager page, check the number next to the  ![](figures/icon_mrs_tasknum.jpg)  icon. If the number is 0, there is no running tasks in the cluster.
11. Click  **Hosts**. If the cluster is an analysis cluster, select the checkbox of the host corresponding to the business IP address of the  **NameNode**  recorded in  [9](#li3448141413114). If the cluster is a streaming cluster, you do not need to distinguish the active and standby nodes. You only need to choose hosts for the scale-up.
12. <a name="li12169193211415"></a>Choose  **More**  \>  **Stop All Roles**  and wait until all roles are stopped.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   When the node where MRS Manager resides is scaled up, MRS Manager may not be accessed due to an active/standby switchover. It is a normal phenomenon. Try to log in to MRS Manager later. If the login fails for a long time, contact O&M personnel.  
    >-   After all roles are stopped, the following alarms may be generated. After the scale-up of Master node specifications is complete and all roles are started, the alarms are automatically cleared.  
    >    -   [ALM-12006 Node Fault](alm-12006-node-fault.md)  
    >    -   [ALM-12010 Manager Heartbeat Interruption Between the Active and Standby Nodes](alm-12010-manager-heartbeat-interruption-between-the-active-and-standby-nodes.md)  
    >    -   [ALM-12039 GaussDB Data Is Not Synchronized](alm-12039-gaussdb-data-is-not-synchronized.md)  
    >    -   [ALM-14000 HDFS Service Unavailable](alm-14000-hdfs-service-unavailable.md)  
    >    -   [ALM-14010 NameService Service Is Abnormal](alm-14010-nameservice-service-is-abnormal.md)  
    >    -   [ALM-14012 HDFS JournalNode Data Is Not Synchronized](alm-14012-hdfs-journalnode-data-is-not-synchronized.md)  
    >    -   [ALM-16004 Hive Service Unavailable](alm-16004-hive-service-unavailable.md)  
    >    -   [ALM-18000 Yarn Service Unavailable](alm-18000-yarn-service-unavailable.md)  
    >    -   [ALM-19000 HBase Service Unavailable](alm-19000-hbase-service-unavailable.md)  
    >    -   [ALM-20002 Hue Service Unavailable](alm-20002-hue-service-unavailable.md)  
    >    -   [ALM-23001 Loader Service Unavailable](alm-23001-loader-service-unavailable.md)  
    >    -   [ALM-27001 DBService Unavailable](alm-27001-dbservice-unavailable.md)  
    >    -   [ALM-27003 DBService Heartbeat Interruption Between the Active and Standby Nodes](alm-27003-dbservice-heartbeat-interruption-between-the-active-and-standby-nodes.md)  
    >    -   [ALM-27004 Data Inconsistency Between Active and Standby DBServices](alm-27004-data-inconsistency-between-active-and-standby-dbservices.md)  
    >    -   [ALM-43001 Spark Service Unavailable](alm-43001-spark-service-unavailable.md)  


**Scaling Up Master Node Specifications**

1.  Log in to the MRS management console.
2.  In the left navigation pane, choose  **Clusters**  \>  **Active Clusters**, select the cluster for which you want to scale up Master node specifications, and click its name to switch to the cluster details page.
3.  On the  **Nodes**  tab page, select  **Scale Up Specifications**  in the  **Operation**  column of the Master node group.
4.  Select the target specifications and click  **Next**.
5.  On the  **Confirm**  page that is displayed, confirm the target node specifications and fees and click  **OK**.
6.  Ensure that all services on the standby Master node have been stopped. For operation details, refer to  [1](#li487181481727)  to  [12](#li12169193211415)  in the  **Preparing for Scaling Up Master Node Specifications**  part. On the  **Scale Up Master Node Specifications**  page, select  **Are you sure you have stopped all services on the standby Master node?**  and  **If not all services are stopped before the scale-up, data saving failure or data damage may occur.**  and click  **Submit Order**.
7.  On the  **Warning**  page that is displayed, confirm again that all services on the standby Master node are stopped and click  **OK**  to start scaling up the specifications of the standby Master node.

    The node specifications scale-up takes some time. Please wait. After the scale-up is successful, the cluster status changes to  **Scaled-up-first**. Otherwise, contact O&M personnel.

8.  After the standby Master node has been scaled up successfully, start all services and set parameters on the standby Master node by referring to  [1](#li1571022151014)  to  [11](#li47118211017)  in the  **Operations After the Master Node Specifications Scale-up**  part.
9.  After the services on the standby Master node are started, perform an active/standby NameNode switchover. Perform this step only for an analysis cluster and skip this step for a streaming cluster.
    1.  Access the NameNode web UI of the active and standby nodes separately. For details about how to access the NameNode web UI, see  [11](#li47118211017).
    2.  <a name="li67484244318"></a>In the navigation bar on the NameNode web UI, choose  **Overview**  and record the NameNode IDs of the active and standby nodes. Do not close the page after recording.

        **Figure  1**  NameNode ID of the active node<a name="fig72881017493"></a>  
        ![](figures/namenode-id-of-the-active-node.png "namenode-id-of-the-active-node")

    3.  Log in to the ECS of any Master node and run the following command to configure environment variables:

        ```
        source /opt/client/bigdata_env
        ```

    4.  If the Kerberos authentication is enabled for the current cluster, run the following command to authenticate the user. If the Kerberos authentication is disabled for the current cluster, skip this step.

        ```
        kinit MRS cluster user
        ```

        For example,  **kinit admin**.

    5.  Run the following command to perform an active/standby NameNode switchover:

        ```
        hdfs haadmin -failover <NameNode ID of the active node> <NameNode ID of the standby node>
        ```

    6.  Go to the NameNode web UI page that is not closed in  [9.b](#li67484244318)  and refresh the page. You can view that the active/standby NameNode switchover is complete.

        **Figure  2**  NameNode<a name="fig3872103795519"></a>  
        ![](figures/namenode.png "namenode")

10. Stop all services on the active Master node by referring to  [1](#li487181481727)  to  [12](#li12169193211415)  in the  **Preparing for Scaling Up Master Node Specifications**  part.
11. On the  **Scale Up Master Node Specifications**  page, select  **I confirm that all services on the standby Master node have been started.**  and  **I confirm that all services on the active Master node have been stopped.**  and click  **Submit**.
12. On the  **Confirm**  page that is displayed, confirm again that all services on the active Master node are stopped and click  **OK**  to start scaling up the specifications of the active Master node.

    The node specifications scale-up takes some time. Please wait. After the scale-up is successful, the cluster status changes to  **Scaled-up-success**. Otherwise, contact O&M personnel.

13. Start all services and set parameters on the active Master node by referring to  [1](#li1571022151014)  to  [11](#li47118211017)  in the  **Operations After the Master Node Specifications Scale-up**  part.
14. On the  **Scale Up Master Node Specifications**  page, select  **Are you sure you have started all services on the active Master node?**  and click  **OK**  to complete the scale-up.

**Operations After the Master Node Specifications Scale-up**

1.  <a name="li1571022151014"></a>Log in to MRS Manager and go to the cluster management page. For details, see  [Accessing MRS Manager](accessing-mrs-manager.md)  or  [Accessing MRS Manager Supporting Kerberos Authentication](accessing-mrs-manager-supporting-kerberos-authentication.md).
2.  Click  **Hosts**. Check basic information about the host corresponding to the business IP address of the NameNode recorded in  [9](#li3448141413114)  in the  **Preparing for Scaling Up Master Node Specifications**  part. If the  **Health Status**  is  **Good**  and  **Disk Usage**,  **Memory Usage**, and  **CPU Usage**  have values, perform  [9](#li1271115271019). If any of the preceding conditions is not met, go to the next step.
3.  Log in to the standby Master node remotely. For details, see  [Logging In to a Master Node](logging-in-to-a-master-node.md).
4.  Run the following command to switch to user  **omm**:

    ```
    su - omm
    ```

5.  Run the following command to start the Agent:

    ```
    sh /opt/Bigdata/nodeagent/bin/start-agent.sh
    ```

6.  Run the following command to check whether the Agent is started successfully:

    ```
    jps | grep NodeAgent
    ```

7.  Log in to MRS Manager and go to the cluster management page. For details, see  [Accessing MRS Manager](accessing-mrs-manager.md)  or  [Accessing MRS Manager Supporting Kerberos Authentication](accessing-mrs-manager-supporting-kerberos-authentication.md).
8.  Click  **Hosts**. Check basic information about the host corresponding to the business IP address of the NameNode recorded in  [9](#li3448141413114)  in the  **Preparing for Scaling Up Master Node Specifications**  part to ensure that  **Health Status**  is  **Good**  and  **Disk Usage**,  **Memory Usage**, and  **CPU Usage**  have values.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >It may take 3 minutes until the host status is normal after the Agent is started successfully. Please wait. If the host status is abnormal for a long time, contact O&M personnel.  

9.  <a name="li1271115271019"></a>On the MRS Manager page, click  **Hosts**  and select the checkbox of the host corresponding to the business IP address of the NameNode recorded in  [9](#li3448141413114)  in the  **Preparing for Scaling Up Master Node Specifications**  part.
10. Choose  **More**  \>  **Start All Roles**  and wait until all roles are started.
11. <a name="li47118211017"></a>Access the NameNode web UI and check the NameNode startup status.

    1.  On the MRS management console, click  **Clusters**.
    2.  On the  **Active Clusters**  page, click the name of the specified cluster.

        On the cluster details page, record the  **AZ**,  **VPC**,  **Cluster Manager IP Address**  of the cluster, and  **Default Security Group**  of the Master node.

    3.  On the ECS management console, create an ECS.

        -   The  **AZ**,  **VPC**, and  **Security Group**  of the ECS must be the same as those of the cluster to be accessed.
        -   Select a Windows public image. For example, select the enterprise image  **Enterprise\_Windows\_STD\_2012R2\_20170316-0\(80GB\)**.
        -   For details about other configuration parameters, see  **Elastic Cloud Server \> User Guide \> Getting Started \> Creating and Logging In to a Windows ECS**.

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >If the security group of the ECS is different from  **Default Security Group**  of the Master node, you can modify the configuration using either of the following methods:  
        >-   Change the security group of the ECS to the default security group of the Master node. For details, see  **Elastic Cloud Server**  \>  **User Guide**  \>  **Security Group**  \>  **Changing a Security Group**.  
        >-   Add two security group rules to the security groups of the Master and Core nodes to enable the ECS to access the cluster. Set  **Protocol**  to  **TCP**  and  **ports**  of the two security group rules to  **28443**  and  **20009**, respectively. For details, see  **Virtual Private Cloud \> User Guide \> Security \> Security Group \> Adding a Security Group**.  

    4.  On the VPC management console, apply for an EIP and bind it to the ECS.

        See  **"Assigning an EIP and Binding It to an ECS" in the** _Virtual Private Cloud User Guide_ **\(Network Components \> EIP \> Assigning an EIP and Binding It to an ECS\)**.

    5.  Log in to the ECS.

        The Windows system account, password, EIP, and the security group rules are required for logging in to the ECS. For details, see  **Elastic Cloud Server \> User Guide \> ECS Logins \> Logging In to a Windows ECS**.

    6.  On the Windows remote desktop, use your browser to access the NameNode web UI.

        For example, you can use Internet Explorer 11 in the Windows 2012 OS.

        The address format of the NameNode web UI is as follows:

        -   Applicable to MRS 1.6.3 or earlier

            **http://_IP address of the active NameNode role instance_:25002/dfshealth.html\#tab-overview**

        -   Applicable to versions later than MRS 1.6.3 and earlier than MRS 1.9.2.

            **http://_IP address of the active NameNode role instance_:9870/dfshealth.html\#tab-overview**

    7.  Go to the  **NameNode Web UI**  page, choose  **Startup Progress**  in the navigation bar. After ensuring that  **Percent Complete**  is displayed as 100%, go to the next step, as shown in  [Figure 3](#f687f1ab2505e4f519765e6f2a26208e9).

        **Figure  3**  NameNode startup status<a name="f687f1ab2505e4f519765e6f2a26208e9"></a>  
        ![](figures/namenode-startup-status.png "namenode-startup-status")

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >Perform  [11](#li47118211017)  for an analysis cluster and skip this step for a streaming cluster.  


