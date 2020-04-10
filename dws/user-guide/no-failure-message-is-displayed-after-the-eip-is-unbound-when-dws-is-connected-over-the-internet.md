# No Failure Message Is Displayed After the EIP Is Unbound When DWS Is Connected Over the Internet<a name="dws_03_0025"></a>

After the EIP is unbound, the network may be disconnected. However, the TCP layer fails to identify that the physical connection is faulty in time due to  **keepalive**  settings. As a result, the gsql, ODBC, and JDBC clients also cannot identify the network fault in time.

The duration when the database responds the disconnection message to the client depends on the settings of  **keepalive**  parameters. The specific algorithm for calculating the duration is  **keepalive\_time**  +  **keepalive\_probes**  x  **keepalive\_intvl**.

Values of  **keepalive**  parameters affect network communication stability. Therefore, adjust the parameter values based on service pressure and network conditions.

In the Linux environment, run the  **sysctl**  command to modify the following parameters:

-   net.ipv4.tcp\_keepalive\_time
-   net.ipv4.tcp\_keeaplive\_probes
-   net.ipv4.tcp\_keepalive\_intvl

For example, if you want to change the value of  **net.ipv4.tcp\_keepalive\_time**, run the following command to change the value to  **120**  seconds.

**sysctl net.ipv4.tcp\_keepalive\_time=120**

In the Windows environment, modify the following configuration information in registry  **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\services\\Tcpip\\Parameters**:

-   KeepAliveTime
-   KeepAliveInterval
-   TcpMaxDataRetransmissions \(equivalent to  **tcp\_keepalive\_probes**\)

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>If you cannot find the preceding parameters in registry  **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\services\\Tcpip\\Parameters**, add these parameters. Open  **Registry Editor**, right-click the blank area on the right, and choose  **Create**  \>  **DWORD \(32-bit\) Value**  to add these parameters.  

