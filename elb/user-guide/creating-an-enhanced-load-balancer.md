# Creating an Enhanced Load Balancer<a name="en-us_topic_0052569751"></a>

## Scenarios<a name="section38819676182646"></a>

This section describes how to create an enhanced load balancer.

## Prepare for Creation<a name="section95639111874"></a>

-   Select the protocol.

    <a name="table66244785114429"></a><table><thead align="left"><tr id="row36701900114429"><th class="cellrowborder" colspan="2" valign="top" id="mcps1.1.5.1.1"><p id="p4473966141520"><a name="p4473966141520"></a><a name="p4473966141520"></a><strong id="b842352706102621"><a name="b842352706102621"></a><a name="b842352706102621"></a>Protocol</strong></p>
    </th>
    <th class="cellrowborder" valign="top" id="mcps1.1.5.1.2"><p id="p60499166141520"><a name="p60499166141520"></a><a name="p60499166141520"></a><strong id="b8423527061772"><a name="b8423527061772"></a><a name="b8423527061772"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" id="mcps1.1.5.1.3"><p id="p18652969141520"><a name="p18652969141520"></a><a name="p18652969141520"></a><strong id="b842352706102634"><a name="b842352706102634"></a><a name="b842352706102634"></a>Application Scenario</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row52657811114429"><td class="cellrowborder" valign="top" width="13.35133513351335%" headers="mcps1.1.5.1.1 "><p id="p8541510141438"><a name="p8541510141438"></a><a name="p8541510141438"></a>Layer 4</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.591259125912593%" headers="mcps1.1.5.1.1 "><p id="p20330484141012"><a name="p20330484141012"></a><a name="p20330484141012"></a>TCP</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.593759375937594%" headers="mcps1.1.5.1.2 "><a name="ul39716962141048"></a><a name="ul39716962141048"></a><ul id="ul39716962141048"><li id="li2168697141048"><a name="li2168697141048"></a><a name="li2168697141048"></a>Source IP address–based sticky sessions</li><li id="li15734882141048"><a name="li15734882141048"></a><a name="li15734882141048"></a>Fast data transfer</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="36.46364636463646%" headers="mcps1.1.5.1.3 "><a name="ul2315607141239"></a><a name="ul2315607141239"></a><ul id="ul2315607141239"><li id="li5593824141239"><a name="li5593824141239"></a><a name="li5593824141239"></a>Scenarios that require high reliability and data accuracy, such as file transfer, email sending and receiving, and remote login</li><li id="li59642403141239"><a name="li59642403141239"></a><a name="li59642403141239"></a>Web applications that feature a number of concurrent connections and require high performance</li></ul>
    </td>
    </tr>
    <tr id="row10296890141711"><td class="cellrowborder" valign="top" width="13.35133513351335%" headers="mcps1.1.5.1.1 "><p id="p55450303141740"><a name="p55450303141740"></a><a name="p55450303141740"></a>Layer 7</p>
    <p id="p7817510164448"><a name="p7817510164448"></a><a name="p7817510164448"></a></p>
    </td>
    <td class="cellrowborder" valign="top" width="12.591259125912593%" headers="mcps1.1.5.1.1 "><p id="p800742416177"><a name="p800742416177"></a><a name="p800742416177"></a>HTTP</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.593759375937594%" headers="mcps1.1.5.1.2 "><a name="ul21894483141932"></a><a name="ul21894483141932"></a><ul id="ul21894483141932"><li id="li48229158141932"><a name="li48229158141932"></a><a name="li48229158141932"></a>Cookie-based sticky sessions</li><li id="li10273639141932"><a name="li10273639141932"></a><a name="li10273639141932"></a>X-Forward-For request header</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="36.46364636463646%" headers="mcps1.1.5.1.3 "><p id="p55802598141819"><a name="p55802598141819"></a><a name="p55802598141819"></a>Applications in which the data content needs to be identified, such as web applications and mobile games</p>
    </td>
    </tr>
    <tr id="row28640447153915"><td class="cellrowborder" valign="top" width="13.35133513351335%" headers="mcps1.1.5.1.1 "><p id="p56437432153915"><a name="p56437432153915"></a><a name="p56437432153915"></a>Layer 7</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.591259125912593%" headers="mcps1.1.5.1.1 "><p id="p25931503153925"><a name="p25931503153925"></a><a name="p25931503153925"></a>HTTPS</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.593759375937594%" headers="mcps1.1.5.1.2 "><a name="ul15623313153925"></a><a name="ul15623313153925"></a><ul id="ul15623313153925"><li id="li47997652153925"><a name="li47997652153925"></a><a name="li47997652153925"></a>Unified certificate management<p id="p57548904164633"><a name="p57548904164633"></a><a name="p57548904164633"></a>You can upload certificates to the load balancer. The decryption operations are performed on the load balancer to reduce the work load of backend ECSs.</p>
    </li><li id="li62604581153925"><a name="li62604581153925"></a><a name="li62604581153925"></a>Multiple encryption protocols and cipher suites</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="36.46364636463646%" headers="mcps1.1.5.1.3 "><p id="p46181812153925"><a name="p46181812153925"></a><a name="p46181812153925"></a>Applications that require encrypted transmission</p>
    </td>
    </tr>
    </tbody>
    </table>


