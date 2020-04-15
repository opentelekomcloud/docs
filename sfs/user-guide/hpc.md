# HPC<a name="sfs_01_0052"></a>

## Context<a name="section5199218591644"></a>

HPC is short for high-performance computing. An HPC system or environment is made up of a single computer system with many CPUs, or a cluster of multiple computers clusters. It can handle a large amount of data and perform high-performance computing that would be rather difficult for PCs. HPC has ultra-high capability in floating-point computation and can be used for compute-intensive and data-intensive fields, such as industrial design, bioscience, energy exploration, image rendering, and heterogeneous computing. Different scenarios put different requirements on the file system:

-   Industrial design: In automobile manufacturing, CAE and CAD simulation software are widely used. When the software is operating, compute nodes need to communicate with each other closely, which requires high bandwidth and low latency of the file system.
-   Bioscience: The file system should have high bandwidth and large storage, and be easy to expand.
    -   Bioinformatics: To sequence, stitch and compare genes.
    -   Molecular dynamics: To simulate the changes of proteins in molecular and atomic levels.
    -   New drug R&D: To complete high-throughput screening \(HTS\) to shorten the R&D cycle and reduce the investment.

-   Energy exploration: Field operations, geologic prospecting, geological data processing and interpretation, and identification of oil and gas reservoirs all require large memory and high bandwidth of the file system.
-   Image rendering: Image processing, 3D rendering, and frequent processing of small files require high read/write performance, large capacity, and high bandwidth of file systems.
-   Heterogeneous computing: Compute elements may have different instruction set architectures, requiring the file system provide high bandwidth and low latency.

SFS is a shared storage service based on file systems. It features high-speed data sharing, dynamic storage tiering, as well as on-demand, smooth, and online resizing. These outstanding features empower SFS to meet the demanding requirements of HPC on storage capacity, throughput, IOPS, and latency.

A biological company needs to perform plenty of gene sequencing using software. However, due to the trivial steps, slow deployment, complex process, and low efficiency, self-built clusters are reluctant to keep abreast of business development. However, things are getting better since the company resorted to professional HPC service process management software. With massive compute and storage resource of the cloud platform, the initial investment and cost during O&M are greatly reduced, the service rollout time is shortened, and efficiency is boosted.

## Configuration Process<a name="section652070912244"></a>

1.  Organize the files of DNA sequencing to be uploaded.
2.  Log in to SFS Console. Create a file system to store the files of DNA sequencing.
3.  Log in to the ECSs that function as the head node and compute node, and mount the file system.
4.  On the head node, upload the files to the file system.
5.  On the compute node, edit the files.

## Prerequisites<a name="section44286645122428"></a>

-   A VPC has been created.
-   ECSs that function as head nodes and compute nodes have been created, and have been assigned to the VPC.
-   SFS has been subscribed.

## Example Configuration<a name="section66406365122442"></a>

1.  Log in to SFS Console.
2.  In the upper right corner of the page, click  **Create File System**.
3.  On the  **Create File System**  page, set parameters as instructed.
4.  After the configuration is complete, click  **Create Now**.

    For details about how to mount a file system to an ECS running Linux, see  [Mounting an NFS File System to ECSs \(Linux\)](mounting-an-nfs-file-system-to-ecss-(linux).md). For details about how to mount a file system running Windows, see  [Mounting an NFS File System to ECSs \(Windows 2012\)](mounting-an-nfs-file-system-to-ecss-(windows-2012).md).

5.  Log in to the head node, and upload the files to the file system.
6.  Start gene sequencing, and the compute node obtains the gene sequencing file from the mounted file system for calculation.

