# Executing a Backup Policy at Once<a name="EN-US_TOPIC_0056584626"></a>

You can manually execute a backup policy to back up an associated ECS immediately.

## Context<a name="section23057992172444"></a>

-   If an ECS is being backed up, you cannot manually execute a backup policy on it.
-   If a manual backup job is still in progress, scheduled automatic backup operations will be postponed to the next backup cycle. An interval of at least 3 hours is recommended between a manual backup operation and a scheduled automatic backup operation.

## Prerequisites<a name="section32767464153317"></a>

At least one backup policy has been created and has been associated with at least one ECS.

## Procedure<a name="section63279899152627"></a>

1.  Log in to the CSBS management console.
    1.  Log in to the management console.
    2.  Click  ![](figures/icon-region.png)  in the upper left corner of the management console and select a region and a project.
    3.  Click  ![](figures/icon-servicelist.png). Under  **Storage**, click  **Cloud Server Backup Service**.

2.  Click the  **Policies**  tab.
3.  In the upper right corner of the backup policy you want to execute, choose  **More**  \>  **Backup Now**.
4.  Click  **OK**.

