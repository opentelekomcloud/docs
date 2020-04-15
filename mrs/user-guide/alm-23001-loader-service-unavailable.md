# ALM-23001 Loader Service Unavailable<a name="EN-US_TOPIC_0125375426"></a>

## Description<a name="sabc88d49701045d582b02bfd7a30765e"></a>

The system checks the Loader service availability every 60 seconds. This alarm is generated when the Loader service is unavailable and is cleared when the Loader service recovers.

## Attribute<a name="s96d91fddd75449f3ae720a1aeec54d6f"></a>

<a name="t15e7ac3a0cd14acf9204e53ca751c6d6"></a>
<table><thead align="left"><tr id="rf2e36abe713c4ee79a0f900929f8de5d"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="a5813d960cc024c68a1b11f10e0b86de2"><a name="a5813d960cc024c68a1b11f10e0b86de2"></a><a name="a5813d960cc024c68a1b11f10e0b86de2"></a><strong id="af77258d02f314ae8a91402be3580a19e"><a name="af77258d02f314ae8a91402be3580a19e"></a><a name="af77258d02f314ae8a91402be3580a19e"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="a452bd3dc0e8f4b77933a89baa55ea478"><a name="a452bd3dc0e8f4b77933a89baa55ea478"></a><a name="a452bd3dc0e8f4b77933a89baa55ea478"></a><strong id="a6203b1b6853843ffbabd80d7971be426"><a name="a6203b1b6853843ffbabd80d7971be426"></a><a name="a6203b1b6853843ffbabd80d7971be426"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="a5a3b15f8973d4d079cb6f8230fbff4d6"><a name="a5a3b15f8973d4d079cb6f8230fbff4d6"></a><a name="a5a3b15f8973d4d079cb6f8230fbff4d6"></a><strong id="ad2fd958152e44eb58d103831cf5b40bb"><a name="ad2fd958152e44eb58d103831cf5b40bb"></a><a name="ad2fd958152e44eb58d103831cf5b40bb"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r783cbf0ec2c24252a3c0d171f3156b32"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="a2ed8055eb1e447689e4f76fc266960f6"><a name="a2ed8055eb1e447689e4f76fc266960f6"></a><a name="a2ed8055eb1e447689e4f76fc266960f6"></a>23001</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="a22a8ee13d8d64697a42154b9913f3634"><a name="a22a8ee13d8d64697a42154b9913f3634"></a><a name="a22a8ee13d8d64697a42154b9913f3634"></a>Critical</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="a7a077883e26b4c10b8d6c71fec311833"><a name="a7a077883e26b4c10b8d6c71fec311833"></a><a name="a7a077883e26b4c10b8d6c71fec311833"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="scf39399a533546428d363386b06f7850"></a>

<a name="t3287bbd623a148faad6f99a195b44ed9"></a>
<table><thead align="left"><tr id="rd0ca5c8f5b1d4583bb114bb7ebbf6e57"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="a2836e0a8b1bd42a2811d268e883f1022"><a name="a2836e0a8b1bd42a2811d268e883f1022"></a><a name="a2836e0a8b1bd42a2811d268e883f1022"></a><strong id="af8f623e2cb0e4215822ab610367d3ae8"><a name="af8f623e2cb0e4215822ab610367d3ae8"></a><a name="af8f623e2cb0e4215822ab610367d3ae8"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="a0ef4a7f1afd94e40bcaa6c5a4bf39e67"><a name="a0ef4a7f1afd94e40bcaa6c5a4bf39e67"></a><a name="a0ef4a7f1afd94e40bcaa6c5a4bf39e67"></a><strong id="a0edd7fb5f4ef4c6d8615fe5a0171ede2"><a name="a0edd7fb5f4ef4c6d8615fe5a0171ede2"></a><a name="a0edd7fb5f4ef4c6d8615fe5a0171ede2"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r50a2ce4317d049c7a2f7d7e39dcf905e"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ace1f514d874b43328ca39f1b63b6ff43"><a name="ace1f514d874b43328ca39f1b63b6ff43"></a><a name="ace1f514d874b43328ca39f1b63b6ff43"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a7f81822a28564dbcaf86c5acdfd4d725"><a name="a7f81822a28564dbcaf86c5acdfd4d725"></a><a name="a7f81822a28564dbcaf86c5acdfd4d725"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="re212639fcd794546a16c24d42342acac"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="aa5a8f9a58db04473b0c70d7747a9ffac"><a name="aa5a8f9a58db04473b0c70d7747a9ffac"></a><a name="aa5a8f9a58db04473b0c70d7747a9ffac"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0065810728_p410176895830"><a name="en-us_topic_0065810728_p410176895830"></a><a name="en-us_topic_0065810728_p410176895830"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="r6365d171439646b885d6f35b61665c91"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a37dfe7b236ca4405b8cf771bbf9f2c32"><a name="a37dfe7b236ca4405b8cf771bbf9f2c32"></a><a name="a37dfe7b236ca4405b8cf771bbf9f2c32"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="adae4a67625294f1bae66954272689c0c"><a name="adae4a67625294f1bae66954272689c0c"></a><a name="adae4a67625294f1bae66954272689c0c"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s74cc9eb13c834481b8d26915287e3728"></a>

