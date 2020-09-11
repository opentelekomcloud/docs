# ALM-12053 File Handle Usage Exceeds the Threshold<a name="EN-US_TOPIC_0125375912"></a>

## Description<a name="s0b56c53b7c4d41e9bee11e31f741d2ff"></a>

The system checks the file handle usage every 30 seconds and compares the actual usage with the threshold \(the default threshold is 80%\). This alarm is generated when the file handle usage exceeds the threshold for several times \(5 times by default\) consecutively.

To change the threshold, choose  **System**  \>  **Threshold Configuration**  \>  **Device**  \>  **Host**  \>  **Host Status**  \>  **Host File Handle Usage**  \>  **Host File Handle Usage**.

When the  **hit number**  is 1, this alarm is cleared when the host file handle usage is less than or equal to the threshold. When the  **hit number**  is greater than 1, this alarm is cleared when the host file handle usage is less than or equal to 90% of the threshold.

## Attribute<a name="sf6048e1494124094a5c5db46a784a7de"></a>

<a name="t08b590ce8be94484bc33ea12b29ab227"></a>
<table><thead align="left"><tr id="r9581b802bbc6400eb82f0737c7dff31b"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="a6913635adcc94bb09d989669edee6639"><a name="a6913635adcc94bb09d989669edee6639"></a><a name="a6913635adcc94bb09d989669edee6639"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="a55025b15c65945c583e2d7b48f473b1f"><a name="a55025b15c65945c583e2d7b48f473b1f"></a><a name="a55025b15c65945c583e2d7b48f473b1f"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="a56e7d92a792644cd8307d0cdfcc38996"><a name="a56e7d92a792644cd8307d0cdfcc38996"></a><a name="a56e7d92a792644cd8307d0cdfcc38996"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="ra2409bfef18b41269d6e6d5dcfc90b5d"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="a8180a12fe11d4b9ebdb6bcbac99caa67"><a name="a8180a12fe11d4b9ebdb6bcbac99caa67"></a><a name="a8180a12fe11d4b9ebdb6bcbac99caa67"></a>12053</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="adc7131beafc64e5d8c386a1f6a14a6f4"><a name="adc7131beafc64e5d8c386a1f6a14a6f4"></a><a name="adc7131beafc64e5d8c386a1f6a14a6f4"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="aab2c0478ea7e4e1598969fd2b539a1d6"><a name="aab2c0478ea7e4e1598969fd2b539a1d6"></a><a name="aab2c0478ea7e4e1598969fd2b539a1d6"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="sa4c1a5c570cb43bf94efe3e5cfd3b1d1"></a>

<a name="td1efa290a49b4f2587b8a8543d98171c"></a>
<table><thead align="left"><tr id="r1ccbe51d7487442abc32b31099cb86e4"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="adf180650d21044d2b0bf5774806f18d7"><a name="adf180650d21044d2b0bf5774806f18d7"></a><a name="adf180650d21044d2b0bf5774806f18d7"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="ab77eb301a27c434fb10007d857d95075"><a name="ab77eb301a27c434fb10007d857d95075"></a><a name="ab77eb301a27c434fb10007d857d95075"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="rab0bb2b0f5bf4167afb0bdb1413053c8"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a45c14ef198144748813c4236efde5e03"><a name="a45c14ef198144748813c4236efde5e03"></a><a name="a45c14ef198144748813c4236efde5e03"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="adf1c61f0e69c4fff998979cf8dfb913f"><a name="adf1c61f0e69c4fff998979cf8dfb913f"></a><a name="adf1c61f0e69c4fff998979cf8dfb913f"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="r7e7b9d9a9e80464abb437015a66f9d21"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a7ea5262176f24c729fbacec9673c1f6c"><a name="a7ea5262176f24c729fbacec9673c1f6c"></a><a name="a7ea5262176f24c729fbacec9673c1f6c"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ab5e706409d1c4237920f78f5f73d2656"><a name="ab5e706409d1c4237920f78f5f73d2656"></a><a name="ab5e706409d1c4237920f78f5f73d2656"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="rf7a8d21f5357437da98ead40c137beb1"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a3bfc17a39107416d8f191cf5d60a1d9b"><a name="a3bfc17a39107416d8f191cf5d60a1d9b"></a><a name="a3bfc17a39107416d8f191cf5d60a1d9b"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a854fbadfd8b844d1b5c26b754b6dd561"><a name="a854fbadfd8b844d1b5c26b754b6dd561"></a><a name="a854fbadfd8b844d1b5c26b754b6dd561"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="r9099fc395b7542c0915c14ebe0486595"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="aa6c6916357cf4a639644805eed8dfd73"><a name="aa6c6916357cf4a639644805eed8dfd73"></a><a name="aa6c6916357cf4a639644805eed8dfd73"></a>Trigger Condition</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a8153fe5b02754870874c975f25f17acc"><a name="a8153fe5b02754870874c975f25f17acc"></a><a name="a8153fe5b02754870874c975f25f17acc"></a>Generates an alarm when the actual indicator value exceeds the specified threshold.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s4fda38ad42c846e9954c8a4174907172"></a>

The I/O operations, such as opening a file or connecting to network, cannot be performed and programs are abnormal.

## Possible Causes<a name="sbf7da2f1e8ca49eba007b75672a17831"></a>

-   The number of file handles cannot meet the current service requirements.
-   The system is abnormal.

## Procedure<a name="sdbf7a073c1aa4b89894228d09155d5d6"></a>

**Increase the number of file handles.**

1.  On MRS Manager, click the alarm in the real-time alarm list. In the  **Alarm Details**  area, obtain the IP address of the host for which the alarm is generated.
2.  Use PuTTY to log in to the host for which the alarm is generated as user  **root**.
3.  Run the  **ulimit -n**  command to check the current maximum number of file handles of the system.
4.  If the file handle usage exceeds the threshold, contact the system administrator to increase the number of file handles.
5.  Wait 5 minutes and check whether the alarm is cleared.
    -   If yes, no further action is required.
    -   If no, go to  [6](#lc15b874d78744665b94240fbca556064).


**Check whether the system environment is abnormal.**

1.  <a name="lc15b874d78744665b94240fbca556064"></a>Contact the system administrator to check whether the operating system is abnormal.
    -   If yes, go to  [7](#l7736008db330452c8c079d39b713f2ce)  to rectify the fault.
    -   If no, go to  [9](#l3ab046424b6b4121b8ae44f692cef102).

2.  <a name="l7736008db330452c8c079d39b713f2ce"></a>Wait 5 minutes and check whether the alarm is cleared.
    -   If yes, no further action is required.
    -   If no, go to  [9](#l3ab046424b6b4121b8ae44f692cef102).


**Collect fault information.**

1.  On MRS Manager, choose  **System**  \>  **Export Log**.
2.  <a name="l3ab046424b6b4121b8ae44f692cef102"></a>Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).

    Telephone:

    Germany: 0800 330 44 44

    International: +800 44556600


## Related Information<a name="sba01dc9522ca4b28b94feb5e7783b336"></a>

N/A

