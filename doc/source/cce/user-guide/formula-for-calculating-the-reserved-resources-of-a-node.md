# Formula for Calculating the Reserved Resources of a Node<a name="cce_01_0178"></a>

Some of the resources on the  node  need to run some necessary  Kubernetes  system components and resources to make the node as part of your cluster. Therefore, the total number of node resources and the number of assignable node resources in Kubernetes are different. The larger the node specifications, the more the containers deployed on the node. Therefore, Kubernetes needs to reserve more resources.

To ensure node stability, CCE  cluster  nodes reserve some resources for Kubernetes components \(such as kubelet, kube-proxy, and docker\) based on node specifications.

CCE calculates the resources that can be allocated to user nodes as follows:

**Allocatable = Capacity - Reserved - Eviction Threshold**

That is,  **Configurable amount on the node**  =  **Total amount**  –  **Reserved amount**  –  **Eviction threshold**.

-   The rules for reserving the node memory are as follows:

    1.  total\_mem ≤ 4 GB, reserved\_value = total\_mem x 25%
    2.  4 GB < total\_mem ≤ 8 GB, reserved\_value = 4 GB x 25% + \(total\_mem – 4 GB\) x 20%
    3.  8 GB < total\_mem ≤ 16 GB, reserved\_value = 4 GB x 25% + 4 GB x 20% + \(total\_mem – 8 GB\) x 10%
    4.  16 GB < total\_mem ≤ 128 GB, reserved\_value = 4 GB x 25% + 4 GB x 20% + 8 GB x 10% + \(total\_mem – 16 GB\) x 6%
    5.  total\_mem \> 128 GB, eserved\_value = 4 GB x 25% + 4 GB x 20% + 8 GB x 10% + 112 GB x 6% + \(total\_mem – 128 GB\) x 2%

    In the preceding information,  **total\_mem**  indicates the total memory and  **reserved\_value**  indicates the reserved memory.

-   The rules for reserving the node CPU are as follows:

    1.  total\_cpu ≤ 1 core, reserved\_value = total\_cpu x 6%
    2.  1 core < total\_cpu ≤ 2 core, reserved\_value = 1 core x 6% + \(total\_cpu – 1 core\) x 1%
    3.  2 core < total\_cpu ≤ 4 core, reserved\_value = 1 core x 6% + 1 core x 1% + \(total\_cpu – 2 core\) x 0.5%
    4.  total\_cpu \> 4 core, reserved\_value = 1 core x 6% + 1 core x 1% + 2 core x 0.5% + \(total\_cpu – 4 core\) x 0.25%

    In the preceding information,  **total\_cpu**  indicates the total CPU, and  **reserved\_value**  indicates the reserved CPU.

-   CCE reserves an extra 100Mi for kubelet eviction.

