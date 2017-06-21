## Disk-intensive ECSs

### Overview

Disk-intensive ECSs use local storage and provide high network performance. They
are purpose-built for applications that require high IOPS and fast data
processing, such as distributed Hadoop computing and the processing of large
volumes of concurrent data and logs.

### Specifications

**Table 1-1** Disk-intensive d1 ECS specifications
<table>
      <tr>
         <th>ECS Type</th>
         <th>vCPUs</th>
         <th>Memory (RAM in GB)</th>
         <th>Flavor</th>
         <th>Local Disks</th>
         <th>Capacity of One Local Disk</th>
     </tr>
     <tr>
         <td rowspan="4">Disk-intensive</td>
         <td>4</td>
         <td>32</td>
         <td>d1.xlarge</td>
         <td>3</td>
         <td>1,800 GB</td>
     </tr>
     <tr>
         <td>8</td>
         <td>64</td>
         <td>d1.2xlarge</td>
         <td>6</td>
         <td>1,800 GB</td>
     </tr> 
     <tr>
         <td>16</td>
         <td>128</td>
         <td>d1.4xlarge</td>
         <td>12</td>
         <td>1,800 GB</td>
     </tr> 
     <tr>
         <td>36</td>
         <td>256</td>
         <td>d1.8xlarge</td>
         <td>24</td>
         <td>1,800 GB</td>
     </tr>
</table>

### Features

Disk-intensive ECSs have the following features:

-   HDD-based data storage
-   Enhanced SR-IOV network performance. On disk-intensive ECSs, SR-IOV is enabled by default, providing high PPS performance and low network jitter and latency.
-   Up to 24 local disks, 36 vCPUs, and 256 GB memory capacity

### Notes
<ul>
<li>Disk-intensive ECSs do not support NIC hot swapping.</li>
<li>Disk-intensive ECSs do not support changing specifications.</li>
<li>Disk-intensive ECSs do not support OS reinstallation or change.</li>
<li>Disk-intensive ECSs support the following OSs:
<ul>
<li>Windows 2016 DataCenter 64bit</li>
<li>Windows 2012 Standard 64bit</li>
<li>Windows 2012 Datacenter 64bit</li>
<li>Windows 2012 R2 Datacenter 64bit</li>
<li> Windows 2012 R2 Standard 64bit</li>
<li>Windows 2012 R2 Essentials 64bit</li>
<li>Windows 2008 R2 Datacenter 64bit</li>
<li>Windows 2008 R2 Enterprise 64bit</li>
<li>Windows 2008 WEB R2 64bit</li>
<li>Windows 2008 R2 Standard 64bit</li>
<li>Windows 2008 R2 SP1 Enterprise 64bit</li>
<li>CentOS 7.3 64bit</li>
<li>CentOS 7.2 64bit</li>
<li>CentOS 7.1 64bit</li>
<li>CentOS 7.0 64bit</li>
<li>CentOS 6.8 64bit</li>
<li>CentOS 6.7 64bit</li>
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
<li>CoreOS 1185.5.0 64bit</li>
<li>EulerOS 2.2 64bit</li><ul></li>
<li>The primary and extended NICs of a disk-intensive ECS have specified application scenarios. For details, see <b>[Table 1-2](#jump)</b>.
<dd><b><span id="jump">Table 1-2</span></b> Application scenarios of primary and extended NICs of a disk-intensive ECS
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
         <td>To improve network performance, you can set the MTU of the extended NIC to 8888.</td>
      </tr>
</table>
<li>Disk-intensive ECSs can use both local disks and EVS disks to store data. Use restrictions on the two types of storage media are as follows:
<ul>
<li>Only an EVS disk, not a local disk, can be used as the system disk of a disk-intensive ECS.</li>
<li>Both an EVS disk and a local disk can be used as the data disk of a disk-intensive ECS.</li>
<li>A disk-intensive ECS can have up to 28 disks attached.
<dd>The system disk of an ECS uses one mount point. Therefore, an ECS can have up to 27 data disks attached. The total sum of 27 includes the number of EVS disks and the number of local disks.</dd>
<dd>For example, if you create a d1.xlarge disk-intensive ECS, it can have up to 28 disks attached, where
<ul>
<li>The number of system disks is 1.</li>
<li>The number of local disks is 3.</li>
<li>The number of EVS disks is at most 24.</li></dd></ul>
</li></li></ul>
