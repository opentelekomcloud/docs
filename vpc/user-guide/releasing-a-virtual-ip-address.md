# Releasing a Virtual IP Address<a name="vpc_vip_0009"></a>

## Scenarios<a name="s82ad41fd6a5740a4b4bfef1650e82610"></a>

If you no longer need a virtual IP address or a reserved virtual IP address, you can release it to avoid wasting resources.

## Prerequisites<a name="section109701750171413"></a>

Before deleting a virtual IP address, ensure that the virtual IP address has been unbound from the following resources:

-   ECS
-   EIP
-   CCE cluster

## Procedure<a name="s9698f949de9c4b25be927641c30412bf"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  On the console homepage, under  **Network**, click  **Virtual Private Cloud**.

1.  In the navigation pane on the left, click  **Virtual Private Cloud**.
2.  On the  **Virtual Private Cloud**  page, locate the VPC containing the subnet from which a virtual IP address is to be released, and click the VPC name.
3.  On the  **Subnets**  tab, click the name of the subnet from which a virtual IP address is to be released.
4.  Click the  **Virtual IP Addresses**  tab, locate the row that contains the virtual IP address to be released, click  **More**  in the  **Operation**  column, and select  **Release**.
5.  Click  **Yes**  in the displayed dialog box.

