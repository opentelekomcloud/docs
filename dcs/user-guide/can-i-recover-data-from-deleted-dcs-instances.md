# Can I Recover Data from Deleted DCS Instances?<a name="en-us_topic_0054235829"></a>

Data that is automatically deleted by DCS instances or manually deleted by users using Redis clients cannot be recovered. By default, data is not evicted from DCS instances. However, you can modify the value of the  **maxmemory-policy**  parameter to adjust the eviction policy, and then DCS instances evict keys according to the eviction policy.

If a DCS instance is deleted, instance data will also be removed and cannot be recovered. Therefore, exercise caution when deleting DCS instances.

Master/Standby DCS instances support data backup. If you have backed up the instance data before deleting them, the deleted instance data can be recovered.

