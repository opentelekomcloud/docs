# How Do I Enable ICMP Security Group Rules?<a name="cce_01_0084"></a>

If a workload uses UDP for both load balancing and health checking, enable  ICMP security group  rules for the nodes of the workload.

## Procedure<a name="section865612352391"></a>

1.  Log in to the Elastic Cloud Server \(ECS\) console, find the ECS corresponding to any node where the workload runs, and click the ECS name. The ECS details page is displayed.
2.  On the  **Security Groups**  tab page, click  **Modify Security Group Rule**.

    **Figure  1**  Modifying security group rules<a name="fig1975116510166"></a>  
    ![](figures/modifying-security-group-rules.png "modifying-security-group-rules")

3.  On the  **Inbound Rules**  tag page, click  **Add Rule**  to add an inbound rule for the ECS. For details, see  [Figure 2](#fig11855954171611). Click  **OK**.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >You only need to add security group rules to any node where the workload runs.  

    **Figure  2**  Adding security group rules<a name="fig11855954171611"></a>  
    ![](figures/adding-security-group-rules.png "adding-security-group-rules")


