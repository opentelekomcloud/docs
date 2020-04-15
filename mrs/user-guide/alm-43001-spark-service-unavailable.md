# ALM-43001 Spark Service Unavailable<a name="EN-US_TOPIC_0125375691"></a>

## Description<a name="sc7e924ee37744c39bbfb24f5e893e4bf"></a>

The system checks the Spark service status every 60 seconds. This alarm is generated when the Spark service is unavailable and is cleared when the Spark service recovers.

## Attribute<a name="s70f283a8061646ffadbffbcd1feafb35"></a>

<a name="ta500fbcb0cb4438c956ed4644dc61df4"></a>
<table><thead align="left"><tr id="r5f9cb0e73fdd427693f4b4f1433c50a6"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="ad10fa11125994b4699a8101c7604ba28"><a name="ad10fa11125994b4699a8101c7604ba28"></a><a name="ad10fa11125994b4699a8101c7604ba28"></a><strong id="en-us_topic_0087163353_b5717331502"><a name="en-us_topic_0087163353_b5717331502"></a><a name="en-us_topic_0087163353_b5717331502"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="a19538cba98a84bfcb9a5926a9fff9c83"><a name="a19538cba98a84bfcb9a5926a9fff9c83"></a><a name="a19538cba98a84bfcb9a5926a9fff9c83"></a><strong id="en-us_topic_0087163353_b127219338016"><a name="en-us_topic_0087163353_b127219338016"></a><a name="en-us_topic_0087163353_b127219338016"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="a8ad9f6ecfb48404bb0347178b0973f5a"><a name="a8ad9f6ecfb48404bb0347178b0973f5a"></a><a name="a8ad9f6ecfb48404bb0347178b0973f5a"></a><strong id="en-us_topic_0087163353_b19814198947"><a name="en-us_topic_0087163353_b19814198947"></a><a name="en-us_topic_0087163353_b19814198947"></a>Automatically&nbsp;Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r993b21feabac47998425687f585e30de"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="aa5abc67abd3046fa811e25d70d03a603"><a name="aa5abc67abd3046fa811e25d70d03a603"></a><a name="aa5abc67abd3046fa811e25d70d03a603"></a>43001</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="ac003139a0f9a4f3ea6d9fb629e2ddafc"><a name="ac003139a0f9a4f3ea6d9fb629e2ddafc"></a><a name="ac003139a0f9a4f3ea6d9fb629e2ddafc"></a>Critical</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="a67cf0918bf294b8c833fbc9bc68b30d2"><a name="a67cf0918bf294b8c833fbc9bc68b30d2"></a><a name="a67cf0918bf294b8c833fbc9bc68b30d2"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="sfda18a6e6ef44e47ae5c4164c21e4a2c"></a>

<a name="tba063a9185c1403bb42b0612bab33832"></a>
<table><thead align="left"><tr id="r052defd0c4474a049f67b116b098570b"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="a9585cef436b54635bd12ac82d7539efd"><a name="a9585cef436b54635bd12ac82d7539efd"></a><a name="a9585cef436b54635bd12ac82d7539efd"></a><strong id="en-us_topic_0087163353_b19034291706"><a name="en-us_topic_0087163353_b19034291706"></a><a name="en-us_topic_0087163353_b19034291706"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="a4879a2c1f0d146d389d0833288068102"><a name="a4879a2c1f0d146d389d0833288068102"></a><a name="a4879a2c1f0d146d389d0833288068102"></a><strong id="en-us_topic_0087163353_b101361286011"><a name="en-us_topic_0087163353_b101361286011"></a><a name="en-us_topic_0087163353_b101361286011"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r1f772c0bd28048908298bb82c21aeef8"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a8260a717c505458087792f70de659c11"><a name="a8260a717c505458087792f70de659c11"></a><a name="a8260a717c505458087792f70de659c11"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ae9a06b6d1eef45fb9ca1217b4ae007d0"><a name="ae9a06b6d1eef45fb9ca1217b4ae007d0"></a><a name="ae9a06b6d1eef45fb9ca1217b4ae007d0"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="ra78e5f2f3d234cf58f9bddbb1e033bb0"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a0621235089574ecfa8c93ce2444acdef"><a name="a0621235089574ecfa8c93ce2444acdef"></a><a name="a0621235089574ecfa8c93ce2444acdef"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="aaf8f1a77c80740968ad265d0bc4fd1e7"><a name="aaf8f1a77c80740968ad265d0bc4fd1e7"></a><a name="aaf8f1a77c80740968ad265d0bc4fd1e7"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="r4ae353d8fc474adeaaf602c6231b058f"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a735306a2464242f9bfb9b42140aa0dfd"><a name="a735306a2464242f9bfb9b42140aa0dfd"></a><a name="a735306a2464242f9bfb9b42140aa0dfd"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="aa126aa91a17543089771834fd9e6be4b"><a name="aa126aa91a17543089771834fd9e6be4b"></a><a name="aa126aa91a17543089771834fd9e6be4b"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s37baca9f39bd4daaba96c2b212f71098"></a>

The tasks submitted by users fail to be executed.

## Possible Causes<a name="sec64a551321c44d9b9d5382f51728146"></a>

-   The KrbServer service is abnormal.
-   The LdapServer service is abnormal.
-   The ZooKeeper service is abnormal.
-   The HDFS service is abnormal.
-   The Yarn service is abnormal.
-   The corresponding Hive service is abnormal.

## Procedure<a name="sb551263b391343e6ab8c88d679f6346a"></a>

1.  **Check whether service unavailability alarms exist in services on which Spark depends.**
    1.  On MRS Manager, click  **Alarm**.
    2.  Check whether the following alarms exist in the alarm list:
        -   ALM-25500 KrbServer Service Unavailable
        -   ALM-25000 LdapServer Service Unavailable
        -   ALM-13000 ZooKeeper Service Unavailable
        -   ALM-14000 HDFS Service Unavailable
        -   ALM-18000 Yarn Service Unavailable
        -   ALM-16004 Hive Service Unavailable

            If yes, go to  [1.c](#lfc757e6a86134afa9254872ff9e1d162)

            If no, go to  [2](#l23f92b4f42a34b10a6f0a4c83b6f6fb4).

    3.  <a name="lfc757e6a86134afa9254872ff9e1d162"></a>Handle the service unavailability alarms based on the troubleshooting methods provided in the alarm help.

        After all the service unavailability alarms are cleared, wait a few minutes and check whether this alarm is cleared.

        -   If yes, no further action is required.
        -   If no, go to  [2](#l23f92b4f42a34b10a6f0a4c83b6f6fb4).

2.  <a name="l23f92b4f42a34b10a6f0a4c83b6f6fb4"></a>**Collect fault information.**
    1.  On MRS Manager, choose  **System \> Export Log**.
    2.  Select the following nodes from the  **Service**  drop-down list and click **OK** \(Hive is the specific Hive service determined based on **ServiceName**  in the alarm location information\).
        -   KrbServer
        -   LdapServer
        -   ZooKeeper
        -   HDFS
        -   Yarn
        -   Hive

    3.  Set  **Start Time** for log collection to 10 minutes ahead of the alarm generation time and **End Time** to 10 minutes behind the alarm generation time, and click **Download**.
    4.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="scf32f68a203f4c5281a48ac203c93a6e"></a>

N/A

