# ALM-27004 Data Inconsistency Between Active and Standby DBServices<a name="EN-US_TOPIC_0125375575"></a>

## Description<a name="s8eaef8246ed940a9995b57579c0a2d94"></a>

The system checks the data synchronization status between the active and standby DBServices every 10 seconds. This alarm is generated when the synchronization status cannot be queried six times consecutively or when the synchronization status is abnormal. This alarm is cleared when data synchronization is normal.

## Attribute<a name="s6722eb2d62a343c9832c75dafe42f230"></a>

<a name="en-us_topic_0035998747_table15697576"></a>
<table><thead align="left"><tr id="en-us_topic_0035998747_row32894845"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="en-us_topic_0035998747_p47236811"><a name="en-us_topic_0035998747_p47236811"></a><a name="en-us_topic_0035998747_p47236811"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="en-us_topic_0035998747_p976457"><a name="en-us_topic_0035998747_p976457"></a><a name="en-us_topic_0035998747_p976457"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="en-us_topic_0035998747_p11984159"><a name="en-us_topic_0035998747_p11984159"></a><a name="en-us_topic_0035998747_p11984159"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998747_row31192822"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0035998747_p43590645"><a name="en-us_topic_0035998747_p43590645"></a><a name="en-us_topic_0035998747_p43590645"></a>27004</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0035998747_p41181381"><a name="en-us_topic_0035998747_p41181381"></a><a name="en-us_topic_0035998747_p41181381"></a>Critical</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0035998747_p47357582"><a name="en-us_topic_0035998747_p47357582"></a><a name="en-us_topic_0035998747_p47357582"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s2bd12467263d472b94d6b3ba2f9e312f"></a>

<a name="en-us_topic_0035998747_table10758903"></a>
<table><thead align="left"><tr id="en-us_topic_0035998747_row49957660"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0035998747_p20038698"><a name="en-us_topic_0035998747_p20038698"></a><a name="en-us_topic_0035998747_p20038698"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0035998747_p12521852"><a name="en-us_topic_0035998747_p12521852"></a><a name="en-us_topic_0035998747_p12521852"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998747_row7637115"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998747_p14626574"><a name="en-us_topic_0035998747_p14626574"></a><a name="en-us_topic_0035998747_p14626574"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998747_p43901854"><a name="en-us_topic_0035998747_p43901854"></a><a name="en-us_topic_0035998747_p43901854"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998747_row59572368"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998747_p60632485"><a name="en-us_topic_0035998747_p60632485"></a><a name="en-us_topic_0035998747_p60632485"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998747_p12284267"><a name="en-us_topic_0035998747_p12284267"></a><a name="en-us_topic_0035998747_p12284267"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998747_row43449544"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998747_p29752153"><a name="en-us_topic_0035998747_p29752153"></a><a name="en-us_topic_0035998747_p29752153"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998747_p61114224"><a name="en-us_topic_0035998747_p61114224"></a><a name="en-us_topic_0035998747_p61114224"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998747_row13157104"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998747_p59092488"><a name="en-us_topic_0035998747_p59092488"></a><a name="en-us_topic_0035998747_p59092488"></a>Local DBService HA Name</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998747_p21762200"><a name="en-us_topic_0035998747_p21762200"></a><a name="en-us_topic_0035998747_p21762200"></a>Specifies a local DBService HA.</p>
</td>
</tr>
<tr id="en-us_topic_0035998747_row61642077"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998747_p26952341"><a name="en-us_topic_0035998747_p26952341"></a><a name="en-us_topic_0035998747_p26952341"></a>Peer DBService HA Name</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998747_p35656026"><a name="en-us_topic_0035998747_p35656026"></a><a name="en-us_topic_0035998747_p35656026"></a>Specifies a peer DBService HA.</p>
</td>
</tr>
<tr id="en-us_topic_0035998747_row52468780"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998747_p22112815"><a name="en-us_topic_0035998747_p22112815"></a><a name="en-us_topic_0035998747_p22112815"></a>SYNC_PERSENT</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998747_p46307570"><a name="en-us_topic_0035998747_p46307570"></a><a name="en-us_topic_0035998747_p46307570"></a>Specifies the synchronization percentage.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s5d3eee21954448068d86e5523c8b171f"></a>

