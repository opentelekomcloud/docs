# What Is CSBS?<a name="EN-US_TOPIC_0056584628"></a>

Cloud Server Backup Service \(CSBS\) can back up an entire ECS. It can use the consistent backup data of multiple Elastic Volume Service \(EVS\) disks to restore the service data of an ECS. CSBS ensures data security and service continuity.

CSBS provides crash-consistent backup of multiple EVS disks to ensure that these EVS disks are backed up at the same time. Different from application-consistent backup, crash-consistent backup does not freeze applications and file systems and does not include memory data.

