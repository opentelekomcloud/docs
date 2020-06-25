# What Operation Will Be Suspended After An AS Group Is Disabled?<a name="EN-US_TOPIC_0141570908"></a>

After an AS group is disabled, the group will not automatically any trigger scaling actions, but the on-going scaling action will continue. Scaling policies will not trigger any scaling actions. After you manually change the number of expected instances, no scaling action is triggered although the number of actual instances is not equal to that of expected instances.

The health check continues to check the health status of the instances but does not remove the instances.

