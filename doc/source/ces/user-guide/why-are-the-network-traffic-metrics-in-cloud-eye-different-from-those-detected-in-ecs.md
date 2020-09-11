# Why Are the Network Traffic Metrics in Cloud Eye Different from Those Detected in ECS?<a name="EN-US_TOPIC_0084812087"></a>

The sample data collection interval in Cloud Eye is different from that used by the metric monitoring tool in the ECS.

Cloud Eye collects ECS and EVS data at four-minute intervals. The data collection interval for ECS second generation is 5 minutes. However, the metric monitoring tool in the ECS collects data at one-second intervals.

As the data collection cycle gets longer, the distortion of short time data increases. Therefore, Cloud Eye is suitable for monitoring long-term websites and applications running on ECSs.

Furthermore, you can configure alarm thresholds to generate alarms in the event of resource exceptions or insufficiency, improving resource reliability.

