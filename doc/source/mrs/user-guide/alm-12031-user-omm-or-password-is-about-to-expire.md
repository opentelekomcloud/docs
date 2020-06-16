# ALM-12031 User omm or Password Is About to Expire<a name="EN-US_TOPIC_0125375486"></a>

## Description<a name="sb10118a656f64784a0d1a44686059b45"></a>

At 00:00 every day, the system starts checking whether user  **omm**  and its password are about to expire every 8 hours. This alarm is generated when the user or password is going to expire in 15 days.

It is cleared when the validity period of user  **omm**  is changed or the password is reset and the alarm handling is complete.

## Attribute<a name="sdce81727a7664ac4813304ef8e01e5a5"></a>

<a name="tb2c29de0d10047ff872c96a8c779806b"></a>
<table><thead align="left"><tr id="rf1b0fd075b754bd4bd91eaf77be2f136"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="a3015a68d91164c2a9fd3243e4657f533"><a name="a3015a68d91164c2a9fd3243e4657f533"></a><a name="a3015a68d91164c2a9fd3243e4657f533"></a><strong id="a3c17a4c42ef5421a8fa562b8658d5d86"><a name="a3c17a4c42ef5421a8fa562b8658d5d86"></a><a name="a3c17a4c42ef5421a8fa562b8658d5d86"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="a62eb584c7cb34df79e7fab28755a67ce"><a name="a62eb584c7cb34df79e7fab28755a67ce"></a><a name="a62eb584c7cb34df79e7fab28755a67ce"></a><strong id="abe6909e4c16c40cd8a55efda52748e21"><a name="abe6909e4c16c40cd8a55efda52748e21"></a><a name="abe6909e4c16c40cd8a55efda52748e21"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="a9b2e6b97430745acb1bafd011d9af6df"><a name="a9b2e6b97430745acb1bafd011d9af6df"></a><a name="a9b2e6b97430745acb1bafd011d9af6df"></a><strong id="a370539e5d00540a0ab076b1be40c779b"><a name="a370539e5d00540a0ab076b1be40c779b"></a><a name="a370539e5d00540a0ab076b1be40c779b"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="rdb21fcdb8dc04e118d7da16fc3e5931e"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="a0a78b859d1c443cf9d39df9cedeb4ab9"><a name="a0a78b859d1c443cf9d39df9cedeb4ab9"></a><a name="a0a78b859d1c443cf9d39df9cedeb4ab9"></a>12031</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="a487e7b632533402894cffafe7f5eaae0"><a name="a487e7b632533402894cffafe7f5eaae0"></a><a name="a487e7b632533402894cffafe7f5eaae0"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="a9b7c38670685421085de91b29464c962"><a name="a9b7c38670685421085de91b29464c962"></a><a name="a9b7c38670685421085de91b29464c962"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="se1b0fa1611d04a00b6deb4ab6c1e9395"></a>

<a name="t99f1952817c74400941254113513d900"></a>
<table><thead align="left"><tr id="raa8929479dfd445b94485fd69b27c241"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="a251600c1c3b0463f890c303b272a5daf"><a name="a251600c1c3b0463f890c303b272a5daf"></a><a name="a251600c1c3b0463f890c303b272a5daf"></a><strong id="adb4324b047a746498b884bb83fbd370b"><a name="adb4324b047a746498b884bb83fbd370b"></a><a name="adb4324b047a746498b884bb83fbd370b"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="a539b8717ca4b4245a147b5c03a76b92f"><a name="a539b8717ca4b4245a147b5c03a76b92f"></a><a name="a539b8717ca4b4245a147b5c03a76b92f"></a><strong id="a23454b53b13043f68c55944c6b82aa38"><a name="a23454b53b13043f68c55944c6b82aa38"></a><a name="a23454b53b13043f68c55944c6b82aa38"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="rc492a20d3b7545f7828b7970aaefc78b"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a125a2fa6c4994536905d8a7d969501c4"><a name="a125a2fa6c4994536905d8a7d969501c4"></a><a name="a125a2fa6c4994536905d8a7d969501c4"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a53f7a1fc90114a6781ace1419d37b6a9"><a name="a53f7a1fc90114a6781ace1419d37b6a9"></a><a name="a53f7a1fc90114a6781ace1419d37b6a9"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="r3ba351076d684c75aa7bf5536a63fa8c"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ac44e6bfe41634c54939e25e42b8c8a24"><a name="ac44e6bfe41634c54939e25e42b8c8a24"></a><a name="ac44e6bfe41634c54939e25e42b8c8a24"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="aed41c98b179a4e29b85f83e61fcc0403"><a name="aed41c98b179a4e29b85f83e61fcc0403"></a><a name="aed41c98b179a4e29b85f83e61fcc0403"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="r4e89975cda1146b7a57c602be1e44238"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="aba620c5e65664d0f80b36fe2fb69e9e8"><a name="aba620c5e65664d0f80b36fe2fb69e9e8"></a><a name="aba620c5e65664d0f80b36fe2fb69e9e8"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a6f2c362fc2ad4ef191daa3a530121e1f"><a name="a6f2c362fc2ad4ef191daa3a530121e1f"></a><a name="a6f2c362fc2ad4ef191daa3a530121e1f"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s8918f1f8bf574311ae8132b45039a220"></a>

The node trust relationship is unavailable and Manager cannot manage services.

## Possible Causes<a name="sc8f4236124d649648c4b11dd2385e8b3"></a>

User  **omm**  or its password is about to expire.

## Procedure<a name="s86db88878b63441489a3179bc9aa2965"></a>

1.  Check whether user  **omm**  and its password in the system are valid.
    1.  Log in to the faulty node.
    2.  Run the following command to view information about user  **omm**  and its password:

        **chage -l omm**

    3.  Check whether the user and password are about to expire based on the system message.

        1.  View the value of  **Password expires**  to check whether the password is about to expire.
        2.  View the value of  **Account expires**  to check whether the user is about to expire.

        >![](/images/icon-note.gif) **NOTE:**   
        >If the parameter value is  **never**, the user and password are valid permanently; if the value is a date, check whether the user and password are going to expire within 15 days.  

        -   If yes, go to  [1.d](#l6e84fdccc7554be6ae52969a1456ffa2).
        -   If no, go to  [2](#lbb55e71d00914579bab0ea8b3901eab5).

    4.  <a name="l6e84fdccc7554be6ae52969a1456ffa2"></a>Modify the validity period:
        -   Run the following command to set a validity period for user  **omm**:

            chage -E  _'specified date'_ **omm**

        -   Run the following command to set the number of validity days for user  **omm**:

            **chage -M** _'number of days'_ **omm**

    5.  Check whether the alarm is cleared automatically in the next periodic check.
        -   If yes, no further action is required.
        -   If no, go to  [2](#lbb55e71d00914579bab0ea8b3901eab5).

2.  <a name="lbb55e71d00914579bab0ea8b3901eab5"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## **Related Information**<a name="sc138a89975e8456fbffecfe630804bd2"></a>

N/A

