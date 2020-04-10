# Viewing the Virtualization Type of a Windows ECS<a name="EN-US_TOPIC_0125075471"></a>

Open the cmd window and run the following command to query the  virtualization type  of the ECS:

**systeminfo**

If the values of  **System Manufacturer**  and  **BIOS Version**  are  **Xen**, the ECS uses Xen. If KVM is required, perform the operations in this section to optimize a Windows private image.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>If the ECS uses KVM, you are also advised to optimize the private image to prevent any exceptions with the ECSs created from the image.  

**Figure  1**  Viewing the virtualization type of the Windows ECS<a name="fig167731211184410"></a>  
![](figures/viewing-the-virtualization-type-of-the-windows-ecs.png "viewing-the-virtualization-type-of-the-windows-ecs")

