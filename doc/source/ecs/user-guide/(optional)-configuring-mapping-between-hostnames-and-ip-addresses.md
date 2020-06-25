# \(Optional\) Configuring Mapping Between Hostnames and IP Addresses<a name="EN-US_TOPIC_0074752335"></a>

ECSs in the same VPC can communicate with each other using hostnames. In such a case, you are required to configure the mapping between hostnames and IP addresses. The communication using hostnames is more convenient than that using IP addresses.

## Constraints<a name="section1399111463019"></a>

This method applies only to Linux ECSs.

## Procedure<a name="section4184679493755"></a>

For example, there are two ECSs in a VPC, ecs-01 and ecs-02. Perform the following operations to enable communication using hostnames between ecs-01 and ecs-02:

1.  Log in to ecs-01 and ecs-02 and obtain their private IP addresses.
    1.  Log in to the management console.
    2.  Under  **Computing**, click  **Elastic Cloud Server**.
    3.  On the  **Elastic Cloud Server**  page, obtain the private IP address in the  **IP Address**  column.

        For example, the obtained private IP addresses are as follows:

        ecs-01: 192.168.0.1

        ecs-02: 192.168.0.2

2.  Obtain the hostnames for the two ECSs.
    1.  Log in to the ECS.
    2.  Run the following command to view the ECS hostname:

        **sudo hostname**

        For example, the obtained hostnames are as follows:

        ecs-01: hostname01

        ecs-02: hostname02

3.  Create mapping between the hostnames and IP addresses and add information about other ECSs in the same VPC.
    1.  Log in to ecs-01.
    2.  <a name="li6087483710276"></a>Run the following command to switch to user  **root**:

        **sudo su -**

    3.  Run the following command to edit the hosts configuration file:

        **vi /etc/hosts**

    4.  Press  **i**  to enter editing mode.
    5.  Add the statement in the following format to set up the mapping:

        _Private IP address hostname_

        For example, add the following statement:

        192.168.0.1 hostname01

        192.168.0.2 hostname02

    6.  Press  **Esc**  to exit editing mode.
    7.  <a name="li64061240102622"></a>Run the following command to save the configuration and exit:

        **:wq**

    8.  Log in to ecs-02.
    9.  Repeat  [3.b](#li6087483710276)  to  [3.g](#li64061240102622).

4.  Check whether the ECSs can communicate with each other using hostnames.

    Log in to an ECS in the same VPC, run the following command to ping the added host, and check whether the operation is successful:

    **ping **_hostname_


