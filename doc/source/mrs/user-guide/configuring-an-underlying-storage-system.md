# Configuring an Underlying Storage System<a name="EN-US_TOPIC_0228886230"></a>

If you want to use a unified client API and a global namespace to access persistent storage systems including HDFS and OBS to separate computing from storage, you can configure the underlying storage system of Alluxio on MRS Manager. After a cluster is created, the default underlying storage address is  **hdfs://hacluster/**, that is, the HDFS root directory is mapped to Alluxio.

## Prerequisites<a name="s5e180c6a1e264422a14ddfca7e340a74"></a>

-   Alluxio has been installed in a cluster.
-   The password of user  **admin**  has been obtained. The password of user  **admin**  is specified by you during MRS cluster creation.

## Configuring HDFS as the Underlying File System of Alluxio<a name="section1848314194712"></a>

1.  Log in to MRS Manager. For details, see  [Accessing MRS Manager](accessing-mrs-manager.md). Then, choose  **Services**  \>  **Alluxio**.
2.  On the  **Service Configuration**  tab page, set  **Type**  to  **All**. The Alluxio configuration page is displayed.
3.  In the left pane, choose  **Alluxio**  \>  **Under Stores**, and modify the value of  **alluxio.master.mount.table.root.ufs**  to  **hdfs://hacluster/_XXX_/**.

    For example, if you want to use  **_HDFS root directory_/alluxio/**  as the root directory of Alluxio, modify the value of  **alluxio.master.mount.table.root.ufs**  to  **hdfs://hacluster/alluxio/**.

4.  Click  **Save Configuration**. In the displayed dialog box, select  **Restart the affected services or instances**.
5.  Click  **OK**  to restart Alluxio.

