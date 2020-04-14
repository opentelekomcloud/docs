# What Can I Do If Instances in an AS Group Frequently Fail in Health Checks and Are Deleted and Then Created Repeatedly?<a name="EN-US_TOPIC_0141570910"></a>

The security group rule of the instance must allow communication with the 100.125.0.0/16 network, and the protocol and port number must be the same as those used by ELB for health checks. Otherwise, the health check will fail. As a result, the instances will be deleted and created again and again.

