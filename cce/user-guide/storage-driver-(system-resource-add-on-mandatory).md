# storage-driver \(System Resource Add-on, Mandatory\)<a name="cce_01_0127"></a>

## Introduction<a name="section25311744154917"></a>

storage-driver is a FlexVolume driver used to support IaaS storage services such as  EVS and SFS.

The  storage-driver  complies with the NBI standard of Kubernetes. It provides a standard  Kubernetes  FlexVolume interface that allows  containers  to use IaaS storage services such as  EVS and SFS. By installing and upgrading the storage-driver, you can quickly install and update cloud storage services.

>![](public_sys-resources/icon-note.gif) **NOTE:** 
>-   The storage-driver is a system resource add-on. It is provided in the operating system images of the new nodes in CCE.
>-   When an upgrade or bug fix is available for the storage function, you only need to install or upgrade the storage-driver add-on to upgrade the function. Upgrading the cluster or creating a cluster is not required.

## Installing the Add-on<a name="section776571919194"></a>

By default, storage-driver is installed in CCE clusters of Kubernetes v1.11 and later.

If storage-driver is not installed in a cluster, perform the following steps to install it:

1.  Log in to the CCE console. In the navigation pane, choose  **Add-ons**. On the  **Add-on Marketplace**  tag page, click  **Install Add-on**  under  **storage-driver**.
2.  On the  **Install Add-on**  page, select the cluster and the add-on version, and click  **Next: Configuration**.
3.  Click  **Install**  to install the add-on. Note that the storage-driver has no configurable parameters and can be directly installed.

    When the installation is complete, an instance of the storage-driver is installed on each node of the selected cluster.


## Upgrading the Add-on<a name="section455343310401"></a>

1.  Log in to the CCE console. In the navigation pane, choose  **Add-ons**. On the  **Add-on Instance**  tab page, select the cluster and click  **Upgrade**  under  **storage-driver**.

    >![](public_sys-resources/icon-note.gif) **NOTE:** 
    >-   If the  **Upgrade**  button is unavailable, the current add-on is already up-to-date and no upgrade is required.
    >-   When the upgrade is complete, the original storage-driver version on cluster nodes will be replaced by the latest version.

2.  On the  **Basic Information**  page, select the add-on version and click  **Next: Configuration**.
3.  Click  **Upgrade**  to upgrade the storage-driver add-on. Note that the storage-driver has no configurable parameters and can be directly upgraded.

## Uninstalling the Add-on<a name="section20765191931911"></a>

1.  Log in to the CCE console. In the navigation pane, choose  **Add-ons**. On the  **Add-on Instance**  tab page, select the cluster and click  **Uninstall**  under  **storage-driver**.
2.  In the dialog box that is displayed, click  **Yes**  to uninstall the add-on.

