# How Can I Check that the Traffic from the Frontend and to the Backend Is Inconsistent?<a name="EN-US_TOPIC_0132401669"></a>

Check whether there are requests failed to be processed, especially requests with  _4xx_  status code. The requests may be rejected by ELB because they are considered abnormal and are not forwarded to backend servers.

