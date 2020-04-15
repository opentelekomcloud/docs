# Why Is the Interval That Backend Servers Receive Health Check Packets Is Different from the Configured Interval?<a name="EN-US_TOPIC_0210351704"></a>

Each LVS or Nginx node in the ELB cluster detects backend servers at the interval that you specified when adding the listener.

During this period, backend servers receive multiple detection packets from LVS and Nginx nodes. It seems that backend servers receive these packets at intervals shorter than the specified interval.

