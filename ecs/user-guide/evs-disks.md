# EVS Disks<a name="EN-US_TOPIC_0030828256"></a>

## What Is Elastic Volume Service?<a name="section134415526532"></a>

Elastic Volume Service \(EVS\) offers scalable block storage for ECSs. With high reliability, high performance, and rich specifications, EVS disks can be used for distributed file systems, development and test environments, data warehouse applications, and high-performance computing \(HPC\) scenarios to meet diverse service requirements.

## Disk Types<a name="section60010917143352"></a>

ECSs support the following types of EVS disks for storing data:

-   Common I/O: EVS disks of this type deliver a maximum of 1,000 IOPS. This disk type is suitable for application scenarios that require large capacity, a medium read/write rate, and fewer transactions, such as enterprise office applications and small-scale testing.
-   High I/O: EVS disks of this type deliver a maximum of 3,000 IOPS and a minimum of 6 ms read/write latency. This disk type is designed to meet the needs of mainstream high-performance, high-reliability application scenarios, such as enterprise applications, large-scale development and testing, and web server logs.
-   Ultra-high I/O: EVS disks of this type deliver a maximum of 20,000 IOPS and a minimum of 1 ms read/write latency. This disk type is excellent for ultra-high I/O, ultra-high bandwidth, and read/write-intensive application scenarios, such as distributed file systems in HPC scenarios or NoSQL/RDS in I/O-intensive scenarios.
-   High I/O \(performance-optimized I\): EVS disks of this type deliver a maximum of 550 MB/s throughput, which is higher than high I/O EVS disks. They are cost-effective and offer balanced IOPS and bandwidth. Such disks apply to hybrid load scenario consisting of online analytical processing \(OLAP\) and online transaction processing \(OLTP\) or consisting of large and small HPC files.
-   Ultra-high I/O \(latency-optimized\): EVS disks of this type deliver a maximum of 1 GB/s throughput and a minimum of 1 ms read/write latency. They can be used for key enterprise services, such as SAP HANA.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >High I/O \(performance-optimized I\) and ultra-high I/O \(latency-optimized\) EVS disks can be attached to SAP HANA or HL1 ECSs only.  


EVS disks with different I/O capacities provide different features at different prices. Choose EVS disks based on your requirements. For more information about EVS disk specifications and performance, see  _Elastic Volume Service User Guide_.

## Device Types<a name="section64489635143430"></a>

EVS disks have two device types, Virtual Block Device \(VBD\) and Small Computer System Interface \(SCSI\).

-   VBD

    When you create an EVS disk on the management console,  **Device Type**  of the EVS disk is VBD by default. VBD EVS disks support only simple SCSI read/write commands.

-   SCSI

    You can create EVS disks for which  **Device Type**  is SCSI on the management console. These EVS disks support transparent SCSI command transmission, allowing ECS OS to directly access underlying storage media. SCSI EVS disks support both basic and advanced SCSI commands.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >For more information about how to use SCSI EVS disks, for example, how to install the driver, see "Device Types and Usage Instructions" in  _Elastic Volume Service User Guide_.  


## Helpful Links<a name="section37175862145513"></a>

-   [Which ECSs Can Be Attached with SCSI EVS Disks?](which-ecss-can-be-attached-with-scsi-evs-disks.md)

