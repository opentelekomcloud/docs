# Service Advantages<a name="smn_pd_23000"></a>

SMN has the following advantages over any traditional messaging systems.

**Table  1**  SMN advantages

<a name="table33619972192228"></a>
<table><thead align="left"><tr id="row43997757192228"><th class="cellrowborder" valign="top" width="20.927907209279073%" id="mcps1.2.4.1.1"><p id="p63437102192228"><a name="p63437102192228"></a><a name="p63437102192228"></a>Item</p>
</th>
<th class="cellrowborder" valign="top" width="41.415858414158585%" id="mcps1.2.4.1.2"><p id="p38131623192228"><a name="p38131623192228"></a><a name="p38131623192228"></a>SMN</p>
</th>
<th class="cellrowborder" valign="top" width="37.656234376562345%" id="mcps1.2.4.1.3"><p id="p1653757192228"><a name="p1653757192228"></a><a name="p1653757192228"></a>Traditional Messaging System</p>
</th>
</tr>
</thead>
<tbody><tr id="row14883814192228"><td class="cellrowborder" valign="top" width="20.927907209279073%" headers="mcps1.2.4.1.1 "><p id="p64738257192228"><a name="p64738257192228"></a><a name="p64738257192228"></a>Simplicity</p>
</td>
<td class="cellrowborder" valign="top" width="41.415858414158585%" headers="mcps1.2.4.1.2 "><p id="p9307469192228"><a name="p9307469192228"></a><a name="p9307469192228"></a>SMN provides three basic APIs to create topics, add subscriptions, and publish messages and can be quickly integrated with your services. It enables you to send messages in substantial quantity and do not require highly skilled development.</p>
</td>
<td class="cellrowborder" valign="top" width="37.656234376562345%" headers="mcps1.2.4.1.3 "><p id="p15707521192228"><a name="p15707521192228"></a><a name="p15707521192228"></a>A self-developed messaging system is expensive and takes long time to be integrated with your services. Its APIs are complicated and hard to use.</p>
</td>
</tr>
<tr id="row7149968192228"><td class="cellrowborder" valign="top" width="20.927907209279073%" headers="mcps1.2.4.1.1 "><p id="p42276556192228"><a name="p42276556192228"></a><a name="p42276556192228"></a>Stability and reliability</p>
</td>
<td class="cellrowborder" valign="top" width="41.415858414158585%" headers="mcps1.2.4.1.2 "><p id="p1849045192228"><a name="p1849045192228"></a><a name="p1849045192228"></a>SMN stores messages in multiple data centers and supports transparent topic migration. Once a message fails to deliver, SMN saves it in a message queue and tries to deliver it again. If one service node is faulty, your requests are automatically processed by another available node.</p>
</td>
<td class="cellrowborder" valign="top" width="37.656234376562345%" headers="mcps1.2.4.1.3 "><p id="p15554962192228"><a name="p15554962192228"></a><a name="p15554962192228"></a>A traditional messaging system cannot achieve the stability and reliability required by critical services and does not provide measures to ensure service continuity.</p>
</td>
</tr>
<tr id="row5776936192228"><td class="cellrowborder" valign="top" width="20.927907209279073%" headers="mcps1.2.4.1.1 "><p id="p65278671192228"><a name="p65278671192228"></a><a name="p65278671192228"></a>Multiple messaging types</p>
</td>
<td class="cellrowborder" valign="top" width="41.415858414158585%" headers="mcps1.2.4.1.2 "><p id="p53080990192228"><a name="p53080990192228"></a><a name="p53080990192228"></a>You publish a message once, and SMN delivers it to endpoints in various message types.</p>
</td>
<td class="cellrowborder" valign="top" width="37.656234376562345%" headers="mcps1.2.4.1.3 "><p id="p4592958192228"><a name="p4592958192228"></a><a name="p4592958192228"></a>You need to develop separate messaging systems in multiple types to send SMS message, email, HTTP, or HTTPS notifications.</p>
</td>
</tr>
<tr id="row41336628192228"><td class="cellrowborder" valign="top" width="20.927907209279073%" headers="mcps1.2.4.1.1 "><p id="p59932560192228"><a name="p59932560192228"></a><a name="p59932560192228"></a>Security</p>
</td>
<td class="cellrowborder" valign="top" width="41.415858414158585%" headers="mcps1.2.4.1.2 "><p id="p22699152192228"><a name="p22699152192228"></a><a name="p22699152192228"></a>SMN isolates data based on topics and does not allow any unauthorized users to access message queues, thereby protecting your service data.</p>
</td>
<td class="cellrowborder" valign="top" width="37.656234376562345%" headers="mcps1.2.4.1.3 "><p id="p26691996192228"><a name="p26691996192228"></a><a name="p26691996192228"></a>Service data is potentially exposed to unauthorized access due to lack of effective protection mechanisms.</p>
</td>
</tr>
</tbody>
</table>

