# Overview<a name="EN-US_TOPIC_0166390462"></a>

At least one listener must be added to a load balancer. A listener receives requests from clients and routes requests to backend servers using the protocol, port, and load balancing algorithm you select.

## Supported Protocols<a name="section189395119572"></a>

ELB provides load balancing at both Layer 4 and Layer 7. Select a protocol that meets your needs in a specific scenario.

**Table  1**  Protocols supported by ELB

<a name="table66244785114429"></a>
<table><thead align="left"><tr id="row36701900114429"><th class="cellrowborder" colspan="2" valign="top" id="mcps1.2.5.1.1"><p id="p4473966141520"><a name="p4473966141520"></a><a name="p4473966141520"></a><strong id="b842352706102621"><a name="b842352706102621"></a><a name="b842352706102621"></a>Protocol</strong></p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.5.1.2"><p id="p60499166141520"><a name="p60499166141520"></a><a name="p60499166141520"></a><strong id="b1253116427617"><a name="b1253116427617"></a><a name="b1253116427617"></a>Description</strong></p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.5.1.3"><p id="p18652969141520"><a name="p18652969141520"></a><a name="p18652969141520"></a><strong id="b84235270616379"><a name="b84235270616379"></a><a name="b84235270616379"></a>Application Scenario</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row52657811114429"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="p8541510141438"><a name="p8541510141438"></a><a name="p8541510141438"></a>Layer 4</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.1 "><p id="p20330484141012"><a name="p20330484141012"></a><a name="p20330484141012"></a>TCP</p>
</td>
<td class="cellrowborder" valign="top" width="39%" headers="mcps1.2.5.1.2 "><a name="ul39716962141048"></a><a name="ul39716962141048"></a><ul id="ul39716962141048"><li>Source IP address-based sticky sessions</li><li>Fast data transfer</li></ul>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.5.1.3 "><a name="ul2315607141239"></a><a name="ul2315607141239"></a><ul id="ul2315607141239"><li>Scenarios that require high reliability and data accuracy, such as file transfer, email sending and receiving, and remote login</li><li>Web applications with a number of concurrent connections or requiring high performance</li></ul>
</td>
</tr>
<tr id="row10959143516391"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="p9959153583918"><a name="p9959153583918"></a><a name="p9959153583918"></a>Layer 4</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.1 "><p id="p5270937101819"><a name="p5270937101819"></a><a name="p5270937101819"></a>UDP</p>
</td>
<td class="cellrowborder" valign="top" width="39%" headers="mcps1.2.5.1.2 "><a name="ul9365451918"></a><a name="ul9365451918"></a><ul id="ul9365451918"><li>Low reliability</li><li>Fast data transfer</li></ul>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.5.1.3 "><p id="p154747282312"><a name="p154747282312"></a><a name="p154747282312"></a>Scenarios that focus more on timeliness than on reliability, such as video chats, games, and real-time financial quotations</p>
</td>
</tr>
<tr id="row0310182312312"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="p1031015238313"><a name="p1031015238313"></a><a name="p1031015238313"></a>Layer 4</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.1 "><p id="p9310132318310"><a name="p9310132318310"></a><a name="p9310132318310"></a>SSL</p>
</td>
<td class="cellrowborder" valign="top" width="39%" headers="mcps1.2.5.1.2 "><a name="ul19369121019249"></a><a name="ul19369121019249"></a><ul id="ul19369121019249"><li>TCP-based security encryption</li><li>High reliability</li><li>Supported by only classic load balancers</li></ul>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.5.1.3 "><p id="p1231015231431"><a name="p1231015231431"></a><a name="p1231015231431"></a>Applications that require encrypted transmission</p>
</td>
</tr>
<tr id="row10296890141711"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="p55450303141740"><a name="p55450303141740"></a><a name="p55450303141740"></a>Layer 7</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.1 "><p id="p3481406314187"><a name="p3481406314187"></a><a name="p3481406314187"></a>HTTP</p>
</td>
<td class="cellrowborder" valign="top" width="39%" headers="mcps1.2.5.1.2 "><a name="ul21894483141932"></a><a name="ul21894483141932"></a><ul id="ul21894483141932"><li>Cookie-based sticky sessions</li><li>X-Forward-For request header</li></ul>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.5.1.3 "><p id="p55802598141819"><a name="p55802598141819"></a><a name="p55802598141819"></a>Applications where data content needs to be identified, such as web applications and mobile games</p>
</td>
</tr>
<tr id="row25590944144339"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="p28991905144339"><a name="p28991905144339"></a><a name="p28991905144339"></a>Layer 7</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.1 "><p id="p11410140144345"><a name="p11410140144345"></a><a name="p11410140144345"></a>HTTPS</p>
</td>
<td class="cellrowborder" valign="top" width="39%" headers="mcps1.2.5.1.2 "><a name="ul51806117144345"></a><a name="ul51806117144345"></a><ul id="ul51806117144345"><li>An extension of HTTP for encrypted data transmission to prevent unauthorized access</li><li>Encryption and decryption performed on load balancers to reduce the workload of backend servers.</li><li>A broad suite of encryption protocols and cipher suites (which are only provided for classic load balancers)</li></ul>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.5.1.3 "><p id="p8947194144345"><a name="p8947194144345"></a><a name="p8947194144345"></a>Applications that require encrypted transmission</p>
</td>
</tr>
</tbody>
</table>

