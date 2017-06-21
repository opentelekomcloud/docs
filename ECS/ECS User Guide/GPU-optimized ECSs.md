## GPU-optimized ECSs

### Overview

GPU-optimized ECSs are classified as g1 and g2 ECSs:

-   GPU-optimized g1 ECSs are based on NVIDIA Tesla M60 hardware virtualization and provide economical graphics acceleration with a maximum of 1 GB video RAM and 4,096 x 2,160 resolution. They support DirectX and OpenGL and are used for applications that require high performance in graphics rendering.
-   GPU-optimized g2 ECSs are based on NVIDIA Tesla M60 hardware passthrough and provide graphics acceleration and single-precision computing with a maximum of 8 GB video RAM and 4,096 x 2,160 resolution. They support DirectX, OpenGL, CUDA, and OpenCL, provide 2,048 CUDA cores, and are used for media editing, 3D rendering, and transcoding.

Select a type based on service requirements.

### Specifications

**Table 1-1** GPU-optimized g1 ECS specifications
<table>
      <tr>
         <th>ECS Type</th>
         <th>vCPUs</th>
         <th>Memory (RAM in GB)</th>
         <th>Flavor</th>
         <th>GPUs</th>
         <th>GPU Type</th>
      </tr>
      <tr>
         <td rowspan="2">GPU-optimized</td>
         <td>4</td>
         <td>8</td>
         <td>g1.xlarge</td>
         <td>1</td>
         <td>M60-1Q</td>
      </tr>
      <tr>
         <td>8</td>
         <td>16</td>
         <td>g1.2xlarge</td>
         <td>1</td>
         <td>M60-1Q</td>
      </tr>
</table>     

**Table 1-2** GPU-optimized g2 ECS specifications
<table>
      <tr>
         <th>ECS Type</th>
         <th>vCPUs</th>
         <th>Memory (RAM in GB)</th>
         <th>Flavor</th>
         <th>GPUs</th>
         <th>GPU Type</th>
      </tr>
      <tr>
         <td>GPU-optimized</td>
         <td>8</td>
         <td>64</td>
         <td>g2.2xlarge</td>
         <td>1</td>
         <td>M60</td>
      </tr>
</table>

### Features
<ul>
<li>GPU-optimized g1 ECSs have the following features:
<ul>
<li>NVIDIA M60 GPUs</li>
<li>Graphics acceleration applications</li>
<li>GPU hardware virtualization (vGPUs)</li>
<li>Application flow identical to common ECSs</li>
<li>Automatic scheduling of GPU-optimized g1 ECSs to AZs where NVIDIA M60 GPUs are used</li>
<li>A maximum specification of 1 GB video RAM and 4,096 x 2,160 resolution for processing graphics</li></ul>
<li>GPU-optimized g2 ECSs have the following features:
<ul>
<li>NVIDIA M60 GPUs</li>
<li>Graphics acceleration applications</li>
<li>GPU hardware passthrough</li>
<li>Enhanced SR-IOV network performance and high bandwidths</li>
<li>Application flow identical to common ECSs</li>
<li>Automatic scheduling of GPU-optimized g2 ECSs to AZs where NVIDIA M60 GPUs are used</li>
<li>A maximum specification of 8 GB video RAM and 4,096 x 2,160 resolution for processing graphics</li>
<li>DirectX, OpenGL, CUDA, and OpenCL</li>
<li>Up to 2,048 CUDA cores</li></ul>
</ul>
### Notes on Using GPU-optimized g1 ECSs
<ul>
<li>GPU-optimized g1 ECSs do not support specifications change.</li>
<li>GPU-optimized g1 ECSs support the following OSs:
<ul>
<li>Windows Server 2008</li>
<li>Windows Server 2012</li>
<li>Windows Server 2016</li>
</ul>
<li>If a GPU-optimized g1 ECS is created using a private image, install a GPU driver on the ECS after the ECS creation. To download the driver, visit <a href="http://www.nvidia.com/grid-eval">http://www.nvidia.com/grid-eval</a>, set the NVIDIA GRID version to **4.1**, and select the **GRID for UVP** software package. The operations are as follows:
<ol>
<li>Click the **Archived Versions** tab.</li>
<li>Click **NVIDIA GRID** of version **4.1**.</li>
<li>On the **Product Download** page, click **GRID for UVP**.</li></ol>
<li>If you log in to a GPU-optimized g1 ECS using MSTSC, graphics acceleration will fail. This is because MSTSC replaces the WDDM GPU driver with a non-accelerated remote desktop display driver. Therefore, you must use other methods to log in to the ECS, such as VNC.
<dd>If the remote login function available on the management console fails to meet your service requirements, you must install a suitable remote login tool on the ECS.</dd></li></ul>
### Notes on Using GPU-optimized g2 ECSs
<ul>
<li>GPU-optimized g2 ECSs do not support specifications change.</li>
<li>GPU-optimized g2 ECSs support the following OSs:
<ul>
<li>Windows Server 2008</li>
<li>Windows Server 2012</li>
</ul>
<li>If a GPU-optimized g2 ECS is created using a private image, install a GPU driver during the private image creation. Otherwise, install the GPU driver after creating the ECS.
<dd>To download the GPU driver, access
<a href="http://www.nvidia.com/Download/index.aspx?lang=en-us">http://www.nvidia.com/Download/index.aspx?lang=en-us</a>. You are suggested to
select the latest CUDA toolkit version.</dd></li>
<li>If a GPU-optimized g2 ECS is created using a private image, install an SR-IOV driver during the private image creation. Otherwise, install it after the ECS is created.
<dd>To download the SR-IOV driver, access
<a href="https://downloadcenter.intel.com/search?keyword=Intel++Ethernet+Connections+CD">https://downloadcenter.intel.com/search?keyword=Intel++Ethernet+Connections+CD</a>. You are suggested to select version 20.4.1 or later.</dd>
<dd>During driver installation, if you encounter the "No Intel adapter found" error, see section <a href="How Can I Handle the Issue that a Windows 7 ECS with an Intel 82599 NIC Installed Reports an Error in SR-IOV Scenarios?">How Can I Handle the Issue that a Windows 7 ECS with an Intel 82599 NIC Installed Reports an Error in SR-IOV Scenarios?</a> for troubleshooting.</dd></li>
<li>If you log in to a GPU-optimized g2 ECS using MSTSC, graphics acceleration will fail. This is because MSTSC replaces the WDDM GPU driver with a non-accelerated remote desktop display driver. Therefore, you must use other methods to log in to the ECS, such as VNC.</li>
<li>GPU-optimized g2 ECSs do not support remote login provided by the public cloud platform. Before logging in to such an ECS using VNC, install the VNC server on the ECS.</li>
