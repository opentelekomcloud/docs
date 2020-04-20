# What Should I Do If a Database Client Problem Causes a Connection Failure?<a name="dds_faq_0014"></a>

Identify a DDS DB instance connection failure caused by a client problem from the following aspects.

1.  ECS Security Policy

    In Windows, check whether the DDS port is enabled in the Windows security policy.

    In Linux, run the  **iptables**  command to check whether the DDS port is enabled in firewall settings.

2.  Application Configuration

    Check whether the IP address, port parameter, and Java database connectivity \(JDBC\) are configured correctly.


>![](public_sys-resources/icon-note.gif) **NOTE:**   
>If the problem persists, contact post-sales technical support.  

