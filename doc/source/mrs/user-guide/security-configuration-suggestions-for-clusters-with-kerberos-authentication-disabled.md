# Security Configuration Suggestions for Clusters with Kerberos Authentication Disabled<a name="EN-US_TOPIC_0127570182"></a>

The Hadoop community version provides two authentication modes: Kerberos authentication \(security mode\) and Simple authentication \(normal mode\). When creating a cluster, you can choose to enable or disable Kerberos authentication.

Clusters in security mode use the Kerberos protocol for security authentication.

In normal mode, MRS cluster components use a native open source authentication mechanism, which is typically Simple authentication. If Simple authentication is used, authentication is automatically performed by a client user \(for example, user  **root**\) by default when a client connects to a server. The authentication is imperceptible to the administrator or service user. In addition, when being executed, the client may even pretend to be any user \(including  **superuser**\) by injecting  **UserGroupInformation**. Cluster resource management and data control APIs are not authenticated on the server and are easily exploited and attacked by hackers.

Therefore, in normal mode, network access permissions must be strictly controlled to ensure cluster security. You are advised to perform the following operations to ensure cluster security.

-   Deploy service applications on ECSs in the same VPC and subnet and avoid accessing MRS clusters through an external network.
-   Configure security group rules to strictly control the access scope. Do not configure access rules that allow  **Any**  or  **0.0.0.0**  for the inbound direction of MRS cluster ports.
-   If you want to access the native pages of the components in the cluster from the external, follow instructions in  [Creating an SSH Channel to Connect an MRS Cluster and Configuring the Browser](creating-an-ssh-channel-to-connect-an-mrs-cluster-and-configuring-the-browser.md)  for configuration.

