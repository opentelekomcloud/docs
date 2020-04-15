# What Should I Do If My Disk Capacity Exceeds 2 TB After Expansion?<a name="evs_faq_0024"></a>

An EVS system disk supports up to 1 TB \(1024 GB\). You can expand the capacity of a system disk to up to 1 TB.

An EVS data disk supports up to 32 TB \(32768 GB\).

-   With MBR, the disk space exceeding 2 TB cannot be allocated and used, because the maximum disk capacity supported by MBR is 2 TB \(2048 GB\).

    In this case, if you want to expand the disk capacity to over 2 TB, change the partition style from MBR to GPT. Ensure that the disk data has been backed up before changing the partition style because services will be interrupted and data on the disk will be cleared during this change.


-   With GPT, you can expand the capacity of a data disk to up to 32 TB.

If the in-use partition style is GPT, perform the extension operation according to the following topics:

-   Windows:
    -   [Extending Disk Partitions and File Systems \(Windows\)](extending-disk-partitions-and-file-systems-(windows).md)

-   Linux:
    -   [Extending Partitions and File Systems for Data Disks \(Linux\)](extending-partitions-and-file-systems-for-data-disks-(linux).md)


