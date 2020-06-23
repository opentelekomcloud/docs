# What Should I Do If a DDS Server Problem Causes a Connection Failure?<a name="dds_faq_0015"></a>

Check whether the following problems occur on the DDS database. Check the following one at a time.

1.  The maximum number of connections is reached.

    **Solution**: Use the Cloud Eye resource monitoring function to check whether the number of current connections and the CPU usage are normal. If the number of connections or CPU usage reaches the maximum, restart the DDS database, disconnect DB instances, or increase the node quantity.

2.  DB instance status is normal, such as a restarting or system failure.

    **Solution**: Restart the DB instance to see if the problem is resolved. If the problem persists, contact post-sales technical support.


