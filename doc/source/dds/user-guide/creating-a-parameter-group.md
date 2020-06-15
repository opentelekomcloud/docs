# Creating a Parameter Group<a name="en-us_topic_parameter_group"></a>

## **Scenarios**<a name="section10048988195440"></a>

DB parameter groups act as a container for engine configuration values that are applied to one or more DB instances. This section guides you on how to create a parameter group to manage your DB instance configurations.

>![](/images/icon-note.gif) **NOTE:**   
>-   DDS does not share parameter group quotas with RDS.  
>-   Each account can create a maximum of 1000 DDS parameter groups for the cluster and replica set instances.  

## Cluster<a name="section23494442161723"></a>

1.  [Log in to the DDS console.](logging-in-to-the-dds-console.md)
2.  In the navigation pane on the left, click  **Parameter Group Management**.
3.  On the  **Parameter Group Management**  page, click  **Create Parameter Group**.
4.  Specify  **DB Engine Version**,  **DB Instance Type**,  **Node Type**,  **Parameter Group Name**, and  **Description**  and then click  **OK**.
    -   **Node Type**: specifies the node type that this parameter group will apply to. For example, to create a parameter group applying to config, select  **config**.
    -   **Parameter Group Name**: specifies the parameter group name, which is a string of 1 to 64 characters composed of only letters \(case-sensitive\), digits, hyphens \(-\), underscores \(\_\), and periods \(.\).
    -   **Description**: contains a maximum of 256 characters and cannot contain the carriage return character and the following special characters: \>!<"&'=

5.  On the  **Parameter Group Management**  page, view and manage parameter groups on the  **Clusters**  tab.

## Replica Set<a name="section47857970184222"></a>

1.  [Log in to the DDS console.](logging-in-to-the-dds-console.md)
2.  In the navigation pane on the left, click  **Parameter Group Management**.
3.  On the  **Parameter Group Management**  page, click  **Create Parameter Group**.
4.  Specify  **DB Engine Version**,  **DB Instance Type**,  **Parameter Group Name**, and  **Description**  and then click  **OK**.
    -   **Parameter Group Name**: specifies the parameter group name, which is a string of 1 to 64 characters composed of only letters \(case-sensitive\), digits, hyphens \(-\), underscores \(\_\), and periods \(.\).
    -   **Description**: contains a maximum of 256 characters and cannot contain the carriage return character and the following special characters: \>!<"&'=

5.  On the  **Parameter Group Management**  page, view and manage parameter groups on the  **Replica Sets**  tab.

