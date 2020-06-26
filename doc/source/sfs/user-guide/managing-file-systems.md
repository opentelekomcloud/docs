# Managing File Systems<a name="sfs_01_0034"></a>

## Viewing a File System<a name="section1863183113513"></a>

You can search for file systems by file system name keyword or file system status, and view their basic information.

## Procedure<a name="section029319391613"></a>

1.  Log in to SFS Console.
2.  In the file system list, view all file systems.  [Table 1](#table37365828114557)  describes the parameters of each file system.

    **Table  1**  Parameter description

    <a name="table37365828114557"></a>
    <table><thead align="left"><tr id="row19122233114557"><th class="cellrowborder" valign="top" width="24.060000000000002%" id="mcps1.2.3.1.1"><p id="p48573226114557"><a name="p48573226114557"></a><a name="p48573226114557"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="75.94%" id="mcps1.2.3.1.2"><p id="p42117262114557"><a name="p42117262114557"></a><a name="p42117262114557"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row43511042114557"><td class="cellrowborder" valign="top" width="24.060000000000002%" headers="mcps1.2.3.1.1 "><p id="p34733515114557"><a name="p34733515114557"></a><a name="p34733515114557"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="75.94%" headers="mcps1.2.3.1.2 "><p id="p61951365114557"><a name="p61951365114557"></a><a name="p61951365114557"></a>Name of the file system, for example, <strong id="b1789719584817"><a name="b1789719584817"></a><a name="b1789719584817"></a>sfs-name-001</strong></p>
    </td>
    </tr>
    <tr id="row38769363537"><td class="cellrowborder" valign="top" width="24.060000000000002%" headers="mcps1.2.3.1.1 "><p id="p08761636185312"><a name="p08761636185312"></a><a name="p08761636185312"></a>AZ</p>
    </td>
    <td class="cellrowborder" valign="top" width="75.94%" headers="mcps1.2.3.1.2 "><p id="p48761636105311"><a name="p48761636105311"></a><a name="p48761636105311"></a>Availability zone where the file system is located</p>
    </td>
    </tr>
    <tr id="row20691380114557"><td class="cellrowborder" valign="top" width="24.060000000000002%" headers="mcps1.2.3.1.1 "><p id="p65389082114557"><a name="p65389082114557"></a><a name="p65389082114557"></a>Status</p>
    </td>
    <td class="cellrowborder" valign="top" width="75.94%" headers="mcps1.2.3.1.2 "><p id="p62024260114557"><a name="p62024260114557"></a><a name="p62024260114557"></a>The value can be <strong id="b11116165615101"><a name="b11116165615101"></a><a name="b11116165615101"></a>Available</strong>, <strong id="b11172566107"><a name="b11172566107"></a><a name="b11172566107"></a>Unavailable</strong>, <strong id="b18118556111016"><a name="b18118556111016"></a><a name="b18118556111016"></a>Frozen</strong>, <strong id="b20132195613103"><a name="b20132195613103"></a><a name="b20132195613103"></a>Creating</strong>, <strong id="b1213316566107"><a name="b1213316566107"></a><a name="b1213316566107"></a>Deleting</strong>, <strong id="b3319181910111"><a name="b3319181910111"></a><a name="b3319181910111"></a>Deletion error</strong>, <strong id="b332131914111"><a name="b332131914111"></a><a name="b332131914111"></a>Expanding</strong>, <strong id="b33221219161116"><a name="b33221219161116"></a><a name="b33221219161116"></a>Expansion error</strong>, <strong id="b133223192119"><a name="b133223192119"></a><a name="b133223192119"></a>Capacity reducing</strong>, <strong id="b1732321971120"><a name="b1732321971120"></a><a name="b1732321971120"></a>Capacity reduction error</strong>, and <strong id="b4324171912115"><a name="b4324171912115"></a><a name="b4324171912115"></a>Capacity reduction failed</strong>.</p>
    </td>
    </tr>
    <tr id="row20249422122817"><td class="cellrowborder" valign="top" width="24.060000000000002%" headers="mcps1.2.3.1.1 "><p id="p166491045144519"><a name="p166491045144519"></a><a name="p166491045144519"></a>Share Protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="75.94%" headers="mcps1.2.3.1.2 "><p id="p10246151145017"><a name="p10246151145017"></a><a name="p10246151145017"></a>The NFS protocol is supported.</p>
    </td>
    </tr>
    <tr id="row31409628202754"><td class="cellrowborder" valign="top" width="24.060000000000002%" headers="mcps1.2.3.1.1 "><p id="p35229290202754"><a name="p35229290202754"></a><a name="p35229290202754"></a>Available Capacity (GB)</p>
    </td>
    <td class="cellrowborder" valign="top" width="75.94%" headers="mcps1.2.3.1.2 "><p id="p1648700614288"><a name="p1648700614288"></a><a name="p1648700614288"></a>Remaining space of the file system, available to data storage</p>
    <div class="note" id="note3647551314288"><a name="note3647551314288"></a><a name="note3647551314288"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p5984416914288"><a name="p5984416914288"></a><a name="p5984416914288"></a>The space information is refreshed every 15 minutes.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row38633965114557"><td class="cellrowborder" valign="top" width="24.060000000000002%" headers="mcps1.2.3.1.1 "><p id="p1531121819414"><a name="p1531121819414"></a><a name="p1531121819414"></a>Maximum Capacity (GB)</p>
    </td>
    <td class="cellrowborder" valign="top" width="75.94%" headers="mcps1.2.3.1.2 "><p id="p32916417153520"><a name="p32916417153520"></a><a name="p32916417153520"></a>Maximum capacity of the file system</p>
    </td>
    </tr>
    <tr id="row15695362119"><td class="cellrowborder" valign="top" width="24.060000000000002%" headers="mcps1.2.3.1.1 "><p id="p1556983618112"><a name="p1556983618112"></a><a name="p1556983618112"></a>Encrypted</p>
    </td>
    <td class="cellrowborder" valign="top" width="75.94%" headers="mcps1.2.3.1.2 "><p id="p1956943691114"><a name="p1956943691114"></a><a name="p1956943691114"></a>Encryption status of the created file system. The value can be <strong id="b842352706175533"><a name="b842352706175533"></a><a name="b842352706175533"></a>Yes</strong> or <strong id="b842352706175536"><a name="b842352706175536"></a><a name="b842352706175536"></a>No</strong>.</p>
    </td>
    </tr>
    <tr id="row65429735114557"><td class="cellrowborder" valign="top" width="24.060000000000002%" headers="mcps1.2.3.1.1 "><p id="p65317149114557"><a name="p65317149114557"></a><a name="p65317149114557"></a>Shared Path</p>
    </td>
    <td class="cellrowborder" valign="top" width="75.94%" headers="mcps1.2.3.1.2 "><p id="p56197716114557"><a name="p56197716114557"></a><a name="p56197716114557"></a>Shared path of the file system. The format is <em id="i12751455165915"><a name="i12751455165915"></a><a name="i12751455165915"></a>File system domain name</em><strong id="b166268134012"><a name="b166268134012"></a><a name="b166268134012"></a>:/</strong><em id="i198081316606"><a name="i198081316606"></a><a name="i198081316606"></a>path</em> or <em id="i183863116420"><a name="i183863116420"></a><a name="i183863116420"></a>File system IP address</em><strong id="b183876115425"><a name="b183876115425"></a><a name="b183876115425"></a>:/</strong>.</p>
    <div class="note" id="note6962192620914"><a name="note6962192620914"></a><a name="note6962192620914"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1196315261698"><a name="p1196315261698"></a><a name="p1196315261698"></a>If the shared path is too long to display completely, expand the column to view the full shared path.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row27443506111522"><td class="cellrowborder" valign="top" width="24.060000000000002%" headers="mcps1.2.3.1.1 "><p id="p46592934111528"><a name="p46592934111528"></a><a name="p46592934111528"></a>Operation</p>
    </td>
    <td class="cellrowborder" valign="top" width="75.94%" headers="mcps1.2.3.1.2 "><p id="p55891167164624"><a name="p55891167164624"></a><a name="p55891167164624"></a>Valid operations include capacity adjustment, viewing monitoring indicators, and deletion.</p>
    </td>
    </tr>
    </tbody>
    </table>

3.  Click the name of a file system to view detailed information about the file system. See  [Figure 1](#fig964613241271).

    **Figure  1**  File system information<a name="fig964613241271"></a>  
    ![](figures/file-system-information.png "file-system-information")

4.  \(Optional\) Search for and view file systems by file system name keyword, key ID, or file system status.
    -   In the upper right corner of the page, click  **Search by Tag**  to query the file systems by tag.
        -   On the  **Search by Tag**  tab page that is displayed, enter a tag key and a tag value \(must be among existing keys and values\) and click  **Search**.
        -   You can use more than one tag for a combination search. Each time after a key and a value are entered, click  ![](figures/button-5.png). The added tag search criteria are displayed under the text boxes. When more than one tag is added, they will be applied together for a combination search. A maximum of 10 tags can be added at one time.
        -   You can click  **Reset**  under the search criteria to reset.



## Deleting a File System<a name="section986124520526"></a>

After a file system is deleted, data in it cannot be restored. To prevent data loss, before deleting a file system, ensure that files in it have been backed up locally.

## Prerequisites<a name="section39130845104113"></a>

Before deleting the file system, unmount it first. For details about how to unmount the file system, see  [Unmounting a File System](step-3-unmount-a-file-system.md).

## Procedure<a name="section187813405311"></a>

1.  Log in to SFS Console.
2.  In the file system list, click  **Delete**  in the row of the file system you want to delete.
3.  In the displayed dialog box, as shown in  [Figure 2](#fig51368710153938), confirm the information, and then click  **Yes**. 

    >![](/images/icon-note.gif) **NOTE:**   
    >Only  **Available**  and  **Unavailable**  file systems can be deleted.  

    **Figure  2**  Deleting a file system<a name="fig51368710153938"></a>  
    ![](figures/deleting-a-file-system.png "deleting-a-file-system")

4.  Check the file system list to confirm that the file system is deleted successfully.
5.  \(Optional\) If you want to delete more than one file system at a time, select the file systems, and then click  **Delete**  in the upper left part of the file system list. In the dialog box that is displayed, confirm the information, enter  **Delete**  in the text box, and then click  **Yes**. 

