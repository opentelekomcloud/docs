# Querying a Grant<a name="kms_01_0030"></a>

## Scenario<a name="section24674565101656"></a>

This section describes how to view the details about a grant, such as the grant ID, grantee user ID, granted operation, and creation time.

## Prerequisites<a name="section358224101847"></a>

-   You have obtained an account and its password for logging in to the management console.
-   You have created a grant.

## Procedure<a name="section63833929154647"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner of the management console and select a region or project.
3.  Choose  **Security**  \>  **Key Management Service**. The  **Key Management Service**  page is displayed.
4.  Click the alias of the desired CMK to view its details.
5.  Information about the CMK and grants created on it are displayed,  [Figure 1](#fig26845936115420)  shows example grant information.

    **Figure  1**  Querying a grant<a name="fig26845936115420"></a>  
    ![](figures/querying-a-grant.png "querying-a-grant")

    [Table 1](#table41279785172331)  provides more details.

    **Table  1**  Parameter description

    <a name="table41279785172331"></a>
    <table><thead align="left"><tr id="row17212539172331"><th class="cellrowborder" valign="top" width="21.43%" id="mcps1.2.3.1.1"><p id="p65692410172331"><a name="p65692410172331"></a><a name="p65692410172331"></a><strong>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="78.57%" id="mcps1.2.3.1.2"><p id="p19485008172331"><a name="p19485008172331"></a><a name="p19485008172331"></a><strong id="b842352706193336"><a name="b842352706193336"></a><a name="b842352706193336"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row26851533113637"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.3.1.1 "><p id="p45703547113642"><a name="p45703547113642"></a><a name="p45703547113642"></a>Grant ID</p>
    </td>
    <td class="cellrowborder" valign="top" width="78.57%" headers="mcps1.2.3.1.2 "><p id="p10999799113642"><a name="p10999799113642"></a><a name="p10999799113642"></a>Randomly generated unique identification of a grant</p>
    </td>
    </tr>
    <tr id="row33403013172331"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.3.1.1 "><p id="p21289517172331"><a name="p21289517172331"></a><a name="p21289517172331"></a>Grantee</p>
    </td>
    <td class="cellrowborder" valign="top" width="78.57%" headers="mcps1.2.3.1.2 "><p id="p46729293172331"><a name="p46729293172331"></a><a name="p46729293172331"></a>ID of an authorized user.</p>
    </td>
    </tr>
    <tr id="row17910458172331"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.3.1.1 "><p id="p41460994172331"><a name="p41460994172331"></a><a name="p41460994172331"></a>Granted Operations</p>
    </td>
    <td class="cellrowborder" valign="top" width="78.57%" headers="mcps1.2.3.1.2 "><p id="p2897367172331"><a name="p2897367172331"></a><a name="p2897367172331"></a>Authorized operations (such as <strong id="b842352706112139"><a name="b842352706112139"></a><a name="b842352706112139"></a>Create Data Key</strong>) on the CMK</p>
    </td>
    </tr>
    <tr id="row26076305172331"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.3.1.1 "><p id="p31805988172331"><a name="p31805988172331"></a><a name="p31805988172331"></a>Creation Time</p>
    </td>
    <td class="cellrowborder" valign="top" width="78.57%" headers="mcps1.2.3.1.2 "><p id="p26148215172331"><a name="p26148215172331"></a><a name="p26148215172331"></a>Creation time of the grant</p>
    </td>
    </tr>
    </tbody>
    </table>

6.  Click a grant ID to view the grant details,  [Figure 2](#fig962432095216)  shows example grant information.

    **Figure  2**  Viewing grant details<a name="fig962432095216"></a>  
    ![](figures/viewing-grant-details.png "viewing-grant-details")


