## Interconnecting SMN with Other Cloud Services


### Scenarios

SMN can be interconnected with CES to offer comprehensive alarm notifications.

You can configure flexible alarm and notification rules in CES to send resource status and performance updates to users so that they can prevent potential service interruptions.

When you create an alarm rule, you can choose whether to enable the notification function. If it is enabled, SMN will send a notification to users after CES generates an alarm. Currently, notifications can be sent using emails and SMS messages.

CES has predefined the message content and template for invoking SMN. You only need to create an SMN topic and add subscriptions to it, and then subscribers can receive event notifications based on the alarm rule configured in CES. Alternatively, you can create a user group when configuring the alarm rule in CES so that users in the group can receive notifications.

For details about creating an SMN topic and adding subscriptions, see sections <a href="Creating a Topic">Creating a Topic</a> and <a href="Adding a Subscription to the Topic">Adding a Subscription to the Topic</a>. The following procedure describes how to add an alarm rule in CES.

### Configuration Example

When the CPU usage of an ECS is higher than 80%, the system sends a notification to specified users by email or SMS message.

The specific operations are as follows:

1.  On the CES console, choose **Alarm** and click **Add Alarm Rule**.

2.  Specify the required parameters. For example, you can select **Elastic Cloud Server** for **Service** and the ECS instance to be monitored for **Monitored Object**.

3.  Set **Metric** to **CPU Usage**.

4.  Set **Threshold** to **Max.** \> **80%**.

5.  Set **Occurrences** to **3** and **Monitoring Interval** to **5 minutes**.

6.  Select **Yes** for **Send Notification**.

7.  Select an SMN topic already created from the **Topic Name** drop-down list or click **Create Topic** to create a new one on the SMN console. For details about how to create an SMN topic, see section <a href="Creating a Topic">Creating a Topic</a>.

8.  After you create the topic, switch back to the **Add Alarm Rule** page, click ![](./figure/002.png) beside **Create Topic**, and select the topic you created.

	Click **OK**. Subscribers in the topic you selected will receive a confirmation message. Only when they confirm the subscription can they receive alarm notifications.

1.  Select **Generated alarm** for **Trigger Condition**.

2.  Click **OK**.

	If the CPU usage of the monitored ECS instance exceeds 80% for three consecutive times within five minutes, an alarm will be generated. Users A and B will receive alarm notifications by email, and user C can receive them by SMS message.

### Interconnecting SMN with a Third-Party Application


SMN provides simple APIs, which require very little initial development and no maintenance or management, and is charged on a pay-per-use basis.

Developers can easily integrate the powerful messaging function provided by SMN into their applications, so that these applications can call SMN APIs to send emails or SMS messages to individuals or user groups.
