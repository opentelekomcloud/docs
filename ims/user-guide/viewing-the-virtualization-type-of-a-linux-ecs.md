# Viewing the Virtualization Type of a Linux ECS<a name="EN-US_TOPIC_0037352185"></a>

You can run the following command to query the virtualization type of an ECS:

**lscpu**

If the value of  **Hypervisor vendor**  is  **Xen**, the ECS uses Xen. If KVM is required, perform the operations in this section to optimize the Linux private image.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>If the ECS uses KVM, you are also advised to optimize the private image to prevent any exceptions with the ECSs created from the image.  

**Figure  1**  Viewing the virtualization type of a Linux ECS<a name="fig19508525221"></a>  
![](figures/viewing-the-virtualization-type-of-a-linux-ecs.png "viewing-the-virtualization-type-of-a-linux-ecs")

