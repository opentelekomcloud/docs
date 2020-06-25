# How Can I Check the Network Conditions of a Backend ECS?<a name="EN-US_TOPIC_0115500496"></a>

1.  Check that the primary NIC has an IP address bound.
    1.  Log in to the ECS.
    2.  Run the  **ifconfig**  or  **ip address**  command to check the IP address of the NIC.

        >![](/images/icon-note.gif) **NOTE:**   
        >For Windows ECSs, run  **ipconfig**  in the CLI to check the IP address.  


2.  Ping the gateway of the subnet where the ECS resides from the ECS to check for basic communication functions.
    1.  On the VPC details page, locate the target subnet and view the gateway address in the  **Gateway**  column. Generally, the gateway address ends with  **.1**.
    2.  Ping the subnet gateway from the ECS. If the gateway cannot be pinged, check the networks at Layer 2 and Layer 3.


