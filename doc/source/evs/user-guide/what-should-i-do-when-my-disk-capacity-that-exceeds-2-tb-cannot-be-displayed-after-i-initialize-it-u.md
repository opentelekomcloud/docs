# What Should I Do When My Disk Capacity That Exceeds 2 TB Cannot Be Displayed After I Initialize It Using fdisk?<a name="evs_faq_0035"></a>

If your disk capacity is greater than 2 TB, do not use the fdisk partition tool. Otherwise, the disk capacity exceeding 2 TB cannot be displayed after initialization.

In this case, use the parted partition tool to repartition the disk. Meanwhile, choose the GPT partition style during the repartition because the maximum disk capacity supported by the MBR partition style is 2 TB.

For details, see  [Introduction to Data Disk Initialization Scenarios and Partition Styles](introduction-to-data-disk-initialization-scenarios-and-partition-styles.md).

