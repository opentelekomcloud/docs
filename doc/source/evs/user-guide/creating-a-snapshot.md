# Creating a Snapshot<a name="en-us_topic_0066615262"></a>

## Scenarios<a name="section36690541174716"></a>

You can create an EVS snapshot on the management console to save the EVS disk data at a specific time point.

A maximum of 7 snapshots can be created for an EVS disk.

## Procedure<a name="section3347385018116"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  Under  **Storage**, click  **Elastic Volume Service**.

    The disk list page is displayed.

4.  Switch to the  **Create Snapshot**  page in either of the following ways:
    -   In the disk list, locate the row that contains the target disk, click  **More**  in the  **Operation**  column, and choose  **Create Snapshot**.

        Configure the basic settings for the snapshot according to  [Table 1](#table17584125003610).

        **Table  1**  Parameter description

        <a name="table17584125003610"></a>
        <table><thead align="left"><tr id="row858695093614"><th class="cellrowborder" valign="top" width="22.444444444444443%" id="mcps1.2.4.1.1"><p id="p13587450173612"><a name="p13587450173612"></a><a name="p13587450173612"></a>Parameter</p>
        </th>
        <th class="cellrowborder" valign="top" width="44.45454545454545%" id="mcps1.2.4.1.2"><p id="p458865013366"><a name="p458865013366"></a><a name="p458865013366"></a>Description</p>
        </th>
        <th class="cellrowborder" valign="top" width="33.1010101010101%" id="mcps1.2.4.1.3"><p id="p12589155043617"><a name="p12589155043617"></a><a name="p12589155043617"></a>Example Value</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row155895505360"><td class="cellrowborder" valign="top" width="22.444444444444443%" headers="mcps1.2.4.1.1 "><p id="p458955012367"><a name="p458955012367"></a><a name="p458955012367"></a>Snapshot Name</p>
        </td>
        <td class="cellrowborder" valign="top" width="44.45454545454545%" headers="mcps1.2.4.1.2 "><p id="p16592850123618"><a name="p16592850123618"></a><a name="p16592850123618"></a>Mandatory</p>
        <p id="p15593850143611"><a name="p15593850143611"></a><a name="p15593850143611"></a>The name can contain a maximum of 64 characters.</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.1010101010101%" headers="mcps1.2.4.1.3 "><p id="p559411502365"><a name="p559411502365"></a><a name="p559411502365"></a>snapshot-01</p>
        </td>
        </tr>
        </tbody>
        </table>

    -   In the navigation tree on the left, choose  **Elastic Volume Service**  \>  **Snapshots**.

        On the  **Snapshots**  page, click  **Create Snapshot**.

        Configure the basic settings for the snapshot according to  [Table 2](#table31596124394).

        **Table  2**  Parameter description

        <a name="table31596124394"></a>
        <table><thead align="left"><tr id="row16162191293911"><th class="cellrowborder" valign="top" width="22.444444444444443%" id="mcps1.2.4.1.1"><p id="p1416381283916"><a name="p1416381283916"></a><a name="p1416381283916"></a>Parameter</p>
        </th>
        <th class="cellrowborder" valign="top" width="44.45454545454545%" id="mcps1.2.4.1.2"><p id="p6164112173911"><a name="p6164112173911"></a><a name="p6164112173911"></a>Description</p>
        </th>
        <th class="cellrowborder" valign="top" width="33.1010101010101%" id="mcps1.2.4.1.3"><p id="p1167912153918"><a name="p1167912153918"></a><a name="p1167912153918"></a>Example Value</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row19686104164510"><td class="cellrowborder" valign="top" width="22.444444444444443%" headers="mcps1.2.4.1.1 "><p id="p17686343457"><a name="p17686343457"></a><a name="p17686343457"></a>Region</p>
        </td>
        <td class="cellrowborder" valign="top" width="44.45454545454545%" headers="mcps1.2.4.1.2 "><p id="p068614174517"><a name="p068614174517"></a><a name="p068614174517"></a>Mandatory</p>
        <p id="p176472021164517"><a name="p176472021164517"></a><a name="p176472021164517"></a>After you select a region, the disks in the selected region will be displayed for you to choose.</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.1010101010101%" headers="mcps1.2.4.1.3 "><p id="p1868674204519"><a name="p1868674204519"></a><a name="p1868674204519"></a>-</p>
        </td>
        </tr>
        <tr id="row716819126391"><td class="cellrowborder" valign="top" width="22.444444444444443%" headers="mcps1.2.4.1.1 "><p id="p13169191220397"><a name="p13169191220397"></a><a name="p13169191220397"></a>Snapshot Name</p>
        </td>
        <td class="cellrowborder" valign="top" width="44.45454545454545%" headers="mcps1.2.4.1.2 "><p id="p18169121217392"><a name="p18169121217392"></a><a name="p18169121217392"></a>Mandatory</p>
        <p id="p9171141210396"><a name="p9171141210396"></a><a name="p9171141210396"></a>The name can contain a maximum of 64 characters.</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.1010101010101%" headers="mcps1.2.4.1.3 "><p id="p1917212125397"><a name="p1917212125397"></a><a name="p1917212125397"></a>snapshot-01</p>
        </td>
        </tr>
        <tr id="row143561437133918"><td class="cellrowborder" valign="top" width="22.444444444444443%" headers="mcps1.2.4.1.1 "><p id="p16357113712393"><a name="p16357113712393"></a><a name="p16357113712393"></a>Select Disk</p>
        </td>
        <td class="cellrowborder" valign="top" width="44.45454545454545%" headers="mcps1.2.4.1.2 "><p id="p544913924010"><a name="p544913924010"></a><a name="p544913924010"></a>Mandatory</p>
        <p id="p9449939144017"><a name="p9449939144017"></a><a name="p9449939144017"></a>Select a disk based on which the snapshot is to be created.</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.1010101010101%" headers="mcps1.2.4.1.3 "><p id="p184516390403"><a name="p184516390403"></a><a name="p184516390403"></a>volume-01</p>
        </td>
        </tr>
        </tbody>
        </table>

5.  Click  **Create Now**.
6.  Return to the  **Snapshots**  page to view the snapshot creation information.

    When the snapshot status changes to  **Available**, the creation is successful.


