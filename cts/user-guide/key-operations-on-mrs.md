# Key Operations on MRS<a name="en-us_topic_0100363631"></a>

MapReduce Service \(MRS\) is a data processing and analysis service that is based on a cloud computing platform. It is stable, reliable, scalable, and easy to manage.

With CTS, you can record operations associated with MRS for later query, audit, and backtrack operations.

**Table  1**  MRS operations that can be recorded by CTS

<a name="table62813597184426"></a>
<table><thead align="left"><tr id="r8c41e65ddd9e4a8686f29fcacf0ab184"><th class="cellrowborder" valign="top" width="30.303030303030305%" id="mcps1.2.4.1.1"><p id="a6ce86ddfbe1447fab1fc17a5d983c9b9"><a name="a6ce86ddfbe1447fab1fc17a5d983c9b9"></a><a name="a6ce86ddfbe1447fab1fc17a5d983c9b9"></a><strong id="b842352706103557"><a name="b842352706103557"></a><a name="b842352706103557"></a>Operation</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.27272727272727%" id="mcps1.2.4.1.2"><p id="a2bcc9749a8554e7597f29142322de4ca"><a name="a2bcc9749a8554e7597f29142322de4ca"></a><a name="a2bcc9749a8554e7597f29142322de4ca"></a><strong id="b84235270610360"><a name="b84235270610360"></a><a name="b84235270610360"></a>Resource Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="42.42424242424242%" id="mcps1.2.4.1.3"><p id="a250839f2eefd40108074865cfb0a4773"><a name="a250839f2eefd40108074865cfb0a4773"></a><a name="a250839f2eefd40108074865cfb0a4773"></a><strong id="b842352706182955"><a name="b842352706182955"></a><a name="b842352706182955"></a>Trace Name</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r623e7fa2ba624825916daca6c67e5fe2"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="a0176ddb229d24adfb461ccc3765aa220"><a name="a0176ddb229d24adfb461ccc3765aa220"></a><a name="a0176ddb229d24adfb461ccc3765aa220"></a>Creating a cluster</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="aab773315151d42babe30f3d70de22072"><a name="aab773315151d42babe30f3d70de22072"></a><a name="aab773315151d42babe30f3d70de22072"></a>cluster</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="a5d984b470ff743af88b92752646c3c77"><a name="a5d984b470ff743af88b92752646c3c77"></a><a name="a5d984b470ff743af88b92752646c3c77"></a>createCluster</p>
</td>
</tr>
<tr id="r57d0b77068c046d98c8f72a6a3271ce4"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="a1b392f3a716e491d8036cfea33e7261f"><a name="a1b392f3a716e491d8036cfea33e7261f"></a><a name="a1b392f3a716e491d8036cfea33e7261f"></a>Deleting a cluster</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="ae725e06a491e44c894251fe15229d444"><a name="ae725e06a491e44c894251fe15229d444"></a><a name="ae725e06a491e44c894251fe15229d444"></a>cluster</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="a197f6856629741038cca443d10a1e7a3"><a name="a197f6856629741038cca443d10a1e7a3"></a><a name="a197f6856629741038cca443d10a1e7a3"></a>deleteCluster</p>
</td>
</tr>
<tr id="rc41114d375384cc7b538158479f32bf7"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240321_p448303184426"><a name="en-us_topic_0100240321_p448303184426"></a><a name="en-us_topic_0100240321_p448303184426"></a>Expanding a cluster</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="a9ad2fb5c42fc4bd184f70075bfc3d3c6"><a name="a9ad2fb5c42fc4bd184f70075bfc3d3c6"></a><a name="a9ad2fb5c42fc4bd184f70075bfc3d3c6"></a>cluster</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="a865a7fd7967c4e43aae7258249951db5"><a name="a865a7fd7967c4e43aae7258249951db5"></a><a name="a865a7fd7967c4e43aae7258249951db5"></a>scaleOutCluster</p>
</td>
</tr>
<tr id="r1e2e432022f04fb2bc214e6e6076f494"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="a8d96a5bf07ec4c39b152692875faf94c"><a name="a8d96a5bf07ec4c39b152692875faf94c"></a><a name="a8d96a5bf07ec4c39b152692875faf94c"></a>Shrinking a cluster</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="a0143fbf4b82f46ac996bdc037a2d4716"><a name="a0143fbf4b82f46ac996bdc037a2d4716"></a><a name="a0143fbf4b82f46ac996bdc037a2d4716"></a>cluster</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="a893190c50744439980ab6f73ba7f1a66"><a name="a893190c50744439980ab6f73ba7f1a66"></a><a name="a893190c50744439980ab6f73ba7f1a66"></a>scaleInCluster</p>
</td>
</tr>
</tbody>
</table>

