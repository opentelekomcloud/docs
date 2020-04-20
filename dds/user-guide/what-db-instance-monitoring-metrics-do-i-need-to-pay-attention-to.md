# What DB Instance Monitoring Metrics Do I Need to Pay Attention To?<a name="dds_faq_0019"></a>

You need to focus on the CPU, memory, and storage space usage.

You can configure DDS to report alarms as needed. If an alarm is reported, you can take proper measures to clear it.

**Configuration examples:**

-   Configure DDS to report alarms to Cloud Eye if CPU utilization reaching or exceeding a certain value \(90% for example\) for multiple times \(3 for example\) within a period of time \(5 minutes for example\).
-   Configure DDS to report alarms to Cloud Eye if its memory utilization reaches or exceeds a specific value \(for example, 90%\) multiple times \(for example, 4 times\) within a set period \(for example, 5 minutes\).
-   Configure DDS to report alarms to Cloud Eye if its storage utilization reaches or exceeds a specific value \(for example, 85%\) multiple times \(for example, 5 times\) within a set period \(for example, 5 minutes\).

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>For details on Cloud Eye alarm configuration, see "Alarm Rule Management" in  _Cloud Eye Service User Guide_.  

**Measures:**

If a storage usage alarm is reported, perform either of the following operations:

-   Check the storage space consumption and see whether any space can be freed up by deleting data from DB instances or dumping the data to another system.
-   Scale up the storage space. For details, see section  [Scaling Up Storage Space](scaling-up-storage-space.md).

