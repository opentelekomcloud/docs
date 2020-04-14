# Does an Abrupt Change on Monitoring Indicator Values Cause an Incorrect Scaling Action?<a name="EN-US_TOPIC_0042018400"></a>

No. Monitoring data used by AS is from Cloud Eye. The monitoring interval of Cloud Eye can be set to 5 minutes, 20 minutes, or 1 hour. Therefore, an abrupt change of monitoring indicator values will not cause an incorrect scaling action.

In addition, AS allows you to configure the cooldown period to prevent unnecessary scaling actions caused by frequently reported alarms. You can customize the cooldown period.

