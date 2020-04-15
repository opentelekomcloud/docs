# Login Using VNC<a name="EN-US_TOPIC_0093263550"></a>

## Scenarios<a name="section1657615471270"></a>

This section describes how to use VNC provided on the management console to log in to an ECS. This function applies to emergency O&M. In other scenarios, you are advised to log in to ECSs using SSH or MSTSC.

For instructions about how to copy and paste data on VNC pages after the ECS login, see  [Follow-up Procedure](#section322133015286).

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>Before using remote login \(VNC\) provided on the management console to log in to a Linux ECS authenticated using a key pair, log in to the ECS  [using an SSH key](login-using-an-ssh-key.md)  and set a login password.  

## Constraints<a name="en-us_topic_0027268511_section19897287191525"></a>

-   The remote login function is implemented using customized ports. Therefore, before attempting to log in remotely, ensure that the port to be used is not blocked by the firewall. For example, if the remote login link is xxx:8002, ensure that port 8002 is not blocked by the firewall.
-   If the client OS uses a local proxy and the firewall port cannot be configured on the local proxy, disable the proxy mode and then try logging in remotely.

## Login Notes<a name="en-us_topic_0027268511_section3272280121431"></a>

1.  When you log in to the ECS using VNC, four types of keyboards will be used, as described in  [Table 1](#en-us_topic_0027268511_en-us_topic_0039525621_table10692372181721).

    **Table  1**  Keyboard types

    <a name="en-us_topic_0027268511_en-us_topic_0039525621_table10692372181721"></a>
    <table><thead align="left"><tr id="en-us_topic_0027268511_en-us_topic_0039525621_row53137814181721"><th class="cellrowborder" valign="top" width="21.62%" id="mcps1.2.4.1.1"><p id="en-us_topic_0027268511_en-us_topic_0039525621_p30908407181721"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p30908407181721"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p30908407181721"></a>Keyboard Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="43.79%" id="mcps1.2.4.1.2"><p id="en-us_topic_0027268511_en-us_topic_0039525621_p37714767181721"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p37714767181721"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p37714767181721"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="34.589999999999996%" id="mcps1.2.4.1.3"><p id="en-us_topic_0027268511_en-us_topic_0039525621_p757482181721"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p757482181721"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p757482181721"></a>Keyboard Language</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0027268511_en-us_topic_0039525621_row42556453181721"><td class="cellrowborder" valign="top" width="21.62%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p38862229181721"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p38862229181721"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p38862229181721"></a>Physical keyboard</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.79%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p42383623181721"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p42383623181721"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p42383623181721"></a>Used by the terminal and allows terminal data input.</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.589999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p51975930181721"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p51975930181721"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p51975930181721"></a>Selected by users locally.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0027268511_en-us_topic_0039525621_row18005491181721"><td class="cellrowborder" valign="top" width="21.62%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p12192092181721"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p12192092181721"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p12192092181721"></a>Input method keyboard on the terminal</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.79%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p56742150181721"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p56742150181721"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p56742150181721"></a>Used for logging in to the management console from a terminal, such as a computer. The keyboard input method of the terminal must comply with the physical keyboard language type. In this way, the entered data can be correctly transferred from the physical keyboard to the VNC client.</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.589999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p52047219181721"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p52047219181721"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p52047219181721"></a>Selected by users locally.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0027268511_en-us_topic_0039525621_row29768537181721"><td class="cellrowborder" valign="top" width="21.62%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p4356315181721"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p4356315181721"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p4356315181721"></a>VNC keyboard</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.79%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p46406878181721"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p46406878181721"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p46406878181721"></a>Used for VNC logins. The VNC keyboard input method must comply with the physical keyboard language type. In this way, the entered data can be correctly transferred from the VNC client to the ECS OS.</p>
    <div class="note" id="en-us_topic_0027268511_en-us_topic_0039525621_note1570793894248"><a name="en-us_topic_0027268511_en-us_topic_0039525621_note1570793894248"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_note1570793894248"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0027268511_en-us_topic_0039525621_p4859993494248"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p4859993494248"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p4859993494248"></a>The English keyboard is used by default. The system also supports other keyboard languages.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="34.589999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p70096579373"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p70096579373"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p70096579373"></a>Can be configured through the management console.</p>
    <p id="en-us_topic_0027268511_en-us_topic_0039525621_p4116452181721"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p4116452181721"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p4116452181721"></a>For instructions about how to select a VNC keyboard language, see <a href="#en-us_topic_0027268511_section46750509111459">Logging In to an ECS Using an English Keyboard</a> and <a href="#en-us_topic_0027268511_section5982347111459">Logging In to an ECS Using a Non-English Keyboard</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0027268511_en-us_topic_0039525621_row25012200181721"><td class="cellrowborder" valign="top" width="21.62%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p59196322181721"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p59196322181721"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p59196322181721"></a>ECS OS keyboard</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.79%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p6445544610506"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p6445544610506"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p6445544610506"></a>Input method keyboard configured in the ECS OS. Ensure that this input method complies with the physical keyboard language type for correct response to the entered data transferred from the VNC client.</p>
    <div class="note" id="en-us_topic_0027268511_en-us_topic_0039525621_note17013726105332"><a name="en-us_topic_0027268511_en-us_topic_0039525621_note17013726105332"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_note17013726105332"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="en-us_topic_0027268511_en-us_topic_0039525621_ul4327783510508"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_ul4327783510508"></a><ul id="en-us_topic_0027268511_en-us_topic_0039525621_ul4327783510508"><li>The default OS keyboard language of an ECS created using a public image is English. For additional information, see <em id="i45659338194"><a name="i45659338194"></a><a name="i45659338194"></a><a href="https://docs.otc.t-systems.com/en-us/ims/index.html" target="_blank" rel="noopener noreferrer">Public Images Introduction</a></em>.</li><li>The OS keyboard language of an ECS created using a private image is customized.</li></ul>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="34.589999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p49626590181721"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p49626590181721"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p49626590181721"></a>Configured by users locally.</p>
    <p id="en-us_topic_0027268511_en-us_topic_0039525621_p20720990181721"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p20720990181721"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p20720990181721"></a>For instructions about how to change an ECS OS keyboard language, see <a href="#en-us_topic_0027268511_section66962382111459">Changing the OS Keyboard Language</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

2.  When you log in to the ECS using VNC, ensure that your configured keyboard language is correct.

    The entered data is as expected only if the input method keyboard on the terminal, the VNC keyboard, and the ECS OS keyboard languages are the same as the physical keyboard language. For details about language configuration in the four types of keyboards, see  [Table 2](#en-us_topic_0027268511_en-us_topic_0039525621_table31240733181814).

    **Table  2**  Language configuration in the four types of keyboards

    <a name="en-us_topic_0027268511_en-us_topic_0039525621_table31240733181814"></a>
    <table><thead align="left"><tr id="en-us_topic_0027268511_en-us_topic_0039525621_row7187309181814"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.1"><p id="en-us_topic_0027268511_en-us_topic_0039525621_p55421616181814"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p55421616181814"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p55421616181814"></a>Physical Keyboard</p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.2"><p id="en-us_topic_0027268511_en-us_topic_0039525621_p23271888181814"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p23271888181814"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p23271888181814"></a>Input Method Keyboard on the Terminal</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.05%" id="mcps1.2.6.1.3"><p id="en-us_topic_0027268511_en-us_topic_0039525621_p43044593181814"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p43044593181814"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p43044593181814"></a>VNC Keyboard</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.95%" id="mcps1.2.6.1.4"><p id="en-us_topic_0027268511_en-us_topic_0039525621_p33575573181814"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p33575573181814"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p33575573181814"></a>ECS OS Keyboard</p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.5"><p id="en-us_topic_0027268511_en-us_topic_0039525621_p56577338181814"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p56577338181814"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p56577338181814"></a>Supported or Not</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0027268511_en-us_topic_0039525621_row61810526182231"><td class="cellrowborder" rowspan="8" valign="top" width="20%" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p26481438182231"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p26481438182231"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p26481438182231"></a>English</p>
    </td>
    <td class="cellrowborder" rowspan="4" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p48583343182231"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p48583343182231"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p48583343182231"></a>English</p>
    </td>
    <td class="cellrowborder" rowspan="2" valign="top" width="16.05%" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p25476291182231"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p25476291182231"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p25476291182231"></a>English</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.95%" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p27720152182231"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p27720152182231"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p27720152182231"></a>English</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p55366256182231"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p55366256182231"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p55366256182231"></a>Yes</p>
    </td>
    </tr>
    <tr id="en-us_topic_0027268511_en-us_topic_0039525621_row55112854181814"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p8676484181814"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p8676484181814"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p8676484181814"></a>German</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p53450661181814"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p53450661181814"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p53450661181814"></a>No</p>
    </td>
    </tr>
    <tr id="en-us_topic_0027268511_en-us_topic_0039525621_row19041350181814"><td class="cellrowborder" rowspan="2" valign="top" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p35663203181814"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p35663203181814"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p35663203181814"></a>German</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p22664992181814"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p22664992181814"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p22664992181814"></a>English</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p53223387181814"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p53223387181814"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p53223387181814"></a>No</p>
    </td>
    </tr>
    <tr id="en-us_topic_0027268511_en-us_topic_0039525621_row11541330181814"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p48305560181814"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p48305560181814"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p48305560181814"></a>German</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p58514702181814"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p58514702181814"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p58514702181814"></a>No</p>
    </td>
    </tr>
    <tr id="en-us_topic_0027268511_en-us_topic_0039525621_row26308419182924"><td class="cellrowborder" rowspan="4" valign="top" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p15985449182924"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p15985449182924"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p15985449182924"></a>German</p>
    </td>
    <td class="cellrowborder" rowspan="2" valign="top" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p55258849182942"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p55258849182942"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p55258849182942"></a>English</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p16417465183032"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p16417465183032"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p16417465183032"></a>English</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p28085585183043"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p28085585183043"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p28085585183043"></a>No</p>
    </td>
    </tr>
    <tr id="en-us_topic_0027268511_en-us_topic_0039525621_row45219031182924"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p40442689183032"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p40442689183032"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p40442689183032"></a>German</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p61478188183043"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p61478188183043"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p61478188183043"></a>No</p>
    </td>
    </tr>
    <tr id="en-us_topic_0027268511_en-us_topic_0039525621_row4466119182924"><td class="cellrowborder" rowspan="2" valign="top" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p65516692182945"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p65516692182945"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p65516692182945"></a>German</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p12275038183032"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p12275038183032"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p12275038183032"></a>English</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p50765805183043"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p50765805183043"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p50765805183043"></a>No</p>
    </td>
    </tr>
    <tr id="en-us_topic_0027268511_en-us_topic_0039525621_row27668196182924"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p21489343183032"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p21489343183032"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p21489343183032"></a>German</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p33405417183049"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p33405417183049"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p33405417183049"></a>No</p>
    </td>
    </tr>
    <tr id="en-us_topic_0027268511_en-us_topic_0039525621_row1648328818311"><td class="cellrowborder" rowspan="8" valign="top" width="20%" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p4886474918318"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p4886474918318"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p4886474918318"></a>German</p>
    </td>
    <td class="cellrowborder" rowspan="4" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p6349176418318"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p6349176418318"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p6349176418318"></a>English</p>
    </td>
    <td class="cellrowborder" rowspan="2" valign="top" width="16.05%" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p2040204618318"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p2040204618318"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p2040204618318"></a>English</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.95%" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p479456918318"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p479456918318"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p479456918318"></a>English</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p5390415118318"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p5390415118318"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p5390415118318"></a>No</p>
    </td>
    </tr>
    <tr id="en-us_topic_0027268511_en-us_topic_0039525621_row5764100418311"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p5613255118318"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p5613255118318"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p5613255118318"></a>German</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p5928237818318"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p5928237818318"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p5928237818318"></a>No</p>
    </td>
    </tr>
    <tr id="en-us_topic_0027268511_en-us_topic_0039525621_row1303258718311"><td class="cellrowborder" rowspan="2" valign="top" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p5993276918318"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p5993276918318"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p5993276918318"></a>German</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p3697029718318"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p3697029718318"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p3697029718318"></a>English</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p6244405018318"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p6244405018318"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p6244405018318"></a>No</p>
    </td>
    </tr>
    <tr id="en-us_topic_0027268511_en-us_topic_0039525621_row5117229618311"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p6565458018318"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p6565458018318"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p6565458018318"></a>German</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p2689824318318"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p2689824318318"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p2689824318318"></a>No</p>
    </td>
    </tr>
    <tr id="en-us_topic_0027268511_en-us_topic_0039525621_row1581944118311"><td class="cellrowborder" rowspan="4" valign="top" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p609063618318"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p609063618318"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p609063618318"></a>German</p>
    </td>
    <td class="cellrowborder" rowspan="2" valign="top" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p5603480018318"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p5603480018318"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p5603480018318"></a>English</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p1994018118318"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p1994018118318"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p1994018118318"></a>English</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p3869497318318"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p3869497318318"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p3869497318318"></a>No</p>
    </td>
    </tr>
    <tr id="en-us_topic_0027268511_en-us_topic_0039525621_row801999018311"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p1848781218318"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p1848781218318"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p1848781218318"></a>German</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p56854418318"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p56854418318"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p56854418318"></a>No</p>
    </td>
    </tr>
    <tr id="en-us_topic_0027268511_en-us_topic_0039525621_row6689709618311"><td class="cellrowborder" rowspan="2" valign="top" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p3070590318318"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p3070590318318"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p3070590318318"></a>German</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p1851465718318"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p1851465718318"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p1851465718318"></a>English</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p2980232418318"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p2980232418318"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p2980232418318"></a>No</p>
    </td>
    </tr>
    <tr id="en-us_topic_0027268511_en-us_topic_0039525621_row3970959018311"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p1577780518318"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p1577780518318"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p1577780518318"></a>German</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p216114218318"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p216114218318"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p216114218318"></a>Yes</p>
    </td>
    </tr>
    </tbody>
    </table>

3.  If the password used when you create the ECS is entered using the English keyboard, you must use the English keyboard to enter the password when logging in to the ECS later.

## Logging In to an ECS Using an English Keyboard<a name="en-us_topic_0027268511_section46750509111459"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  Under  **Computing**, click  **Elastic Cloud Server**.
4.  In the search box above the upper right corner of the ECS list, enter the ECS name and click  ![](figures/icon-search.png)  for search.
5.  Locate the row containing the ECS and click  **Remote Login**  in the  **Operation**  column.
6.  <a name="en-us_topic_0027268511_li17715715111459"></a>In the displayed  **Configure Keyboard Layout for Remote Login**  dialog box, select the English keyboard.

    **Figure  1**  Keyboard layout configuration<a name="en-us_topic_0027268511_fig25223713111459"></a>  
    ![](figures/keyboard-layout-configuration.png "keyboard-layout-configuration")

7.  Click  **Remote Login**.
8.  \(Optional\) If you have changed the system language, in the dialog box that is displayed \(as shown in  [Figure 2](#en-us_topic_0027268511_fig54376817111459)\), click  **Start Remote Login**.

    **Figure  2**  Remote Login<a name="en-us_topic_0027268511_fig54376817111459"></a>  
    ![](figures/remote-login.png "remote-login")

9.  \(Optional\) When the system displays "Press CTRL+ALT+DELETE to log on", click  **Send CtrlAltDel**  in the upper part of the remote login page to log in to the ECS.

    **Figure  3**  Send CtrlAltDel<a name="fig51941916112020"></a>  
    ![](figures/send-ctrlaltdel.png "send-ctrlaltdel")

10. \(Optional\) Have the cursor displayed in the remote login panel. Perform this step if the cursor is not displayed after you remotely log in to a G1 ECS. To do so, click  **Local Cursor**  in the upper part of the remote login panel.

    **Figure  4**  Local Cursor<a name="en-us_topic_0027268511_fig3022163194924"></a>  
    ![](figures/local-cursor.png "local-cursor")

11. Enter the ECS password as prompted.

## Logging In to an ECS Using a Non-English Keyboard<a name="en-us_topic_0027268511_section5982347111459"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  Under  **Computing**, click  **Elastic Cloud Server**.
4.  In the search box above the upper right corner of the ECS list, enter the ECS name, IP address, or ID, and click  ![](figures/icon-search.png)  for search.
5.  Locate the row containing the ECS and click  **Remote Login**  in the  **Operation**  column.
6.  In the displayed  **Configure Keyboard Layout for Remote Login**  dialog box, select the English keyboard.

    **Figure  5**  Keyboard layout configuration<a name="en-us_topic_0093263550_en-us_topic_0027268511_fig25223713111459"></a>  
    ![](figures/keyboard-layout-configuration.png "keyboard-layout-configuration")


1.  Click  **Remote Login**.
2.  \(Optional\) If you have changed the system language, in the dialog box that is displayed \(as shown in  [Figure 6](#en-us_topic_0093263550_en-us_topic_0027268511_fig54376817111459)\), click  **Start Remote Login**.

    **Figure  6**  Remote Login<a name="en-us_topic_0093263550_en-us_topic_0027268511_fig54376817111459"></a>  
    ![](figures/remote-login.png "remote-login")

3.  \(Optional\) When the system displays "Press CTRL+ALT+DELETE to log on", click  **Send CtrlAltDel**  in the upper part of the remote login page to log in to the ECS.

    **Figure  7**  Send CtrlAltDel<a name="en-us_topic_0027290684_fig22996848191913"></a>  
    ![](figures/send-ctrlaltdel.png "send-ctrlaltdel")

4.  \(Optional\) Have the cursor displayed in the remote login panel. Perform this step if the cursor is not displayed after you remotely log in to a G1 ECS. To do so, click  **Local Cursor**  in the upper part of the remote login panel.

    **Figure  8**  Local Cursor<a name="en-us_topic_0093263550_en-us_topic_0027268511_fig3022163194924"></a>  
    ![](figures/local-cursor.png "local-cursor")

5.  Enter the ECS password as prompted.
    -   When logging in to the ECS using VNC for the first time, use the English keyboard to enter the password. After you have logged in to the ECS, see  [Changing the OS Keyboard Language](#en-us_topic_0027268511_section66962382111459)  to change the keyboard language of the ECS OS. You can then select the keyboard language and enter the password the next time you log in.
    -   If you have changed the keyboard language of the ECS OS, ensure that the keyboard language in use, the keyboard language selected in step  [6](#en-us_topic_0027268511_li17715715111459), and the changed OS keyboard language are all the same.


## Changing the OS Keyboard Language<a name="en-us_topic_0027268511_section66962382111459"></a>

If the ECS is running Linux, run the following command:

**loadkeys **_keymapfile_

The  _keymapfile_  parameter indicates the name of the file containing the mappings between the keys and displayed characters.

For example, if the name of a German keyboard mapping file is  **de**, run the  **loadkeys de**  command.

## Configuration Example<a name="en-us_topic_0027268511_section11831862125315"></a>

**Scenarios**

If you attempt to log in to an ECS created using a public image for the first time, the languages of the four types of keyboards before the configuration are as follows \(**Before configuration**  row in  [Table 3](#en-us_topic_0027268511_en-us_topic_0039525621_table18256759113132)\):

-   Physical keyboard: German
-   Input method keyboard on the terminal: English
-   VNC keyboard: English
-   ECS OS keyboard: English

In this case, you must change the languages of the other three types of keyboards to the same language as the physical keyboard for expected data entering. For details, see the  **Solution 1**  row in  [Table 3](#en-us_topic_0027268511_en-us_topic_0039525621_table18256759113132).

**Table  3**  Languages in the four types of keyboards

<a name="en-us_topic_0027268511_en-us_topic_0039525621_table18256759113132"></a>
<table><thead align="left"><tr id="en-us_topic_0027268511_en-us_topic_0039525621_row9068515113132"><th class="cellrowborder" valign="top" width="12.479999999999999%" id="mcps1.2.6.1.1"><p id="en-us_topic_0027268511_en-us_topic_0039525621_p14582234113132"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p14582234113132"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p14582234113132"></a>-</p>
</th>
<th class="cellrowborder" valign="top" width="15.110000000000001%" id="mcps1.2.6.1.2"><p id="en-us_topic_0027268511_en-us_topic_0039525621_p42361586113132"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p42361586113132"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p42361586113132"></a>Physical Keyboard</p>
</th>
<th class="cellrowborder" valign="top" width="27.71%" id="mcps1.2.6.1.3"><p id="en-us_topic_0027268511_en-us_topic_0039525621_p27977739113132"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p27977739113132"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p27977739113132"></a>Input Method Keyboard on the Terminal</p>
</th>
<th class="cellrowborder" valign="top" width="17.560000000000002%" id="mcps1.2.6.1.4"><p id="en-us_topic_0027268511_en-us_topic_0039525621_p334247113132"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p334247113132"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p334247113132"></a>VNC Keyboard</p>
</th>
<th class="cellrowborder" valign="top" width="27.139999999999997%" id="mcps1.2.6.1.5"><p id="en-us_topic_0027268511_en-us_topic_0039525621_p28450884113132"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p28450884113132"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p28450884113132"></a>ECS OS Keyboard</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0027268511_en-us_topic_0039525621_row66463964113132"><td class="cellrowborder" valign="top" width="12.479999999999999%" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p35901676113132"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p35901676113132"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p35901676113132"></a>Before configuration</p>
</td>
<td class="cellrowborder" valign="top" width="15.110000000000001%" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p39567167113132"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p39567167113132"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p39567167113132"></a>German</p>
</td>
<td class="cellrowborder" valign="top" width="27.71%" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p4754515113132"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p4754515113132"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p4754515113132"></a>English</p>
</td>
<td class="cellrowborder" valign="top" width="17.560000000000002%" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p10285226113132"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p10285226113132"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p10285226113132"></a>English</p>
</td>
<td class="cellrowborder" valign="top" width="27.139999999999997%" headers="mcps1.2.6.1.5 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p60540098113132"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p60540098113132"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p60540098113132"></a>English</p>
</td>
</tr>
<tr id="en-us_topic_0027268511_en-us_topic_0039525621_row51666207113132"><td class="cellrowborder" valign="top" width="12.479999999999999%" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0027268511_p55039631141644"><a name="en-us_topic_0027268511_p55039631141644"></a><a name="en-us_topic_0027268511_p55039631141644"></a>Solution 1</p>
</td>
<td class="cellrowborder" valign="top" width="15.110000000000001%" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p37520760113132"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p37520760113132"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p37520760113132"></a>German</p>
</td>
<td class="cellrowborder" valign="top" width="27.71%" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p57919400113132"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p57919400113132"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p57919400113132"></a>German</p>
</td>
<td class="cellrowborder" valign="top" width="17.560000000000002%" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p59003866113132"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p59003866113132"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p59003866113132"></a>German</p>
</td>
<td class="cellrowborder" valign="top" width="27.139999999999997%" headers="mcps1.2.6.1.5 "><p id="en-us_topic_0027268511_en-us_topic_0039525621_p32027277113132"><a name="en-us_topic_0027268511_en-us_topic_0039525621_p32027277113132"></a><a name="en-us_topic_0027268511_en-us_topic_0039525621_p32027277113132"></a>German</p>
</td>
</tr>
<tr id="en-us_topic_0027268511_row2539012014327"><td class="cellrowborder" valign="top" width="12.479999999999999%" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0027268511_p3256759814327"><a name="en-us_topic_0027268511_p3256759814327"></a><a name="en-us_topic_0027268511_p3256759814327"></a>Solution 2</p>
</td>
<td class="cellrowborder" valign="top" width="15.110000000000001%" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0027268511_p3263481314327"><a name="en-us_topic_0027268511_p3263481314327"></a><a name="en-us_topic_0027268511_p3263481314327"></a>English</p>
</td>
<td class="cellrowborder" valign="top" width="27.71%" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0027268511_p3872257314327"><a name="en-us_topic_0027268511_p3872257314327"></a><a name="en-us_topic_0027268511_p3872257314327"></a>English</p>
</td>
<td class="cellrowborder" valign="top" width="17.560000000000002%" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0027268511_p2451625614327"><a name="en-us_topic_0027268511_p2451625614327"></a><a name="en-us_topic_0027268511_p2451625614327"></a>English</p>
</td>
<td class="cellrowborder" valign="top" width="27.139999999999997%" headers="mcps1.2.6.1.5 "><p id="en-us_topic_0027268511_p5598411614327"><a name="en-us_topic_0027268511_p5598411614327"></a><a name="en-us_topic_0027268511_p5598411614327"></a>English</p>
</td>
</tr>
</tbody>
</table>

**Procedure**

1.  <a name="en-us_topic_0027268511_en-us_topic_0039525621_li55865773114331"></a>Locally configure the language, for example, German, in the input method keyboard on the terminal.
2.  Set the VNC keyboard language to English.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >When you log in to the ECS using VNC for the first time, the default ECS OS keyboard language is English. Therefore, you must set the VNC keyboard language to English.  

3.  Log in to the ECS and change the ECS OS language to German.

    For details, see  [Changing the OS Keyboard Language](#en-us_topic_0027268511_section66962382111459).

4.  <a name="en-us_topic_0027268511_en-us_topic_0039525621_li62706781115148"></a>Change the VNC keyboard language to German.

    For details, see  [Logging In to an ECS Using a Non-English Keyboard](#en-us_topic_0027268511_section5982347111459).


To set the languages on the four types of keyboards to all be the same, perform  [1](#en-us_topic_0027268511_en-us_topic_0039525621_li55865773114331)  to  [4](#en-us_topic_0027268511_en-us_topic_0039525621_li62706781115148).

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>During the configuration, if English characters cannot be entered using the current physical keyboard, use the English soft keyboard to modify the configuration described in the  **Solution 2**  row of  [Table 3](#en
>-us_topic_0027268511_en-us_topic_0039525621_table18256759113132). In such a case, you only need to use the English soft keyboard to enter characters.  
>-   To enable the Windows English soft keyboard, choose  **Start**  \>  **Run**, enter  **osk**, and press  **Enter**.  
>-   The method of enabling the Linux English soft keyboard varies depending on the OS version and is not described in this document.  

## Follow-up Procedure<a name="section322133015286"></a>

Local commands can be copied to an ECS. To do so, perform the following operations:

1.  Log in to the ECS using VNC.
2.  Click  **Input Commands**  in the upper right corner of the page.

    **Figure  9**  Input Commands<a name="en-us_topic_0093263548_fig18993162320449"></a>  
    ![](figures/input-commands.png "input-commands")

3.  Press  **Ctrl+C**  to copy data from the local computer.
4.  Press  **Ctrl+V**  to paste the local data to the  **Copy Commands**  window.
5.  Click  **Send**.

    Send the copied data to the CLI.


>![](public_sys-resources/icon-note.gif) **NOTE:**   
>There is a low probability that data is lost when you use Input Commands on the VNC page of a GUI-based Linux ECS. This is because the number of ECS vCPUs fails to meet GUI requirements. In such a case, you are advised to send a maximum of 5 characters at a time or switch from GUI to CLI \(also called text interface\), and then use the command input function.  

## Helpful Links<a name="en-us_topic_0027268511_section32612662143917"></a>

For FAQs about VNC-based ECS logins, see the following links:

-   [What Browser Version Is Required to Remotely Log In to an ECS?](what-browser-version-is-required-to-remotely-log-in-to-an-ecs.md)
-   [Why Cannot I Use the German Keyboard to Enter Characters After I Log In to an ECS Using VNC?](why-cannot-i-use-the-german-keyboard-to-enter-characters-after-i-log-in-to-an-ecs-using-vnc.md)
-   [Why Cannot I Use the MAC Keyboard to Enter Lowercase Characters After I Log In to an ECS Using VNC?](why-cannot-i-use-the-mac-keyboard-to-enter-lowercase-characters-after-i-log-in-to-an-ecs-using-vnc.md)
-   [What Should I Do If the Page Does not Respond After I Log In to an ECS Using VNC and Do Not Perform Any Operation for a Long Period of Time?](what-should-i-do-if-the-page-does-not-respond-after-i-log-in-to-an-ecs-using-vnc-and-do-not-perform.md)
-   [What Should I Do If I Cannot View Data After Logging In to an ECS Using VNC?](what-should-i-do-if-i-cannot-view-data-after-logging-in-to-an-ecs-using-vnc.md)
-   [Why Are Characters Entered Through VNC Still Incorrect After the Keyboard Language Is Switched?](why-are-characters-entered-through-vnc-still-incorrect-after-the-keyboard-language-is-switched.md)
-   [Why Does a Blank Screen Appear While the System Displays a Message Indicating Successful Authentication After I Attempted to Log In to an ECS Using VNC?](why-does-a-blank-screen-appear-while-the-system-displays-a-message-indicating-successful-authenticat.md)

