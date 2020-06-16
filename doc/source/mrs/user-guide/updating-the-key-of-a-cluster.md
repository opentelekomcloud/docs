# Updating the Key of a Cluster<a name="EN-US_TOPIC_0221415065"></a>

## Scenario<a name="section5340973015462"></a>

When a cluster is created, the system automatically generates an encryption key to store the security information in the cluster \(such as all database user passwords and key file access passwords\) in encryption mode. After a cluster is successfully installed, it is advised to regularly update the encryption key based on the following procedure.

## Impact on the System<a name="section30675106154659"></a>

-   After a cluster key is updated, a new key is generated randomly in the cluster. This key is used to encrypt and decrypt the newly stored data. The old key is not deleted, and it is used to decrypt the old encrypted data. After security information is modified, for example, a database user password is changed, the new password is encrypted using the new key.
-   When the key is updated in a cluster, the cluster must be stopped and cannot be accessed.

## Prerequisites<a name="section51431510154729"></a>

You have stopped the upper-layer service applications that depend on the cluster.

## Procedure<a name="section15677452162911"></a>

1.  On MRS Manager, choose  **Service**  \>  **More**  \>  **Stop Cluster**.

    Select  **I have read the information and understand the impact** in the displayed window, and click **OK**. After **Operation succeeded** is displayed, click **Finish**. The cluster is stopped.

2.  Log in to the active management node.
3.  Run the following command to switch the user:

    **sudo su - omm**

4.  Run the following command to disable logout upon timeout:

    **TMOUT=0**

5.  Run the following command to switch the directory:

    **cd $\{BIGDATA\_HOME\}/om-0.0.1/tools**

6.  Run the following command to update the cluster key:

    **sh updateRootKey.sh**

    Enter  **y**  as prompted.

    ```
    The root key update is a critical operation.
    Do you want to continue?(y/n):
    ```

    If the following information is displayed, the key is updated successfully.

    ```
    ...
    Step 4-1: The key save path is obtained successfully.
    ...
    Step 4-4: The root key is sent successfully.
    ```

7.  On MRS Manager, choose  **Service**  \>  **More**  \>  **Start Cluster**.

    In the confirmation dialog box, click  **OK** to start the cluster. After **Operation succeeded** is displayed, click **Finish**. The cluster is started.


