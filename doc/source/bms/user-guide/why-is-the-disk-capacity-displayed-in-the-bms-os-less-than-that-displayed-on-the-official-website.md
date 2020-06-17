# Why Is the Disk Capacity Displayed in the BMS OS Less Than That Displayed on the Official Website?<a name="EN-US_TOPIC_0094808032"></a>

Possible causes of this issue are as follows:

1.  Hardware vendors have a different method of calculating storage capacity from that of the OS. Hardware vendors use decimal notation to calculate disk capacity, in which 1 GB = 1000 x 1000 x 1000 bytes. In the OS, the capacity is calculated in binary mode, in which 1 GB = 1024 x 1024 x 1024 bytes.
2.  The system contains hidden partitions, such as the boot partition, system backup, and restoration partition.
3.  The file system consumes some disk capacity. Before using a hard disk, the OS partitions the disk and initializes the file system. The configuration also occupies a small amount of disk capacity.
4.  The RAID array occupies some disk capacity. For example, If two 600 GB hard disks form RAID 1, only 600 GB capacity of one disk can be used.

