# ALM-28001 Spark Service Unavailable<a name="EN-US_TOPIC_0125375566"></a>

## Description<a name="sa40900a890a84c8a8ac52c8928d741a0"></a>

The system checks the Spark service status every 30 seconds. This alarm is generated when the Spark service is unavailable and is cleared when the Spark service recovers.

## Attribute<a name="s78c00667b87f4e428f3a72bc3a902bb0"></a>

<a name="t92baeb84c8444e94b686519a48434ccd"></a>
<table><thead align="left"><tr id="reec2ba8c09f64a0b98df300cac03ff14"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="a5007029f2dd04b9381b10d9be5c84f37"><a name="a5007029f2dd04b9381b10d9be5c84f37"></a><a name="a5007029f2dd04b9381b10d9be5c84f37"></a><strong id="a6e141f8e16ce40c8a1b70f72401dc1c9"><a name="a6e141f8e16ce40c8a1b70f72401dc1c9"></a><a name="a6e141f8e16ce40c8a1b70f72401dc1c9"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="a8bff38bc11f04af7bb89a791989d7958"><a name="a8bff38bc11f04af7bb89a791989d7958"></a><a name="a8bff38bc11f04af7bb89a791989d7958"></a><strong id="a44bd4c4704dc449e9a024e9763628b33"><a name="a44bd4c4704dc449e9a024e9763628b33"></a><a name="a44bd4c4704dc449e9a024e9763628b33"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="adb2b42f4e40340e9a18c3ba3d6dee7e2"><a name="adb2b42f4e40340e9a18c3ba3d6dee7e2"></a><a name="adb2b42f4e40340e9a18c3ba3d6dee7e2"></a><strong id="a5b8689c95d184798941fe7838e5ec8c7"><a name="a5b8689c95d184798941fe7838e5ec8c7"></a><a name="a5b8689c95d184798941fe7838e5ec8c7"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r48a365a0701d467e987d26e85ae7c3c7"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="a75c96bd9edcf4e008f063dfb2bbf3e00"><a name="a75c96bd9edcf4e008f063dfb2bbf3e00"></a><a name="a75c96bd9edcf4e008f063dfb2bbf3e00"></a>28001</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="ad3cfcc166aef47018d2d935bdfdd81df"><a name="ad3cfcc166aef47018d2d935bdfdd81df"></a><a name="ad3cfcc166aef47018d2d935bdfdd81df"></a>Critical</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="aebc54af4f65e4ff9be891a9a75f5a239"><a name="aebc54af4f65e4ff9be891a9a75f5a239"></a><a name="aebc54af4f65e4ff9be891a9a75f5a239"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="sd705d3137da043df8f2c02173f48d819"></a>

<a name="en-us_topic_0035998748_table53044787"></a>
<table><thead align="left"><tr id="en-us_topic_0035998748_row2530563"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0035998748_p3649016"><a name="en-us_topic_0035998748_p3649016"></a><a name="en-us_topic_0035998748_p3649016"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0035998748_p27134857"><a name="en-us_topic_0035998748_p27134857"></a><a name="en-us_topic_0035998748_p27134857"></a><strong id="a519edcb3be9a48d982ed14af73e72244"><a name="a519edcb3be9a48d982ed14af73e72244"></a><a name="a519edcb3be9a48d982ed14af73e72244"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998748_row50439840"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998748_p59095202"><a name="en-us_topic_0035998748_p59095202"></a><a name="en-us_topic_0035998748_p59095202"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998748_p21982073"><a name="en-us_topic_0035998748_p21982073"></a><a name="en-us_topic_0035998748_p21982073"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998748_row63620936"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998748_p53022201"><a name="en-us_topic_0035998748_p53022201"></a><a name="en-us_topic_0035998748_p53022201"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998748_p66939890"><a name="en-us_topic_0035998748_p66939890"></a><a name="en-us_topic_0035998748_p66939890"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998748_row65588106"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998748_p11036355"><a name="en-us_topic_0035998748_p11036355"></a><a name="en-us_topic_0035998748_p11036355"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998748_p21529561"><a name="en-us_topic_0035998748_p21529561"></a><a name="en-us_topic_0035998748_p21529561"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s2321c96c0aed424d85fe41bf5c6689a1"></a>

The Spark tasks submitted by users fail to be executed.

## Possible Causes<a name="sc278333662bf4989892dc43034816b6a"></a>

Any of the following services is abnormal:

-   KrbServer
-   LdapServer
-   ZooKeeper
-   HDFS
-   Yarn
-   Hive

## Procedure<a name="s4778cc7648fb4acab31248834fe52528"></a>

1.  Check whether service unavailability alarms exist in services that Spark depends on.
    1.  On MRS Manager, click  **Alarm**.
    2.  Check whether any of the following alarms exists in the alarm list:
        1.  ALM-25500 KrbServer Service Unavailable
        2.  ALM-25000 LdapServer Service Unavailable
        3.  ALM-13000 ZooKeeper Service Unavailable
        4.  ALM-14000 HDFS Service Unavailable
        5.  ALM-18000 Yarn Service Unavailable
        6.  ALM-16004 Hive Service Unavailable

        -   If yes, go to  [1.c](#l5e1054aba71047c0b858c58b92875c02).
        -   If no, go to  [2](#l5312b2640f0d47068b7b69e64f9bd7a5).

    3.  <a name="l5e1054aba71047c0b858c58b92875c02"></a>Handle the alarms using the troubleshooting methods provided in the alarm help.

        After all the alarms are cleared, wait a few minutes and check whether this alarm is cleared.

        -   If yes, no further action is required.
        -   If no, go to  [2](#l5312b2640f0d47068b7b69e64f9bd7a5).

2.  <a name="l5312b2640f0d47068b7b69e64f9bd7a5"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="s96365b8091944b3aa0a2f2da0b8152cd"></a>

N/A

