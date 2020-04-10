# Basic Concepts<a name="sfs_01_0008"></a>

Before you start, understand the following concepts.

-   NFS

    Network File System \(NFS\) is a distributed file system protocol that allows different computers and operating systems to share data over a network.

-   File system

    A file system provides users with shared file storage service through NFS. It is used for accessing network files remotely. After a user creates a shared path on the management console, the file system can be mounted to multiple ECSs and is accessible through the standard POSIX.

-   POSIX

    Portable Operating System Interface \(POSIX\) is a set of interrelated standards specified by Institute of Electrical and Electronics Engineers \(IEEE\) to define the application programming interface \(API\) for software compatible with variants of the Unix operating system. POSIX is intended to achieve software portability at the source code level. That is, a program written for a POSIX compatible operating system may be compiled and executed on any other POSIX operating system.

-   DHCP

    Dynamic Host Configuration Protocol \(DHCP\) is a LAN network protocol. The server controls an IP address range, and a client can automatically obtain the IP address and subnet mask allocated by the server when logging in to the server. By default, DHCP is not automatically installed as a service component of Windows Server. Manual installation and configuration are required.

-   Project

    A project is used to group and isolate OpenStack resources, such as compute, storage, and network resources. A project can be a department or a project team. More than one project can be created for an account.


