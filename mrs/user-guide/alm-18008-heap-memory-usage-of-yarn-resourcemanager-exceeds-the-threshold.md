# ALM-18008 Heap Memory Usage of Yarn ResourceManager Exceeds the Threshold<a name="EN-US_TOPIC_0125375667"></a>

## Description<a name="sf51eae172a7743db9576484fab3b47be"></a>

The system checks the heap memory usage of Yarn ResourceManager every 30 seconds and compares the actual usage with the threshold. The alarm is generated when the heap memory usage of Yarn ResourceManager exceeds the threshold \(80% of the maximum memory by default\).

To change the threshold, choose  **System** \> **Threshold Configuration** \> **Service** \> **Yarn**. This alarm is cleared when the heap memory usage of Yarn ResourceManager is less than or equal to the threshold.

## Attribute<a name="sc089da1d61e74ddcabad5ceba2462da7"></a>

<a name="t6436834181124243bec6886685aa6cfb"></a>
<table><thead align="left"><tr id="r8bc573457f504048ad2d8ec3629b7446"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="a9faa13617e84406abf3b2d770b341762"><a name="a9faa13617e84406abf3b2d770b341762"></a><a name="a9faa13617e84406abf3b2d770b341762"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="a921c1175b4144600932caee3c6c4655f"><a name="a921c1175b4144600932caee3c6c4655f"></a><a name="a921c1175b4144600932caee3c6c4655f"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="a82a9794011c14f5b83f650e9a60f0bbc"><a name="a82a9794011c14f5b83f650e9a60f0bbc"></a><a name="a82a9794011c14f5b83f650e9a60f0bbc"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="rce30b9f54a07496691212adee7fce700"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="a171ef75fbafa4f4ea4ef278c28df3846"><a name="a171ef75fbafa4f4ea4ef278c28df3846"></a><a name="a171ef75fbafa4f4ea4ef278c28df3846"></a>18008</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="a2dee74266527480ba5865682eb0d1e98"><a name="a2dee74266527480ba5865682eb0d1e98"></a><a name="a2dee74266527480ba5865682eb0d1e98"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="a1cd52b2973944923b3d4b592ea516f47"><a name="a1cd52b2973944923b3d4b592ea516f47"></a><a name="a1cd52b2973944923b3d4b592ea516f47"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="sfe65e4f68e7f4b32ae59f85ec57b8820"></a>

<a name="t3a60c77410c54bdc82db6e1df5126b1c"></a>
<table><thead align="left"><tr id="rde224c1bd57d46459b55fb70436a13ca"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="a0b42f77af5a845ebbddb629342d40636"><a name="a0b42f77af5a845ebbddb629342d40636"></a><a name="a0b42f77af5a845ebbddb629342d40636"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="a5bc14d34b532456a83cf27f8416f8791"><a name="a5bc14d34b532456a83cf27f8416f8791"></a><a name="a5bc14d34b532456a83cf27f8416f8791"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r3b5ce6824c4440659ec62416b4e83764"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ab05864cd4d7245aeaeee971b2e3beb0d"><a name="ab05864cd4d7245aeaeee971b2e3beb0d"></a><a name="ab05864cd4d7245aeaeee971b2e3beb0d"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a17aa9496211047e3bff7f15b5216adcc"><a name="a17aa9496211047e3bff7f15b5216adcc"></a><a name="a17aa9496211047e3bff7f15b5216adcc"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="rd8b31259da5a4ee1a1e836e7dc324790"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="aa7bf835cb91744f68a99138d7d14675a"><a name="aa7bf835cb91744f68a99138d7d14675a"></a><a name="aa7bf835cb91744f68a99138d7d14675a"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ae3e21e37a56548ce9eb57a111189fb97"><a name="ae3e21e37a56548ce9eb57a111189fb97"></a><a name="ae3e21e37a56548ce9eb57a111189fb97"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="r98cd53d926a14747a9839fdb1dd441fb"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a9acf0e7db7614b5f8c50fd534721b030"><a name="a9acf0e7db7614b5f8c50fd534721b030"></a><a name="a9acf0e7db7614b5f8c50fd534721b030"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a51d1d05948f24f79b9f10c9b9945aabb"><a name="a51d1d05948f24f79b9f10c9b9945aabb"></a><a name="a51d1d05948f24f79b9f10c9b9945aabb"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="re2754b61aff2415487ebe32cbd80d891"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ae8f716b8cc3f4a4a993eb1278f7785e6"><a name="ae8f716b8cc3f4a4a993eb1278f7785e6"></a><a name="ae8f716b8cc3f4a4a993eb1278f7785e6"></a>Trigger Condition</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="adbeca1f06db64741a5e7049d5c34a7d9"><a name="adbeca1f06db64741a5e7049d5c34a7d9"></a><a name="adbeca1f06db64741a5e7049d5c34a7d9"></a>Generates an alarm when the actual indicator value exceeds the specified threshold.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s7cac88f2cc394b91954aae3b5a3e9e57"></a>

Overhigh heap memory usage of the Yarn ResourceManager deteriorates Yarn task submission and running performance or even causes OOM, which results in unavailable Yarn service.

## Possible Causes<a name="s10dfc97886e74b9fbf6e25606cc81299"></a>

The heap memory of the Yarn ResourceManager instance is overused or inappropriately allocated.

## Procedure<a name="s21abee465d544f28a1c180cdcf5999cd"></a>

**Check the heap memory usage.**

1.  On MRS Manager, click  **Alarm** and select the alarm whose **Alarm ID** is **18008**. Then check the IP address and role name of the instance in **Location**.
2.  On MRS Manager, choose  **Service** \> **Yarn** \> **Instance** \> **ResourceManager** \> **Customize** \> **Percentage of Used Heap Memory of the ResourceManager**.
3.  Check whether the used heap memory of ResourceManager reaches 80% of the maximum heap memory specified for ResourceManager.
    -   If yes, go to  [4](#l0913a530153f4d969d31dcca40ee1a27).
    -   If no, go to  [6](#l78d821be1633426ab1dc6716ed5df612).

4.  <a name="l0913a530153f4d969d31dcca40ee1a27"></a>On MRS Manager, choose  **Service** \> **Yarn** \> **Service Configuration** \> **All** \> **ResourceManager** \> **System**. Increase the value of **-Xmx** in the **GC\_OPTS** parameter as required, click **Save Configuration**, and select **Restart the affected services or instance**. Click **OK**  to restart the role instance.
5.  Check whether the alarm is cleared.
    -   If yes, no further action is required.
    -   If no, go to  [6](#l78d821be1633426ab1dc6716ed5df612).


**Collect fault information.**

1.  <a name="l78d821be1633426ab1dc6716ed5df612"></a>On MRS Manager, choose  **System** \> **Export Log**.
2.  Select the following node from the  **Service** drop-down list and click **OK**.
    -   NodeAgent
    -   Yarn

3.  Set  **Start Time** for log collection to 10 minutes ahead of the alarm generation time and **End Time** to 10 minutes behind the alarm generation time, and click **Download**.
4.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).

## Related Information<a name="s363714484ec94dca84219b52de6e71e6"></a>

N/A

