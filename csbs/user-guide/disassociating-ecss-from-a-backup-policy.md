# Disassociating ECSs from a Backup Policy<a name="EN-US_TOPIC_0056584632"></a>

When an ECS associated with a backup policy no longer needs to be backed up, you can disassociate it from the backup policy.

## Prerequisites<a name="section827113912477"></a>

-   You have created at least one backup policy.
-   The backup policy is associated with at least one ECS.

## Procedure<a name="section10737011135117"></a>

1.  Log in to the CSBS management console.
    1.  Log in to the management console.
    2.  Click  ![](figures/icon-region.png)  in the upper left corner of the management console and select a region and a project.
    3.  Click  ![](figures/icon-servicelist.png). Under  **Storage**, click  **Cloud Server Backup Service**.

2.  Click the  **Policies**  tab.
3.  In the row of the backup policy from which you want to disassociate the ECS, click  ![](figures/icon-down(2).png).
4.  Under  **Associated Servers**, click  **Disassociate**  in the row of the target ECS, or select the target ECS from the list and then click  **Disassociate**  in the upper left corner of the list.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   When the target ECS is being backed up, you can still disassociate it. However, the backup job will continue and backups will be generated.  
    >-   After an ECS is disassociated from the associated backup policy, its existing backups will not be deleted. If you want to delete them, manually delete them.  

5.  Click  **OK**.

