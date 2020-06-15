# Configuring Key Event Notification<a name="en-us_cts_01_0001"></a>

## **Scenarios**<a name="section227013810565"></a>

You can configure the key event notification function on CTS so that SMN can send messages to notify you of some key operations. This function is triggered by CTS, but notifications need to be sent by SMN. This function is used in the following scenarios: 

-   Real-time perception and confirmation of high-risk operations \(such as VM restart and security configuration changes\), cost-sensitive operations \(such as creating and deleting high-price resources\), and service-sensitive operations \(such as network configuration changes\)
-   Perception and confirmation of unauthorized operations such as login of a user with high permissions or operations of a user without required permissions
-   Interconnecting with your own audit system: All audit logs are synchronized to your audit system in real time to analyze the interface invoking success rate, unauthorized operations, security, and costs.

## Instructions<a name="section166121016175719"></a>

-   Key event notifications are sent to related subscribers using the SMN service. Therefore, before using CTS, you need to know how to create topics and add subscriptions on the SMN console.
-   Currently, you can create 100 custom notifications on CTS and specify the key operations, users, and topics for each notification.
-   You can configure key event notifications for a maximum of 50 users in 10 user groups. For each notification, you can select multiple users in one user group.
-   You can select a maximum of 1000 key operations of 100 cloud services for each notification.
-   The customized key event notification function is the upgrade version of the previous notification function. More configuration items and more powerful functions are provided. The old version will be brought offline recently.

## Procedure<a name="section50451709105654"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region-0.png)  in the upper left corner to select the desired region and project.
3.  Click  **Service List**  and choose  **Management & Deployment \> Cloud Trace Service**.
4.  In the navigation pane on the left, choose  **Key Event Notifications**.

    The  **Key Event Notifications**  page is displayed.

5.  Click  **Create Key Event Notification**. On the displayed page, specify required parameters.
6.  Enter a key event notification name.

    **Notification Name**: Identifies key event notifications. This parameter is mandatory. The value contains a maximum of 64 characters, and only letters, digits, and underscores \(\_\) are allowed.

7.  Configure key operations.

    You can select  **Typical**,  **All**, or  **Custom**  based on actual requirements:

    -   **Typical**: This scenario is suitable for routine audit of enterprises. Currently, CTS can enable text notifications pertaining to key operations such as creating and deleting some core resources of ECS, VPC, EVS, or KMS, and logging in to IAM.

        >![](/images/icon-note.gif) **NOTE:**   
        >Because IAM is a global service, the  **Login**  function is only provided for the central region of the current site. After this function is enabled, SMN deployed in the central region will send notifications upon the login of any region.  

    -   **All**: This scenario applies when CTS is interconnected with your own audit system. Notifications will be sent through SMN for all operations performed on interconnected cloud services. When  **All**  is selected, you cannot modify any settings, and CTS sends notifications for all traces sent from interconnected services by default. You are advised to use the SMN topic for which HTTPS is selected.
    -   **Custom**: This scenario is suitable for enterprises that require awareness and confirmation of high-risk, cost-sensitive, service-sensitive, and unauthorized operations. You can also interconnect CTS with your own audit system for log analysis. CTS enables you to configure key operations that can trigger notifications and add a maximum of 1000 key operations of 100 services. For details, see section "Supported Operations and Operation Lists" in the  _Cloud Trace Service User Guide_.

8.  Configure users.

    You can specify the users to whom SMN messages will be sent when they perform key operations.

    -   If you do not specify any users, CTS notifies all users when key operations are initiated.
    -   If you specify users, you can select whether to send SMN messages to subscribers. You can configure key event notifications for a maximum of 50 users in 10 user groups. For each notification, you can select multiple users in one user group.

9.  Configure an SMN topic.
    -   You can select an existing topic or create a one on the SMN console.
    -   If you do not want to send notifications, no further action is required.


