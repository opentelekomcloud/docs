# ALM-25004 Abnormal LdapServer Data Synchronization<a name="EN-US_TOPIC_0125376032"></a>

## Description<a name="s46d8ac404095428788d4973e795d695e"></a>

This alarm is generated when LdapServer data on Manager is inconsistent or LdapServer data is different between LdapServer and Manager. It is cleared when the data becomes consistent.

## Attribute<a name="s3ce62f777bfa4221a2b383baa21a32f0"></a>

<a name="en-us_topic_0035998743_table53406450"></a>
<table><thead align="left"><tr id="en-us_topic_0035998743_row25792371"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="en-us_topic_0035998743_p8807292"><a name="en-us_topic_0035998743_p8807292"></a><a name="en-us_topic_0035998743_p8807292"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="en-us_topic_0035998743_p42302050"><a name="en-us_topic_0035998743_p42302050"></a><a name="en-us_topic_0035998743_p42302050"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="en-us_topic_0035998743_p3913996"><a name="en-us_topic_0035998743_p3913996"></a><a name="en-us_topic_0035998743_p3913996"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998743_row48598242"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0035998743_p44143566"><a name="en-us_topic_0035998743_p44143566"></a><a name="en-us_topic_0035998743_p44143566"></a>25004</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0035998743_p18859061"><a name="en-us_topic_0035998743_p18859061"></a><a name="en-us_topic_0035998743_p18859061"></a>Critical</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0035998743_p51188993"><a name="en-us_topic_0035998743_p51188993"></a><a name="en-us_topic_0035998743_p51188993"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="sbe310bc2c6bd47768f417e71ee14ad01"></a>

<a name="en-us_topic_0035998743_table52667802"></a>
<table><thead align="left"><tr id="en-us_topic_0035998743_row22098140"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0035998743_p45118907"><a name="en-us_topic_0035998743_p45118907"></a><a name="en-us_topic_0035998743_p45118907"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0035998743_p30752875"><a name="en-us_topic_0035998743_p30752875"></a><a name="en-us_topic_0035998743_p30752875"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998743_row7954964"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998743_p40372317"><a name="en-us_topic_0035998743_p40372317"></a><a name="en-us_topic_0035998743_p40372317"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998743_p48932206"><a name="en-us_topic_0035998743_p48932206"></a><a name="en-us_topic_0035998743_p48932206"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998743_row37736673"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998743_p36771698"><a name="en-us_topic_0035998743_p36771698"></a><a name="en-us_topic_0035998743_p36771698"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998743_p25717600"><a name="en-us_topic_0035998743_p25717600"></a><a name="en-us_topic_0035998743_p25717600"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998743_row30131813"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998743_p24757801"><a name="en-us_topic_0035998743_p24757801"></a><a name="en-us_topic_0035998743_p24757801"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998743_p59224828"><a name="en-us_topic_0035998743_p59224828"></a><a name="en-us_topic_0035998743_p59224828"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s8a7c67905d4645baa691d7ee29622030"></a>

LdapServer data inconsistency occurs because LdapServer data on Manager or in the cluster is damaged. The LdapServer process with damaged data cannot provide services externally, and the authentication functions of Manager and the cluster are affected.

## Possible Causes<a name="s8c6ac286e34f480e9e9f10032c8c6d9c"></a>

-   The network of the node where the LdapServer process locates is faulty.
-   The LdapServer process is abnormal.
-   The OS restart damages data on LdapServer.

## Procedure<a name="se53e7ac103a84b84a64511d1a602dcf1"></a>

