# Setting Health Check for a Container<a name="cce_01_0112"></a>

Health check  regularly checks the health status of containers during container running. If the health check function is not configured, a pod cannot detect service exceptions or automatically restart the service to restore it. This will result in a situation where the pod status is normal but the service in the pod is abnormal.

CCE provides the following health check probes:

-   **Liveness Probe**: checks whether a container exists. It is similar to the  **ps**  command that checks whether a process exists. If the liveness check of a container fails, the cluster restarts the container. If the liveness check is successful, no operation is executed. If the liveness check of a container fails, the cluster restarts the container.
-   **Readiness Probe**: checks whether a container is ready to process user requests. Upon detecting that the container is unready, service traffic will not be directed to the container. It may take a long time for some applications to start up before they can provide services. For example, loading disk data or relying on startup of an external module. In this case, the application process is running, but the application cannot provide services. To address this issue, this health check probe is used. If the container readiness check fails, the cluster masks all requests sent to the container. If the container readiness check is successful, the container can be accessed.

## Health Check Methods<a name="section476025319384"></a>

-   **HTTP request**

    This health check mode is applicable to containers that provide HTTP/HTTPS services. The cluster periodically initiates an HTTP/HTTPS GET request to such containers. If the return code of the HTTP/HTTPS response is within 200–399, the probe is successful. Otherwise, the probe fails. In this health check mode, you must specify a container listening port and an HTTP/HTTPS request path.

    For example, if you have an HTTP service container, after you specify port 80 for container listening and the HTTP request path  **/health-check**, the cluster periodically initiates the  **GET http://containerIP:80/health-check**  request to the container.

-   **TCP port**

    For a container that provides TCP communication services, the cluster periodically establishes a TCP connection to the container. If the connection is successful, the probe is successful. Otherwise, the probe fails. In this health check mode, you must specify a container listening port. For example, if you have an Nginx container with service port 80, after you configure TCP port probe for the container and specify port 80 for the probe, the cluster periodically initiates a TCP connection to port 80 of the container. If the connection is successful, the probe is successful. Otherwise, the probe fails.

-   **CLI**

    The CLI mode is an efficient health check mode. In this mode, you must specify an executable command in a container. The cluster will periodically execute the command in the container. If the command output is 0, the health check is successful. Otherwise, the health check fails.

    The CLI mode can be used to replace the following modes:

    -   TCP Link Setup Mode: Write a program script to connect to a container port. If the connection is successful, the script returns 0. Otherwise, the script returns –1.
    -   HttpGet Request Mode: Write a program script to run the wget command for a container.

        **wget http://127.0.0.1:80/health-check**

        Check the return code of the response. If the return code is within 200–399, the script returns 0. Otherwise, the script returns –1.

        >![](public_sys-resources/icon-notice.gif) **NOTICE:**   
        >-   Put the program to be executed in the container image so that the program can be executed.  
        >-   If the command to be executed is a shell script, do not directly specify the script as the command, but add a script interpreter. For example, if the script is  **/data/scripts/health\_check.sh**, you must specify  **sh/data/scripts/health\_check.sh**  for command execution. The reason is that the cluster is not in the terminal environment when executing programs in a container.  



## Common Parameter Description<a name="section2050653544516"></a>

**Table  1**  Common parameter description

<a name="t045a8ee10cb946eaa4c01da4319b7206"></a>
<table><thead align="left"><tr id="re3891f83a0b242b1bf3f178042398166"><th class="cellrowborder" valign="top" width="27%" id="mcps1.2.3.1.1"><p id="afec93a787dcb46788032cfc70a14a22e"><a name="afec93a787dcb46788032cfc70a14a22e"></a><a name="afec93a787dcb46788032cfc70a14a22e"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="73%" id="mcps1.2.3.1.2"><p id="en-us_topic_0052519475_p74835383351"><a name="en-us_topic_0052519475_p74835383351"></a><a name="en-us_topic_0052519475_p74835383351"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r82f45c7641534b8d80da858ce9ce9be7"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="p173810322919"><a name="p173810322919"></a><a name="p173810322919"></a>Initial Delay (s)</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="p173941610161614"><a name="p173941610161614"></a><a name="p173941610161614"></a>Check delay time in seconds. Set this parameter according to the normal startup time of services.</p>
<p id="en-us_topic_0052519475_p05855219373"><a name="en-us_topic_0052519475_p05855219373"></a><a name="en-us_topic_0052519475_p05855219373"></a>For example, if this parameter is set to 30, the health check will be started 30 seconds after the container is started. The time is reserved for containerized services to start.</p>
</td>
</tr>
<tr id="rf8dd0b9b29af4b96bcf3efaecb0c4bb2"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="p36325348374"><a name="p36325348374"></a><a name="p36325348374"></a>Timeout (s)</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="p052822120161"><a name="p052822120161"></a><a name="p052822120161"></a>Timeout duration. Unit: second.</p>
<p id="a376926047bc64e0a9304d6c9828fc5a2"><a name="a376926047bc64e0a9304d6c9828fc5a2"></a><a name="a376926047bc64e0a9304d6c9828fc5a2"></a>For example, if this parameter is set to <strong id="b84235270617502"><a name="b84235270617502"></a><a name="b84235270617502"></a>10</strong>, the timeout wait time for performing a health check is 10s. If the wait time elapses, the health check is regarded as a failure. If the parameter is left blank or set to <strong id="b84235270617523"><a name="b84235270617523"></a><a name="b84235270617523"></a>0</strong>, the default timeout time is 1s.</p>
</td>
</tr>
</tbody>
</table>

