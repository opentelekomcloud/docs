# Unbinding an EIP from an ECS and Releasing the EIP<a name="vpc_eip_0001"></a>

## Scenarios<a name="s36c772a5e6194d30b86be9c3d783e9cd"></a>

If you no longer need an EIP, unbind it from the ECS and release the EIP to avoid wasting network resources.

-   EIPs assigned and bound to load balancers in the ELB service are displayed in the EIP list of the VPC service, but you cannot unbind these EIPs from the load balancers.
-   Only unbound EIPs can be released. To release bound EIPs, you must first unbind them.

## Procedure<a name="s1422e532d0334624ab4f0b711fe90744"></a>

**Unbinding a single EIP**

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  On the console homepage, under  **Network**, click  **Elastic IP**.
4.  On the displayed page, locate the row that contains the target EIP, and click  **Unbind**.
5.  Click  **Yes**  in the displayed dialog box.

**Releasing a single EIP**

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  On the console homepage, under  **Network**, click  **Elastic IP**.
4.  On the displayed page, locate the row that contains the target EIP, click  **More**  in the  **Operation**  column, and click  **Release**.
5.  Click  **Yes**  in the displayed dialog box.

**Unbinding multiple EIPs at once**

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  On the console homepage, under  **Network**, click  **Elastic IP**.
4.  On the displayed page, select the EIPs to be unbound.
5.  Click  **Unbind**  above the EIP list.
6.  Click  **Yes**  in the displayed dialog box.

**Releasing multiple EIPs at once**

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  On the console homepage, under  **Network**, click  **Elastic IP**.
4.  On the displayed page, select the EIPs to be released.
5.  Click  **Release**  above the EIP list.
6.  Click  **Yes**  in the displayed dialog box.

