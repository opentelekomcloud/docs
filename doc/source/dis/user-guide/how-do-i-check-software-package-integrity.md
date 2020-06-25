# How Do I Check Software Package Integrity?<a name="dis_faq_0009"></a>

This section describes how to verify integrity of the DIS SDK software package on a Linux system by using a verification file.

## Prerequisites<a name="s4105765a7f484146a9d77cd7bf878754"></a>

-   The PuTTY tool is available.
-   The WinSCP tool is available.

## Procedure<a name="s2d0d3a107aab4159983abb5eece1b209"></a>

1.  Upload the DIS SDK software package  **dis-sdk-1.2.3.zip**  to any directory on the Linux system by using WinSCP.
2.  <a name="l8c35f745b7e945219234467020564558"></a>Log in to the Linux system by using PuTTY. In the directory in which  **dis-sdk-1.2.3.zip**  is stored, run the following command to obtain the verification code of the DIS SDK software package:

    **sha256sum dis-sdk-1.2.3.zip**

    Example verification code:

    ```
    # sha256sum dis-sdk-1.2.3.zip
    8be2c937e8d78b1a9b99777cee4e7131f8bf231de3f839cf214e7c5b5ba3c088 dis-sdk-1.2.3.zip
    ```

3.  Open the DIS SDK verification file  **dis-sdk-1.2.3.zip.sha256sum** and compare it with the verification code obtained in [2](#l8c35f745b7e945219234467020564558).
    -   If they are consistent, it indicates that the DIS SDK software package is not tampered with.
    -   If they are inconsistent, the DIS SDK software package is tampered with and you need to obtain an untampered package.


