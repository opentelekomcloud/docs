# Configuring an Instance Removal Policy<a name="EN-US_TOPIC_0044005301"></a>

When instances are automatically removed from your AS group, the instances that are not in the currently used AZs will be removed first. Besides, AS will check whether instances are evenly distributed in the currently used AZs. If the number of instances in an AZ is greater than that in other AZs, AS attempts to balance load between AZs when removing instances. If the load between AZs is balanced, AS removes instances following the pre-configured instance removal policy.

AS supports the following instance removal policies:

-   **Oldest instance**: The oldest instance is removed from the AS group first. Use this policy if you want to replace old instances by new instances in an AS group.
-   **Newest instance**: The latest instance is removed from the AS group first. Use this policy if you want to test a new AS configuration and do not want to retain it.
-   **Oldest instance created from oldest AS configuration**: The oldest instance created based on the oldest configuration is removed from the AS group first. Use this policy if you want to update an AS group and delete the instances created based on early AS configurations gradually.
-   **Newest instance created from oldest AS configuration**: The latest instance created based on the oldest configuration is removed from the AS group first.

>![](/images/icon-note.gif) **NOTE:**   
>A manually added ECS is removed in the lowest priority. AS does not delete a manually added ECS when removing it. If multiple manually added ECSs must be removed, AS preferentially removes the earliest-added ECS.  

