# Creating a Grant<a name="kms_01_0029"></a>

## Scenario<a name="section24674565101656"></a>

You can create grants for other users to use the CMK. You can create a maximum of 100 grants for a CMK.

The owner of a CMK can create a grant for the CMK on the KMS management console or by making the API calls. A user, who has been granted with the grant creation permission by the owner of the CMK, can create grants for the CMK only by making the API calls.

## Prerequisites<a name="section358224101847"></a>

-   You have obtained an account and its password for logging in to the management console.
-   You have obtained the user ID of the grantee \(user to whom permissions are to be authorized\).
-   The desired CMK is in  **Enabled**  status.

## Procedure<a name="section679064101921"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner of the management console and select a region or project.
3.  Choose  **Security**  \>  **Key Management Service**. The  **Key Management Service**  page is displayed.
4.  Click the alias of the desired CMK to go to the page displaying its details. You can create grants on the  **Grants**  tab page.

    **Figure  1**  Grants tab<a name="fig60093886153616"></a>  
    ![](figures/grants-tab.png "grants-tab")

5.  Click  **Create Grant**. The  **Create Grant**  dialog box is displayed.

    **Figure  2**  Creating a grant<a name="fig398977361785"></a>  
    ![](figures/creating-a-grant.png "creating-a-grant")

6.  In the dialog box that is displayed, enter the ID of the user to be authorized and select permissions to be granted.

    >![](/images/icon-notice.gif) **NOTICE:**   
    >A grantee can perform the authorized operations only by calling the necessary API. For details, see the  _Key Management Service API Reference_.  

    **Table  1**  Parameter description

    <a name="table25612854105354"></a>
    <table><thead align="left"><tr id="row30007999105354"><th class="cellrowborder" valign="top" width="20.79%" id="mcps1.2.4.1.1"><p id="p65451019105354"><a name="p65451019105354"></a><a name="p65451019105354"></a><strong>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.769999999999996%" id="mcps1.2.4.1.2"><p id="p67041161105354"><a name="p67041161105354"></a><a name="p67041161105354"></a><strong id="b842352706193336"><a name="b842352706193336"></a><a name="b842352706193336"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.44%" id="mcps1.2.4.1.3"><p id="p6529557818381"><a name="p6529557818381"></a><a name="p6529557818381"></a><strong id="b842352706191839"><a name="b842352706191839"></a><a name="b842352706191839"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row66499537105354"><td class="cellrowborder" valign="top" width="20.79%" headers="mcps1.2.4.1.1 "><p id="p17753435105354"><a name="p17753435105354"></a><a name="p17753435105354"></a>Key ID</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.769999999999996%" headers="mcps1.2.4.1.2 "><p id="p28742121105354"><a name="p28742121105354"></a><a name="p28742121105354"></a>ID of a CMK (automatically read by the system)</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.44%" headers="mcps1.2.4.1.3 "><p id="p5445043218381"><a name="p5445043218381"></a><a name="p5445043218381"></a>-</p>
    </td>
    </tr>
    <tr id="row57352501105354"><td class="cellrowborder" valign="top" width="20.79%" headers="mcps1.2.4.1.1 "><p id="p15041029105354"><a name="p15041029105354"></a><a name="p15041029105354"></a>Grantee</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.769999999999996%" headers="mcps1.2.4.1.2 "><p id="p30977284105656"><a name="p30977284105656"></a><a name="p30977284105656"></a>The user ID of the grantee is required.</p>
    <div class="note" id="note60358307151159"><a name="note60358307151159"></a><a name="note60358307151159"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p5739729810481"><a name="p5739729810481"></a><a name="p5739729810481"></a>The user IDs are provided by grantees who can obtain their IDs by clicking their portraits and choosing <strong id="b842352706153032"><a name="b842352706153032"></a><a name="b842352706153032"></a>My Credential</strong> &gt; <strong id="b842352706153036"><a name="b842352706153036"></a><a name="b842352706153036"></a>User ID</strong>.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="21.44%" headers="mcps1.2.4.1.3 "><p id="p4840887118381"><a name="p4840887118381"></a><a name="p4840887118381"></a>d9a6b2bdaedd4ba586cabe6372d1b312</p>
    </td>
    </tr>
    <tr id="row26165823105354"><td class="cellrowborder" valign="top" width="20.79%" headers="mcps1.2.4.1.1 "><p id="p39056879105354"><a name="p39056879105354"></a><a name="p39056879105354"></a>Granted Operations</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.769999999999996%" headers="mcps1.2.4.1.2 "><p id="p16848805145830"><a name="p16848805145830"></a><a name="p16848805145830"></a>The following permissions can be authorized:</p>
    <div class="note" id="note62771120438"><a name="note62771120438"></a><a name="note62771120438"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul11971183416718"></a><a name="ul11971183416718"></a><ul id="ul11971183416718"><li>You can create multiple grants on a CMK to provide different permissions to the same user. The user's permissions on the CMK are the combination of all the grants.</li><li>This parameter cannot be left blank.</li><li><strong id="b842352706111632"><a name="b842352706111632"></a><a name="b842352706111632"></a>Create Grant</strong> cannot be selected exclusively.</li></ul>
    </div></div>
    <a name="ul2209518113624"></a><a name="ul2209518113624"></a><ul id="ul2209518113624"><li><strong id="b842352706154510"><a name="b842352706154510"></a><a name="b842352706154510"></a>Create Data Key Without Plaintext</strong></li><li><strong id="b84235270615163"><a name="b84235270615163"></a><a name="b84235270615163"></a>Create Data Key</strong></li><li><strong id="b842352706151612"><a name="b842352706151612"></a><a name="b842352706151612"></a>Encrypt Data Key</strong></li><li><strong id="b842352706151616"><a name="b842352706151616"></a><a name="b842352706151616"></a>Decrypt Data Key</strong></li><li><strong id="b842352706151627"><a name="b842352706151627"></a><a name="b842352706151627"></a>Query Key Information</strong></li><li><strong id="b842352706151632"><a name="b842352706151632"></a><a name="b842352706151632"></a>Create Grant</strong></li><li><strong id="b842352706151544"><a name="b842352706151544"></a><a name="b842352706151544"></a>Retire Grant</strong><a name="ul168911571675"></a><a name="ul168911571675"></a><ul id="ul168911571675"><li>A grantee can retire a grant if the grantee does not need that permission.</li><li>If, before retiring a grant, the grantee has granted the permission to another user, that user's permission will not be affected by the grant retirement.</li></ul>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="21.44%" headers="mcps1.2.4.1.3 "><p id="p2880447018381"><a name="p2880447018381"></a><a name="p2880447018381"></a>-</p>
    </td>
    </tr>
    </tbody>
    </table>

7.  Click  **OK**. When message  **Grant of  _key alias_  created successfully**  is displayed in the upper right corner, the grant has been created.

    In the list of grants, you can view the grant ID, grantee ID, granted operation, and creation time of the grant.


