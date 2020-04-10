# How Do I Troubleshoot Insufficient EIPs When a Node Is Added?<a name="cce_01_0203"></a>

## Symptom<a name="en-us_topic_0089615102_s29366dd7fe2e4257bd9481f435155270"></a>

When a node is added,  **EIP**  is set to  **Automatically assign**. The node cannot be created, and a message indicating that EIPs are insufficient is displayed.

**Figure  1**  Purchasing an EIP<a name="fig716922665112"></a>  
![](figures/purchasing-an-eip.png "purchasing-an-eip")

## Solution<a name="section2011614514539"></a>

Two methods are available to solve the problem.

-   Method 1: Unbind the VMs bound with EIPs and add a node again.
    1.  Log in to the management console.
    2.  Choose  **Service List \> Computing**  \>  **Elastic Cloud Server**.
    3.  In the ECS list, locate the target ECS and click its name.
    4.  On the ECS details page, click the  **EIPs**  tab. In the EIP list, click  **Unbind**  at the row of the target ECS and click  **Yes**.

        **Figure  2**  Unbinding an EIP<a name="fig1725274315571"></a>  
        ![](figures/unbinding-an-eip.png "unbinding-an-eip")

    5.  Return to the  **Create Node**  page on the CCE console and click  **Use existing**  to add an EIP.

        **Figure  3**  Using an unbound EIP<a name="fig38458333918"></a>  
        ![](figures/using-an-unbound-eip.png "using-an-unbound-eip")


-   Method 2: Increase the EIP quota.

    Quotas are used to limit the number of resources available to users. If the existing resource quota cannot meet your service requirements, you can increase your quota.


