# What Is a Cooldown Period? Why Is It Required?<a name="EN-US_TOPIC_0127556109"></a>

A cooldown period is a period of time after each scaling action is complete. During the cooldown period, scaling actions triggered by alarms will be denied. Scheduled and periodic scaling actions are not restricted.

Before an instance is added to the AS group, it requires 2 to 3 minutes to execute the configuration script to install and configure applications. The time varies depending on many factors, such as the instance specifications and startup scripts. Therefore, if an instance is put into use without cooldown after started, the system will continuously increase instances until the load decreases. After the new instances take over services, the system detects that the load is too low and decreases instances in the AS group. A cooldown prevents the AS group from repeatedly triggering unnecessary scaling actions.

The following uses an example to introduce the cooling principles:

When a traffic peak occurs, an alarm policy is triggered. In this case, AS automatically adds an instance to the AS group to help handle the added demands. However, it takes several minutes for the instance to start. After the instance is started, it takes a certain period of time to receive requests from ELB. During this period, alarms may be triggered continuously. As a result, an instance is added each time an alarm is triggered. If you set a cooldown time, after an instance is started, AS stops adding new instances according to the alarm policy until the specified period of time \(300 seconds by default\) passes. Therefore, the newly started instance has time to start processing application traffic. If an alarm is triggered again after the cooldown period elapses, AS starts another instance and the cooldown period takes effect again.

