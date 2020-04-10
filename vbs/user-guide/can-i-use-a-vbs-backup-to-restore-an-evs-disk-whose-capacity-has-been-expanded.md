# Can I Use a VBS Backup to Restore an EVS Disk Whose Capacity Has Been Expanded?<a name="EN-US_TOPIC_0018020175"></a>

Yes. After restoration, the capacity of the expanded EVS disk goes back to the original capacity before expansion. If you want to use the capacity added to the disk, you need to attach the restored disk to an ECS, log in to the ECS, and then manually modify the file system configuration. For detailed operations, see sections about post-expansion operations on EVS disks in the  _Elastic Volume Service User Guide_.

