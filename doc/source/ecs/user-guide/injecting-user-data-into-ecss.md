# Injecting User Data into ECSs<a name="EN-US_TOPIC_0032380449"></a>

## Scenarios<a name="section59120639141539"></a>

Use the user data injection function to inject user data into ECSs to:

-   Simplify ECS configuration.
-   Initialize the ECS OS configuration.
-   Upload your scripts to ECSs during ECS creation.
-   Perform other tasks using scripts.

## Use Restrictions<a name="section31714110141539"></a>

-   Linux
    -   The image that is used to create ECSs must have Cloud-Init installed.

    -   The user data to be injected must be less than or equal to 32 KB.
    -   If user data is uploaded as text, the data can contain only ASCII characters. If user data is uploaded using a file, the file can contain any characters and the file size cannot exceed 32 KB.
    -   The image that is used to create ECSs must be a public image, a private image created based on a public image, or a private image with Cloud-Init installed.
    -   The format of the customized scripts must comply with user data script specifications.
    -   DHCP must be enabled on the VPC network, and port 80 must be enabled for the security group in the outbound direction.

-   Windows
    -   The image that is used to create ECSs must have Cloudbase-Init installed.
    -   The user data to be injected must be less than or equal to 32 KB.
    -   User data uploaded as text can contain only ASCII characters. User data uploaded as a file can contain any characters, and the file size must be less than or equal to 32 KB.
    -   The image that is used to create ECSs must be a public image, a private image created based on a public image, or a private image with Cloudbase-Init installed.
    -   DHCP must be enabled on the VPC network, and port 80 must be enabled for the security group in the outbound direction.


## Injecting User Data<a name="section60709488141539"></a>

