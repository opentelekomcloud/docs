# Configuring CORS<a name="en-us_topic_0045853860"></a>

This section describes how to use CORS in HTML5 to implement cross-origin access.

## Procedure<a name="s933c5484fd734428b5e2e24bf708a8e5"></a>

1.  Log in to OBS Browser.
2.  Select the bucket to be configured and click  **More**  \>  **Configure CORS Rule**.
3.  Click  **Add**.

    >![](public_sys-resources/icon-note.gif) **NOTE:** 
    >You can set a maximum of 100 CORS rules for one bucket.

4.  In the  **Add CORS Rule**  dialog box that is displayed, enter CORS rules.

    **Figure  1**  Adding a CORS rule<a name="fe30e6fe056434c66a690c9063d04e6bb"></a>  
    ![](figures/adding-a-cors-rule.png "adding-a-cors-rule")

    [Table 1](#t810c07199d9d4fb4949e45cc402582a0)  describes parameters in CORS rules.

    **Table  1**  Parameters in CORS rules

    <a name="t810c07199d9d4fb4949e45cc402582a0"></a>
    <table><thead align="left"><tr id="r282c3ed8eee94e42b62d5849670244ca"><th class="cellrowborder" valign="top" width="32%" id="mcps1.2.3.1.1"><p id="a602c237b70394ce5a689bb6ebdca0c16"><a name="a602c237b70394ce5a689bb6ebdca0c16"></a><a name="a602c237b70394ce5a689bb6ebdca0c16"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="68%" id="mcps1.2.3.1.2"><p id="a1d5215e5897b4b16828bfbc8b1878a5a"><a name="a1d5215e5897b4b16828bfbc8b1878a5a"></a><a name="a1d5215e5897b4b16828bfbc8b1878a5a"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r2ff60e1cc4c04df0bd1b01f6f2bb5196"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p id="a157438a1cf0e4973a1bbe1e79572c531"><a name="a157438a1cf0e4973a1bbe1e79572c531"></a><a name="a157438a1cf0e4973a1bbe1e79572c531"></a>Allowed Origin</p>
    </td>
    <td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><p id="af293f21d2e374fa4934e7bd8be3752eb"><a name="af293f21d2e374fa4934e7bd8be3752eb"></a><a name="af293f21d2e374fa4934e7bd8be3752eb"></a>Specifies the origin of cross-origin requests. That is, requests from the origin can access the bucket. This parameter is mandatory.</p>
    <p id="ac0e68ea7740c478ba86dfb9ee32ff300"><a name="ac0e68ea7740c478ba86dfb9ee32ff300"></a><a name="ac0e68ea7740c478ba86dfb9ee32ff300"></a>Multiple matching rules are allowed. One rule occupies one line, and allows one wildcard character (<strong id="b15430134443519"><a name="b15430134443519"></a><a name="b15430134443519"></a>*</strong>) at most. Example:</p>
    <pre class="screen" id="scbcd7fb5598746eb8312b7ae6cacc05f"><a name="scbcd7fb5598746eb8312b7ae6cacc05f"></a><a name="scbcd7fb5598746eb8312b7ae6cacc05f"></a>http://rds.example.com
    https://*.vbs.example.com</pre>
    </td>
    </tr>
    <tr id="rab81f76db9364bf8ab978a987ee0e07b"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p id="a25b2e075e2234e10937f43f599273668"><a name="a25b2e075e2234e10937f43f599273668"></a><a name="a25b2e075e2234e10937f43f599273668"></a>Allowed Method</p>
    </td>
    <td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><p id="a901f59948c80429583c364e96bd352c6"><a name="a901f59948c80429583c364e96bd352c6"></a><a name="a901f59948c80429583c364e96bd352c6"></a>Specifies the method of cross-origin requests, that is, the operation type of buckets and objects. This parameter is mandatory. The following methods are included: Get, Post, Put, Delete, and Head.</p>
    </td>
    </tr>
    <tr id="r467a5c6a833f4015bb22f4087de6b74c"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p id="a6dc9a4d89e134b2aa83df07975ff13fe"><a name="a6dc9a4d89e134b2aa83df07975ff13fe"></a><a name="a6dc9a4d89e134b2aa83df07975ff13fe"></a>Allowed Header</p>
    </td>
    <td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><p id="adea4598de03143f2a8e47195d17341d1"><a name="adea4598de03143f2a8e47195d17341d1"></a><a name="adea4598de03143f2a8e47195d17341d1"></a>Specifies the allowed header of cross-origin requests. This parameter is optional. Only CORS requests matching the allowed header are valid.</p>
    <p id="a055e9cbebabc4c85ad34a31b69b5ada3"><a name="a055e9cbebabc4c85ad34a31b69b5ada3"></a><a name="a055e9cbebabc4c85ad34a31b69b5ada3"></a>You can enter multiple allowed headers (one per line) and each line can contain one wildcard character (*) at most. Spaces and special characters including <strong id="b56257227210"><a name="b56257227210"></a><a name="b56257227210"></a>&amp;:&lt;</strong> are not allowed.</p>
    </td>
    </tr>
    <tr id="r64d7889221344540a64115505d5e1e72"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p id="a910e77b75bbd4c2986a23ce2aab35e6f"><a name="a910e77b75bbd4c2986a23ce2aab35e6f"></a><a name="a910e77b75bbd4c2986a23ce2aab35e6f"></a>Exposed Header</p>
    </td>
    <td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><p id="a4e770b7fc6404388bcf68eb959df4401"><a name="a4e770b7fc6404388bcf68eb959df4401"></a><a name="a4e770b7fc6404388bcf68eb959df4401"></a>Specifies the supplemented header in CORS responses, providing additional information for clients. This parameter is optional.</p>
    <p id="a37cf726ebb9649ef98d0256ee1c35dc9"><a name="a37cf726ebb9649ef98d0256ee1c35dc9"></a><a name="a37cf726ebb9649ef98d0256ee1c35dc9"></a>You can enter multiple exposed headers (one per line). Spaces and special characters including <strong id="b31335915574"><a name="b31335915574"></a><a name="b31335915574"></a>*&amp;:&lt;</strong> are not allowed.</p>
    </td>
    </tr>
    <tr id="r878b4e4c1aa9415ebabb6923463b8153"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p id="a69c5c5a0268b4a33a275a5109847d94c"><a name="a69c5c5a0268b4a33a275a5109847d94c"></a><a name="a69c5c5a0268b4a33a275a5109847d94c"></a>Cache Duration (s)</p>
    </td>
    <td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><p id="ab09e25a0b9b74b6a978e809ab22ba139"><a name="ab09e25a0b9b74b6a978e809ab22ba139"></a><a name="ab09e25a0b9b74b6a978e809ab22ba139"></a>Mandatory. Specifies the duration that your browser can cache CORS responses, expressed in seconds. The default value is 100.</p>
    </td>
    </tr>
    </tbody>
    </table>

5.  Click  **OK**.
6.  Click  **OK**  to save the rules.

    After CORS is successfully configured, only the addresses specified in  **Allowed Origin**  can access a bucket in OBS using the method specified in  **Allowed Method**. For example, you configure CORS parameters of bucket  **testbucket**  as follows:  **Allowed Origin: www.example.com**;  **Allowed Method: GET**;  **Allowed Header**: left blank;  **Exposed Header**: left blank;  **Cache Duration \(s\): 100**. Then OBS only allows GET requests from  **www.example.com**  to access the  **testbucket**, without restrictions on request headers. The client can cache the CORS response for 100 seconds. 

7.  In the displayed dialog box, click  **Close**  to close the dialog box.

