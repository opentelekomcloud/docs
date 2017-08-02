## Large-Memory ECSs

### Overview

Large-memory ECSs provide an even larger amount of memory than memory-optimized
ECSs. They are used for applications that require a large amount of memory,
rapid data switching, low latency, and process large volumes of data.

### Specifications

**Table 1-1** Large-memory e1 ECS specifications
<table>
      <tr>
         <th>ECS Type</th>
         <th>vCPUs</th>
         <th>Memory (RAM in GB)</th>
         <th>Flavor</th>
      </tr>
      <tr>
         <td rowspan="4">Large-memory</td>
         <td>4</td>
         <td>128</td>
         <td>e1.xlarge</td>
      </tr>
      <tr>
         <td>8</td>
         <td>256</td>
         <td>e1.2xlarge</td>
      </tr>
      <tr>
         <td>16</td>
         <td>470</td>
         <td>e1.4xlarge</td>
      </tr>
      <tr>
         <td>32</td>
         <td>940</td>
         <td>e1.8xlarge</td>
      </tr>
</table>
<b>Table 1-2</b> Large-memory e2 ECS specifications
<table>
      <tr>
         <th>Category</th>
         <th>vCPUs</th>
         <th>Memory (RAM in GB)</th>
         <th>Flavor</th>
      </tr>
      <tr>
         <td rowspan=4>Large-memory</td>
         <td>8</td>
         <td>128</td>
         <td>e2.2xlarge</td>
      </tr>
      <tr>
         <td>12</td>
         <td>256</td>
         <td>e2.3xlarge</td>
      </tr>
      <tr>
         <td>18</td>
         <td>445</td>
         <td>e2.4xlarge</td>
      </tr>
      <tr>
         <td>36</td>
         <td>890</td>
         <td>e2.9xlarge</td>
      </tr>
</table>

### Features

Enhanced SR-IOV network performance.

### Notes
<ul>
<li>Large-memory ECSs do not support NIC hot swapping.</li>
<li>Large-memory ECSs support the following OSs:
<ul>
<li>Windows 2016 DataCenter 64bit</li>
<li>Windows 2012 Standard 64bit</li>
<li>Windows 2012 Datacenter 64bit</li>
<li>Windows 2012 R2 Datacenter 64bit</li>
<li>Windows 2012 R2 Standard 64bit</li>
<li>Windows 2012 R2 Essentials 64bit</li>
<li>CentOS 7.3 64bit</li>
<li>CentOS 7.2 64bit</li>
<li>CentOS 7.1 64bit</li>
<li>CentOS 7.0 64bit</li>
<li>CentOS 6.8 64bit</li>
<li> CentOS 6.7 64bit</li>
<li>CentOS 6.6 64bit</li>
<li>CentOS 6.5 64bit</li>
<li>CentOS 6.4 64bit</li>
<li>CentOS 6.3 64bit</li>
<li>Debian 8.0 64bit</li>
<li>Debian 8.4 64bit</li>
<li>Debian 8.5 64bit</li>
<li>Debian 8.6 64bit</li>
<li>Debian 8.7 64bit</li>
<li>OpenSUSE 42.2 64bit</li>
<li>Ubuntu Server 16.10 64bit</li>
<li>Ubuntu Server 16.04 64bit</li>
<li>SUSE Linux Enterprise Server 11 SP3 64bit</li>
<li>SUSE Linux Enterprise Server 11 SP4 64bit</li>
<li>SUSE Linux Enterprise Server 12 64bit</li>
<li>SUSE Linux Enterprise Server 12 SP1 64bit</li>
<li>SUSE Linux Enterprise Server 12 SP2 64bit</li>
<li>RedHat Linux Enterprise 6.8 64bit</li>
<li>RedHat Linux Enterprise 7.0 64bit</li>
<li>RedHat Linux Enterprise 7.2 64bit</li>
<li>RedHat Linux Enterprise 7.3 64bit</li>
<li>Fedora 25 64bit</li>
<li>Oracle Enterprise Linux 6.8 64bit</li>
<li>Oracle Enterprise Linux 7.3 64bit</li>
<li>EulerOS 2.2 64bit</li>
</ul>
<li>The primary and extended NICs of a large-memory ECS have specified
application scenarios. For details, see <b><a href="#tips">Table 1-3</a></b>.</li>

<b><a name="tips">Table 1-3</a></b> Application scenarios of the primary and extended NICs of a large-memory ECS
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
<li>A large-memory ECS can have up to 40 disks attached.
<dd>An example is provided as follows:
If you create an e1.xlarge large-memory ECS, it can have up to 40 disks
attached, where
<ul>
<li>The number of system disks is 1.</li>
<li>The number of EVS disks is at most 39.</li></ul></ul></ul>
  
