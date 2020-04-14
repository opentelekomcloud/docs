# Changing the Alias and Description of a CMK<a name="kms_01_0033"></a>

## Scenario<a name="section6530676516634"></a>

The alias of a CMK is a user-friendly name designed to help you locate the CMK easier.

This section describes how to change the alias and description of a CMK on the KMS management console.

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>-   A Default Master Key \(the alias suffix of which is  **/default**\) does not allow alias and description changes.  
>-   The alias and description of a CMK cannot be changed if the CMK is in  **Pending deletion**  status.  

## Prerequisites<a name="section6205788316731"></a>

-   You have obtained an account and its password for logging in to the management console.
-   The CMK is in  **Enabled**,  **Disabled**, or  **Pending import**  status.

## Procedure<a name="section4980422016839"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner of the management console and select a region or project.
3.  Choose  **Security**  \>  **Key Management Service**. The  **Key Management Service**  page is displayed.
4.  Click the alias of the desired CMK. Details about the CMK are displayed.
5.  Click  ![](figures/icon-edit.png)  in the  **Alias**  or  **Description**  line to change the alias or description of the CMK,  [Figure 1](#fig12770609173123)  highlights these options.

    **Figure  1**  CMK details<a name="fig12770609173123"></a>  
    ![](figures/cmk-details.png "cmk-details")

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   The alias must be 1 to 255 characters in length. Only digits, letters, underscores \(\_\), hyphens \(-\), colons \(:\), and forward slashes \(/\) are allowed.  
    >-   Length of the description cannot exceed 255 characters.  

6.  Click  ![](figures/icon-complete.png)  to save the changes.

