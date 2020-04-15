# Installing a GRID/vGPU Driver on a GPU-accelerated ECS<a name="EN-US_TOPIC_0149610914"></a>

## Scenarios<a name="section18938132731610"></a>

Before using a GPU-accelerated ECS, install a proper GPU driver on it for GPU acceleration. There are two types of NVIDIA Tesla GPU drivers for GPU-accelerated ECSs, Tesla and GRID/vGPU drivers.

To use graphics acceleration, such as OpenGL, DirectX, or Vulcan, install the GRID/vGPU driver and separately purchase and configure a GRID license. The GRID/vGPU driver with a vDWS license also supports CUDA for both computing and graphics acceleration.

This section describes how to install a GRID/vGPU driver, purchase or apply for a GRID license, and configure the license server.

Process of installing a GRID/vGPU driver:

1.  [Purchasing a GRID License](#section1130184214229)
2.  [Download GRID driver and software license packages.](#section91244318407)
3.  [Deploy and configure the license server.](#section19229135113439)
4.  [Install the GRID driver and configure the license.](#section17545653184812)

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>-   A graphics-accelerated \(G series\) ECS created using a public image has a GRID driver of a specified version installed by default, but the GRID license must be purchased and configured separately. Before using such an ECS, check whether the desired driver has been installed on it and whether the version of the installed driver meets service requirements.  
>-   A computing-accelerated \(P series\) ECS created using a public image has a Tesla driver of a specified version installed by default. Before using such an ECS, check whether the desired driver has been installed on it and whether the version of the installed driver meets service requirements.  
>-   NVIDIA allows you to apply for a 90-day trial license.  
>-   For details about GPU-accelerated ECSs with different specifications and application scenarios, see  [GPU-accelerated ECSs](gpu-accelerated-ecss.md).  

**Table  1**  Acceleration supported by GPU drivers

<a name="table8917107174212"></a>
<table><thead align="left"><tr id="row991219704215"><th class="cellrowborder" valign="top" width="10.97%" id="mcps1.2.9.1.1"><p id="p39120764214"><a name="p39120764214"></a><a name="p39120764214"></a>Driver Type</p>
</th>
<th class="cellrowborder" valign="top" width="12.53%" id="mcps1.2.9.1.2"><p id="p139122774218"><a name="p139122774218"></a><a name="p139122774218"></a>License</p>
</th>
<th class="cellrowborder" valign="top" width="10.89%" id="mcps1.2.9.1.3"><p id="p99125713426"><a name="p99125713426"></a><a name="p99125713426"></a>CUDA</p>
</th>
<th class="cellrowborder" valign="top" width="8.48%" id="mcps1.2.9.1.4"><p id="p209123714425"><a name="p209123714425"></a><a name="p209123714425"></a>OpenGL</p>
</th>
<th class="cellrowborder" valign="top" width="9.4%" id="mcps1.2.9.1.5"><p id="p091214714427"><a name="p091214714427"></a><a name="p091214714427"></a>DirectX</p>
</th>
<th class="cellrowborder" valign="top" width="11.29%" id="mcps1.2.9.1.6"><p id="p691216704210"><a name="p691216704210"></a><a name="p691216704210"></a>Vulcan</p>
</th>
<th class="cellrowborder" valign="top" width="18.529999999999998%" id="mcps1.2.9.1.7"><p id="p179123724213"><a name="p179123724213"></a><a name="p179123724213"></a>Application Scenario</p>
</th>
<th class="cellrowborder" valign="top" width="17.91%" id="mcps1.2.9.1.8"><p id="p18178924144619"><a name="p18178924144619"></a><a name="p18178924144619"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row96781191420"><td class="cellrowborder" valign="top" width="10.97%" headers="mcps1.2.9.1.1 "><p id="p1591447114213"><a name="p1591447114213"></a><a name="p1591447114213"></a>GRID/vGPU driver</p>
</td>
<td class="cellrowborder" valign="top" width="12.53%" headers="mcps1.2.9.1.2 "><p id="p14915207134210"><a name="p14915207134210"></a><a name="p14915207134210"></a>Required</p>
</td>
<td class="cellrowborder" valign="top" width="10.89%" headers="mcps1.2.9.1.3 "><p id="p16915273428"><a name="p16915273428"></a><a name="p16915273428"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="8.48%" headers="mcps1.2.9.1.4 "><p id="p119161479424"><a name="p119161479424"></a><a name="p119161479424"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="9.4%" headers="mcps1.2.9.1.5 "><p id="p6917177104211"><a name="p6917177104211"></a><a name="p6917177104211"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="11.29%" headers="mcps1.2.9.1.6 "><p id="p4917207154214"><a name="p4917207154214"></a><a name="p4917207154214"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="18.529999999999998%" headers="mcps1.2.9.1.7 "><p id="p189178715422"><a name="p189178715422"></a><a name="p189178715422"></a>3D rendering, graphics workstation, and game acceleration</p>
</td>
<td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.2.9.1.8 "><p id="p197573180464"><a name="p197573180464"></a><a name="p197573180464"></a>The GRID/vGPU driver must be paid and requires a license to accelerate graphics and image applications.</p>
</td>
</tr>
<tr id="row9914147204218"><td class="cellrowborder" valign="top" width="10.97%" headers="mcps1.2.9.1.1 "><p id="p1391214714214"><a name="p1391214714214"></a><a name="p1391214714214"></a>Tesla driver</p>
</td>
<td class="cellrowborder" valign="top" width="12.53%" headers="mcps1.2.9.1.2 "><p id="p13913971429"><a name="p13913971429"></a><a name="p13913971429"></a>Not required</p>
</td>
<td class="cellrowborder" valign="top" width="10.89%" headers="mcps1.2.9.1.3 "><p id="p10913197154217"><a name="p10913197154217"></a><a name="p10913197154217"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="8.48%" headers="mcps1.2.9.1.4 "><p id="p89131972421"><a name="p89131972421"></a><a name="p89131972421"></a>Not supported</p>
</td>
<td class="cellrowborder" valign="top" width="9.4%" headers="mcps1.2.9.1.5 "><p id="p129137715422"><a name="p129137715422"></a><a name="p129137715422"></a>Not supported</p>
</td>
<td class="cellrowborder" valign="top" width="11.29%" headers="mcps1.2.9.1.6 "><p id="p79138712422"><a name="p79138712422"></a><a name="p79138712422"></a>Not supported</p>
</td>
<td class="cellrowborder" valign="top" width="18.529999999999998%" headers="mcps1.2.9.1.7 "><p id="p99135734212"><a name="p99135734212"></a><a name="p99135734212"></a>Scientific computing, deep learning training, and inference</p>
</td>
<td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.2.9.1.8 "><p id="p137571518174618"><a name="p137571518174618"></a><a name="p137571518174618"></a>The Tesla driver is downloaded free of charge and usually used with NVIDIA CUDA SDK to accelerate general computing applications.</p>
</td>
</tr>
</tbody>
</table>

## Purchasing a GRID License<a name="section1130184214229"></a>

-   Purchase a license.

    To obtain an official license, contact NVIDIA or their NVIDIA agent in your local country or region.

-   Apply for a trial license.

    Log in at the  [official NVIDIA website](https://www.nvidia.com/object/nvidia-enterprise-account.html)  and enter desired information.

    For details about how to register an account and apply for a trial license, see  [official NVIDIA help page](https://nvid.nvidia.com/NvidiaUtilities/#/needHelp).

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >The method of using a trial license is the same as that of using an official license. You can use an official license to activate an account with a trial license to prevent repetitive registration. The trial license has a validity period of 90 days. After the trial license expires, it cannot be used any more. Purchase an official license then.  

    **Figure  1**  Applying for a trial license<a name="fig45088922717"></a>  
    ![](figures/applying-for-a-trial-license.png "applying-for-a-trial-license")


## Downloading GRID Driver and Software License Packages<a name="section91244318407"></a>

1.  [Obtain the driver installation package](https://www.nvidia.com/grid-eval)  required for an OS. For details, see  [Table 2](#table230940145218).

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >For a GPU passthrough ECS, select a GRID driver version as required.  
    >For a GPU virtualization ECS, select a driver version based on  [Table 2](#table230940145218).  

    **Table  2**  GRID/vGPU driver versions supported by GPU-accelerated ECSs

    <a name="table230940145218"></a>
    <table><thead align="left"><tr id="row1230860145216"><th class="cellrowborder" valign="top" width="10.891089108910892%" id="mcps1.2.6.1.1"><p id="p103087005217"><a name="p103087005217"></a><a name="p103087005217"></a>ECS Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.82178217821782%" id="mcps1.2.6.1.2"><p id="p831263814595"><a name="p831263814595"></a><a name="p831263814595"></a>GPU Attachment</p>
    </th>
    <th class="cellrowborder" valign="top" width="28.71287128712871%" id="mcps1.2.6.1.3"><p id="p10464537154117"><a name="p10464537154117"></a><a name="p10464537154117"></a>OS</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.762376237623762%" id="mcps1.2.6.1.4"><p id="p130820145216"><a name="p130820145216"></a><a name="p130820145216"></a>Driver Version</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.81188118811881%" id="mcps1.2.6.1.5"><p id="p32836161156"><a name="p32836161156"></a><a name="p32836161156"></a>CPU Architecture</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1443710550468"><td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.6.1.1 "><p id="p0222125913469"><a name="p0222125913469"></a><a name="p0222125913469"></a>G6</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.6.1.2 "><p id="p9222359154617"><a name="p9222359154617"></a><a name="p9222359154617"></a>GPU virtualization</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.2.6.1.3 "><a name="ul1341917351493"></a><a name="ul1341917351493"></a><ul id="ul1341917351493"><li>Windows Server 2016 Standard 64bit</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.6.1.4 "><p id="p322265913467"><a name="p322265913467"></a><a name="p322265913467"></a>GRID 7.1: NVIDIA vGPU for Linux KVM</p>
    <p id="p1753013398443"><a name="p1753013398443"></a><a name="p1753013398443"></a>Verify other driver versions.</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.6.1.5 "><p id="p1828331614520"><a name="p1828331614520"></a><a name="p1828331614520"></a>x86_64</p>
    </td>
    </tr>
    <tr id="row2017804416017"><td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.6.1.1 "><p id="p1617817444014"><a name="p1617817444014"></a><a name="p1617817444014"></a>G2</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.6.1.2 "><p id="p1617864420013"><a name="p1617864420013"></a><a name="p1617864420013"></a>GPU passthrough</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.2.6.1.3 "><a name="ul1535413327215"></a><a name="ul1535413327215"></a><ul id="ul1535413327215"><li>Windows Server 2012</li><li>Windows Server 2008</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.6.1.4 "><p id="p61788448016"><a name="p61788448016"></a><a name="p61788448016"></a>Select a version as required.</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.6.1.5 "><p id="p728317168515"><a name="p728317168515"></a><a name="p728317168515"></a>x86_64</p>
    </td>
    </tr>
    <tr id="row53092007529"><td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.6.1.1 "><p id="p93091200526"><a name="p93091200526"></a><a name="p93091200526"></a>G1</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.6.1.2 "><p id="p1631215381599"><a name="p1631215381599"></a><a name="p1631215381599"></a>GPU virtualization</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.2.6.1.3 "><a name="ul1854703165713"></a><a name="ul1854703165713"></a><ul id="ul1854703165713"><li>Windows Server 2016</li><li>Windows Server 2012</li><li>Windows Server 2008</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.6.1.4 "><p id="p1330911065220"><a name="p1330911065220"></a><a name="p1330911065220"></a>vGPU 4.1: GRID for UVP</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.6.1.5 "><p id="p152839165513"><a name="p152839165513"></a><a name="p152839165513"></a>x86_64</p>
    </td>
    </tr>
    <tr id="row1383513813532"><td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.6.1.1 "><p id="p10494441165310"><a name="p10494441165310"></a><a name="p10494441165310"></a>P2v</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.6.1.2 "><p id="p18494164165320"><a name="p18494164165320"></a><a name="p18494164165320"></a>GPU passthrough</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.2.6.1.3 "><a name="ul94948412537"></a><a name="ul94948412537"></a><ul id="ul94948412537"><li>Windows Server 2016 Standard 64bit</li><li>Windows Server 2012 R2 Standard 64bit</li><li>Ubuntu Server 16.04 64bit</li><li>CentOS 7.4 64bit</li><li>EulerOS 2.2 64bit</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.6.1.4 "><p id="p1049454175316"><a name="p1049454175316"></a><a name="p1049454175316"></a>Select a version as required.</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.6.1.5 "><p id="p5283216652"><a name="p5283216652"></a><a name="p5283216652"></a>x86_64</p>
    </td>
    </tr>
    <tr id="row8919171710547"><td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.6.1.1 "><p id="p11919717115417"><a name="p11919717115417"></a><a name="p11919717115417"></a>P2</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.6.1.2 "><p id="p14313153819594"><a name="p14313153819594"></a><a name="p14313153819594"></a>GPU passthrough</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.2.6.1.3 "><p id="p1546463718419"><a name="p1546463718419"></a><a name="p1546463718419"></a>Ubuntu Server 16.04 64bit</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.6.1.4 "><p id="p2919117165413"><a name="p2919117165413"></a><a name="p2919117165413"></a>Select a version as required.</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.6.1.5 "><p id="p1028351612512"><a name="p1028351612512"></a><a name="p1028351612512"></a>x86_64</p>
    </td>
    </tr>
    <tr id="row1452816207544"><td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.6.1.1 "><p id="p2528202025418"><a name="p2528202025418"></a><a name="p2528202025418"></a>P1</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.6.1.2 "><p id="p96883531726"><a name="p96883531726"></a><a name="p96883531726"></a>GPU passthrough</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.2.6.1.3 "><a name="ul1740013273448"></a><a name="ul1740013273448"></a><ul id="ul1740013273448"><li>Windows Server 2012 R2 Standard 64bit</li><li>Ubuntu Server 16.04 64bit</li><li>CentOS 7.4 64bit</li><li>Debian 9.0 64bit</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.6.1.4 "><p id="p19688053127"><a name="p19688053127"></a><a name="p19688053127"></a>Select a version as required.</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.6.1.5 "><p id="p22837161852"><a name="p22837161852"></a><a name="p22837161852"></a>x86_64</p>
    </td>
    </tr>
    </tbody>
    </table>

2.  After the registration, log in at the  [official NVIDIA website](https://nvid.nvidia.com/dashboard/)  and enter the account.
3.  Check whether NVIDIA is used for the first time.
    1.  If yes, go to step  [4](#li1859773663819).
    2.  If no, go to step  [6](#li0791101412396).

4.  <a name="li1859773663819"></a>Obtain the Product Activation Key \(PAK\) from the email indicating successful registration with NVIDIA.

    **Figure  2**  PAK<a name="fig133361216153817"></a>  
    ![](figures/pak.png "pak")

5.  Enter the PAK obtained in step  [4](#li1859773663819)  on the  **Redeem Product Activation Keys**  page and click  **Redeem**.

    **Figure  3**  Redeem Product Activation Keys<a name="fig16617143616380"></a>  
    ![](figures/redeem-product-activation-keys.png "redeem-product-activation-keys")

6.  <a name="li0791101412396"></a>Specify  **Username**  and  **Password**  and click  **LOGIN**.

    **Figure  4**  Logging in to the official NVIDIA website<a name="fig1367291114395"></a>  
    ![](figures/logging-in-to-the-official-nvidia-website.png "logging-in-to-the-official-nvidia-website")

7.  Log in at the official NVIDIA website as prompted and choose  **Software & Services**  \>  **Product Information**.

    **Figure  5**  Product Information<a name="fig028419910169"></a>  
    ![](figures/product-information.png "product-information")

8.  Click the  **Archived Versions**  tab.
9.  Download the NVIDIA or vGPU driver of the required version. For details, see  [Table 2](#table230940145218).
10. Decompress the vGPU driver installation package and install the driver that matches your ECS OS.
11. On the  **Product Download**  page, click  **2019.05 License Manager for Linux**  to download the software license package.

    **Figure  6**  Selecting product information<a name="fig13215124318392"></a>  
    ![](figures/selecting-product-information.png "selecting-product-information")


## Deploying and Configuring the License Server<a name="section19229135113439"></a>

The following uses an ECS running CentOS 7.5 as an example to describe how to deploy and configure the license server on the ECS.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>-   The target ECS must have at least 2 vCPUs and 4 GB of memory.  
>-   Ensure that the MAC address of the target ECS has been recorded.  
>-   If the license server is used in the production environment, deploy it in high availability mode. For details, see  [official NVIDIA documentation for license server high availability](https://docs.nvidia.com/grid/ls/2019.05/grid-license-server-user-guide/index.html#license-server-high-availability).  

1.  Configure the network.
    -   If the license server is to be accessed using the VPC, ensure that the license server and the GPU-accelerated ECS with the GRID driver installed are in the same VPC subnet.
    -   If the license server is to be accessed using a public IP address, configure the security group to which license server belongs and add inbound rules for TCP 7070 and TCP 8080.


1.  Install the license server.

    For details, see the  [official NVIDIA documentation for installing the license server](https://docs.nvidia.com/grid/ls/latest/grid-license-server-user-guide/index.html#installing-nvidia-grid-license-server).

2.  Obtain the license file.
    1.  Log in at  [http://nvid.nvidia.com/dashboard/](http://nvid.nvidia.com/dashboard/)  again and select  **Register License Server**.

        **Figure  7**  Selecting Register License Server<a name="fig1319854518598"></a>  
        ![](figures/selecting-register-license-server.png "selecting-register-license-server")

    2.  Enter the MAC address \(no colons are allowed in the MAC address\) of the license server in the  **MAC address**  text box and click  **Create**. If two ECSs are deployed to work in active/standby mode, enter the MAC addresses of the two ECSs in the table.

        **Figure  8**  Entering the MAC addresses of the ECSs on which the license server is deployed<a name="fig1311314141015"></a>  
        ![](figures/entering-the-mac-addresses-of-the-ecss-on-which-the-license-server-is-deployed.png "entering-the-mac-addresses-of-the-ecss-on-which-the-license-server-is-deployed")

    3.  On the  **View Server**  page, click  **Map Add-Ons**.

        **Figure  9**  Map Add-Ons<a name="fig14172558038"></a>  
        ![](figures/map-add-ons.png "map-add-ons")

    4.  On the  **Map Add-Ons**  page, set  **Qty to Add**  and click  **Map Add-Ons**.

        **Figure  10**  Setting  **Qty to Add**<a name="fig885115301363"></a>  
        ![](figures/setting-qty-to-add.png "setting-qty-to-add")

    5.  Download the license file.

        **Figure  11**  Downloading the license file<a name="fig19995314613"></a>  
        ![](figures/downloading-the-license-file.png "downloading-the-license-file")

3.  In the web browser, access the homepage of the license server management page using the link configured during the installation.

    Default URL: http://_IP address of the ECS_:8080/licserver

4.  Choose  **License Server**  \>  **License Management**, select the .bin license file to be uploaded, and click  **Upload**.

    **Figure  12**  Qty to Add<a name="fig101141159980"></a>  
    ![](figures/qty-to-add.png "qty-to-add")


## Installing the GRID Driver and Configuring the License<a name="section17545653184812"></a>

1.  Install the GRID/vGPU driver of a desired version, for example, on a GPU-accelerated Windows ECS.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >Microsoft remote login protocols do not support GPU 3D hardware acceleration. To use this function, install third-party desktop protocol software, such as VNC, PCoIP, TeamViewer, or NICE DCV, and access the ECS through the client.  

2.  Open the NVIDIA control panel on the Windows control panel.
3.  Enter the IP address and port number of the deployed license server in the level-1 license server, and then click  **Apply**. If the message indicating that you have obtained a GRID/vGPU license, the installation is successful. Additionally, the MAC address of the GPU-accelerated ECS with the GRID driver installed is displayed on the  **Licensed Clients**  page of the license server management console.

    **Figure  13**  License server management console<a name="fig7104162713349"></a>  
    ![](figures/license-server-management-console.png "license-server-management-console")


