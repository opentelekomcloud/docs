# Why Is the Remaining Space Not Changed After a Backup Is Deleted?<a name="EN-US_TOPIC_0127994691"></a>

This situation appears because the deletion operations are asynchronous. After a backup is deleted, no fee will be generated. The underlying backup data will be deleted gradually based on the backup size within three days. After the underlying backup data is deleted, the remaining space will change accordingly.

