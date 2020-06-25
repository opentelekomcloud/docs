# What Is the Expected Number of Instances?<a name="EN-US_TOPIC_0141570907"></a>

The expected number of instances refers to the number of ECSs that are expected to run in an AS group. It is between the minimum number of instances and the maximum number of instances. You can manually change the expected number of instances or change it based on the scheduled, periodic, or alarm policies.

After you set the expected number of instances when creating an AS group and the number is not 0, a scaling action will be automatically triggered to add the required number of ECSs to the AS group.

Manually adjust the expected number of instances: After you manually change the number of expected instances, the current number of instances is not consistent with the expected number. As a result, a scaling action is triggered to adjust the number of instances in the AS group to the expected number.

Change the number of expected instances by scaling policies: After a scaling policy which adds two instances to an AS group is triggered, the system will add two to the expected number of instances. In this case, the system triggers a scaling action to add two instances so that the number of instances in the AS group is the same as the expected number.

