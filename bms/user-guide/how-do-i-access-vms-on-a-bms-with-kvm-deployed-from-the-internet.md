# How Do I Access VMs on a BMS with KVM Deployed from the Internet?<a name="EN-US_TOPIC_0151841140"></a>

## Solution<a name="section185821210121911"></a>

You can install the port mapping software rinetd on a Linux BMS so that you can access VMs deployed on the BMS from the Internet. Take CentOS 7 as an example. Perform the following steps:

1.  Download the rinetd installation package from the following path and upload it to the BMS:

    [http://www.boutell.com/rinetd/http/rinetd.tar.gz](http://www.boutell.com/rinetd/http/rinetd.tar.gz)

2.  Run the following commands to install rinetd:

    **tar zxvf rinetd.tar.gz**

    **mkdir -p /usr/man/man8**

    **cd rinetd/**

    **make**

    **make install**

3.  Run the following command to add the port mapping rule to the configuration file:

    **vi /etc/rinetd.conf**

    The following is an example: Local IP address Local port VM internal IP address VM port

    **0.0.0.0 22222 192.168.124.81 22**

4.  Run the following command to start the rinetd process:

    **/usr/sbin/rinetd**

5.  Run the following command to connect to port 22222 corresponding to the BMS using SSH to access the VMs from the Internet:

    **ssh** _BMS EIP_**:22222**

    ![](figures/22.png)


