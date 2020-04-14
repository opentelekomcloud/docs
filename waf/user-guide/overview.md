# Overview<a name="EN-US_TOPIC_0193630273"></a>

Before using WAF, you need to  connect your domain name  to it and enable it for protection to take effect.

[Table 1](#table186068221358)  describes the procedure to use WAF.

**Table  1**  Procedure to use WAF

<a name="table186068221358"></a>
<table><thead align="left"><tr id="row760782211359"><th class="cellrowborder" valign="top" width="28.99%" id="mcps1.2.3.1.1"><p id="p560712263512"><a name="p560712263512"></a><a name="p560712263512"></a>Step</p>
</th>
<th class="cellrowborder" valign="top" width="71.00999999999999%" id="mcps1.2.3.1.2"><p id="p196074222353"><a name="p196074222353"></a><a name="p196074222353"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row16607422173517"><td class="cellrowborder" valign="top" width="28.99%" headers="mcps1.2.3.1.1 "><p id="p14746935173916"><a name="p14746935173916"></a><a name="p14746935173916"></a>Creating a domain name</p>
</td>
<td class="cellrowborder" valign="top" width="71.00999999999999%" headers="mcps1.2.3.1.2 "><p id="p6607162211352"><a name="p6607162211352"></a><a name="p6607162211352"></a>Add a website to be protected. For details, see <a href="creating-a-domain-name.md">Creating a Domain Name</a>.</p>
</td>
</tr>
<tr id="row460742212359"><td class="cellrowborder" valign="top" width="28.99%" headers="mcps1.2.3.1.1 "><p id="p260772263514"><a name="p260772263514"></a><a name="p260772263514"></a>Enabling WAF protection</p>
</td>
<td class="cellrowborder" valign="top" width="71.00999999999999%" headers="mcps1.2.3.1.2 "><p id="p6607202215355"><a name="p6607202215355"></a><a name="p6607202215355"></a>Enable WAF protection to protect your web services. For details, see <a href="enabling-waf-protection.md">Enabling WAF Protection</a>.</p>
<div class="note" id="note012284223119"><a name="note012284223119"></a><a name="note012284223119"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul697716015340"></a><a name="ul697716015340"></a><ul id="ul697716015340"><li>The WAF engine is not running on your web server. Therefore, your web server performance is not affected.</li><li>After the domain name is connected to WAF, there will be a latency of tens of milliseconds, but might be raised based on the size of the requested page or number of incoming requests.</li></ul>
</div></div>
</td>
</tr>
<tr id="row1960762215351"><td class="cellrowborder" valign="top" width="28.99%" headers="mcps1.2.3.1.1 "><p id="p19607112220359"><a name="p19607112220359"></a><a name="p19607112220359"></a>Configuring rules</p>
</td>
<td class="cellrowborder" valign="top" width="71.00999999999999%" headers="mcps1.2.3.1.2 "><p id="p12607112215352"><a name="p12607112215352"></a><a name="p12607112215352"></a>In addition to the built-in protection rules, WAF provides a rich set of custom rules. For details, see <a href="rule-configurations.md">Rule Configurations</a>.</p>
</td>
</tr>
<tr id="row16914191884019"><td class="cellrowborder" valign="top" width="28.99%" headers="mcps1.2.3.1.1 "><p id="p209141418104019"><a name="p209141418104019"></a><a name="p209141418104019"></a>Enabling alarm notification</p>
</td>
<td class="cellrowborder" valign="top" width="71.00999999999999%" headers="mcps1.2.3.1.2 "><p id="p1491512181402"><a name="p1491512181402"></a><a name="p1491512181402"></a>Once the function is enabled, users can receive attack logs at the earliest moment. For details, see <a href="enabling-alarm-notification.md">Enabling Alarm Notification</a>.</p>
</td>
</tr>
<tr id="row758655211510"><td class="cellrowborder" valign="top" width="28.99%" headers="mcps1.2.3.1.1 "><p id="p0924629858"><a name="p0924629858"></a><a name="p0924629858"></a>Handling false alarms</p>
</td>
<td class="cellrowborder" valign="top" width="71.00999999999999%" headers="mcps1.2.3.1.2 "><p id="p1955314388418"><a name="p1955314388418"></a><a name="p1955314388418"></a>If the attack events blocked or logged are false positives, mask them. For details, see <a href="handling-false-alarms.md">Handling False Alarms</a>.</p>
</td>
</tr>
<tr id="row1999341519405"><td class="cellrowborder" valign="top" width="28.99%" headers="mcps1.2.3.1.1 "><p id="p299315156400"><a name="p299315156400"></a><a name="p299315156400"></a>Viewing <strong id="b1101678347"><a name="b1101678347"></a><a name="b1101678347"></a>Dashboard</strong></p>
</td>
<td class="cellrowborder" valign="top" width="71.00999999999999%" headers="mcps1.2.3.1.2 "><p id="p1199319156407"><a name="p1199319156407"></a><a name="p1199319156407"></a>View the request and attack statistics, event distribution, and top 5 attack resource IP addresses of yesterday, today, past 3 days, past 7 days, or past 30 days. For details, see <a href="dashboard.md">Dashboard</a>.</p>
</td>
</tr>
</tbody>
</table>

For details about how to connect your domain name to WAF, see  [Figure 1](#en-us_topic_0119807183_fig1251423693315).

**Figure  1**  Flowchart for connecting your domain name to WAF<a name="en-us_topic_0119807183_fig1251423693315"></a>  
![](figures/flowchart-for-connecting-your-domain-name-to-waf.png "flowchart-for-connecting-your-domain-name-to-waf")

