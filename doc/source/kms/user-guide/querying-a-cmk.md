# Querying a CMK<a name="en-us_topic_0034330264"></a>

## Scenario<a name="section6530676516634"></a>

This section describes how to use the management console to view the information about a CMK, such as its alias, status, ID, and creation time. The status of a CMK can be  **Enabled**,  **Disabled**,  **Pending deletion**, or  **Pending import**.

## Prerequisites<a name="section6205788316731"></a>

You have obtained an account and its password for logging in to the management console.

## Procedure<a name="section4980422016839"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner of the management console and select a region or project.
3.  Choose  **Security**  \>  **Key Management Service**. The  **Key Management Service**  page is displayed.
4.  In the CMK list you can view details about the CMKs, as shown in  [Figure 1](#fig4265586161137).

    **Figure  1**  CMK list<a name="fig4265586161137"></a>  
    ![](figures/cmk-list.png "cmk-list")

    >![](/images/icon-note.gif) **NOTE:**   
    >-   Select the CMK status from the drop-down list of  **All statuses**. Then the CMK list displays only the CMKs in the corresponding state.  
    >-   Enter the alias of a CMK in the search box on top of the CMK list. Click  ![](figures/icon-search.png)  or press Enter to search for the specified CMK.  
    >-   You can click  **Search Tag**  to search for the CMK that meets the search criteria.  
    >-   You can click  ![](figures/icon-setting.png)  at the upper right corner on top of the CMK list to show or hide columns of the CMK list.  

    [Table 1](#table15653286125723)  describes the parameters of a CMK list.

    **Table  1**  CMK list parameters

    <a name="table15653286125723"></a>
    <table><thead align="left"><tr id="row16764658153819"><th class="cellrowborder" valign="top" width="24.25%" id="mcps1.2.3.1.1"><p id="p14764258193819"><a name="p14764258193819"></a><a name="p14764258193819"></a><strong>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="75.75%" id="mcps1.2.3.1.2"><p id="p676455893817"><a name="p676455893817"></a><a name="p676455893817"></a><strong id="b842352706112113"><a name="b842352706112113"></a><a name="b842352706112113"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1764115873811"><td class="cellrowborder" valign="top" width="24.25%" headers="mcps1.2.3.1.1 "><p id="p576455823813"><a name="p576455823813"></a><a name="p576455823813"></a>Alias</p>
    </td>
    <td class="cellrowborder" valign="top" width="75.75%" headers="mcps1.2.3.1.2 "><p id="p97641858183818"><a name="p97641858183818"></a><a name="p97641858183818"></a>Alias of a CMK</p>
    </td>
    </tr>
    <tr id="row87642058133813"><td class="cellrowborder" valign="top" width="24.25%" headers="mcps1.2.3.1.1 "><p id="p117641558113812"><a name="p117641558113812"></a><a name="p117641558113812"></a>Status</p>
    </td>
    <td class="cellrowborder" valign="top" width="75.75%" headers="mcps1.2.3.1.2 "><p id="p1076495815384"><a name="p1076495815384"></a><a name="p1076495815384"></a>Status of a CMK, which can be one of the following:</p>
    <a name="ul19764125893812"></a><a name="ul19764125893812"></a><ul id="ul19764125893812"><li><strong id="b842352706171111"><a name="b842352706171111"></a><a name="b842352706171111"></a>Enabled</strong><p id="p9764125816382"><a name="p9764125816382"></a><a name="p9764125816382"></a>The CMK is enabled.</p>
    </li><li><strong id="b842352706174855"><a name="b842352706174855"></a><a name="b842352706174855"></a>Disabled</strong><p id="p4764155803819"><a name="p4764155803819"></a><a name="p4764155803819"></a>The CMK is disabled.</p>
    </li><li><strong id="b842352706114222"><a name="b842352706114222"></a><a name="b842352706114222"></a>Pending deletion</strong><p id="p3764458173813"><a name="p3764458173813"></a><a name="p3764458173813"></a>The CMK is scheduled for deletion.</p>
    </li><li><strong id="b842352706114648"><a name="b842352706114648"></a><a name="b842352706114648"></a>Pending import</strong><p id="p1876418588384"><a name="p1876418588384"></a><a name="p1876418588384"></a>If your CMK does not have the key material, its status is <strong id="b842352706114727"><a name="b842352706114727"></a><a name="b842352706114727"></a>Pending import</strong>.</p>
    </li></ul>
    </td>
    </tr>
    <tr id="row1576425817386"><td class="cellrowborder" valign="top" width="24.25%" headers="mcps1.2.3.1.1 "><p id="p167641858103812"><a name="p167641858103812"></a><a name="p167641858103812"></a>ID</p>
    </td>
    <td class="cellrowborder" valign="top" width="75.75%" headers="mcps1.2.3.1.2 "><p id="p8764258143816"><a name="p8764258143816"></a><a name="p8764258143816"></a>Random ID of a CMK generated during the CMK creation</p>
    </td>
    </tr>
    <tr id="row14764125813817"><td class="cellrowborder" valign="top" width="24.25%" headers="mcps1.2.3.1.1 "><p id="p107649589384"><a name="p107649589384"></a><a name="p107649589384"></a>Creation Time</p>
    </td>
    <td class="cellrowborder" valign="top" width="75.75%" headers="mcps1.2.3.1.2 "><p id="p8764165817388"><a name="p8764165817388"></a><a name="p8764165817388"></a>Creation time of the CMK</p>
    </td>
    </tr>
    <tr id="row12764145843815"><td class="cellrowborder" valign="top" width="24.25%" headers="mcps1.2.3.1.1 "><p id="p5764758143816"><a name="p5764758143816"></a><a name="p5764758143816"></a>Expiration Time</p>
    </td>
    <td class="cellrowborder" valign="top" width="75.75%" headers="mcps1.2.3.1.2 "><p id="p1476425813388"><a name="p1476425813388"></a><a name="p1476425813388"></a>Expiration time of the key material. When the material expires, the CMK becomes an empty CMK.</p>
    </td>
    </tr>
    <tr id="row1276445816383"><td class="cellrowborder" valign="top" width="24.25%" headers="mcps1.2.3.1.1 "><p id="p376411581387"><a name="p376411581387"></a><a name="p376411581387"></a>Origin</p>
    </td>
    <td class="cellrowborder" valign="top" width="75.75%" headers="mcps1.2.3.1.2 "><p id="p0764115833812"><a name="p0764115833812"></a><a name="p0764115833812"></a>Source of key material, which can be one of the following:</p>
    <a name="ul1476475818381"></a><a name="ul1476475818381"></a><ul id="ul1476475818381"><li><strong id="b842352706115215"><a name="b842352706115215"></a><a name="b842352706115215"></a>External</strong><p id="p14764165843814"><a name="p14764165843814"></a><a name="p14764165843814"></a>You import the key material for the CMK.</p>
    </li><li>Key Management Service<p id="p1176465810383"><a name="p1176465810383"></a><a name="p1176465810383"></a>The CMK uses KMS-generated material.</p>
    </li></ul>
    </td>
    </tr>
    </tbody>
    </table>

5.  You can click the alias of a CMK to view its details, as shown in  [Figure 2](#fig14725810113147).

    **Figure  2**  Viewing CMK details<a name="fig14725810113147"></a>  
    ![](figures/viewing-cmk-details.png "viewing-cmk-details")


