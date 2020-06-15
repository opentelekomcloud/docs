# Why Cannot I Delete a CMK Immediately?<a name="kms_01_0039"></a>

The decision to delete a CMK should be taken with caution. Before deletion, confirm that the CMK's encrypted data has all been migrated. Once the CMK is deleted, you will not be able to decrypt data with it. Therefore, KMS offers a waiting period of 7 to 1096 days for the deletion to finally take effect. On the scheduled day of deletion, the CMK will be permanently deleted. However, prior to the scheduled day, you can still cancel the deletion.

