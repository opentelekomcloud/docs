# What Are the Differences Between CSBS and VBS?<a name="EN-US_TOPIC_0086428372"></a>

CSBS mainly creates consistency backups online for all EVS disks of the ECS. You are advised to use CSBS in a scenario where the whole ECS, including its configurations and specifications, as well as the consistency data of multiple EVS disks, is protected, or if you want to use backups to create images and provision ECSs, in order to quickly restore the service running environment.

In comparison, VBS generally creates online backups for a single EVS disk \(system or data disk\) of the ECS. If the system disk does not have user-defined data, you can perform the backup only for the data disk using VBS to safeguard your data and reduce the backup costs.

CSBS backups will also be displayed on the VBS page and can be used to restore individual disks.

