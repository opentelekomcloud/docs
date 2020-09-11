# ALM-27001 DBService Unavailable<a name="EN-US_TOPIC_0125375933"></a>

## Description<a name="s5756aef4410c4ca184f965bcea5071dc"></a>

The alarm module checks the DBService status every 30 seconds. This alarm is generated when the system detects that DBService is unavailable and is cleared when DBService recovers.

## Attribute<a name="sc97fbea08caa41e5ac67c8a259605dbd"></a>

<a name="en-us_topic_0035998745_table60151347"></a>
<table><thead align="left"><tr id="en-us_topic_0035998745_row54597003"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="en-us_topic_0035998745_p60281111"><a name="en-us_topic_0035998745_p60281111"></a><a name="en-us_topic_0035998745_p60281111"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="en-us_topic_0035998745_p50931783"><a name="en-us_topic_0035998745_p50931783"></a><a name="en-us_topic_0035998745_p50931783"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="en-us_topic_0035998745_p31833731"><a name="en-us_topic_0035998745_p31833731"></a><a name="en-us_topic_0035998745_p31833731"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998745_row28395444"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0035998745_p18329666"><a name="en-us_topic_0035998745_p18329666"></a><a name="en-us_topic_0035998745_p18329666"></a>27001</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0035998745_p8307988"><a name="en-us_topic_0035998745_p8307988"></a><a name="en-us_topic_0035998745_p8307988"></a>Critical</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0035998745_p1858451"><a name="en-us_topic_0035998745_p1858451"></a><a name="en-us_topic_0035998745_p1858451"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s92ca768dd9444bd4819f669a9d3e662e"></a>

<a name="en-us_topic_0035998745_table16316838"></a>
<table><thead align="left"><tr id="en-us_topic_0035998745_row11041789"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0035998745_p21969731"><a name="en-us_topic_0035998745_p21969731"></a><a name="en-us_topic_0035998745_p21969731"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0035998745_p34717793"><a name="en-us_topic_0035998745_p34717793"></a><a name="en-us_topic_0035998745_p34717793"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998745_row60677888"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998745_p15961928"><a name="en-us_topic_0035998745_p15961928"></a><a name="en-us_topic_0035998745_p15961928"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998745_p17847776"><a name="en-us_topic_0035998745_p17847776"></a><a name="en-us_topic_0035998745_p17847776"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998745_row26412257"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998745_p59018101"><a name="en-us_topic_0035998745_p59018101"></a><a name="en-us_topic_0035998745_p59018101"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998745_p15736877"><a name="en-us_topic_0035998745_p15736877"></a><a name="en-us_topic_0035998745_p15736877"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998745_row7414170"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998745_p63676932"><a name="en-us_topic_0035998745_p63676932"></a><a name="en-us_topic_0035998745_p63676932"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998745_p57557895"><a name="en-us_topic_0035998745_p57557895"></a><a name="en-us_topic_0035998745_p57557895"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="scdef08aca6da4e00accf91f4f9c3371f"></a>

The database service is unavailable and cannot provide data import or query functions for upper-layer services, which results in service exceptions.

## Possible Causes<a name="sc526370536294ade904d5d877af09062"></a>

-   The floating IP address does not exist.
-   There is no active DBServer instance.
-   The active and standby DBServer processes are abnormal.

## Procedure<a name="s3c19075e22df4816a33c913edeb75f1a"></a>

