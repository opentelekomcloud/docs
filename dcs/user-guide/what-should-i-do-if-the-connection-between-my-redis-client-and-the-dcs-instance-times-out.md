# What Should I Do If the Connection Between My Redis Client and the DCS Instance Times Out?<a name="en-us_topic_0054235831"></a>

Reconnect your client to the DCS instance.

The timeout is probably due to network connectivity problems or DCS instance errors. For example, if your DCS instance is overloaded or experiences a failover, your Redis client returns the error message "Connection timed out" or "Connection reset by peer".

Some Redis clients do not support automatic reconnection. If you use these Redis clients, the applications that use DCS must be able to proactively initiate reconnection.

