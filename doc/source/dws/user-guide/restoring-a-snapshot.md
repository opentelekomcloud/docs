# Restoring a Snapshot<a name="en-us_topic_0053720821"></a>

## Scenario<a name="section5077928895949"></a>

This section describes how to restore a snapshot when you want to check point-in-time snapshot data of the cluster. To ensure that the services of the cluster for which you want to restore the snapshot are uninterrupted, DWS creates a new cluster with the same flavor and node quantity as the original cluster by default and imports the snapshot data. 

## Prerequisites<a name="section6649278810248"></a>

-   The number of nodes in the cluster for which you want to restore snapshots must be less than or equal to the user's remaining node quota.
-   The status of the snapshot is  **Available**.

## Restoring a Snapshot to a New Cluster<a name="section1075799010355"></a>

1.  Log in to the DWS management console.
2.  In the navigation tree on the left, click  **Snapshot Management**.

    All snapshots are displayed by default.

3.  In the  **Operation**  column of the snapshot that you want to restore, click  **Restore**.
4.  Configuring parameters for the new cluster.

    You can only configure the following parameters. Retain values of other parameters. For details, see  [Creating a Cluster](creating-a-cluster.md).

    -   **Region**
    -   **AZ**
    -   **Cluster Name**
    -   **Database Port**
    -   **VPC**
    -   **Subnet**
    -   **Security Group**
    -   **EIP**
    -   **Advanced Settings**

        When  **Custom**  is selected, set the following parameters:

        -   **Parameter Group**
        -   **Tag**
        -   **Automated Snapshot**

            When  **Automated Snapshot**  is enabled, set the following parameters:

            -   **Retention Days**
            -   **Start Time**
            -   **Execution Period**


5.  Click  **Restore Now**.
6.  Click  **Submit**  to restore the snapshot to the new cluster.

    >![](/images/icon-note.gif) **NOTE:**   
    >If the number of applied nodes, vCPU \(cores\), or memory \(GB\) exceed the user's remaining quota, a warning dialog box is displayed indicating insufficient quota and displaying the detailed remaining quota and the current quota application information. In this case, you can click  **Increase quota**  in the warning dialog box to submit a work order and apply for higher node quota.  
    >For details about quota, see  [What Is User Quota?](what-is-user-quota.md).  

    When the status of the new cluster changes to  **Available**, the snapshot is restored.

    After the snapshot is restored, the private network address and EIP \(if  **EIP**  is set to  **Automatically assign**\) are automatically assigned. 


