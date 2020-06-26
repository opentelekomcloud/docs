# Application Scenarios<a name="sdrs_pro_0003"></a>

## Cross-AZ DR<a name="section28371841112010"></a>

SDRS uses storage-layer synchronization and replication to provide cross-AZ DR to ensure data crash consistency and server-level protection with zero RPO. If a source AZ encounters a disaster \(such as a fire or an earthquake\) or a device fault \(such as a software or hardware damage\), replications running in the source AZ can quickly restore in the target AZ.

For users of stateful applications, such as users of Microsoft Office 365, the data of these users must be stored on the disks of the servers with Microsoft Office 365 deployed. For such users, SDRS is suitable.

## DR Drill<a name="section143868154117"></a>

DR drills can be used to simulate fault scenarios, specify the emergency recovery solutions, and verify whether the solutions are applicable and effective. The existing services will not be affected during the DR drill. When a real fault occurs, you can use the solutions to rapidly restore services, enhancing service continuity.

