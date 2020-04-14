# How Do I Change the SID of a Windows Server 2012 BMS?<a name="EN-US_TOPIC_0104580828"></a>

## Scenarios<a name="section1040713710414"></a>

A Security Identifier \(SID\) is a unique value that identifies a user, group, or computer account \(administrator account\). When an account is created for the first time, a unique SID is assigned to each account on the network. A SID is determined by the computer name, current time, and CPU use time of the current user-mode thread.

A complete SID contains:

-   User and group security description
-   48-bit ID authority
-   Revision level
-   Variable sub-authority values

An example SID is S-1-5-21-287469276-4015456986-3235239863-500.

<a name="table6579131713422"></a>
<table><tbody><tr id="row7580111774215"><td class="cellrowborder" valign="top" width="12.15%"><p id="p858041716423"><a name="p858041716423"></a><a name="p858041716423"></a>S</p>
</td>
<td class="cellrowborder" valign="top" width="12.1%"><p id="p195801175424"><a name="p195801175424"></a><a name="p195801175424"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="22.78%"><p id="p958071720421"><a name="p958071720421"></a><a name="p958071720421"></a>5</p>
</td>
<td class="cellrowborder" valign="top" width="35.15%"><p id="p858061754220"><a name="p858061754220"></a><a name="p858061754220"></a>21-287469276-4015456986-3235239863</p>
</td>
<td class="cellrowborder" valign="top" width="17.82%"><p id="p10580191714214"><a name="p10580191714214"></a><a name="p10580191714214"></a>500</p>
</td>
</tr>
<tr id="row1758012178427"><td class="cellrowborder" valign="top" width="12.15%"><p id="p12580117154211"><a name="p12580117154211"></a><a name="p12580117154211"></a>The string is a SID.</p>
</td>
<td class="cellrowborder" valign="top" width="12.1%"><p id="p1058061711425"><a name="p1058061711425"></a><a name="p1058061711425"></a>SID version</p>
</td>
<td class="cellrowborder" valign="top" width="22.78%"><p id="p135808173424"><a name="p135808173424"></a><a name="p135808173424"></a>SID authority, which is NT in this example</p>
</td>
<td class="cellrowborder" valign="top" width="35.15%"><p id="p13580181714421"><a name="p13580181714421"></a><a name="p13580181714421"></a>SID sub-authorities</p>
</td>
<td class="cellrowborder" valign="top" width="17.82%"><p id="p55808170424"><a name="p55808170424"></a><a name="p55808170424"></a>Accounts and groups in the domain</p>
</td>
</tr>
</tbody>
</table>

Currently, all the Windows Server 2012 BMSs have the same SID. In the cluster deployment scenario, you need to change the SID of the BMSs to ensure that each BMS uses a unique SID.

## Procedure<a name="section01514191545"></a>

1.  Log in to the BMS OS.
2.  <a name="li7621152616481"></a>Click  ![](figures/81-14.png)  in the lower left corner, choose  **Windows PowerShell**, and run the  **whoami /user**  command to query the SID.

    **Figure  1**  Querying the original SID<a name="fig951703185413"></a>  
    ![](figures/querying-the-original-sid.png "querying-the-original-sid")

3.  Modify the Cloudbase-Init configuration files.
    1.  Open the  **cloudbase-init.conf** and **cloudbase-init-unattend.con** files in the **C:\\Program Files\\Cloudbase Solutions\\Cloudbase-Init\\conf**  directory.
    2.  Add  **first\_logon\_behaviour=no**  to both files.

        ```
        [DEFAULT]
        username=Administrator
        groups=Administrators
        first_logon_behaviour=no
        netbios_host_name_compatibility=false
        metadata_services=cloudbaseinit.metadata.services.httpser
        inject_user_password=true
        ...
        ```

    3.  Delete  **cloudbaseinit.plugins.common.sethostname.SetHostNamePlugin** from the **cloudbase-init-unattend.conf**  file.

        ![](figures/56.png)

4.  Open the CLI and enter the following command to open the Sysprep window:

    ```
    C:\Program Files\Cloudbase Solutions\Cloudbase-Init\conf> C:\Windows\System32\Sysprep\sysprep.exe /unattend:Unattend.xml
    ```

5.  In the  **System Preparation Tool 3.14**  dialog box, configure parameters and click  **OK**.

    **Figure  2**  System Preparation Tool settings<a name="fig1916144511312"></a>  
    ![](figures/system-preparation-tool-settings.png "system-preparation-tool-settings")

6.  After the configuration is complete, the BMS automatically restarts. You need to encapsulate and decompress the package again. After the BMS restarts, you need to reset the password for the Windows OS. Contact the customer service.
7.  Log in to the BMS OS and check the SID using the method in  [2](#li7621152616481).

    **Figure  3**  Querying the new SID<a name="fig11868182131019"></a>  
    ![](figures/querying-the-new-sid.png "querying-the-new-sid")

    As shown in the preceding figure, the SID has been changed successfully.


