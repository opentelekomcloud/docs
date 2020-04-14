# Protocols and Ports<a name="EN-US_TOPIC_0166390463"></a>

## Frontend Protocols and Ports<a name="section795615356171"></a>

Frontend protocols and ports are used by load balancers to receive requests from clients. Load balancers use TCP, UDP, or SSL at Layer 4, and HTTP or HTTPS at Layer 7. Select a protocol and a port that best suit your needs.

**Table  1**  Frontend protocols and ports

<a name="table16662138185223"></a>
<table><thead align="left"><tr id="row66696918185223"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.3.1.1"><p id="p33741271185223"><a name="p33741271185223"></a><a name="p33741271185223"></a><strong id="b194111818274"><a name="b194111818274"></a><a name="b194111818274"></a>Protocol</strong></p>
</th>
<th class="cellrowborder" valign="top" width="75%" id="mcps1.2.3.1.2"><p id="p578219194238"><a name="p578219194238"></a><a name="p578219194238"></a><strong id="b371215143273"><a name="b371215143273"></a><a name="b371215143273"></a>Port</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row60479457185223"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p66997849185223"><a name="p66997849185223"></a><a name="p66997849185223"></a>TCP</p>
</td>
<td class="cellrowborder" rowspan="5" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="p1467622095114"><a name="p1467622095114"></a><a name="p1467622095114"></a>For one load balancer:</p>
<a name="ul3677162065116"></a><a name="ul3677162065116"></a><ul id="ul3677162065116"><li>The port numbers of different protocols must be unique except UDP. Specifically, the port numbers used by UDP can be the same as those of other protocols. For example, if you have a UDP listener that uses port 88, you can add a TCP, HTTP, or HTTPS listener that also uses port 88. However, if you already have an HTTP listener that uses port 443, you cannot add an HTTPS or TCP listener that also uses the same port.</li><li>The port numbers of the same protocol must be unique. For example, if you have a TCP listener that uses port 80, you cannot add another TCP listener with the same port.</li></ul>
<p id="p568392015110"><a name="p568392015110"></a><a name="p568392015110"></a>The port numbers range from 1 to 65535.</p>
<p id="p188415513232"><a name="p188415513232"></a><a name="p188415513232"></a>The following are some commonly-used protocols and port numbers:</p>
<p id="p1539004613252"><a name="p1539004613252"></a><a name="p1539004613252"></a>TCP/80</p>
<p id="p1772713917262"><a name="p1772713917262"></a><a name="p1772713917262"></a>HTTPS/443</p>
</td>
</tr>
<tr id="row3124943991152"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p1280950091152"><a name="p1280950091152"></a><a name="p1280950091152"></a>UDP</p>
</td>
</tr>
<tr id="row53288272185223"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p21382803185223"><a name="p21382803185223"></a><a name="p21382803185223"></a>HTTP</p>
</td>
</tr>
<tr id="row21290497142014"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p57396749142014"><a name="p57396749142014"></a><a name="p57396749142014"></a>HTTPS</p>
</td>
</tr>
<tr id="row57281241122611"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p67299415263"><a name="p67299415263"></a><a name="p67299415263"></a>SSL (only classic load balancers)</p>
</td>
</tr>
</tbody>
</table>

## Backend Protocols and Ports<a name="section4613345111719"></a>

Backend protocols and ports are used by backend servers to receive requests from load balancers. If backend servers have Internet Information Services \(IIS\) installed, the default backend protocol and port are HTTP and 80.

**Table  2**  Backend protocols and ports

<a name="table67551915287"></a>
<table><thead align="left"><tr id="row37561916289"><th class="cellrowborder" valign="top" width="36.199999999999996%" id="mcps1.2.3.1.1"><p id="p1275619112819"><a name="p1275619112819"></a><a name="p1275619112819"></a><strong id="b826511683014"><a name="b826511683014"></a><a name="b826511683014"></a>Protocol</strong></p>
</th>
<th class="cellrowborder" valign="top" width="63.800000000000004%" id="mcps1.2.3.1.2"><p id="p87561111286"><a name="p87561111286"></a><a name="p87561111286"></a><strong id="b129619103302"><a name="b129619103302"></a><a name="b129619103302"></a>Port</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row167563117285"><td class="cellrowborder" valign="top" width="36.199999999999996%" headers="mcps1.2.3.1.1 "><p id="p77561619285"><a name="p77561619285"></a><a name="p77561619285"></a>TCP</p>
</td>
<td class="cellrowborder" rowspan="3" valign="top" width="63.800000000000004%" headers="mcps1.2.3.1.2 "><p id="p12756717286"><a name="p12756717286"></a><a name="p12756717286"></a>Backend ports of the same load balancer can also be the same. The port numbers range from 1 to 65535.</p>
<p id="p197565112816"><a name="p197565112816"></a><a name="p197565112816"></a>The following are some commonly-used protocols and port numbers:</p>
<p id="p675619192820"><a name="p675619192820"></a><a name="p675619192820"></a>TCP/80</p>
<p id="p7756819284"><a name="p7756819284"></a><a name="p7756819284"></a>HTTP/443</p>
</td>
</tr>
<tr id="row207571213284"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p167572016288"><a name="p167572016288"></a><a name="p167572016288"></a>UDP</p>
</td>
</tr>
<tr id="row157575116281"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p37571419283"><a name="p37571419283"></a><a name="p37571419283"></a>HTTP</p>
</td>
</tr>
</tbody>
</table>

