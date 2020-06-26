# Resizing a File System<a name="sfs_01_0039"></a>

You can expand or shrink the capacity of a file system when needed.

## Rules for Resizing<a name="section20105436211757"></a>

-   Expanding a file system

    Total capacity of a file system after expansion ≤ \(Capacity quota of the cloud account - Total capacity of all the other file systems owned by the cloud account\)

    For example, cloud account A has a quota of 500 TB. This account has already created three file systems: SFS1 \(350 TB\), SFS2 \(50 TB\), and SFS3 \(70 TB\). If this account needs to expand SFS2, the new capacity of SFS2 cannot be greater than 80 TB. Otherwise, the system will display a message indicating an insufficient quota and the expansion operation will fail.

-   Shrinking a file system
    -   When a shrink error or failure occurs on a file system, it takes approximately five minutes for the file system to restore to the available state.
    -   After a shrink operation fails, you can only reattempt to shrink the file system storage capacity but cannot expand it directly.
    -   Total capacity of a file system after shrinking ≥ Used capacity of the file system

        For example, cloud account B has created a file system, SFS1. The total capacity and used capacity of SFS1 are 50 TB and 10 TB respectively. When shrinking SFS1, the user cannot set the new capacity to be smaller than 10 TB.



## Procedure<a name="en-us_topic_0051702894_section1607836314443"></a>

1.  Log in to SFS Console.
2.  In the file system list, click  **Resize**  in the row of the file system you want to resize. The  **Resize File System**  dialog box is displayed. See  [Figure 1](#fig50999458171929).

    **Figure  1**  Resizing a file system<a name="fig50999458171929"></a>  
    ![](figures/resizing-a-file-system.png "resizing-a-file-system")

3.  Enter a new maximum capacity of the file system based on service requirements, and click  **OK**.  [Table 1](#table1834202713541)  describes the parameters.

    **Table  1**  Parameter description

    <a name="table1834202713541"></a>
    <table><thead align="left"><tr id="row134242765411"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p33421271543"><a name="p33421271543"></a><a name="p33421271543"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p2342132725418"><a name="p2342132725418"></a><a name="p2342132725418"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row172041324557"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p72048255517"><a name="p72048255517"></a><a name="p72048255517"></a>Used Capacity (GB)</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p5205172185510"><a name="p5205172185510"></a><a name="p5205172185510"></a>Used capacity of the current file system</p>
    </td>
    </tr>
    <tr id="row20398205885419"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p1439885815413"><a name="p1439885815413"></a><a name="p1439885815413"></a>Maximum Capacity (GB)</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p23981058105414"><a name="p23981058105414"></a><a name="p23981058105414"></a>Maximum capacity of the current file system</p>
    </td>
    </tr>
    <tr id="row311311253562"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p81132025155610"><a name="p81132025155610"></a><a name="p81132025155610"></a>New Maximum Capacity (GB)</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p1018375325614"><a name="p1018375325614"></a><a name="p1018375325614"></a>Target maximum capacity of the file system after expanding or shrinking. The value ranges from <strong id="b4809751457"><a name="b4809751457"></a><a name="b4809751457"></a>1 GB</strong> to <strong id="b10681155658"><a name="b10681155658"></a><a name="b10681155658"></a>512,000 GB</strong>.</p>
    <div class="note" id="note13597123622317"><a name="note13597123622317"></a><a name="note13597123622317"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p115971236122312"><a name="p115971236122312"></a><a name="p115971236122312"></a>The new maximum capacity cannot be smaller than the used capacity.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

4.  In the dialog box that is displayed, confirm the information and click  **Yes**.
5.  In the file system list, check the capacity information after resizing.

