# How Do I Install the NVIDIA Driver on a P1 ECS?<a name="EN-US_TOPIC_0093842586"></a>

## Prerequisites<a name="section2413882291912"></a>

-   The target ECS has had an EIP bound.
-   You have obtained the driver installation package required for an OS. For details, see  [Table 1](#en-us_topic_0093345963_table121731221584).

**Table  1**  NVIDIA drivers

<a name="en-us_topic_0093345963_table121731221584"></a>
<table><thead align="left"><tr id="en-us_topic_0093345963_row1173321281"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="en-us_topic_0093345963_p13173621816"><a name="en-us_topic_0093345963_p13173621816"></a><a name="en-us_topic_0093345963_p13173621816"></a>OS</p>
</th>
<th class="cellrowborder" valign="top" width="36%" id="mcps1.2.4.1.2"><p id="en-us_topic_0093345963_p1517317215810"><a name="en-us_topic_0093345963_p1517317215810"></a><a name="en-us_topic_0093345963_p1517317215810"></a>Driver</p>
</th>
<th class="cellrowborder" valign="top" width="44%" id="mcps1.2.4.1.3"><p id="en-us_topic_0093345963_p191731422081"><a name="en-us_topic_0093345963_p191731422081"></a><a name="en-us_topic_0093345963_p191731422081"></a>How to Obtain</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0093345963_row111733211812"><td class="cellrowborder" rowspan="2" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0093345963_p817310213813"><a name="en-us_topic_0093345963_p817310213813"></a><a name="en-us_topic_0093345963_p817310213813"></a>Ubuntu 16.04</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0093345963_p31731929816"><a name="en-us_topic_0093345963_p31731929816"></a><a name="en-us_topic_0093345963_p31731929816"></a>GPU driver installation package <strong id="en-us_topic_0093345963_b842352706111915"><a name="en-us_topic_0093345963_b842352706111915"></a><a name="en-us_topic_0093345963_b842352706111915"></a>NVIDIA-Linux-x86_64-375.66.run</strong></p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0093345963_p917318216819"><a name="en-us_topic_0093345963_p917318216819"></a><a name="en-us_topic_0093345963_p917318216819"></a><a href="http://www.nvidia.com/download/driverResults.aspx/118955/en-us" target="_blank" rel="noopener noreferrer">http://www.nvidia.com/download/driverResults.aspx/118955/en-us</a></p>
</td>
</tr>
<tr id="en-us_topic_0093345963_row4589124216911"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0093345963_p859194214910"><a name="en-us_topic_0093345963_p859194214910"></a><a name="en-us_topic_0093345963_p859194214910"></a>CUDA Toolkit installation package <strong id="en-us_topic_0093345963_b842352706111938"><a name="en-us_topic_0093345963_b842352706111938"></a><a name="en-us_topic_0093345963_b842352706111938"></a>cuda_8.0.61_375.26_linux.run</strong></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0093345963_p205911142897"><a name="en-us_topic_0093345963_p205911142897"></a><a name="en-us_topic_0093345963_p205911142897"></a><a href="https://developer.nvidia.com/compute/cuda/8.0/Prod2/local_installers/cuda_8.0.61_375.26_linux-run" target="_blank" rel="noopener noreferrer">https://developer.nvidia.com/compute/cuda/8.0/Prod2/local_installers/cuda_8.0.61_375.26_linux-run</a></p>
</td>
</tr>
<tr id="en-us_topic_0093345963_row0173521783"><td class="cellrowborder" rowspan="2" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0093345963_p16173162288"><a name="en-us_topic_0093345963_p16173162288"></a><a name="en-us_topic_0093345963_p16173162288"></a>CentOS 7.4</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0093345963_p730815123107"><a name="en-us_topic_0093345963_p730815123107"></a><a name="en-us_topic_0093345963_p730815123107"></a>GPU driver installation package <strong id="en-us_topic_0093345963_b427040171"><a name="en-us_topic_0093345963_b427040171"></a><a name="en-us_topic_0093345963_b427040171"></a>NVIDIA-Linux-x86_64-375.66.run</strong></p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0093345963_p14461202015150"><a name="en-us_topic_0093345963_p14461202015150"></a><a name="en-us_topic_0093345963_p14461202015150"></a><a href="http://www.nvidia.com/download/driverResults.aspx/118955/en-us" target="_blank" rel="noopener noreferrer">http://www.nvidia.com/download/driverResults.aspx/118955/en-us</a></p>
</td>
</tr>
<tr id="en-us_topic_0093345963_row842018532920"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0093345963_p0308121211107"><a name="en-us_topic_0093345963_p0308121211107"></a><a name="en-us_topic_0093345963_p0308121211107"></a>CUDA Toolkit installation package <strong id="en-us_topic_0093345963_b1857082158"><a name="en-us_topic_0093345963_b1857082158"></a><a name="en-us_topic_0093345963_b1857082158"></a>cuda_8.0.61_375.26_linux.run</strong></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0093345963_p2462920141518"><a name="en-us_topic_0093345963_p2462920141518"></a><a name="en-us_topic_0093345963_p2462920141518"></a><a href="https://developer.nvidia.com/compute/cuda/8.0/Prod2/local_installers/cuda_8.0.61_375.26_linux-run" target="_blank" rel="noopener noreferrer">https://developer.nvidia.com/compute/cuda/8.0/Prod2/local_installers/cuda_8.0.61_375.26_linux-run</a></p>
</td>
</tr>
<tr id="en-us_topic_0093345963_row1981748163016"><td class="cellrowborder" rowspan="2" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0093345963_p13817482306"><a name="en-us_topic_0093345963_p13817482306"></a><a name="en-us_topic_0093345963_p13817482306"></a>Debian 9.0</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0093345963_p12844883011"><a name="en-us_topic_0093345963_p12844883011"></a><a name="en-us_topic_0093345963_p12844883011"></a>GPU driver installation package <strong id="en-us_topic_0093345963_b301822939"><a name="en-us_topic_0093345963_b301822939"></a><a name="en-us_topic_0093345963_b301822939"></a>NVIDIA-Linux-x86_64-384.81.run</strong></p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0093345963_p2081448153010"><a name="en-us_topic_0093345963_p2081448153010"></a><a name="en-us_topic_0093345963_p2081448153010"></a><a href="http://www.nvidia.com/download/driverResults.aspx/124722/en-us" target="_blank" rel="noopener noreferrer">http://www.nvidia.com/download/driverResults.aspx/124722/en-us</a></p>
</td>
</tr>
<tr id="en-us_topic_0093345963_row1017372982"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0093345963_p1919002911104"><a name="en-us_topic_0093345963_p1919002911104"></a><a name="en-us_topic_0093345963_p1919002911104"></a>CUDA Toolkit installation package <strong id="en-us_topic_0093345963_b919071598"><a name="en-us_topic_0093345963_b919071598"></a><a name="en-us_topic_0093345963_b919071598"></a>cuda_9.0.176_384.81_linux.run</strong></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0093345963_p171735213819"><a name="en-us_topic_0093345963_p171735213819"></a><a name="en-us_topic_0093345963_p171735213819"></a><a href="https://developer.nvidia.com/compute/cuda/9.0/Prod/local_installers/cuda_9.0.176_384.81_linux-run" target="_blank" rel="noopener noreferrer">https://developer.nvidia.com/compute/cuda/9.0/Prod/local_installers/cuda_9.0.176_384.81_linux-run</a></p>
</td>
</tr>
</tbody>
</table>

## Procedure<a name="section441725229194"></a>

The procedure for installing the NVIDIA driver varies according to the OS.

-   **Ubuntu 16.04 64bit**

1.  Log in to the target ECS and run the following command to switch to user  **root**:

    **sudo su**

2.  \(Optional\) Install the GCC and g++ software.

    Perform this step only if the GCC and g++ software has not been installed.

    **apt-get install gcc**

    **apt-get install g++**

    **apt-get install make**

3.  \(Optional\) Disable the Nouveau driver.

    Perform this step if the Nouveau driver has been installed on the target ECS. This prevents conflict with the NVIDIA driver installation.

    1.  Run the following command to check whether the Nouveau driver is running on the target ECS:

        **lsmod | grep nouveau**

        -   If yes, go to  [3.b](#en-us_topic_0093345963_li2691446193813).
        -   If no, go to  [4](#en-us_topic_0093345963_li7971016194610).

    2.  <a name="en-us_topic_0093345963_li2691446193813"></a>Add the following statement to the end of the  **/etc/modprobe.d/blacklist.conf**  file:

        **blacklist nouveau**

        **options nouveau modeset=0**

    3.  Run the following commands to back up and create an initramfs application:

        **mv /boot/initramfs-$\(uname -r\).img /boot/initramfs-$\(uname -r\).img.bak**

        **update-initramfs -u**

    4.  Run the following command to restart the ECS:

        **reboot**

4.  <a name="en-us_topic_0093345963_li7971016194610"></a>\(Optional\) Disable the X service.

    If the ECS has been logged in using the GUI, disable the X service before installing the NVIDIA driver.

    1.  Run the following command to switch to multi-user mode:

        **systemctl set-default multi-user.target**

    2.  Run the following command to restart the ECS:

        **reboot**

5.  \(Optional\) Install the GPU driver.

    You can either use the GPU driver provided in the CUDA Toolkit installation package or download the required GPU driver. Unless otherwise specified, you are advised to install GPU driver  **NVIDIA-Linux-x86\_64-375.66.run**, which has been fully verified.

    1.  Upload the GPU driver installation package  **NVIDIA-Linux-x86\_64-_xxx.yy_.run**  to the  **/tmp**  directory of the ECS.

        To download the GPU driver, log in at  [http://www.nvidia.com/Download/index.aspx?lang=en](http://www.nvidia.com/Download/index.aspx?lang=en).

        **Figure  1**  Downloading the GPU driver<a name="en-us_topic_0093345963_fig3284155103612"></a>  
        ![](figures/downloading-the-gpu-driver.png "downloading-the-gpu-driver")

    2.  Run the following command to install the GPU driver:

        **sh ./NVIDIA-Linux-x86\_64-_xxx.yy_.run**

    3.  Run the following command to delete the installation package:

        **rm -f NVIDIA-Linux-x86\_64-_xxx.yy_.run**

6.  Install the CUDA Toolkit.

    Unless otherwise specified, you are advised to install CUDA Toolkit  **cuda\_8.0.61\_375.26\_linux.run**, which has been fully verified.

    1.  Upload the CUDA Toolkit installation package  **cuda\__a.b.cc_\__xxx.yy_\_linux.run**  to the  **/tmp**  directory of the ECS.

        To download the CUDA Toolkit, log in at  [https://developer.nvidia.com/cuda-downloads](https://developer.nvidia.com/cuda-downloads).

    2.  Run the following command to change the permission:

        **chmod +x cuda\__a.b.cc_\__xxx.yy_\_linux.run**

    3.  Run the following command to install the CUDA Toolkit:

        **./cuda\__a.b.cc_\__xxx.yy_\_linux.run -toolkit -samples -silent -override --tmpdir=/tmp/**

    4.  Run the following command to delete the installation package:

        **rm -f cuda\__a.b.cc_\__xxx.yy_\_linux.run**

    5.  Run the following commands to check whether the installation is successful:

        **cd /usr/local/cuda/samples/1\_Utilities/deviceQueryDrv/**

        **make**

        **./deviceQueryDrv**

        If the terminal display contains "Result = PASS", both CUDA Toolkit and GPU driver have been installed.

        ```
        ./deviceQueryDrv Starting...  
           
         CUDA Device Query (Driver API) statically linked version   
         Detected 1 CUDA Capable device(s)  
           
         Device 0: "Tesla P100-PCIE-16GB"  
           CUDA Driver Version:                           8.0  
           CUDA Capability Major/Minor version number:    6.0  
           Total amount of global memory:                 16276 MBytes (17066885120 bytes)  
           (56) Multiprocessors, ( 64) CUDA Cores/MP:     3584 CUDA Cores  
           GPU Max Clock rate:                            1329 MHz (1.33 GHz)  
           Memory Clock rate:                             715 Mhz  
           Memory Bus Width:                              4096-bit  
           L2 Cache Size:                                 4194304 bytes  
           Max Texture Dimension Sizes                    1D=(131072) 2D=(131072, 65536) 3D=(16384, 16384, 16384)  
           Maximum Layered 1D Texture Size, (num) layers  1D=(32768), 2048 layers  
           Maximum Layered 2D Texture Size, (num) layers  2D=(32768, 32768), 2048 layers  
           Total amount of constant memory:               65536 bytes  
           Total amount of shared memory per block:       49152 bytes  
           Total number of registers available per block: 65536  
           Warp size:                                     32  
           Maximum number of threads per multiprocessor:  2048  
           Maximum number of threads per block:           1024  
           Max dimension size of a thread block (x,y,z): (1024, 1024, 64)  
           Max dimension size of a grid size (x,y,z):    (2147483647, 65535, 65535)  
           Texture alignment:                             512 bytes  
           Maximum memory pitch:                          2147483647 bytes  
           Concurrent copy and kernel execution:          Yes with 2 copy engine(s)  
           Run time limit on kernels:                     No  
           Integrated GPU sharing Host Memory:            No  
           Support host page-locked memory mapping:       Yes  
           Concurrent kernel execution:                   Yes  
           Alignment requirement for Surfaces:            Yes  
           Device has ECC support:                        Enabled  
           Device supports Unified Addressing (UVA):      Yes  
           Device PCI Domain ID / Bus ID / location ID:   0 / 0 / 6  
           Compute Mode:  
              < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >  
         Result = PASS 
        ```



-   **CentOS 7.4**

1.  Log in to the target ECS and run the following command to switch to user  **root**:

    **sudo su**

2.  \(Optional\) Install GCC, g++, and kernel-devel.

    Perform this step only if GCC, g++, and kernel-devel have not been installed.

    **yum install gcc**

    **yum install gcc-c++**

    **yum install make**

    **yum install kernel-devel-\`uname -r\`**

3.  \(Optional\) Disable the Nouveau driver.

    Perform this step if the Nouveau driver has been installed on the target ECS. This prevents conflict with the NVIDIA driver installation.

    1.  Run the following command to check whether the Nouveau driver is running on the target ECS:

        **lsmod | grep nouveau**

        -   If yes, go to  [3.b](#en-us_topic_0093345963_li17783295461).
        -   If no, go to  [4](#en-us_topic_0093345963_li7971016194610).

    2.  <a name="en-us_topic_0093345963_li17783295461"></a>Add the following statement to the end of the  **/etc/modprobe.d/blacklist.conf**  file:

        **blacklist nouveau**

    3.  Run the following commands to back up and create an initramfs application:

        **mv /boot/initramfs-$\(uname -r\).img /boot/initramfs-$\(uname -r\).img.bak**

        **dracut -v /boot/initramfs-$\(uname -r\).img $\(uname -r\)**

    4.  Run the following command to restart the ECS:

        **reboot**

4.  \(Optional\) Disable the X service.

    If the ECS has been logged in using the GUI, disable the X service before installing the NVIDIA driver.

    1.  Run the following command to switch to multi-user mode:

        **systemctl set-default multi-user.target**

    2.  Run the following command to restart the ECS:

        **reboot**

5.  \(Optional\) Install the GPU driver.

    You can either use the GPU driver provided in the CUDA Toolkit installation package or download the required GPU driver. Unless otherwise specified, you are advised to install GPU driver  **NVIDIA-Linux-x86\_64-375.66.run**, which has been fully verified.

    1.  Upload the GPU driver installation package  **NVIDIA-Linux-x86\_64-_xxx.yy_.run**  to the  **/tmp**  directory of the ECS.

        To download the GPU driver, log in at  [http://www.nvidia.com/Download/index.aspx?lang=en](http://www.nvidia.com/Download/index.aspx?lang=en).

        **Figure  2**  Downloading the driver installation package<a name="en-us_topic_0093345963_EN-US_TOPIC_0093345963_fig3284155103612"></a>  
        ![](figures/downloading-the-driver-installation-package.png "downloading-the-driver-installation-package")

    2.  Run the following command to install the GPU driver:

        **sh ./NVIDIA-Linux-x86\_64-_xxx.yy_.run**

    3.  Run the following command to delete the installation package:

        **rm -f NVIDIA-Linux-x86\_64-_xxx.yy_.run**

6.  Install the CUDA Toolkit.

    Unless otherwise specified, you are advised to install CUDA Toolkit  **cuda\_8.0.61\_375.26\_linux.run**, which has been fully verified.

    1.  Upload the CUDA Toolkit installation package  **cuda\__a.b.cc_\__xxx.yy_\_linux.run**  to the  **/tmp**  directory of the ECS.

        To download the CUDA Toolkit, log in at  [https://developer.nvidia.com/cuda-downloads](https://developer.nvidia.com/cuda-downloads).

    2.  Run the following command to change the permission:

        **chmod +x cuda\__a.b.cc_\__xxx.yy_\_linux.run**

    3.  Run the following command to install the CUDA Toolkit:

        **./cuda\__a.b.cc_\__xxx.yy_\_linux.run -toolkit -samples -silent -override --tmpdir=/tmp/**

    4.  Run the following command to delete the installation package:

        **rm -f cuda\__a.b.cc_\__xxx.yy_\_linux.run**

    5.  Run the following commands to check whether the installation is successful:

        **cd /usr/local/cuda/samples/1\_Utilities/deviceQueryDrv/**

        **make**

        **./deviceQueryDrv**

        If the terminal display contains "Result = PASS", both CUDA Toolkit and GPU driver have been installed.

        ```
        ./deviceQueryDrv Starting...  
           
         CUDA Device Query (Driver API) statically linked version   
         Detected 1 CUDA Capable device(s)  
           
         Device 0: "Tesla P100-PCIE-16GB"  
           CUDA Driver Version:                           8.0  
           CUDA Capability Major/Minor version number:    6.0  
           Total amount of global memory:                 16276 MBytes (17066885120 bytes)  
           (56) Multiprocessors, ( 64) CUDA Cores/MP:     3584 CUDA Cores  
           GPU Max Clock rate:                            1329 MHz (1.33 GHz)  
           Memory Clock rate:                             715 Mhz  
           Memory Bus Width:                              4096-bit  
           L2 Cache Size:                                 4194304 bytes  
           Max Texture Dimension Sizes                    1D=(131072) 2D=(131072, 65536) 3D=(16384, 16384, 16384)  
           Maximum Layered 1D Texture Size, (num) layers  1D=(32768), 2048 layers  
           Maximum Layered 2D Texture Size, (num) layers  2D=(32768, 32768), 2048 layers  
           Total amount of constant memory:               65536 bytes  
           Total amount of shared memory per block:       49152 bytes  
           Total number of registers available per block: 65536  
           Warp size:                                     32  
           Maximum number of threads per multiprocessor:  2048  
           Maximum number of threads per block:           1024  
           Max dimension size of a thread block (x,y,z): (1024, 1024, 64)  
           Max dimension size of a grid size (x,y,z):    (2147483647, 65535, 65535)  
           Texture alignment:                             512 bytes  
           Maximum memory pitch:                          2147483647 bytes  
           Concurrent copy and kernel execution:          Yes with 2 copy engine(s)  
           Run time limit on kernels:                     No  
           Integrated GPU sharing Host Memory:            No  
           Support host page-locked memory mapping:       Yes  
           Concurrent kernel execution:                   Yes  
           Alignment requirement for Surfaces:            Yes  
           Device has ECC support:                        Enabled  
           Device supports Unified Addressing (UVA):      Yes  
           Device PCI Domain ID / Bus ID / location ID:   0 / 0 / 6  
           Compute Mode:  
              < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >  
         Result = PASS 
        ```



-   **Debian 9.0 OS**

1.  Log in to the target ECS and run the following command to switch to user  **root**:

    **sudo su**

2.  \(Optional\) Install the dependency software GCC and g++ of the NVIDIA driver.

    Perform this step only if the GCC and g++ software has not been installed.

    **apt-get install gcc**

    **apt-get install g++**

    **apt-get install make**

    **apt-get install linux-headers-$\(uname -r\)**

3.  \(Optional\) Disable the Nouveau driver.

    Perform this step if the Nouveau driver has been installed on the target ECS. This prevents conflict with the NVIDIA driver installation.

    1.  Run the following command to check whether the Nouveau driver is running on the target ECS:

        **lsmod | grep nouveau**

        -   If yes, go to  [3.b](#en-us_topic_0093345963_li948211510131).
        -   If no, go to  [4](#en-us_topic_0093345963_li151251998136).

    2.  <a name="en-us_topic_0093345963_li948211510131"></a>Add the following statement to the end of the  **/etc/modprobe.d/blacklist.conf**  file:

        **blacklist nouveau**

        **options nouveau modeset=0**

    3.  Run the following commands to back up and create an initramfs application:

        **mv /boot/initramfs-$\(uname -r\).img /boot/initramfs-$\(uname -r\).img.bak**

        **update-initramfs -u**

    4.  Run the following command to restart the ECS:

        **reboot**

4.  <a name="en-us_topic_0093345963_li151251998136"></a>\(Optional\) Disable the X service.

    If the ECS has been logged in using the GUI, disable the X service before installing the NVIDIA driver.

    1.  Run the following command to switch to multi-user mode:

        **systemctl set-default multi-user.target**

    2.  Run the following command to restart the ECS:

        **reboot**

5.  \(Optional\) Install the GPU driver.

    You can either use the GPU driver provided in the CUDA Toolkit installation package or download the required GPU driver. Unless otherwise specified, you are advised to install GPU driver  **NVIDIA-Linux-x86\_64-384.81.run**, which has been fully verified.

    1.  Upload the GPU driver installation package  **NVIDIA-Linux-x86\_64-_xxx.yy_.run**  to the  **/tmp**  directory of the ECS.

        To download the GPU driver, log in at  [http://www.nvidia.com/Download/index.aspx?lang=en](http://www.nvidia.com/Download/index.aspx?lang=en).

        **Figure  3**  Downloading the GPU driver<a name="en-us_topic_0093345963_fig14536376291"></a>  
        ![](figures/downloading-the-gpu-driver-3.png "downloading-the-gpu-driver-3")

    2.  Run the following command to install the GPU driver:

        **sh ./NVIDIA-Linux-x86\_64-_xxx.yy_.run**

    3.  Run the following command to delete the installation package:

        **rm -f NVIDIA-Linux-x86\_64-_xxx.yy_.run**

6.  Install the CUDA Toolkit.

    The CUDA Toolkit version required by Debian 9.0 GCC must be 9.0 or later. Unless otherwise specified, you are advised to install CUDA Toolkit  **cuda\_9.0.176\_384.81\_linux.run**, which has been fully verified.

    1.  Upload the CUDA Toolkit installation package  **cuda\__a.b.cc_\__xxx.yy_\_linux.run**  to the  **/tmp**  directory of the ECS.

        To download the CUDA Toolkit, log in at  [https://developer.nvidia.com/cuda-downloads](https://developer.nvidia.com/cuda-downloads).

    2.  Run the following command to change the permission:

        **chmod +x cuda\__a.b.cc_\__xxx.yy_\_linux.run**

    3.  Run the following command to install the CUDA Toolkit:

        **./cuda\__a.b.cc_\__xxx.yy_\_linux.run -toolkit -samples -silent -override --tmpdir=/tmp/**

    4.  Run the following command to delete the installation package:

        **rm -f cuda\__a.b.cc_\__xxx.yy_\_linux.run**

    5.  Run the following commands to check whether the installation is successful:

        **cd /usr/local/cuda/samples/1\_Utilities/deviceQueryDrv/**

        **make**

        **./deviceQueryDrv**

        If the terminal display contains "Result = PASS", both CUDA Toolkit and GPU driver have been installed.

        ```
        ./deviceQueryDrv Starting...
         
        CUDA Device Query (Driver API) statically linked version 
        Detected 1 CUDA Capable device(s)
         
        Device 0: "Tesla P100-PCIE-16GB"
          CUDA Driver Version:                           9.0
          CUDA Capability Major/Minor version number:    6.0
          Total amount of global memory:                 16276 MBytes (17066885120 bytes)
          (56) Multiprocessors, ( 64) CUDA Cores/MP:     3584 CUDA Cores
          GPU Max Clock rate:                            1329 MHz (1.33 GHz)
          Memory Clock rate:                             715 Mhz
          Memory Bus Width:                              4096-bit
          L2 Cache Size:                                 4194304 bytes
          Max Texture Dimension Sizes                    1D=(131072) 2D=(131072, 65536) 3D=(16384, 16384, 16384)
          Maximum Layered 1D Texture Size, (num) layers  1D=(32768), 2048 layers
          Maximum Layered 2D Texture Size, (num) layers  2D=(32768, 32768), 2048 layers
          Total amount of constant memory:               65536 bytes
          Total amount of shared memory per block:       49152 bytes
          Total number of registers available per block: 65536
          Warp size:                                     32
          Maximum number of threads per multiprocessor:  2048
          Maximum number of threads per block:           1024
          Max dimension size of a thread block (x,y,z): (1024, 1024, 64)
          Max dimension size of a grid size (x,y,z):    (2147483647, 65535, 65535)
          Texture alignment:                             512 bytes
          Maximum memory pitch:                          2147483647 bytes
          Concurrent copy and kernel execution:          Yes with 2 copy engine(s)
          Run time limit on kernels:                     No
          Integrated GPU sharing Host Memory:            No
          Support host page-locked memory mapping:       Yes
          Concurrent kernel execution:                   Yes
          Alignment requirement for Surfaces:            Yes
          Device has ECC support:                        Enabled
          Device supports Unified Addressing (UVA):      Yes
          Supports Cooperative Kernel Launch:            Yes
          Supports MultiDevice Co-op Kernel Launch:      Yes
          Device PCI Domain ID / Bus ID / location ID:   0 / 0 / 6
          Compute Mode:
             < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >
        Result = PASS
        ```



