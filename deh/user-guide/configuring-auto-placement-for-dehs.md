# Configuring Auto Placement for DeHs<a name="EN-US_TOPIC_0046252768"></a>

## Scenarios<a name="section9864143152219"></a>

You can configure the automatic placement function for each DeH. This function determines whether to allow the system to automatically place ECSs on the DeH.

## Procedure<a name="section65161568234"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  Under  **Computing**, click  **Dedicated Host**.

    The  **Dedicated Host**  page is displayed.

4.  In the list of DeHs, locate the target DeH and enable or disable  **Auto Placement**.

## Verification<a name="section1818217330243"></a>

Assume that you have two DeHs with  **Auto Placement**  enabled. The  **vCPUs**  and  **Memory \(GB\)**  values of DeH A are  **83/100**  and  ****167/232****, and those of DeH B are  **100/100**  and  **232/232**. When creating an ECS, select  **Auto Placement**  for  **DeH**. Then the system automatically creates the ECS on DeH B to balance the load of each DeH.

