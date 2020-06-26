# Step 4: Confirm<a name="EN-US_TOPIC_0163572592"></a>

## Confirming the Order<a name="section11999172313116"></a>

1.  On the  **Confirm**  page, view details about the ECS configuration.

    To learn more about the price, click  **Pricing details**.

2.  Configure the number of ECSs to be created.

    After the configuration, click  **Price Calculator**  to view the ECS configuration fee.

3.  Confirm the configuration and click  **Create Now**.

## Follow-up Procedure<a name="section71001031128"></a>

-   After an ECS with an EIP bound is created, the system automatically generates a reverse domain name in the format of "ecs-xx-xx-xx-xx.compute.xxx.com" for each EIP by default. In the format, "xx-xx-xx-xx" indicates the EIP, and "xxx" indicates the domain name of the cloud service provider. You can use the reverse domain name to access the ECS.

    Use one of the following commands to obtain the default reverse domain name of an EIP:

    -   ping -a  _EIP_
    -   nslookup \[-qt=ptr\]  _EIP_
    -   dig -x  _EIP_


