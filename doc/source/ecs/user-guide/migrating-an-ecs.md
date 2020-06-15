# Migrating an ECS<a name="EN-US_TOPIC_0133365988"></a>

## Scenarios<a name="section17761164816565"></a>

ECSs can be migrated between DeHs and public resource pools.

-   An ECS created on a DeH can be migrated to another DeH.
-   An ECS created on a DeH can be migrated to a public resource pool.
-   An ECS deployed in a public resource pool can be migrated to a DeH.

## Notes<a name="section1213835718599"></a>

-   Only a stopped ECS can be migrated.
-   CBR and CSBS backups are not affected by cold migrations.
-   ECS IDs remain unchanged after a cold migration.

## Procedure<a name="section12638144614015"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region-0.png)  in the upper left corner and select the desired region and project.
3.  Under  **Computing**, click  **Elastic Cloud Server**.
4.  On the  **Elastic Cloud Server**  page, select the target ECS.
5.  Click  **Migrate ECS**  in the  **Operation**  column.
6.  In the  **Migrate ECS**  dialog box, migrate the ECS as prompted.
    -   If you want to migrate the ECS to a DeH, select a DeH from the list.
    -   If you want to migrate the ECS to another DeH, select  **Migrated** **To another DeH**.
    -   If you want to migrate the ECS from a DeH to a public resource pool, select  **Migrated** **Out of DeH**.

7.  Click  **OK**.

    The ECS is migrated as required.


