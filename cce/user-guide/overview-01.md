# Overview<a name="cce_01_0042"></a>

Container storage  is a component that provides storage for container workloads. It supports multiple types of storage. A  pod  can use any amount of storage.

>![](public_sys-resources/icon-note.gif) **NOTE:** 
>In CCE clusters earlier than Kubernetes 1.13, end-to-end capacity expansion of container storage is not supported, and the PVC capacity is inconsistent with the storage capacity.

## Selecting a Storage Type<a name="section13374182011418"></a>

You can use the following types of storage when creating a workload: You are advised to store workload data on EVS disks. If you store workload data on a local disk and a fault occurs on the node, the data cannot be restored.

-   Local disk: Mount the file directory of the host where a container is located to a specified container path \(corresponding to  HostPath  in  Kubernetes\). Alternatively, you can leave the source path empty \(corresponding to  EmptyDir  in Kubernetes\). If the source path is left empty, a temporary directory of the host will be mounted to the mounting point of the container. A specified source path is used when data needs to be persistently stored on the host, while EmptyDir is used when temporary storage is needed. A  ConfigMap  is a type of resource that stores configuration information required by a workload. Its content is user-defined. A  secret  is a type of resource that holds sensitive data, such as authentication and key information. Its content is user-defined. For details, see  [Using Local Disks for Storage](using-local-disks-for-storage.md).
-   EVS: Mount an EVS disk to a container path. When the container is migrated, the mounted EVS disk is migrated together. This storage type is applicable when data needs to be stored permanently. For details, see  [Using EVS Disks for Storage](using-evs-disks-for-storage.md).
-   SFS: Create  SFS  file systems and mount them to a container path. The file systems created by the underlying SFS service can also be used. SFS file systems are applicable to persistent storage for frequent read/write in multiple workload scenarios, including media processing, content management, big data analysis, and workload analysis. For details, see  [Using SFS File Systems for Storage](using-sfs-file-systems-for-storage.md).

