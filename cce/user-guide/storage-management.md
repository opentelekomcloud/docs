# Storage Management<a name="cce_01_0041"></a>

-   **[Storage Overview](storage-overview.md)**  
Container storage  is a component that provides storage for container workloads. It supports multiple types of storage. A  pod  can use any amount of storage.
-   **[Using Local Disks for Storage](using-local-disks-for-storage.md)**  
Use the  local disk storage  to mount the file directory of the host where the container is located to the specified path of the container, or leave the source path empty.
-   **[Using EVS Disks for Storage](using-evs-disks-for-storage.md)**  
To meet data  persistency  requirements,  CCE  allows  EVS  disks to be mounted to  containers. By using EVS disks, you can mount the remote file directory of storage system into a container so that data in the data volume is permanently preserved. Even if the container is deleted, only the attached data volume is deleted. Data in the data volume is still stored in the storage system.
-   **[Using SFS File Systems for Storage](using-sfs-file-systems-for-storage.md)**  
File storage  is applicable to various scenarios, such as  media processing,  content management,  big data, and workload analysis.

