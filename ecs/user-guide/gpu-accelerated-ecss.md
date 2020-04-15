# GPU-accelerated ECSs<a name="EN-US_TOPIC_0097289624"></a>

GPU-accelerated ECSs provide outstanding floating-point computing capabilities. They are suitable for applications that require real-time, highly concurrent massive computing.

GPU-accelerated ECSs are classified as graphics-accelerated \(G series\) and computing-accelerated \(P series\) ECSs.

-   G series of ECSs are suitable for 3D animation rendering and CAD.
-   P series of ECSs are designed for deep learning, scientific computing, and CAE.

## GPU-accelerated ECS Types<a name="section106800321171"></a>

G and P series of ECSs are as follows:

-   G series
    -   [Graphics-accelerated Enhancement G6](#section131302034104515)
    -   [Graphics-accelerated G2](#section19580124512184)
    -   [Graphics-accelerated G1](#section013611544538)

-   P series
    -   [Computing-accelerated P2v](#section208472383415)
    -   [Computing-accelerated P2](#section5477185118234)
    -   [Computing-accelerated P1](#section1124594913391)


Helpful links:

-   [Installing a GRID/vGPU Driver on a GPU-accelerated ECS](installing-a-grid-vgpu-driver-on-a-gpu-accelerated-ecs.md)
-   [Installing the NVIDIA GPU Driver and CUDA Toolkit on a P2v ECS](installing-the-nvidia-gpu-driver-and-cuda-toolkit-on-a-p2v-ecs.md)
-   [Installing the NVIDIA GPU Driver and CUDA Toolkit on a P1 ECS](installing-the-nvidia-gpu-driver-and-cuda-toolkit-on-a-p1-ecs.md)
-   [Installing the NVIDIA GPU Driver and CUDA Toolkit on a P2 ECS](installing-the-nvidia-gpu-driver-and-cuda-toolkit-on-a-p2-ecs.md)

## Graphics-accelerated Enhancement G6<a name="section131302034104515"></a>

**Overview**

G6 ECSs use NVIDIA Tesla T4 GPUs to support DirectX, OpenGL, and Vulkan and provide 16 GB of GPU memory. The theoretical Pixel rate is 101.8 GPixel/s and Texture rate 254.4 GTexel/s, meeting professional graphics processing requirements.

Select your desired GPU-accelerated ECS type and specifications.

**Specifications**

**Table  1**  G6 ECS specifications

<a name="table19812808468"></a>
<table><thead align="left"><tr id="row2022219194610"><th class="cellrowborder" valign="top" width="11.538846115388461%" id="mcps1.2.10.1.1"><p id="p1722211115468"><a name="p1722211115468"></a><a name="p1722211115468"></a>Flavor</p>
</th>
<th class="cellrowborder" valign="top" width="10.188981101889812%" id="mcps1.2.10.1.2"><p id="p8222319467"><a name="p8222319467"></a><a name="p8222319467"></a>vCPUs</p>
</th>
<th class="cellrowborder" valign="top" width="11.808819118088191%" id="mcps1.2.10.1.3"><p id="p12221017468"><a name="p12221017468"></a><a name="p12221017468"></a>Memory (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="15.008499150084992%" id="mcps1.2.10.1.4"><p id="p142224124616"><a name="p142224124616"></a><a name="p142224124616"></a>Maximum/Assured Bandwidth (Gbit/s)</p>
</th>
<th class="cellrowborder" valign="top" width="10.20897910208979%" id="mcps1.2.10.1.5"><p id="p13223519464"><a name="p13223519464"></a><a name="p13223519464"></a>Max. PPS (10,000)</p>
</th>
<th class="cellrowborder" valign="top" width="9.959004099590041%" id="mcps1.2.10.1.6"><p id="p152235144616"><a name="p152235144616"></a><a name="p152235144616"></a>NIC Multi-Queue</p>
</th>
<th class="cellrowborder" valign="top" width="9.27907209279072%" id="mcps1.2.10.1.7"><p id="p622316134614"><a name="p622316134614"></a><a name="p622316134614"></a>GPUs</p>
</th>
<th class="cellrowborder" valign="top" width="11.61883811618838%" id="mcps1.2.10.1.8"><p id="p1622371174619"><a name="p1622371174619"></a><a name="p1622371174619"></a>GPU Memory (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="10.388961103889612%" id="mcps1.2.10.1.9"><p id="p122311204617"><a name="p122311204617"></a><a name="p122311204617"></a>Virtualization Type</p>
</th>
</tr>
</thead>
<tbody><tr id="row1222371184610"><td class="cellrowborder" valign="top" width="11.538846115388461%" headers="mcps1.2.10.1.1 "><p id="p132236154613"><a name="p132236154613"></a><a name="p132236154613"></a>G6.10xlarge.7</p>
</td>
<td class="cellrowborder" valign="top" width="10.188981101889812%" headers="mcps1.2.10.1.2 "><p id="p32231518466"><a name="p32231518466"></a><a name="p32231518466"></a>40</p>
</td>
<td class="cellrowborder" valign="top" width="11.808819118088191%" headers="mcps1.2.10.1.3 "><p id="p1122315110466"><a name="p1122315110466"></a><a name="p1122315110466"></a>280</p>
</td>
<td class="cellrowborder" valign="top" width="15.008499150084992%" headers="mcps1.2.10.1.4 "><p id="p622319118461"><a name="p622319118461"></a><a name="p622319118461"></a>25/15</p>
</td>
<td class="cellrowborder" valign="top" width="10.20897910208979%" headers="mcps1.2.10.1.5 "><p id="p182232120462"><a name="p182232120462"></a><a name="p182232120462"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="9.959004099590041%" headers="mcps1.2.10.1.6 "><p id="p72231210467"><a name="p72231210467"></a><a name="p72231210467"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="9.27907209279072%" headers="mcps1.2.10.1.7 "><p id="p222316110461"><a name="p222316110461"></a><a name="p222316110461"></a>1 x T4</p>
</td>
<td class="cellrowborder" valign="top" width="11.61883811618838%" headers="mcps1.2.10.1.8 "><p id="p1422319114469"><a name="p1422319114469"></a><a name="p1422319114469"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="10.388961103889612%" headers="mcps1.2.10.1.9 "><p id="p12238115460"><a name="p12238115460"></a><a name="p12238115460"></a>KVM</p>
</td>
</tr>
<tr id="row13223141144610"><td class="cellrowborder" valign="top" width="11.538846115388461%" headers="mcps1.2.10.1.1 "><p id="p162230174616"><a name="p162230174616"></a><a name="p162230174616"></a>G6.20xlarge.7</p>
</td>
<td class="cellrowborder" valign="top" width="10.188981101889812%" headers="mcps1.2.10.1.2 "><p id="p12249164611"><a name="p12249164611"></a><a name="p12249164611"></a>80</p>
</td>
<td class="cellrowborder" valign="top" width="11.808819118088191%" headers="mcps1.2.10.1.3 "><p id="p1022411120467"><a name="p1022411120467"></a><a name="p1022411120467"></a>560</p>
</td>
<td class="cellrowborder" valign="top" width="15.008499150084992%" headers="mcps1.2.10.1.4 "><p id="p32241010463"><a name="p32241010463"></a><a name="p32241010463"></a>30/30</p>
</td>
<td class="cellrowborder" valign="top" width="10.20897910208979%" headers="mcps1.2.10.1.5 "><p id="p1522416110468"><a name="p1522416110468"></a><a name="p1522416110468"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9.959004099590041%" headers="mcps1.2.10.1.6 "><p id="p1922413118464"><a name="p1922413118464"></a><a name="p1922413118464"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="9.27907209279072%" headers="mcps1.2.10.1.7 "><p id="p13224181164612"><a name="p13224181164612"></a><a name="p13224181164612"></a>2 x T4</p>
</td>
<td class="cellrowborder" valign="top" width="11.61883811618838%" headers="mcps1.2.10.1.8 "><p id="p422401104615"><a name="p422401104615"></a><a name="p422401104615"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="10.388961103889612%" headers="mcps1.2.10.1.9 "><p id="p922415174612"><a name="p922415174612"></a><a name="p922415174612"></a>KVM</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>A G6.10xlarge.7 ECS exclusively uses a T4 GPU for professional graphics acceleration. Such an ECS can be used for heavy-load CPU inference.  

**G6 ECS Features**

-   Graphics acceleration APIs
    -   DirectX 12, Direct2D, DirectX Video Acceleration \(DXVA\)
    -   OpenGL 4.5
    -   Vulkan 1.0

-   CUDA\* and OpenCL
-   NVIDIA T4 GPUs
-   Graphics acceleration applications
-   Heavy-load CPU inference
-   Application flow identical to common ECSs
-   Automatic scheduling of G6 ECSs to AZs where NVIDIA T4 GPUs are used
-   One built-in NVENC and two NVDEC GPUs

**Supported Common Software**

G6 ECSs are used in graphics acceleration scenarios, such as video rendering, cloud desktop, and 3D visualization. If the software relies on GPU DirectX and OpenGL hardware acceleration, use G6 ECSs. G6 ECSs support the following commonly used graphics processing software:

-   AutoCAD
-   3DS MAX
-   MAYA
-   Agisoft PhotoScan
-   ContextCapture

**Notes**

-   G6 ECSs support specifications modification.
-   G6 ECSs support the following OS:
    -   Windows Server 2016 Standard 64bit


## Graphics-accelerated G2<a name="section19580124512184"></a>

**Overview**

G2 ECSs are based on NVIDIA Tesla M60 hardware passthrough and provide graphics acceleration and single-precision computing with up to 8 GB of GPU memory and 4,096 x 2,160 resolution. They support DirectX, OpenGL, CUDA, and OpenCL, provide 2,048 CUDA cores, and are used for media editing, 3D rendering, and transcoding.

**Specifications**

**Table  2**  G2 ECS specifications

<a name="table763065410199"></a>
<table><thead align="left"><tr id="row147011547195"><th class="cellrowborder" valign="top" width="17.028297170282972%" id="mcps1.2.8.1.1"><p id="p071210544195"><a name="p071210544195"></a><a name="p071210544195"></a>ECS Type</p>
</th>
<th class="cellrowborder" valign="top" width="12.37876212378762%" id="mcps1.2.8.1.2"><p id="p17305541192"><a name="p17305541192"></a><a name="p17305541192"></a>vCPUs</p>
</th>
<th class="cellrowborder" valign="top" width="12.568743125687432%" id="mcps1.2.8.1.3"><p id="p274335411192"><a name="p274335411192"></a><a name="p274335411192"></a>Memory (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="15.218478152184781%" id="mcps1.2.8.1.4"><p id="p175718549196"><a name="p175718549196"></a><a name="p175718549196"></a>Flavor</p>
</th>
<th class="cellrowborder" valign="top" width="19.26807319268073%" id="mcps1.2.8.1.5"><p id="p157667546193"><a name="p157667546193"></a><a name="p157667546193"></a>Virtualization Type</p>
</th>
<th class="cellrowborder" valign="top" width="10.54894510548945%" id="mcps1.2.8.1.6"><p id="p1777855410191"><a name="p1777855410191"></a><a name="p1777855410191"></a>GPUs</p>
</th>
<th class="cellrowborder" valign="top" width="12.988701129887009%" id="mcps1.2.8.1.7"><p id="p17871054121910"><a name="p17871054121910"></a><a name="p17871054121910"></a>GPU Memory (GB)</p>
</th>
</tr>
</thead>
<tbody><tr id="row3800454161918"><td class="cellrowborder" valign="top" width="17.028297170282972%" headers="mcps1.2.8.1.1 "><p id="p7813175413191"><a name="p7813175413191"></a><a name="p7813175413191"></a>Accelerated graphics processing G2</p>
</td>
<td class="cellrowborder" valign="top" width="12.37876212378762%" headers="mcps1.2.8.1.2 "><p id="p98231254151912"><a name="p98231254151912"></a><a name="p98231254151912"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="12.568743125687432%" headers="mcps1.2.8.1.3 "><p id="p283475415197"><a name="p283475415197"></a><a name="p283475415197"></a>64</p>
</td>
<td class="cellrowborder" valign="top" width="15.218478152184781%" headers="mcps1.2.8.1.4 "><p id="p178467542191"><a name="p178467542191"></a><a name="p178467542191"></a>g2.2xlarge</p>
</td>
<td class="cellrowborder" valign="top" width="19.26807319268073%" headers="mcps1.2.8.1.5 "><p id="p11862105411919"><a name="p11862105411919"></a><a name="p11862105411919"></a>Xen</p>
</td>
<td class="cellrowborder" valign="top" width="10.54894510548945%" headers="mcps1.2.8.1.6 "><p id="p78752540196"><a name="p78752540196"></a><a name="p78752540196"></a>1 x M60</p>
</td>
<td class="cellrowborder" valign="top" width="12.988701129887009%" headers="mcps1.2.8.1.7 "><p id="p1288885421919"><a name="p1288885421919"></a><a name="p1288885421919"></a>8</p>
</td>
</tr>
</tbody>
</table>

**G2 ECS Features**

-   NVIDIA M60 GPUs
-   Graphics acceleration applications
-   GPU hardware passthrough
-   Enhanced SR-IOV network performance and high bandwidths
-   Automatic scheduling of G2 ECSs to AZs where NVIDIA M60 GPUs are used
-   A maximum specification of 8 GB of GPU memory and 4,096 x 2,160 resolution for processing graphics and videos
-   DirectX, OpenGL, CUDA, and OpenCL
-   Up to 2,048 CUDA cores

**Notes**

-   G2 ECSs do not support specifications modification.
-   G2 ECSs support the following OSs:
    -   Windows Server 2012
    -   Windows Server 2008

-   If a G2 ECS is created using a private image, make sure that the GPU driver has been installed during the private image creation. If not, install the driver after creating the ECS.

    To download the GPU driver, log in at  [http://www.nvidia.com/Download/index.aspx?lang=en-us](http://www.nvidia.com/Download/index.aspx?lang=en-us). You are advised to select the latest CUDA toolkit version.

    >![](public_sys-resources/icon-notice.gif) **NOTICE:**   
    >After the GPU driver is installed, run the following command to switch the GPU working mode and restart the ECS \(for example, the GPU driver is installed in  **C:\\Program Files\\NVIDIA Corporation\\NVSMI\\nvidia-smi.exe**\):  
    >**"C:\\Program Files\\NVIDIA Corporation\\NVSMI\\nvidia-smi.exe" -dm 0**  

-   If a G2 ECS is created using a private image, make sure that the SR-IOV driver has been installed during the private image creation. If not, install the driver after creating the ECS.

    To download the SR-IOV driver, log in at  [https://downloadcenter.intel.com/search?keyword=Intel++Ethernet+Connections+CD](https://downloadcenter.intel.com/search?keyword=Intel++Ethernet+Connections+CD). You are advised to select version 20.4.1 or later.

    During driver installation, if you encounter the "No Intel adapter found" error, see  [How Can I Handle the Issue that a Windows 7 ECS Equipped with an Intel 82599 NIC Reports an Error in SR-IOV Scenarios?](how-can-i-handle-the-issue-that-a-windows-7-ecs-equipped-with-an-intel-82599-nic-reports-an-error-in.md)  for troubleshooting.

-   If you log in to a G2 ECS using MSTSC, GPU acceleration will fail. This is because MSTSC replaces the WDDM GPU driver with a non-accelerated remote desktop display driver. In such an event, you must use other methods to log in to the ECS, such as VNC.
-   G2 ECSs do not support remote login provided by the public cloud platform. Before logging in to such an ECS using VNC, install the VNC server on the ECS.

## Graphics-accelerated G1<a name="section013611544538"></a>

**Overview**

G1 ECSs are based on NVIDIA GRID vGPUs and provide economical graphics acceleration. They use NVIDIA Tesla M60 GPUs and support DirectX and OpenGL. The ECSs have up to 4 GB of GPU memory and 4,096 x 2,160 resolution, and are used for applications that require high performance in graphics rendering.

**Specifications**

**Table  3**  G1 ECS specifications

<a name="table10957165555517"></a>
<table><thead align="left"><tr id="row10495675513"><th class="cellrowborder" valign="top" width="14.92%" id="mcps1.2.8.1.1"><p id="p111245612551"><a name="p111245612551"></a><a name="p111245612551"></a>ECS Type</p>
</th>
<th class="cellrowborder" valign="top" width="12.06%" id="mcps1.2.8.1.2"><p id="p1244566558"><a name="p1244566558"></a><a name="p1244566558"></a>vCPUs</p>
</th>
<th class="cellrowborder" valign="top" width="13.94%" id="mcps1.2.8.1.3"><p id="p935185619555"><a name="p935185619555"></a><a name="p935185619555"></a>Memory (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="14.99%" id="mcps1.2.8.1.4"><p id="p84285620550"><a name="p84285620550"></a><a name="p84285620550"></a>Flavor</p>
</th>
<th class="cellrowborder" valign="top" width="19.02%" id="mcps1.2.8.1.5"><p id="p165225675517"><a name="p165225675517"></a><a name="p165225675517"></a>Virtualization Type</p>
</th>
<th class="cellrowborder" valign="top" width="12.75%" id="mcps1.2.8.1.6"><p id="p85935618555"><a name="p85935618555"></a><a name="p85935618555"></a>GPUs</p>
</th>
<th class="cellrowborder" valign="top" width="12.32%" id="mcps1.2.8.1.7"><p id="p11652056155520"><a name="p11652056155520"></a><a name="p11652056155520"></a>GPU Memory (GB)</p>
</th>
</tr>
</thead>
<tbody><tr id="row2761456135515"><td class="cellrowborder" rowspan="2" valign="top" width="14.92%" headers="mcps1.2.8.1.1 "><p id="p138417565553"><a name="p138417565553"></a><a name="p138417565553"></a>Basic graphics processing G1</p>
</td>
<td class="cellrowborder" valign="top" width="12.06%" headers="mcps1.2.8.1.2 "><p id="p49245645517"><a name="p49245645517"></a><a name="p49245645517"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="13.94%" headers="mcps1.2.8.1.3 "><p id="p17100175611552"><a name="p17100175611552"></a><a name="p17100175611552"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="14.99%" headers="mcps1.2.8.1.4 "><p id="p3108175613556"><a name="p3108175613556"></a><a name="p3108175613556"></a>g1.xlarge</p>
</td>
<td class="cellrowborder" valign="top" width="19.02%" headers="mcps1.2.8.1.5 "><p id="p1511917568554"><a name="p1511917568554"></a><a name="p1511917568554"></a>Xen</p>
</td>
<td class="cellrowborder" valign="top" width="12.75%" headers="mcps1.2.8.1.6 "><p id="p1113116563554"><a name="p1113116563554"></a><a name="p1113116563554"></a>1 x M60-1Q</p>
</td>
<td class="cellrowborder" valign="top" width="12.32%" headers="mcps1.2.8.1.7 "><p id="p7138156145520"><a name="p7138156145520"></a><a name="p7138156145520"></a>1</p>
</td>
</tr>
<tr id="row161421056125514"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p1015075605511"><a name="p1015075605511"></a><a name="p1015075605511"></a>8</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p141591561559"><a name="p141591561559"></a><a name="p141591561559"></a>16</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p8167356155511"><a name="p8167356155511"></a><a name="p8167356155511"></a>g1.2xlarge</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p7176556135510"><a name="p7176556135510"></a><a name="p7176556135510"></a>Xen</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p11185125665520"><a name="p11185125665520"></a><a name="p11185125665520"></a>1 x M60-1Q</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.6 "><p id="p111951656115516"><a name="p111951656115516"></a><a name="p111951656115516"></a>1</p>
</td>
</tr>
</tbody>
</table>

**G1 ECS Features**

-   NVIDIA M60 GPUs
-   Graphics acceleration applications
-   GPU hardware virtualization \(vGPUs\) and GPU passthrough
-   Application flow identical to common ECSs
-   Automatic scheduling of G1 ECSs to AZs where NVIDIA M60 GPUs are used
-   A maximum specification of 1 GB of GPU memory and 4,096 x 2,160 resolution for processing graphics and videos

**Notes**

-   G1 ECSs do not support specifications modification.
-   G1 ECSs support the following OSs:
    -   Windows Server 2016
    -   Windows Server 2012
    -   Windows Server 2008

-   If a G1 ECS is created using a private image, install a GPU driver on the ECS after the ECS creation. 

## Computing-accelerated P2v<a name="section208472383415"></a>

**Overview**

Compared with P2 ECSs, P2v ECSs use NVIDIA Tesla V100 GPUs and provide flexibility, high-performance computing, and cost-effectiveness. These ECSs use GPU NVLink for direct communication between GPUs, improving data transmission efficiency. P2v ECSs provide outstanding general computing capabilities and have strengths in AI-based deep learning, scientific computing, Computational Fluid Dynamics \(CFD\), computing finance, seismic analysis, molecular modeling, and genomics.

**Specifications**

**Table  4**  P2v ECS specifications

<a name="table87321433202814"></a>
<table><thead align="left"><tr id="row1873312333288"><th class="cellrowborder" valign="top" width="11.821182118211821%" id="mcps1.2.11.1.1"><p id="p13733133142812"><a name="p13733133142812"></a><a name="p13733133142812"></a>Flavor</p>
</th>
<th class="cellrowborder" valign="top" width="7.520752075207522%" id="mcps1.2.11.1.2"><p id="p7733103302820"><a name="p7733103302820"></a><a name="p7733103302820"></a>vCPUs</p>
</th>
<th class="cellrowborder" valign="top" width="10.971097109710973%" id="mcps1.2.11.1.3"><p id="p3733103302818"><a name="p3733103302818"></a><a name="p3733103302818"></a>Memory (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="14.561456145614562%" id="mcps1.2.11.1.4"><p id="p473316332283"><a name="p473316332283"></a><a name="p473316332283"></a>Maximum/Assured Bandwidth (Gbit/s)</p>
</th>
<th class="cellrowborder" valign="top" width="9.730973097309732%" id="mcps1.2.11.1.5"><p id="p67338330282"><a name="p67338330282"></a><a name="p67338330282"></a>Max. PPS (10,000)</p>
</th>
<th class="cellrowborder" valign="top" width="9.72097209720972%" id="mcps1.2.11.1.6"><p id="p1373320337288"><a name="p1373320337288"></a><a name="p1373320337288"></a>NIC Multi-Queue</p>
</th>
<th class="cellrowborder" valign="top" width="8.71087108710871%" id="mcps1.2.11.1.7"><p id="p1734193313284"><a name="p1734193313284"></a><a name="p1734193313284"></a>GPUs</p>
</th>
<th class="cellrowborder" valign="top" width="8.900890089008902%" id="mcps1.2.11.1.8"><p id="p19734153312818"><a name="p19734153312818"></a><a name="p19734153312818"></a>GPU Connection</p>
</th>
<th class="cellrowborder" valign="top" width="8.970897089708972%" id="mcps1.2.11.1.9"><p id="p1673403313284"><a name="p1673403313284"></a><a name="p1673403313284"></a>GPU Memory (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="9.090909090909092%" id="mcps1.2.11.1.10"><p id="p2073433311288"><a name="p2073433311288"></a><a name="p2073433311288"></a>Virtualization Type</p>
</th>
</tr>
</thead>
<tbody><tr id="row1473423316281"><td class="cellrowborder" valign="top" width="11.821182118211821%" headers="mcps1.2.11.1.1 "><p id="p197341433122812"><a name="p197341433122812"></a><a name="p197341433122812"></a>p2v.2xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="7.520752075207522%" headers="mcps1.2.11.1.2 "><p id="p9734533152812"><a name="p9734533152812"></a><a name="p9734533152812"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="10.971097109710973%" headers="mcps1.2.11.1.3 "><p id="p8734163314288"><a name="p8734163314288"></a><a name="p8734163314288"></a>64</p>
</td>
<td class="cellrowborder" valign="top" width="14.561456145614562%" headers="mcps1.2.11.1.4 "><p id="p14734833122814"><a name="p14734833122814"></a><a name="p14734833122814"></a>10/4</p>
</td>
<td class="cellrowborder" valign="top" width="9.730973097309732%" headers="mcps1.2.11.1.5 "><p id="p11734533162819"><a name="p11734533162819"></a><a name="p11734533162819"></a>50</p>
</td>
<td class="cellrowborder" valign="top" width="9.72097209720972%" headers="mcps1.2.11.1.6 "><p id="p973412332288"><a name="p973412332288"></a><a name="p973412332288"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="8.71087108710871%" headers="mcps1.2.11.1.7 "><p id="p77351233192818"><a name="p77351233192818"></a><a name="p77351233192818"></a>1 x V100</p>
</td>
<td class="cellrowborder" valign="top" width="8.900890089008902%" headers="mcps1.2.11.1.8 "><p id="p1973533320282"><a name="p1973533320282"></a><a name="p1973533320282"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="8.970897089708972%" headers="mcps1.2.11.1.9 "><p id="p1573593372814"><a name="p1573593372814"></a><a name="p1573593372814"></a>1 x 16 GB</p>
</td>
<td class="cellrowborder" valign="top" width="9.090909090909092%" headers="mcps1.2.11.1.10 "><p id="p3735193317289"><a name="p3735193317289"></a><a name="p3735193317289"></a>KVM</p>
</td>
</tr>
<tr id="row7735833162818"><td class="cellrowborder" valign="top" width="11.821182118211821%" headers="mcps1.2.11.1.1 "><p id="p1073523317287"><a name="p1073523317287"></a><a name="p1073523317287"></a>p2v.4xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="7.520752075207522%" headers="mcps1.2.11.1.2 "><p id="p1573523322817"><a name="p1573523322817"></a><a name="p1573523322817"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="10.971097109710973%" headers="mcps1.2.11.1.3 "><p id="p11735733202819"><a name="p11735733202819"></a><a name="p11735733202819"></a>128</p>
</td>
<td class="cellrowborder" valign="top" width="14.561456145614562%" headers="mcps1.2.11.1.4 "><p id="p57361433192813"><a name="p57361433192813"></a><a name="p57361433192813"></a>15/8</p>
</td>
<td class="cellrowborder" valign="top" width="9.730973097309732%" headers="mcps1.2.11.1.5 "><p id="p1373633315286"><a name="p1373633315286"></a><a name="p1373633315286"></a>100</p>
</td>
<td class="cellrowborder" valign="top" width="9.72097209720972%" headers="mcps1.2.11.1.6 "><p id="p173613339283"><a name="p173613339283"></a><a name="p173613339283"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="8.71087108710871%" headers="mcps1.2.11.1.7 "><p id="p173613333284"><a name="p173613333284"></a><a name="p173613333284"></a>2 x V100</p>
</td>
<td class="cellrowborder" valign="top" width="8.900890089008902%" headers="mcps1.2.11.1.8 "><p id="p973610339286"><a name="p973610339286"></a><a name="p973610339286"></a>NVLink</p>
</td>
<td class="cellrowborder" valign="top" width="8.970897089708972%" headers="mcps1.2.11.1.9 "><p id="p127361233182819"><a name="p127361233182819"></a><a name="p127361233182819"></a>2 x 16 GB</p>
</td>
<td class="cellrowborder" valign="top" width="9.090909090909092%" headers="mcps1.2.11.1.10 "><p id="p1073743362811"><a name="p1073743362811"></a><a name="p1073743362811"></a>KVM</p>
</td>
</tr>
<tr id="row273713330285"><td class="cellrowborder" valign="top" width="11.821182118211821%" headers="mcps1.2.11.1.1 "><p id="p573712336284"><a name="p573712336284"></a><a name="p573712336284"></a>p2v.8xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="7.520752075207522%" headers="mcps1.2.11.1.2 "><p id="p19737163342819"><a name="p19737163342819"></a><a name="p19737163342819"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="10.971097109710973%" headers="mcps1.2.11.1.3 "><p id="p273733372819"><a name="p273733372819"></a><a name="p273733372819"></a>256</p>
</td>
<td class="cellrowborder" valign="top" width="14.561456145614562%" headers="mcps1.2.11.1.4 "><p id="p97371333202817"><a name="p97371333202817"></a><a name="p97371333202817"></a>25/15</p>
</td>
<td class="cellrowborder" valign="top" width="9.730973097309732%" headers="mcps1.2.11.1.5 "><p id="p1173717338286"><a name="p1173717338286"></a><a name="p1173717338286"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="9.72097209720972%" headers="mcps1.2.11.1.6 "><p id="p57383338285"><a name="p57383338285"></a><a name="p57383338285"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="8.71087108710871%" headers="mcps1.2.11.1.7 "><p id="p1273813311283"><a name="p1273813311283"></a><a name="p1273813311283"></a>4 x V100</p>
</td>
<td class="cellrowborder" valign="top" width="8.900890089008902%" headers="mcps1.2.11.1.8 "><p id="p9738143315282"><a name="p9738143315282"></a><a name="p9738143315282"></a>NVLink</p>
</td>
<td class="cellrowborder" valign="top" width="8.970897089708972%" headers="mcps1.2.11.1.9 "><p id="p07381533192816"><a name="p07381533192816"></a><a name="p07381533192816"></a>4 x 16 GB</p>
</td>
<td class="cellrowborder" valign="top" width="9.090909090909092%" headers="mcps1.2.11.1.10 "><p id="p15738183332812"><a name="p15738183332812"></a><a name="p15738183332812"></a>KVM</p>
</td>
</tr>
<tr id="row197385334287"><td class="cellrowborder" valign="top" width="11.821182118211821%" headers="mcps1.2.11.1.1 "><p id="p6739153319288"><a name="p6739153319288"></a><a name="p6739153319288"></a>p2v.16xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="7.520752075207522%" headers="mcps1.2.11.1.2 "><p id="p10739173322814"><a name="p10739173322814"></a><a name="p10739173322814"></a>64</p>
</td>
<td class="cellrowborder" valign="top" width="10.971097109710973%" headers="mcps1.2.11.1.3 "><p id="p5739233122811"><a name="p5739233122811"></a><a name="p5739233122811"></a>512</p>
</td>
<td class="cellrowborder" valign="top" width="14.561456145614562%" headers="mcps1.2.11.1.4 "><p id="p11739153392819"><a name="p11739153392819"></a><a name="p11739153392819"></a>30/30</p>
</td>
<td class="cellrowborder" valign="top" width="9.730973097309732%" headers="mcps1.2.11.1.5 "><p id="p373933362812"><a name="p373933362812"></a><a name="p373933362812"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9.72097209720972%" headers="mcps1.2.11.1.6 "><p id="p147391833102815"><a name="p147391833102815"></a><a name="p147391833102815"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="8.71087108710871%" headers="mcps1.2.11.1.7 "><p id="p773917330288"><a name="p773917330288"></a><a name="p773917330288"></a>8 x V100</p>
</td>
<td class="cellrowborder" valign="top" width="8.900890089008902%" headers="mcps1.2.11.1.8 "><p id="p1874093362814"><a name="p1874093362814"></a><a name="p1874093362814"></a>NVLink</p>
</td>
<td class="cellrowborder" valign="top" width="8.970897089708972%" headers="mcps1.2.11.1.9 "><p id="p274083312282"><a name="p274083312282"></a><a name="p274083312282"></a>8 x 16 GB</p>
</td>
<td class="cellrowborder" valign="top" width="9.090909090909092%" headers="mcps1.2.11.1.10 "><p id="p574073311284"><a name="p574073311284"></a><a name="p574073311284"></a>KVM</p>
</td>
</tr>
</tbody>
</table>

**P2v ECS Features**

-   Up to eight NVIDIA Tesla V100 GPUs on an ECS
-   NVIDIA CUDA parallel computing and common deep learning frameworks, such as TensorFlow, Caffe, PyTorch, and MXNet
-   15.7 TFLOPS of single-precision computing and 7.8 TFLOPS of double-precision computing
-   NVIDIA Tensor cores with 125 TFLOPS of single- and double-precision computing for deep learning
-   Up to 30 GB/s of network bandwidth on a single ECS
-   16 GB of HBM2 GPU memory with a bandwidth of 900 GB/s
-   Comprehensive basic capabilities

    Networks are user-defined, subnets can be divided, and network access policies can be configured as needed. Mass storage is used, elastic capacity expansion as well as backup and restoration are supported to make data more secure. Auto Scaling allows you to add or reduce the number of ECSs quickly.

-   Flexibility

    Similar to other types of ECSs, P2v ECSs can be provisioned in a few minutes.

-   Excellent supercomputing ecosystem

    The supercomputing ecosystem allows you to build up a flexible, high-performance, cost-effective computing platform. A large number of HPC applications and deep-learning frameworks can run on P2v ECSs.


**Supported Common Software**

P2v ECSs are used in computing acceleration scenarios, such as deep learning training, inference, scientific computing, molecular modeling, and seismic analysis. If the software is required to support GPU CUDA, use P2v ECSs. P2v ECSs support the following commonly used software:

-   Common deep learning frameworks, such as TensorFlow, Caffe, PyTorch, and MXNet
-   CUDA GPU rendering supported by RedShift for Autodesk 3dsMax and V-Ray for 3ds Max
-   Agisoft PhotoScan
-   MapD

**Notes**

-   If a P2v ECS is created using a private image, make sure that the NVIDIA driver has been installed during the private image creation. If not, install the driver for computing acceleration after the P2v ECS is created. For details, see  [Installing the NVIDIA GPU Driver and CUDA Toolkit on a P2v ECS](installing-the-nvidia-gpu-driver-and-cuda-toolkit-on-a-p2v-ecs.md).
-   P2v ECSs do not support specifications modification.
-   P2v ECSs support the following OSs:
    -   Windows Server 2016 Standard 64bit
    -   Windows Server 2012 R2 Standard 64bit
    -   Ubuntu Server 16.04 64bit
    -   CentOS 7.4 64bit
    -   EulerOS 2.2 64bit


## Computing-accelerated P2<a name="section5477185118234"></a>

**Overview**

Compared with P1 ECSs, P2 ECSs use NVIDIA Tesla V100 GPUs, which have improved both single- and double-precision computing capabilities by 50% and offer 112 TFLOPS of deep learning.

**Specifications**

**Table  5**  P2 ECS specifications

<a name="table179717351266"></a>
<table><thead align="left"><tr id="row182153672615"><th class="cellrowborder" valign="top" width="12.34%" id="mcps1.2.11.1.1"><p id="p451936142613"><a name="p451936142613"></a><a name="p451936142613"></a>Flavor</p>
</th>
<th class="cellrowborder" valign="top" width="7.5200000000000005%" id="mcps1.2.11.1.2"><p id="p181123612611"><a name="p181123612611"></a><a name="p181123612611"></a>vCPUs</p>
</th>
<th class="cellrowborder" valign="top" width="8.91%" id="mcps1.2.11.1.3"><p id="p1017636202619"><a name="p1017636202619"></a><a name="p1017636202619"></a>Memory (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="10.83%" id="mcps1.2.11.1.4"><p id="p5975101918215"><a name="p5975101918215"></a><a name="p5975101918215"></a>Maximum/Assured Bandwidth (Gbit/s)</p>
</th>
<th class="cellrowborder" valign="top" width="10.54%" id="mcps1.2.11.1.5"><p id="p79761919182119"><a name="p79761919182119"></a><a name="p79761919182119"></a>Max. PPS (10,000)</p>
</th>
<th class="cellrowborder" valign="top" width="7.5200000000000005%" id="mcps1.2.11.1.6"><p id="p250571402111"><a name="p250571402111"></a><a name="p250571402111"></a>NIC Multi-Queue</p>
</th>
<th class="cellrowborder" valign="top" width="8.42%" id="mcps1.2.11.1.7"><p id="p1221636152619"><a name="p1221636152619"></a><a name="p1221636152619"></a>GPUs</p>
</th>
<th class="cellrowborder" valign="top" width="10.8%" id="mcps1.2.11.1.8"><p id="p1129153612268"><a name="p1129153612268"></a><a name="p1129153612268"></a>GPU Memory (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="13.87%" id="mcps1.2.11.1.9"><p id="p510333614263"><a name="p510333614263"></a><a name="p510333614263"></a>Local Disks</p>
</th>
<th class="cellrowborder" valign="top" width="9.25%" id="mcps1.2.11.1.10"><p id="p91091136172614"><a name="p91091136172614"></a><a name="p91091136172614"></a>Virtualization Type</p>
</th>
</tr>
</thead>
<tbody><tr id="row4115236182617"><td class="cellrowborder" valign="top" width="12.34%" headers="mcps1.2.11.1.1 "><p id="p1120143611269"><a name="p1120143611269"></a><a name="p1120143611269"></a>p2.2xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.11.1.2 "><p id="p81261436202611"><a name="p81261436202611"></a><a name="p81261436202611"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="8.91%" headers="mcps1.2.11.1.3 "><p id="p613113613267"><a name="p613113613267"></a><a name="p613113613267"></a>64</p>
</td>
<td class="cellrowborder" valign="top" width="10.83%" headers="mcps1.2.11.1.4 "><p id="p20327021122217"><a name="p20327021122217"></a><a name="p20327021122217"></a>5/1.6</p>
</td>
<td class="cellrowborder" valign="top" width="10.54%" headers="mcps1.2.11.1.5 "><p id="p4919151532210"><a name="p4919151532210"></a><a name="p4919151532210"></a>35</p>
</td>
<td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.11.1.6 "><p id="p129828722214"><a name="p129828722214"></a><a name="p129828722214"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="8.42%" headers="mcps1.2.11.1.7 "><p id="p51361736172611"><a name="p51361736172611"></a><a name="p51361736172611"></a>1 x V100</p>
</td>
<td class="cellrowborder" valign="top" width="10.8%" headers="mcps1.2.11.1.8 "><p id="p141421836122617"><a name="p141421836122617"></a><a name="p141421836122617"></a>1 x 16</p>
</td>
<td class="cellrowborder" valign="top" width="13.87%" headers="mcps1.2.11.1.9 "><p id="p19148036182615"><a name="p19148036182615"></a><a name="p19148036182615"></a>1 x 800 GB NVMe</p>
</td>
<td class="cellrowborder" valign="top" width="9.25%" headers="mcps1.2.11.1.10 "><p id="p1415363616265"><a name="p1415363616265"></a><a name="p1415363616265"></a>KVM</p>
</td>
</tr>
<tr id="row1615513618269"><td class="cellrowborder" valign="top" width="12.34%" headers="mcps1.2.11.1.1 "><p id="p101612363261"><a name="p101612363261"></a><a name="p101612363261"></a>p2.4xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.11.1.2 "><p id="p1216643632615"><a name="p1216643632615"></a><a name="p1216643632615"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="8.91%" headers="mcps1.2.11.1.3 "><p id="p8169193615267"><a name="p8169193615267"></a><a name="p8169193615267"></a>128</p>
</td>
<td class="cellrowborder" valign="top" width="10.83%" headers="mcps1.2.11.1.4 "><p id="p20327152112229"><a name="p20327152112229"></a><a name="p20327152112229"></a>8/3.2</p>
</td>
<td class="cellrowborder" valign="top" width="10.54%" headers="mcps1.2.11.1.5 "><p id="p1591915153221"><a name="p1591915153221"></a><a name="p1591915153221"></a>70</p>
</td>
<td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.11.1.6 "><p id="p1698297102215"><a name="p1698297102215"></a><a name="p1698297102215"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="8.42%" headers="mcps1.2.11.1.7 "><p id="p1017643642616"><a name="p1017643642616"></a><a name="p1017643642616"></a>2 x V100</p>
</td>
<td class="cellrowborder" valign="top" width="10.8%" headers="mcps1.2.11.1.8 "><p id="p161831936182616"><a name="p161831936182616"></a><a name="p161831936182616"></a>2 x 16</p>
</td>
<td class="cellrowborder" valign="top" width="13.87%" headers="mcps1.2.11.1.9 "><p id="p6192436172613"><a name="p6192436172613"></a><a name="p6192436172613"></a>2 x 800 GB NVMe</p>
</td>
<td class="cellrowborder" valign="top" width="9.25%" headers="mcps1.2.11.1.10 "><p id="p1619812366261"><a name="p1619812366261"></a><a name="p1619812366261"></a>KVM</p>
</td>
</tr>
<tr id="row3202236162615"><td class="cellrowborder" valign="top" width="12.34%" headers="mcps1.2.11.1.1 "><p id="p52051436122614"><a name="p52051436122614"></a><a name="p52051436122614"></a>p2.8xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.11.1.2 "><p id="p142103360264"><a name="p142103360264"></a><a name="p142103360264"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="8.91%" headers="mcps1.2.11.1.3 "><p id="p19213536142614"><a name="p19213536142614"></a><a name="p19213536142614"></a>256</p>
</td>
<td class="cellrowborder" valign="top" width="10.83%" headers="mcps1.2.11.1.4 "><p id="p83274217221"><a name="p83274217221"></a><a name="p83274217221"></a>10/6.5</p>
</td>
<td class="cellrowborder" valign="top" width="10.54%" headers="mcps1.2.11.1.5 "><p id="p189201515132211"><a name="p189201515132211"></a><a name="p189201515132211"></a>140</p>
</td>
<td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.11.1.6 "><p id="p199824712212"><a name="p199824712212"></a><a name="p199824712212"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="8.42%" headers="mcps1.2.11.1.7 "><p id="p1221943614265"><a name="p1221943614265"></a><a name="p1221943614265"></a>4 x V100</p>
</td>
<td class="cellrowborder" valign="top" width="10.8%" headers="mcps1.2.11.1.8 "><p id="p322573617261"><a name="p322573617261"></a><a name="p322573617261"></a>4 x 16</p>
</td>
<td class="cellrowborder" valign="top" width="13.87%" headers="mcps1.2.11.1.9 "><p id="p62301836182620"><a name="p62301836182620"></a><a name="p62301836182620"></a>4 x 800 GB NVMe</p>
</td>
<td class="cellrowborder" valign="top" width="9.25%" headers="mcps1.2.11.1.10 "><p id="p12363363263"><a name="p12363363263"></a><a name="p12363363263"></a>KVM</p>
</td>
</tr>
</tbody>
</table>

**P2 ECS Features**

-   NVIDIA Tesla V100 GPUs
-   GPU hardware passthrough
-   14 TFLOPS of single-precision computing, 7 TFLOPS of double-precision computing, and 112 TFLOPS of deep learning
-   Maximum bandwidth of 12 Gbit/s
-   16 GB of HBM2 GPU memory with a bandwidth of 900 GB/s
-   800 GB NVMe SSDs for temporary local storage
-   Comprehensive basic capabilities

    Networks are user-defined, subnets can be divided, and network access policies can be configured as needed. Mass storage is used, elastic capacity expansion as well as backup and restoration are supported to make data more secure. Auto Scaling allows you to add or reduce the number of ECSs quickly.

-   Flexibility

    Similar to other types of ECSs, P2 ECSs can be provisioned in a few minutes.

-   Excellent supercomputing ecosystem

    The supercomputing ecosystem allows you to build up a flexible, high-performance, cost-effective computing platform. A large number of HPC applications and deep-learning frameworks can run on P2 ECSs.


**Supported Common Software**

P2 ECSs are used in computing acceleration scenarios, such as deep learning training, inference, scientific computing, molecular modeling, and seismic analysis. If the software requires GPU CUDA parallel computing, use P2 ECSs. P2 ECSs support the following commonly used software:

-   Common deep learning frameworks, such as TensorFlow, Caffe, PyTorch, and MXNet
-   CUDA GPU rendering supported by RedShift for Autodesk 3dsMax and V-Ray for 3ds Max
-   Agisoft PhotoScan
-   MapD

**Notes**

-   The system disk of a P2 ECS must be greater than or equal to 15 GB. It is recommended that the system disk be greater than 40 GB.
-   The local NVMe SSDs attached to P2 ECSs are dedicated for services with strict requirements on storage I/O performance, such as deep learning training and HPC. Local disks are attached to the ECSs of specified flavors and cannot be separately bought. In addition, you are not allowed to detach a local disk and then attach it to another ECS.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >Data may be lost on the local NVMe SSDs attached to P2 ECSs due to, for example, a disk or host fault. Therefore, you are suggested to store only temporary data in local NVMe SSDs. If you store important data in such a disk, securely back up the data.  

-   If a P2 ECS is created using a private image, make sure that the NVIDIA driver has been installed during the private image creation. If not, install the driver for computing acceleration after the P2 ECS is created. For details, see  [Installing the NVIDIA GPU Driver and CUDA Toolkit on a P2 ECS](installing-the-nvidia-gpu-driver-and-cuda-toolkit-on-a-p2-ecs.md).
-   P2 ECSs do not support specifications modification.
-   P2 ECSs support the following OSs:

    Ubuntu Server 16.04 64bit

-   After you delete a P2 ECS, the data stored in local NVMe SSDs is automatically cleared.

## Computing-accelerated P1<a name="section1124594913391"></a>

**Overview**

P1 ECSs use NVIDIA Tesla P100 GPUs and provide flexibility, high performance, and cost-effectiveness. These ECSs support GPU Direct for direct communication between GPUs, improving data transmission efficiency. P1 ECSs provide outstanding general computing capabilities and have strengths in deep learning, graphic databases, high-performance databases, Computational Fluid Dynamics \(CFD\), computing finance, seismic analysis, molecular modeling, and genomics. They are designed for scientific computing.

**Specifications**

**Table  6**  P1 ECS specifications

<a name="table1888295812406"></a>
<table><thead align="left"><tr id="row9924155884012"><th class="cellrowborder" valign="top" width="12.52125212521252%" id="mcps1.2.11.1.1"><p id="p29321858164010"><a name="p29321858164010"></a><a name="p29321858164010"></a>Flavor</p>
</th>
<th class="cellrowborder" valign="top" width="7.520752075207521%" id="mcps1.2.11.1.2"><p id="p3941658204013"><a name="p3941658204013"></a><a name="p3941658204013"></a>vCPUs</p>
</th>
<th class="cellrowborder" valign="top" width="9.02090209020902%" id="mcps1.2.11.1.3"><p id="p8950185818401"><a name="p8950185818401"></a><a name="p8950185818401"></a>Memory (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="11.63116311631163%" id="mcps1.2.11.1.4"><p id="p157691452122312"><a name="p157691452122312"></a><a name="p157691452122312"></a>Maximum/Assured Bandwidth (Gbit/s)</p>
</th>
<th class="cellrowborder" valign="top" width="9.47094709470947%" id="mcps1.2.11.1.5"><p id="p776917521239"><a name="p776917521239"></a><a name="p776917521239"></a>Max. PPS (10,000)</p>
</th>
<th class="cellrowborder" valign="top" width="9.78097809780978%" id="mcps1.2.11.1.6"><p id="p137691552112310"><a name="p137691552112310"></a><a name="p137691552112310"></a>NIC Multi-Queue</p>
</th>
<th class="cellrowborder" valign="top" width="9.77097709770977%" id="mcps1.2.11.1.7"><p id="p1595718582408"><a name="p1595718582408"></a><a name="p1595718582408"></a>GPUs</p>
</th>
<th class="cellrowborder" valign="top" width="9.760976097609761%" id="mcps1.2.11.1.8"><p id="p199641058194015"><a name="p199641058194015"></a><a name="p199641058194015"></a>GPU Memory (GB)</p>
</th>
<th class="cellrowborder" valign="top" width="10.76107610761076%" id="mcps1.2.11.1.9"><p id="p097115581402"><a name="p097115581402"></a><a name="p097115581402"></a>Local Disks</p>
</th>
<th class="cellrowborder" valign="top" width="9.760976097609761%" id="mcps1.2.11.1.10"><p id="p1797765814017"><a name="p1797765814017"></a><a name="p1797765814017"></a>Virtualization Type</p>
</th>
</tr>
</thead>
<tbody><tr id="row098118587405"><td class="cellrowborder" valign="top" width="12.52125212521252%" headers="mcps1.2.11.1.1 "><p id="p1299065811409"><a name="p1299065811409"></a><a name="p1299065811409"></a>p1.2xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="7.520752075207521%" headers="mcps1.2.11.1.2 "><p id="p1099435818406"><a name="p1099435818406"></a><a name="p1099435818406"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="9.02090209020902%" headers="mcps1.2.11.1.3 "><p id="p19245964016"><a name="p19245964016"></a><a name="p19245964016"></a>64</p>
</td>
<td class="cellrowborder" valign="top" width="11.63116311631163%" headers="mcps1.2.11.1.4 "><p id="p16445132618246"><a name="p16445132618246"></a><a name="p16445132618246"></a>5/1.6</p>
</td>
<td class="cellrowborder" valign="top" width="9.47094709470947%" headers="mcps1.2.11.1.5 "><p id="p1792712162413"><a name="p1792712162413"></a><a name="p1792712162413"></a>35</p>
</td>
<td class="cellrowborder" valign="top" width="9.78097809780978%" headers="mcps1.2.11.1.6 "><p id="p1206121515242"><a name="p1206121515242"></a><a name="p1206121515242"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="9.77097709770977%" headers="mcps1.2.11.1.7 "><p id="p15975911401"><a name="p15975911401"></a><a name="p15975911401"></a>1 x P100</p>
</td>
<td class="cellrowborder" valign="top" width="9.760976097609761%" headers="mcps1.2.11.1.8 "><p id="p121565919402"><a name="p121565919402"></a><a name="p121565919402"></a>1 x 16</p>
</td>
<td class="cellrowborder" valign="top" width="10.76107610761076%" headers="mcps1.2.11.1.9 "><p id="p172212598401"><a name="p172212598401"></a><a name="p172212598401"></a>1 x 800 GB NVMe</p>
</td>
<td class="cellrowborder" valign="top" width="9.760976097609761%" headers="mcps1.2.11.1.10 "><p id="p3294596404"><a name="p3294596404"></a><a name="p3294596404"></a>KVM</p>
</td>
</tr>
<tr id="row153310597408"><td class="cellrowborder" valign="top" width="12.52125212521252%" headers="mcps1.2.11.1.1 "><p id="p1338165918403"><a name="p1338165918403"></a><a name="p1338165918403"></a>p1.4xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="7.520752075207521%" headers="mcps1.2.11.1.2 "><p id="p84514590405"><a name="p84514590405"></a><a name="p84514590405"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="9.02090209020902%" headers="mcps1.2.11.1.3 "><p id="p25015954014"><a name="p25015954014"></a><a name="p25015954014"></a>128</p>
</td>
<td class="cellrowborder" valign="top" width="11.63116311631163%" headers="mcps1.2.11.1.4 "><p id="p1044562672420"><a name="p1044562672420"></a><a name="p1044562672420"></a>8/3.2</p>
</td>
<td class="cellrowborder" valign="top" width="9.47094709470947%" headers="mcps1.2.11.1.5 "><p id="p17927152122418"><a name="p17927152122418"></a><a name="p17927152122418"></a>70</p>
</td>
<td class="cellrowborder" valign="top" width="9.78097809780978%" headers="mcps1.2.11.1.6 "><p id="p6206101515247"><a name="p6206101515247"></a><a name="p6206101515247"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="9.77097709770977%" headers="mcps1.2.11.1.7 "><p id="p145865916402"><a name="p145865916402"></a><a name="p145865916402"></a>2 x P100</p>
</td>
<td class="cellrowborder" valign="top" width="9.760976097609761%" headers="mcps1.2.11.1.8 "><p id="p263175920406"><a name="p263175920406"></a><a name="p263175920406"></a>2 x 16</p>
</td>
<td class="cellrowborder" valign="top" width="10.76107610761076%" headers="mcps1.2.11.1.9 "><p id="p1369165994013"><a name="p1369165994013"></a><a name="p1369165994013"></a>2 x 800 GB NVMe</p>
</td>
<td class="cellrowborder" valign="top" width="9.760976097609761%" headers="mcps1.2.11.1.10 "><p id="p1474759164014"><a name="p1474759164014"></a><a name="p1474759164014"></a>KVM</p>
</td>
</tr>
<tr id="row16781059194017"><td class="cellrowborder" valign="top" width="12.52125212521252%" headers="mcps1.2.11.1.1 "><p id="p1583859184016"><a name="p1583859184016"></a><a name="p1583859184016"></a>p1.8xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" width="7.520752075207521%" headers="mcps1.2.11.1.2 "><p id="p1790125914408"><a name="p1790125914408"></a><a name="p1790125914408"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="9.02090209020902%" headers="mcps1.2.11.1.3 "><p id="p199819595405"><a name="p199819595405"></a><a name="p199819595405"></a>256</p>
</td>
<td class="cellrowborder" valign="top" width="11.63116311631163%" headers="mcps1.2.11.1.4 "><p id="p344512265247"><a name="p344512265247"></a><a name="p344512265247"></a>10/6.5</p>
</td>
<td class="cellrowborder" valign="top" width="9.47094709470947%" headers="mcps1.2.11.1.5 "><p id="p109271221142415"><a name="p109271221142415"></a><a name="p109271221142415"></a>140</p>
</td>
<td class="cellrowborder" valign="top" width="9.78097809780978%" headers="mcps1.2.11.1.6 "><p id="p8206715152419"><a name="p8206715152419"></a><a name="p8206715152419"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="9.77097709770977%" headers="mcps1.2.11.1.7 "><p id="p1910612592401"><a name="p1910612592401"></a><a name="p1910612592401"></a>4 x P100</p>
</td>
<td class="cellrowborder" valign="top" width="9.760976097609761%" headers="mcps1.2.11.1.8 "><p id="p1511315910407"><a name="p1511315910407"></a><a name="p1511315910407"></a>4 x 16</p>
</td>
<td class="cellrowborder" valign="top" width="10.76107610761076%" headers="mcps1.2.11.1.9 "><p id="p201201559154018"><a name="p201201559154018"></a><a name="p201201559154018"></a>4 x 800 GB NVMe</p>
</td>
<td class="cellrowborder" valign="top" width="9.760976097609761%" headers="mcps1.2.11.1.10 "><p id="p01291559174013"><a name="p01291559174013"></a><a name="p01291559174013"></a>KVM</p>
</td>
</tr>
</tbody>
</table>

**P1 ECS Features**

-   Up to four NVIDIA Tesla P100 GPUs on a P1 ECS \(If eight P100 GPUs are required on an instance, use BMS.\)
-   GPU hardware passthrough
-   9.3 TFLOPS of single-precision computing and 4.7 TFLOPS of double-precision computing
-   Maximum network bandwidth of 10 Gbit/s
-   16 GB of HBM2 GPU memory with a bandwidth of 732 GB/s
-   800 GB NVMe SSDs for temporary local storage
-   Comprehensive basic capabilities

    Networks are user-defined, subnets can be divided, and network access policies can be configured as needed. Mass storage is used, elastic capacity expansion as well as backup and restoration are supported to make data more secure. Auto Scaling allows you to add or reduce the number of ECSs quickly.

-   Flexibility

    Similar to other types of ECSs, P1 ECSs can be provisioned in a few minutes. You can configure specifications as needed. P1 ECSs with two, four, and eight GPUs will be supported later.

-   Excellent supercomputing ecosystem

    The supercomputing ecosystem allows you to build up a flexible, high-performance, cost-effective computing platform. A large number of HPC applications and deep-learning frameworks can run on P1 ECSs.


**Supported Common Software**

P1 ECSs are used in computing acceleration scenarios, such as deep learning training, inference, scientific computing, molecular modeling, and seismic analysis. If the software requires GPU CUDA parallel computing, use P1 ECSs. P1 ECSs support the following commonly used software:

-   Deep learning frameworks, such as TensorFlow, Caffe, PyTorch, and MXNet
-   RedShift for Autodesk 3dsMax, V-Ray for 3ds Max
-   Agisoft PhotoScan
-   MapD

**Notes**

-   It is recommended that the system disk of a P1 ECS be greater than 40 GB.
-   The local NVMe SSDs attached to P1 ECSs are dedicated for services with strict requirements on storage I/O performance, such as deep learning training and HPC. Local disks are attached to the ECSs of specified flavors and cannot be separately bought. In addition, you are not allowed to detach a local disk and then attach it to another ECS.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >Data may be lost on the local NVMe SSDs attached to P1 ECSs due to a fault, for example, due to a disk or host fault. Therefore, you are suggested to store only temporary data in local NVMe SSDs. If you store important data in such a disk, securely back up the data.  

-   After a P1 ECS is created, you must install the NVIDIA driver for computing acceleration. For details, see  [Installing the NVIDIA GPU Driver and CUDA Toolkit on a P1 ECS](installing-the-nvidia-gpu-driver-and-cuda-toolkit-on-a-p1-ecs.md).
-   P1 ECSs do not support specifications modification.
-   P1 ECSs support the following OSs:
    -   Windows Server 2012 R2 Standard 64bit
    -   Ubuntu Server 16.04 64bit
    -   CentOS 7.4 64bit
    -   Debian 9.0 64bit

-   After you delete a P1 ECS, the data stored in local NVMe SSDs is automatically cleared.

