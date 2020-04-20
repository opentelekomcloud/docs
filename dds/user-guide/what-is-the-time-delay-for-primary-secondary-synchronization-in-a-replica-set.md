# What Is the Time Delay for Primary/Secondary Synchronization in a Replica Set?<a name="dds_faq_0006"></a>

The delay for primary/secondary synchronization cannot be calculated using a formula. The delay is affected by the following factors:

1.  Network communication status
2.  Transaction pressure on the primary node, that is, transactions per second \(TPS\) of the primary node
3.  Transaction size executed by the primary node, that is, the duration of a transaction execution
4.  Load of the secondary node

If the primary node bears heavy pressure within a period and executes a large number of transactions per second, the synchronization to the secondary node is delayed.

You can view  **Delay Between Primary and Secondary Nodes**  of the secondary node on the Cloud Eye console to know the synchronization delay.

