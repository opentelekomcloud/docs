# High Reliability<a name="dds_01_0007"></a>

## Failover<a name="section56101305112535"></a>

The three-node replica set architecture of DDS ensures high service availability.

In a replica set, both the primary and secondary nodes provide services. If a primary node goes down or becomes faulty, a secondary node is automatically assigned to the primary role and continues normal operation. If a secondary node is unavailable, a hidden node will take the role of the secondary to ensure high availability.

## Multi-Copy Redundancy<a name="section18363126194820"></a>

config and shard use the three-node replica set HA architecture. Using this architecture, nodes are deployed on different servers and racks.

## Data Backups<a name="section144894164812"></a>

Data can be backed up automatically or manually. Automated backups execute full backups on DB instances. A manual backup is a full backup of DB instances initiated by users. These backups can be used to restore DB instances with a few clicks.

Backups are stored in Object Storage Service \(OBS\), improving the data disaster recovery capabilities while reducing the needed storage space. When a DB instance is created, the automated backup policy is enabled by default. After the DB instance is created, an automated full backup is triggered instantly. The backup retention period is 7 days by default. You can set the backup retention period and modify the backup policy. In addition, you can initiate backup at any time according to your service requirements. Manual backups are saved until you manually delete them.

## Data Restore<a name="section986045820483"></a>

You can use backup data to restore instance data. Restored data is the same as the original data.

