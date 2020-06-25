# Key Operations Recorded by CTS<a name="smn_ug_0012"></a>

After you enable CTS, whenever an SMN API is called, the operation is recorded in a log file, which is then delivered to a specified OBS bucket for storage.

However, if someone makes an API call to cancel a subscription without login, CTS will not record the operation. For example, if a subscriber clicks the link in an email notification to cancel the subscription, the Unsubscribe API is called, but CTS does not record the operation.

[Table 1](#table2434760155120)  lists the SMN operations that will be recorded by CTS.

**Table  1**  SMN operations recorded by CTS

<a name="table2434760155120"></a>
<table><thead align="left"><tr id="en-us_topic_0100240386_row64314438155120"><th class="cellrowborder" valign="top" width="32.6%" id="mcps1.2.4.1.1"><p id="en-us_topic_0100240386_p42086993155120"><a name="en-us_topic_0100240386_p42086993155120"></a><a name="en-us_topic_0100240386_p42086993155120"></a><strong id="b842352706184229"><a name="b842352706184229"></a><a name="b842352706184229"></a>Operation</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25.69%" id="mcps1.2.4.1.2"><p id="en-us_topic_0100240386_p46895820155120"><a name="en-us_topic_0100240386_p46895820155120"></a><a name="en-us_topic_0100240386_p46895820155120"></a><strong id="b84235270612502"><a name="b84235270612502"></a><a name="b84235270612502"></a>Resource</strong></p>
</th>
<th class="cellrowborder" valign="top" width="41.71%" id="mcps1.2.4.1.3"><p id="en-us_topic_0100240386_p40465036155120"><a name="en-us_topic_0100240386_p40465036155120"></a><a name="en-us_topic_0100240386_p40465036155120"></a>Trace Name</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0100240386_row56442456155120"><td class="cellrowborder" valign="top" width="32.6%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240386_p8436249155120"><a name="en-us_topic_0100240386_p8436249155120"></a><a name="en-us_topic_0100240386_p8436249155120"></a>Creating a topic</p>
</td>
<td class="cellrowborder" valign="top" width="25.69%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240386_p52532121155120"><a name="en-us_topic_0100240386_p52532121155120"></a><a name="en-us_topic_0100240386_p52532121155120"></a>Topic</p>
</td>
<td class="cellrowborder" valign="top" width="41.71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240386_p18974707155935"><a name="en-us_topic_0100240386_p18974707155935"></a><a name="en-us_topic_0100240386_p18974707155935"></a>createTopic</p>
</td>
</tr>
<tr id="en-us_topic_0100240386_row43864299155120"><td class="cellrowborder" valign="top" width="32.6%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240386_p63347368155120"><a name="en-us_topic_0100240386_p63347368155120"></a><a name="en-us_topic_0100240386_p63347368155120"></a>Deleting a topic</p>
</td>
<td class="cellrowborder" valign="top" width="25.69%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240386_p16889066155120"><a name="en-us_topic_0100240386_p16889066155120"></a><a name="en-us_topic_0100240386_p16889066155120"></a>Topic</p>
</td>
<td class="cellrowborder" valign="top" width="41.71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240386_p8136046155935"><a name="en-us_topic_0100240386_p8136046155935"></a><a name="en-us_topic_0100240386_p8136046155935"></a>deleteTopic</p>
</td>
</tr>
<tr id="en-us_topic_0100240386_row31207493155120"><td class="cellrowborder" valign="top" width="32.6%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240386_p44778982155120"><a name="en-us_topic_0100240386_p44778982155120"></a><a name="en-us_topic_0100240386_p44778982155120"></a>Updating a topic</p>
</td>
<td class="cellrowborder" valign="top" width="25.69%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240386_p59408927155120"><a name="en-us_topic_0100240386_p59408927155120"></a><a name="en-us_topic_0100240386_p59408927155120"></a>Topic</p>
</td>
<td class="cellrowborder" valign="top" width="41.71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240386_p25598164155935"><a name="en-us_topic_0100240386_p25598164155935"></a><a name="en-us_topic_0100240386_p25598164155935"></a>updateTopic</p>
</td>
</tr>
<tr id="en-us_topic_0100240386_row23891005155120"><td class="cellrowborder" valign="top" width="32.6%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240386_p56123262155120"><a name="en-us_topic_0100240386_p56123262155120"></a><a name="en-us_topic_0100240386_p56123262155120"></a>Updating attributes of a topic</p>
</td>
<td class="cellrowborder" valign="top" width="25.69%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240386_p65497473155120"><a name="en-us_topic_0100240386_p65497473155120"></a><a name="en-us_topic_0100240386_p65497473155120"></a>Topic</p>
</td>
<td class="cellrowborder" valign="top" width="41.71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240386_p4797422155935"><a name="en-us_topic_0100240386_p4797422155935"></a><a name="en-us_topic_0100240386_p4797422155935"></a>updateTopicAttribute</p>
</td>
</tr>
<tr id="en-us_topic_0100240386_row33256118155120"><td class="cellrowborder" valign="top" width="32.6%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240386_p9391008155120"><a name="en-us_topic_0100240386_p9391008155120"></a><a name="en-us_topic_0100240386_p9391008155120"></a>Deleting all topic attributes</p>
</td>
<td class="cellrowborder" valign="top" width="25.69%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240386_p8468194155120"><a name="en-us_topic_0100240386_p8468194155120"></a><a name="en-us_topic_0100240386_p8468194155120"></a>Topic</p>
</td>
<td class="cellrowborder" valign="top" width="41.71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240386_p7659984155935"><a name="en-us_topic_0100240386_p7659984155935"></a><a name="en-us_topic_0100240386_p7659984155935"></a>deleteTopicAttributes</p>
</td>
</tr>
<tr id="en-us_topic_0100240386_row66406871155120"><td class="cellrowborder" valign="top" width="32.6%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240386_p10247493155120"><a name="en-us_topic_0100240386_p10247493155120"></a><a name="en-us_topic_0100240386_p10247493155120"></a>Deleting a specified topic attribute</p>
</td>
<td class="cellrowborder" valign="top" width="25.69%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240386_p57829849155120"><a name="en-us_topic_0100240386_p57829849155120"></a><a name="en-us_topic_0100240386_p57829849155120"></a>Topic</p>
</td>
<td class="cellrowborder" valign="top" width="41.71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240386_p14093206155935"><a name="en-us_topic_0100240386_p14093206155935"></a><a name="en-us_topic_0100240386_p14093206155935"></a>deleteTopicAttributeByName</p>
</td>
</tr>
<tr id="en-us_topic_0100240386_row13593683155120"><td class="cellrowborder" valign="top" width="32.6%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240386_p27346542155120"><a name="en-us_topic_0100240386_p27346542155120"></a><a name="en-us_topic_0100240386_p27346542155120"></a>Adding a subscription</p>
</td>
<td class="cellrowborder" valign="top" width="25.69%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240386_p38669833155120"><a name="en-us_topic_0100240386_p38669833155120"></a><a name="en-us_topic_0100240386_p38669833155120"></a>Subscription</p>
</td>
<td class="cellrowborder" valign="top" width="41.71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240386_p6291234155935"><a name="en-us_topic_0100240386_p6291234155935"></a><a name="en-us_topic_0100240386_p6291234155935"></a>subscribe</p>
</td>
</tr>
<tr id="en-us_topic_0100240386_row4585378155120"><td class="cellrowborder" valign="top" width="32.6%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240386_p35871332155120"><a name="en-us_topic_0100240386_p35871332155120"></a><a name="en-us_topic_0100240386_p35871332155120"></a>Deleting a subscription</p>
</td>
<td class="cellrowborder" valign="top" width="25.69%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240386_p1025369155120"><a name="en-us_topic_0100240386_p1025369155120"></a><a name="en-us_topic_0100240386_p1025369155120"></a>Subscription</p>
</td>
<td class="cellrowborder" valign="top" width="41.71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240386_p22906846155935"><a name="en-us_topic_0100240386_p22906846155935"></a><a name="en-us_topic_0100240386_p22906846155935"></a>unsubscribe</p>
</td>
</tr>
<tr id="en-us_topic_0100240386_row9296965155120"><td class="cellrowborder" valign="top" width="32.6%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240386_p14856696155120"><a name="en-us_topic_0100240386_p14856696155120"></a><a name="en-us_topic_0100240386_p14856696155120"></a>Creating a message template</p>
</td>
<td class="cellrowborder" valign="top" width="25.69%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240386_p32715836155120"><a name="en-us_topic_0100240386_p32715836155120"></a><a name="en-us_topic_0100240386_p32715836155120"></a>Message template</p>
</td>
<td class="cellrowborder" valign="top" width="41.71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240386_p56093055155935"><a name="en-us_topic_0100240386_p56093055155935"></a><a name="en-us_topic_0100240386_p56093055155935"></a>createMessageTemplate</p>
</td>
</tr>
<tr id="en-us_topic_0100240386_row26198021155120"><td class="cellrowborder" valign="top" width="32.6%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240386_p41664963155120"><a name="en-us_topic_0100240386_p41664963155120"></a><a name="en-us_topic_0100240386_p41664963155120"></a>Creating message templates in batches</p>
</td>
<td class="cellrowborder" valign="top" width="25.69%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240386_p29425642155120"><a name="en-us_topic_0100240386_p29425642155120"></a><a name="en-us_topic_0100240386_p29425642155120"></a>Message template</p>
</td>
<td class="cellrowborder" valign="top" width="41.71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240386_p22539455155935"><a name="en-us_topic_0100240386_p22539455155935"></a><a name="en-us_topic_0100240386_p22539455155935"></a>batchCreateMessageTemplate</p>
</td>
</tr>
<tr id="en-us_topic_0100240386_row43565619155120"><td class="cellrowborder" valign="top" width="32.6%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240386_p39154279155120"><a name="en-us_topic_0100240386_p39154279155120"></a><a name="en-us_topic_0100240386_p39154279155120"></a>Modifying a message template</p>
</td>
<td class="cellrowborder" valign="top" width="25.69%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240386_p65605284155120"><a name="en-us_topic_0100240386_p65605284155120"></a><a name="en-us_topic_0100240386_p65605284155120"></a>Message template</p>
</td>
<td class="cellrowborder" valign="top" width="41.71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240386_p56700449155935"><a name="en-us_topic_0100240386_p56700449155935"></a><a name="en-us_topic_0100240386_p56700449155935"></a>updateMessageTemplate</p>
</td>
</tr>
<tr id="en-us_topic_0100240386_row44741097155120"><td class="cellrowborder" valign="top" width="32.6%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240386_p150220155120"><a name="en-us_topic_0100240386_p150220155120"></a><a name="en-us_topic_0100240386_p150220155120"></a>Deleting a message template</p>
</td>
<td class="cellrowborder" valign="top" width="25.69%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240386_p46070259155120"><a name="en-us_topic_0100240386_p46070259155120"></a><a name="en-us_topic_0100240386_p46070259155120"></a>Message template</p>
</td>
<td class="cellrowborder" valign="top" width="41.71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240386_p62676657155935"><a name="en-us_topic_0100240386_p62676657155935"></a><a name="en-us_topic_0100240386_p62676657155935"></a>deleteMessageTemplate</p>
</td>
</tr>
</tbody>
</table>

