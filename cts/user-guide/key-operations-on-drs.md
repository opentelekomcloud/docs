# Key Operations on DRS<a name="en-us_topic_0100363626"></a>

Data Replication Service \(DRS\) is an easy-to-use, stable, and efficient cloud service used for database migration and synchronization. DRS makes data flow between databases simple, greatly reducing data transfer costs. DRS enables you to quickly transfer data between databases in different scenarios.

With CTS, you can record operations associated with DRS for future query, audit, and backtrack operations.

**Table  1**  DRS operations that can be recorded by CTS

<a name="table736611611325"></a>
<table><thead align="left"><tr id="r3a3e42a6c378482780503e36b8adedeb"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="aedac587b4b3742fc94d93ff3487a9991"><a name="aedac587b4b3742fc94d93ff3487a9991"></a><a name="aedac587b4b3742fc94d93ff3487a9991"></a>Operation</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="a3f5ae52c35864072999081d073590efd"><a name="a3f5ae52c35864072999081d073590efd"></a><a name="a3f5ae52c35864072999081d073590efd"></a>Resource Type</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="a6233c63b47d748119b811028b6aafdd2"><a name="a6233c63b47d748119b811028b6aafdd2"></a><a name="a6233c63b47d748119b811028b6aafdd2"></a>Trace Name</p>
</th>
</tr>
</thead>
<tbody><tr id="r9d24c5a149e648c0bb64953bfd9c6eb1"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="a22847bdeb356483f992916d411c8e6c1"><a name="a22847bdeb356483f992916d411c8e6c1"></a><a name="a22847bdeb356483f992916d411c8e6c1"></a>Creating a task</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240370_p641337791171"><a name="en-us_topic_0100240370_p641337791171"></a><a name="en-us_topic_0100240370_p641337791171"></a>job</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="a8c89bc1074524c37a16c786f26c1ff82"><a name="a8c89bc1074524c37a16c786f26c1ff82"></a><a name="a8c89bc1074524c37a16c786f26c1ff82"></a>createJob</p>
</td>
</tr>
<tr id="ra4ea187a215446d2acb644c36385ede7"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240370_p656760711654"><a name="en-us_topic_0100240370_p656760711654"></a><a name="en-us_topic_0100240370_p656760711654"></a>Editing a task</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240370_p457557531171"><a name="en-us_topic_0100240370_p457557531171"></a><a name="en-us_topic_0100240370_p457557531171"></a>job</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="a5b844863609d45b8bd50e370f7e5d8f0"><a name="a5b844863609d45b8bd50e370f7e5d8f0"></a><a name="a5b844863609d45b8bd50e370f7e5d8f0"></a>modifyJob</p>
</td>
</tr>
<tr id="r72f6314da7cd4aa58d1e860e2f1fb3b0"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="af4d1df0edd2a476f948eb0ff1512f7ca"><a name="af4d1df0edd2a476f948eb0ff1512f7ca"></a><a name="af4d1df0edd2a476f948eb0ff1512f7ca"></a>Deleting a task</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240370_p28388601171"><a name="en-us_topic_0100240370_p28388601171"></a><a name="en-us_topic_0100240370_p28388601171"></a>job</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="a09ee28a45d1942459c88d487448b170d"><a name="a09ee28a45d1942459c88d487448b170d"></a><a name="a09ee28a45d1942459c88d487448b170d"></a>deleteJob</p>
</td>
</tr>
<tr id="r2e0bba5f23654d67ab2ef043b4103791"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="a9d17a004ef42442581b463fe71341c55"><a name="a9d17a004ef42442581b463fe71341c55"></a><a name="a9d17a004ef42442581b463fe71341c55"></a>Cloning a task</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240370_p562635681171"><a name="en-us_topic_0100240370_p562635681171"></a><a name="en-us_topic_0100240370_p562635681171"></a>job</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="a32f9b0eed08c40f8ab37ca8e2f7babb0"><a name="a32f9b0eed08c40f8ab37ca8e2f7babb0"></a><a name="a32f9b0eed08c40f8ab37ca8e2f7babb0"></a>cloneJob</p>
</td>
</tr>
<tr id="r4828ee7d8d1a4f48b3f231aa689d10ab"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="a55a0d5c494da4369b7b14e947b47305e"><a name="a55a0d5c494da4369b7b14e947b47305e"></a><a name="a55a0d5c494da4369b7b14e947b47305e"></a>Starting a task</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240370_p126252941171"><a name="en-us_topic_0100240370_p126252941171"></a><a name="en-us_topic_0100240370_p126252941171"></a>job</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="acf97ff21106744c287626724903a2646"><a name="acf97ff21106744c287626724903a2646"></a><a name="acf97ff21106744c287626724903a2646"></a>startJob</p>
</td>
</tr>
<tr id="rfce19025f0134daf8e0eba9268c384d6"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240370_p247781611654"><a name="en-us_topic_0100240370_p247781611654"></a><a name="en-us_topic_0100240370_p247781611654"></a>Retrying a task</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240370_p99254831171"><a name="en-us_topic_0100240370_p99254831171"></a><a name="en-us_topic_0100240370_p99254831171"></a>job</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="acc9bb00474da4d759beecaa6b2e018e1"><a name="acc9bb00474da4d759beecaa6b2e018e1"></a><a name="acc9bb00474da4d759beecaa6b2e018e1"></a>retryJob</p>
</td>
</tr>
</tbody>
</table>

