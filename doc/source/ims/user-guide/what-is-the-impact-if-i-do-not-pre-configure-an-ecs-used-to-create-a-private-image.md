# What Is the Impact If I Do Not Pre-configure an ECS Used to Create a Private Image?<a name="EN-US_TOPIC_0030713216"></a>

Before using an ECS or external image file to create a private image, you need to pre-configure the VM where the ECS or image file is located. If you do not perform the pre-configuration, there will be the following impacts:

1.  If you do not set the IP address obtaining mode to DHCP for the ECS NICs or do not delete residual udev rules, ECSs created from the registered private image retain the configuration of the source image file, or the ECS NICs do not start from eth0. In this case, you need to remotely log in to the ECS to configure it.
2.  If you do not configure the image used to create a Linux ECS, the following issues may occur during the ECS creation:
    -   Customized passwords cannot be injected.
    -   Certificated cannot be injected.
    -   Other customized configurations cannot be performed on the ECS.

3.  If you do not delete the automatic attaching detection information of user disks from the  **fstab**  file, the ECSs created from the private image may fail to start.

