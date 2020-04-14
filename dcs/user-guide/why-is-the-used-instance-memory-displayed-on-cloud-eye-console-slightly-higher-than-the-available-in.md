# Why Is the Used Instance Memory Displayed on Cloud Eye Console Slightly Higher than the Available Instance Memory?<a name="EN-US_TOPIC_0237964752"></a>

For DCS instances in single-node and master/standby modes, the used instance memory is measured by the redis-server process. For DCS instances in cluster mode, the used cluster memory is the sum of used memory of all shards in the cluster. The redis-server of each shard measures the used memory of the shard.

Due to internal implementation of the open-source redis-server, the used instance memory is normally slightly higher than the available instance memory.

