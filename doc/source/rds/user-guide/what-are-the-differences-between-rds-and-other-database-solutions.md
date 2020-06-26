# What Are the Differences Between RDS and Other Database Solutions?<a name="rds_faq_0004"></a>

**Table  1**  Differences between RDS and other database solution

<a name="t1ee19783e84542c99ecf2686c040f909"></a>
<table><thead align="left"><tr id="ra1834b44ed1543f58625a2961e79fe53"><th class="cellrowborder" valign="top" width="24.5%" id="mcps1.2.4.1.1"><p id="ac00772621b6c43e784ed4ff099743327"><a name="ac00772621b6c43e784ed4ff099743327"></a><a name="ac00772621b6c43e784ed4ff099743327"></a><strong id="b146061211191912"><a name="b146061211191912"></a><a name="b146061211191912"></a>Function Item</strong></p>
</th>
<th class="cellrowborder" valign="top" width="42.17%" id="mcps1.2.4.1.2"><p id="a5870ab40d5324a058fb9bae32ce61401"><a name="a5870ab40d5324a058fb9bae32ce61401"></a><a name="a5870ab40d5324a058fb9bae32ce61401"></a>RDS</p>
</th>
<th class="cellrowborder" valign="top" width="33.33%" id="mcps1.2.4.1.3"><p id="a40c70442a3fb4e7d929e7a6b364a6e46"><a name="a40c70442a3fb4e7d929e7a6b364a6e46"></a><a name="a40c70442a3fb4e7d929e7a6b364a6e46"></a>Self-Built Database Service</p>
</th>
</tr>
</thead>
<tbody><tr id="rbde998da857b4cee87a88d986d274cb4"><td class="cellrowborder" valign="top" width="24.5%" headers="mcps1.2.4.1.1 "><p id="a096abf7dadaa4933b46c41e72faed520"><a name="a096abf7dadaa4933b46c41e72faed520"></a><a name="a096abf7dadaa4933b46c41e72faed520"></a>Service availability</p>
</td>
<td class="cellrowborder" valign="top" width="42.17%" headers="mcps1.2.4.1.2 "><p id="p76401257185214"><a name="p76401257185214"></a><a name="p76401257185214"></a>For more information, see the <em id="i20443841131020"><a name="i20443841131020"></a><a name="i20443841131020"></a>Elastic Cloud Server User Guide</em>.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="ac26fea6051264be49d778b31638b273d"><a name="ac26fea6051264be49d778b31638b273d"></a><a name="ac26fea6051264be49d778b31638b273d"></a>Requires self-guarantee, primary/standby relationship setup, and RAID setup.</p>
</td>
</tr>
<tr id="r9a80f74e79f048c698680a8116632fea"><td class="cellrowborder" valign="top" width="24.5%" headers="mcps1.2.4.1.1 "><p id="ad197764913904f12ba146feda19c96ab"><a name="ad197764913904f12ba146feda19c96ab"></a><a name="ad197764913904f12ba146feda19c96ab"></a>Data reliability</p>
</td>
<td class="cellrowborder" valign="top" width="42.17%" headers="mcps1.2.4.1.2 "><p id="p1542794165316"><a name="p1542794165316"></a><a name="p1542794165316"></a>For more information, see the <em id="i19488151141111"><a name="i19488151141111"></a><a name="i19488151141111"></a>Elastic Volume Service User Guide</em>.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="a10276158f2fd4ae7a4365892f2f9b6fa"><a name="a10276158f2fd4ae7a4365892f2f9b6fa"></a><a name="a10276158f2fd4ae7a4365892f2f9b6fa"></a>Requires self-guarantee, primary/standby relationship setup, and RAID setup.</p>
</td>
</tr>
<tr id="re899ffa7c7f8487cb183cc38a03c05be"><td class="cellrowborder" valign="top" width="24.5%" headers="mcps1.2.4.1.1 "><p id="a35c768d18d7745bbac22de2557865f6e"><a name="a35c768d18d7745bbac22de2557865f6e"></a><a name="a35c768d18d7745bbac22de2557865f6e"></a>System security</p>
</td>
<td class="cellrowborder" valign="top" width="42.17%" headers="mcps1.2.4.1.2 "><p id="ad4a6e830a7844b6e83acf83b7e97885b"><a name="ad4a6e830a7844b6e83acf83b7e97885b"></a><a name="ad4a6e830a7844b6e83acf83b7e97885b"></a>Defends against Anti-DDoS attacks and promptly repairs database security vulnerabilities.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="a6d1a37d47d50422c9ac620d3fdc5714f"><a name="a6d1a37d47d50422c9ac620d3fdc5714f"></a><a name="a6d1a37d47d50422c9ac620d3fdc5714f"></a>Requires procurement of expensive devices and software, as well as manual detection and repair of security vulnerabilities.</p>
</td>
</tr>
<tr id="r7168aea7b4ee415c8e4512564a3969ac"><td class="cellrowborder" valign="top" width="24.5%" headers="mcps1.2.4.1.1 "><p id="aa74a1ff0081e4e0fb746d7a844386c0a"><a name="aa74a1ff0081e4e0fb746d7a844386c0a"></a><a name="aa74a1ff0081e4e0fb746d7a844386c0a"></a>Database backup</p>
</td>
<td class="cellrowborder" valign="top" width="42.17%" headers="mcps1.2.4.1.2 "><p id="a87a1913b75f84d36811af516e7c0af84"><a name="a87a1913b75f84d36811af516e7c0af84"></a><a name="a87a1913b75f84d36811af516e7c0af84"></a>Automated backups</p>
</td>
<td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="a3b3b04ae813d4c51b69f91a0cb96f246"><a name="a3b3b04ae813d4c51b69f91a0cb96f246"></a><a name="a3b3b04ae813d4c51b69f91a0cb96f246"></a>You must find backup storage space to back up the database by yourself and periodically check whether backup data can be restored.</p>
</td>
</tr>
<tr id="r7a013e013f8c40fc90265eec20210d4b"><td class="cellrowborder" valign="top" width="24.5%" headers="mcps1.2.4.1.1 "><p id="a65e609812cb24296bf72e0cad3fc4d9f"><a name="a65e609812cb24296bf72e0cad3fc4d9f"></a><a name="a65e609812cb24296bf72e0cad3fc4d9f"></a>Hardware and software investment</p>
</td>
<td class="cellrowborder" valign="top" width="42.17%" headers="mcps1.2.4.1.2 "><p id="a8a7a6cd27c1f481d8c7bf225a08bea81"><a name="a8a7a6cd27c1f481d8c7bf225a08bea81"></a><a name="a8a7a6cd27c1f481d8c7bf225a08bea81"></a>Supports on-demand pricing and scaling without requiring hardware and software investment.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="acd33914e287f42feadd9e7f2d0e3322a"><a name="acd33914e287f42feadd9e7f2d0e3322a"></a><a name="acd33914e287f42feadd9e7f2d0e3322a"></a>Requires large investment in database servers.</p>
</td>
</tr>
<tr id="r7da3646cc0e34148bbac24861043bfdc"><td class="cellrowborder" valign="top" width="24.5%" headers="mcps1.2.4.1.1 "><p id="a50cdab79c87c4a50a7ab7eab795bcd10"><a name="a50cdab79c87c4a50a7ab7eab795bcd10"></a><a name="a50cdab79c87c4a50a7ab7eab795bcd10"></a>System hosting</p>
</td>
<td class="cellrowborder" valign="top" width="42.17%" headers="mcps1.2.4.1.2 "><p id="a48f5e90c4bf447c8ac9ea9a62c09ded5"><a name="a48f5e90c4bf447c8ac9ea9a62c09ded5"></a><a name="a48f5e90c4bf447c8ac9ea9a62c09ded5"></a>Not required.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="a6edeca2a84104c7f820b018fce12ece5"><a name="a6edeca2a84104c7f820b018fce12ece5"></a><a name="a6edeca2a84104c7f820b018fce12ece5"></a>The hosting cost is high.</p>
</td>
</tr>
<tr id="r90b088f853c74afc9d000d9cef4791b9"><td class="cellrowborder" valign="top" width="24.5%" headers="mcps1.2.4.1.1 "><p id="afc7b55249c72439d9cd8700c6ebfaf9e"><a name="afc7b55249c72439d9cd8700c6ebfaf9e"></a><a name="afc7b55249c72439d9cd8700c6ebfaf9e"></a>Maintenance cost</p>
</td>
<td class="cellrowborder" valign="top" width="42.17%" headers="mcps1.2.4.1.2 "><p id="a0cd09c5aac8340989ed2d74df707063c"><a name="a0cd09c5aac8340989ed2d74df707063c"></a><a name="a0cd09c5aac8340989ed2d74df707063c"></a>Not required.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="a4dca35fd8d5b431cafcc03cae476060d"><a name="a4dca35fd8d5b431cafcc03cae476060d"></a><a name="a4dca35fd8d5b431cafcc03cae476060d"></a>Full-time Database Administrators (DBAs) are required for maintenance, leading to high manpower costs.</p>
</td>
</tr>
<tr id="r68f30bd1ba8946e3b4b1d44947fea974"><td class="cellrowborder" valign="top" width="24.5%" headers="mcps1.2.4.1.1 "><p id="ae794be61ed254c9c9acf92f09b492fc5"><a name="ae794be61ed254c9c9acf92f09b492fc5"></a><a name="ae794be61ed254c9c9acf92f09b492fc5"></a>Deployment and scaling</p>
</td>
<td class="cellrowborder" valign="top" width="42.17%" headers="mcps1.2.4.1.2 "><p id="a5c3bf3bc081e49f0bef8806fd149094e"><a name="a5c3bf3bc081e49f0bef8806fd149094e"></a><a name="a5c3bf3bc081e49f0bef8806fd149094e"></a>Supports elastic scaling, fast deployment, and on-demand enabling.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="a0c9be0b3891144279c7b1181a1bc8740"><a name="a0c9be0b3891144279c7b1181a1bc8740"></a><a name="a0c9be0b3891144279c7b1181a1bc8740"></a>Requires procurement, deployment, and coordination of hardware.</p>
</td>
</tr>
<tr id="r4b02d6be6e5d496d8623ec4608c5b281"><td class="cellrowborder" valign="top" width="24.5%" headers="mcps1.2.4.1.1 "><p id="a828f5464c50b4e00bc890d54fad26bf0"><a name="a828f5464c50b4e00bc890d54fad26bf0"></a><a name="a828f5464c50b4e00bc890d54fad26bf0"></a>Resource utilization</p>
</td>
<td class="cellrowborder" valign="top" width="42.17%" headers="mcps1.2.4.1.2 "><p id="acceb29dfcbcd4ba397f461e8c0091f07"><a name="acceb29dfcbcd4ba397f461e8c0091f07"></a><a name="acceb29dfcbcd4ba397f461e8c0091f07"></a>Bills users based on the resources actually used, resulting in high resource utilization.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="a9ace631b8b31480b904ccb07776a762d"><a name="a9ace631b8b31480b904ccb07776a762d"></a><a name="a9ace631b8b31480b904ccb07776a762d"></a>Peak resource utilization is considered, leading to low resource usage.</p>
</td>
</tr>
</tbody>
</table>

