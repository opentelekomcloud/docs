# ALM-25500 KrbServer Service Unavailable<a name="EN-US_TOPIC_0125376027"></a>

## Description<a name="s3137aa4243a8414c9cf0a7c7627c687f"></a>

The system checks the KrbServer service status every 30 seconds. This alarm is generated when the KrbServer service is abnormal and is cleared when the KrbServer service is in the normal state.

## Attribute<a name="scb545d65ff4b48e29069174ab9b5c9ed"></a>

<a name="en-us_topic_0035998744_table4400500"></a>
<table><thead align="left"><tr id="en-us_topic_0035998744_row63695501"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="en-us_topic_0035998744_p59061958"><a name="en-us_topic_0035998744_p59061958"></a><a name="en-us_topic_0035998744_p59061958"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="en-us_topic_0035998744_p19289328"><a name="en-us_topic_0035998744_p19289328"></a><a name="en-us_topic_0035998744_p19289328"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="en-us_topic_0035998744_p18931763"><a name="en-us_topic_0035998744_p18931763"></a><a name="en-us_topic_0035998744_p18931763"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998744_row57077814"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0035998744_p59900193"><a name="en-us_topic_0035998744_p59900193"></a><a name="en-us_topic_0035998744_p59900193"></a>25500</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0035998744_p20077469"><a name="en-us_topic_0035998744_p20077469"></a><a name="en-us_topic_0035998744_p20077469"></a>Critical</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0035998744_p15662289"><a name="en-us_topic_0035998744_p15662289"></a><a name="en-us_topic_0035998744_p15662289"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="scf0fecd9de3a4809bcab4ab7913232ea"></a>

<a name="en-us_topic_0035998744_table60685926"></a>
<table><thead align="left"><tr id="en-us_topic_0035998744_row31278690"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0035998744_p50545980"><a name="en-us_topic_0035998744_p50545980"></a><a name="en-us_topic_0035998744_p50545980"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0035998744_p583706"><a name="en-us_topic_0035998744_p583706"></a><a name="en-us_topic_0035998744_p583706"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998744_row47280229"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998744_p4493316"><a name="en-us_topic_0035998744_p4493316"></a><a name="en-us_topic_0035998744_p4493316"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998744_p28414304"><a name="en-us_topic_0035998744_p28414304"></a><a name="en-us_topic_0035998744_p28414304"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998744_row54402144"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998744_p44497505"><a name="en-us_topic_0035998744_p44497505"></a><a name="en-us_topic_0035998744_p44497505"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998744_p47528147"><a name="en-us_topic_0035998744_p47528147"></a><a name="en-us_topic_0035998744_p47528147"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998744_row25100141"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998744_p19845579"><a name="en-us_topic_0035998744_p19845579"></a><a name="en-us_topic_0035998744_p19845579"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998744_p63988077"><a name="en-us_topic_0035998744_p63988077"></a><a name="en-us_topic_0035998744_p63988077"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s6c666576994a432082e3f0b47d1b44a9"></a>

-   No operation can be performed for the KrbServer component in the cluster.
-   KrbServer authentication of other components will be affected.
-   The health status of components that depend on KrbServer in the cluster is  **Bad**.

## Possible Causes<a name="se67ea8806c0f4ff188213a1bcc855cbf"></a>

-   The node where the KrbServer service resides is faulty.
-   The OLdap service is unavailable.

## Procedure<a name="sb4f276e6425f498a93e293ce3dd03689"></a>

1.  Check whether the node where the KrbServer service locates is faulty.
    1.  <a name="l9ac9d7d0e43f4995aedfbaefd6648c98"></a>On MRS Manager, choose  **Service**  \>  **KrbServer**  \>  **Instance**  to go to the KrbServer instance page. Obtain the host name of the node where the KrbServer service resides.
    2.  On the  **Alarm**  page of MRS Manager, check whether alarm  **ALM-12006 Node Fault**  is generated.
        -   If yes, go to  [1.c](#l8a718180ff494194b7c9034c414cb644).
        -   If no, go to  [2.a](#l699a821d999f46ddaf5a2a182d64d8b0).

    3.  <a name="l8a718180ff494194b7c9034c414cb644"></a>Check whether the host name in the alarm is consistent with the host name in  [1.a](#l9ac9d7d0e43f4995aedfbaefd6648c98).
        -   If yes, go to  [1.d](#l7d3eb1a206924aa8bdc98d35f198241e).
        -   If no, go to  [2.a](#l699a821d999f46ddaf5a2a182d64d8b0).

    4.  <a name="l7d3eb1a206924aa8bdc98d35f198241e"></a>Rectify the fault by following the steps provided in  **ALM-12006 Node Fault**.
    5.  In the alarm list, check whether alarm  **ALM-25500 KrbServer Service Unavailable**  is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [3](#l17086263f2f14c90be69c88d687d2ff9).

2.  Check whether the OLdap service is unavailable.
    1.  <a name="l699a821d999f46ddaf5a2a182d64d8b0"></a>On the  **Alarm**  page of MRS Manager, check whether alarm  **ALM-12004 OLdap Resource Is Abnormal**  is generated.
        -   If yes, go to  [2.b](#le5e65bf4f10447e9b0a72a20574a24d1).
        -   If no, go to  [3](#l17086263f2f14c90be69c88d687d2ff9).

    2.  <a name="le5e65bf4f10447e9b0a72a20574a24d1"></a>Rectify the fault by following the steps provided in  **ALM-12004 OLdap Resource Is Abnormal**.
    3.  In the alarm list, check whether alarm  **ALM-25500 KrbServer Service Unavailable**  is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [3](#l17086263f2f14c90be69c88d687d2ff9).

3.  <a name="l17086263f2f14c90be69c88d687d2ff9"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="s62e171bf48174535927088b84f0f8883"></a>

N/A

