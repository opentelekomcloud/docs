# What Should I Do If the System Displays Error Code 0x112f When I Log In to a Windows ECS?<a name="EN-US_TOPIC_0120795668"></a>

## Symptom<a name="section98881979313"></a>

When I log in to a Windows ECS, the system displays error code 0x112f.

**Figure  1**  0x112f<a name="fig1256612592310"></a>  
![](figures/0x112f.jpg "0x112f")

## Possible Causes<a name="section121093216419"></a>

The ECS memory is insufficient.

## Solution<a name="section1299216522414"></a>

-   Method 1 \(recommended\)

    Modify the ECS specifications to increase the vCPUs and memory size. For instructions about how to modify ECS specifications, see  [General Operations for Modifying Specifications](general-operations-for-modifying-specifications.md).

-   Method 2

    Enable virtual memory on the ECS to obtain its idle memory.

    For instructions about how to enable virtual memory, see  [How Can I Enable Virtual Memory on a Windows ECS?](how-can-i-enable-virtual-memory-on-a-windows-ecs.md)

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >This method will deteriorate the disk I/O performance. Therefore, use this method only when necessary.  


