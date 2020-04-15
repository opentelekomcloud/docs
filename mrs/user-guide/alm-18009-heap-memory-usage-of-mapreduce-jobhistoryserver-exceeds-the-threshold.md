# ALM-18009 Heap Memory Usage of MapReduce JobHistoryServer Exceeds the Threshold<a name="EN-US_TOPIC_0125375364"></a>

## Description<a name="s7980881b9f474752ada6dc7d578f8dc6"></a>

The system checks the heap memory usage of MapReduce JobHistoryServer every 30 seconds and compares the actual usage with the threshold. The alarm is generated when the heap memory usage of MapReduce JobHistoryServer exceeds the threshold \(80% of the maximum memory by default\).

To change the threshold, choose  **System** \> **Threshold Configuration** \> **Service** \> **MapReduce**. This alarm is cleared when the heap memory usage of MapReduce JobHistoryServer is less than or equal to the threshold.

## Attribute<a name="see8ab95615d54c508caab4995e616698"></a>

<a name="tcc070353c1ff4d3a8f6f7fd4ad3e2f8a"></a>
<table><thead align="left"><tr id="r3ea37c76d2ee4e0bbb6ce446dc3d4653"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="a10e50e29d19e4ecd9a441eedf5b4ca08"><a name="a10e50e29d19e4ecd9a441eedf5b4ca08"></a><a name="a10e50e29d19e4ecd9a441eedf5b4ca08"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="a68d41b20ab6643fe96b487aa234d531b"><a name="a68d41b20ab6643fe96b487aa234d531b"></a><a name="a68d41b20ab6643fe96b487aa234d531b"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="a1b1be691028448f2a56f709ba8774347"><a name="a1b1be691028448f2a56f709ba8774347"></a><a name="a1b1be691028448f2a56f709ba8774347"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="rc9b08429da9f4f18b626c75725d17ac3"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="aeeaf04da7b004f58bf620be917f7e7e2"><a name="aeeaf04da7b004f58bf620be917f7e7e2"></a><a name="aeeaf04da7b004f58bf620be917f7e7e2"></a>18009</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="a7c5f120278dd465481449cbf6451acff"><a name="a7c5f120278dd465481449cbf6451acff"></a><a name="a7c5f120278dd465481449cbf6451acff"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="a3b6882a0033245778341485e4e710c00"><a name="a3b6882a0033245778341485e4e710c00"></a><a name="a3b6882a0033245778341485e4e710c00"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s79962ec5e1bd4d2bbc35fe0b7507fa45"></a>

<a name="t849d86b324054c5c9f374f3d92ac7373"></a>
<table><thead align="left"><tr id="reae41dfd723744e0b5e612c7f7d89a51"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="a8c211b19327942ea976a7538607cc989"><a name="a8c211b19327942ea976a7538607cc989"></a><a name="a8c211b19327942ea976a7538607cc989"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="a0098964078044692bb6d67a61d055864"><a name="a0098964078044692bb6d67a61d055864"></a><a name="a0098964078044692bb6d67a61d055864"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="rf501bcc2605641f5a78ed7d7dd0f20dc"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a44ca8b4ac8a54a2a9500d00756ab8bdd"><a name="a44ca8b4ac8a54a2a9500d00756ab8bdd"></a><a name="a44ca8b4ac8a54a2a9500d00756ab8bdd"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a126afc1361824827adaae236b3cb4b66"><a name="a126afc1361824827adaae236b3cb4b66"></a><a name="a126afc1361824827adaae236b3cb4b66"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="r57b23386515648ec99f764223b3b5964"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a4e9ea555a0fd4d96bc13515fbd98460a"><a name="a4e9ea555a0fd4d96bc13515fbd98460a"></a><a name="a4e9ea555a0fd4d96bc13515fbd98460a"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="af459c7855e85440da0b4fc4a56935d01"><a name="af459c7855e85440da0b4fc4a56935d01"></a><a name="af459c7855e85440da0b4fc4a56935d01"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="r34cdc7c510e94a8381b5ec952a14232a"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a7a8ce83ce99f4ace8a19cee63cc8d28b"><a name="a7a8ce83ce99f4ace8a19cee63cc8d28b"></a><a name="a7a8ce83ce99f4ace8a19cee63cc8d28b"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a1c64ffc789ff435a85a058f405f1cbc4"><a name="a1c64ffc789ff435a85a058f405f1cbc4"></a><a name="a1c64ffc789ff435a85a058f405f1cbc4"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="raeb51d2b0c1343cea8c41a12187943d5"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a5c600aa50a344cffb6268fbde4350aa5"><a name="a5c600aa50a344cffb6268fbde4350aa5"></a><a name="a5c600aa50a344cffb6268fbde4350aa5"></a>Trigger Condition</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a3ea83044f0f04c96aa80d4d66df68691"><a name="a3ea83044f0f04c96aa80d4d66df68691"></a><a name="a3ea83044f0f04c96aa80d4d66df68691"></a>Generates an alarm when the actual indicator value exceeds the specified threshold.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s97585207a557429eac8eb4907005dc0e"></a>

Overhigh heap memory usage of the MapReduce JobHistoryServer deteriorates performance of MapReduce log archiving or even causes OOM, which results in unavailable MapReduce service.

## Possible Causes<a name="sb8ea74a4caa74ac2a8b932ea5684fa6d"></a>

The heap memory of the MapReduce JobHistoryServer instance is overused or inappropriately allocated.

## Procedure<a name="s1853a8aeb5ab46fa865ddbb227a207c6"></a>

**Check the memory usage.**

1.  On MRS Manager, click  **Alarm** and select the alarm whose **Alarm ID** is **18009**. Then check the IP address and role name of the instance in **Location**.
2.  On MRS Manager, choose  **Service** \> **MapReduce** \> **Instance** \> **JobHistoryServer** \> **Customize** \> **Percentage of Used Heap Memory of the JobHistoryServer.**
3.  JobHistoryServer indicates the corresponding HostName of the instance for which the alarm is generated. Check the heap memory usage.
4.  Check whether the used heap memory of JobHistoryServer reaches 80% of the maximum heap memory specified for JobHistoryServer.
    -   If yes, go to  [5](#le860a5cfa925484993d16fc99b212a5c).
    -   If no, go to  [7](#le80ab327bfb44ad9b993636e256e5cc6).

5.  <a name="le860a5cfa925484993d16fc99b212a5c"></a>On MRS Manager, choose  **Service** \> **MapReduce** \> **Service Configuration** \> **All** \> **JobHistoryServer** \> **System**. Increase the value of **-Xmx** in the **GC\_OPTS** parameter as required, click **Save Configuration**, and select **Restart the affected services or instance**. Click **OK**  to restart the role instance.
6.  Check whether the alarm is cleared.
    -   If yes, no further action is required.
    -   If no, go to  [7](#le80ab327bfb44ad9b993636e256e5cc6).


**Collect fault information.**

1.  <a name="le80ab327bfb44ad9b993636e256e5cc6"></a>On MRS Manager, choose  **System** \> **Export Log**.
2.  Select the following node from the  **Service** drop-down list and click **OK**.
    -   NodeAgent
    -   MapReduce

3.  Set  **Start Time** for log collection to 10 minutes ahead of the alarm generation time and **End Time** to 10 minutes behind the alarm generation time, and click **Download**.
4.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).

## Related Information<a name="s38e940861f794fcfbf0ecd91a062ef05"></a>

N/A

