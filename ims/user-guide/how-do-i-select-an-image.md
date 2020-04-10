# How Do I Select an Image?<a name="EN-US_TOPIC_0195253327"></a>

When creating an ECS or BMS, you can select an appropriate image from multiple image types with different OSs based on the following factors:

-   [Region and AZ](#section79821850163918)
-   [Image Type](#section17380359193914)
-   [OS](#section7760131584018)

## Region and AZ<a name="section79821850163918"></a>

An image is a regional resource. You cannot use an image to create an instance across regions. For example, when creating an instance in region A, you can select an image only from region A. For more regions, see  [Region and AZ](region-and-az.md).

## Image Type<a name="section17380359193914"></a>

Images are classified into public images, private images, shared images, and Marketplace images. Private images are classified into system disk images, data disk images, and full-ECS images. For details, see  [What Is Image Management Service?](what-is-image-management-service.md).

## OS<a name="section7760131584018"></a>

When selecting an OS, consider the following factors:

-   Architecture types

    <a name="table7114194612536"></a>
    <table><thead align="left"><tr id="row19115746145312"><th class="cellrowborder" valign="top" width="22.682268226822682%" id="mcps1.1.4.1.1"><p id="p13115154685311"><a name="p13115154685311"></a><a name="p13115154685311"></a>System Architecture</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.582358235823584%" id="mcps1.1.4.1.2"><p id="p5115124625316"><a name="p5115124625316"></a><a name="p5115124625316"></a>Applicable Memory</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.73537353735374%" id="mcps1.1.4.1.3"><p id="p311524618538"><a name="p311524618538"></a><a name="p311524618538"></a>Constraints</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1511594645320"><td class="cellrowborder" valign="top" width="22.682268226822682%" headers="mcps1.1.4.1.1 "><p id="p711514615311"><a name="p711514615311"></a><a name="p711514615311"></a>32-bit</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.582358235823584%" headers="mcps1.1.4.1.2 "><p id="p1115946155317"><a name="p1115946155317"></a><a name="p1115946155317"></a>Smaller than 4 GB</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.73537353735374%" headers="mcps1.1.4.1.3 "><a name="ul1721228185513"></a><a name="ul1721228185513"></a><ul id="ul1721228185513"><li>If the instance memory is greater than 4 GB, the 32-bit OS cannot be used.</li><li>A 32-bit OS allows addressing only within a 4 GB memory range. An OS with more than 4 GB memory cannot be accessed.</li></ul>
    </td>
    </tr>
    <tr id="row911534619535"><td class="cellrowborder" valign="top" width="22.682268226822682%" headers="mcps1.1.4.1.1 "><p id="p111513467530"><a name="p111513467530"></a><a name="p111513467530"></a>64-bit</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.582358235823584%" headers="mcps1.1.4.1.2 "><p id="p11115646185320"><a name="p11115646185320"></a><a name="p11115646185320"></a>4 GB or larger</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.73537353735374%" headers="mcps1.1.4.1.3 "><p id="p3115646145310"><a name="p3115646145310"></a><a name="p3115646145310"></a>If your application requires more than 4 GB memory or the memory may need to be expanded to more than 4 GB, use a 64-bit OS.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   OS types

    <a name="table097815412573"></a>
    <table><thead align="left"><tr id="row9979195420571"><th class="cellrowborder" valign="top" width="22.882288228822883%" id="mcps1.1.4.1.1"><p id="p10979554205714"><a name="p10979554205714"></a><a name="p10979554205714"></a>OS Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="43.784378437843785%" id="mcps1.1.4.1.2"><p id="p49791854185717"><a name="p49791854185717"></a><a name="p49791854185717"></a>Applicable Scenario</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="p6979105475717"><a name="p6979105475717"></a><a name="p6979105475717"></a>Constraints</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8979135495717"><td class="cellrowborder" valign="top" width="22.882288228822883%" headers="mcps1.1.4.1.1 "><p id="p12979754145719"><a name="p12979754145719"></a><a name="p12979754145719"></a>Windows</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.784378437843785%" headers="mcps1.1.4.1.2 "><a name="ul83661354598"></a><a name="ul83661354598"></a><ul id="ul83661354598"><li>Runs programs developed on Windows (for example, .NET).</li><li>Supports databases such as SQL Server. (You need to install the database.)</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p951713315619"><a name="p951713315619"></a><a name="p951713315619"></a>The system disk must be no less than 1 GB or larger, and the memory must be no less than 1 GB.</p>
    </td>
    </tr>
    <tr id="row149796547573"><td class="cellrowborder" valign="top" width="22.882288228822883%" headers="mcps1.1.4.1.1 "><p id="p12979165475710"><a name="p12979165475710"></a><a name="p12979165475710"></a>Linux</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.784378437843785%" headers="mcps1.1.4.1.2 "><a name="ul12695213017"></a><a name="ul12695213017"></a><ul id="ul12695213017"><li>Runs high-performance server applications (for example, Web) and supports common programming languages such as PHP and Python.</li><li>Supports databases such as MySQL. (You need to install the database.)</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p3780917866"><a name="p3780917866"></a><a name="p3780917866"></a>The system disk must be no less than 1 GB or larger, and the memory must be no less than 512 MB.</p>
    </td>
    </tr>
    </tbody>
    </table>


