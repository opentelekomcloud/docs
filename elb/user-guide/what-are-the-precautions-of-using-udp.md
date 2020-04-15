# What Are the Precautions of Using UDP?<a name="EN-US_TOPIC_0112849191"></a>

## How UDP Health Checks Work<a name="section53210693319"></a>

UDP is a connectionless protocol, which does not establish a three-way handshake before sending data. A UDP health check is implemented as follows:

1.  The health check node sends an ICMP request message to the backend server based on the health check configuration.
    -   If the health check node receives an ICMP reply message from the backend server, it considers that the backend server is healthy and continues the health check.
    -   If the health check node does not receive an ICMP reply message from the backend server, it considers the backend server unhealthy.

2.  After receiving the ICMP reply message, the health check node sends a UDP probe packet to the backend server.
    -   If the health check node receives an ICMP Port Unreachable message from the backend server within the timeout duration, the server is considered unhealthy.
    -   If the health check node does not receive an ICMP Port Unreachable message from the backend server within the timeout duration, the server is healthy.


When you use UDP for health checks, you are advised to retain the default settings on the configuration page.

## Troubleshooting Procedure<a name="section1651117513338"></a>

If the port of the backend server is inconsistent with that displayed on the health check configuration page, perform the following operations:

1.  Check whether the timeout duration is too short.

    A possible cause is that the ICMP Echo Reply or ICMP Port Unreachable message returned by the backend server does not reach the health check node within the timeout duration. As a result, the health check result is inaccurate.

    It is recommended that you change the timeout duration to a larger value.

    The principle of UDP health checks is different from that of other health checks. Therefore, you are advised to set a longer health check timeout duration. Otherwise, the backend server may be considered healthy or unhealthy repeatedly.

2.  Check whether the backend server restricts the rates at which ICMP messages are generated.

For Linux, run the following commands to query the rate limit and rate mask:

```
sysctl -q net.ipv4.icmp_ratelimit
```

The default value is  **1000**.

```
sysctl -q net.ipv4.icmp_ratemask
```

The default value is  **6168**.

If the returned value of the first command is the default value or  **0**, run the following command to remove the rate limit of Port Unreachable messages:

```
sysctl -w net.ipv4.icmp_ratemask=6160
```

For more information, see the  _Linux Programmer's Manual_. In Linux, run the following command to display the manual:

```
man 7 icmp
```

You can visit  [http://man7.org/linux/man-pages/man7/icmp.7.html](http://man7.org/linux/man-pages/man7/icmp.7.html).

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>Once the rate limit is lifted, the number of ICMP Port Unreachable messages on the backend server will not be limited.  

## Precautions<a name="section1386314212366"></a>

Pay attention to the following points when using the UDP protocol:

-   Health check uses UDP and ping packets to detect the status of the backend server. To ensure smooth transmission of these packets, ensure that ICMP is enabled on the backend server by performing the following:

    Log in to the server and run the following command as user  **root**:

    **cat /proc/sys/net/ipv4/icmp\_echo\_ignore\_all**

    -   If the returned value is  **1**, ICMP is disabled.
    -   If the returned value is  **0**, ICMP is enabled.

-   If UDP is used, the health check result may be different from the actual status of servers.

    If a backend server runs Linux, the rate of ICMP packets on the server is limited due to the anti-ICMP attack protection mechanism of Linux. In this case, when a service exception occurs, ELB will not receive error message  **port XX unreachable**  and still determine that the health check is successful. As a result, there is an inconsistency between the health check result and the actual server status.

-   A listener that uses the UDP protocol cannot be not added to a private network classic load balancer.

