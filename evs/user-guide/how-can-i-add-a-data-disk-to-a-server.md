# How Can I Add a Data Disk to a Server?<a name="evs_faq_0043"></a>

When a server is created, the system disk is automatically created and attached. You do not need to create the system disk separately.

Data disks can be created during or after the server creation. If you create data disks during the server creation, the system will automatically attach the data disks to the server. If you create data disks after the server creation, you need to manually attach the created data disks to the server.

On a Windows server:

-   If a data disk is created along with the server, you need to log in to the server and initialize the disk. The data disk, for example  **Disk \(D:\)**, can be viewed after the initialization succeeds.
-   If a data disk is not created along with the server, you need to create a data disk and attach it to a server. Then, log in to the server and initialize the disk. The data disk, for example  **Disk \(D:\)**, can be viewed after the initialization succeeds.

On a Linux server:

-   If a data disk is created along with the server, you need to log in to the server and initialize the disk. The data disk, for example  **dev/vdb1**, can be viewed after the initialization succeeds and the disk has been mounted via the  **mount**  command.
-   If a data disk is not created along with the server, you need to create a data disk and attach it to a server. Then, log in to the server and initialize the disk. The data disk, for example  **dev/vdb1**, can be viewed after the initialization succeeds and the disk has been mounted via the  **mount**  command.

For details, see  [Introduction to Data Disk Initialization Scenarios and Partition Styles](introduction-to-data-disk-initialization-scenarios-and-partition-styles.md).

