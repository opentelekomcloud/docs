# Do I Need to Stop the ECS Before Backing It Up?<a name="EN-US_TOPIC_0056584623"></a>

No. CSBS allows you to back up ECSs that are in use. When an ECS is running, data is written onto EVS disks on the ECS, and some newly generated data is stored in the ECS memory as cached data. During a backup process, the data in the memory will not be automatically written onto EVS disks, resulting in data inconsistency between EVS disks and their backups.

To ensure data integrity, back up the ECS during off-peak hours when no write operation is performed on the EVS disks. Before backing up applications that requires strict consistency, such as databases and email systems, you are advised to suspend all write operations. If write operations cannot be suspended, you can stop the application systems or the ECS for offline backup.

