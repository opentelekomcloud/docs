# Installing Special Windows Drivers<a name="EN-US_TOPIC_0081795392"></a>

Before using some types of ECSs to create private images, you need to install special drivers on the ECSs.

## GPU Driver<a name="section1416112291151"></a>

If you want to use the created private image to create GPU-accelerated ECSs, install a proper GPU driver for the image to enable GPU acceleration. There are two types of NVIDIA Tesla GPU drivers for GPU-accelerated ECSs, Tesla and GRID/vGPU drivers.

-   To use graphics acceleration, such as OpenGL, DirectX, or Vulcan, install the GRID/vGPU driver and separately configure a GRID license. The GRID/vGPU driver with a vDWS license also supports CUDA for both computing and graphics acceleration.
-   To use NVIDIA CUDA computing acceleration, install the Tesla driver.

1.  To install the GRID driver on a G1 ECS, perform the following operations:
    1.  [Obtain the driver installation package](https://www.nvidia.com/grid-eval)  required for an OS. For details, see  [Table 1](#en-us_topic_0149610914_table230940145218).

        >![](/images/icon-note.gif) **NOTE:**   
        >For a GPU passthrough ECS, select a GRID driver version as required.  
        >For a GPU virtualization ECS, select a driver version based on  [Table 1](#en-us_topic_0149610914_table230940145218).  

        **Table  1**  GRID/vGPU driver versions supported by GPU-accelerated ECSs

        <a name="en-us_topic_0149610914_table230940145218"></a>
        <table><thead align="left"><tr id="en-us_topic_0149610914_row1230860145216"><th class="cellrowborder" valign="top" width="10.891089108910892%" id="mcps1.2.6.1.1"><p id="en-us_topic_0149610914_p103087005217"><a name="en-us_topic_0149610914_p103087005217"></a><a name="en-us_topic_0149610914_p103087005217"></a>ECS Type</p>
        </th>
        <th class="cellrowborder" valign="top" width="17.82178217821782%" id="mcps1.2.6.1.2"><p id="en-us_topic_0149610914_p831263814595"><a name="en-us_topic_0149610914_p831263814595"></a><a name="en-us_topic_0149610914_p831263814595"></a>GPU Attachment</p>
        </th>
        <th class="cellrowborder" valign="top" width="28.71287128712871%" id="mcps1.2.6.1.3"><p id="en-us_topic_0149610914_p10464537154117"><a name="en-us_topic_0149610914_p10464537154117"></a><a name="en-us_topic_0149610914_p10464537154117"></a>OS</p>
        </th>
        <th class="cellrowborder" valign="top" width="23.762376237623762%" id="mcps1.2.6.1.4"><p id="en-us_topic_0149610914_p130820145216"><a name="en-us_topic_0149610914_p130820145216"></a><a name="en-us_topic_0149610914_p130820145216"></a>Driver Version</p>
        </th>
        <th class="cellrowborder" valign="top" width="18.81188118811881%" id="mcps1.2.6.1.5"><p id="en-us_topic_0149610914_p32836161156"><a name="en-us_topic_0149610914_p32836161156"></a><a name="en-us_topic_0149610914_p32836161156"></a>CPU Architecture</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="en-us_topic_0149610914_row1443710550468"><td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0149610914_p0222125913469"><a name="en-us_topic_0149610914_p0222125913469"></a><a name="en-us_topic_0149610914_p0222125913469"></a>G6</p>
        </td>
        <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0149610914_p9222359154617"><a name="en-us_topic_0149610914_p9222359154617"></a><a name="en-us_topic_0149610914_p9222359154617"></a>GPU virtualization</p>
        </td>
        <td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.2.6.1.3 "><a name="en-us_topic_0149610914_ul1341917351493"></a><a name="en-us_topic_0149610914_ul1341917351493"></a><ul id="en-us_topic_0149610914_ul1341917351493"><li>Windows Server 2016 Standard 64bit</li></ul>
        </td>
        <td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0149610914_p322265913467"><a name="en-us_topic_0149610914_p322265913467"></a><a name="en-us_topic_0149610914_p322265913467"></a>GRID 7.1: NVIDIA vGPU for Linux KVM</p>
        <p id="en-us_topic_0149610914_p1753013398443"><a name="en-us_topic_0149610914_p1753013398443"></a><a name="en-us_topic_0149610914_p1753013398443"></a>Verify other driver versions.</p>
        </td>
        <td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.6.1.5 "><p id="en-us_topic_0149610914_p1828331614520"><a name="en-us_topic_0149610914_p1828331614520"></a><a name="en-us_topic_0149610914_p1828331614520"></a>x86_64</p>
        </td>
        </tr>
        <tr id="en-us_topic_0149610914_row2017804416017"><td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0149610914_p1617817444014"><a name="en-us_topic_0149610914_p1617817444014"></a><a name="en-us_topic_0149610914_p1617817444014"></a>G2</p>
        </td>
        <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0149610914_p1617864420013"><a name="en-us_topic_0149610914_p1617864420013"></a><a name="en-us_topic_0149610914_p1617864420013"></a>GPU passthrough</p>
        </td>
        <td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.2.6.1.3 "><a name="en-us_topic_0149610914_ul1535413327215"></a><a name="en-us_topic_0149610914_ul1535413327215"></a><ul id="en-us_topic_0149610914_ul1535413327215"><li>Windows Server 2012</li><li>Windows Server 2008</li></ul>
        </td>
        <td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0149610914_p61788448016"><a name="en-us_topic_0149610914_p61788448016"></a><a name="en-us_topic_0149610914_p61788448016"></a>Select a version as required.</p>
        </td>
        <td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.6.1.5 "><p id="en-us_topic_0149610914_p728317168515"><a name="en-us_topic_0149610914_p728317168515"></a><a name="en-us_topic_0149610914_p728317168515"></a>x86_64</p>
        </td>
        </tr>
        <tr id="en-us_topic_0149610914_row53092007529"><td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0149610914_p93091200526"><a name="en-us_topic_0149610914_p93091200526"></a><a name="en-us_topic_0149610914_p93091200526"></a>G1</p>
        </td>
        <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0149610914_p1631215381599"><a name="en-us_topic_0149610914_p1631215381599"></a><a name="en-us_topic_0149610914_p1631215381599"></a>GPU virtualization</p>
        </td>
        <td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.2.6.1.3 "><a name="en-us_topic_0149610914_ul1854703165713"></a><a name="en-us_topic_0149610914_ul1854703165713"></a><ul id="en-us_topic_0149610914_ul1854703165713"><li>Windows Server 2016</li><li>Windows Server 2012</li><li>Windows Server 2008</li></ul>
        </td>
        <td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0149610914_p1330911065220"><a name="en-us_topic_0149610914_p1330911065220"></a><a name="en-us_topic_0149610914_p1330911065220"></a>vGPU 4.1: GRID for UVP</p>
        </td>
        <td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.6.1.5 "><p id="en-us_topic_0149610914_p152839165513"><a name="en-us_topic_0149610914_p152839165513"></a><a name="en-us_topic_0149610914_p152839165513"></a>x86_64</p>
        </td>
        </tr>
        <tr id="en-us_topic_0149610914_row1383513813532"><td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0149610914_p10494441165310"><a name="en-us_topic_0149610914_p10494441165310"></a><a name="en-us_topic_0149610914_p10494441165310"></a>P2v</p>
        </td>
        <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0149610914_p18494164165320"><a name="en-us_topic_0149610914_p18494164165320"></a><a name="en-us_topic_0149610914_p18494164165320"></a>GPU passthrough</p>
        </td>
        <td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.2.6.1.3 "><a name="en-us_topic_0149610914_ul94948412537"></a><a name="en-us_topic_0149610914_ul94948412537"></a><ul id="en-us_topic_0149610914_ul94948412537"><li>Windows Server 2016 Standard 64bit</li><li>Windows Server 2012 R2 Standard 64bit</li><li>Ubuntu Server 16.04 64bit</li><li>CentOS 7.4 64bit</li><li>EulerOS 2.2 64bit</li></ul>
        </td>
        <td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0149610914_p1049454175316"><a name="en-us_topic_0149610914_p1049454175316"></a><a name="en-us_topic_0149610914_p1049454175316"></a>Select a version as required.</p>
        </td>
        <td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.6.1.5 "><p id="en-us_topic_0149610914_p5283216652"><a name="en-us_topic_0149610914_p5283216652"></a><a name="en-us_topic_0149610914_p5283216652"></a>x86_64</p>
        </td>
        </tr>
        <tr id="en-us_topic_0149610914_row8919171710547"><td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0149610914_p11919717115417"><a name="en-us_topic_0149610914_p11919717115417"></a><a name="en-us_topic_0149610914_p11919717115417"></a>P2</p>
        </td>
        <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0149610914_p14313153819594"><a name="en-us_topic_0149610914_p14313153819594"></a><a name="en-us_topic_0149610914_p14313153819594"></a>GPU passthrough</p>
        </td>
        <td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0149610914_p1546463718419"><a name="en-us_topic_0149610914_p1546463718419"></a><a name="en-us_topic_0149610914_p1546463718419"></a>Ubuntu Server 16.04 64bit</p>
        </td>
        <td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0149610914_p2919117165413"><a name="en-us_topic_0149610914_p2919117165413"></a><a name="en-us_topic_0149610914_p2919117165413"></a>Select a version as required.</p>
        </td>
        <td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.6.1.5 "><p id="en-us_topic_0149610914_p1028351612512"><a name="en-us_topic_0149610914_p1028351612512"></a><a name="en-us_topic_0149610914_p1028351612512"></a>x86_64</p>
        </td>
        </tr>
        <tr id="en-us_topic_0149610914_row1452816207544"><td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0149610914_p2528202025418"><a name="en-us_topic_0149610914_p2528202025418"></a><a name="en-us_topic_0149610914_p2528202025418"></a>P1</p>
        </td>
        <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0149610914_p96883531726"><a name="en-us_topic_0149610914_p96883531726"></a><a name="en-us_topic_0149610914_p96883531726"></a>GPU passthrough</p>
        </td>
        <td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.2.6.1.3 "><a name="en-us_topic_0149610914_ul1740013273448"></a><a name="en-us_topic_0149610914_ul1740013273448"></a><ul id="en-us_topic_0149610914_ul1740013273448"><li>Windows Server 2012 R2 Standard 64bit</li><li>Ubuntu Server 16.04 64bit</li><li>CentOS 7.4 64bit</li><li>Debian 9.0 64bit</li></ul>
        </td>
        <td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0149610914_p19688053127"><a name="en-us_topic_0149610914_p19688053127"></a><a name="en-us_topic_0149610914_p19688053127"></a>Select a version as required.</p>
        </td>
        <td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.6.1.5 "><p id="en-us_topic_0149610914_p22837161852"><a name="en-us_topic_0149610914_p22837161852"></a><a name="en-us_topic_0149610914_p22837161852"></a>x86_64</p>
        </td>
        </tr>
        </tbody>
        </table>

    2.  After the registration, log in at the  [official NVIDIA website](https://nvid.nvidia.com/dashboard/)  and enter the account.
    3.  Check whether NVIDIA is used for the first time.
        1.  If yes, go to step  [1.d](#en-us_topic_0149610914_li1859773663819).
        2.  If no, go to step  [1.f](#en-us_topic_0149610914_li0791101412396).

    4.  <a name="en-us_topic_0149610914_li1859773663819"></a>Obtain the Product Activation Key \(PAK\) from the email indicating successful registration with NVIDIA.

        **Figure  1**  PAK<a name="en-us_topic_0149610914_fig133361216153817"></a>  
        ![](figures/pak.png "pak")

    5.  Enter the PAK obtained in step  [1.d](#en-us_topic_0149610914_li1859773663819)  on the  **Redeem Product Activation Keys**  page and click  **Redeem**.

        **Figure  2**  Redeem Product Activation Keys<a name="en-us_topic_0149610914_fig16617143616380"></a>  
        ![](figures/redeem-product-activation-keys.png "redeem-product-activation-keys")

    6.  <a name="en-us_topic_0149610914_li0791101412396"></a>Specify  **Username**  and  **Password**  and click  **LOGIN**.

        **Figure  3**  Logging in to the official NVIDIA website<a name="en-us_topic_0149610914_fig1367291114395"></a>  
        ![](figures/logging-in-to-the-official-nvidia-website.png "logging-in-to-the-official-nvidia-website")

    7.  Log in at the official NVIDIA website as prompted and choose  **Software & Services**  \>  **Product Information**.

        **Figure  4**  Product Information<a name="en-us_topic_0149610914_fig028419910169"></a>  
        ![](figures/product-information.png "product-information")

    8.  Click the  **Archived Versions**  tab.
    9.  Download the NVIDIA or vGPU driver of the required version. For details, see  [Table 1](#en-us_topic_0149610914_table230940145218).
    10. Decompress the vGPU driver installation package and install the driver that matches your ECS OS.
    11. On the  **Product Download**  page, click  **2019.05 License Manager for Linux**  to download the software license package.

        **Figure  5**  Selecting product information<a name="en-us_topic_0149610914_fig13215124318392"></a>  
        ![](figures/selecting-product-information.png "selecting-product-information")

2.  To install the GPU driver on a G2 ECS, perform the following operations:

    To download the GPU driver, log in at  [http://www.nvidia.com/Download/index.aspx?lang=en-us](http://www.nvidia.com/Download/index.aspx?lang=en-us). You are suggested to select the latest CUDA toolkit version.

    >![](/images/icon-notice.gif) **NOTICE:**   
    >After the GPU driver is installed, run the following command to switch the GPU working mode and restart the ECS \(for example, the GPU driver is installed in  **C:\\Program Files\\NVIDIA Corporation\\NVSMI\\nvidia-smi.exe**\):  
    >**"C:\\Program Files\\NVIDIA Corporation\\NVSMI\\nvidia-smi.exe" -dm 0**  


## SR-IOV NIC Driver<a name="section14162103933018"></a>

If you want to use the created private image to create G2 ECSs, install the SR-IOV NIC driver for the image to improve performance and scalability.

To download the SR-IOV driver, log in at  [https://downloadcenter.intel.com/search?keyword=Intel++Ethernet+Connections+CD](https://downloadcenter.intel.com/search?keyword=Intel++Ethernet+Connections+CD). You are advised to select version 20.4.1 or later.

If error "No Intel adapter found" occurs during the driver installation, refer to  [What Do I Do If a Windows 7 ECS Equipped with an Intel 82599 NIC Reports an Error in SR-IOV Scenarios?](what-do-i-do-if-a-windows-7-ecs-equipped-with-an-intel-82599-nic-reports-an-error-in-sr-iov-scenario.md)  for troubleshooting.

