## High-Performance ECSs

### Overview

High-performance h1 ECSs provide a large number of CPU cores, large memory size,
and high throughput. These ECSs are suitable for high-performance processor
applications restricted by computing performance.

High-performance h2 ECSs are designed to meet high end computational needs, such
as molecular modeling and computational fluid dynamics. In addition to the
substantial CPU power, the high-performance h2 ECSs offer diverse options for
low latency RDMA networking using FDR InfiniBand and several memory
configurations to support memory-intensive computational requirements.

### Specifications

**Table 1-1** High-performance first-generation h1 ECS specifications
<table>
      <tr>
         <th>ECS Type</th>
         <th>vCPUs</th>
         <th>Memory (RAM in GB)</th>
         <th>Flavor</th>
      </tr>
      <tr>
          <td rowspan="15">High-performance</td>
          <td>2</td>
          <td>4</td>
          <td>h1.large</td>
      </tr>
      <tr>
          <td>4</td>
          <td>8</td>
          <td>h1.xlarge</td>
      </tr>
      <tr>
          <td>8</td>
          <td>16</td>
          <td>h1.2xlarge</td>
      </tr>
      <tr>
          <td>16</td>
          <td>32</td>
          <td>h1.4xlarge</td>
      </tr>
      <tr>
          <td>32</td>
          <td>64</td>
          <td>h1.8xlarge</td>
      </tr>
      <tr>
          <td>2</td>
          <td>8</td>
          <td>h1.large.4</td>
      </tr>
      <tr>
          <td>4</td>
          <td>16</td>
          <td>h1.xlarge.4</td>
      </tr>
      <tr>
          <td>8</td>
          <td>32</td>
          <td>h1.2xlarge.4</td>
      </tr>
      <tr>
          <td>16</td>
          <td>64</td>
          <td>h1.4xlarge.4</td>
      </tr>
      <tr>
          <td>32</td>
          <td>128</td>
          <td>h1.8xlarge.4</td>
      </tr>
      <tr>
          <td>2</td>
          <td>16</td>
          <td>h1.large.8</td>
      </tr>
      <tr>
          <td>4</td>
          <td>32</td>
          <td>h1.xlarge.8</td>
      </tr>
      <tr>
          <td>8</td>
          <td>64</td>
          <td>h1.2xlarge.8</td>
      </tr>
      <tr>
          <td>16</td>
          <td>128</td>
          <td>h1.4xlarge.8</td>
      </tr>
      <tr>
          <td>32</td>
          <td>256</td>
          <td>h1.8xlarge.8</td>
      </tr>
</table>

**Table 1-2** High-performance second-generation h2 ECS specifications
<table>
      <tr>
         <th>ECS Type</th>
         <th>vCPUs</th>
         <th>Memory (RAM in GB)</th>
         <th>Flavor Name</th>
         <th>Local Disks</th>
         <th>Capacity of One Local Disk (TB)</th>
      </tr>
      <tr>
          <td rowspan="2">High-performance</td>
          <td>12</td>
          <td>128</td>
          <td>h2.3xlarge.10</td>
          <td>1</td>
          <td>3.2</td>
      </tr>
      <tr>
          <td>12</td>
          <td>256</td>
          <td>h2.3xlarge.20</td>
          <td>1</td>
          <td>3.2</td>
      </tr>
</table>
### Features

High-performance ECSs have the following features:

-   Large memory capacity and more processor cores than other types of ECSs
-   Up to 32 vCPUs
-   High-performance h2 ECSs use InfiniBand NICs that provide a bandwidth of 100 Gbit/s.

### Notes on Using High-Performance h1 ECSs
<ul>
<li>High-performance h1 ECSs do not support NIC hot swapping.</li>
<li>High-performance h1 ECSs support changing specifications only if the source and target ECSs are of the same type.</li>
<li>High-performance h1 ECSs support the following OSs:
<ul>
<li>CentOS 6.8 64bit</li>
<li>CentOS 7.2 64bit</li>
<li>CentOS 7.3 64bit</li>
<li>Windows Server 2008</li>
<li>Windows Server 2012</li>
<li>Windows Server 2016</li>
<li>SUSE Enterprise Linux Server 11 SP3 64bit</li>
<li>SUSE Enterprise Linux Server 11 SP4 64bit</li>
<li>SUSE Enterprise Linux Server 12 SP1 64bit</li>
<li>SUSE Enterprise Linux Server 12 SP2 64bit</li>
<li>Red Hat Enterprise Linux 6.8 64bit</li>
<li>Red Hat Enterprise Linux 7.3 64bit</li>
</ul>
<li>The primary and extended NICs of a high-performance h1 ECS have specified application scenarios. For details, see the following table.
<dd><b>Table 1-3</b> Application scenarios of the primary and extended NICs of a high-performance h1 ECS<dd>
<table>
      <tr>
         <th>NIC Type</th>
         <th>Application Scenario</th>
         <th>Remarks</th>
      </tr>
      <tr>
         <td>Primary NIC</td>
         <td>Applies to vertical layer 3 communication.</td>
         <td>N/A</td>
      </tr>
      <tr>
         <td>Extended NIC</td>
         <td>Applies to horizontal layer 2 communication.</td>
         <td>To improve network performance, you can set the MTU of the extended NIC to <b>8888</b>.</td>
      </tr>
</table>
### Notes on Using High-Performance h2 ECSs
<ul>
<li>High-performance h2 ECSs do not support OS reinstallation or change.</li>
<li>High-performance h2 ECSs do not support specifications change.</li>
<li>High-performance h2 ECSs cannot be used to create an image.</li>
<li>High-performance h2 ECSs do not support cold migration, live migration, or HA.</li>
<li>High-performance h2 ECSs support the following OSs:
<ul>
<li>CentOS 6.5 64bit</li>
<li>CentOS 7.2 64bit</li>
<li>SUSE Linux Enterprise Server 11 SP4 64bit</li>
<li>Red Hat Enterprise Linux 7.2 64bit</li></ul>
<li>High-performance h2 ECSs use InfiniBand NICs that provide a bandwidth of 100 Gbit/s.</li>
<li>High-performance h2 ECSs use PCIe 3.2 TB SSD cards for temporary local storage.</li>
<li>If a high-performance h2 ECS is created using a private image, install an InfiniBand NIC driver on the ECS after the ECS creation following the instructions provided by Mellanox. Before installing the driver, download a required driver version at the Mellanox official website based on the InfiniBand NIC type.
<ul>
<li>InfiniBand NIC type: **Mellanox Technologies ConnectX-4 Infiniband HBA(MCX455A-ECAT)**</li>
<li>Mellanox official website: <a href="http://www.mellanox.com/">http://www.mellanox.com/</a></li></ul>
<li>After you delete a high-performance h2 ECS, the data stored in SSD disks is automatically cleared. Therefore, do not store persistence data into SSD disks during ECS running.</li></ul>

### Related Links

<a href="Improving the Performance of Memory-optimized m2 and High-Performance h2 ECSs">Improving the Performance of Memory-optimized m2 and High-Performance h2 ECSs</a>

<a href="How Can I Check Whether the Network Communication Between Two ECSs
Equipped with an InfiniBand NIC Driver Is Normal?">How Can I Check Whether the Network Communication Between Two ECSs Equipped with an InfiniBand NIC Driver Is Normal?</a>
