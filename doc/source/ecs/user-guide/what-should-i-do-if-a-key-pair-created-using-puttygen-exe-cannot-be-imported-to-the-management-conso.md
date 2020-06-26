# What Should I Do If a Key Pair Created Using  **puttygen.exe**  Cannot Be Imported to the Management Console?<a name="EN-US_TOPIC_0047654687"></a>

## Symptom<a name="section51637593141938"></a>

When a key pair created using  **puttygen.exe**  was imported to the management console, the system displayed a message indicating that importing the public key failed.

## Possible Causes<a name="section30783045141945"></a>

The format of the public key content does not meet system requirements.

Storing a public key by clicking  **Save public key**  of  **puttygen.exe**  will change the format of the public key content. Such a key cannot be imported to the management console.

## Solution<a name="section24548136141951"></a>

Use the locally stored private key and  **PuTTY Key Generator**  to restore the format of the public key content. Then, import the public key to the management console.

1.  Double-click  **puttygen.exe**  to switch to the  **PuTTY Key Generator**  page.

    **Figure  1**  PuTTY Key Generator<a name="en-us_topic_0014250631_en-us_topic_0037960038_fig4490538015580"></a>  
    ![](figures/putty-key-generator.png "putty-key-generator")

2.  Click  **Load**  and select the private key.

    The system automatically loads the private key and restores the format of the public key content in  **PuTTY Key Generator**. The content in the red box in  [Figure 2](#fig5530274016810)  is the public key with the format meeting system requirements.

    **Figure  2**  Restoring the format of the public key content<a name="fig5530274016810"></a>  
    ![](figures/obtaining-the-public-and-private-keys.png "obtaining-the-public-and-private-keys")

3.  Copy the public key content to a .txt file and save the file in a local directory.
4.  Import the public key to the management console.
    1.  Log in to the management console.
    2.  Click  ![](figures/icon-region-0.png)  in the upper left corner and select the desired region and project.
    3.  Under  **Computing**, click  **Elastic Cloud Server**.
    4.  In the navigation pane on the left, choose  **Key Pair**.
    5.  On the right side of the page, click  **Import Key Pair**.
    6.  Copy the public key content in the .txt file to  **Public Key Content**  and click  **OK**.


