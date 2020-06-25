# Why Can I Remotely Access an ECS But Cannot Ping It?<a name="EN-US_TOPIC_0018078505"></a>

## Symptom<a name="section112601346131"></a>

An ECS can be remotely accessed, but the EIP bound to it cannot be pinged.

## Possible Causes<a name="section20883121316810"></a>

A desired inbound rule is not added for the security group, and ICMP is not enabled.

## Solution<a name="section77204542"></a>

1.  Log in to the management console.
2.  Under  **Computing**, click  **Elastic Cloud Server**.
3.  On the  **Elastic Cloud Server**  page, click the name of the target ECS.

    The page providing details about the ECS is displayed.

4.  Click the  **Security Groups**  tab, expand the information of the security group, and click the security group ID.
5.  On the  **Inbound Rules**  tab of the  **Security Group**  page, click  **Add Rule**.
6.  Add an inbound rule for the security group and enable ICMP.
    -   **Protocol/Application**:  **ICMP**
    -   **Source**:  **IP address** **0.0.0.0/0**