Data loading, import, and conversion are unavailable.

## Possible Causes<a name="s2d312a87012d4edaa6152183ae636ef4"></a>

-   The services that Loader depends on are abnormal.
    -   ZooKeeper is abnormal.
    -   HDFS is abnormal.
    -   DBService is abnormal.
    -   Yarn is abnormal.
    -   MapReduce is abnormal.

-   The network is faulty. Loader cannot communicate with its dependent services.
-   Loader is running improperly.

## Procedure<a name="s6b9a5fa5a176448089133ddb62875ed3"></a>

1.  Check the ZooKeeper status.
    1.  On MRS Manager, choose  **Service \> ZooKeeper**. Check whether the health status of ZooKeeper is normal.
        -   If yes, go to  [1.c](#l7e711144abab46b69f72dd85d9d3a26a).
        -   If no, go to  [1.b](#l05236ee8900b4ca79f793a1cd65080b7).

    2.  <a name="l05236ee8900b4ca79f793a1cd65080b7"></a>Choose  **More \> Restart Service**  to restart ZooKeeper. After ZooKeeper starts, check whether alarm ALM-23001 Loader Service Unavailable is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [1.c](#l7e711144abab46b69f72dd85d9d3a26a).

    3.  <a name="l7e711144abab46b69f72dd85d9d3a26a"></a>On MRS Manager, check whether alarm ALM-12007 Process Fault is reported.
        -   If yes, go to  [1.d](#lee8f887d562e4d1ebe972b0395c0b2ab).
        -   If no, go to  [2.a](#l0e9f93075a82442abe60a9116a029ffe).

    4.  <a name="lee8f887d562e4d1ebe972b0395c0b2ab"></a>In  **Alarm Details**  of alarm ALM-12007 Process Fault, check whether  **ServiceName** is **ZooKeeper**.
        -   If yes, go to  [1.e](#lc5010ebf687746ecb413077e6894a835).
        -   If no, go to  [2.a](#l0e9f93075a82442abe60a9116a029ffe).

    5.  <a name="lc5010ebf687746ecb413077e6894a835"></a>Clear the alarm according to the handling suggestions of ALM-12007 Process Fault.
    6.  Check whether alarm ALM-23001 Loader Service Unavailable is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [2.a](#l0e9f93075a82442abe60a9116a029ffe).

2.  Check the HDFS status.
    1.  <a name="l0e9f93075a82442abe60a9116a029ffe"></a>On MRS Manager, check whether alarm ALM-14000 HDFS Service Unavailable is reported.
        -   If yes, go to  [2.b](#l18075383ac23408e8620bf75e9ddfe8c).
        -   If no, go to  [3.a](#en-us_topic_0065810728_li72981765544).

    2.  <a name="l18075383ac23408e8620bf75e9ddfe8c"></a>Clear the alarm according to the handling suggestions of ALM-14000 HDFS Service Unavailable.
    3.  Check whether alarm ALM-23001 Loader Service Unavailable is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [3.a](#en-us_topic_0065810728_li72981765544).

3.  Check the DBService status.
    1.  <a name="en-us_topic_0065810728_li72981765544"></a>On MRS Manager, choose  **Service \> DBService**. Check whether the health status of DBService is normal.
        -   If yes, go to  [3.a](#en-us_topic_0065810728_li72981765544).
        -   If no, go to  [3.b](#l4248a88a0ac5431fb05a6842aed908f8).

    2.  <a name="l4248a88a0ac5431fb05a6842aed908f8"></a>Choose  **More \> Restart Service**  to restart DBService. After DBService starts, check whether alarm ALM-23001 Loader Service Unavailable is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [4.a](#l26a5005a5739428596f257b9db8543f2).

4.  Check the MapReduce status.
    1.  <a name="l26a5005a5739428596f257b9db8543f2"></a>On MRS Manager, choose  **Service \> MapReduce**. Check whether the health status of MapReduce is normal.
        -   If yes, go to  [5.a](#le4df9b73a35f44d6abeb7163cf8d200e).
        -   If no, go to  [4.b](#l89f4e9819f724392a735481175a45bf5).

    2.  <a name="l89f4e9819f724392a735481175a45bf5"></a>Choose  **More \> Restart Service**  to restart MapReduce. After MapReduce starts, check whether alarm ALM-23001 Loader Service Unavailable is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [5.a](#le4df9b73a35f44d6abeb7163cf8d200e).

5.  Check the Yarn status.
    1.  <a name="le4df9b73a35f44d6abeb7163cf8d200e"></a>On MRS Manager, choose  **Service \> Yarn**. Check whether the health status of Yarn is normal.
        -   If yes, go to  [5.c](#l07fe99d1256a4f988c358c431b8e09ef).
        -   If no, go to  [5.b](#l29c403f2e1f946e39c2de2932aa87ff0).

    2.  <a name="l29c403f2e1f946e39c2de2932aa87ff0"></a>Choose  **More \> Restart Service**  to restart Yarn. After Yarn starts, check whether alarm ALM-23001 Loader Service Unavailable is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [5.c](#l07fe99d1256a4f988c358c431b8e09ef).

    3.  <a name="l07fe99d1256a4f988c358c431b8e09ef"></a>On MRS Manager, check whether alarm ALM-18000 Yarn Service Unavailable is reported.
        -   If yes, go to  [5.d](#l5c7cc070cd1f4bd3a57da52af8397461).
        -   If no, go to  [6.a](#l4f407905c7df4c8f810c4b7551f80b7c).

    4.  <a name="l5c7cc070cd1f4bd3a57da52af8397461"></a>Clear the alarm according to the handling suggestions of ALM-18000 Yarn Service Unavailable.
    5.  Check whether alarmALM-23001 Loader Service Unavailable is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [6.a](#l4f407905c7df4c8f810c4b7551f80b7c).

6.  Check the network connections between Loader and its dependent components.
    1.  <a name="l4f407905c7df4c8f810c4b7551f80b7c"></a>On MRS Manager, choose  **Service \> Loader**.
    2.  Click  **Instance**. The Sqoop instance list is displayed.
    3.  <a name="lda0629623917492982d2772bc34ba363"></a>Record the management IP addresses of all Sqoop instances.
    4.  Log in to the hosts using the IP addresses obtained in  [6.c](#lda0629623917492982d2772bc34ba363). Run the following commands to switch the user:

        **sudo su - root**

        **su - omm**

    5.  Run the  **ping**  command to check whether the network connection between the hosts where the Sqoop instances reside and the dependent components is normal. \(The dependent components include ZooKeeper, DBService, HDFS, MapReduce, and Yarn. The method to obtain the IP addresses of the dependent components is the same as that used to obtain the IP addresses of the Sqoop instances.\)
        -   If yes, go to  [7.a](#lf0c75803ba6a4701b5468bc8eeb53acb).
        -   If no, go to  [6.f](#le3345b870e6f4732bc915aa2ce6b19d6).

    6.  <a name="le3345b870e6f4732bc915aa2ce6b19d6"></a>Contact the network administrator to repair the network.
    7.  Check whether alarm ALM-23001 Loader Service Unavailable is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [7.a](#lf0c75803ba6a4701b5468bc8eeb53acb).

7.  Collect fault information.
    1.  <a name="lf0c75803ba6a4701b5468bc8eeb53acb"></a>On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


