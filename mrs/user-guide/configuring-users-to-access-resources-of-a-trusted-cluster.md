# Configuring Users to Access Resources of a Trusted Cluster<a name="EN-US_TOPIC_0125375362"></a>

## Scenario<a name="s04900aab7a0d46dea40d0315c9ce3903"></a>

After cross-cluster mutual trust is configured, permission must be configured for users in the local cluster, so that the users can access the same resources in the peer cluster as the users in the peer cluster.

## Prerequisites<a name="s48f46ce3edfd4566be4cd3d66838e2a9"></a>

The mutual trust relationship has been configured between two clusters \(clusters A and B\). The clients of the clusters have been updated.

## Procedure<a name="s476a669f2e7d4a70a0b734fdd3f6546f"></a>

1.  Log in to MRS Manager of cluster A and choose  **System**  \>  **Manage User**. Check whether cluster A has accounts that are the same as those of cluster B.
    -   If yes, go to  [2](#l19561ff7f8b4469db842fe0beb479e26).
    -   If no, go to  [3](#l3332dd26fdd64330a98ba30f083b7c2d).

2.  <a name="l19561ff7f8b4469db842fe0beb479e26"></a>Click  ![](figures/icon_mrs_up.png)  on the left side of the username to unfold detailed user information. Check the user groups and roles of the accounts to ensure that they have the same permission as the accounts of cluster B.

    For example, user  **admin** of cluster A has the permission to access and create files in the **/tmp** directory of cluster A. Then go to [4](#l30e0cd486de24332a3172a6563226f78).

3.  <a name="l3332dd26fdd64330a98ba30f083b7c2d"></a>Create the accounts in cluster A and bind the accounts to the user group and roles required by the services. Then go to  [4](#l30e0cd486de24332a3172a6563226f78).
4.  <a name="l30e0cd486de24332a3172a6563226f78"></a>Choose  **Service**  \>  **HDFS**  \>  **Instance**. Query **OM IP Address** of **NameNode\(Active\)**.
5.  Log in to the client of cluster B.

    For example, if you have updated the client on the Master2 node, log in to the Master2 node to use the client. For details, see  [Client Management](client-management.md).

6.  Run the following command to access the  **/tmp**  directory of cluster A.

    **hdfs dfs -ls hdfs://192.168.6.159:25000/tmp**

    In the preceding command,  **192.168.6.159** is the IP address of the active NameNode of cluster A; **9820**  is the default port for communication between the client and the NameNode.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >For MRS 1.6.2 or earlier, the default port is  **25000**. For details, see  [List of Open Source Component Ports](list-of-open-source-component-ports.md).  

7.  Run the following command to create a file in the  **/tmp**  directory of cluster A.

    **hdfs dfs -touchz hdfs://192.168.6.159:25000/tmp/mrstest.txt**

    If you can query the  **mrstest.txt**  file in the  **/tmp**  directory of cluster A, the cross-cluster mutual trust is configured successfully.


