# Lifecycle<a name="EN-US_TOPIC_0140735213"></a>

The lifecycle of a BMS contains all the statuses from its creation to deletion. This section describes each state and the conversion between states.

**Figure  1**  BMS statuses<a name="fig1550378185310"></a>  
![](figures/bms-statuses.png "bms-statuses")

**Table  1**  Descriptions of BMS statuses

<a name="table23129774195029"></a>
<table><thead align="left"><tr id="row31891630195029"><th class="cellrowborder" valign="top" width="13.96%" id="mcps1.2.5.1.1"><p id="p33085243195029"><a name="p33085243195029"></a><a name="p33085243195029"></a>Status</p>
</th>
<th class="cellrowborder" valign="top" width="15.190000000000001%" id="mcps1.2.5.1.2"><p id="p62659045195029"><a name="p62659045195029"></a><a name="p62659045195029"></a>Attribute</p>
</th>
<th class="cellrowborder" valign="top" width="49.99%" id="mcps1.2.5.1.3"><p id="p42217875195029"><a name="p42217875195029"></a><a name="p42217875195029"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="20.86%" id="mcps1.2.5.1.4"><p id="p7964122017267"><a name="p7964122017267"></a><a name="p7964122017267"></a>API Status</p>
</th>
</tr>
</thead>
<tbody><tr id="row64204718195029"><td class="cellrowborder" valign="top" width="13.96%" headers="mcps1.2.5.1.1 "><p id="p6022155818450"><a name="p6022155818450"></a><a name="p6022155818450"></a>Creating</p>
</td>
<td class="cellrowborder" valign="top" width="15.190000000000001%" headers="mcps1.2.5.1.2 "><p id="p4816713195029"><a name="p4816713195029"></a><a name="p4816713195029"></a>Intermediate state</p>
</td>
<td class="cellrowborder" valign="top" width="49.99%" headers="mcps1.2.5.1.3 "><p id="p11928492203457"><a name="p11928492203457"></a><a name="p11928492203457"></a>A BMS is in this state after you apply for the BMS and before the BMS enters the running state.</p>
<p id="p54609433195029"><a name="p54609433195029"></a><a name="p54609433195029"></a>If the BMS keeps in this state for a long period of time, exceptions occur. Contact the administrator to handle the exceptions.</p>
</td>
<td class="cellrowborder" valign="top" width="20.86%" headers="mcps1.2.5.1.4 "><p id="p69641020192610"><a name="p69641020192610"></a><a name="p69641020192610"></a>BUILD/BUILDING</p>
</td>
</tr>
<tr id="row47440894105334"><td class="cellrowborder" valign="top" width="13.96%" headers="mcps1.2.5.1.1 "><p id="p4544589218523"><a name="p4544589218523"></a><a name="p4544589218523"></a>Starting</p>
</td>
<td class="cellrowborder" valign="top" width="15.190000000000001%" headers="mcps1.2.5.1.2 "><p id="p63907192105357"><a name="p63907192105357"></a><a name="p63907192105357"></a>Intermediate state</p>
</td>
<td class="cellrowborder" valign="top" width="49.99%" headers="mcps1.2.5.1.3 "><p id="p9100060105357"><a name="p9100060105357"></a><a name="p9100060105357"></a>A BMS is in this state when the BMS is in an intermediate state between <strong id="b799819279486"><a name="b799819279486"></a><a name="b799819279486"></a>Stopped</strong> and <strong id="b20172811484"><a name="b20172811484"></a><a name="b20172811484"></a>Running</strong>.</p>
<p id="p14791683105357"><a name="p14791683105357"></a><a name="p14791683105357"></a>If the BMS keeps in this state for a long period of time, exceptions occur. Contact the administrator to handle the exceptions.</p>
</td>
<td class="cellrowborder" valign="top" width="20.86%" headers="mcps1.2.5.1.4 "><p id="p696482072617"><a name="p696482072617"></a><a name="p696482072617"></a>SHUTOFF</p>
</td>
</tr>
<tr id="row32093542195029"><td class="cellrowborder" valign="top" width="13.96%" headers="mcps1.2.5.1.1 "><p id="p210136741863"><a name="p210136741863"></a><a name="p210136741863"></a>Running</p>
</td>
<td class="cellrowborder" valign="top" width="15.190000000000001%" headers="mcps1.2.5.1.2 "><p id="p45227832195029"><a name="p45227832195029"></a><a name="p45227832195029"></a>Stable state</p>
</td>
<td class="cellrowborder" valign="top" width="49.99%" headers="mcps1.2.5.1.3 "><p id="p57478049203527"><a name="p57478049203527"></a><a name="p57478049203527"></a>A BMS is in this state when the BMS is running properly.</p>
<p id="p39575784195029"><a name="p39575784195029"></a><a name="p39575784195029"></a>A BMS in this state can provide services for you.</p>
</td>
<td class="cellrowborder" valign="top" width="20.86%" headers="mcps1.2.5.1.4 "><p id="p8964182042613"><a name="p8964182042613"></a><a name="p8964182042613"></a>ACTIVE</p>
</td>
</tr>
<tr id="row21015765105421"><td class="cellrowborder" valign="top" width="13.96%" headers="mcps1.2.5.1.1 "><p id="p163037118639"><a name="p163037118639"></a><a name="p163037118639"></a>Stopping</p>
</td>
<td class="cellrowborder" valign="top" width="15.190000000000001%" headers="mcps1.2.5.1.2 "><p id="p37779111105435"><a name="p37779111105435"></a><a name="p37779111105435"></a>Intermediate state</p>
</td>
<td class="cellrowborder" valign="top" width="49.99%" headers="mcps1.2.5.1.3 "><p id="p40209165105435"><a name="p40209165105435"></a><a name="p40209165105435"></a>A BMS is in this state when the BMS is in an intermediate state between <strong id="b1922962135612"><a name="b1922962135612"></a><a name="b1922962135612"></a>Running</strong> and <strong id="b1423072115568"><a name="b1423072115568"></a><a name="b1423072115568"></a>Stopped</strong>.</p>
<p id="p26338170105435"><a name="p26338170105435"></a><a name="p26338170105435"></a>If the BMS keeps in this state for a long period of time, exceptions occur. Contact the administrator to handle the exceptions.</p>
</td>
<td class="cellrowborder" valign="top" width="20.86%" headers="mcps1.2.5.1.4 "><p id="p59641920102610"><a name="p59641920102610"></a><a name="p59641920102610"></a>ACTIVE</p>
</td>
</tr>
<tr id="row20637738195029"><td class="cellrowborder" valign="top" width="13.96%" headers="mcps1.2.5.1.1 "><p id="p6225753318751"><a name="p6225753318751"></a><a name="p6225753318751"></a>Stopped</p>
</td>
<td class="cellrowborder" valign="top" width="15.190000000000001%" headers="mcps1.2.5.1.2 "><p id="p45622085195029"><a name="p45622085195029"></a><a name="p45622085195029"></a>Stable state</p>
</td>
<td class="cellrowborder" valign="top" width="49.99%" headers="mcps1.2.5.1.3 "><p id="p19889388203530"><a name="p19889388203530"></a><a name="p19889388203530"></a>A BMS is in this state after the BMS is correctly stopped.</p>
<p id="p4401411195029"><a name="p4401411195029"></a><a name="p4401411195029"></a>A BMS in this state cannot provide services.</p>
</td>
<td class="cellrowborder" valign="top" width="20.86%" headers="mcps1.2.5.1.4 "><p id="p996402014263"><a name="p996402014263"></a><a name="p996402014263"></a>SHUTOFF</p>
</td>
</tr>
<tr id="row39612707195029"><td class="cellrowborder" valign="top" width="13.96%" headers="mcps1.2.5.1.1 "><p id="p5390378518812"><a name="p5390378518812"></a><a name="p5390378518812"></a>Restarting</p>
</td>
<td class="cellrowborder" valign="top" width="15.190000000000001%" headers="mcps1.2.5.1.2 "><p id="p53454972195029"><a name="p53454972195029"></a><a name="p53454972195029"></a>Intermediate state</p>
</td>
<td class="cellrowborder" valign="top" width="49.99%" headers="mcps1.2.5.1.3 "><p id="p52330452203536"><a name="p52330452203536"></a><a name="p52330452203536"></a>A BMS is in this state when the BMS is being restarted.</p>
<p id="p34885491195029"><a name="p34885491195029"></a><a name="p34885491195029"></a>If the BMS keeps in this state for a long period of time, exceptions occur. Contact the administrator to handle the exceptions.</p>
</td>
<td class="cellrowborder" valign="top" width="20.86%" headers="mcps1.2.5.1.4 "><p id="p2096419208264"><a name="p2096419208264"></a><a name="p2096419208264"></a>REBOOT</p>
</td>
</tr>
<tr id="row1487187144415"><td class="cellrowborder" valign="top" width="13.96%" headers="mcps1.2.5.1.1 "><p id="p148714784418"><a name="p148714784418"></a><a name="p148714784418"></a>Forcibly restarting</p>
</td>
<td class="cellrowborder" valign="top" width="15.190000000000001%" headers="mcps1.2.5.1.2 "><p id="p144877712444"><a name="p144877712444"></a><a name="p144877712444"></a>Intermediate state</p>
</td>
<td class="cellrowborder" valign="top" width="49.99%" headers="mcps1.2.5.1.3 "><p id="p1748711774416"><a name="p1748711774416"></a><a name="p1748711774416"></a>A BMS is in this state when the BMS is being forcibly restarted.</p>
</td>
<td class="cellrowborder" valign="top" width="20.86%" headers="mcps1.2.5.1.4 "><p id="p1448747144417"><a name="p1448747144417"></a><a name="p1448747144417"></a>HARD_REBOOT</p>
</td>
</tr>
<tr id="row39752192105447"><td class="cellrowborder" valign="top" width="13.96%" headers="mcps1.2.5.1.1 "><p id="p6527987918853"><a name="p6527987918853"></a><a name="p6527987918853"></a>Deleting</p>
</td>
<td class="cellrowborder" valign="top" width="15.190000000000001%" headers="mcps1.2.5.1.2 "><p id="p2205719010551"><a name="p2205719010551"></a><a name="p2205719010551"></a>Intermediate state</p>
</td>
<td class="cellrowborder" valign="top" width="49.99%" headers="mcps1.2.5.1.3 "><p id="p4180197510551"><a name="p4180197510551"></a><a name="p4180197510551"></a>A BMS is in this state when the BMS is being deleted.</p>
<p id="p4067345910551"><a name="p4067345910551"></a><a name="p4067345910551"></a>If the BMS keeps in this state for a long period of time, exceptions occur. Contact the administrator to handle the exceptions.</p>
</td>
<td class="cellrowborder" valign="top" width="20.86%" headers="mcps1.2.5.1.4 "><p id="p19641820142613"><a name="p19641820142613"></a><a name="p19641820142613"></a>ACTIVE/SHUTOFF/REBOOT/HARD_REBOOT/ERROR</p>
</td>
</tr>
<tr id="row29232435195029"><td class="cellrowborder" valign="top" width="13.96%" headers="mcps1.2.5.1.1 "><p id="p1832878318926"><a name="p1832878318926"></a><a name="p1832878318926"></a>Deleted</p>
</td>
<td class="cellrowborder" valign="top" width="15.190000000000001%" headers="mcps1.2.5.1.2 "><p id="p63984572195029"><a name="p63984572195029"></a><a name="p63984572195029"></a>Intermediate state</p>
</td>
<td class="cellrowborder" valign="top" width="49.99%" headers="mcps1.2.5.1.3 "><p id="p15367866195029"><a name="p15367866195029"></a><a name="p15367866195029"></a>A BMS is in this state after the BMS is correctly deleted. A BMS in this state cannot provide services and will be removed from the system in a short time.</p>
</td>
<td class="cellrowborder" valign="top" width="20.86%" headers="mcps1.2.5.1.4 "><p id="p109757752215"><a name="p109757752215"></a><a name="p109757752215"></a>DELETED</p>
</td>
</tr>
<tr id="row4093067195029"><td class="cellrowborder" valign="top" width="13.96%" headers="mcps1.2.5.1.1 "><p id="p6516233618950"><a name="p6516233618950"></a><a name="p6516233618950"></a>Faulty</p>
</td>
<td class="cellrowborder" valign="top" width="15.190000000000001%" headers="mcps1.2.5.1.2 "><p id="p11070690195029"><a name="p11070690195029"></a><a name="p11070690195029"></a>Stable state</p>
</td>
<td class="cellrowborder" valign="top" width="49.99%" headers="mcps1.2.5.1.3 "><p id="p52961886203752"><a name="p52961886203752"></a><a name="p52961886203752"></a>A BMS is in this state when an exception occurs on the BMS.</p>
<p id="p24310688195029"><a name="p24310688195029"></a><a name="p24310688195029"></a>A BMS in this state cannot provide services. Contact the administrator to rectify the fault.</p>
</td>
<td class="cellrowborder" valign="top" width="20.86%" headers="mcps1.2.5.1.4 "><p id="p166225892215"><a name="p166225892215"></a><a name="p166225892215"></a>ERROR</p>
</td>
</tr>
<tr id="row0593154818386"><td class="cellrowborder" valign="top" width="13.96%" headers="mcps1.2.5.1.1 "><p id="p195941348143818"><a name="p195941348143818"></a><a name="p195941348143818"></a>Rebuilding</p>
</td>
<td class="cellrowborder" valign="top" width="15.190000000000001%" headers="mcps1.2.5.1.2 "><p id="p19594948113810"><a name="p19594948113810"></a><a name="p19594948113810"></a>Intermediate state</p>
</td>
<td class="cellrowborder" valign="top" width="49.99%" headers="mcps1.2.5.1.3 "><p id="p7594348183817"><a name="p7594348183817"></a><a name="p7594348183817"></a>A BMS is in this state when it is being rebuilt.</p>
</td>
<td class="cellrowborder" valign="top" width="20.86%" headers="mcps1.2.5.1.4 "><p id="p16594848133819"><a name="p16594848133819"></a><a name="p16594848133819"></a>SHUTOFF</p>
</td>
</tr>
</tbody>
</table>

