# Can I Use Images in Formats Other Than Those Specified in This Document?<a name="EN-US_TOPIC_0030713217"></a>

No, you cannot. Currently, only the VMDK, VHD, RAW, QCOW2, VHDX, QED, VDI, QCOW, ZVHD2, and ZVHD are supported.

Images of the -flat.vmdk format and image file packages containing snapshot volumes or delta volumes are not supported. You can use qemu-img to convert the format of an image into a supported one before uploading it to the cloud platform.

>![](/images/icon-note.gif) **NOTE:**   
>For how to install and use qemu-img on Windows, visit the following website:  
>[https://cloudbase.it/qemu-img-windows/](https://cloudbase.it/qemu-img-windows/)  

