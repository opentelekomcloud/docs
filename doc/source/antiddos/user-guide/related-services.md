# Related Services<a name="EN-US_TOPIC_0204851508"></a>

## CTS<a name="s4ed2944294c94b9685dd0ad9acd2c361"></a>

Cloud Trace Service \(CTS\) provides you with a history of Anti-DDoS operations. After enabling CTS, you can view all generated traces to review and audit performed Anti-DDoS operations. For details, see the  _Cloud Trace Service User Guide_.

-   Anti-DDoS operations that can be recorded by CTS

    **Table  1**  Anti-DDoS operations that can be recorded by CTS

    <a name="t8517317c2d5f4e93a9d56077b4dec2aa"></a>
    <table><thead align="left"><tr id="r71578f6d75db4ac0a267f3c568120a52"><th class="cellrowborder" valign="top" width="55.85%" id="mcps1.2.3.1.1"><p id="afadd5afcfbee4372afd773bc8cbf6116"><a name="afadd5afcfbee4372afd773bc8cbf6116"></a><a name="afadd5afcfbee4372afd773bc8cbf6116"></a>Operation</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.15%" id="mcps1.2.3.1.2"><p id="a602681b4740847c4894d9382fbd51ac6"><a name="a602681b4740847c4894d9382fbd51ac6"></a><a name="a602681b4740847c4894d9382fbd51ac6"></a>Trace Name</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r0f66a4ec148e4fb3b0c081ced721672c"><td class="cellrowborder" valign="top" width="55.85%" headers="mcps1.2.3.1.1 "><p id="p3689577916038"><a name="p3689577916038"></a><a name="p3689577916038"></a>Enabling Anti-DDoS</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.15%" headers="mcps1.2.3.1.2 "><p id="p23847134191911"><a name="p23847134191911"></a><a name="p23847134191911"></a>openAntiddos</p>
    </td>
    </tr>
    <tr id="r460f7b2568c249d99d7d57dbb59f1ba9"><td class="cellrowborder" valign="top" width="55.85%" headers="mcps1.2.3.1.1 "><p id="p858403916038"><a name="p858403916038"></a><a name="p858403916038"></a>Disabling Anti-DDoS</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.15%" headers="mcps1.2.3.1.2 "><p id="p28400374191931"><a name="p28400374191931"></a><a name="p28400374191931"></a>deleteAntiddos</p>
    </td>
    </tr>
    <tr id="r3e7c2fe75a1c4d579504534f6ac8e8db"><td class="cellrowborder" valign="top" width="55.85%" headers="mcps1.2.3.1.1 "><p id="p1436225216038"><a name="p1436225216038"></a><a name="p1436225216038"></a>Adjusting Anti-DDoS security settings</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.15%" headers="mcps1.2.3.1.2 "><p id="p65888903191945"><a name="p65888903191945"></a><a name="p65888903191945"></a>updateAntiddos</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Using CTS to view Anti-DDoS audit logs
    1.  Log in to the management console.
    2.  Click  ![](figures/icon_dt.png)  in the upper left corner to select a region or project.
    3.  Select  **Cloud Trace Service**  under  **Management & Deployment**.
    4.  In the left navigation pane, choose  **Trace List**.
    5.  You can use filters to query traces. The following four filters are available:
        -   **Trace Source**,  **Resource Type**, and  **Search By**
            -   Select query conditions from the drop-down list, for example, choose  **Anti-DDoS**  \>  **anti-ddos**  \>  **Trace name**  \>  **openAntiddos**  to query all Anti-DDoS enabling operations.
            -   **Trace name**: This option allows you to select a trace name, such as  **openAntiddos**.
            -   **Resource ID**: This option allows you to select or manually enter the ID of the instance for which you want to view audit logs.
            -   **Resource name**: This option allows you to select or manually enter the name of the instance for which you want to view audit logs.

        -   **Operator**: Select a specific operator \(at user level rather than tenant level\).
        -   **Trace Status**: Available options include  **All trace statuses**,  **normal**,  **warning**, and  **incident**. You can only select one of them.
        -   Start time and end time: You can specify the time period to query traces.

    6.  Click  ![](figures/chakanshilijiantou.png)  on the left of the record to be queried to extend its details.
    7.  In the row containing the desired record, click  **View Trace**.


## IAM<a name="section16851842101240"></a>

Identity and Access Management \(IAM\) provides the permission management function for Anti-DDoS. Only users who have Anti-DDoS Administrator permissions can use Anti-DDoS. To apply for Anti-DDoS Administrator permissions, contact a user with Security Administrator permissions. For details, see the  _Identity and Access Management User Guide_.

## SMN<a name="section329492519538"></a>

The Simple Message Notification \(SMN\) service provides the notification function. When alarm notification is enabled in Anti-DDoS, you will receive alarm messages by SMS or email if your IP address is under a DDoS attack.

For details about SMN, see the  _Simple Message Notification User Guide_.

