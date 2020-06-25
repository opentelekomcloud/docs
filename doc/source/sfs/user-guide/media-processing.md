# Media Processing<a name="sfs_01_0053"></a>

## Context<a name="section5199218591644"></a>

Media processing involves uploading, downloading, cataloging, transcoding, and archiving media materials, as well as storing, invoking, and managing audio and video data. Media processing has the following requirements on shared file systems:

-   Media materials feature a high video bit rate and a large scale. The capacity of file systems must be large and easy to be expanded.
-   Acquisition, editing, and synthesis of audio and video data require stable and low-latency file systems.
-   Concurrent editing requires file systems to deliver reliable and easy-to-use data sharing.
-   Video rendering and special effects need processing small files frequently. The file systems must offer a high I/O performance.

SFS is a shared storage service based on file systems. It features high-speed data sharing, dynamic storage tiering, as well as on-demand, smooth, and online resizing. The outstanding features empower SFS to meet the demanding requirements of media processing on storage capacity, throughput, IOPS, and latency.

A TV channel has a large amount of audio and video materials to process. The work will be done on multiple editing workstations. The TV channel uses SFS to enable file sharing among the editing workstations. First, a file system is mounted to ECSs that function as upload workstations and editing workstations. Then raw materials are uploaded to the shared file system through the upload workstations. Then, the editing workstations concurrently edit the materials in the shared file system.

## Configuration Process<a name="section652070912244"></a>

1.  Organize the material files that are to be uploaded.
2.  Log in to SFS Console. Create a file system to store the material files.
3.  Log in to the ECSs that function as upload workstations and editing workstations, and mount the file system.
4.  On the upload workstations, upload the material files to the file system.
5.  On the editing stations, edit the material files.

## Prerequisites<a name="section44286645122428"></a>

-   A VPC has been created.
-   ECSs that function as upload workstations and editing workstations have been created, and have been assigned to the VPC.
-   SFS has been subscribed.

## Example Configuration<a name="section66406365122442"></a>

1.  Log in to SFS Console.
2.  In the upper right corner of the page, click  **Create File System**.
3.  On the  **Create File System**  page, set parameters as instructed.
4.  After the configuration is complete, click  **Create Now**.

    For details about how to mount a file system to an ECS running Linux, see  [Mounting an NFS File System to ECSs \(Linux\)](mounting-an-nfs-file-system-to-ecss-(linux).md). For details about how to mount a file system running Windows, see  [Mounting an NFS File System to ECSs \(Windows 2012\)](mounting-an-nfs-file-system-to-ecss-(windows-2012).md).

5.  Log in to the upload workstations, and upload the material files to the file system.
6.  Log in to the editing stations, and edit the material files.

