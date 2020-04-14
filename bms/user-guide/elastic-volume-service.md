# Elastic Volume Service<a name="EN-US_TOPIC_0083745260"></a>

## What Is Elastic Volume Service?<a name="section134415526532"></a>

The EVS service offers scalable block storage for BMSs. With high reliability, high performance, and rich specifications, EVS disks can be used for distributed file systems, development and test environments, data warehouse applications, and high-performance computing \(HPC\) scenarios to meet diverse service requirements.

BMSs support EVS disks and are not subject to the capacity limit of local disks faced by traditional physical servers. In addition, shared EVS disks are supported. Multiple BMSs can access, read data from, and write data to a shared disk simultaneously, meeting your requirements for deploying core system clusters.

## EVS Disk Types<a name="section589163701010"></a>

BMSs support the following types of EVS disks for storing data:

-   Common I/O: EVS disks of this type deliver a maximum of 1000 IOPS. This disk type is suitable for application scenarios that require large capacity, a medium read/write speed, and fewer transactions, such as enterprise office applications and small-scale testing.
-   High I/O: EVS disks of this type deliver a maximum of 3000 IOPS and a minimum of 6 ms read/write latency. This disk type is designed to meet the needs of mainstream high-performance, high-reliability application scenarios, such as enterprise applications, large-scale development and test, and web server logs.
-   Ultra-high I/O: EVS disks of this type deliver a maximum of 20000 IOPS and a minimum of 1 ms read/write latency. This disk type is excellent for ultra-high I/O, ultra-high bandwidth, and read/write-intensive application scenarios, such as distributed file systems in HPC scenarios or NoSQL/RDS in I/O-intensive scenarios.

## EVS Disk Performance<a name="section156512755611"></a>

The key indicators of EVS disk performance include read/write I/O latency, IOPS, and throughput.

-   IOPS: number of read/write operations performed by an EVS disk per second
-   Throughput: amount of data successfully transmitted by an EVS disk per second, that is, the amount of data read from and written into an EVS disk
-   Read/write I/O latency: minimum interval between two consecutive read/write operations of an EVS disk

For details about EVS disk performance, see  _Elastic Volume Service User Guide_.

## EVS Disk Device Types<a name="section139751861558"></a>

The BMS only supports the Small Computer System Interface \(SCSI\) EVS disks.

You can create EVS disks for which  **Device Type**  is SCSI on the management console. These EVS disks support transparent SCSI command transmission, allowing BMS OS to directly access underlying storage media. Besides basic read/write SCSI commands, such EVS disks also support advanced SCSI commands.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>The BMS public image OS is preinstalled with the driver required for using SCSI device type disks, and you do not need to install the driver explicitly. You can also learn how to install drivers in "Installing the SDI Card Driver" in  _Bare Metal Server Private Image Creation Guide_.  

