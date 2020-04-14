# Instance Family<a name="EN-US_TOPIC_0083745258"></a>

## Overview<a name="section19818434175418"></a>

An instance is a BMS. Different instance types provide varied computing capabilities, storage space, and network performance. You can select a BMS type that suits your service requirements. 

## BMS Types<a name="section868481015595"></a>

The cloud platform provides a variety of BMS flavors. You can choose BMS flavors that best suit your needs.

-   Compute-optimized

    This type of BMS uses the SDI iNIC and supports OLTP databases with higher performance, higher memory ratio, and transactional workloads cache.

    **Table  1**  Compute-optimized BMS specifications

    <a name="table10545111565016"></a>
    <table><thead align="left"><tr id="row8550715135020"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.1"><p id="p1655381515507"><a name="p1655381515507"></a><a name="p1655381515507"></a>Flavor Name/ID</p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.2"><p id="p5553181513508"><a name="p5553181513508"></a><a name="p5553181513508"></a>CPU</p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.3"><p id="p1554715135011"><a name="p1554715135011"></a><a name="p1554715135011"></a>Memory</p>
    </th>
    <th class="cellrowborder" valign="top" width="18%" id="mcps1.2.6.1.4"><p id="p18556915115016"><a name="p18556915115016"></a><a name="p18556915115016"></a>Local Disk</p>
    </th>
    <th class="cellrowborder" valign="top" width="22%" id="mcps1.2.6.1.5"><p id="p155716150503"><a name="p155716150503"></a><a name="p155716150503"></a>Extended Configuration</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1155910156507"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.1 "><p id="p1560131514507"><a name="p1560131514507"></a><a name="p1560131514507"></a>physical.o2.medium</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="p18560191555018"><a name="p18560191555018"></a><a name="p18560191555018"></a>2 * 8 Core Intel Xeon E5-2667 V4 (3.2 GHz)</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.3 "><p id="p1545271520519"><a name="p1545271520519"></a><a name="p1545271520519"></a>256 DDR4 RAM (GB)</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.6.1.4 "><p id="p1625339185114"><a name="p1625339185114"></a><a name="p1625339185114"></a>2 * 800GB SAS SSD RAID 1 + NVMe SSD Card 1.6 TB</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.5 "><p id="p4564141518506"><a name="p4564141518506"></a><a name="p4564141518506"></a>2 x 2 * 10GE</p>
    </td>
    </tr>
    </tbody>
    </table>

-   High-performance computing

    High-performance BMSs provide a large number of CPU cores, large memory size, and high throughput. These BMSs are suitable for high-performance processor applications restricted by computing performance. This flavor uses the V5 CPU server and InfiniBand NIC to support quick BMS provisioning.

    **Table  2**  High-performance computing BMS specifications

    <a name="table562512229332"></a>
    <table><thead align="left"><tr id="row1764712225332"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.1"><p id="p16516224337"><a name="p16516224337"></a><a name="p16516224337"></a>Flavor Name/ID</p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.2"><p id="p12655142217334"><a name="p12655142217334"></a><a name="p12655142217334"></a>CPU</p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.3"><p id="p196591122123319"><a name="p196591122123319"></a><a name="p196591122123319"></a>Memory</p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.4"><p id="p4669922153320"><a name="p4669922153320"></a><a name="p4669922153320"></a>Local Disk</p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.5"><p id="p1867262216336"><a name="p1867262216336"></a><a name="p1867262216336"></a>Extended Configuration</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row13675522123311"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.1 "><p id="p76796228333"><a name="p76796228333"></a><a name="p76796228333"></a>physical.h2.large</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="p868482214333"><a name="p868482214333"></a><a name="p868482214333"></a>2 * 18 Core Intel Skylake 6151 V5 (3.0 GHz)</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.3 "><p id="p10688152253318"><a name="p10688152253318"></a><a name="p10688152253318"></a>192 DDR4 RAM (GB)</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.4 "><p id="p96941222103320"><a name="p96941222103320"></a><a name="p96941222103320"></a>1 * 1.6TB NVMe SSD</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p9699142219332"><a name="p9699142219332"></a><a name="p9699142219332"></a>1 * 100G IB + 2 * 10GE</p>
    </td>
    </tr>
    </tbody>
    </table>

