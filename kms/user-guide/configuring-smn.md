# Configuring SMN<a name="kms_01_0021"></a>

## Scenario<a name="section33487757104334"></a>

This section describes how to configure the Simple Message Notification \(SMN\) function on the Cloud Trace Service \(CTS\) console.

Decryption will fail if the CMK used has been scheduled for deletion. You will receive messages about the decryption failure on terminals \(SMS, email, HTTP, or HTTPS\) if the SMN function has been configured in CTS.

## Prerequisites<a name="section57729878104346"></a>

-   You have obtained an account and its password for logging in to the management console.
-   CTS has been enabled.
-   You have subscribed to SMN.

## Procedure<a name="section2642313510441"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner of the management console and select a region or project.
3.  Choose  **Management & Deployment**  \>  **Cloud Trace Service**  to go to the CTS console.
4.  In the navigation tree on the left, click  **Tracker**.
5.  If the desired tracker is not enabled, click  **Enable**. In the dialog box that is displayed, click  **OK**  to enable the tracker. If the tracker is already enabled, skip this step.
6.  In the navigation tree on the left, click  **Key Event Notifications**. The  **Key Event Notifications**  page is displayed.
7.  Click  **Create Key Event Notification**  at the upper right corner of the page. The creation page is displayed.
8.  In the  **Basic Information**  area, enter a notification name. See  [Figure 1](#fig197519401153)  for details.

    **Figure  1**  Configuring basic information<a name="fig197519401153"></a>  
    ![](figures/configuring-basic-information.png "configuring-basic-information")

9.  Select operation types in the  **Operation**  area. See  [Figure 2](#fig103085242037)  for details.

    **Figure  2**  Selecting operation types<a name="fig103085242037"></a>  
    ![](figures/selecting-operation-types.png "selecting-operation-types")

    **Table  1**  Parameters for operation types

    <a name="table974844017112"></a>
    <table><thead align="left"><tr id="row975324001110"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.4.1.1"><p id="p14754174018114"><a name="p14754174018114"></a><a name="p14754174018114"></a><strong id="b781913712291"><a name="b781913712291"></a><a name="b781913712291"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="56.99999999999999%" id="mcps1.2.4.1.2"><p id="p7755540161113"><a name="p7755540161113"></a><a name="p7755540161113"></a><strong id="b842352706193336"><a name="b842352706193336"></a><a name="b842352706193336"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.3"><p id="p12757154015119"><a name="p12757154015119"></a><a name="p12757154015119"></a><strong id="b1666133143013"><a name="b1666133143013"></a><a name="b1666133143013"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1277234051113"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="p12772184001112"><a name="p12772184001112"></a><a name="p12772184001112"></a>Operation Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.2 "><p id="p6773140181114"><a name="p6773140181114"></a><a name="p6773140181114"></a>SMN sends messages to users when deletion, creation, or login operations are performed on CMKs.</p>
    </td>
    <td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.3 "><p id="p2077784018118"><a name="p2077784018118"></a><a name="p2077784018118"></a>Delete</p>
    </td>
    </tr>
    </tbody>
    </table>

10. In the  **User**  area, specify the user who performs the specified operations. See  [Figure 3](#fig58261115592)  for details.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   You can select  **All users**  so that SMN notifications are sent when specified operations are performed by any user.  
    >-   You can also select  **Specified users**  and add users to the  **User List**. Then SMN notifications are sent when the specified operations are performed by specified users.  

    **Figure  3**  Specifying users<a name="fig58261115592"></a>  
    ![](figures/specifying-users.png "specifying-users")

11. In the  **Topic**  area, configure whether to send notifications. See  [Figure 4](#fig14611311075)  for details.

    **Figure  4**  Configuring SMN topic<a name="fig14611311075"></a>  
    ![](figures/configuring-smn-topic.png "configuring-smn-topic")

    **Table  2**  Parameters for configuring the SMN notification

    <a name="table6950950191420"></a>
    <table><thead align="left"><tr id="row1794875018140"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.4.1.1"><p id="p1694845015149"><a name="p1694845015149"></a><a name="p1694845015149"></a><strong>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="61%" id="mcps1.2.4.1.2"><p id="p8948450141410"><a name="p8948450141410"></a><a name="p8948450141410"></a><strong id="b1569808375"><a name="b1569808375"></a><a name="b1569808375"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.3"><p id="p1994855091419"><a name="p1994855091419"></a><a name="p1994855091419"></a><strong id="b842352706113752"><a name="b842352706113752"></a><a name="b842352706113752"></a>Configuration</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1994915091417"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="p169491550181420"><a name="p169491550181420"></a><a name="p169491550181420"></a>Send Notification</p>
    </td>
    <td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.2 "><p id="p11949205021412"><a name="p11949205021412"></a><a name="p11949205021412"></a>Specifies whether notifications will be sent.</p>
    <a name="ul99495502145"></a><a name="ul99495502145"></a><ul id="ul99495502145"><li>Select <strong id="b842352706105958"><a name="b842352706105958"></a><a name="b842352706105958"></a>Yes</strong> to activate notification.</li><li>Select <strong id="b84235270611036"><a name="b84235270611036"></a><a name="b84235270611036"></a>No</strong> to deactivate notification.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.3 "><p id="p694935011419"><a name="p694935011419"></a><a name="p694935011419"></a>Yes</p>
    </td>
    </tr>
    <tr id="row1294955011411"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="p10949115012143"><a name="p10949115012143"></a><a name="p10949115012143"></a>SMN Topic</p>
    </td>
    <td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.2 "><p id="p1894995051416"><a name="p1894995051416"></a><a name="p1894995051416"></a>You can select an existing topic or click <strong id="b84235270618437"><a name="b84235270618437"></a><a name="b84235270618437"></a>Topic</strong> to create a topic.</p>
    <p id="p894995019149"><a name="p894995019149"></a><a name="p894995019149"></a>For details about topics, see the <i><cite id="citec6d4c7dd347a4853a8892f68f2d2d7b6095641"><a name="citec6d4c7dd347a4853a8892f68f2d2d7b6095641"></a><a name="citec6d4c7dd347a4853a8892f68f2d2d7b6095641"></a>Simple Message Notification User Guide</cite></i>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.3 "><p id="p994965011410"><a name="p994965011410"></a><a name="p994965011410"></a>KMS</p>
    </td>
    </tr>
    </tbody>
    </table>

12. Click  **OK**. The SMN notification is configured.