## Create a Load Balancer<a name="section50279541173248"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/en-us_image_0093332126.png)  and select the desired region and project.
3.  Under  **Network**, click **Elastic Load Balance**.
4.  On the  **Elastic Load Balance** page, click **Create Enhanced Load Balancer** and specify the parameters based on [Table 1](#table19774449171721).

    **Table  1**  Load balancer parameters

    <a name="table19774449171721"></a><table><thead align="left"><tr id="row29122391171721"><th class="cellrowborder" valign="top" width="23.18%" id="mcps1.2.4.1.1"><p id="p10103438171721"><a name="p10103438171721"></a><a name="p10103438171721"></a><strong id="b842352706114331"><a name="b842352706114331"></a><a name="b842352706114331"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.26%" id="mcps1.2.4.1.2"><p id="p13072170171721"><a name="p13072170171721"></a><a name="p13072170171721"></a><strong id="b8423527061772_1"><a name="b8423527061772_1"></a><a name="b8423527061772_1"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.56%" id="mcps1.2.4.1.3"><p id="p52212883171721"><a name="p52212883171721"></a><a name="p52212883171721"></a><strong id="b84235270617719"><a name="b84235270617719"></a><a name="b84235270617719"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1385136171721"><td class="cellrowborder" valign="top" width="23.18%" headers="mcps1.2.4.1.1 "><p id="p45087210171721"><a name="p45087210171721"></a><a name="p45087210171721"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.26%" headers="mcps1.2.4.1.2 "><p id="p28185384171721"><a name="p28185384171721"></a><a name="p28185384171721"></a>Specifies the load balancer name.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.56%" headers="mcps1.2.4.1.3 "><p id="p1314771171721"><a name="p1314771171721"></a><a name="p1314771171721"></a>elb93wd</p>
    </td>
    </tr>
    <tr id="row18944101171721"><td class="cellrowborder" valign="top" width="23.18%" headers="mcps1.2.4.1.1 "><p id="p58077182171721"><a name="p58077182171721"></a><a name="p58077182171721"></a>VPC</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.26%" headers="mcps1.2.4.1.2 "><p id="p6631263171721"><a name="p6631263171721"></a><a name="p6631263171721"></a>Specifies the VPC where the load balancer works.</p>
    <p id="p59681370171721"><a name="p59681370171721"></a><a name="p59681370171721"></a>You can select an existing VPC or create one.</p>
    <p id="p261425171721"><a name="p261425171721"></a><a name="p261425171721"></a>For more information about VPC, see the <em id="i84235269714525"><a name="i84235269714525"></a><a name="i84235269714525"></a>Virtual Private Cloud User Guide</em>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.56%" headers="mcps1.2.4.1.3 "><p id="p21175451171721"><a name="p21175451171721"></a><a name="p21175451171721"></a>vpc-4536</p>
    </td>
    </tr>
    <tr id="row56361337171721"><td class="cellrowborder" valign="top" width="23.18%" headers="mcps1.2.4.1.1 "><p id="p1865595171721"><a name="p1865595171721"></a><a name="p1865595171721"></a>Subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.26%" headers="mcps1.2.4.1.2 "><p id="p16895530171721"><a name="p16895530171721"></a><a name="p16895530171721"></a>Specifies the subnet that the load balancer belongs to.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.56%" headers="mcps1.2.4.1.3 "><p id="p26360685171721"><a name="p26360685171721"></a><a name="p26360685171721"></a>subnet-4536</p>
    </td>
    </tr>
    <tr id="row35919578171721"><td class="cellrowborder" valign="top" width="23.18%" headers="mcps1.2.4.1.1 "><p id="p23804695171721"><a name="p23804695171721"></a><a name="p23804695171721"></a>Virtual IP Address</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.26%" headers="mcps1.2.4.1.2 "><p id="p49132124171721"><a name="p49132124171721"></a><a name="p49132124171721"></a>Specifies the IP address bound to the load balancer. You can select <strong id="b84235270615249"><a name="b84235270615249"></a><a name="b84235270615249"></a>Automatically assign</strong>&nbsp;or&nbsp;<strong id="b84235270615254"><a name="b84235270615254"></a><a name="b84235270615254"></a>Manually specify</strong>. If you select&nbsp;<strong id="b61315038315318"><a name="b61315038315318"></a><a name="b61315038315318"></a>Manually specify</strong>, enter an IP address.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.56%" headers="mcps1.2.4.1.3 "><p id="p20279122171721"><a name="p20279122171721"></a><a name="p20279122171721"></a>Manually specify</p>
    </td>
    </tr>
    <tr id="row48294375171721"><td class="cellrowborder" valign="top" width="23.18%" headers="mcps1.2.4.1.1 "><p id="p52399063171831"><a name="p52399063171831"></a><a name="p52399063171831"></a>EIP</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.26%" headers="mcps1.2.4.1.2 "><p id="p27351457171721"><a name="p27351457171721"></a><a name="p27351457171721"></a>Specifies the public IP address bound to the load balancer for routing access requests to multiple ECSs over the Internet.</p>
    <p id="p34304080171721"><a name="p34304080171721"></a><a name="p34304080171721"></a>The following options are available:</p>
    <a name="ul40301268171721"></a><a name="ul40301268171721"></a><ul id="ul40301268171721"><li id="li27167097171721"><a name="li27167097171721"></a><a name="li27167097171721"></a><strong id="b84235270615639"><a name="b84235270615639"></a><a name="b84235270615639"></a>Not required</strong>: No EIP will be bound to the load balancer. Therefore, the load balancer cannot receive requests from clients over the Internet.</li><li id="li43177289171721"><a name="li43177289171721"></a><a name="li43177289171721"></a><strong id="b842352706201836"><a name="b842352706201836"></a><a name="b842352706201836"></a>New EIP</strong>: The system will assign a new EIP.</li><li id="li2186694171721"><a name="li2186694171721"></a><a name="li2186694171721"></a><strong id="b380112059535"><a name="b380112059535"></a><a name="b380112059535"></a>Use existing</strong>: An existing EIP will be bound to the load balancer. You need to select an EIP.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="23.56%" headers="mcps1.2.4.1.3 "><p id="p41882624171721"><a name="p41882624171721"></a><a name="p41882624171721"></a>Use existing</p>
    </td>
    </tr>
    <tr id="row11981483171721"><td class="cellrowborder" valign="top" width="23.18%" headers="mcps1.2.4.1.1 "><p id="p30976079171721"><a name="p30976079171721"></a><a name="p30976079171721"></a>Bandwidth</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.26%" headers="mcps1.2.4.1.2 "><p id="p26034434171721"><a name="p26034434171721"></a><a name="p26034434171721"></a>Specifies the public network bandwidth when a new EIP is used.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.56%" headers="mcps1.2.4.1.3 "><p id="p28414447171721"><a name="p28414447171721"></a><a name="p28414447171721"></a>100 Mbit/s</p>
    </td>
    </tr>
    <tr id="row57564991616"><td class="cellrowborder" valign="top" width="23.18%" headers="mcps1.2.4.1.1 "><p id="p157617491163"><a name="p157617491163"></a><a name="p157617491163"></a>Tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.26%" headers="mcps1.2.4.1.2 "><p id="p1864552153110"><a name="p1864552153110"></a><a name="p1864552153110"></a>Identifies cloud resources so that they can be easily categorized and quickly searched. A tag consists of a tag key and a tag value. That is, you can distinguish cloud resources from two dimensions. The tag key marks a tag, and the tag value specifies specific tag content.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.56%" headers="mcps1.2.4.1.3 "><p id="p197634910161"><a name="p197634910161"></a><a name="p197634910161"></a>N/A</p>
    </td>
    </tr>
    <tr id="row54403434171721"><td class="cellrowborder" valign="top" width="23.18%" headers="mcps1.2.4.1.1 "><p id="p44602014171721"><a name="p44602014171721"></a><a name="p44602014171721"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.26%" headers="mcps1.2.4.1.2 "><p id="p55993375171721"><a name="p55993375171721"></a><a name="p55993375171721"></a>Provides supplementary information about the load balancer.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.56%" headers="mcps1.2.4.1.3 "><p id="p39169492171721"><a name="p39169492171721"></a><a name="p39169492171721"></a>N/A</p>
    </td>
    </tr>
    </tbody>
    </table>

5.  Click  **Create Now**.
6.  Confirm the specifications and click  **Submit**.

## Add a Listener<a name="section5962364716114"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/en-us_image_0093340518.png)  and select the desired region and project.
3.  Under  **Network**, click **Elastic Load Balance**.
4.  On the  **Elastic Load Balance**  page, locate the row that contains the target load balancer and click its name.
5.  In the  **Listeners** area, click **Add Listener**.
6.  In the displayed  **Add Listener** dialog box, configure the parameters by referring to [Table 2](#table1782216171449). When **Frontend Protocol** is set to **HTTPS**, a certificate must be deployed for the load balancer.

    > ![](public_sys-resources/icon-note.gif) **NOTE:** 

    > To add a listener in IP mode \(DR mode\), you must set  **Frontend Protocol** to **TCP** and **Port** to **0**.

    **Table  2**  Listener parameters

    <a name="table1782216171449"></a><table><thead align="left"><tr id="row5822101719444"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p11262131634517"><a name="p11262131634517"></a><a name="p11262131634517"></a><strong id="b84235270615222"><a name="b84235270615222"></a><a name="b84235270615222"></a>Item</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p10270161664511"><a name="p10270161664511"></a><a name="p10270161664511"></a><strong id="b842352706114331_1"><a name="b842352706114331_1"></a><a name="b842352706114331_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p12751116104512"><a name="p12751116104512"></a><a name="p12751116104512"></a><strong id="b8423527061772_2"><a name="b8423527061772_2"></a><a name="b8423527061772_2"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p15283316174520"><a name="p15283316174520"></a><a name="p15283316174520"></a><strong id="b842352706151735"><a name="b842352706151735"></a><a name="b842352706151735"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row16822141716449"><td class="cellrowborder" rowspan="5" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1129514168451"><a name="p1129514168451"></a><a name="p1129514168451"></a>Listener</p>
    <p id="p19264101754519"><a name="p19264101754519"></a><a name="p19264101754519"></a></p>
    <p id="p17257617194512"><a name="p17257617194512"></a><a name="p17257617194512"></a></p>
    <p id="p7253101774516"><a name="p7253101774516"></a><a name="p7253101774516"></a></p>
    <p id="p15250181717458"><a name="p15250181717458"></a><a name="p15250181717458"></a></p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p18301141664519"><a name="p18301141664519"></a><a name="p18301141664519"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p3310111619452"><a name="p3310111619452"></a><a name="p3310111619452"></a>Specifies the listener name.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p53155163453"><a name="p53155163453"></a><a name="p53155163453"></a>listener01</p>
    </td>
    </tr>
    <tr id="row082231713448"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p332513166451"><a name="p332513166451"></a><a name="p332513166451"></a>Frontend Protocol/Port</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p3331161611453"><a name="p3331161611453"></a><a name="p3331161611453"></a>Specifies the protocol and port the load balancer uses to receive requests from the client and forwards the requests to backend ECSs.</p>
    <p id="p1733619169458"><a name="p1733619169458"></a><a name="p1733619169458"></a>The port number ranges from 1 to 65535, and the following protocols are available:</p>
    <a name="ul1333921624515"></a><a name="ul1333921624515"></a><ul id="ul1333921624515"><li id="li17340416124515"><a name="li17340416124515"></a><a name="li17340416124515"></a>HTTP: load balancing at Layer 7</li></ul>
    <a name="ul134851611458"></a><a name="ul134851611458"></a><ul id="ul134851611458"><li id="li1035331611451"><a name="li1035331611451"></a><a name="li1035331611451"></a>TCP: load balancing at Layer 4</li><li id="li17357116144515"><a name="li17357116144515"></a><a name="li17357116144515"></a>HTTPS: HTTPS-based load balancing</li></ul>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p236512161451"><a name="p236512161451"></a><a name="p236512161451"></a>HTTP/80</p>
    </td>
    </tr>
    <tr id="row48221117114413"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p1837421618454"><a name="p1837421618454"></a><a name="p1837421618454"></a>Backend Protocol</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p2380816174514"><a name="p2380816174514"></a><a name="p2380816174514"></a>Specifies the protocol and port used by backend ECSs to receive requests.</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p15389191654518"><a name="p15389191654518"></a><a name="p15389191654518"></a>N/A</p>
    </td>
    </tr>
    <tr id="row108231817124412"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p12398171674512"><a name="p12398171674512"></a><a name="p12398171674512"></a>Certificate</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p12404916104520"><a name="p12404916104520"></a><a name="p12404916104520"></a>Specifies the certificate to be used when the frontend protocol is HTTPS.</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p6410516124517"><a name="p6410516124517"></a><a name="p6410516124517"></a>N/A</p>
    </td>
    </tr>
    <tr id="row158234176442"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p10421201694518"><a name="p10421201694518"></a><a name="p10421201694518"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p54261816204515"><a name="p54261816204515"></a><a name="p54261816204515"></a>Provides supplementary information about the listener.</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p643415167457"><a name="p643415167457"></a><a name="p643415167457"></a>N/A</p>
    </td>
    </tr>
    <tr id="row178231017164411"><td class="cellrowborder" rowspan="6" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1144191654517"><a name="p1144191654517"></a><a name="p1144191654517"></a>Backend ECS group</p>
    <p id="p8449171694513"><a name="p8449171694513"></a><a name="p8449171694513"></a></p>
    <p id="p12244517144516"><a name="p12244517144516"></a><a name="p12244517144516"></a></p>
    <p id="p13241111764516"><a name="p13241111764516"></a><a name="p13241111764516"></a></p>
    <p id="p62371417144516"><a name="p62371417144516"></a><a name="p62371417144516"></a></p>
    <p id="p4234817184510"><a name="p4234817184510"></a><a name="p4234817184510"></a></p>
    <p id="p6232111716456"><a name="p6232111716456"></a><a name="p6232111716456"></a></p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p245413166458"><a name="p245413166458"></a><a name="p245413166458"></a>Backend ECS Group</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p7466141664510"><a name="p7466141664510"></a><a name="p7466141664510"></a>Specifies a group of backend ECSs that have the same features.</p>
    <a name="ul12474141664517"></a><a name="ul12474141664517"></a><ul id="ul12474141664517"><li id="li1047851614514"><a name="li1047851614514"></a><a name="li1047851614514"></a>Select <strong id="b13855896163224"><a name="b13855896163224"></a><a name="b13855896163224"></a>Create new</strong> if you want to create a backend ECS group.</li><li id="li124821169458"><a name="li124821169458"></a><a name="li124821169458"></a>Select <strong id="b842352706132312"><a name="b842352706132312"></a><a name="b842352706132312"></a>Not required</strong> if you do not need a backend ECS group.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p144911316194516"><a name="p144911316194516"></a><a name="p144911316194516"></a>Create new</p>
    </td>
    </tr>
    <tr id="row282311715442"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p8500101684519"><a name="p8500101684519"></a><a name="p8500101684519"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p95041016184518"><a name="p95041016184518"></a><a name="p95041016184518"></a>Specifies the name of the backend ECS group.</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p9517116154512"><a name="p9517116154512"></a><a name="p9517116154512"></a>pool-i28r</p>
    </td>
    </tr>
    <tr id="row15823101734416"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p5525716114510"><a name="p5525716114510"></a><a name="p5525716114510"></a>Load Balancing Algorithm</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p1553151614452"><a name="p1553151614452"></a><a name="p1553151614452"></a>Specifies the algorithm the load balancer uses to distribute traffic.</p>
    <a name="ul1953513163458"></a><a name="ul1953513163458"></a><ul id="ul1953513163458"><li id="li1537151620458"><a name="li1537151620458"></a><a name="li1537151620458"></a><strong id="b84235270615355"><a name="b84235270615355"></a><a name="b84235270615355"></a>Weighted round robin</strong>: Requests are forwarded to different ECSs in sequence, and backend ECSs assigned with higher weights receive more requests than those with smaller weights. The weight indicates the processing performance of the ECS. ECSs with the same weights process the equal number of connections.</li><li id="li654410161453"><a name="li654410161453"></a><a name="li654410161453"></a><strong id="b842352706103824"><a name="b842352706103824"></a><a name="b842352706103824"></a>Weighted least connections</strong>: In addition to the weight assigned to each backend ECS, the number of connections processed by each ECS is also considered. Connection requests are forwarded to the ECS with the lowest ratio of connections to weight.</li><li id="li11550181694510"><a name="li11550181694510"></a><a name="li11550181694510"></a><strong id="b84235270616237"><a name="b84235270616237"></a><a name="b84235270616237"></a>Source IP hash</strong>: The source IP address of the request is used as the hash key to identify an ECS in the static fragment table.</li></ul>
    <div class="note" id="note13555516114519"><a name="note13555516114519"></a><a name="note13555516114519"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p956671619453"><a name="p956671619453"></a><a name="p956671619453"></a>As access traffic changes, choose the most appropriate algorithm to improve load balancing.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p8571201611452"><a name="p8571201611452"></a><a name="p8571201611452"></a>Weighted round robin</p>
    </td>
    </tr>
    <tr id="row15823171754418"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p155791916204514"><a name="p155791916204514"></a><a name="p155791916204514"></a>Sticky Session Type</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p65841716164516"><a name="p65841716164516"></a><a name="p65841716164516"></a>If the sticky session feature is enabled, all requests from the same client during one session will be sent to the same backend ECS.</p>
    <p id="p18596416114511"><a name="p18596416114511"></a><a name="p18596416114511"></a>Specifies the sticky session type. The following options are available:</p>
    <a name="ul1160071614512"></a><a name="ul1160071614512"></a><ul id="ul1160071614512"><li id="li11602191620456"><a name="li11602191620456"></a><a name="li11602191620456"></a><strong>Source IP address</strong>: The source IP address of the request is used as the hash key to identify an ECS in the static fragment table.</li><li id="li46080161455"><a name="li46080161455"></a><a name="li46080161455"></a><strong id="b842352706162813"><a name="b842352706162813"></a><a name="b842352706162813"></a>HTTP cookie</strong>: The load balancer generates a cookie after it receives a request from a client. All the subsequent requests with the cookie are distributed to the same backend ECS.</li><li id="li1612181654516"><a name="li1612181654516"></a><a name="li1612181654516"></a><strong>App cookie</strong>: This type of sticky session relies on backend applications. All requests with the cookie generated by backend applications are distributed to the same backend ECS.</li></ul>
    <div class="note" id="note161910162455"><a name="note161910162455"></a><a name="note161910162455"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p136311416114515"><a name="p136311416114515"></a><a name="p136311416114515"></a><strong id="b44249155162219"><a name="b44249155162219"></a><a name="b44249155162219"></a>Source IP address</strong>&nbsp;is the only choice available when TCP is used as the frontend protocol. If HTTP or HTTPS is used as the frontend protocol, the sticky session type can be&nbsp;<strong id="b842352706221152"><a name="b842352706221152"></a><a name="b842352706221152"></a>HTTP cookie</strong>&nbsp;or&nbsp;<strong id="b842352706221155"><a name="b842352706221155"></a><a name="b842352706221155"></a>App cookie</strong>. Choose an appropriate sticky session type to better distribute access traffic and improve load balancing.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p86371916204516"><a name="p86371916204516"></a><a name="p86371916204516"></a>Source IP address</p>
    </td>
    </tr>
    <tr id="row1182351734420"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p464551614518"><a name="p464551614518"></a><a name="p464551614518"></a>Cookie Name</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p765121604519"><a name="p765121604519"></a><a name="p765121604519"></a>Specifies the cookie name. When <strong id="b84235270617853"><a name="b84235270617853"></a><a name="b84235270617853"></a>App cookie</strong> is selected, you need to enter a cookie name.</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p76562165450"><a name="p76562165450"></a><a name="p76562165450"></a>cookie1223</p>
    </td>
    </tr>
    <tr id="row1582316176445"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p16665216194512"><a name="p16665216194512"></a><a name="p16665216194512"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p10671171610455"><a name="p10671171610455"></a><a name="p10671171610455"></a>Provides supplementary information about the backend ECS group.</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p0678116154512"><a name="p0678116154512"></a><a name="p0678116154512"></a>N/A</p>
    </td>
    </tr>
    <tr id="row118261417144415"><td class="cellrowborder" rowspan="8" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p13922101614510"><a name="p13922101614510"></a><a name="p13922101614510"></a>Health check</p>
    <p id="p1292531634518"><a name="p1292531634518"></a><a name="p1292531634518"></a></p>
    <p id="p492771694518"><a name="p492771694518"></a><a name="p492771694518"></a></p>
    <p id="p29311916154515"><a name="p29311916154515"></a><a name="p29311916154515"></a></p>
    <p id="p5934121618455"><a name="p5934121618455"></a><a name="p5934121618455"></a></p>
    <p id="p17198101734512"><a name="p17198101734512"></a><a name="p17198101734512"></a></p>
    <p id="p519551714450"><a name="p519551714450"></a><a name="p519551714450"></a></p>
    <p id="p219131764513"><a name="p219131764513"></a><a name="p219131764513"></a></p>
    <p id="p7190417124511"><a name="p7190417124511"></a><a name="p7190417124511"></a></p>
    <p id="p1052161734510"><a name="p1052161734510"></a><a name="p1052161734510"></a></p>
    <p id="p14801017194518"><a name="p14801017194518"></a><a name="p14801017194518"></a></p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p69401716184518"><a name="p69401716184518"></a><a name="p69401716184518"></a>Health Check Protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p1394721694517"><a name="p1394721694517"></a><a name="p1394721694517"></a>Specifies the health check protocol. You can use either TCP or HTTP. Once you have selected a specific protocol, you cannot change it. The following options are available:</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p7952141617457"><a name="p7952141617457"></a><a name="p7952141617457"></a>HTTP</p>
    </td>
    </tr>
    <tr id="row669020142195"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p1888615282196"><a name="p1888615282196"></a><a name="p1888615282196"></a>Domain Name</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p989272815199"><a name="p989272815199"></a><a name="p989272815199"></a>Specified the domain name in the health check request. The domain name consists of digits, letters, hyphens (-), and periods (.), and must start with a digit or character. The field is left blank by default.</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p1589614281193"><a name="p1589614281193"></a><a name="p1589614281193"></a>www.elb.com</p>
    </td>
    </tr>
    <tr id="row7826181794417"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p0959121624516"><a name="p0959121624516"></a><a name="p0959121624516"></a>Interval</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p496611694513"><a name="p496611694513"></a><a name="p496611694513"></a>Specifies the maximum amount of time between health checks in the unit of second.</p>
    <p id="p15969151610458"><a name="p15969151610458"></a><a name="p15969151610458"></a>The value ranges from 1 to 5.</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p2097518163453"><a name="p2097518163453"></a><a name="p2097518163453"></a>5 seconds</p>
    </td>
    </tr>
    <tr id="row7826141720445"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p15984716174517"><a name="p15984716174517"></a><a name="p15984716174517"></a>Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p1498961618457"><a name="p1498961618457"></a><a name="p1498961618457"></a>Specifies the maximum amount of time you need to wait when receiving a response from the health check in the unit of second.</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p16996201674516"><a name="p16996201674516"></a><a name="p16996201674516"></a>10 seconds</p>
    </td>
    </tr>
    <tr id="row5827181718448"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p54141774516"><a name="p54141774516"></a><a name="p54141774516"></a>Check Path</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p17121917194515"><a name="p17121917194515"></a><a name="p17121917194515"></a>Specifies the health check path, which is a URL. This parameter is required if <strong id="b842352706111632"><a name="b842352706111632"></a><a name="b842352706111632"></a>Health Check Protocol</strong>&nbsp;is set to&nbsp;<strong id="b842352706111636"><a name="b842352706111636"></a><a name="b842352706111636"></a>HTTP</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p918121724515"><a name="p918121724515"></a><a name="p918121724515"></a>/index.html</p>
    </td>
    </tr>
    <tr id="row108271817124413"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p52961718456"><a name="p52961718456"></a><a name="p52961718456"></a>Maximum Retries</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p53517171450"><a name="p53517171450"></a><a name="p53517171450"></a>Specifies the maximum number of retries for the health check. The value ranges from 1 to 10.</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p194110177458"><a name="p194110177458"></a><a name="p194110177458"></a>3</p>
    </td>
    </tr>
    <tr id="row4827101794418"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p186061720455"><a name="p186061720455"></a><a name="p186061720455"></a>HTTP Method</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p765141784519"><a name="p765141784519"></a><a name="p765141784519"></a>Specifies the HTTP request method. This parameter is required if <strong id="b84235270617210_1"><a name="b84235270617210_1"></a><a name="b84235270617210_1"></a>Health Check Protocol</strong>&nbsp;is set to&nbsp;<strong id="b8423527061727_1"><a name="b8423527061727_1"></a><a name="b8423527061727_1"></a>HTTP</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p07113175451"><a name="p07113175451"></a><a name="p07113175451"></a>GET</p>
    </td>
    </tr>
    <tr id="row2082711174445"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p148691774510"><a name="p148691774510"></a><a name="p148691774510"></a>HTTP Status Code</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p18931617114517"><a name="p18931617114517"></a><a name="p18931617114517"></a>Specifies the returned status code for an HTTP request. This parameter is required if <strong id="b60236725817247"><a name="b60236725817247"></a><a name="b60236725817247"></a>Health Check Protocol</strong>&nbsp;is set to&nbsp;<strong id="b191107531017247"><a name="b191107531017247"></a><a name="b191107531017247"></a>HTTP</strong>&nbsp;or&nbsp;<strong id="b842352706943"><a name="b842352706943"></a><a name="b842352706943"></a>HTTPS</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p199811179454"><a name="p199811179454"></a><a name="p199811179454"></a>201</p>
    </td>
    </tr>
    </tbody>
    </table>

7.  Click  **OK**.

## Add a Whitelist<a name="section15874839185642"></a>

You can add a whitelist of specified IP addresses to control access to the listener.

For details, see  [Whitelist](https://support.huaweicloud.com/en-us/usermanual-elb/en-us_elb_03_0003.html).

> ![](public_sys-resources/icon-notice.gif) **NOTICE:** 

> Adding the whitelist may cause risks. Once the whitelist is set, only the IP addresses specified in the whitelist can access the listener.

> If access control is enabled but no whitelist is added, the listener cannot be accessed.

## Add Backend ECSs<a name="section3453061616119"></a>

You must add backend ECSs in running state to your listener so that the load balancer can distribute traffic to the ECSs. Perform the following operations to add backend ECSs:

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/en-us_image_0093332127.png)  and select the desired region and project.
3.  Under  **Network**, click **Elastic Load Balance**.
4.  On the  **Elastic Load Balance**  page, locate the row that contains the target load balancer and click its name.
5.  In the  **Backend ECS Groups** area, click **More** in the **Operation**  column.
6.  Select  **Add Backend ECS**  from the drop-down list.
7.  Enter the backend port number and select the backend ECSs to be added. You can filter backend ECSs by name or private IP address.
8.  Click  **OK**.

## Bind an EIP to a Load Balancer<a name="section62070810184614"></a>

You can bind an EIP to a load balancer to receive requests over the Internet.

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/en-us_image_0093340398.png)  and select the desired region and project.
3.  Under  **Network**, click **Elastic Load Balance**.
4.  Locate the row that contains the target load balancer and click its name.
5.  On the load balancer details page, click  **Bind** following **EIP**  and select the EIP to be bound from the drop-down list.
6.  Click  ![](figures/en-us_image_0093338676.png)  to bind the EIP to the load balancer.

    > ![](public_sys-resources/icon-note.gif) **NOTE:** 

    > Click  **Unbind**  if you do not need this EIP.


## Delete a Load Balancer<a name="section16591966183956"></a>

If you do not need a load balancer any longer, perform the following operations to delete it:

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/en-us_image_0093338676.png)  and select the desired region and project.
3.  Under  **Network**, click **Elastic Load Balance**.
4.  On the  **Elastic Load Balance** page, click **Delete** in the **Operation**  column.
5.  In the displayed  **Delete Load Balancer** dialog box, click **OK**.

> ![](public_sys-resources/icon-note.gif) **NOTE:** 

> If the load balancer has listeners, delete the listeners before deleting the load balancer.

## Export Load Balancer Information<a name="section19169366120"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/en-us_image_0119673679.png)  and select the desired region and project.
3.  Under  **Network**, click **Elastic Load Balance**.
4.  In the upper right corner of the load balancer list, click  ![](figures/en-us_image_0119672719.png).

