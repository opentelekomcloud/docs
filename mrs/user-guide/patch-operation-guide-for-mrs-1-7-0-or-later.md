# Patch Operation Guide for MRS 1.7.0 or Later<a name="EN-US_TOPIC_0135782409"></a>

If you obtain patch information from the following sources, upgrade the patch according to actual requirements.

-   You obtain information about the patch released by MRS from a message pushed by the message center service.
-   You obtain information about the patch by accessing the cluster and viewing patch information.

## Preparing for Patch Installation<a name="section1967921120584"></a>

-   Follow instructions in  [Performing a Health Check](performing-a-health-check.md)  to check cluster status. If the cluster health status is normal, install a patch.
-   You need to confirm the target patch to be installed according to the patch information in the patch content.

## Installing a Patch<a name="section17824113381616"></a>

1.  Log in to the MRS management console.
2.  Choose  **Cluster \> Active Cluster**  and click the name of the cluster to be queried to enter the page displaying the cluster's basic information.
3.  On the  **Patch Information** page, click **Install** in the **Operation**  column to install the target patch.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >For the isolated host nodes in the cluster, follow instructions in  [Restoring Patches for the Isolated Hosts](restoring-patches-for-the-isolated-hosts.md)  to restore the patch.  


## Uninstalling a Patch<a name="section1482663319163"></a>

1.  Log in to the MRS management console.
2.  Choose  **Cluster \> Active Cluster**  and click the name of the cluster to be queried to enter the page displaying the cluster's basic information.
3.  On the  **Patch Information** page, click **Uninstall** in the **Operation**  column to uninstall the target patch.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >For the isolated host nodes in the cluster, follow instructions in  [Restoring Patches for the Isolated Hosts](restoring-patches-for-the-isolated-hosts.md)  to restore the patch.  


