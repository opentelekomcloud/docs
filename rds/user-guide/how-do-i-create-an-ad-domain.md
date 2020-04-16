# How Do I Create an AD Domain?<a name="rds_faq_0112"></a>

Active Directory, which is short for AD, is a directory service on Windows Standard Server, Windows Enterprise Server, and Windows Datacenter Server. \(Active Directory cannot run on the Windows Web Server, but it can manage the computers running the Windows Web Server.\) Active Directory stores information about objects on the network and makes this information easy for administrators and users to find and use. Active Directory uses a structured data store as the basis for a logical, hierarchical organization of directory information.

## Procedure<a name="section178181710277"></a>

This section describes how to use Windows Server 2012 R2 to create a domain server.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>1.  When you configure an AD domain information during the DB instance creation, do not configure or disable Group Policy Object \(GPO\) for your domain controller server. Otherwise, the DB instance creation will fail.  
>2.  If GPO is required, you need to create an ECS and set up a new domain controller server with GPO disabled. Then, establish trust between your domain controller server and the new domain controller server. For details, contact customer service.  

1.  Install an AD domain controller.
    1.  In Server Manager, choose  **Manage**  \>  **Add Roles and Features**.
    2.  In the  **Add Roles and Features Wizard**  dialog box, click  **Next**  until the  **Select server roles**  page is displayed. Select  **Active Directory Domain Services**  and click  **Add Features**  in the displayed box.
    3.  Click  **Next**  until the  **Confirm installation selections**  page is displayed. Click  **Install**  to start the role installation process.
    4.  After the installation is complete, a yellow triangle icon is displayed. Click  **Promote this server to a domain controller**. The  **Active Directory Domain Services Configuration Wizard**  window is displayed.

        ![](figures/en-us_image_0226197169.png)

    5.  On the  **Deployment Configuration**  page, select  **Add a new forest**  and set a domain name, such as newrds.com.
    6.  Click  **Next**. On the displayed page, enter the DSRM password \(non-domain user\).
    7.  Click  **Next**  until the  **Prerequisites Check**  page displayed. Click  **Install**. After the installation is complete, the server automatically reboots.
    8.  Modify the DNS configuration of the network interface. Set the IP address of the active DNS server to the server's private IP address, such as 192.168.0.133.

2.  Create and add a domain account.
    1.  Open  **Active Directory Users and Computers**, right-click on the  **Users**  and choose  **New**  \>  **User**. Enter the username and click  **Next**.
    2.  Enter the first name, last name, and user logon name, such as luna@newrds.com.
    3.  Enter the password and then confirm it. Deselect all check boxes \(do not change the password at the first login\).
    4.  After the user is added, a figure similar to the following is displayed. You can add domain accounts to user groups for permission control.

        ![](figures/image_three.png)

    5.  Add the domain account for logging in to RDS to the Admin group.  ![](figures/image_one.png)![](figures/en-us_image_0226196782.png)![](figures/en-us_image_0226196735.png)![](figures/image_two.png)

