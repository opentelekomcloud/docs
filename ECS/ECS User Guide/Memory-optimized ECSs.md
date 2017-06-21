## Memory-optimized ECSs

### Overview

Memory-optimized m1 ECSs have a large memory size and provide high memory
performance. They are designed for memory-intensive applications that process a
large amount of data, such as precision advertising, e-commerce big data
analysis, and IoV big data analysis.

Memory-optimized m2 ECSs are designed for memory-optimized applications and
apply to the following scenarios:

-   High performance relational (MySQL) and NoSQL (MongoDB, Cassandra) databases
-   Distributed web scale cache stores that provide in-memory caching of
    key-value type data (Memcached and Redis)
-   Applications performing real-time processing of big unstructured data
    (financial services, Hadoop/Spark clusters)
-   High-performance computing (HPC) and Electronic Design Automation (EDA)

### Specifications

**Table 1-1** Memory-optimized first-generation m1 ECS specifications
<table>
      <tr>
          <th>ECS Type</th>
          <th>vCPUs</th>
          <th>Memory (RAM in GB)</th>
          <th>Flavor</th>
      </tr> 
      <tr>
          <td rowspan="5">Memory-optimized</td>
          <td>1</td>
          <td>8</td>
          <td>m1.medium</td>
      </tr>
      <tr>
          <td>2</td>
          <td>16</td>
          <td>m1.large</td>
      </tr>
      <tr>
          <td>4</td>
          <td>32</td>
          <td>m1.xlarge</td>
      </tr>
      <tr>
          <td>8</td>
          <td>64</td>
          <td>m1.2xlarge</td>
      </tr>
      <tr>
          <td>16</td>
          <td>128</td>
          <td>m1.4xlarge</td>
      </tr>
</table>
**Table 1-2** Memory-optimized second-generation m2 ECS specifications
<table>
      <tr>
          <th>ECS Type</th>
          <th>vCPUs</th>
          <th>Memory (RAM in GB)</th>
          <th>Flavor</th>
      </tr> 
      <tr>
          <td>Memory-optimized</td>
          <td>32</td>
          <td>256</td>
          <td>m2.8xlarge.8</td>
      </tr>
</table>

### Notes
<ul>
<li>Memory-optimized m2 ECSs do not have InfiniBand or SSD NICs configured.</li>
<li>Only the memory-optimized m2 ECSs of the same type support flavor change.
However, the memory-optimized m2 ECSs in the current version support only
one flavor.</li>
<li>Memory-optimized m2 ECSs support the following OSs:
<ul>
<li>CentOS 7.2 64bit</li>
<li>CentOS 6.5 64bit</li>
<li>SUSE Linux Enterprise Server 11 SP4 64bit</li>
<li>Red Hat Enterprise Linux 7.2 64bit</li>
<li>Windows 2012DC edition</li></ul>

### Related Links

<a href="Improving the Performance of Memory-optimized m2 and High-Performance h2 ECSs">Improving the Performance of Memory-optimized m2 and High-Performance h2 ECSs</a>
