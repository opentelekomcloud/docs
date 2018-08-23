# Load Balancer Type<a name="en-us_elb_01_0007"></a>

ELB provides two types of load balancers: classic load balancer and enhanced load balancer. You can select an appropriate type to better fit your scenarios and requirements. Both types of load balancers can work in a public or private network.

## Classic Load Balancer<a name="section437740211821"></a>

Classic load balancers are applicable to web services with low access traffic and simple application models.

## Enhanced Load Balancer<a name="section6674613411752"></a>

Enhanced load balancers are applicable to web services with high access traffic. They forward the requests based on domain names or URLs, making request routing more flexible. Enhanced load balancers provide comprehensive Layer 7 load balancing capabilities and more powerful forwarding performance.

## Differences<a name="section566245111734"></a>

-   Application scenario

    Enhanced load balancers forward the requests based on domain names or URLs, making request routing more flexible. Therefore, they are applicable to web services with high access traffic.

    Classic load balancers are applicable to web services with low access traffic and simple application models.


-   Feature

    [Table 1](#table6357031615712)  lists the features of enhanced and classic load balancers.

    **Table  1**  Function comparison

    <a name="table6357031615712"></a><table><thead align="left"><tr id="row2772050015712"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p4504482815755"><a name="p4504482815755"></a><a name="p4504482815755"></a><strong id="b84235270693547"><a name="b84235270693547"></a><a name="b84235270693547"></a>Function</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p2475243715755"><a name="p2475243715755"></a><a name="p2475243715755"></a><strong id="b84235270693554"><a name="b84235270693554"></a><a name="b84235270693554"></a>Classic Load Balancer</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p5879037915755"><a name="p5879037915755"></a><a name="p5879037915755"></a><strong id="b8423527069361"><a name="b8423527069361"></a><a name="b8423527069361"></a>Enhanced Load Balancer</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6356639815712"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p3229821710363"><a name="p3229821710363"></a><a name="p3229821710363"></a>Public and private network load balancing</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p6601881810363"><a name="p6601881810363"></a><a name="p6601881810363"></a>Supported</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p4592404710363"><a name="p4592404710363"></a><a name="p4592404710363"></a>Supported</p>
    </td>
    </tr>
    <tr id="row895479615712"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p5841651610363"><a name="p5841651610363"></a><a name="p5841651610363"></a>Load balancing at Layer 4 and Layer 7</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p3411734710363"><a name="p3411734710363"></a><a name="p3411734710363"></a>Supported (UDP not supported for private network load balancers)</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p19691124315148"><a name="p19691124315148"></a><a name="p19691124315148"></a>Supported</p>
    </td>
    </tr>
    <tr id="row7028404153925"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p5428175710363"><a name="p5428175710363"></a><a name="p5428175710363"></a>Load balancing algorithm (round robin, least connections, and source IP hash)</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p5956993310363"><a name="p5956993310363"></a><a name="p5956993310363"></a>Supported</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p6043528110363"><a name="p6043528110363"></a><a name="p6043528110363"></a>Supported</p>
    </td>
    </tr>
    <tr id="row27107177153925"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p3390510010363"><a name="p3390510010363"></a><a name="p3390510010363"></a>Sticky session</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p6195858810363"><a name="p6195858810363"></a><a name="p6195858810363"></a>Supported</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p5258971210363"><a name="p5258971210363"></a><a name="p5258971210363"></a>Supported</p>
    </td>
    </tr>
    <tr id="row48722680155017"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1873900110363"><a name="p1873900110363"></a><a name="p1873900110363"></a>WebSocket protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p2835467010363"><a name="p2835467010363"></a><a name="p2835467010363"></a>Supported</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1502689610363"><a name="p1502689610363"></a><a name="p1502689610363"></a>Supported</p>
    </td>
    </tr>
    <tr id="row39069843155017"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1586285410363"><a name="p1586285410363"></a><a name="p1586285410363"></a>Forwarding based on domain name and URL</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p4728709610363"><a name="p4728709610363"></a><a name="p4728709610363"></a>Not supported</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p504955310363"><a name="p504955310363"></a><a name="p504955310363"></a>Supported</p>
    </td>
    </tr>
    <tr id="row47086911155017"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p2785298210363"><a name="p2785298210363"></a><a name="p2785298210363"></a>ECSs as backend servers</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p598418810363"><a name="p598418810363"></a><a name="p598418810363"></a>Supported</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1495723810363"><a name="p1495723810363"></a><a name="p1495723810363"></a>Supported</p>
    </td>
    </tr>
    <tr id="row46158875155023"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p4232997810363"><a name="p4232997810363"></a><a name="p4232997810363"></a>Access control (whitelist)</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p617616610363"><a name="p617616610363"></a><a name="p617616610363"></a>Not supported</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p3050746310363"><a name="p3050746310363"></a><a name="p3050746310363"></a>Supported</p>
    </td>
    </tr>
    <tr id="row17544173155023"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p2690725010363"><a name="p2690725010363"></a><a name="p2690725010363"></a>Standard OpenStack APIs</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p4215914510363"><a name="p4215914510363"></a><a name="p4215914510363"></a>Not supported</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p5944762210363"><a name="p5944762210363"></a><a name="p5944762210363"></a>Supported</p>
    </td>
    </tr>
    <tr id="row59281454142913"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1492825413296"><a name="p1492825413296"></a><a name="p1492825413296"></a>BMSs as backend servers</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p392855416299"><a name="p392855416299"></a><a name="p392855416299"></a>Not supported</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p38512179378"><a name="p38512179378"></a><a name="p38512179378"></a>Supported</p>
    </td>
    </tr>
    <tr id="row146501817105312"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p5651151725313"><a name="p5651151725313"></a><a name="p5651151725313"></a>SNI for certificates</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p166511617175313"><a name="p166511617175313"></a><a name="p166511617175313"></a>Supported</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p13652121775314"><a name="p13652121775314"></a><a name="p13652121775314"></a>Not supported</p>
    </td>
    </tr>
    <tr id="row14422449125319"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1442216491533"><a name="p1442216491533"></a><a name="p1442216491533"></a>SSL protocol and SSL encryption algorithms</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p114222490532"><a name="p114222490532"></a><a name="p114222490532"></a>Supported</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p242217497533"><a name="p242217497533"></a><a name="p242217497533"></a>Not supported</p>
    </td>
    </tr>
    <tr id="row68631143155616"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p10863124311562"><a name="p10863124311562"></a><a name="p10863124311562"></a>SSL protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p38631743165611"><a name="p38631743165611"></a><a name="p38631743165611"></a>Supported</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p58635433562"><a name="p58635433562"></a><a name="p58635433562"></a>Not supported</p>
    </td>
    </tr>
    <tr id="row1383115695416"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p128311656205420"><a name="p128311656205420"></a><a name="p128311656205420"></a>OBS storage for access logs</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1783155615415"><a name="p1783155615415"></a><a name="p1783155615415"></a>Supported</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p92481516105516"><a name="p92481516105516"></a><a name="p92481516105516"></a>Not supported</p>
    </td>
    </tr>
    <tr id="row257915119235"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p15580612236"><a name="p15580612236"></a><a name="p15580612236"></a>Weight assigned for ECSs</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p196781017236"><a name="p196781017236"></a><a name="p196781017236"></a>Not supported</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1058010132314"><a name="p1058010132314"></a><a name="p1058010132314"></a>Supported</p>
    </td>
    </tr>
    </tbody>
    </table>


