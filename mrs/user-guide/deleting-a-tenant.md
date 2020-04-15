# Deleting a Tenant<a name="EN-US_TOPIC_0125375390"></a>

## Scenario<a name="section12862319193852"></a>

On MRS Manager, you can delete a tenant that is not required.

## Prerequisites<a name="section52490834193910"></a>

-   A tenant has been added.
-   You have checked whether the tenant to be deleted has sub-tenants. If the tenant has sub-tenants, delete  them; otherwise, you cannot delete the tenant.
-   The role of the tenant to be deleted cannot be associated with any user or user group. For details about how to cancel the binding between roles and users, see  [Modifying User Information](modifying-user-information.md).

## Procedure<a name="section65778356193917"></a>

1.  On MRS Manager, click  **Tenant**.
2.  In the tenant list on the left, move the cursor to the tenant node where the tenant is to be deleted. Click  **Delete**.

    The  **Delete Tenant** dialog box is displayed. To save tenant data, select **Reserve the data of this tenant**. Otherwise, the tenant storage space will be deleted.

3.  Click  **OK**.

    It takes a few minutes to save the configuration. The tenant is deleted successfully. The tenant's role and storage space are deleted.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   After the tenant is deleted, the tenant's task queue persists in Yarn.  
    >-   If you choose not to reserve data when deleting the parent tenant, data of sub-tenants is also deleted if the sub-tenants use storage resources.  