1.  Create a user data script, the format of which complies with user data script specifications. For details, see  [Helpful Links](#section54344118153243).
2.  When creating an ECS, set  **Advanced Options**  to  **Configure now**, and paste the content of the user data script to the  **User Data Injection**  text box or upload the user data file.

    >![](/images/icon-note.gif) **NOTE:**   
    >User data can be injected as either text or a file.  
    >Text: Copy the content of the user data script to the text box.  
    >File: Save the user data script to a text file and then upload the file.  

    **Figure  1**  Injecting user data<a name="fig87313493915"></a>  
    ![](figures/injecting-user-data.png "injecting-user-data")

3.  The created ECS automatically runs Cloud-Init/Cloudbase-Init and reads the user data script upon startup.

## User Data Scripts of Linux ECSs<a name="section0609912614"></a>

Customized user data scripts of Linux ECSs are based on the open-source Cloud-Init architecture. This architecture uses ECS metadata as the data source for automatically configuring the ECSs. The customized script types are compatible with open-source Cloud-Init. For details about Cloud-Init, see  [http://cloudinit.readthedocs.io/en/latest/topics/format.html](http://cloudinit.readthedocs.io/en/latest/topics/format.html).

-   Script execution time: A customized user data script is executed after the time when the status of the target ECS changes to  **Running**  and before the time when  **/etc/init**  is executed.

    >![](/images/icon-note.gif) **NOTE:**   
    >By default, the scripts are executed as user  **root**.  


-   Script type: Both user-data scripts and Cloud-Config data scripts are supported.

    **Table  1**  Linux ECS script types

    <a name="table039994053718"></a>
    <table><thead align="left"><tr id="row4399194017376"><th class="cellrowborder" valign="top" width="17.648235176482352%" id="mcps1.2.4.1.1"><p id="p1239916402370"><a name="p1239916402370"></a><a name="p1239916402370"></a>-</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.125587441255874%" id="mcps1.2.4.1.2"><p id="p1939914407374"><a name="p1939914407374"></a><a name="p1939914407374"></a>User-Data Script</p>
    </th>
    <th class="cellrowborder" valign="top" width="38.226177382261774%" id="mcps1.2.4.1.3"><p id="p1439913405374"><a name="p1439913405374"></a><a name="p1439913405374"></a>Cloud-Config Data Script</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3399194012374"><td class="cellrowborder" valign="top" width="17.648235176482352%" headers="mcps1.2.4.1.1 "><p id="p3399174019374"><a name="p3399174019374"></a><a name="p3399174019374"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.125587441255874%" headers="mcps1.2.4.1.2 "><p id="p239984053714"><a name="p239984053714"></a><a name="p239984053714"></a>Scripts, such as Shell and Python scripts, are used for custom configurations.</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.226177382261774%" headers="mcps1.2.4.1.3 "><p id="p839964053718"><a name="p839964053718"></a><a name="p839964053718"></a>Methods pre-defined in Cloud-Init, such as the Yum source and SSH key, are used for configuring certain ECS applications.</p>
    </td>
    </tr>
    <tr id="row73991405372"><td class="cellrowborder" valign="top" width="17.648235176482352%" headers="mcps1.2.4.1.1 "><p id="p1399174073719"><a name="p1399174073719"></a><a name="p1399174073719"></a>Format</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.125587441255874%" headers="mcps1.2.4.1.2 "><p id="p7604786420"><a name="p7604786420"></a><a name="p7604786420"></a>A script must be started with <span class="parmvalue" id="parmvalue25671095321313"><a name="parmvalue25671095321313"></a><a name="parmvalue25671095321313"></a><b>#!</b></span>, for example, <span class="parmvalue" id="parmvalue1569820674213056"><a name="parmvalue1569820674213056"></a><a name="parmvalue1569820674213056"></a><b>#!/bin/bash</b></span> and <span class="parmvalue" id="parmvalue982854425213127"><a name="parmvalue982854425213127"></a><a name="parmvalue982854425213127"></a><b>#!/usr/bin/env python</b></span>.</p>
    <p id="p173991540123716"><a name="p173991540123716"></a><a name="p173991540123716"></a>When a script is started for the first time, it will be executed at the rc.local-like level, indicating a low priority in the boot sequence.</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.226177382261774%" headers="mcps1.2.4.1.3 "><p id="p113991340193713"><a name="p113991340193713"></a><a name="p113991340193713"></a>The first line must be <span class="parmvalue" id="parmvalue65262554154555"><a name="parmvalue65262554154555"></a><a name="parmvalue65262554154555"></a><b>#cloud-config</b></span>, and no space is allowed in front of it.</p>
    </td>
    </tr>
    <tr id="row3399114093716"><td class="cellrowborder" valign="top" width="17.648235176482352%" headers="mcps1.2.4.1.1 "><p id="p73991440103715"><a name="p73991440103715"></a><a name="p73991440103715"></a>Constraint</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.125587441255874%" headers="mcps1.2.4.1.2 "><p id="p7399104013377"><a name="p7399104013377"></a><a name="p7399104013377"></a>Before Base64 encoding, the size of the script, including the first line, cannot exceed 32 KB.</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.226177382261774%" headers="mcps1.2.4.1.3 "><p id="p5400134023711"><a name="p5400134023711"></a><a name="p5400134023711"></a>Before Base64 encoding, the size of the script, including the first line, cannot exceed 32 KB.</p>
    </td>
    </tr>
    <tr id="row11400540123715"><td class="cellrowborder" valign="top" width="17.648235176482352%" headers="mcps1.2.4.1.1 "><p id="p7599171419383"><a name="p7599171419383"></a><a name="p7599171419383"></a>Frequency</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.125587441255874%" headers="mcps1.2.4.1.2 "><p id="p144004404378"><a name="p144004404378"></a><a name="p144004404378"></a>The script is executed only once when the ECS is started for the first time.</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.226177382261774%" headers="mcps1.2.4.1.3 "><p id="p7400164012372"><a name="p7400164012372"></a><a name="p7400164012372"></a>The execution frequency varies according to the applications configured on the ECS.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   How can I view the customized user data injected into a Linux ECS?
    1.  Log in to the ECS.
    2.  Run the following command to view the customized user data as user  **root**:

        **curl http://169.254.169.254/openstack/latest/user\_data**


-   Script usage examples

    This section describes how to inject scripts in different formats into Linux ECSs and view script execution results.

    **Example 1: Inject a user-data script.**

    When creating an ECS, set  **User Data Injection**  to  **Text**  and enter the customized user data script.

    ```
    #!/bin/bash
    echo "Hello, the time is now $(date -R)" | tee /root/output.txt
    ```

    After the ECS is created, start it and run the  **cat **_\[file\]_  command to check the script execution result.

    ```
    [root@XXXXXXXX ~]# cat /root/output.txt
    Hello, the time is now Mon, 16 Jul 2016 16:03:18+0800
    ```

    **Example 2: Inject a Cloud-Config data script.**

    When creating an ECS, set  **User Data Injection**  to  **Text**  and enter the customized user data script.

    ```
    #cloud-config
    bootcmd:
    - echo 192.168.1.130 us.archive.ubuntu.com >> /etc/hosts
    ```

    After the ECS is created, start it and run the  **cat /etc/hosts**  command to check the script execution result.

    **Figure  2**  Viewing operating results<a name="fig1787242875415"></a>  
    ![](figures/viewing-operating-results.png "viewing-operating-results")


## User Data Scripts of Windows ECSs<a name="section104417127157"></a>

Customized user data scripts of Windows ECSs are based on the open-source Cloudbase-Init architecture. This architecture uses ECS metadata as the data source for initializing and automatically configuring the ECSs. The customized script types are compatible with open-source Cloudbase-Init. For details about Cloudbase-Init, see  [https://cloudbase-init.readthedocs.io/en/latest/userdata.html](https://cloudbase-init.readthedocs.io/en/latest/userdata.html).

-   Script type: Both batch-processing program scripts and PowerShell scripts are supported.

    **Table  2**  Windows ECS script types

    <a name="table17839134102219"></a>
    <table><thead align="left"><tr id="row168401412224"><th class="cellrowborder" valign="top" width="17.18%" id="mcps1.2.4.1.1"><p id="p9840194120228"><a name="p9840194120228"></a><a name="p9840194120228"></a>-</p>
    </th>
    <th class="cellrowborder" valign="top" width="41.870000000000005%" id="mcps1.2.4.1.2"><p id="p1584013415223"><a name="p1584013415223"></a><a name="p1584013415223"></a>Batch-Processing Program Script</p>
    </th>
    <th class="cellrowborder" valign="top" width="40.949999999999996%" id="mcps1.2.4.1.3"><p id="p884014192212"><a name="p884014192212"></a><a name="p884014192212"></a>PowerShell Script</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1384019418223"><td class="cellrowborder" valign="top" width="17.18%" headers="mcps1.2.4.1.1 "><p id="p784064142212"><a name="p784064142212"></a><a name="p784064142212"></a>Format</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.870000000000005%" headers="mcps1.2.4.1.2 "><p id="p984016414220"><a name="p984016414220"></a><a name="p984016414220"></a>The script must be started with <span class="parmvalue" id="parmvalue76648425916272"><a name="parmvalue76648425916272"></a><a name="parmvalue76648425916272"></a><b>rem cmd</b></span>, which is the first line of the script. No space is allowed at the beginning of the first line.</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.949999999999996%" headers="mcps1.2.4.1.3 "><p id="p138409411221"><a name="p138409411221"></a><a name="p138409411221"></a>The script must be started with <span class="parmvalue" id="parmvalue975646085162756"><a name="parmvalue975646085162756"></a><a name="parmvalue975646085162756"></a><b>#ps1</b></span>, which is the first line of the script. No space is allowed at the beginning of the first line.</p>
    </td>
    </tr>
    <tr id="row11840841202215"><td class="cellrowborder" valign="top" width="17.18%" headers="mcps1.2.4.1.1 "><p id="p1840174162220"><a name="p1840174162220"></a><a name="p1840174162220"></a>Constraint</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.870000000000005%" headers="mcps1.2.4.1.2 "><p id="p19840184112223"><a name="p19840184112223"></a><a name="p19840184112223"></a>Before Base64 encoding, the size of the script, including the first line, cannot exceed 32 KB.</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.949999999999996%" headers="mcps1.2.4.1.3 "><p id="p384017415229"><a name="p384017415229"></a><a name="p384017415229"></a>Before Base64 encoding, the size of the script, including the first line, cannot exceed 32 KB.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   How can I view the customized user data injected into a Windows ECS?
    1.  Log in to the ECS.
    2.  Access the following URL in the address box of the browser and view the injected user data:

        **http://169.254.169.254/openstack/latest/user\_data**


-   Script usage examples

    This section describes how to inject scripts in different formats into Windows ECSs and view script execution results.

    **Example 1: Inject a batch-processing program script.**

    When creating an ECS, set  **User Data Injection**  to  **Text**  and enter the customized user data script.

    ```
    rem cmd
    echo "Hello, BAT Test" > C:\1111.txt
    ```

    After the ECS is created, start it and check the script execution result. In this example, a text file named  **1111**  is added to disk C:\\.

    **Figure  3**  Creating text file \(Batch\)<a name="fig8622411077"></a>  
    ![](figures/creating-text-file-(batch).png "creating-text-file-(batch)")

    To view the user data injected into the Windows ECS, log in at http://169.254.169.254/openstack/latest/user\_data.

    **Figure  4**  Viewing user data \(Batch\)<a name="fig14281122141212"></a>  
    ![](figures/viewing-user-data-(batch).png "viewing-user-data-(batch)")

    **Example 2: Inject a PowerShell script.**

    When creating an ECS, set  **User Data Injection**  to  **Text**  and enter the customized user data script.

    ```
    #ps1
    echo "Hello, Powershell Test" > C:\aaaa.txt
    ```

    After the ECS is created, start it and check the script execution result. In this example, a text file named  **aaaa**  is added to disk C:\\.

    **Figure  5**  Creating text file \(PowerShell\)<a name="fig103618447159"></a>  
    ![](figures/creating-text-file-(powershell).png "creating-text-file-(powershell)")

    To view the user data injected into the Windows ECS, log in at http://169.254.169.254/openstack/latest/user\_data.

    **Figure  6**  Viewing user data \(PowerShell\)<a name="fig124617204176"></a>  
    ![](figures/viewing-user-data-(powershell).jpg "viewing-user-data-(powershell)")


## Case 1<a name="section24296060141539"></a>

This case illustrates how to use the user data injection function to simplify Linux ECS configuration.

In this example, vim is configured to enable syntax highlighting, display line numbers, and set the tab stop to  **4**. The .vimrc configuration file is created and injected into the  **/root/.vimrc**  directory during ECS creation. After the ECS is created, vim is automatically configured based on your requirements. This improves ECS configuration efficiency, especially in batch ECS creation scenarios.

The content of the script file to be injected is as follows:

```
#cloud-config
write_files:
  - path: /root/.vimrc
    content: |
      syntax on
      set tabstop=4
      set number      
```

## Case 2<a name="section378450257"></a>

This case illustrates how to use the user data injection function to set the password for logging in to a Linux ECS.

>![](/images/icon-note.gif) **NOTE:**   
>The new password must meet the password complexity requirements listed in  [Table 3](#en-us_topic_0021426802_table4381109318958).  

**Table  3**  Password complexity requirements

<a name="en-us_topic_0021426802_table4381109318958"></a>
<table><thead align="left"><tr id="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_row925712618958"><th class="cellrowborder" valign="top" width="18.000000000000004%" id="mcps1.2.4.1.1"><p id="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p1162970218958"><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p1162970218958"></a><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p1162970218958"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="58.910000000000004%" id="mcps1.2.4.1.2"><p id="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p248177818958"><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p248177818958"></a><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p248177818958"></a>Requirement</p>
</th>
<th class="cellrowborder" valign="top" width="23.090000000000003%" id="mcps1.2.4.1.3"><p id="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p6680635518958"><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p6680635518958"></a><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p6680635518958"></a>Example Value</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_row4260571318958"><td class="cellrowborder" valign="top" width="18.000000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p2851073918958"><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p2851073918958"></a><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p2851073918958"></a>Password</p>
</td>
<td class="cellrowborder" valign="top" width="58.910000000000004%" headers="mcps1.2.4.1.2 "><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_ul5961106018958"></a><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_ul5961106018958"></a><ul id="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_ul5961106018958"><li>Consists of 8 characters to 26 characters.</li><li>Contains at least three of the following character types:<a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_ul24583583181022"></a><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_ul24583583181022"></a><ul id="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_ul24583583181022"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters: $!@%-_=+[]:./^,{}?</li></ul>
</li><li>Cannot contain the username or the username spelled backwards.</li><li>Cannot contain more than two characters in the same sequence as they appear in the username. (This requirement applies only to Windows ECSs.)</li></ul>
</td>
<td class="cellrowborder" valign="top" width="23.090000000000003%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p6481855218958"><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p6481855218958"></a><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p6481855218958"></a>YNbUwp!dUc9MClnv</p>
<div class="note" id="en-us_topic_0035643949_note18511011891"><a name="en-us_topic_0035643949_note18511011891"></a><a name="en-us_topic_0035643949_note18511011891"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0035643949_p351011796"><a name="en-us_topic_0035643949_p351011796"></a><a name="en-us_topic_0035643949_p351011796"></a>The example password is generated randomly. Do not copy this example password.</p>
</div></div>
</td>
</tr>
</tbody>
</table>

The content of the script file to be injected is as follows:

-   Using a plaintext password \(recommended\)

    Password  **Cloud.1234**  is used as an example.

    ```
    #!/bin/bash
    echo 'root:Cloud.1234' | chpasswd;
    ```

-   Using a ciphertext password

    ```
    #!/bin/bash 
    echo 'root:$6$V6azyeLwcD3CHlpY$BN3VVq18fmCkj66B4zdHLWevqcxlig' | chpasswd -e;
    ```

    In the preceding command output,  **$6$V6azyeLwcD3CHlpY$BN3VVq18fmCkj66B4zdHLWevqcxlig**  is the ciphertext password, which can be generated as follows:

    1.  Run the following command to generate an encrypted ciphertext value:

        **python -c "import crypt, getpass, pwd;print crypt.mksalt\(\)"**

        The following information is displayed:

        ```
        $6$V6azyeLwcD3CHlpY
        ```

    2.  Run the following command to generate a ciphertext password based on the salt value:

        **python -c "import crypt, getpass, pwd;print crypt.crypt\('Cloud.1234','\\$6\\$V6azyeLwcD3CHlpY'\)"**

        The following information is displayed:

        ```
        $6$V6azyeLwcD3CHlpY$BN3VVq18fmCkj66B4zdHLWevqcxlig
        ```



After the ECS is created, you can use the password to log in to it.

## Case 3<a name="section852885517018"></a>

This case illustrates how to use the user data injection function to reset the password for logging in to a Linux ECS.

In this example, the password of user  **root**  is reset to  **\*\*\*\*\*\***.

>![](/images/icon-note.gif) **NOTE:**   
>The new password must meet the password complexity requirements listed in  [Table 4](#table580060101120).  

**Table  4**  Password complexity requirements

<a name="table580060101120"></a>
<table><thead align="left"><tr id="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_row925712618958_1"><th class="cellrowborder" valign="top" width="18.000000000000004%" id="mcps1.2.4.1.1"><p id="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p1162970218958_1"><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p1162970218958_1"></a><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p1162970218958_1"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="58.910000000000004%" id="mcps1.2.4.1.2"><p id="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p248177818958_1"><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p248177818958_1"></a><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p248177818958_1"></a>Requirement</p>
</th>
<th class="cellrowborder" valign="top" width="23.090000000000003%" id="mcps1.2.4.1.3"><p id="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p6680635518958_1"><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p6680635518958_1"></a><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p6680635518958_1"></a>Example Value</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_row4260571318958_1"><td class="cellrowborder" valign="top" width="18.000000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p2851073918958_1"><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p2851073918958_1"></a><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p2851073918958_1"></a>Password</p>
</td>
<td class="cellrowborder" valign="top" width="58.910000000000004%" headers="mcps1.2.4.1.2 "><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_ul5961106018958_1"></a><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_ul5961106018958_1"></a><ul id="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_ul5961106018958_1"><li>Consists of 8 characters to 26 characters.</li><li>Contains at least three of the following character types:<a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_ul24583583181022_1"></a><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_ul24583583181022_1"></a><ul id="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_ul24583583181022_1"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters: $!@%-_=+[]:./^,{}?</li></ul>
</li><li>Cannot contain the username or the username spelled backwards.</li><li>Cannot contain more than two characters in the same sequence as they appear in the username. (This requirement applies only to Windows ECSs.)</li></ul>
</td>
<td class="cellrowborder" valign="top" width="23.090000000000003%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p6481855218958_1"><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p6481855218958_1"></a><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p6481855218958_1"></a>YNbUwp!dUc9MClnv</p>
<div class="note" id="en-us_topic_0035643949_note18511011891_1"><a name="en-us_topic_0035643949_note18511011891_1"></a><a name="en-us_topic_0035643949_note18511011891_1"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0035643949_p351011796_1"><a name="en-us_topic_0035643949_p351011796_1"></a><a name="en-us_topic_0035643949_p351011796_1"></a>The example password is generated randomly. Do not copy this example password.</p>
</div></div>
</td>
</tr>
</tbody>
</table>

The content of the script file to be injected is as follows. \(Retain the indentation in the following script.\)

```
#cloud-config
chpasswd:
  list: |
    root:******
  expire: False
```

After the ECS is created, you can use the reset password to log in to it. To ensure system security, change the password of user  **root**  after logging in to the ECS for the first time.

## Case 4<a name="section2212289417182"></a>

This case illustrates how to use the user data injection function to create a user on a Windows ECS and configure the password for the user.

In this example, the user's username is  **abc**, its password is  **\*\*\*\*\*\***, and the user is added to the  **administrators**  user group.

>![](/images/icon-note.gif) **NOTE:**   
>The new password must meet the password complexity requirements listed in  [Table 4](#table580060101120).  

The content of the script file to be injected is as follows:

```
rem cmd
net user abc ****** /add
net localgroup administrators abc /add
```

After the ECS is created, you can use the created username and password to log in to it.

## Case 5<a name="section19429115512011"></a>

This case illustrates how to use the user data injection function to update system software packages for a Linux ECS and enable the HTTPd service. After the user data is injected, you can use the HTTPd service.

The content of the script file to be injected is as follows:

```
#!/bin/bash
yum update -y
service httpd start
chkconfig httpd on
```

## Case 6<a name="section22603169194910"></a>

This case illustrates how to use the user data injection function to assign user  **root**  permission for remotely logging in to a Linux ECS. After injecting the file, you can log in to the ECS as user  **root**  using SSH key pair authentication.

The content of the script file to be injected is as follows:

```
#cloud-config
disable_root: false
runcmd:
- sed -i 's/^PermitRootLogin.*$/PermitRootLogin without-password/' /etc/ssh/sshd_config
- sed -i '/^KexAlgorithms.*$/d' /etc/ssh/sshd_config
- service sshd restart
```

## Helpful Links<a name="section54344118153243"></a>

For more information about user data injection cases, visit the official Cloud-init/Cloudbase-init website:

-   [https://cloudinit.readthedocs.io/en/latest/](https://cloudinit.readthedocs.io/en/latest/)

-   [https://cloudbase-init.readthedocs.io/en/latest/](https://cloudbase-init.readthedocs.io/en/latest/)

