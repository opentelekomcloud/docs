# ALM-18006 MapReduce Job Execution Timeout<a name="EN-US_TOPIC_0125375584"></a>

## Description<a name="sf10f8e14c5b944fb9af9becb36ebdeb1"></a>

The alarm module checks MapReduce job execution every 30 seconds. This alarm is generated when the execution of a submitted MapReduce job times out. It must be manually cleared.

## Attribute<a name="s2fe1613282ba44dcb2072408aa941ae9"></a>

<a name="en-us_topic_0035998739_table58038438"></a>
<table><thead align="left"><tr id="en-us_topic_0035998739_row33645886"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="en-us_topic_0035998739_p40962215"><a name="en-us_topic_0035998739_p40962215"></a><a name="en-us_topic_0035998739_p40962215"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="en-us_topic_0035998739_p29605080"><a name="en-us_topic_0035998739_p29605080"></a><a name="en-us_topic_0035998739_p29605080"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="en-us_topic_0035998739_p49201274"><a name="en-us_topic_0035998739_p49201274"></a><a name="en-us_topic_0035998739_p49201274"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998739_row25880244"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0035998739_p15925039"><a name="en-us_topic_0035998739_p15925039"></a><a name="en-us_topic_0035998739_p15925039"></a>18006</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0035998739_p14859795"><a name="en-us_topic_0035998739_p14859795"></a><a name="en-us_topic_0035998739_p14859795"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0035998739_p62792710"><a name="en-us_topic_0035998739_p62792710"></a><a name="en-us_topic_0035998739_p62792710"></a>No</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="saec15b2100ba498fbcd15a2af9a7d208"></a>

<a name="en-us_topic_0035998739_table53044787"></a>
<table><thead align="left"><tr id="en-us_topic_0035998739_row2530563"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0035998739_p3649016"><a name="en-us_topic_0035998739_p3649016"></a><a name="en-us_topic_0035998739_p3649016"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0035998739_p27134857"><a name="en-us_topic_0035998739_p27134857"></a><a name="en-us_topic_0035998739_p27134857"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998739_row50439840"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998739_p59095202"><a name="en-us_topic_0035998739_p59095202"></a><a name="en-us_topic_0035998739_p59095202"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998739_p21982073"><a name="en-us_topic_0035998739_p21982073"></a><a name="en-us_topic_0035998739_p21982073"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998739_row63620936"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998739_p53022201"><a name="en-us_topic_0035998739_p53022201"></a><a name="en-us_topic_0035998739_p53022201"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998739_p66939890"><a name="en-us_topic_0035998739_p66939890"></a><a name="en-us_topic_0035998739_p66939890"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998739_row65588106"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998739_p11036355"><a name="en-us_topic_0035998739_p11036355"></a><a name="en-us_topic_0035998739_p11036355"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998739_p21529561"><a name="en-us_topic_0035998739_p21529561"></a><a name="en-us_topic_0035998739_p21529561"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998739_row59548322"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998739_p58684749"><a name="en-us_topic_0035998739_p58684749"></a><a name="en-us_topic_0035998739_p58684749"></a>Trigger condition</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998739_p55844233"><a name="en-us_topic_0035998739_p55844233"></a><a name="en-us_topic_0035998739_p55844233"></a>Generates an alarm when the actual indicator value exceeds the specified threshold.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="sd8bfdaf469784eb6922cdbffc36f027d"></a>

Because the execution times out, no execution result can be obtained.

## Possible Causes<a name="s27002b6a62614154a1362d64ca652971"></a>

The specified time period is shorter than the execution time. \(Executing a MapReduce job takes a long time.\)

## Procedure<a name="s86d48215768545fbbdd2319fde059bac"></a>

1.  Check whether time is improperly set.

    Set  **-Dapplication.timeout.interval**  to a larger value, or do not set the parameter. Execute the MapReduce job again and check whether it is executed successfully.

    -   If yes, go to  [2.d](#en-us_topic_0035998739_clean).
    -   If no, go to  [2.a](#l9d61eb755e3f41a9967f227528b43244).

2.  Check the Yarn service status.
    1.  <a name="l9d61eb755e3f41a9967f227528b43244"></a>In the alarm list on MRS Manager, check whether alarm  **ALM-18000 Yarn Service Unavailable**  is generated.
        -   If yes, go to  [2.b](#lbe2ecc21fe42444591465bfaaa1eaae8).
        -   If no, go to  [3](#l3f6577fc988143b09f22d3a0126fa7ad).

    2.  <a name="lbe2ecc21fe42444591465bfaaa1eaae8"></a>Rectify the fault by following the steps provided in  [ALM-18000 Yarn Service Unavailable](alm-18000-yarn-service-unavailable.md).
    3.  Run the MapReduce job command again to check whether the MapReduce job can be executed.
        -   If yes, go to  [2.d](#en-us_topic_0035998739_clean).
        -   If no, go to  [4](#l24f44a5a64234e9c963e6e65dfb0f5b4).

    4.  <a name="en-us_topic_0035998739_clean"></a>In the alarm list, choose  **Operation \>** ![](figures/h00296026-应用组件pdu-01_productdoc-image-a2bfb71d-9772-42d8-a0fb-ba94ca8f6857.png)  to manually clear the alarm. No further action is required.

3.  <a name="l3f6577fc988143b09f22d3a0126fa7ad"></a>Adjust the timeout threshold.

    On MRS Manager, choose  **System**  \>  **Configure Alarm Threshold**  \>  **Service**  \>  **Yarn**  \>  **Timed Out Tasks**, and increase the maximum number of timeout tasks allowed by the current threshold rule. Check whether the alarm is cleared.

    -   If yes, no further action is required.
    -   If no, go to  [4](#l24f44a5a64234e9c963e6e65dfb0f5b4).

4.  <a name="l24f44a5a64234e9c963e6e65dfb0f5b4"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="sf43d418a053644a7b816b4ba8d67a72c"></a>

N/A

