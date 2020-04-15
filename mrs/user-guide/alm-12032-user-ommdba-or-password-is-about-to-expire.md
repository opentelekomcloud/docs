# ALM-12032 User ommdba or Password Is About to Expire<a name="EN-US_TOPIC_0125375736"></a>

## Description<a name="s20b233822ee84c13830a2318a950bf23"></a>

At 00:00 every day, the system starts checking whether user  **ommdba**  and its password are about to expire every 8 hours. This alarm is generated when the user or password is going to expire in 15 days.

It is cleared when the validity period of user  **ommdba**  is changed or the password is reset and the alarm handling is complete.

## Attribute<a name="s767dd084459c4fd19d594d2ab79e6dd3"></a>

<a name="t67c7cce42d9a47169fd50dfe19363ac3"></a>
<table><thead align="left"><tr id="rea6fae53bb564232ae9806b489635da1"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="aabee5155797746a6ad51578446195b78"><a name="aabee5155797746a6ad51578446195b78"></a><a name="aabee5155797746a6ad51578446195b78"></a><strong id="a91a53fc9c6774864be331bc1bfb2e687"><a name="a91a53fc9c6774864be331bc1bfb2e687"></a><a name="a91a53fc9c6774864be331bc1bfb2e687"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="a0e04994c35d948edb116bd7eb57362ea"><a name="a0e04994c35d948edb116bd7eb57362ea"></a><a name="a0e04994c35d948edb116bd7eb57362ea"></a><strong id="a144333ae1f394d5b9f3f9976ec26463b"><a name="a144333ae1f394d5b9f3f9976ec26463b"></a><a name="a144333ae1f394d5b9f3f9976ec26463b"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="af05c69a8a45d4dcc83a61fc31cd2832d"><a name="af05c69a8a45d4dcc83a61fc31cd2832d"></a><a name="af05c69a8a45d4dcc83a61fc31cd2832d"></a><strong id="ad3e89da8007a4fa2b51ee97a70005582"><a name="ad3e89da8007a4fa2b51ee97a70005582"></a><a name="ad3e89da8007a4fa2b51ee97a70005582"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r2b676119103b4a02a68617d540d4329b"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="a53500bb1f89349eab6889278ae039647"><a name="a53500bb1f89349eab6889278ae039647"></a><a name="a53500bb1f89349eab6889278ae039647"></a>12032</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="a57469254921247f1a7475f1605d44a44"><a name="a57469254921247f1a7475f1605d44a44"></a><a name="a57469254921247f1a7475f1605d44a44"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="a533cbb248f9648ae84f55ba94c597e51"><a name="a533cbb248f9648ae84f55ba94c597e51"></a><a name="a533cbb248f9648ae84f55ba94c597e51"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s990ee55994e34a24a33b99dba58fe6ee"></a>

<a name="t89ffd7c1d15e497cadac5759e251d287"></a>
<table><thead align="left"><tr id="re7a281cdf9984dea93030a10ed0bede8"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="a57615cdf741f426d83988521dd2fb555"><a name="a57615cdf741f426d83988521dd2fb555"></a><a name="a57615cdf741f426d83988521dd2fb555"></a><strong id="a43d06e2b8d784e339574912fae745736"><a name="a43d06e2b8d784e339574912fae745736"></a><a name="a43d06e2b8d784e339574912fae745736"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="a23b469bc13ea44fb860aeffabbd3048f"><a name="a23b469bc13ea44fb860aeffabbd3048f"></a><a name="a23b469bc13ea44fb860aeffabbd3048f"></a><strong id="a98955f1e54b24e31a8dbff08eea75a24"><a name="a98955f1e54b24e31a8dbff08eea75a24"></a><a name="a98955f1e54b24e31a8dbff08eea75a24"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r876bb1fcaa6f4b29b43a25908327d6a4"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="aed74424a93ae44299036e3b5fd0d28de"><a name="aed74424a93ae44299036e3b5fd0d28de"></a><a name="aed74424a93ae44299036e3b5fd0d28de"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a3c6ca2c467054a6894808374419d783f"><a name="a3c6ca2c467054a6894808374419d783f"></a><a name="a3c6ca2c467054a6894808374419d783f"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="r314d378edc2a4012866cbaa3fb71d8db"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="af09d5958bd5044af889e2e3ab2b4fd5c"><a name="af09d5958bd5044af889e2e3ab2b4fd5c"></a><a name="af09d5958bd5044af889e2e3ab2b4fd5c"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a74e00a48cbfa4534a3a7716fd87d8349"><a name="a74e00a48cbfa4534a3a7716fd87d8349"></a><a name="a74e00a48cbfa4534a3a7716fd87d8349"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="r4a4e15385f704eb09ef78537ad17f816"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035509088_p81497113018"><a name="en-us_topic_0035509088_p81497113018"></a><a name="en-us_topic_0035509088_p81497113018"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a36ba80cc6b5f4b6e87d9e21a1a4821cd"><a name="a36ba80cc6b5f4b6e87d9e21a1a4821cd"></a><a name="a36ba80cc6b5f4b6e87d9e21a1a4821cd"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="sa6f604d80f544d56b97c02a2b7116e99"></a>

The OMS database cannot be managed and data cannot be accessed.

## Possible Causes<a name="sb05eb9802c2146df8eee3054e084b44f"></a>

User  **ommdba**  or its password is about to expire.

## Procedure<a name="sa9bdd4d2ee5049d7bf137a19d09d8c2e"></a>

1.  Check whether user  **ommdba**  and its password in the system are valid.
    1.  Log in to the faulty node.
    2.  Run the following command to view information about user  **ommdba**  and its password:

        **chage -l ommdba**

    3.  Check whether the user and password are about to expire based on the system message.

        1.  View the value of  **Password expires**  to check whether the password is about to expire.
        2.  View the value of  **Account expires**  to check whether the user is about to expire.

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >If the parameter value is  **never**, the user and password are valid permanently; if the value is a date, check whether the user and password are going to expire within 15 days.  

        -   If yes, go to  [1.d](#laadf0da13df34c51878b081c44194af3).
        -   If no, go to  [2](#l2d27c4d5e737446092cd0a92a83470f6).

    4.  <a name="laadf0da13df34c51878b081c44194af3"></a>Modify the validity period configuration:
        -   Run the following command to set a validity period for user  **ommdba**:

            **chage -E** _'specified date'_ **ommdba**

        -   Run the following command to set the number of validity days for user  **ommdba**:

            **chage -M** _'number of days'_ **ommdba**

    5.  Check whether the alarm is cleared automatically in the next periodic check.
        -   If yes, no further action is required.
        -   If no, go to  [2](#l2d27c4d5e737446092cd0a92a83470f6).

2.  <a name="l2d27c4d5e737446092cd0a92a83470f6"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## **Related Information**<a name="s6c3fea4375344cafadd2fb52b8cf9113"></a>

N/A

