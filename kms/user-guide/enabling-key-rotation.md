# Enabling Key Rotation<a name="kms_01_0139"></a>

## Scenario<a name="section1774863214344"></a>

This section describes how to enable rotation for a key on the KMS console.

By default, automatic key rotation is disabled for a CMK. Every time you enable key rotation, KMS automatically rotates CMKs based on the rotation period you set.

## Prerequisites<a name="sa444d90e5d214eb2811cd143d283ed46"></a>

-   You have obtained an account and its password for logging in to the management console.
-   The CMK is in  **Enabled**  status.
-   The  **Origin**  of the CMK is  **KMS**.

## Procedure<a name="section1953329183312"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner of the management console and select a region or project.
3.  Choose  **Security**  \>  **Key Management Service**. The  **Key Management Service**  page is displayed.
4.  Click the alias of the desired CMK to view its details.
5.  Click  **Rotate Key**. The dialog box is displayed, as shown in  [Figure 1](#fig947023217481).

    **Figure  1**  CMK rotation<a name="fig947023217481"></a>  
    ![](figures/cmk-rotation.png "cmk-rotation")

6.  Click  ![](figures/icon-closed.png)  to set the  **Key Rotation**  status to  ![](figures/icon-open.png), as shown in  [Figure 2](#f6e50215e22ef49a99f916988074aa83e).  [Table 1](#ta8cb67818b87411dad53061d32313de1)  provides more details.

    **Figure  2**  Enabling key rotation<a name="f6e50215e22ef49a99f916988074aa83e"></a>  
    ![](figures/enabling-key-rotation.png "enabling-key-rotation")

    **Table  1**  Description of the parameters for enabling rotation for a CMK

    <a name="ta8cb67818b87411dad53061d32313de1"></a>
    <table><thead align="left"><tr id="r2849aa0f01444575a794decd8e844b36"><th class="cellrowborder" valign="top" width="30.819999999999997%" id="mcps1.2.3.1.1"><p id="a99591e565bb8496286635f01d047ef09"><a name="a99591e565bb8496286635f01d047ef09"></a><a name="a99591e565bb8496286635f01d047ef09"></a><strong>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="69.17999999999999%" id="mcps1.2.3.1.2"><p id="a12c70faacb0944ac889731462ab2eb28"><a name="a12c70faacb0944ac889731462ab2eb28"></a><a name="a12c70faacb0944ac889731462ab2eb28"></a><strong id="b842352706135554"><a name="b842352706135554"></a><a name="b842352706135554"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="rfaa8341df94b422ebe77d8086f4cc34d"><td class="cellrowborder" valign="top" width="30.819999999999997%" headers="mcps1.2.3.1.1 "><p id="a93b8b4a704184ce4b4966acf7ba5f0a4"><a name="a93b8b4a704184ce4b4966acf7ba5f0a4"></a><a name="a93b8b4a704184ce4b4966acf7ba5f0a4"></a>CMK rotation</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.17999999999999%" headers="mcps1.2.3.1.2 "><p id="a0adcdcafb85047f98ddb841342a0edfe"><a name="a0adcdcafb85047f98ddb841342a0edfe"></a><a name="a0adcdcafb85047f98ddb841342a0edfe"></a>Rotation switch. The default status is <a name="image1314638113110"></a><a name="image1314638113110"></a><span><img id="image1314638113110" src="figures/icon-closed.png"></span>.</p>
    <p id="a1a1f61064228406682a554abc968d1b1"><a name="a1a1f61064228406682a554abc968d1b1"></a><a name="a1a1f61064228406682a554abc968d1b1"></a><a name="image1450833918319"></a><a name="image1450833918319"></a><span><img id="image1450833918319" src="figures/icon-closed.png"></span>: disabled</p>
    <p id="a4ca830c8863f4477bae887ed80180a5b"><a name="a4ca830c8863f4477bae887ed80180a5b"></a><a name="a4ca830c8863f4477bae887ed80180a5b"></a><a name="image82741922143318"></a><a name="image82741922143318"></a><span><img id="image82741922143318" src="figures/icon-open.png"></span>: enabled</p>
    <p id="a1ee320d1e9ae45cbab7429d3ae973d74"><a name="a1ee320d1e9ae45cbab7429d3ae973d74"></a><a name="a1ee320d1e9ae45cbab7429d3ae973d74"></a>After rotation is enabled, the CMK will be rotated based on your set period.</p>
    <div class="note" id="nf9ae728bc2a64ab789b50b45a7e6dd95"><a name="nf9ae728bc2a64ab789b50b45a7e6dd95"></a><a name="nf9ae728bc2a64ab789b50b45a7e6dd95"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="a08bf9be780a64626b5a13fb5dc73be69"><a name="a08bf9be780a64626b5a13fb5dc73be69"></a><a name="a08bf9be780a64626b5a13fb5dc73be69"></a>KMS does not rotate a disabled CMK for which rotation has been enabled.</p>
    <p id="a231e698893fb499e84dadf5801cc71f3"><a name="a231e698893fb499e84dadf5801cc71f3"></a><a name="a231e698893fb499e84dadf5801cc71f3"></a>KMS rotates it when it is enabled again. If it has been longer than the rotation period since the CMK was rotated last time, KMS will rotate the CMK within 24 hours.</p>
    </div></div>
    </td>
    </tr>
    <tr id="ra3a0100b49124ed4b3f49738aba25ff5"><td class="cellrowborder" valign="top" width="30.819999999999997%" headers="mcps1.2.3.1.1 "><p id="ac3e20a469b0541aeb96a888d81822ed4"><a name="ac3e20a469b0541aeb96a888d81822ed4"></a><a name="ac3e20a469b0541aeb96a888d81822ed4"></a>Rotation Period (day)</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.17999999999999%" headers="mcps1.2.3.1.2 "><p id="ae14f9a73f7b044d0b92dcd92da7e9d62"><a name="ae14f9a73f7b044d0b92dcd92da7e9d62"></a><a name="ae14f9a73f7b044d0b92dcd92da7e9d62"></a>Rotation period (day). The value is an integer ranging from 30 to 365. The default value is <strong id="b842352706114030"><a name="b842352706114030"></a><a name="b842352706114030"></a>365</strong>.</p>
    <p id="ae6494d1877ab43e4b16f2f080e9bfa20"><a name="ae6494d1877ab43e4b16f2f080e9bfa20"></a><a name="ae6494d1877ab43e4b16f2f080e9bfa20"></a>Set the period based on how often a CMK is used. If it is frequently used, set a short period; otherwise, set a long one.</p>
    </td>
    </tr>
    </tbody>
    </table>

7.  Click  **Enable Rotation**. The page displaying the rotation details is displayed, as shown in  [Figure 3](#fccf4ddb4cc4543259b743554d6dbb7af).

    **Figure  3**  CMK rotation details<a name="fccf4ddb4cc4543259b743554d6dbb7af"></a>  
    ![](figures/cmk-rotation-details.png "cmk-rotation-details")

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >You can click  ![](figures/icon-edit.png)  to change the rotation period. After the period is changed, KMS rotates the CMK by the new period.  


