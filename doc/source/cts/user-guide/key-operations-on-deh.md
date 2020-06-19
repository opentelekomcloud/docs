# Key Operations on DeH<a name="en-us_topic_0100363619"></a>

Dedicated Host \(DeH\) is a service that provides dedicated physical hosts. You can create ECSs on a DeH to enhance isolation, security, and performance of your ECSs. When you migrate services to a DeH, you can continue to use your server software licenses used before the migration. That is, you can use the Bring Your Own License \(BYOL\) feature on the DeH to reduce costs and independently manage your ECSs.

With CTS, you can record operations associated with DeH for later query, audit, and backtrack operations.

**Table  1**  DeH operations that can be recorded by CTS

<a name="table188813184512"></a>
<table><thead align="left"><tr id="rafe0f5be22bb4a0fa55117b0ab049664"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="a96324e1de99b443dae5d6b2045b97b07"><a name="a96324e1de99b443dae5d6b2045b97b07"></a><a name="a96324e1de99b443dae5d6b2045b97b07"></a><strong id="b842352706103557"><a name="b842352706103557"></a><a name="b842352706103557"></a>Operation</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="a24d0fec456cb4876b9909b7040783eaa"><a name="a24d0fec456cb4876b9909b7040783eaa"></a><a name="a24d0fec456cb4876b9909b7040783eaa"></a><strong id="b84235270610360"><a name="b84235270610360"></a><a name="b84235270610360"></a>Resource Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="ad95b30f712ff475397d5ae41ad9b94dc"><a name="ad95b30f712ff475397d5ae41ad9b94dc"></a><a name="ad95b30f712ff475397d5ae41ad9b94dc"></a><strong id="b842352706182955"><a name="b842352706182955"></a><a name="b842352706182955"></a>Trace Name</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="rcfe449403b2648d6af8202c52d04d02f"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240334_p64815508530"><a name="en-us_topic_0100240334_p64815508530"></a><a name="en-us_topic_0100240334_p64815508530"></a>Creating a DeH</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240334_p552435568530"><a name="en-us_topic_0100240334_p552435568530"></a><a name="en-us_topic_0100240334_p552435568530"></a>dedicatedHosts</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240334_p455430588530"><a name="en-us_topic_0100240334_p455430588530"></a><a name="en-us_topic_0100240334_p455430588530"></a>createDedicatedHosts</p>
</td>
</tr>
<tr id="rb0ba5d10ea284dbf96e991b5a31233d9"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240334_p491111858530"><a name="en-us_topic_0100240334_p491111858530"></a><a name="en-us_topic_0100240334_p491111858530"></a>Updating a DeH</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240334_p185830118530"><a name="en-us_topic_0100240334_p185830118530"></a><a name="en-us_topic_0100240334_p185830118530"></a>dedicatedHosts</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240334_p288289388530"><a name="en-us_topic_0100240334_p288289388530"></a><a name="en-us_topic_0100240334_p288289388530"></a>updateDedicatedHosts</p>
</td>
</tr>
<tr id="r8c7ac965c5954cecb13f8319a4fa8a35"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240334_p112219868530"><a name="en-us_topic_0100240334_p112219868530"></a><a name="en-us_topic_0100240334_p112219868530"></a>Deleting a DeH</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240334_p365656758530"><a name="en-us_topic_0100240334_p365656758530"></a><a name="en-us_topic_0100240334_p365656758530"></a>dedicatedHosts</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240334_p90297338530"><a name="en-us_topic_0100240334_p90297338530"></a><a name="en-us_topic_0100240334_p90297338530"></a>releaseDedicatedHosts</p>
</td>
</tr>
</tbody>
</table>

