# Does Standby Cache Node Remain Synchronized With Master Cache Node?<a name="EN-US_TOPIC_0237964739"></a>

Generally, updates to the master cache node are automatically and asynchronously replicated to the standby cache node. This means that data in the standby cache node may not always be consistent with data in the master cache node. This inconsistency is typically seen in either of the following situations:

-   The input/output \(I/O\) write speed of the master cache node is faster than the synchronization speed of the standby cache node.
-   There is network latency between the master and standby cache nodes.

If a failover occurs when some data is not yet replicated to the standby cache node, the unreplicated data may be lost after the failover.