Data may be lost or abnormal if the active instance becomes abnormal.

## Possible Causes<a name="s3272fe4152c4406f9228f531a6536bc8"></a>

-   The network between the active and standby nodes is unstable.
-   The standby DBService is abnormal.
-   The disk space of the standby node is full.

## Procedure<a name="s436c52b43bda46a898b686144fe64712"></a>

1.  Check whether the network between the active and standby nodes is in the normal state.
    1.  Log in to MRS Manager, click  **Alarm**, click the row where the alarm is located in the alarm list, and view the IP address of the standby DBService in the alarm details.
    2.  Log in to the active DBService node.
    3.  Run the  **ping** _heartbeat IP address of_ _the standby_ _DBService_  command to check whether the standby DBService node is reachable.
        -   If yes, go to  [2.a](#l94679874db6446889077ad52c361d328).
        -   If no, go to  [1.d](#l00a6d9a4885f4070958e48e106a17d86).

    4.  <a name="l00a6d9a4885f4070958e48e106a17d86"></a>Contact the public cloud O&M personnel to check whether the network is faulty.
        -   If yes, go to  [1.e](#l8bd2f9ed30b94cd2ad566126fe461d09).
        -   If no, go to  [2.a](#l94679874db6446889077ad52c361d328).

    5.  <a name="l8bd2f9ed30b94cd2ad566126fe461d09"></a>Rectify the network fault and check whether the alarm is cleared from the alarm list.
        -   If yes, no further action is required.
        -   If no, go to  [2.a](#l94679874db6446889077ad52c361d328).

2.  Check whether the standby DBService is in the normal state.
    1.  <a name="l94679874db6446889077ad52c361d328"></a>Log in to the standby DBService node.
    2.  Run the following command to switch the user:

        **sudo su - root**

        **su - omm**

    3.  Go to the  **$\{DBSERVER\_HOME\}/sbin** directory and run the **./status-dbserver.sh**  command to check whether the GaussDB resource status of the standby DBService is in the normal state. In the command output, check whether the following information is displayed in the row where  **ResName** is **gaussDB**:

        For example:

        ```
        10_10_10_231 gaussDB Standby_normal Normal Active_standby
        ```

        -   If yes, go to  [3.a](#lb01023be8604450f9d69f7d08e31a793).
        -   If no, go to  [4](#lee97ac4901cf4405b92a45e4bcff0a34).

3.  Check whether the disk space of the standby node is insufficient.
    1.  <a name="lb01023be8604450f9d69f7d08e31a793"></a>Use PuTTY to log in to the standby DBService node as user  **root**.
    2.  Run the  **su - omm** command to switch to user **omm**.
    3.  Go to the  **$\{DBSERVER\_HOME\}**  directory, and run the following commands to obtain the DBService data directory:

        **cd $\{DBSERVER\_HOME\}**

        **source .dbservice\_profile**

        **echo $\{DBSERVICE\_DATA\_DIR\}**

    4.  Run the  **df -h**  command to check the system disk partition usage.
    5.  Check whether the DBService data directory space is full.
        -   If yes, go to  [3.f](#l063d6adc4576465a9feb6dae4a7d30cc).
        -   If no, go to  [4](#lee97ac4901cf4405b92a45e4bcff0a34).

    6.  <a name="l063d6adc4576465a9feb6dae4a7d30cc"></a>Perform an upgrade and expand the capacity.
    7.  After capacity expansion, wait 2 minutes and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [4](#lee97ac4901cf4405b92a45e4bcff0a34).

4.  <a name="lee97ac4901cf4405b92a45e4bcff0a34"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="se0322a5727dc490fbba3452c74fb385f"></a>

N/A

