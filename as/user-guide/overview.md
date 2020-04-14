# Overview<a name="EN-US_TOPIC_0151270384"></a>

AS policies can trigger scaling actions to adjust the number of instances in an AS group. An AS policy defines the condition to trigger a scaling action and the operation to be performed during a scaling action. When the trigger condition is met, the system automatically triggers a scaling action.

AS supports the following policies:

-   Alarm policy: AS automatically increases or decreases the number of instances in an AS group or sets the number of instances to the configured value when an alarm is generated for a configured metric, such as CPU Usage.
-   Scheduled policy: AS automatically increases or decreases the number of instances in an AS group or sets the number of instances to the configured value at a specified time.
-   Periodic policy: AS automatically increases or decreases the number of instances in an AS group or sets the number of instances to the configured value at a configured interval, such as daily, weekly, and monthly.

AS supports dynamic and planned resource adjustment. AS uses the alarm policy to dynamically adjust the number of instances, and uses the scheduled or periodic policy to adjust the number of instances as planned. If the service load is difficult to predict, you can use the alarm policy. The system will trigger scaling actions based on real-time monitoring data \(such as CPU usage\) to dynamically adjust the number of instances in the AS group. If the service load changes regularly, you can use a scheduled or periodic policy to adjust the number of instances in the AS group.

