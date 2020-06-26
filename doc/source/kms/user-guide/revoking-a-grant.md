# Revoking a Grant<a name="kms_01_0031"></a>

## Scenario<a name="section1615963710458"></a>

You can revoke a grant in either of the following scenarios:

-   A grantee does not need the grant. \(The grantee can either tell the user who has created the grant to revoke the grant or call the necessary API to revoke the grant directly.\)
-   You do not want the grantee to have the grant.

When a grant is revoked, the grantee does not have the corresponding permission any more. However, if the grantee has created the same grant to another user, permission of that user will not be affected.

This section describes how to revoke a grant.

## Prerequisites<a name="section51403752104654"></a>

-   You have obtained an account and its password for logging in to the management console.
-   You have created a grant.

## Procedure<a name="section64073293104744"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner of the management console and select a region or project.
3.  Choose  **Security**  \>  **Key Management Service**. The  **Key Management Service**  page is displayed.
4.  Click the alias of the desired CMK to view its details.
5.  In the row containing the desired grantee, click  **Revoke Grant**  in the  **Operation**  column.
6.  In the dialog box that is displayed, click  **Yes**. When  **Grant  _grant\_ID_  revoked successfully**  is displayed in the upper right corner, the grant has been revoked.

