# What Should I Do If a Database Client Problem Causes a Connection Failure?<a name="rds_faq_0021"></a>

Identify an RDS connection failure caused by a client problem from the following aspects.

1.  ECS Security Policy

    In Windows, check whether the RDS DB instance port is enabled in the Windows security policy. In Linux, run the  **iptables**  command to check whether the RDS DB instance port is enabled in firewall settings.

2.  Application Configuration

    Check whether the connection address, port parameter configuration, and JDBC connection parameter configuration are correct.

3.  Incorrect User Name or Password

    Check whether the user name or password is correct if an error similar to the following occurs during RDS DB connection:

    -   \[Warning\] Access denied for user 'username'@'yourIp' \(using password: NO\)
    -   \[Warning\] Access denied for user 'username'@'yourIp' \(using password: YES\)
    -   Login failed for user 'username'


>![](public_sys-resources/icon-note.gif) **NOTE:**   
>If the problem persists, contact post-sales technical support.  

