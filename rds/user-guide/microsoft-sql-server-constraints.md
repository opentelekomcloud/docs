# Microsoft SQL Server Constraints<a name="rds_03_0003"></a>

RDS for Microsoft  SQL Server  only supports DB instances under the License Included model and does not support "bring your own license" \(BYOL\). After a DB instance is created, it contains the Microsoft SQL Server software license.

[Table 1](#table459454418106)  shows the constraints designed to ensure the stability and security of RDS for Microsoft SQL Server.

Microsoft SQL Server DB instances are classified into two types: single and primary/standby. DB instances of different series have different function constraints. For details, see  [Function Comparison](function-comparison.md).

**Table  1**  Function constraints

<a name="table459454418106"></a>
<table><thead align="left"><tr id="row4049162018106"><th class="cellrowborder" valign="top" width="37.3%" id="mcps1.2.4.1.1"><p id="p5859577718106"><a name="p5859577718106"></a><a name="p5859577718106"></a><strong id="b156942317347"><a name="b156942317347"></a><a name="b156942317347"></a>Function Item</strong></p>
</th>
<th class="cellrowborder" valign="top" width="32.26%" id="mcps1.2.4.1.2"><p id="p3508412418106"><a name="p3508412418106"></a><a name="p3508412418106"></a><strong id="b940101324515"><a name="b940101324515"></a><a name="b940101324515"></a>Primary/Standby</strong></p>
</th>
<th class="cellrowborder" valign="top" width="30.44%" id="mcps1.2.4.1.3"><p id="p784925818106"><a name="p784925818106"></a><a name="p784925818106"></a><strong id="b6894191610456"><a name="b6894191610456"></a><a name="b6894191610456"></a>Single</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row2566425218106"><td class="cellrowborder" valign="top" width="37.3%" headers="mcps1.2.4.1.1 "><p id="p6553851418106"><a name="p6553851418106"></a><a name="p6553851418106"></a>Maximum number of databases</p>
</td>
<td class="cellrowborder" valign="top" width="32.26%" headers="mcps1.2.4.1.2 "><p id="p701945418106"><a name="p701945418106"></a><a name="p701945418106"></a>100 (can be increased)</p>
</td>
<td class="cellrowborder" valign="top" width="30.44%" headers="mcps1.2.4.1.3 "><p id="p1795761718106"><a name="p1795761718106"></a><a name="p1795761718106"></a>100 (can be increased)</p>
</td>
</tr>
<tr id="row487497518106"><td class="cellrowborder" valign="top" width="37.3%" headers="mcps1.2.4.1.1 "><p id="p5932866118106"><a name="p5932866118106"></a><a name="p5932866118106"></a>Number of database accounts</p>
</td>
<td class="cellrowborder" valign="top" width="32.26%" headers="mcps1.2.4.1.2 "><p id="p4089223618106"><a name="p4089223618106"></a><a name="p4089223618106"></a>Unlimited</p>
</td>
<td class="cellrowborder" valign="top" width="30.44%" headers="mcps1.2.4.1.3 "><p id="p2393681118106"><a name="p2393681118106"></a><a name="p2393681118106"></a>Unlimited</p>
</td>
</tr>
<tr id="row1410471418106"><td class="cellrowborder" valign="top" width="37.3%" headers="mcps1.2.4.1.1 "><p id="p163116118106"><a name="p163116118106"></a><a name="p163116118106"></a>Creation of user, LOGIN, or database</p>
</td>
<td class="cellrowborder" valign="top" width="32.26%" headers="mcps1.2.4.1.2 "><p id="p1722646218106"><a name="p1722646218106"></a><a name="p1722646218106"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="30.44%" headers="mcps1.2.4.1.3 "><p id="p5316617618106"><a name="p5316617618106"></a><a name="p5316617618106"></a>Supported</p>
</td>
</tr>
<tr id="row873353818106"><td class="cellrowborder" valign="top" width="37.3%" headers="mcps1.2.4.1.1 "><p id="p3632801618106"><a name="p3632801618106"></a><a name="p3632801618106"></a>Database-level DDL trigger</p>
</td>
<td class="cellrowborder" valign="top" width="32.26%" headers="mcps1.2.4.1.2 "><p id="p6532490818106"><a name="p6532490818106"></a><a name="p6532490818106"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="30.44%" headers="mcps1.2.4.1.3 "><p id="p5682623318106"><a name="p5682623318106"></a><a name="p5682623318106"></a>Supported</p>
</td>
</tr>
<tr id="row4167405218106"><td class="cellrowborder" valign="top" width="37.3%" headers="mcps1.2.4.1.1 "><p id="p2015503218106"><a name="p2015503218106"></a><a name="p2015503218106"></a>Database permission authorization</p>
</td>
<td class="cellrowborder" valign="top" width="32.26%" headers="mcps1.2.4.1.2 "><p id="p2194488918106"><a name="p2194488918106"></a><a name="p2194488918106"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="30.44%" headers="mcps1.2.4.1.3 "><p id="p3270555018106"><a name="p3270555018106"></a><a name="p3270555018106"></a>Supported</p>
</td>
</tr>
<tr id="row2591449518106"><td class="cellrowborder" valign="top" width="37.3%" headers="mcps1.2.4.1.1 "><p id="p1869939018106"><a name="p1869939018106"></a><a name="p1869939018106"></a>KILL permission</p>
</td>
<td class="cellrowborder" valign="top" width="32.26%" headers="mcps1.2.4.1.2 "><p id="p3825565418106"><a name="p3825565418106"></a><a name="p3825565418106"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="30.44%" headers="mcps1.2.4.1.3 "><p id="p1170025418106"><a name="p1170025418106"></a><a name="p1170025418106"></a>Supported</p>
</td>
</tr>
<tr id="row3819342318106"><td class="cellrowborder" valign="top" width="37.3%" headers="mcps1.2.4.1.1 "><p id="p665958718106"><a name="p665958718106"></a><a name="p665958718106"></a>LinkServer</p>
</td>
<td class="cellrowborder" valign="top" width="32.26%" headers="mcps1.2.4.1.2 "><p id="p131659452086"><a name="p131659452086"></a><a name="p131659452086"></a>Coming soon</p>
</td>
<td class="cellrowborder" valign="top" width="30.44%" headers="mcps1.2.4.1.3 "><p id="p187561317991"><a name="p187561317991"></a><a name="p187561317991"></a>Coming soon</p>
</td>
</tr>
<tr id="row5114822618106"><td class="cellrowborder" valign="top" width="37.3%" headers="mcps1.2.4.1.1 "><p id="p4936566918106"><a name="p4936566918106"></a><a name="p4936566918106"></a>Distributed transaction</p>
</td>
<td class="cellrowborder" valign="top" width="32.26%" headers="mcps1.2.4.1.2 "><p id="p1354132017917"><a name="p1354132017917"></a><a name="p1354132017917"></a>Coming soon</p>
</td>
<td class="cellrowborder" valign="top" width="30.44%" headers="mcps1.2.4.1.3 "><p id="p32646235913"><a name="p32646235913"></a><a name="p32646235913"></a>Coming soon</p>
</td>
</tr>
<tr id="row5278603118106"><td class="cellrowborder" valign="top" width="37.3%" headers="mcps1.2.4.1.1 "><p id="p4781015518106"><a name="p4781015518106"></a><a name="p4781015518106"></a>SQL Profiler</p>
</td>
<td class="cellrowborder" valign="top" width="32.26%" headers="mcps1.2.4.1.2 "><p id="p4741731418106"><a name="p4741731418106"></a><a name="p4741731418106"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="30.44%" headers="mcps1.2.4.1.3 "><p id="p1559724618106"><a name="p1559724618106"></a><a name="p1559724618106"></a>Supported</p>
</td>
</tr>
<tr id="row615749418106"><td class="cellrowborder" valign="top" width="37.3%" headers="mcps1.2.4.1.1 "><p id="p2899498018106"><a name="p2899498018106"></a><a name="p2899498018106"></a>Tuning Advisor</p>
</td>
<td class="cellrowborder" valign="top" width="32.26%" headers="mcps1.2.4.1.2 "><p id="p6689201018106"><a name="p6689201018106"></a><a name="p6689201018106"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="30.44%" headers="mcps1.2.4.1.3 "><p id="p4954372918106"><a name="p4954372918106"></a><a name="p4954372918106"></a>Supported</p>
</td>
</tr>
<tr id="row4324038018106"><td class="cellrowborder" valign="top" width="37.3%" headers="mcps1.2.4.1.1 "><p id="p1280989518106"><a name="p1280989518106"></a><a name="p1280989518106"></a>Change Data Capture (CDC)</p>
</td>
<td class="cellrowborder" valign="top" width="32.26%" headers="mcps1.2.4.1.2 "><p id="p3096855018106"><a name="p3096855018106"></a><a name="p3096855018106"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="30.44%" headers="mcps1.2.4.1.3 "><p id="p2542461018106"><a name="p2542461018106"></a><a name="p2542461018106"></a>Supported</p>
</td>
</tr>
<tr id="row2749489818106"><td class="cellrowborder" valign="top" width="37.3%" headers="mcps1.2.4.1.1 "><p id="p1249422718106"><a name="p1249422718106"></a><a name="p1249422718106"></a>Change tracking</p>
</td>
<td class="cellrowborder" valign="top" width="32.26%" headers="mcps1.2.4.1.2 "><p id="p539946118106"><a name="p539946118106"></a><a name="p539946118106"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="30.44%" headers="mcps1.2.4.1.3 "><p id="p3470318318106"><a name="p3470318318106"></a><a name="p3470318318106"></a>Supported</p>
</td>
</tr>
<tr id="row4389319718106"><td class="cellrowborder" valign="top" width="37.3%" headers="mcps1.2.4.1.1 "><p id="p6568807918106"><a name="p6568807918106"></a><a name="p6568807918106"></a>Windows domain account login</p>
</td>
<td class="cellrowborder" valign="top" width="32.26%" headers="mcps1.2.4.1.2 "><p id="p636684918106"><a name="p636684918106"></a><a name="p636684918106"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="30.44%" headers="mcps1.2.4.1.3 "><p id="p12690830184917"><a name="p12690830184917"></a><a name="p12690830184917"></a>Supported</p>
</td>
</tr>
<tr id="row1092173918106"><td class="cellrowborder" valign="top" width="37.3%" headers="mcps1.2.4.1.1 "><p id="p1224564818106"><a name="p1224564818106"></a><a name="p1224564818106"></a>Email</p>
</td>
<td class="cellrowborder" valign="top" width="32.26%" headers="mcps1.2.4.1.2 "><p id="p2101413164916"><a name="p2101413164916"></a><a name="p2101413164916"></a>Not supported</p>
</td>
<td class="cellrowborder" valign="top" width="30.44%" headers="mcps1.2.4.1.3 "><p id="p108453224910"><a name="p108453224910"></a><a name="p108453224910"></a>Not supported</p>
</td>
</tr>
<tr id="row6240780418106"><td class="cellrowborder" valign="top" width="37.3%" headers="mcps1.2.4.1.1 "><p id="p2186739518106"><a name="p2186739518106"></a><a name="p2186739518106"></a>SQL Server Integration Services (SSIS)</p>
</td>
<td class="cellrowborder" valign="top" width="32.26%" headers="mcps1.2.4.1.2 "><p id="p1191714134918"><a name="p1191714134918"></a><a name="p1191714134918"></a>Not supported</p>
</td>
<td class="cellrowborder" valign="top" width="30.44%" headers="mcps1.2.4.1.3 "><p id="p2177103316492"><a name="p2177103316492"></a><a name="p2177103316492"></a>Not supported</p>
</td>
</tr>
<tr id="row5933476018106"><td class="cellrowborder" valign="top" width="37.3%" headers="mcps1.2.4.1.1 "><p id="p4138626918106"><a name="p4138626918106"></a><a name="p4138626918106"></a>SQL Server Analysis Services (SSAS)</p>
</td>
<td class="cellrowborder" valign="top" width="32.26%" headers="mcps1.2.4.1.2 "><p id="p2283161514912"><a name="p2283161514912"></a><a name="p2283161514912"></a>Not supported</p>
</td>
<td class="cellrowborder" valign="top" width="30.44%" headers="mcps1.2.4.1.3 "><p id="p4324734174910"><a name="p4324734174910"></a><a name="p4324734174910"></a>Not supported</p>
</td>
</tr>
<tr id="row1505255618106"><td class="cellrowborder" valign="top" width="37.3%" headers="mcps1.2.4.1.1 "><p id="p1129756018106"><a name="p1129756018106"></a><a name="p1129756018106"></a>SQL Server Reporting Services (SSRS)</p>
</td>
<td class="cellrowborder" valign="top" width="32.26%" headers="mcps1.2.4.1.2 "><p id="p13408161492"><a name="p13408161492"></a><a name="p13408161492"></a>Not supported</p>
</td>
<td class="cellrowborder" valign="top" width="30.44%" headers="mcps1.2.4.1.3 "><p id="p17517123534918"><a name="p17517123534918"></a><a name="p17517123534918"></a>Not supported</p>
</td>
</tr>
<tr id="row1239800118106"><td class="cellrowborder" valign="top" width="37.3%" headers="mcps1.2.4.1.1 "><p id="p6471404318106"><a name="p6471404318106"></a><a name="p6471404318106"></a>R Services</p>
</td>
<td class="cellrowborder" valign="top" width="32.26%" headers="mcps1.2.4.1.2 "><p id="p1330971715493"><a name="p1330971715493"></a><a name="p1330971715493"></a>Not supported</p>
</td>
<td class="cellrowborder" valign="top" width="30.44%" headers="mcps1.2.4.1.3 "><p id="p128092364496"><a name="p128092364496"></a><a name="p128092364496"></a>Not supported</p>
</td>
</tr>
<tr id="row5654238218106"><td class="cellrowborder" valign="top" width="37.3%" headers="mcps1.2.4.1.1 "><p id="p1653019918106"><a name="p1653019918106"></a><a name="p1653019918106"></a>Common Language Runtime (CLR)</p>
</td>
<td class="cellrowborder" valign="top" width="32.26%" headers="mcps1.2.4.1.2 "><p id="p1436931884918"><a name="p1436931884918"></a><a name="p1436931884918"></a>Not supported</p>
</td>
<td class="cellrowborder" valign="top" width="30.44%" headers="mcps1.2.4.1.3 "><p id="p268838154913"><a name="p268838154913"></a><a name="p268838154913"></a>Not supported</p>
</td>
</tr>
<tr id="row1093571118106"><td class="cellrowborder" valign="top" width="37.3%" headers="mcps1.2.4.1.1 "><p id="p1337741118106"><a name="p1337741118106"></a><a name="p1337741118106"></a>Asynchronous communication</p>
</td>
<td class="cellrowborder" valign="top" width="32.26%" headers="mcps1.2.4.1.2 "><p id="p1765717232490"><a name="p1765717232490"></a><a name="p1765717232490"></a>Not supported</p>
</td>
<td class="cellrowborder" valign="top" width="30.44%" headers="mcps1.2.4.1.3 "><p id="p829819393498"><a name="p829819393498"></a><a name="p829819393498"></a>Not supported</p>
</td>
</tr>
<tr id="row5141574218106"><td class="cellrowborder" valign="top" width="37.3%" headers="mcps1.2.4.1.1 "><p id="p392555418106"><a name="p392555418106"></a><a name="p392555418106"></a>Replication subscription</p>
</td>
<td class="cellrowborder" valign="top" width="32.26%" headers="mcps1.2.4.1.2 "><p id="p1064617259492"><a name="p1064617259492"></a><a name="p1064617259492"></a>Not supported</p>
</td>
<td class="cellrowborder" valign="top" width="30.44%" headers="mcps1.2.4.1.3 "><p id="p693414411496"><a name="p693414411496"></a><a name="p693414411496"></a>Not supported</p>
</td>
</tr>
<tr id="row604599318106"><td class="cellrowborder" valign="top" width="37.3%" headers="mcps1.2.4.1.1 "><p id="p1996346418106"><a name="p1996346418106"></a><a name="p1996346418106"></a>Policy management</p>
</td>
<td class="cellrowborder" valign="top" width="32.26%" headers="mcps1.2.4.1.2 "><p id="p840122794918"><a name="p840122794918"></a><a name="p840122794918"></a>Not supported</p>
</td>
<td class="cellrowborder" valign="top" width="30.44%" headers="mcps1.2.4.1.3 "><p id="p13418444134910"><a name="p13418444134910"></a><a name="p13418444134910"></a>Not supported</p>
</td>
</tr>
</tbody>
</table>

