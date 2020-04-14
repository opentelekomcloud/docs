# Allocating DeHs<a name="EN-US_TOPIC_0046252762"></a>

## Scenarios<a name="section1181316715399"></a>

You will allocate a DeH for the first time or allocate more DeHs as required.

## Procedure<a name="section8199104219258"></a>

1.  Log in to the management console.
2.  Click  ![](figures/9.png)  in the upper left corner and select the desired region and project.
3.  Under  **Computing**, click  **Dedicated Host**.

    The  **Dedicated Host**  page is displayed.

4.  Click  **Allocate DeH**.

    The  **Allocate DeH**  page is displayed.

5.  Configure the DeH parameters.

    **Table  1**  Parameter description

    <a name="table4657163211216"></a>
    <table><thead align="left"><tr id="row5658232111215"><th class="cellrowborder" valign="top" width="29.720000000000002%" id="mcps1.2.3.1.1"><p id="p86584320121"><a name="p86584320121"></a><a name="p86584320121"></a><strong id="b842352706184931"><a name="b842352706184931"></a><a name="b842352706184931"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="70.28%" id="mcps1.2.3.1.2"><p id="p26581432191220"><a name="p26581432191220"></a><a name="p26581432191220"></a><strong id="b552158191511"><a name="b552158191511"></a><a name="b552158191511"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4658183251214"><td class="cellrowborder" valign="top" width="29.720000000000002%" headers="mcps1.2.3.1.1 "><p id="p4658132151210"><a name="p4658132151210"></a><a name="p4658132151210"></a>Region</p>
    </td>
    <td class="cellrowborder" valign="top" width="70.28%" headers="mcps1.2.3.1.2 "><p id="p565843251213"><a name="p565843251213"></a><a name="p565843251213"></a>A region is a geographic area where your DeHs are located. You are advised to select the region closest to your services to reduce the access latency and improve the download speed.</p>
    </td>
    </tr>
    <tr id="row19658232121210"><td class="cellrowborder" valign="top" width="29.720000000000002%" headers="mcps1.2.3.1.1 "><p id="p1965918329125"><a name="p1965918329125"></a><a name="p1965918329125"></a>AZ</p>
    </td>
    <td class="cellrowborder" valign="top" width="70.28%" headers="mcps1.2.3.1.2 "><p id="p16598328126"><a name="p16598328126"></a><a name="p16598328126"></a>An AZ is a physical region where resources use independent power supply and networks. AZs are physically isolated but interconnected through an internal network. To enhance application availability, you are advised to create DeHs in different AZs.</p>
    </td>
    </tr>
    <tr id="row18659153214125"><td class="cellrowborder" valign="top" width="29.720000000000002%" headers="mcps1.2.3.1.1 "><p id="p18659143201214"><a name="p18659143201214"></a><a name="p18659143201214"></a>DeH Category and DeH Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="70.28%" headers="mcps1.2.3.1.2 "><p id="p765910329129"><a name="p765910329129"></a><a name="p765910329129"></a>For details about the available DeH categories and types, see <a href="overview.md">Overview</a>.</p>
    <div class="note" id="note105323691810"><a name="note105323691810"></a><a name="note105323691810"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p5847157162215"><a name="p5847157162215"></a><a name="p5847157162215"></a>Pay attention to the following when configuring the DeH type:</p>
    <a name="ul944440152218"></a><a name="ul944440152218"></a><ul id="ul944440152218"><li>The DeH type determines the flavors and quantity of ECSs that can run on the DeH.</li><li>The <strong id="b14202574246"><a name="b14202574246"></a><a name="b14202574246"></a>Supported Flavors</strong> area shows the ECS flavors supported by the DeH type. These ECS flavors are for your reference only and cannot be selected. You can create an ECS of the listed flavor only after the DeH is created successfully.</li></ul>
    </div></div>
    </td>
    </tr>
    <tr id="row14444183821318"><td class="cellrowborder" valign="top" width="29.720000000000002%" headers="mcps1.2.3.1.1 "><p id="p17444438161315"><a name="p17444438161315"></a><a name="p17444438161315"></a>Auto Placement</p>
    </td>
    <td class="cellrowborder" valign="top" width="70.28%" headers="mcps1.2.3.1.2 "><p id="p104451387132"><a name="p104451387132"></a><a name="p104451387132"></a>If <strong id="b842352706103317"><a name="b842352706103317"></a><a name="b842352706103317"></a>Auto Placement</strong> is disabled for a DeH, and you enable the automatic placement function during ECS creation, the ECS created will not be scheduled to the DeH. Otherwise, the ECS may be scheduled to this DeH.</p>
    <p id="p6731418142612"><a name="p6731418142612"></a><a name="p6731418142612"></a>If <strong id="b84235270610362"><a name="b84235270610362"></a><a name="b84235270610362"></a>Auto Placement</strong> is disabled for a DeH, you can specify the DeH on which the ECS to be deployed during ECS creation.</p>
    </td>
    </tr>
    <tr id="row19517205991310"><td class="cellrowborder" valign="top" width="29.720000000000002%" headers="mcps1.2.3.1.1 "><p id="p11518159101318"><a name="p11518159101318"></a><a name="p11518159101318"></a>Tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="70.28%" headers="mcps1.2.3.1.2 "><p id="p175181596134"><a name="p175181596134"></a><a name="p175181596134"></a>Tags are identifiers of DeHs. Adding tags to DeHs helps you better identify and manage your DeHs. You can add a maximum of 10 tags to a DeH.</p>
    <p id="p8838814112714"><a name="p8838814112714"></a><a name="p8838814112714"></a>For details about tag operations, see <a href="tag-management.md">Tag Management</a>.</p>
    </td>
    </tr>
    <tr id="row175181759161317"><td class="cellrowborder" valign="top" width="29.720000000000002%" headers="mcps1.2.3.1.1 "><p id="p1951895913138"><a name="p1951895913138"></a><a name="p1951895913138"></a>DeH Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="70.28%" headers="mcps1.2.3.1.2 "><p id="p151814593135"><a name="p151814593135"></a><a name="p151814593135"></a>You can specify the DeH name, which contains a maximum of 64 characters, including only letters, digits, underscores (_), periods (.), and hyphens (-).</p>
    </td>
    </tr>
    <tr id="row12554123171412"><td class="cellrowborder" valign="top" width="29.720000000000002%" headers="mcps1.2.3.1.1 "><p id="p17555142320145"><a name="p17555142320145"></a><a name="p17555142320145"></a>Quantity</p>
    </td>
    <td class="cellrowborder" valign="top" width="70.28%" headers="mcps1.2.3.1.2 "><p id="p11555132320149"><a name="p11555132320149"></a><a name="p11555132320149"></a>When you allocate multiple DeHs, the system will add a suffix to each DeH name, for example, <strong id="b19884101116291"><a name="b19884101116291"></a><a name="b19884101116291"></a>my_DeH-001</strong> and <strong id="b1979181413298"><a name="b1979181413298"></a><a name="b1979181413298"></a>my_DeH-002</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    After the configuration, click  **Price Calculator**  to view the fees for current configuration.

6.  Click  **Allocate Now**, confirm the configuration information, and click  **Submit**.

## Results<a name="section121771812163913"></a>

You can view the newly created DeH on the  **Dedicated Host**  page. If the DeH is not displayed immediately, refresh the page and wait for a while. If the status of the DeH changes to Available, you can use the DeH.

## Follow-up Operations<a name="section46318974102947"></a>

After a DeH is provisioned, you can perform the following operations as needed:

-   [Deploying ECSs on DeHs](deploying-ecss-on-dehs.md)
-   [Migrating ECSs on DeHs](migrating-ecss-on-dehs.md)

