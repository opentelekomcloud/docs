# How Do I Prevent ECSs from Being Removed from an AS Group Automatically?<a name="EN-US_TOPIC_0117813398"></a>

You can enable instance protection for in-service ECSs in an AS group. After the configuration, when AS automatically reduces the number of ECSs in an AS group, the in-service ECSs with instance protection enabled will not be removed. You can also set the minimum number of instances for an AS group and the instance removal policy to ensure that an AS group has some in-service ECSs.

Unhealthy ECSs are removed from an AS group and new ECSs are created. Therefore, do not stop or delete ECSs that have been added to an AS group on the ECS console. The stopped or deleted ECSs are considered unhealthy and automatically removed from the AS group. Even when an AS group is disabled, AS checks the status of ECSs in the AS group. In this case, however, unhealthy ECSs will not be removed from the AS group.

