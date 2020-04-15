# What Can I Do If Switching from a Non-root User to User root Times Out?<a name="EN-US_TOPIC_0094801708"></a>

## Symptom<a name="section174441551144120"></a>

When you run the  **sudo**  command to switch to user  **root**  on a Ubuntu or Debian ECS, the system prompts connection timeout.

**Figure  1**  Connection timeout<a name="fig727412824411"></a>  
![](figures/connection-timeout.png "connection-timeout")

## Solution<a name="section1933384114410"></a>

1.  Log in to the ECS.
2.  Run the following command to edit the hosts configuration file:

    **vi /etc/hosts**

3.  Press  **i**  to enter editing mode.
4.  Add the IP address and hostname to the last line of the hosts configuration file.

    _Private IP address hostname_

    An example is provided as follows:

    If the ECS hostname is  **hostname**  and the private IP address of the ECS is 192.168.0.1, add the following statement:

    192.168.0.1 hostname

5.  Press  **Esc**  to exit editing mode.
6.  Run the following command to save the configuration and exit:

    **:wq**


>![](public_sys-resources/icon-note.gif) **NOTE:**   
>To update the hostname of a Ubuntu or Debian ECS, set the value of parameter  **manage\_etc\_hosts**  in the  **/etc/cloud/cloud.cfg**  file to  **false**  and update the new hostname in the  **/etc/hosts**  file. When editing the  **/etc/hosts**  file, do not delete the statement in the line where  **127.0.0.1**  is located. Otherwise, switching from a non-root user to user  **root**  will time out.  

