# ALM-43011 Non-Heap Memory Usage of the JDBCServer Process Exceeds the Threshold<a name="EN-US_TOPIC_0125375659"></a>

## Description<a name="s04abd9c4f1f34de9a48d702f507d83c7"></a>

The system checks the non-heap memory usage of the JDBCServer process every 30 seconds. The alarm is generated when the non-heap memory usage of the JDBCServer process exceeds the threshold \(90% of the maximum memory\).

## Attribute<a name="sa13b87bf670a4de9b9d140d598b7f139"></a>

<a name="tece671a3d3dc4788b69f7aa62589697a"></a>
<table><thead align="left"><tr id="r6534d94ce350453e9c7e775bee7fdf9f"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="aa1e845ee99ba47b29fcd0898606c6bf1"><a name="aa1e845ee99ba47b29fcd0898606c6bf1"></a><a name="aa1e845ee99ba47b29fcd0898606c6bf1"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="a3574986377794b66b3ac6a58c1315360"><a name="a3574986377794b66b3ac6a58c1315360"></a><a name="a3574986377794b66b3ac6a58c1315360"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="afe748735b97747bdb836a66e540a79d8"><a name="afe748735b97747bdb836a66e540a79d8"></a><a name="afe748735b97747bdb836a66e540a79d8"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="r76e118fbead04d608d1ba8d6dc3bca1f"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="a651852193e33430898753269087cc258"><a name="a651852193e33430898753269087cc258"></a><a name="a651852193e33430898753269087cc258"></a>43011</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="a25f3ff47eed1458b9b253e20dccce672"><a name="a25f3ff47eed1458b9b253e20dccce672"></a><a name="a25f3ff47eed1458b9b253e20dccce672"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="aaa617272ce0042fb86ca1736ac14716d"><a name="aaa617272ce0042fb86ca1736ac14716d"></a><a name="aaa617272ce0042fb86ca1736ac14716d"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s3ae0e411336945ada314f2b5d30024f1"></a>

<a name="ta8df109e9e2541f7be53cc25946c4801"></a>
<table><thead align="left"><tr id="rab35b67eb71a4780b11af55f2210d41c"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="a06e8f358e72f477abcbb21e5ac577864"><a name="a06e8f358e72f477abcbb21e5ac577864"></a><a name="a06e8f358e72f477abcbb21e5ac577864"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="a71ce5e8ae3334295878dfddee2643c17"><a name="a71ce5e8ae3334295878dfddee2643c17"></a><a name="a71ce5e8ae3334295878dfddee2643c17"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="rd0546170d0a243f49ce88c11f90c1b55"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a749a7cd3d44346889f4ebcc80d09da74"><a name="a749a7cd3d44346889f4ebcc80d09da74"></a><a name="a749a7cd3d44346889f4ebcc80d09da74"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a17ca0a638f3745dd83fb9a63bb5d0bc1"><a name="a17ca0a638f3745dd83fb9a63bb5d0bc1"></a><a name="a17ca0a638f3745dd83fb9a63bb5d0bc1"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="r397f926d1d4748f9abc0ff7f5c10dc1f"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a03f9694eff2044e3b7100b6bde1491d3"><a name="a03f9694eff2044e3b7100b6bde1491d3"></a><a name="a03f9694eff2044e3b7100b6bde1491d3"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a1b791e8c8ddd440594eadea5046a8142"><a name="a1b791e8c8ddd440594eadea5046a8142"></a><a name="a1b791e8c8ddd440594eadea5046a8142"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="rbb1ab2dc24f3459c9140e0b9fd9a4d27"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a0885ba3a634c430b9e0ac4ea328794c3"><a name="a0885ba3a634c430b9e0ac4ea328794c3"></a><a name="a0885ba3a634c430b9e0ac4ea328794c3"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a6a4c9879580c411d864ae720b183137a"><a name="a6a4c9879580c411d864ae720b183137a"></a><a name="a6a4c9879580c411d864ae720b183137a"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s036c5e2ba95040f2b98ca9b0a51a114a"></a>

Overhigh non-heap memory usage of the JDBCServer process deteriorates JDBCServer running performance or even causes OOM, which results in unavailable JDBCServer process.

## Possible Causes<a name="sfedfbf85e4c540d6ada7e4643f78eb11"></a>

The non-heap memory of the JDBCServer process is overused or inappropriately allocated.

## Procedure<a name="s65db35ea8ad9427fa538c23f43daba80"></a>

1.  Check non-heap memory usage.
    1.  On MRS Manager, click  **Alarm** and select the alarm whose **Alarm ID** is **43011**. Then check the IP address and role name of the instance in **Location**.
    2.  On MRS Manager, choose  **Service** \> **Spark** \> **Instance** and click the JDBCServer for which the alarm is generated to enter the **Instance Status** page. Then choose **Customize** \> **Statistics for the non-heap memory of the JDBCServe Process** and click **OK**.
    3.  Check whether the used non-heap memory of the JDBCServer process reaches 90% of the maximum non-heap memory specified for JDBCServer.
        -   If yes, go to  [1.d](#l327124029aba49f0976d1b4ea2d1921b).
        -   If no, go to  [2](#l7874f49605914d52af72cef71fe7757f).

    4.  <a name="l327124029aba49f0976d1b4ea2d1921b"></a>On MRS Manager, choose  **Service** \> **Spark** \> **Service Configuration**, and set **Type** to **All**. Choose **JDBCServer** \> **Tuning**. Increase the value of**-XX:MaxMetaspaceSize** in **spark.driver.extraJavaOptions**  as required.
    5.  Check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [2](#l7874f49605914d52af72cef71fe7757f).

2.  <a name="l7874f49605914d52af72cef71fe7757f"></a>Collect fault information.
    1.  On MRS Manager, choose  **System** \> **Export Log**.
    2.  Select  **Spark** from the **Service** drop-down list and click **OK**.
    3.  Set  **Start Time** for log collection to 10 minutes ahead of the alarm generation time and **End Time** to 10 minutes behind the alarm generation time, and click **Download**.
    4.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="sde1beade2dfb444ca7af54f2c8fb1fe0"></a>

N/A

