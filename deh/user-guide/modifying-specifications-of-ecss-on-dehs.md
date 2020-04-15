# Modifying Specifications of ECSs on DeHs<a name="EN-US_TOPIC_0102639795"></a>

## Scenarios<a name="section794312566456"></a>

When the specifications of ECSs on a DeH cannot meet service requirements, you can modify the ECS specifications by upgrading the vCPUs and memory. For some ECSs, you can change the ECS type when modifying the ECS specifications. You can change the specifications of a general-purpose ECS to that of an H1 ECS. You can change XEN instances to KVM instances.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>XEN instances: indicate ECSs that are virtualized by XEN.  
>KVM instances: indicate ECSs that are virtualized by KVM.  
>Before changing a XEN instance to a KVM instance, manually install the desired driver on the ECS. Otherwise, the ECS will be unavailable after the modification is performed. For example, starting the OS will fail.  

## Procedure<a name="section11641463461"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  Under  **Computing**, click  **Dedicated Host**.

    The  **Dedicated Host**  page is displayed.

4.  Click the name of the target DeH in the list of DeHs.

    The DeH details page is displayed.

5.  On the  **ECSs on the DeH**  tab, query the status of the target ECS.
6.  If the ECS is not in the  **Stopped**  state, click  **More**  and select  **Stop**  in the  **Operation**  column.
7.  After the ECS status changes to  **Stopped**, click  **Modify Specifications**  in the  **Operation**  column.

    The ECS page is displayed. For details, see the  _Elastic Cloud Server User Guide_.


