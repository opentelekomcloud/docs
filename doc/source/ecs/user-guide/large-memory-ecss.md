# Large-Memory ECSs<a name="EN-US_TOPIC_0038024694"></a>

## Overview<a name="section25374905172644"></a>

Large-memory ECSs provide an even larger amount of memory than memory-optimized ECSs. They are used for applications that require a large amount of memory, rapid data switching, low latency, and process large volumes of data. Large-memory ECSs provide large memory and high computing, storage, and network performance.

-   Applications

    Large-memory ECSs are suitable for applications that require a large amount of memory, rapid data switching, and low latency, and process large volumes of data.

-   Application scenarios

    E3 ECSs: OLAP and OLTP applications with hyper-threading enabled, SAP HANA applications \(including Business Suite S/4HANA, Business Suite on HANA, and Business Warehouse on HANA\), and big data processing engines \(Apache Spark\)

    E2 ECSs: OLAP applications, such as in-memory databases \(SAP HANA SoH, SAP HANA applications, including Business Suite S/4HANA, Business Suite on HANA, and Business Warehouse on HANA\), big data processing engines \(Apache Spark\), high-performance databases, and distributed memory cache

    E1 ECSs: OLTP applications, such as in-memory databases \(SAP HANA BWoH, SAP HANA applications, including Business Suite S/4HANA, Business Suite on HANA, and Business Warehouse on HANA\), big data processing engines \(Apache Spark\), and data mining


## Specifications<a name="section60740876172648"></a>

**Table  1**  E3 ECS specifications