1.  Check whether the floating IP address exists in the cluster environment.
    1.  On MRS Manager, choose  **Service**  \>  **DBService**  \>  **Instance**.
    2.  Check whether the active instance exists.
        -   If yes, go to  [1.c](#en-us_topic_0035998745_step111).
        -   If no, go to  [2.a](#en-us_topic_0035998745_step88).

    3.  <a name="en-us_topic_0035998745_step111"></a>Select the active DBServer instance and record the IP address.
    4.  Log in to the host that corresponds to the preceding IP address, and run the  **ifconfig**  command to check whether the DBService floating IP address exists on the node.
        -   If yes, go to  [1.e](#en-us_topic_0035998745_checkfloatip).
        -   If no, go to  [2.a](#en-us_topic_0035998745_step88).

    5.  <a name="en-us_topic_0035998745_checkfloatip"></a>Run the  **ping** _floating IP__address_  command to check whether the DBService floating IP address can be pinged.
        -   If yes, go to  [1.f](#en-us_topic_0035998745_findfloatip).
        -   If no, go to  [2.a](#en-us_topic_0035998745_step88).

    6.  <a name="en-us_topic_0035998745_findfloatip"></a>Log in to the host that corresponds to the DBService floating IP address, and run the  **ifconfig** _interface_ **down**  command to delete the floating IP address.
    7.  On MRS Manager, choose  **Service**  \>  **DBService**  \>  **More**  \>  **Restart Service**  to restart DBService. Check whether DBService is restarted successfully.
        -   If yes, go to  [1.h](#en-us_topic_0035998745_resumealarm1).
        -   If no, go to  [2.a](#en-us_topic_0035998745_step88).

    8.  <a name="en-us_topic_0035998745_resumealarm1"></a>Wait about 2 minutes and check whether the alarm is cleared from the alarm list.
        -   If yes, no further action is required.
        -   If no, go to  [3.a](#en-us_topic_0035998745_loginact).

2.  Check the status of the active DBServer instance.
    1.  <a name="en-us_topic_0035998745_step88"></a>Select the DBServer instance whose role status is abnormal and record the IP address.
    2.  On the  **Alarm**  page, check whether alarm  **ALM-12007 Process Fault**  occurs in the DBServer instance on the host that corresponds to the IP address.
        -   If yes, go to  [2.c](#en-us_topic_0035998745_alarm27001).
        -   If no, go to  [4](#lf6335e7d8e9748e88cb53edd624c2526).

    3.  <a name="en-us_topic_0035998745_alarm27001"></a>Follow procedures in  **ALM-12007 Process Fault**  to handle the alarm.
    4.  Wait about 5 minutes and check whether the alarm is cleared from the alarm list.
        -   If yes, no further action is required.
        -   If no, go to  [4](#lf6335e7d8e9748e88cb53edd624c2526).

3.  Check the status of the active and standby DBServers.
    1.  <a name="en-us_topic_0035998745_loginact"></a>Log in to the host that corresponds to the DBService floating IP address, and run the  **sudo su - root** and **su - omm**  commands to switch to user  **omm**. Run the **cd $\{BIGDATA\_HOME\}/FusionInsight/dbservice/**  command to go to the installation directory of DBService.
    2.  Run the  **sh sbin/status-dbserver.sh**  command to view the status of DBService's active and standby HA processes. Check whether the status can be viewed successfully.
        -   If yes, go to  [3.c](#en-us_topic_0035998745_loginactive).
        -   If no, go to  [4](#lf6335e7d8e9748e88cb53edd624c2526).

    3.  <a name="en-us_topic_0035998745_loginactive"></a>Check whether the active and standby HA processes are normal.
        -   If yes, go to  [4](#lf6335e7d8e9748e88cb53edd624c2526).
        -   If no, go to  [3.d](#en-us_topic_0035998745_recoverdb).

    4.  <a name="en-us_topic_0035998745_recoverdb"></a>On MRS Manager, choose  **Service**  \>  **DBService**  \>  **More**  \>  **Restart Service**  to restart DBService, and check whether DBService is restarted successfully.
        -   If yes, go to  [3.e](#en-us_topic_0035998745_resumealarm).
        -   If no, go to  [4](#lf6335e7d8e9748e88cb53edd624c2526).

    5.  <a name="en-us_topic_0035998745_resumealarm"></a>Wait about 2 minutes and check whether the alarm is cleared from the alarm list.
        -   If yes, no further action is required.
        -   If no, go to  [4](#lf6335e7d8e9748e88cb53edd624c2526).

4.  <a name="lf6335e7d8e9748e88cb53edd624c2526"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="en-us_topic_0035998745_section570775"></a>

N/A

