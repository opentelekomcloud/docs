# Why Is the Used Instance Memory Displayed on Cloud Eye Console Slightly Higher than the Instance Available Memory?<a name="en-us_topic_0078401074"></a>

For DCS instances in single-node and master/standby modes, the used instance memory is measured by the redis-server process. For DCS instances in Proxy Cluster mode, the used cluster memory is the sum of used memory of all shards in the cluster. The redis-server of each shard measures the used memory of the shard.

Due to internal implementation of the open-source redis-server, the used instance memory is normally slightly higher than the available instance memory.

