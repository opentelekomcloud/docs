# Constraints and Limitations<a name="EN-US_TOPIC_0056725852"></a>

Note the following constraints and limitations about CSBS:

-   An ECS can be associated with only one backup policy.
-   Shared EVS disks in ECSs can be backed up.
-   CSBS supports crash-consistent backup of EVS disks on an ECS but not application-consistent backup of them.
-   CSBS does not support consistent backup of multiple ECSs.
-   CSBS supports backup and restoration of all EVS disks as a whole instead of part of the EVS disks on an ECS. In addition, CSBS does not support file- or directory-level restoration.
-   You are not advised to back up an ECS whose capacity exceeds 4 TB.
-   Servers or disks at the disaster recovery \(DR\) site can be restored only when DR protection is disabled for servers deployed with Storage Disaster Recovery Service.

