# How Should I Handle Abnormal Instances in an AS Group?<a name="EN-US_TOPIC_0113805650"></a>

In normal cases, you do not need to handle instances in abnormal state because the AS service periodically checks the health status of instances in an AS group. When an AS group is enabled, abnormal instances are removed and new instances are created to ensure that the number of expected instances is the same as current instances. When an AS group is disabled, checking instance health status continues. However, AS will not remove instances.

It should be noted that if the ELB health check mode is selected, ELB sends heartbeat messages to backend ECSs through an intranet. Therefore, to ensure that the ELB health check can run properly, ensure that your ECS can be accessed through an intranet. Perform the following steps to check this:

1.  <a name="li25183589153427"></a>In the  **Listener**  area, locate the row containing the target listener and click  **View**  in the  **Health Check**  column. A dialog box is displayed.
    -   **Health Check Protocol**: Ensure that the protocol has been configured and port has been enabled for the ECS to be checked.
    -   **Check Path**: If HTTP is used for the health check, ensure that the health check path for backend ECSs is correct.

2.  Check whether software \(such as firewall\) on the ECS masks the source IP address performing the health check.
3.  Check whether the rules of backend ECS security groups and network ACL allow access by 100.125.0.0/16, and configure the protocol and port used for health check. Obtain the health check protocol and port from the dialog box displayed in step  [1](#li25183589153427).
    -   If the default health check mode is used, service ports of the backend ECSs must be enabled.
    -   If the health check port is different from service ports of the ECSs, communication between the service ports of the ECSs and health check port must be enabled.

4.  If the issue persists, contact technical support.

