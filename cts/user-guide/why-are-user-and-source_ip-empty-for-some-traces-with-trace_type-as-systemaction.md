# Why Are  **user**  and  **source\_ip**  Empty for Some Traces with  **trace\_type**  as  **systemAction**?<a name="cts_faq_019"></a>

The  **trace\_type**  field indicates the request resource. This field can be  **ConsoleAction**,  **ApiCall**, and  **SystemAction**.

**SystemAction**  indicates that the operations are not triggered by users, such as automatic alarms, elastic scaling, scheduled backup tasks, and secondary invocations generated within the system to respond to the user's request. In this case, no user or device that triggers an operation exists. Therefore,  **user**  and  **source\_ip**  are both empty.

