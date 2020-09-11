# Installing the NVIDIA GPU Driver and CUDA Toolkit on a P2 ECS<a name="EN-US_TOPIC_0097395656"></a>

## Scenarios<a name="section671317415422"></a>

If a P2 ECS is created using a private image, make sure that the NVIDIA driver has been installed during the private image creation. If not, install the driver for computing acceleration after the P2 ECS is created. For other types of ECSs, determine whether to install a driver according to the notes on using the ECSs in  [ECS Types](ecs-types.md).

The procedure for installing the NVIDIA driver varies according to the OS. For details, see this section.

## Prerequisites<a name="section073732576"></a>

-   The target ECS has had an EIP bound.
-   You have obtained the driver installation package required for an OS. For details, see  [Table 1](#table16574141765514).

**Table  1**  NVIDIA drivers

<a name="table16574141765514"></a>
<table><thead align="left"><tr id="row85812017155513"><th class="cellrowborder" valign="top" width="17.2%" id="mcps1.2.5.1.1"><p id="p927113851715"><a name="p927113851715"></a><a name="p927113851715"></a>OS</p>
</th>
<th class="cellrowborder" valign="top" width="17.330000000000002%" id="mcps1.2.5.1.2"><p id="p1018825145513"><a name="p1018825145513"></a><a name="p1018825145513"></a>Driver</p>
</th>
<th class="cellrowborder" valign="top" width="23.59%" id="mcps1.2.5.1.3"><p id="p19587191710551"><a name="p19587191710551"></a><a name="p19587191710551"></a>Installation Package</p>
</th>
<th class="cellrowborder" valign="top" width="41.88%" id="mcps1.2.5.1.4"><p id="p10589141755518"><a name="p10589141755518"></a><a name="p10589141755518"></a>How to Obtain</p>
</th>
</tr>
</thead>
<tbody><tr id="row9592141711559"><td class="cellrowborder" rowspan="2" valign="top" width="17.2%" headers="mcps1.2.5.1.1 "><p id="p1253572917458"><a name="p1253572917458"></a><a name="p1253572917458"></a>Ubuntu 16.04</p>
</td>
<td class="cellrowborder" valign="top" width="17.330000000000002%" headers="mcps1.2.5.1.2 "><p id="p20626154685513"><a name="p20626154685513"></a><a name="p20626154685513"></a>GPU driver</p>
</td>
<td class="cellrowborder" valign="top" width="23.59%" headers="mcps1.2.5.1.3 "><p id="p13597111716554"><a name="p13597111716554"></a><a name="p13597111716554"></a>NVIDIA-Linux-x86_64-384.81.run</p>
</td>
<td class="cellrowborder" valign="top" width="41.88%" headers="mcps1.2.5.1.4 "><p id="p359918174554"><a name="p359918174554"></a><a name="p359918174554"></a><a href="http://www.nvidia.com/download/driverResults.aspx/124722/en-us" target="_blank" rel="noopener noreferrer">http://www.nvidia.com/download/driverResults.aspx/124722/en-us</a></p>
</td>
</tr>
<tr id="row18601171712555"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p362634625512"><a name="p362634625512"></a><a name="p362634625512"></a>CUDA Toolkit</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p660320178554"><a name="p660320178554"></a><a name="p660320178554"></a>cuda_9.0.176_384.81_linux.run</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p14605517155515"><a name="p14605517155515"></a><a name="p14605517155515"></a><a href="https://developer.nvidia.com/compute/cuda/9.0/Prod/local_installers/cuda_9.0.176_384.81_linux-run" target="_blank" rel="noopener noreferrer">https://developer.nvidia.com/compute/cuda/9.0/Prod/local_installers/cuda_9.0.176_384.81_linux-run</a></p>
</td>
</tr>
</tbody>
</table>

## Ubuntu 16.04 64bit<a name="section146153428432"></a>

1.  Log in to the P2 ECS.
2.  Run the following command to switch to user  **root**:

    **sudo su**

3.  \(Optional\) Install GCC and g++.

    Perform this step only if GCC and g++ have not been installed.

    **apt-get update**

    **apt-get install gcc**

    **apt-get install g++**

    **apt-get install make**

4.  \(Optional\) Disable the Nouveau driver.

    Perform this step if the Nouveau driver has been installed on the target ECS. This prevents conflict with the NVIDIA driver installation.

    1.  Run the following command to check whether the Nouveau driver is running on the target ECS:

        **lsmod | grep nouveau**

        -   If yes, go to  [4.b](#en-us_topic_0093345963_li2691446193813).
        -   If no, go to  [5](#li111302143486).

    2.  <a name="en-us_topic_0093345963_li2691446193813"></a>Add the following statements to the end of the  **/etc/modprobe.d/blacklist-nouveau.conf**  file \(if the file is unavailable, create one\):

        **blacklist nouveau**

        **options nouveau modeset=0**

    3.  Run the following command to obtain  **initramfs**  again:

        **update-initramfs -u**

    4.  Run the following command to restart the ECS:

        **reboot**

5.  <a name="li111302143486"></a>\(Optional\) Disable the X service.

    If the ECS has been logged in using the GUI, disable the X service before installing the NVIDIA driver.

    1.  Run the following command to switch to multi-user mode:

        **systemctl set-default multi-user.target**

    2.  Run the following command to restart the ECS:

        **reboot**

6.  \(Optional\) Install the GPU driver.

    You can either use the GPU driver provided in the CUDA Toolkit installation package or download the required GPU driver. Unless otherwise specified, you are advised to install GPU driver  **NVIDIA-Linux-x86\_64-384.81.run**  provided in  [Prerequisites](#section073732576), which has been fully verified.

    1.  Upload the GPU driver installation package  **NVIDIA-Linux-x86\_64-384.81.run**  to the  **/tmp**  directory on the ECS.
    2.  Run the following command to install the GPU driver:

        **sh ./NVIDIA-Linux-x86\_64-384.81.run**

    3.  Run the following command to delete the installation package:

        **rm -rf NVIDIA-Linux-x86\_64-384.81.run**

7.  Install the CUDA Toolkit.

    Unless otherwise specified, you are advised to install CUDA Toolkit  **cuda\_9.0.176\_384.81\_linux.run**  provided in  [Prerequisites](#section073732576), which has been fully verified.

    1.  Upload the CUDA Toolkit installation package  **cuda\_9.0.176\_384.81\_linux.run**  to the  **/tmp**  directory on the ECS.
    2.  Run the following command to change the permission:

        **chmod +x cuda\_9.0.176\_384.81\_linux.run**

    3.  Run the following command to install the CUDA Toolkit:

        **./cuda\_9.0.176\_384.81\_linux.run -toolkit -samples -silent -override --tmpdir=/tmp/**

        ```
        root@user-OpenStack-Nova:/tmp# ./cuda_9.0.176_384.81_linux.run -toolkit -samples -silent -override --tmpdir=/tmp/  
         Missing recommended library: libGLU.so  
         Missing recommended library: libX11.so  
         Missing recommended library: libXi.so  
         Missing recommended library: libXmu.so  
         Missing recommended library: libGL.so  
           
         Copying samples to /root/NVIDIA_CUDA-8.0_Samples now...  
         Finished copying samples. 
        ```

    4.  Run the following command to delete the installation package:

        **rm -rf** **cuda\_9.0.176\_384.81\_linux.run**

    5.  Run the following commands to check whether the installation is successful:

        **cd /usr/local/cuda/samples/1\_Utilities/deviceQueryDrv/**

        **make**

        **./deviceQueryDrv**

        If the terminal display contains "Result = PASS", both CUDA Toolkit and GPU driver have been installed.

        ```
        ./deviceQueryDrv Starting...
        CUDA Device Query (Driver API) statically linked version 
        Detected 1 CUDA Capable device(s)
        Device 0: "Tesla V100-PCIE-16GB"
          CUDA Driver Version:                           9.0
          CUDA Capability Major/Minor version number:    7.0
          Total amount of global memory:                 16152 MBytes (16936927232 bytes)
          (80) Multiprocessors, ( 64) CUDA Cores/MP:     5120 CUDA Cores
          GPU Max Clock rate:                            1380 MHz (1.38 GHz)
          Memory Clock rate:                             877 Mhz
          Memory Bus Width:                              4096-bit
          L2 Cache Size:                                 6291456 bytes
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
          Concurrent copy and kernel execution:          Yes with 7 copy engine(s)
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



