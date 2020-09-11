# ALM-25000 LdapServer Service Unavailable<a name="EN-US_TOPIC_0125375559"></a>

## Description<a name="s715f82c60bab44cdbf3ef23e26501df9"></a>

The system checks the LdapServer service status every 30 seconds. This alarm is generated when the system detects that both the active and standby LdapServer services are abnormal. It is cleared when one or both LdapServer services are normal.

## Attribute<a name="s110b2ddaa134409aa22f6fd6cf6924a8"></a>

<a name="en-us_topic_0035998742_table66898905"></a>
<table><thead align="left"><tr id="en-us_topic_0035998742_row21436848"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="en-us_topic_0035998742_p58663159"><a name="en-us_topic_0035998742_p58663159"></a><a name="en-us_topic_0035998742_p58663159"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="en-us_topic_0035998742_p54095401"><a name="en-us_topic_0035998742_p54095401"></a><a name="en-us_topic_0035998742_p54095401"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="en-us_topic_0035998742_p19651376"><a name="en-us_topic_0035998742_p19651376"></a><a name="en-us_topic_0035998742_p19651376"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998742_row48257652"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0035998742_p16555740"><a name="en-us_topic_0035998742_p16555740"></a><a name="en-us_topic_0035998742_p16555740"></a>25000</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0035998742_p65946577"><a name="en-us_topic_0035998742_p65946577"></a><a name="en-us_topic_0035998742_p65946577"></a>Critical</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0035998742_p40072506"><a name="en-us_topic_0035998742_p40072506"></a><a name="en-us_topic_0035998742_p40072506"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s2dcf13c31ac6401b99ac679b082a7735"></a>

<a name="en-us_topic_0035998742_table24647552"></a>
<table><thead align="left"><tr id="en-us_topic_0035998742_row23371976"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0035998742_p14081900"><a name="en-us_topic_0035998742_p14081900"></a><a name="en-us_topic_0035998742_p14081900"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0035998742_p66892145"><a name="en-us_topic_0035998742_p66892145"></a><a name="en-us_topic_0035998742_p66892145"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998742_row49554687"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998742_p54506685"><a name="en-us_topic_0035998742_p54506685"></a><a name="en-us_topic_0035998742_p54506685"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998742_p52965331"><a name="en-us_topic_0035998742_p52965331"></a><a name="en-us_topic_0035998742_p52965331"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998742_row6925935"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998742_p24129853"><a name="en-us_topic_0035998742_p24129853"></a><a name="en-us_topic_0035998742_p24129853"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998742_p8361080"><a name="en-us_topic_0035998742_p8361080"></a><a name="en-us_topic_0035998742_p8361080"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998742_row8140857"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998742_p55429698"><a name="en-us_topic_0035998742_p55429698"></a><a name="en-us_topic_0035998742_p55429698"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998742_p60620523"><a name="en-us_topic_0035998742_p60620523"></a><a name="en-us_topic_0035998742_p60620523"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="saf7e3637535c41ea9caad3170ff484a5"></a>

No operation can be performed for the KrbServer and LdapServer users in the cluster. For example, users, user groups, or roles cannot be added, deleted, or modified, and user passwords cannot be changed on MRS Manager. Authentication for existing users in the cluster is not affected.

## Possible Causes<a name="sfb68a725149a4b7785f4d3a28cc599bb"></a>

-   The node where the LdapServer service resides is faulty.
-   The LdapServer process is abnormal.

## Procedure<a name="sf925801d02af4444a1d269e5dabffd54"></a>

1.  Check whether the nodes where the two SlapdServer instances of the LdapServer service reside are faulty.
    1.  <a name="l9d425276eb41468cbe458576745626d5"></a>On MRS Manager, choose  **Service**  \>  **LdapServer**  \>  **Instance**  to go to the LdapServer instance page. Obtain the host name of the node where the two SlapdServer instances reside.
    2.  On the  **Alarm**  page of MRS Manager, check whether alarm  **ALM-12006 Node Fault**  is generated.
        -   If yes, go to  [1.c](#l30fd91548d364c968c3a286bd2c8f34a).
        -   If no, go to  [2.a](#l0b5ddb621891417d8fa2699748304a72).

    3.  <a name="l30fd91548d364c968c3a286bd2c8f34a"></a>Check whether the host name in the alarm is consistent with the host name in  [1.a](#l9d425276eb41468cbe458576745626d5).
        -   If yes, go to  [1.d](#l53c556c8918d4b2abb7a967cfbfe22df).
        -   If no, go to  [2.a](#l0b5ddb621891417d8fa2699748304a72).

    4.  <a name="l53c556c8918d4b2abb7a967cfbfe22df"></a>Rectify the fault by following the steps provided in  **ALM-12006 Node Fault**.
    5.  In the alarm list, check whether alarm  **ALM-25000 LdapServer Service Unavailable**  is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [3](#ldd846a382dca450a8fac7c3c7e0ed61e).

2.  Check whether the LdapServer process is in the normal state.
    1.  <a name="l0b5ddb621891417d8fa2699748304a72"></a>On the  **Alarm**  page of MRS Manager, check whether alarm  **ALM-12007 Process Fault**  is generated.
        -   If yes, go to  [2.b](#l296318b8150d44deb9e2b5a3167dea0c).
        -   If no, go to  [3](#ldd846a382dca450a8fac7c3c7e0ed61e).

    2.  <a name="l296318b8150d44deb9e2b5a3167dea0c"></a>Check whether the service name and host name in the alarm are consistent with those of LdapServer.
        -   If yes, go to  [2.c](#en-us_topic_0035998742_alarm53004).
        -   If no, go to  [3](#ldd846a382dca450a8fac7c3c7e0ed61e).

    3.  <a name="en-us_topic_0035998742_alarm53004"></a>Rectify the fault by following the steps provided in  **ALM-12007 Process Fault**.
    4.  In the alarm list, check whether alarm  **ALM-25000 LdapServer Service Unavailable**  is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [3](#ldd846a382dca450a8fac7c3c7e0ed61e).

3.  <a name="ldd846a382dca450a8fac7c3c7e0ed61e"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="se5ee1afd26b8423691d5c39e85f3e6ee"></a>

N/A

