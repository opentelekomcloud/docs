# Dynamically Expanding Resources<a name="EN-US_TOPIC_0042018377"></a>

Before using AS to perform scaling actions, you must specify how to perform the scaling actions to dynamically expand resources.

If your demands change frequently, you can also configure alarm policies for dynamically expanding or reducing resources. When the conditions for triggering an AS policy are met, AS automatically changes the expected number of instances for triggering a scaling action to scale up or down resources. For details about how to create an alarm policy, see  [Creating an AS Policy](creating-an-as-policy.md).

For example, for a web application that allows users to purchase train tickets, when the CPU usage of the instances that run the application goes up to 90%, an instance needs to be added to ensure that services run properly. When the CPU usage goes down to 30%, an instance needs to be deleted to prevent resource waste. To meet the requirements, you can configure two alarm policies. The trigger condition of the first policy is that the maximum CPU usage becomes greater than 90% and the action is to add one instance.  The trigger condition of the second policy is that the minimum CPU usage becomes less than 30% and the action is to reduce one instance. 

