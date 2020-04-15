# Patch Operation Guide for Versions Earlier than MRS 1.7.0<a name="EN-US_TOPIC_0135782408"></a>

If you obtain patch information from the following sources, upgrade the patch according to actual requirements.

-   You obtain information about the patch released by MRS from a message pushed by the message center service.
-   You obtain information about the patch by accessing the cluster and viewing patch information.

## Preparing for Patch Installation<a name="section1967921120584"></a>

-   Follow instructions in  [Performing a Health Check](performing-a-health-check.md)  to check cluster status. If the cluster health status is normal, install a patch.
-   The administrator has uploaded the cluster patch package to the server. For details, see  [Uploading the Patch Package](#section419755718157).
-   You need to confirm the target patch to be installed according to the patch information in the patch content.

## Uploading the Patch Package<a name="section419755718157"></a>

1.  Access MRS Manager. For details, see  [Accessing MRS Manager](accessing-mrs-manager.md).
2.  Choose  **System**  \>  **Manage Patch**. The **Manage Patch**  page is displayed.
3.  Click  **Upload Patch**  and set the following parameters.
    -   **Patch File Path**: Folder created in the OBS bucket where the patch package is stored, for example, **MRS\_1.6.2/MRS\_1\_6\_2\_11.tar.gz**
    -   **Bucket**: Name of the OBS bucket where the patch package is stored, for example, **mrs\_patch**

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >You can obtain the bucket name and patch file path on the  **Patch Information** tab page. The value of the **Patch Path**  is in the following format: \[Bucket name\]/\[Patch file path\].  

    -   **AK**: For details, see **My Credential**  \>  **User Guide**  \>  **How Do I Manage Access Keys?**.
    -   **SK:** For details, see **My Credential**  \>  **User Guide**  \>  **How Do I Manage Access Keys?**.

4.  Click  **OK**  to upload the patch.

## Installing a Patch<a name="section919765751516"></a>

1.  Access MRS Manager. For details, see  [Accessing MRS Manager](accessing-mrs-manager.md).
2.  Choose  **System**  \>  **Manage Patch**. The **Manage Patch**  page is displayed.
3.  In the  **Operation** column, click **Install**.
4.  In the displayed dialog box, click  **OK**  to install the patch.
5.  After the patch is installed, you can view the installation status in the progress bar. If the installation fails, contact the administrator.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >For the isolated host nodes in the cluster, follow instructions in  [Restoring Patches for the Isolated Hosts](restoring-patches-for-the-isolated-hosts.md)  to restore the patch.  


## Uninstalling a Patch<a name="section21988577158"></a>

1.  Access MRS Manager. For details, see  [Accessing MRS Manager](accessing-mrs-manager.md).
2.  Choose  **System**  \>  **Manage Patch**. The **Manage Patch**  page is displayed.
3.  In the  **Operation** column, click **Uninstall**.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >For the isolated host nodes in the cluster, follow instructions in  [Restoring Patches for the Isolated Hosts](restoring-patches-for-the-isolated-hosts.md)  to restore the patch.  


