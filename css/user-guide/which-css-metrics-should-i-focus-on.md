# Which CSS Metrics Should I Focus On?<a name="css_02_0007"></a>

The metrics that you need to focus on include the disk usage and cluster health status. You can log in to Cloud Eye and configure alarm prompts according to actual conditions. If alarms are reported, clear them by using related measures. For details about how to configure alarms, see  [Creating Alarm Rules](creating-alarm-rules.md).

**Configuration examples:**

-   Alarms are reported if the disk usage is higher than or equal to a specified value \(for example, 85%\) and has reached this value multiple times \(for example, 5 times\) within a specified time period \(for example, 5 minutes\).
-   Alarms are reported if the value of the cluster health status metric exceeds 0 for multiple times \(for example, 5 times\) within a specified time period \(for example, 5 minutes\).

**Measures:**

-   Upon receiving alarms related to the disk usage, view disk space consumption and check whether data can be deleted from cluster nodes or archived to other systems to release space.
-   If an alarm related to the cluster health status is received, check whether shard allocation is normal and whether shards are lost.