-   GPU-accelerated

    GPU-accelerated BMSs provide outstanding floating-point computing capabilities. They are suitable for scenarios that require real-time, highly concurrent massive computing, such as deep learning, scientific computing, CAE, 3D animation rendering, and CAD. This flavor uses the G560 server, InfiniBand NIC, and the industry-leading NVIDIA Tesla P100 GPU and Tesla V100 GPU to provide you with excellent performance and cost-effectiveness.

    **Table  3**  GPU-accelerated BMS specifications

    <a name="table5179140713"></a>
    <table><thead align="left"><tr id="row152051413713"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.1"><p id="p121171411715"><a name="p121171411715"></a><a name="p121171411715"></a>Flavor Name/ID</p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.2"><p id="p1122111417713"><a name="p1122111417713"></a><a name="p1122111417713"></a>CPU</p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.3"><p id="p12237142712"><a name="p12237142712"></a><a name="p12237142712"></a>Memory</p>
    </th>
    <th class="cellrowborder" valign="top" width="18%" id="mcps1.2.6.1.4"><p id="p14243145710"><a name="p14243145710"></a><a name="p14243145710"></a>Local Disk</p>
    </th>
    <th class="cellrowborder" valign="top" width="22%" id="mcps1.2.6.1.5"><p id="p192471418718"><a name="p192471418718"></a><a name="p192471418718"></a>Extended Configuration</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row225914377"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.1 "><p id="p9265141716"><a name="p9265141716"></a><a name="p9265141716"></a>physical.p1.large</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="p7271814377"><a name="p7271814377"></a><a name="p7271814377"></a>2 * 14 Core Intel Xeon E5-2690 V4 (2.6 GHz)</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.3 "><p id="p15876898167"><a name="p15876898167"></a><a name="p15876898167"></a>512 DDR4 RAM (GB)</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.6.1.4 "><p id="p122819141374"><a name="p122819141374"></a><a name="p122819141374"></a>2 * 600GB SAS HDD + 6 * 800GB NVMe SSD</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.5 "><p id="p13806255111715"><a name="p13806255111715"></a><a name="p13806255111715"></a>NIC: 1 x 100 Gbit/s IB + 2 x 10GE</p>
    <p id="p82941418718"><a name="p82941418718"></a><a name="p82941418718"></a>GPU: 8 x Tesla P100</p>
    <p id="p672675017477"><a name="p672675017477"></a><a name="p672675017477"></a>Graphics card memory: 16 GB</p>
    </td>
    </tr>
    <tr id="row2029111411720"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.1 "><p id="p17305141777"><a name="p17305141777"></a><a name="p17305141777"></a>physical.p2.large</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="p83212141678"><a name="p83212141678"></a><a name="p83212141678"></a>2 * 14 Core Intel Xeon E5-2690 V4 (2.6 GHz)</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.3 "><p id="p1378910157164"><a name="p1378910157164"></a><a name="p1378910157164"></a>512 DDR4 RAM (GB)</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.6.1.4 "><p id="p133481410720"><a name="p133481410720"></a><a name="p133481410720"></a>2 * 600GB SAS HDD + 6 * 800GB NVMe SSD</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.5 "><p id="p146919146188"><a name="p146919146188"></a><a name="p146919146188"></a>NIC: 1 x 100 Gbit/s IB + 2 x 10GE</p>
    <p id="p13591411718"><a name="p13591411718"></a><a name="p13591411718"></a>GPU: 8 x Tesla V100</p>
    <p id="p122071812484"><a name="p122071812484"></a><a name="p122071812484"></a>Graphics card memory: 16 GB</p>
    </td>
    </tr>
    </tbody>
    </table>

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >physical.p1.large and physical.p2.large BMSs only support Ubuntu 16.04 and CentOS 7.4 private images.  

-   Memory-optimized

    This type of BMS has DIMM memory which has quick read and write speed and high density, and is used in SAP HANA and memory databases.

    **Table  4**  Memory-optimized BMS specifications

    <a name="table126448173512"></a>
    <table><thead align="left"><tr id="row02861487354"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.1"><p id="p629215853514"><a name="p629215853514"></a><a name="p629215853514"></a>Flavor Name/ID</p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.2"><p id="p11295118163519"><a name="p11295118163519"></a><a name="p11295118163519"></a>CPU</p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.3"><p id="p1929919815352"><a name="p1929919815352"></a><a name="p1929919815352"></a>Memory</p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.4"><p id="p1030518820351"><a name="p1030518820351"></a><a name="p1030518820351"></a>Local Disk</p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.5"><p id="p430911813516"><a name="p430911813516"></a><a name="p430911813516"></a>Extended Configuration</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row231278163520"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.1 "><p id="p1731938143514"><a name="p1731938143514"></a><a name="p1731938143514"></a>physical.m2.medium</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="p432514893519"><a name="p432514893519"></a><a name="p432514893519"></a>4 * 24 Core Broadwell EX Xeon E7-8890 V4 (2.2 GHz)</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.3 "><p id="p133301382351"><a name="p133301382351"></a><a name="p133301382351"></a>2048 DDR4 RAM (GB)</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.4 "><p id="p1433648193518"><a name="p1433648193518"></a><a name="p1433648193518"></a>2 * 600GB SAS HDD RAID 1 + 7 * 1.8TB SAS HDD RAID 5 + 2 * 1.6TB NVMe SSD Card</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p1734014873514"><a name="p1734014873514"></a><a name="p1734014873514"></a>2 x 2 * 10GE</p>
    </td>
    </tr>
    <tr id="row334214863511"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.1 "><p id="p7345178203515"><a name="p7345178203515"></a><a name="p7345178203515"></a>physical.m2.xlarge</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="p13489813358"><a name="p13489813358"></a><a name="p13489813358"></a>4 * 24 Core Broadwell EX Xeon E7-8890 V4 (2.2 GHz)</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.3 "><p id="p153571088354"><a name="p153571088354"></a><a name="p153571088354"></a>4096 DDR4 RAM (GB)</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.4 "><p id="p9360985357"><a name="p9360985357"></a><a name="p9360985357"></a>2 * 600GB SAS HDD RAID 1 + 14 * 1.8TB SAS HDD RAID 50 + 2 * 1.6TB NVMe SSD Card</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p203644823519"><a name="p203644823519"></a><a name="p203644823519"></a>2 x 2 * 10GE</p>
    </td>
    </tr>
    </tbody>
    </table>


