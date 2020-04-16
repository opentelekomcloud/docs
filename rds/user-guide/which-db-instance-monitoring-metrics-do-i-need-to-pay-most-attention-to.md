# Which DB Instance Monitoring Metrics Do I Need to Pay Most Attention To?<a name="rds_faq_0036"></a>

You need to pay the most attention to CPU, memory, and storage space usage.

To stay aware of these metrics, you can configure the system to report alarms to Cloud Eye as needed. You can then take measures to clear any reported alarms.

**Configuration examples:**

-   Configure RDS to report alarms to Cloud Eye if its CPU utilization reaches or exceeds a specific value \(for example, 90%\) multiple times \(for example, 3 times\) within a set period \(for example, 5 minutes\).
-   Configure RDS to report alarms to Cloud Eye if its memory utilization reaches or exceeds a specific value \(for example, 90%\) multiple times \(for example, 4 times\) within a set period \(for example, 5 minutes\).
-   Configure RDS to report alarms to Cloud Eye if its storage utilization reaches or exceeds a specific value \(for example, 85%\) multiple times \(for example, 5 times\) within a set period \(for example, 5 minutes\).

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>For details on Cloud Eye alarm configuration, see the "Alarm Rule Management" section in the  _Cloud Eye User Guide_.  

**Measures:**

-   If a CPU or memory alarm is reported, you can scale up the vCPUs or memory by changing the DB instance class.

    For details, see section  [Changing a DB Instance Class](changing-a-db-instance-class.md).

-   If a storage space usage alarm is reported, perform either of the following operations:
    -   Check the storage space consumption to see whether any space can be freed up by deleting data from DB instances or dumping the data to another system.
    -   Scale up the storage space.

        For details, see section  [Scaling Up Storage Space](scaling-up-storage-space.md).



