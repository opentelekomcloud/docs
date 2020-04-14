# Enabling Remote Desktop Connection<a name="EN-US_TOPIC_0030713155"></a>

## Scenarios<a name="section18008450525"></a>

If you want to remotely access the ECS, you must enable  remote desktop connection  when creating the private image. This function must be enabled for the GPU-optimized ECS.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>When registering an external image file as a private image, enable remote desktop connection on the VM where the external image file is located. You are advised to enable this function on the VM and then export the image file.  

## Prerequisites<a name="section12881164595515"></a>

You have logged in to the ECS used to create a Windows private image.

For details about how to log in to the ECS, see  _Elastic Cloud Server User Guide_.

## Procedure<a name="section5900131105513"></a>

1.  Before enabling this function, you are advised to set the resolution of the ECS to 1920×1080.

    On the ECS, choose  **Start**  \>  **Control Panel**. Under  **Appearance and Personalization**, click  **Adjust screen resolution**. Then select a proper value from the  **Resolution**  drop-down list box.

2.  Choose  **Start**, right-click  **Computer**, and choose  **Properties**  from the shortcut menu.
3.  Click  **Remote settings**.
4.  In the  **Remote**  tab, select  **Allow connections from computers running any version of Remote Desktop \(less secure\)**.
5.  Click  **OK**.
6.  Choose  **Start**  \>  **Control Panel**  and navigate to  **Windows Firewall**.
7.  Choose  **Allow a program or feature through Windows Firewall**  in the left pane.
8.  Select programs and features that are allowed by the Windows firewall for  **Remote Desktop**  based on your network requirements and click  **OK**  in the lower part.

    **Figure  1**  Configuring remote desktop<a name="fig33349279102033"></a>  
    ![](figures/configuring-remote-desktop.jpg "configuring-remote-desktop")


