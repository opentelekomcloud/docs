# Migrating ECSs on DeHs<a name="EN-US_TOPIC_0134865621"></a>

## Scenarios<a name="section17761164816565"></a>

ECSs can be migrated between DeHs and public resource pools.

-   An ECS created on a DeH can be migrated to another DeH.
-   An ECS created on a DeH can be migrated to a public resource pool.
-   An ECS deployed in a public resource pool can be migrated to a DeH.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >Operations in this scenario need to be performed on the ECS console. For details, see  **Migrating an ECS**  in the  _Elastic Cloud Server User Guide_.  


## Notes<a name="section1213835718599"></a>

Only a stopped ECS can be migrated.

## **Procedure**<a name="section12638144614015"></a>

1.  Log in to the management console.
2.  Click  ![](figures/9.png)  in the upper left corner and select the desired region and project.
3.  Under  **Computing**, click  **Dedicated Host**.

    The  **Dedicated Host**  page is displayed.

4.  Click the name of the target DeH in the list of DeHs.

    The DeH details page is displayed.

5.  On the  **ECSs on the DeH**  tab, query the status of the ECS to be migrated.
6.  If the ECS is not in the  **Stopped**  state, click  **More**  and select  **Stop**  in the  **Operation**  column.
7.  After the ECS status changes to  **Stopped**, click  **More**  and select  **Migrate ECS**  in the  **Operation**  column.
8.  On the  **Migrate ECS**  page, migrate ECSs as prompted.
    -   If you want to migrate the ECS to another DeH, set  **Migrated **to  **To another DeH**.
    -   If you want to migrate the ECS from a DeH to a public resource pool, set  **Migrated**  to  **Out of DeH**.

9.  Click  **OK**.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >The ECS status changes from  **Resizing**  to  **Stopped**  during ECS migration, which is the same as that when you modify ECS specifications.  


