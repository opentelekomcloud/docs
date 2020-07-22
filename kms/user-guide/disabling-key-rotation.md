# Disabling Key Rotation<a name="kms_01_0045"></a>

## Scenario<a name="section1774863214344"></a>

This section describes how to disable rotation for a key on the KMS console.

## Prerequisites<a name="sa444d90e5d214eb2811cd143d283ed46"></a>

-   You have obtained an account and its password for logging in to the management console.
-   The CMK is in  **Enabled**  status.
-   The  **Origin**  of the CMK is  **KMS**.
-   Key rotation has been enabled.

## Procedure<a name="section1953329183312"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner of the management console and select a region or project.
3.  Choose  **Security**  \>  **Key Management Service**. The  **Key Management Service**  page is displayed.
4.  Click the alias of the desired CMK to view its details.
5.  Click  **Rotation Policy**. The dialog box is displayed, as shown in  [Figure 1](#fig68513241314).

    **Figure  1**  CMK rotation details<a name="fig68513241314"></a>  
    ![](figures/cmk-rotation-details.png "cmk-rotation-details")

6.  Click  ![](figures/icon-open.png)  to disable key rotation.
7.  In the displayed  **Disable Rotation Policy**  dialog box, click  **Yes**.

    **Figure  2**  Disabling key rotation<a name="fig16274101884411"></a>  
    ![](figures/disabling-key-rotation.png "disabling-key-rotation")

8.  Check the rotation status, as shown in  [Figure 3](#fig1580712501294).

    **Figure  3**  Key rotation<a name="fig1580712501294"></a>  
    ![](figures/key-rotation.png "key-rotation")


