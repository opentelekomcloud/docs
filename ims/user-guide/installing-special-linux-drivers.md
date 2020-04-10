# Installing Special Linux Drivers<a name="EN-US_TOPIC_0082002007"></a>

Before using some types of ECSs to create private images, you need to install special drivers on the ECSs.

## NVIDIA Driver<a name="section210402212491"></a>

If you want to use the private image to create P1 ECSs, install the NVIDIA driver for the image to enable computing acceleration. For how to install the NVIDIA driver, see  [How Do I Install the NVIDIA Driver on a P1 ECS?](how-do-i-install-the-nvidia-driver-on-a-p1-ecs.md)

## InfiniBand NIC Driver<a name="section19610134011493"></a>

1.  If you want to use the private image to create H2 ECSs, install the InfiniBand NIC driver for the image. Download the required version \(4.2-1.0.0.0\) of InfiniBand NIC driver from the official website and install the driver by following the instructions provided by Mellanox.
    -   InfiniBand NIC type:  **Mellanox Technologies ConnectX-4 Infiniband HBA \(MCX455A-ECAT\)**
    -   Mellanox official website:  [http://www.mellanox.com/](http://www.mellanox.com/)
    -   NIC driver download path:  [http://www.mellanox.com/page/products\_dyn?product\_family=26&mtag=linux\_sw\_drivers](http://www.mellanox.com/page/products_dyn?product_family=26&mtag=linux_sw_drivers)

2.  If you want to use the private image to create HL1 ECSs, install the InfiniBand NIC driver for the image. Download the required version \(4.2-1.0.0.0\) of InfiniBand NIC driver from the official website and install the driver by following the instructions provided by Mellanox.
    -   InfiniBand NIC type:  **Mellanox Technologies ConnectX-4 Infiniband HBA \(MCX455A-ECAT\)**
    -   Mellanox official website:  [http://www.mellanox.com/](http://www.mellanox.com/)


