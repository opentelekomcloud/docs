# Expanding Resources as Planned<a name="EN-US_TOPIC_0042018378"></a>

To satisfy demands that change regularly, you can configure a scheduled or periodic policy to scale resources at specified time or periodically. For details about how to create a scheduled or periodic policy, see  [Creating an AS Policy](creating-an-as-policy.md).

Take an online course selection web application as an example. This application is frequently used when a semester starts and seldom used in other periods of the semester. You can configure two scheduled policies at the beginning of each semester. The first policy triggers a scaling action to add an instance when the course selection starts, and the second policy triggers a scaling action to reduce an instance when the course selection ends, meeting students' requirements as well as reducing cost.