<a name="table990906134813"></a>
<table><thead align="left"><tr id="row17950661481"><th class="cellrowborder" valign="top" width="15.391539153915392%" id="mcps1.2.6.1.1"><p id="p1695513611482"><a name="p1695513611482"></a><a name="p1695513611482"></a>Flavor</p>
</th>
<th class="cellrowborder" valign="top" width="12.421242124212421%" id="mcps1.2.6.1.2"><p id="p19621644812"><a name="p19621644812"></a><a name="p19621644812"></a>vCPUs</p>
</th>
<th class="cellrowborder" valign="top" width="14.561456145614562%" id="mcps1.2.6.1.3"><p id="p1396916664812"><a name="p1396916664812"></a><a name="p1396916664812"></a>Memory (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="19.321932193219325%" id="mcps1.2.6.1.4"><p id="p89741863481"><a name="p89741863481"></a><a name="p89741863481"></a>Virtualization Type</p>
</th>
<th class="cellrowborder" valign="top" width="38.3038303830383%" id="mcps1.2.6.1.5"><p id="p12984569487"><a name="p12984569487"></a><a name="p12984569487"></a>Hardware</p>
</th>
</tr>
</thead>
<tbody><tr id="row16992136124811"><td class="cellrowborder" valign="top" width="15.391539153915392%" headers="mcps1.2.6.1.1 "><p id="p8814784810"><a name="p8814784810"></a><a name="p8814784810"></a>e3.7xlarge.12</p>
</td>
<td class="cellrowborder" valign="top" width="12.421242124212421%" headers="mcps1.2.6.1.2 "><p id="p12140784810"><a name="p12140784810"></a><a name="p12140784810"></a>28</p>
</td>
<td class="cellrowborder" valign="top" width="14.561456145614562%" headers="mcps1.2.6.1.3 "><p id="p122227144820"><a name="p122227144820"></a><a name="p122227144820"></a>348</p>
</td>
<td class="cellrowborder" valign="top" width="19.321932193219325%" headers="mcps1.2.6.1.4 "><p id="p82718719484"><a name="p82718719484"></a><a name="p82718719484"></a>KVM</p>
</td>
<td class="cellrowborder" rowspan="2" valign="top" width="38.3038303830383%" headers="mcps1.2.6.1.5 "><a name="ul173615734815"></a><a name="ul173615734815"></a><ul id="ul173615734815"><li>CPU: Intel&reg; Xeon&reg; Skylake 6151</li><li>Business network: 25GE Hi1822 IP network</li><li>Storage network: 10GE IP network</li><li>Disk type: ultra-high I/O</li></ul>
</td>
</tr>
<tr id="row7661710484"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p16711713481"><a name="p16711713481"></a><a name="p16711713481"></a>e3.14xlarge.12</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p138019794816"><a name="p138019794816"></a><a name="p138019794816"></a>56</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p5861473487"><a name="p5861473487"></a><a name="p5861473487"></a>696</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p392774489"><a name="p392774489"></a><a name="p392774489"></a>KVM</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  E2 ECS specifications

<a name="table4426383111138"></a>
<table><thead align="left"><tr id="row323980411138"><th class="cellrowborder" valign="top" width="15.680000000000001%" id="mcps1.2.6.1.1"><p id="p8405717163040"><a name="p8405717163040"></a><a name="p8405717163040"></a>Flavor</p>
</th>
<th class="cellrowborder" valign="top" width="12.070000000000002%" id="mcps1.2.6.1.2"><p id="p37815862163040"><a name="p37815862163040"></a><a name="p37815862163040"></a>vCPUs</p>
</th>
<th class="cellrowborder" valign="top" width="14.440000000000003%" id="mcps1.2.6.1.3"><p id="p43186007163040"><a name="p43186007163040"></a><a name="p43186007163040"></a>Memory (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="19.380000000000003%" id="mcps1.2.6.1.4"><p id="p1766425318479"><a name="p1766425318479"></a><a name="p1766425318479"></a>Virtualization Type</p>
</th>
<th class="cellrowborder" valign="top" width="38.43%" id="mcps1.2.6.1.5"><p id="p1341618459165"><a name="p1341618459165"></a><a name="p1341618459165"></a>Hardware</p>
</th>
</tr>
</thead>
<tbody><tr id="row2478456011138"><td class="cellrowborder" valign="top" width="15.680000000000001%" headers="mcps1.2.6.1.1 "><p id="p792104211138"><a name="p792104211138"></a><a name="p792104211138"></a>e2.2xlarge</p>
</td>
<td class="cellrowborder" valign="top" width="12.070000000000002%" headers="mcps1.2.6.1.2 "><p id="p6139236711138"><a name="p6139236711138"></a><a name="p6139236711138"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="14.440000000000003%" headers="mcps1.2.6.1.3 "><p id="p672582611138"><a name="p672582611138"></a><a name="p672582611138"></a>128</p>
</td>
<td class="cellrowborder" valign="top" width="19.380000000000003%" headers="mcps1.2.6.1.4 "><p id="p1669145317476"><a name="p1669145317476"></a><a name="p1669145317476"></a>Xen</p>
</td>
<td class="cellrowborder" rowspan="4" valign="top" width="38.43%" headers="mcps1.2.6.1.5 "><a name="ul147065322718"></a><a name="ul147065322718"></a><ul id="ul147065322718"><li>CPU: Intel&reg; Xeon&reg; Processor Haswell E7-8880</li><li>Business network: 10GE SR-IOV passthrough IP network</li><li>Storage network: 56 Gbit/s InfiniBand network</li><li>Disk type: high I/O (performance-optimized I) and ultra-high I/O (latency-optimized)</li></ul>
</td>
</tr>
<tr id="row418051611138"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p5880303711138"><a name="p5880303711138"></a><a name="p5880303711138"></a>e2.3xlarge</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p307749711138"><a name="p307749711138"></a><a name="p307749711138"></a>12</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p4795071911138"><a name="p4795071911138"></a><a name="p4795071911138"></a>256</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p1676165344711"><a name="p1676165344711"></a><a name="p1676165344711"></a>Xen</p>
</td>
</tr>
<tr id="row5946529311138"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p6009702111138"><a name="p6009702111138"></a><a name="p6009702111138"></a>e2.4xlarge</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p5195946011138"><a name="p5195946011138"></a><a name="p5195946011138"></a>18</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p4796669411138"><a name="p4796669411138"></a><a name="p4796669411138"></a>445</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p15679125320474"><a name="p15679125320474"></a><a name="p15679125320474"></a>Xen</p>
</td>
</tr>
<tr id="row400228411138"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p2980051211138"><a name="p2980051211138"></a><a name="p2980051211138"></a>e2.9xlarge</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p5574959711138"><a name="p5574959711138"></a><a name="p5574959711138"></a>36</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p1942351011138"><a name="p1942351011138"></a><a name="p1942351011138"></a>890</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p1235111514477"><a name="p1235111514477"></a><a name="p1235111514477"></a>Xen</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  E1 ECS specifications

<a name="table54857549174414"></a>
<table><thead align="left"><tr id="row35495632174414"><th class="cellrowborder" valign="top" width="15.7%" id="mcps1.2.6.1.1"><p id="p35165907163036"><a name="p35165907163036"></a><a name="p35165907163036"></a>Flavor</p>
</th>
<th class="cellrowborder" valign="top" width="12.02%" id="mcps1.2.6.1.2"><p id="p35978820163036"><a name="p35978820163036"></a><a name="p35978820163036"></a>vCPUs</p>
</th>
<th class="cellrowborder" valign="top" width="14.48%" id="mcps1.2.6.1.3"><p id="p28603299163036"><a name="p28603299163036"></a><a name="p28603299163036"></a>Memory (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="19.41%" id="mcps1.2.6.1.4"><p id="p1246713010473"><a name="p1246713010473"></a><a name="p1246713010473"></a>Virtualization Type</p>
</th>
<th class="cellrowborder" valign="top" width="38.39%" id="mcps1.2.6.1.5"><p id="p15774111519558"><a name="p15774111519558"></a><a name="p15774111519558"></a>Hardware</p>
</th>
</tr>
</thead>
<tbody><tr id="row60052369193236"><td class="cellrowborder" valign="top" width="15.7%" headers="mcps1.2.6.1.1 "><p id="p22279241193251"><a name="p22279241193251"></a><a name="p22279241193251"></a>e1.xlarge</p>
</td>
<td class="cellrowborder" valign="top" width="12.02%" headers="mcps1.2.6.1.2 "><p id="p40528516193251"><a name="p40528516193251"></a><a name="p40528516193251"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="14.48%" headers="mcps1.2.6.1.3 "><p id="p61584384193251"><a name="p61584384193251"></a><a name="p61584384193251"></a>128</p>
</td>
<td class="cellrowborder" valign="top" width="19.41%" headers="mcps1.2.6.1.4 "><p id="p104721030144719"><a name="p104721030144719"></a><a name="p104721030144719"></a>Xen</p>
</td>
<td class="cellrowborder" rowspan="4" valign="top" width="38.39%" headers="mcps1.2.6.1.5 "><a name="ul85954144616"></a><a name="ul85954144616"></a><ul id="ul85954144616"><li>CPU: Intel&reg; Xeon&reg; Processor Haswell E7-8880</li><li>Business network: 10GE SR-IOV passthrough IP network</li><li>Storage network: 56 Gbit/s InfiniBand network</li><li>Disk type: high I/O (performance-optimized I) and ultra-high I/O (latency-optimized)</li></ul>
</td>
</tr>
<tr id="row62195446193236"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p15060818193251"><a name="p15060818193251"></a><a name="p15060818193251"></a>e1.2xlarge</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p31874147193251"><a name="p31874147193251"></a><a name="p31874147193251"></a>8</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p31669106193251"><a name="p31669106193251"></a><a name="p31669106193251"></a>256</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p747483034718"><a name="p747483034718"></a><a name="p747483034718"></a>Xen</p>
</td>
</tr>
<tr id="row23053169193236"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p43757137193251"><a name="p43757137193251"></a><a name="p43757137193251"></a>e1.4xlarge</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p66726852193251"><a name="p66726852193251"></a><a name="p66726852193251"></a>16</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p36165904193251"><a name="p36165904193251"></a><a name="p36165904193251"></a>470</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p1847883011473"><a name="p1847883011473"></a><a name="p1847883011473"></a>Xen</p>
</td>
</tr>
<tr id="row31549687193236"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p47314592193251"><a name="p47314592193251"></a><a name="p47314592193251"></a>e1.8xlarge</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p56867168193251"><a name="p56867168193251"></a><a name="p56867168193251"></a>32</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p42837859193251"><a name="p42837859193251"></a><a name="p42837859193251"></a>940</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p6995172014715"><a name="p6995172014715"></a><a name="p6995172014715"></a>Xen</p>
</td>
</tr>
</tbody>
</table>

## Notes<a name="section3320087010555"></a>

-   Large-memory ECSs do not support NIC hot swapping.
-   E1 and E2 ECSs support the following OSs:
    -   Windows Server 2016 DataCenter 64bit
    -   Windows Server 2012 Standard 64bit
    -   Windows Server 2012 DataCenter 64bit
    -   Windows Server 2012 R2 DataCenter 64bit
    -   Windows Server 2012 R2 Standard 64bit
    -   Windows Server 2012 R2 Essentials 64bit
    -   CentOS 7.3 64bit
    -   CentOS 7.2 64bit
    -   CentOS 7.1 64bit
    -   CentOS 7.0 64bit
    -   CentOS 6.8 64bit
    -   CentOS 6.7 64bit
    -   CentOS 6.6 64bit
    -   CentOS 6.5 64bit
    -   CentOS 6.4 64bit
    -   CentOS 6.3 64bit
    -   Debian 8.0 64bit
    -   Debian 8.4 64bit
    -   Debian 8.5 64bit
    -   Debian 8.6 64bit
    -   OpenSUSE 42.2 64bit
    -   Ubuntu Server 16.10 64bit
    -   Ubuntu Server 16.04 64bit
    -   SUSE Linux Enterprise Server 11 SP3 64bit
    -   SUSE Linux Enterprise Server 11 SP4 64bit
    -   SUSE Linux Enterprise Server 12 64bit
    -   SUSE Linux Enterprise Server 12 SP1 64bit
    -   SUSE Linux Enterprise Server 12 SP2 64bit
    -   Red Hat Enterprise Linux 6.8 64bit
    -   Red Hat Enterprise Linux 7.0 64bit
    -   Red Hat Enterprise Linux 7.2 64bit
    -   Red Hat Enterprise Linux 7.3 64bit
    -   Fedora 25 64bit
    -   Oracle Enterprise Linux 6.8 64bit
    -   Oracle Enterprise Linux 7.3 64bit
    -   EulerOS 2.2 64bit

-   E3 ECSs support the following OSs that have been verified:

    SUSE Enterprise Linux Server 12 SP2 64bit

    SUSE Enterprise Linux Server 12 SP3 64bit

-   E1 and E2 ECSs can use the following types of EVS disks as system disk and data disk:
    -   High I/O \(performance-optimized I\)
    -   Ultra-high I/O \(latency-optimized\)

-   E3 ECSs can use ultra-high I/O EVS disks as the system disk and data disks.
-   The primary and extension NICs of a large-memory ECS have specified application scenarios. For details, see  [Table 4](#table1642803151326).

    **Table  4**  Application scenarios of the NICs of a large-memory ECS

    <a name="table1642803151326"></a>
    <table><thead align="left"><tr id="row7839896151326"><th class="cellrowborder" valign="top" width="19.61%" id="mcps1.2.4.1.1"><p id="p14196851151326"><a name="p14196851151326"></a><a name="p14196851151326"></a>NIC Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="34.089999999999996%" id="mcps1.2.4.1.2"><p id="p9094287151326"><a name="p9094287151326"></a><a name="p9094287151326"></a>Application Scenario</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.300000000000004%" id="mcps1.2.4.1.3"><p id="p65548643151326"><a name="p65548643151326"></a><a name="p65548643151326"></a>Remarks</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row28810193151326"><td class="cellrowborder" valign="top" width="19.61%" headers="mcps1.2.4.1.1 "><p id="p31051862151326"><a name="p31051862151326"></a><a name="p31051862151326"></a>Primary NIC</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.089999999999996%" headers="mcps1.2.4.1.2 "><p id="p32172868151326"><a name="p32172868151326"></a><a name="p32172868151326"></a>Vertical layer 3 communication</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.300000000000004%" headers="mcps1.2.4.1.3 "><p id="p55865482151326"><a name="p55865482151326"></a><a name="p55865482151326"></a>N/A</p>
    </td>
    </tr>
    <tr id="row7550850151326"><td class="cellrowborder" valign="top" width="19.61%" headers="mcps1.2.4.1.1 "><p id="p57965148151326"><a name="p57965148151326"></a><a name="p57965148151326"></a>Extension NIC</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.089999999999996%" headers="mcps1.2.4.1.2 "><p id="p64665415151326"><a name="p64665415151326"></a><a name="p64665415151326"></a>Horizontal layer 2 communication</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.300000000000004%" headers="mcps1.2.4.1.3 "><p id="p3407238151326"><a name="p3407238151326"></a><a name="p3407238151326"></a>To improve network performance, you can set the MTU of an extension NIC to <strong id="b84235270612277"><a name="b84235270612277"></a><a name="b84235270612277"></a>8888</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Up to 60 disks \(including the system disk\) can be attached to an ECS. For details about restrictions, see  [Can Multiple Disks Be Attached to an ECS?](can-multiple-disks-be-attached-to-an-ecs.md)

    An example is provided as follows:

    If you create an e1.xlarge large-memory ECS, it can be attached with up to 60 disks, where

    -   The number of system disks is 1.
    -   The number of EVS disks is at most 59.

    >![](/images/icon-note.gif) **NOTE:**   
    >The maximum number of disks attached to an existing large-memory ECS remains unchanged. To attach 60 disks, enable advanced disk. For details, see  [Enabling Advanced Disk](enabling-advanced-disk.md).  