3.  Add an RDS DB instance to the domain.

    On the Microsoft SQL Server instance creation page, click  **Configure**  to configure the AD domain and then complete the DB instance creation. After the instance is created, the AD domain can be used.

    ![](figures/image_four.png)

    **Table  1**  AD domain parameters

    <a name="en-us_topic_0192954124_table17700153119104"></a>
    <table><thead align="left"><tr id="row17586181911419"><th class="cellrowborder" valign="top" width="25.09%" id="mcps1.2.3.1.1"><p id="p558701904113"><a name="p558701904113"></a><a name="p558701904113"></a><strong id="b15948920132314"><a name="b15948920132314"></a><a name="b15948920132314"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="74.91%" id="mcps1.2.3.1.2"><p id="p1958719197413"><a name="p1958719197413"></a><a name="p1958719197413"></a><strong id="b152320222235"><a name="b152320222235"></a><a name="b152320222235"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0192954124_row570043161020"><td class="cellrowborder" valign="top" width="25.09%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0192954124_p1253012419555"><a name="en-us_topic_0192954124_p1253012419555"></a><a name="en-us_topic_0192954124_p1253012419555"></a>Directory Address</p>
    </td>
    <td class="cellrowborder" valign="top" width="74.91%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0192954124_p135079514431"><a name="en-us_topic_0192954124_p135079514431"></a><a name="en-us_topic_0192954124_p135079514431"></a>Enter the private IP address of the ECS that supports the AD domain.</p>
    <p id="en-us_topic_0192954124_p1201640182516"><a name="en-us_topic_0192954124_p1201640182516"></a><a name="en-us_topic_0192954124_p1201640182516"></a>For example: 192.168.x.x.</p>
    <div class="note" id="en-us_topic_0192954124_note317205818312"><a name="en-us_topic_0192954124_note317205818312"></a><a name="en-us_topic_0192954124_note317205818312"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0192954124_p1617214589316"><a name="en-us_topic_0192954124_p1617214589316"></a><a name="en-us_topic_0192954124_p1617214589316"></a>The ECS must be in the same subnet as the DB instance.</p>
    </div></div>
    </td>
    </tr>
    <tr id="en-us_topic_0192954124_row8700631121015"><td class="cellrowborder" valign="top" width="25.09%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0192954124_p18462733105818"><a name="en-us_topic_0192954124_p18462733105818"></a><a name="en-us_topic_0192954124_p18462733105818"></a>Domain Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="74.91%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0192954124_p05182429436"><a name="en-us_topic_0192954124_p05182429436"></a><a name="en-us_topic_0192954124_p05182429436"></a>A fully qualified domain name, such as DBStest.com, must:</p>
    <a name="en-us_topic_0192954124_ol1017819516413"></a><a name="en-us_topic_0192954124_ol1017819516413"></a><ol id="en-us_topic_0192954124_ol1017819516413"><li>Be the same as the ECS domain name.</li><li>Be no more than 48 characters long.</li><li>Only include letters, digits, dots (.), and hyphens (-).</li><li>Include a valid top-level domain name which is more than 2 characters long and contains only dots (.) and letters.</li></ol>
    </td>
    </tr>
    <tr id="en-us_topic_0192954124_row6700103115102"><td class="cellrowborder" valign="top" width="25.09%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0192954124_p9530112412554"><a name="en-us_topic_0192954124_p9530112412554"></a><a name="en-us_topic_0192954124_p9530112412554"></a>Directory Administrator</p>
    </td>
    <td class="cellrowborder" valign="top" width="74.91%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0192954124_p32316429583"><a name="en-us_topic_0192954124_p32316429583"></a><a name="en-us_topic_0192954124_p32316429583"></a>You are advised to enter the domain administrator username.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0192954124_row20700183115103"><td class="cellrowborder" valign="top" width="25.09%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0192954124_p1553092435512"><a name="en-us_topic_0192954124_p1553092435512"></a><a name="en-us_topic_0192954124_p1553092435512"></a>Directory Administrator Password</p>
    </td>
    <td class="cellrowborder" valign="top" width="74.91%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0192954124_p22811651192920"><a name="en-us_topic_0192954124_p22811651192920"></a><a name="en-us_topic_0192954124_p22811651192920"></a>Password of the directory administrator.</p>
    <p id="en-us_topic_0192954124_p121331037121419"><a name="en-us_topic_0192954124_p121331037121419"></a><a name="en-us_topic_0192954124_p121331037121419"></a>Must consist of 8 to 32 characters and must be a combination of uppercase letters, lowercase letters, digits, and at least one of the following special characters: ~!@#%^*-_=+? Enter a strong password and periodically change it to improve security, preventing security risks such as brute force cracking.</p>
    <p id="en-us_topic_0192954124_p10149123751418"><a name="en-us_topic_0192954124_p10149123751418"></a><a name="en-us_topic_0192954124_p10149123751418"></a>Keep this password secure. The system cannot retrieve it.</p>
    </td>
    </tr>
    </tbody>
    </table>


