# everest \(System Resource Add-on, Mandatory\)<a name="cce_01_0066"></a>

## Introduction<a name="section25311744154917"></a>

Everest is a cloud-native container storage system. Based on CSI, clusters of Kubernetes v1.15.6 or later can interconnect with storage services such as EVS, OBS, and SFS.

Everest is a system resource add-on. It is installed by default when a cluster of Kubernetes v1.15 or later is created.

## Constraints<a name="section202191122814"></a>

The everest add-on can be installed only in hybrid and BMS clusters of v1.15 or later. By default, the  [storage-driver](storage-driver-(system-resource-add-on-mandatory).md)  add-on must be installed when clusters of v1.13 or earlier are created.

## Installing the Add-on<a name="section194134223382"></a>

This add-on has been installed by default. If it is uninstalled due to some reasons, you can reinstall it by performing the following steps:

1.  Log in to the CCE console. In the navigation pane, choose  **Add-ons**. On the  **Add-on Marketplace**  tab page, click  **Install Add-on**  under  **everest**.
2.  On the  **Install Add-on**  page, select the cluster and the add-on version, and click  **Next: Configuration**.
3.  Select  **Single**  or  **HA**  for  **Add-on Specifications**, and click  **Install**.

    After the add-on is installed, click  **Back to Add-on List**. On the  **Add-on Instance**  tab page, select the corresponding cluster to view the running instance. This indicates that the add-on has been installed on each node in the cluster.


## Upgrading the Add-on<a name="section1441472219383"></a>

1.  Log in to the CCE console. In the navigation pane, choose  **Add-ons**. On the  **Add-on Instance**  tab page, select the cluster and click  **Upgrade**  under  **everest**.

    >![](/images/icon-note.gif) **NOTE:** 
    >-   If the  **Upgrade**  button is unavailable, the current add-on is already up-to-date and no upgrade is required.
    >-   When the upgrade is complete, the original everest version on cluster nodes will be replaced by the latest version.

2.  On the  **Basic Information**  page, select the add-on version and click  **Next**.
3.  Select  **Single**  or  **HA**  for  **Add-on Specifications**, and click  **Upgrade**.

## Uninstalling the Add-on<a name="section64144223384"></a>

1.  Log in to the CCE console. In the navigation pane, choose  **Add-ons**. On the  **Add-on Instance**  tab page, click  **Uninstall**  under  **everest**.
2.  In the dialog box that is displayed, click  **OK**  to uninstall the add-on.

