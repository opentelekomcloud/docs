# Error Code List<a name="obs_03_0013"></a>

If OBS \(compatible with OpenStack Swift\) encounters an error when processing a request, a response containing the error code and error description is returned.  [Table 1](error-code-list.md#table30733758)  describes all error codes in OBS \(compatible with OpenStack Swift\).

**Table  1**  List of error codes in OBS \(compatible with OpenStack Swift\)

<a name="table30733758"></a>
<table><thead align="left"><tr id="row56417443"><th class="cellrowborder" valign="top" width="27.852785278527854%" id="mcps1.2.4.1.1"><p id="p33985582"><a name="p33985582"></a><a name="p33985582"></a>Error Code</p>
</th>
<th class="cellrowborder" valign="top" width="45.904590459045906%" id="mcps1.2.4.1.2"><p id="p33314938"><a name="p33314938"></a><a name="p33314938"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="26.242624262426244%" id="mcps1.2.4.1.3"><p id="p41181705"><a name="p41181705"></a><a name="p41181705"></a>HTTP Status Code</p>
</th>
</tr>
</thead>
<tbody><tr id="row4947497295325"><td class="cellrowborder" valign="top" width="27.852785278527854%" headers="mcps1.2.4.1.1 "><p id="p5371389395339"><a name="p5371389395339"></a><a name="p5371389395339"></a>Moved Permanently</p>
</td>
<td class="cellrowborder" valign="top" width="45.904590459045906%" headers="mcps1.2.4.1.2 "><p id="p5585811195339"><a name="p5585811195339"></a><a name="p5585811195339"></a>The requested resource must be addressed using a specified node. Send all future requests to the node.</p>
</td>
<td class="cellrowborder" valign="top" width="26.242624262426244%" headers="mcps1.2.4.1.3 "><p id="p2821317095339"><a name="p2821317095339"></a><a name="p2821317095339"></a>301 Moved Permanently</p>
</td>
</tr>
<tr id="row2578060295520"><td class="cellrowborder" valign="top" width="27.852785278527854%" headers="mcps1.2.4.1.1 "><p id="p785402295520"><a name="p785402295520"></a><a name="p785402295520"></a>Not Modified</p>
</td>
<td class="cellrowborder" valign="top" width="45.904590459045906%" headers="mcps1.2.4.1.2 "><p id="p326046869577"><a name="p326046869577"></a><a name="p326046869577"></a>The requested resource is not changed (since the last access or based on the conditions specified in the request).</p>
</td>
<td class="cellrowborder" valign="top" width="26.242624262426244%" headers="mcps1.2.4.1.3 "><p id="p5774263995520"><a name="p5774263995520"></a><a name="p5774263995520"></a>304 Not Modified</p>
</td>
</tr>
<tr id="row6566625616251"><td class="cellrowborder" valign="top" width="27.852785278527854%" headers="mcps1.2.4.1.1 "><p id="p1736655116251"><a name="p1736655116251"></a><a name="p1736655116251"></a>Bad Request</p>
</td>
<td class="cellrowborder" valign="top" width="45.904590459045906%" headers="mcps1.2.4.1.2 "><p id="p6451335316251"><a name="p6451335316251"></a><a name="p6451335316251"></a>The syntax of a request is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="26.242624262426244%" headers="mcps1.2.4.1.3 "><p id="p5819912016251"><a name="p5819912016251"></a><a name="p5819912016251"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row5079978216247"><td class="cellrowborder" valign="top" width="27.852785278527854%" headers="mcps1.2.4.1.1 "><p id="p2114171616247"><a name="p2114171616247"></a><a name="p2114171616247"></a>Unauthorized</p>
</td>
<td class="cellrowborder" valign="top" width="45.904590459045906%" headers="mcps1.2.4.1.2 "><p id="p3475744616247"><a name="p3475744616247"></a><a name="p3475744616247"></a>Unauthorized. The authentication failed or the token is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="26.242624262426244%" headers="mcps1.2.4.1.3 "><p id="p6388976516247"><a name="p6388976516247"></a><a name="p6388976516247"></a>401Unauthorized</p>
</td>
</tr>
<tr id="row129792029490"><td class="cellrowborder" valign="top" width="27.852785278527854%" headers="mcps1.2.4.1.1 "><p id="p329382789498"><a name="p329382789498"></a><a name="p329382789498"></a>Forbidden</p>
</td>
<td class="cellrowborder" valign="top" width="45.904590459045906%" headers="mcps1.2.4.1.2 "><p id="p507548299498"><a name="p507548299498"></a><a name="p507548299498"></a>The access was denied.</p>
</td>
<td class="cellrowborder" valign="top" width="26.242624262426244%" headers="mcps1.2.4.1.3 "><p id="p175005059498"><a name="p175005059498"></a><a name="p175005059498"></a>403 Forbidden</p>
</td>
</tr>
<tr id="row41964036101550"><td class="cellrowborder" valign="top" width="27.852785278527854%" headers="mcps1.2.4.1.1 "><p id="p43643764101550"><a name="p43643764101550"></a><a name="p43643764101550"></a>Not Found</p>
</td>
<td class="cellrowborder" valign="top" width="45.904590459045906%" headers="mcps1.2.4.1.2 "><p id="p45483976101550"><a name="p45483976101550"></a><a name="p45483976101550"></a>The requested resource does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="26.242624262426244%" headers="mcps1.2.4.1.3 "><p id="p60323433101550"><a name="p60323433101550"></a><a name="p60323433101550"></a>404 Not Found</p>
</td>
</tr>
<tr id="row6242678394912"><td class="cellrowborder" valign="top" width="27.852785278527854%" headers="mcps1.2.4.1.1 "><p id="p915417594926"><a name="p915417594926"></a><a name="p915417594926"></a>Method Not Allowed</p>
</td>
<td class="cellrowborder" valign="top" width="45.904590459045906%" headers="mcps1.2.4.1.2 "><p id="p329069194926"><a name="p329069194926"></a><a name="p329069194926"></a>The specified method is not allowed on the requested resource.</p>
</td>
<td class="cellrowborder" valign="top" width="26.242624262426244%" headers="mcps1.2.4.1.3 "><p id="p6521941294926"><a name="p6521941294926"></a><a name="p6521941294926"></a>405 Method Not Allowed</p>
</td>
</tr>
<tr id="row629030216328"><td class="cellrowborder" valign="top" width="27.852785278527854%" headers="mcps1.2.4.1.1 "><p id="p3975244516328"><a name="p3975244516328"></a><a name="p3975244516328"></a>Not Acceptable</p>
</td>
<td class="cellrowborder" valign="top" width="45.904590459045906%" headers="mcps1.2.4.1.2 "><p id="p6583150116328"><a name="p6583150116328"></a><a name="p6583150116328"></a>Not acceptable. The request may contain invalid parameters or headers.</p>
</td>
<td class="cellrowborder" valign="top" width="26.242624262426244%" headers="mcps1.2.4.1.3 "><p id="p3075138216328"><a name="p3075138216328"></a><a name="p3075138216328"></a>406 Not Acceptable</p>
</td>
</tr>
<tr id="row5812035916332"><td class="cellrowborder" valign="top" width="27.852785278527854%" headers="mcps1.2.4.1.1 "><p id="p1012863516332"><a name="p1012863516332"></a><a name="p1012863516332"></a>Conflict</p>
</td>
<td class="cellrowborder" valign="top" width="45.904590459045906%" headers="mcps1.2.4.1.2 "><p id="p1511313616332"><a name="p1511313616332"></a><a name="p1511313616332"></a>This operation caused a conflict. For example, a non-empty container is deleted.</p>
</td>
<td class="cellrowborder" valign="top" width="26.242624262426244%" headers="mcps1.2.4.1.3 "><p id="p1620452616332"><a name="p1620452616332"></a><a name="p1620452616332"></a>409 Conflict</p>
</td>
</tr>
<tr id="row18155865"><td class="cellrowborder" valign="top" width="27.852785278527854%" headers="mcps1.2.4.1.1 "><p id="p191517979501"><a name="p191517979501"></a><a name="p191517979501"></a>Missing Content Length</p>
</td>
<td class="cellrowborder" valign="top" width="45.904590459045906%" headers="mcps1.2.4.1.2 "><p id="p77917539501"><a name="p77917539501"></a><a name="p77917539501"></a>HTTP headers must contain the <strong id="b29365919"><a name="b29365919"></a><a name="b29365919"></a>Content-Length</strong> field.</p>
</td>
<td class="cellrowborder" valign="top" width="26.242624262426244%" headers="mcps1.2.4.1.3 "><p id="p271522579501"><a name="p271522579501"></a><a name="p271522579501"></a>411 Length Required</p>
</td>
</tr>
<tr id="row4485256995019"><td class="cellrowborder" valign="top" width="27.852785278527854%" headers="mcps1.2.4.1.1 "><p id="p1757512495024"><a name="p1757512495024"></a><a name="p1757512495024"></a>Precondition Failed</p>
</td>
<td class="cellrowborder" valign="top" width="45.904590459045906%" headers="mcps1.2.4.1.2 "><p id="p1429891595024"><a name="p1429891595024"></a><a name="p1429891595024"></a>At least one specified precondition is not met.</p>
</td>
<td class="cellrowborder" valign="top" width="26.242624262426244%" headers="mcps1.2.4.1.3 "><p id="p1736145595024"><a name="p1736145595024"></a><a name="p1736145595024"></a>412 Precondition Failed</p>
</td>
</tr>
<tr id="row3253737095128"><td class="cellrowborder" valign="top" width="27.852785278527854%" headers="mcps1.2.4.1.1 "><p id="p1828133995128"><a name="p1828133995128"></a><a name="p1828133995128"></a>Request Entity Too Large</p>
</td>
<td class="cellrowborder" valign="top" width="45.904590459045906%" headers="mcps1.2.4.1.2 "><p id="p439352995128"><a name="p439352995128"></a><a name="p439352995128"></a>The size of the uploaded data has exceeded the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="26.242624262426244%" headers="mcps1.2.4.1.3 "><p id="p2033157995128"><a name="p2033157995128"></a><a name="p2033157995128"></a>413 Request Entity Too Large</p>
</td>
</tr>
<tr id="row10805699"><td class="cellrowborder" valign="top" width="27.852785278527854%" headers="mcps1.2.4.1.1 "><p id="p182616094948"><a name="p182616094948"></a><a name="p182616094948"></a>Invalid Range</p>
</td>
<td class="cellrowborder" valign="top" width="45.904590459045906%" headers="mcps1.2.4.1.2 "><p id="p1370124994948"><a name="p1370124994948"></a><a name="p1370124994948"></a>The requested range cannot be obtained.</p>
</td>
<td class="cellrowborder" valign="top" width="26.242624262426244%" headers="mcps1.2.4.1.3 "><p id="p3605941694948"><a name="p3605941694948"></a><a name="p3605941694948"></a>416 Client Requested Range Not Satisfiable</p>
</td>
</tr>
<tr id="row65677253"><td class="cellrowborder" valign="top" width="27.852785278527854%" headers="mcps1.2.4.1.1 "><p id="p5868878094718"><a name="p5868878094718"></a><a name="p5868878094718"></a>Unprocessable Entity</p>
</td>
<td class="cellrowborder" valign="top" width="45.904590459045906%" headers="mcps1.2.4.1.2 "><p id="p3211839494718"><a name="p3211839494718"></a><a name="p3211839494718"></a>The request format is correct but contains incorrect syntax. Therefore, it is unprocessable.</p>
</td>
<td class="cellrowborder" valign="top" width="26.242624262426244%" headers="mcps1.2.4.1.3 "><p id="p5545739194718"><a name="p5545739194718"></a><a name="p5545739194718"></a>422 Unprocessable Entity</p>
</td>
</tr>
<tr id="row35621584"><td class="cellrowborder" valign="top" width="27.852785278527854%" headers="mcps1.2.4.1.1 "><p id="p3719588595921"><a name="p3719588595921"></a><a name="p3719588595921"></a>Internal Error</p>
</td>
<td class="cellrowborder" valign="top" width="45.904590459045906%" headers="mcps1.2.4.1.2 "><p id="p6007671795921"><a name="p6007671795921"></a><a name="p6007671795921"></a>Internal error. Please retry.</p>
</td>
<td class="cellrowborder" valign="top" width="26.242624262426244%" headers="mcps1.2.4.1.3 "><p id="p3437588995921"><a name="p3437588995921"></a><a name="p3437588995921"></a>500 Internal Server Error</p>
</td>
</tr>
<tr id="row43121747"><td class="cellrowborder" valign="top" width="27.852785278527854%" headers="mcps1.2.4.1.1 "><p id="p2841710695921"><a name="p2841710695921"></a><a name="p2841710695921"></a>Service Unavailable</p>
</td>
<td class="cellrowborder" valign="top" width="45.904590459045906%" headers="mcps1.2.4.1.2 "><p id="p2008425695921"><a name="p2008425695921"></a><a name="p2008425695921"></a>The service is unavailable.</p>
</td>
<td class="cellrowborder" valign="top" width="26.242624262426244%" headers="mcps1.2.4.1.3 "><p id="p1621207995921"><a name="p1621207995921"></a><a name="p1621207995921"></a>503 Service Unavailable</p>
</td>
</tr>
</tbody>
</table>