1.  Check whether the network where the LdapServer nodes reside is faulty.
    1.  On MRS Manager, click  **Alarm**. Record the IP address of **HostName** in **Location**  of the alarm as IP1. If multiple alarms exist, record the IP addresses as IP1, IP2, and IP3.
    2.  Contact O&M personnel and log in to the node corresponding to IP1. Run the  **ping**  command on the node to check whether the IP address of the management plane of the active OMS node can be pinged.
        -   If yes, go to  [1.c](#l18a6cd22b54d4137994f0a4e888684b2).
        -   If no, go to  [2.a](#l2a9f68b3af404320bb449b6ea262fcc4).

    3.  <a name="l18a6cd22b54d4137994f0a4e888684b2"></a>Contact public cloud O&M personnel to recover the network and check whether alarm  **ALM-25004 Abnormal LdapServer Data Synchronization**  is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [2.a](#l2a9f68b3af404320bb449b6ea262fcc4).

2.  Check whether the LdapServer process is in the normal state.
    1.  <a name="l2a9f68b3af404320bb449b6ea262fcc4"></a>On the  **Alarm**  page of MRS Manager, check whether alarm  **ALM-12004 OLdap Resource Is Abnormal**  is generated.
        -   If yes, go to  [2.b](#ld8ff891d9d8e459ca4639828d40ad0c5).
        -   If no, go to  [2.d](#la4e67febad0c49c68699d5c85be09b4f).

    2.  <a name="ld8ff891d9d8e459ca4639828d40ad0c5"></a>Rectify the fault by following the steps provided in  **ALM-12004 OLdap Resource Is Abnormal**.
    3.  Check whether alarm  **ALM-25004 Abnormal LdapServer Data Synchronization**  is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [2.d](#la4e67febad0c49c68699d5c85be09b4f).

    4.  <a name="la4e67febad0c49c68699d5c85be09b4f"></a>On the  **Alarm**  page of MRS Manager, check whether alarm  **ALM-12007 Process Fault of LdapServer**  is generated.
        -   If yes, go to  [2.e](#en-us_topic_0035998743_step8).
        -   If no, go to  [3.a](#en-us_topic_0035998743_step10).

    5.  <a name="en-us_topic_0035998743_step8"></a>Rectify the fault by following the steps provided in  **ALM-12007 Process Fault**.
    6.  Check whether alarm  **ALM-25004 Abnormal LdapServer Data Synchronization**  is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [3.a](#en-us_topic_0035998743_step10).

3.  Check whether the OS restart damages data on LdapServer.
    1.  <a name="en-us_topic_0035998743_step10"></a>On MRS Manager, click  **Alarm**. Record the IP address of **HostName** in **Location**  of the alarm as IP1. If multiple alarms exist, record the IP addresses as IP1, IP2, and IP3. Choose  **Service**  \>  **LdapServer**  \>  **Service Configuration**, record the LdapServer port number as PORT. If the IP address in the alarm location information is the IP address of the standby OMS node, the port ID is the default port ID 21750.
    2.  Log in to the node corresponding to IP1 as user  **omm** and run the **ldapsearch -H ldaps://IP1:PORT -x -LLL -b dc=hadoop,dc=com**  command to check whether errors are displayed in the queried information. If the IP address is that of the standby OMS node, run  **export LDAPCONF=$\{CONTROLLER\_HOME\}/ldapserver/ldapserver/local/conf/ldap.conf**  before running the preceding command.
        -   If yes, go to  [3.c](#l1d75cbf780ab4d44967b8b66b7fa70ae).
        -   If no, go to  [4](#l70c04893fc734b37a319699a26999cda).

    3.  <a name="l1d75cbf780ab4d44967b8b66b7fa70ae"></a>Recover the LdapServer and OMS nodes using backup data before the alarm is generated. For details, see section "Recovering Manager Data" in the  _Administrator Guide_.

        >![](/images/icon-note.gif) **NOTE:**   
        >To restore data, use the OMS data and LdapServer data backed up at the same time. Otherwise, the service and operation may fail. To recover data when services are running properly, you are advised to manually back up the latest management data and then recover the data. Otherwise, Manager data produced between the backup and recovery points in time will be lost.  

    4.  Check whether alarm ALM-25004 Abnormal LdapServer Data Synchronization is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [4](#l70c04893fc734b37a319699a26999cda).

4.  <a name="l70c04893fc734b37a319699a26999cda"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="sa5db4ccd79d54f46aed28dfa3f78abd0"></a>

N/A

