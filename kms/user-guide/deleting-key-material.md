# Deleting Key Material<a name="kms_01_0020"></a>

## Scenario<a name="sca880be282b5423eb210862b51049a3e"></a>

When importing key material, you can specify the expiration time. After the key material expires, KMS deletes it, and the status of the CMK changes to  **Pending import**. You can manually delete the key material as needed. The effect of expiration of the key material is the same as that of manual deletion of the key material.

This section describes how to delete imported key material on the management console.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>-   After the key material is deleted, if you need to re-import the key material, the key material to be imported must be the same as that has been deleted.  
>-   After the same key material is re-imported, you can use the CMK to decrypt all data encrypted using this key before deletion.  

## Prerequisites<a name="sb5977e06db7340a1b1c77b833a445de3"></a>

-   You have obtained an account and its password for logging in to the management console.
-   You have imported the key material for a CMK.
-   The material source of the CMK is  **External**.
-   The CMK status is  **Enabled**  or  **Disabled**.

## Procedure<a name="sfc815d094c7c4eee9334ff32ef341265"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner of the management console and select a region or project.
3.  Choose  **Security**  \>  **Key Management Service**. The  **Key Management Service**  page is displayed.
4.  In the row containing the desired CMK, click  **Delete Key Material**.
5.  In the dialog box that is displayed, click  **OK**. A message indicating that the key material is successfully deleted is displayed in the upper right corner of the page.

    After the deletion, the CMK will become unavailable and its status changes to  **Pending import**.


