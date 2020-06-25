# Creating a Connection<a name="en-dc_topic_0055025315"></a>

## Function<a name="section54540374"></a>

This API is used to create a connection.

>![](/images/icon-note.gif) **NOTE:**   
>1.  When creating a hosted connection that does not need to be confirmed, you need to set  **Status**  to  **ACCEPT**.  
>2.  The bandwidth of a hosted connection cannot exceed that of the associated hosting connection.  

## URI<a name="section21101319"></a>

POST /v2.0/dcaas/direct-connects

**Table  1**  Parameter description

<a name="table7306830153125"></a>
<table><thead align="left"><tr id="row59179138153125"><th class="cellrowborder" valign="top" width="18.94%" id="mcps1.2.5.1.1"><p id="p6185651415404"><a name="p6185651415404"></a><a name="p6185651415404"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.71%" id="mcps1.2.5.1.2"><p id="p4432173215404"><a name="p4432173215404"></a><a name="p4432173215404"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="16.14%" id="mcps1.2.5.1.3"><p id="p3329052615404"><a name="p3329052615404"></a><a name="p3329052615404"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="48.209999999999994%" id="mcps1.2.5.1.4"><p id="p1217810515404"><a name="p1217810515404"></a><a name="p1217810515404"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row37905744153125"><td class="cellrowborder" valign="top" width="18.94%" headers="mcps1.2.5.1.1 "><p id="p50466461153125"><a name="p50466461153125"></a><a name="p50466461153125"></a>direct_connect</p>
</td>
<td class="cellrowborder" valign="top" width="16.71%" headers="mcps1.2.5.1.2 "><p id="p61251530153125"><a name="p61251530153125"></a><a name="p61251530153125"></a>Dictionary data structure</p>
</td>
<td class="cellrowborder" valign="top" width="16.14%" headers="mcps1.2.5.1.3 "><p id="p62426879153125"><a name="p62426879153125"></a><a name="p62426879153125"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="48.209999999999994%" headers="mcps1.2.5.1.4 "><p id="p23412453153125"><a name="p23412453153125"></a><a name="p23412453153125"></a>Specifies the <strong id="b842352706163957"><a name="b842352706163957"></a><a name="b842352706163957"></a>direct_connect</strong> object.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section31485239"></a>

[Table 2](#table26517876)  lists the  **direct\_connect**  request parameters.

**Table  2**  Request parameters

<a name="table26517876"></a>
<table><thead align="left"><tr id="row40476817"><th class="cellrowborder" valign="top" width="20.82%" id="mcps1.2.5.1.1"><p id="p57396781"><a name="p57396781"></a><a name="p57396781"></a><strong id="b8423527069918"><a name="b8423527069918"></a><a name="b8423527069918"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="11.26%" id="mcps1.2.5.1.2"><p id="p18627652"><a name="p18627652"></a><a name="p18627652"></a><strong id="b842352706165439"><a name="b842352706165439"></a><a name="b842352706165439"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.84%" id="mcps1.2.5.1.3"><p id="p32444864"><a name="p32444864"></a><a name="p32444864"></a><strong id="b842352706192549"><a name="b842352706192549"></a><a name="b842352706192549"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50.080000000000005%" id="mcps1.2.5.1.4"><p id="p10788361"><a name="p10788361"></a><a name="p10788361"></a><strong id="b84235270616553"><a name="b84235270616553"></a><a name="b84235270616553"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1442054"><td class="cellrowborder" valign="top" width="20.82%" headers="mcps1.2.5.1.1 "><p id="p11555769212825"><a name="p11555769212825"></a><a name="p11555769212825"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="11.26%" headers="mcps1.2.5.1.2 "><p id="p46548661212825"><a name="p46548661212825"></a><a name="p46548661212825"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.84%" headers="mcps1.2.5.1.3 "><p id="p40193754212825"><a name="p40193754212825"></a><a name="p40193754212825"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="50.080000000000005%" headers="mcps1.2.5.1.4 "><p id="p56409663212825"><a name="p56409663212825"></a><a name="p56409663212825"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row56455847212711"><td class="cellrowborder" valign="top" width="20.82%" headers="mcps1.2.5.1.1 "><p id="p60046645212825"><a name="p60046645212825"></a><a name="p60046645212825"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="11.26%" headers="mcps1.2.5.1.2 "><p id="p60303421212825"><a name="p60303421212825"></a><a name="p60303421212825"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.84%" headers="mcps1.2.5.1.3 "><p id="p43405365212825"><a name="p43405365212825"></a><a name="p43405365212825"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="50.080000000000005%" headers="mcps1.2.5.1.4 "><p id="p50361529212825"><a name="p50361529212825"></a><a name="p50361529212825"></a>Specifies the connection name.</p>
</td>
</tr>
<tr id="row17304671212718"><td class="cellrowborder" valign="top" width="20.82%" headers="mcps1.2.5.1.1 "><p id="p21811400212825"><a name="p21811400212825"></a><a name="p21811400212825"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="11.26%" headers="mcps1.2.5.1.2 "><p id="p10454292212825"><a name="p10454292212825"></a><a name="p10454292212825"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.84%" headers="mcps1.2.5.1.3 "><p id="p30649615212825"><a name="p30649615212825"></a><a name="p30649615212825"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="50.080000000000005%" headers="mcps1.2.5.1.4 "><p id="p2345077921328"><a name="p2345077921328"></a><a name="p2345077921328"></a>Provides supplementary information about the connection.</p>
</td>
</tr>
<tr id="row10181252212730"><td class="cellrowborder" valign="top" width="20.82%" headers="mcps1.2.5.1.1 "><p id="p33947790212825"><a name="p33947790212825"></a><a name="p33947790212825"></a>port_type</p>
</td>
<td class="cellrowborder" valign="top" width="11.26%" headers="mcps1.2.5.1.2 "><p id="p24798963212825"><a name="p24798963212825"></a><a name="p24798963212825"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.84%" headers="mcps1.2.5.1.3 "><p id="p20471702212825"><a name="p20471702212825"></a><a name="p20471702212825"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="50.080000000000005%" headers="mcps1.2.5.1.4 "><p id="p470426021328"><a name="p470426021328"></a><a name="p470426021328"></a>Specifies the type of the port used by the connection. The value can be <strong id="b370581214151058"><a name="b370581214151058"></a><a name="b370581214151058"></a>1G</strong> or <strong id="b263825441151058"><a name="b263825441151058"></a><a name="b263825441151058"></a>10G</strong>.</p>
</td>
</tr>
<tr id="row12404882212734"><td class="cellrowborder" valign="top" width="20.82%" headers="mcps1.2.5.1.1 "><p id="p17969725212825"><a name="p17969725212825"></a><a name="p17969725212825"></a>bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="11.26%" headers="mcps1.2.5.1.2 "><p id="p15690831212825"><a name="p15690831212825"></a><a name="p15690831212825"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="17.84%" headers="mcps1.2.5.1.3 "><p id="p31440261212825"><a name="p31440261212825"></a><a name="p31440261212825"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="50.080000000000005%" headers="mcps1.2.5.1.4 "><p id="p3259456521328"><a name="p3259456521328"></a><a name="p3259456521328"></a>Specifies the connection bandwidth (unit: Mbit/s).</p>
</td>
</tr>
<tr id="row13373700212741"><td class="cellrowborder" valign="top" width="20.82%" headers="mcps1.2.5.1.1 "><p id="p39007376212955"><a name="p39007376212955"></a><a name="p39007376212955"></a>location</p>
</td>
<td class="cellrowborder" valign="top" width="11.26%" headers="mcps1.2.5.1.2 "><p id="p2805339212955"><a name="p2805339212955"></a><a name="p2805339212955"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.84%" headers="mcps1.2.5.1.3 "><p id="p43667943212955"><a name="p43667943212955"></a><a name="p43667943212955"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="50.080000000000005%" headers="mcps1.2.5.1.4 "><p id="p859792021328"><a name="p859792021328"></a><a name="p859792021328"></a>Specifies the connection access location.</p>
</td>
</tr>
<tr id="row568472521295"><td class="cellrowborder" valign="top" width="20.82%" headers="mcps1.2.5.1.1 "><p id="p35118572212955"><a name="p35118572212955"></a><a name="p35118572212955"></a>peer_location</p>
</td>
<td class="cellrowborder" valign="top" width="11.26%" headers="mcps1.2.5.1.2 "><p id="p46823096212955"><a name="p46823096212955"></a><a name="p46823096212955"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.84%" headers="mcps1.2.5.1.3 "><p id="p59054635212955"><a name="p59054635212955"></a><a name="p59054635212955"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="50.080000000000005%" headers="mcps1.2.5.1.4 "><p id="p5662013921328"><a name="p5662013921328"></a><a name="p5662013921328"></a>Specifies the physical location of the peer device accessed by the connection. The value can be a street, city, and province, or an IDC.</p>
</td>
</tr>
<tr id="row938903521299"><td class="cellrowborder" valign="top" width="20.82%" headers="mcps1.2.5.1.1 "><p id="p61193031212955"><a name="p61193031212955"></a><a name="p61193031212955"></a>device_id</p>
</td>
<td class="cellrowborder" valign="top" width="11.26%" headers="mcps1.2.5.1.2 "><p id="p32925369212955"><a name="p32925369212955"></a><a name="p32925369212955"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.84%" headers="mcps1.2.5.1.3 "><p id="p34771507212955"><a name="p34771507212955"></a><a name="p34771507212955"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="50.080000000000005%" headers="mcps1.2.5.1.4 "><p id="p4654985521328"><a name="p4654985521328"></a><a name="p4654985521328"></a>Specifies the gateway device ID of the connection.</p>
</td>
</tr>
<tr id="row47530080212912"><td class="cellrowborder" valign="top" width="20.82%" headers="mcps1.2.5.1.1 "><p id="p18777601212955"><a name="p18777601212955"></a><a name="p18777601212955"></a>interface_name</p>
</td>
<td class="cellrowborder" valign="top" width="11.26%" headers="mcps1.2.5.1.2 "><p id="p41025697212955"><a name="p41025697212955"></a><a name="p41025697212955"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.84%" headers="mcps1.2.5.1.3 "><p id="p63373303212955"><a name="p63373303212955"></a><a name="p63373303212955"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="50.080000000000005%" headers="mcps1.2.5.1.4 "><p id="p3850248621328"><a name="p3850248621328"></a><a name="p3850248621328"></a>Specifies the name of the interface accessed by the connection.</p>
</td>
</tr>
<tr id="row57761938115652"><td class="cellrowborder" valign="top" width="20.82%" headers="mcps1.2.5.1.1 "><p id="p48205386115652"><a name="p48205386115652"></a><a name="p48205386115652"></a>redundant_id</p>
</td>
<td class="cellrowborder" valign="top" width="11.26%" headers="mcps1.2.5.1.2 "><p id="p5189660115752"><a name="p5189660115752"></a><a name="p5189660115752"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.84%" headers="mcps1.2.5.1.3 "><p id="p17709321115752"><a name="p17709321115752"></a><a name="p17709321115752"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="50.080000000000005%" headers="mcps1.2.5.1.4 "><p id="p2875131911580"><a name="p2875131911580"></a><a name="p2875131911580"></a>Specifies the ID of the redundant connection using the same gateway.</p>
</td>
</tr>
<tr id="row54509260212915"><td class="cellrowborder" valign="top" width="20.82%" headers="mcps1.2.5.1.1 "><p id="p17229947212955"><a name="p17229947212955"></a><a name="p17229947212955"></a>provider</p>
</td>
<td class="cellrowborder" valign="top" width="11.26%" headers="mcps1.2.5.1.2 "><p id="p61142987212955"><a name="p61142987212955"></a><a name="p61142987212955"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.84%" headers="mcps1.2.5.1.3 "><p id="p65804377212955"><a name="p65804377212955"></a><a name="p65804377212955"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="50.080000000000005%" headers="mcps1.2.5.1.4 "><p id="p2055217021328"><a name="p2055217021328"></a><a name="p2055217021328"></a>Specifies the connection provider.</p>
</td>
</tr>
<tr id="row62300161212918"><td class="cellrowborder" valign="top" width="20.82%" headers="mcps1.2.5.1.1 "><p id="p43762504212955"><a name="p43762504212955"></a><a name="p43762504212955"></a>provider_status</p>
</td>
<td class="cellrowborder" valign="top" width="11.26%" headers="mcps1.2.5.1.2 "><p id="p35371259212955"><a name="p35371259212955"></a><a name="p35371259212955"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.84%" headers="mcps1.2.5.1.3 "><p id="p21643169212955"><a name="p21643169212955"></a><a name="p21643169212955"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="50.080000000000005%" headers="mcps1.2.5.1.4 "><p id="p28964426203734"><a name="p28964426203734"></a><a name="p28964426203734"></a>Specifies the status of the provider's connection.</p>
<p id="p3389609721328"><a name="p3389609721328"></a><a name="p3389609721328"></a>The value can be <strong id="b842352706171439"><a name="b842352706171439"></a><a name="b842352706171439"></a>ACTIVE</strong> or <strong id="b842352706171443"><a name="b842352706171443"></a><a name="b842352706171443"></a>DOWN</strong>.</p>
</td>
</tr>
<tr id="row39647359112012"><td class="cellrowborder" valign="top" width="20.82%" headers="mcps1.2.5.1.1 "><p id="p1555872112023"><a name="p1555872112023"></a><a name="p1555872112023"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="11.26%" headers="mcps1.2.5.1.2 "><p id="p58916789112023"><a name="p58916789112023"></a><a name="p58916789112023"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.84%" headers="mcps1.2.5.1.3 "><p id="p7530619112023"><a name="p7530619112023"></a><a name="p7530619112023"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="50.080000000000005%" headers="mcps1.2.5.1.4 "><p id="p168021375614"><a name="p168021375614"></a><a name="p168021375614"></a>Specifies the connection type. The value can be <strong id="b2101118477"><a name="b2101118477"></a><a name="b2101118477"></a>hosted</strong>.</p>
</td>
</tr>
<tr id="row5337525611209"><td class="cellrowborder" valign="top" width="20.82%" headers="mcps1.2.5.1.1 "><p id="p12222720112023"><a name="p12222720112023"></a><a name="p12222720112023"></a>hosting_id</p>
</td>
<td class="cellrowborder" valign="top" width="11.26%" headers="mcps1.2.5.1.2 "><p id="p50516226112023"><a name="p50516226112023"></a><a name="p50516226112023"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.84%" headers="mcps1.2.5.1.3 "><p id="p65282521112023"><a name="p65282521112023"></a><a name="p65282521112023"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="50.080000000000005%" headers="mcps1.2.5.1.4 "><p id="p53392877112023"><a name="p53392877112023"></a><a name="p53392877112023"></a>Specifies the ID of the hosting connection mapped to the hosted connection.</p>
</td>
</tr>
<tr id="row2497249511206"><td class="cellrowborder" valign="top" width="20.82%" headers="mcps1.2.5.1.1 "><p id="p266578112023"><a name="p266578112023"></a><a name="p266578112023"></a>vlan</p>
</td>
<td class="cellrowborder" valign="top" width="11.26%" headers="mcps1.2.5.1.2 "><p id="p21592892112023"><a name="p21592892112023"></a><a name="p21592892112023"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="17.84%" headers="mcps1.2.5.1.3 "><p id="p4193855112023"><a name="p4193855112023"></a><a name="p4193855112023"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="50.080000000000005%" headers="mcps1.2.5.1.4 "><p id="p4157954112023"><a name="p4157954112023"></a><a name="p4157954112023"></a>Specifies the pre-allocated VLAN to the hosted connection.</p>
</td>
</tr>
<tr id="row21368111958"><td class="cellrowborder" valign="top" width="20.82%" headers="mcps1.2.5.1.1 "><p id="p56574156112023"><a name="p56574156112023"></a><a name="p56574156112023"></a>charge_mode</p>
</td>
<td class="cellrowborder" valign="top" width="11.26%" headers="mcps1.2.5.1.2 "><p id="p19103944112023"><a name="p19103944112023"></a><a name="p19103944112023"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.84%" headers="mcps1.2.5.1.3 "><p id="p3915665112023"><a name="p3915665112023"></a><a name="p3915665112023"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="50.080000000000005%" headers="mcps1.2.5.1.4 "><p id="p68761049141015"><a name="p68761049141015"></a><a name="p68761049141015"></a>Specifies the billing mode. The value can be <strong id="b842352706153349"><a name="b842352706153349"></a><a name="b842352706153349"></a>prepayment</strong>, <strong id="b842352706153353"><a name="b842352706153353"></a><a name="b842352706153353"></a>bandwidth</strong>, or <strong id="b842352706153357"><a name="b842352706153357"></a><a name="b842352706153357"></a>traffic</strong>.</p>
</td>
</tr>
<tr id="row13082768154933"><td class="cellrowborder" valign="top" width="20.82%" headers="mcps1.2.5.1.1 "><p id="p36324518154942"><a name="p36324518154942"></a><a name="p36324518154942"></a>order_id</p>
</td>
<td class="cellrowborder" valign="top" width="11.26%" headers="mcps1.2.5.1.2 "><p id="p56604823154942"><a name="p56604823154942"></a><a name="p56604823154942"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.84%" headers="mcps1.2.5.1.3 "><p id="p21587982154942"><a name="p21587982154942"></a><a name="p21587982154942"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="50.080000000000005%" headers="mcps1.2.5.1.4 "><p id="p3796080154942"><a name="p3796080154942"></a><a name="p3796080154942"></a>Specifies the order number of a connection.</p>
</td>
</tr>
<tr id="row29968911154930"><td class="cellrowborder" valign="top" width="20.82%" headers="mcps1.2.5.1.1 "><p id="p15879398154942"><a name="p15879398154942"></a><a name="p15879398154942"></a>product_id</p>
</td>
<td class="cellrowborder" valign="top" width="11.26%" headers="mcps1.2.5.1.2 "><p id="p11162871154942"><a name="p11162871154942"></a><a name="p11162871154942"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.84%" headers="mcps1.2.5.1.3 "><p id="p31777360154942"><a name="p31777360154942"></a><a name="p31777360154942"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="50.080000000000005%" headers="mcps1.2.5.1.4 "><p id="p23829402154942"><a name="p23829402154942"></a><a name="p23829402154942"></a>Specifies the product ID corresponding to a connection order.</p>
</td>
</tr>
<tr id="row24943363212922"><td class="cellrowborder" valign="top" width="20.82%" headers="mcps1.2.5.1.1 "><p id="p12636115212955"><a name="p12636115212955"></a><a name="p12636115212955"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="11.26%" headers="mcps1.2.5.1.2 "><p id="p19656103212955"><a name="p19656103212955"></a><a name="p19656103212955"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.84%" headers="mcps1.2.5.1.3 "><p id="p8052318212955"><a name="p8052318212955"></a><a name="p8052318212955"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="50.080000000000005%" headers="mcps1.2.5.1.4 "><p id="p8311016203710"><a name="p8311016203710"></a><a name="p8311016203710"></a>Specifies the connection status.</p>
<p id="p2927466021328"><a name="p2927466021328"></a><a name="p2927466021328"></a>The value can be <strong id="b84235270617169"><a name="b84235270617169"></a><a name="b84235270617169"></a>ACTIVE</strong>, <strong id="b842352706171613"><a name="b842352706171613"></a><a name="b842352706171613"></a>DOWN</strong>, <strong id="b842352706171618"><a name="b842352706171618"></a><a name="b842352706171618"></a>BUILD</strong>, <strong id="b842352706171622"><a name="b842352706171622"></a><a name="b842352706171622"></a>ERROR</strong>, <strong id="b842352706171633"><a name="b842352706171633"></a><a name="b842352706171633"></a>PENDING_DELETE</strong>, <strong id="b842352706231627"><a name="b842352706231627"></a><a name="b842352706231627"></a>DELETED</strong>, <strong id="b842352706171637"><a name="b842352706171637"></a><a name="b842352706171637"></a>APPLY</strong>, <strong id="b842352706171640"><a name="b842352706171640"></a><a name="b842352706171640"></a>DENY</strong>, <strong id="b842352706171644"><a name="b842352706171644"></a><a name="b842352706171644"></a>PENDING_PAY</strong>, <strong id="b842352706171648"><a name="b842352706171648"></a><a name="b842352706171648"></a>PAID</strong>, <strong id="b842352706231650"><a name="b842352706231650"></a><a name="b842352706231650"></a>ORDERING</strong>, <strong id="b84235270615185"><a name="b84235270615185"></a><a name="b84235270615185"></a>ACCEPT,</strong> or <strong id="b842352706231656"><a name="b842352706231656"></a><a name="b842352706231656"></a>REJECTED</strong>.</p>
</td>
</tr>
<tr id="row59943627212941"><td class="cellrowborder" valign="top" width="20.82%" headers="mcps1.2.5.1.1 "><p id="p25408944212955"><a name="p25408944212955"></a><a name="p25408944212955"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="11.26%" headers="mcps1.2.5.1.2 "><p id="p47722852212955"><a name="p47722852212955"></a><a name="p47722852212955"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="17.84%" headers="mcps1.2.5.1.3 "><p id="p2012153212955"><a name="p2012153212955"></a><a name="p2012153212955"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="50.080000000000005%" headers="mcps1.2.5.1.4 "><p id="p29293435203715"><a name="p29293435203715"></a><a name="p29293435203715"></a>Specifies the administrative state of the connection.</p>
<p id="p895390621328"><a name="p895390621328"></a><a name="p895390621328"></a>The value can be <strong id="b842352706154840"><a name="b842352706154840"></a><a name="b842352706154840"></a>true</strong> or <strong id="b842352706154844"><a name="b842352706154844"></a><a name="b842352706154844"></a>false</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section14931696"></a>

[Table 3](#table50787760154022)  lists the response parameter.

**Table  3**  Response parameter

<a name="table50787760154022"></a>
<table><thead align="left"><tr id="row48608566154022"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.4.1.1"><p id="p44979764154022"><a name="p44979764154022"></a><a name="p44979764154022"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.2.4.1.2"><p id="p19482271154022"><a name="p19482271154022"></a><a name="p19482271154022"></a><strong id="b1529442006"><a name="b1529442006"></a><a name="b1529442006"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="42%" id="mcps1.2.4.1.3"><p id="p47904218154022"><a name="p47904218154022"></a><a name="p47904218154022"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row55036410154022"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="p28764198154022"><a name="p28764198154022"></a><a name="p28764198154022"></a>direct_connect</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.2 "><p id="p48198727154022"><a name="p48198727154022"></a><a name="p48198727154022"></a>Dictionary data structure</p>
</td>
<td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.4.1.3 "><p id="p14887047154022"><a name="p14887047154022"></a><a name="p14887047154022"></a>Specifies the <strong id="b84235270616488"><a name="b84235270616488"></a><a name="b84235270616488"></a>direct_connect</strong> object.</p>
</td>
</tr>
</tbody>
</table>

Description of field  **direct\_connect**

<a name="table31929956"></a>
<table><thead align="left"><tr id="row12454319"><th class="cellrowborder" valign="top" width="30%" id="mcps1.1.4.1.1"><p id="p2166929"><a name="p2166929"></a><a name="p2166929"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="27%" id="mcps1.1.4.1.2"><p id="p41303584"><a name="p41303584"></a><a name="p41303584"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="43%" id="mcps1.1.4.1.3"><p id="p7224675"><a name="p7224675"></a><a name="p7224675"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row48327783"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.4.1.1 "><p id="p2618796021374"><a name="p2618796021374"></a><a name="p2618796021374"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.2 "><p id="p1461720021374"><a name="p1461720021374"></a><a name="p1461720021374"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.4.1.3 "><p id="p3207700921374"><a name="p3207700921374"></a><a name="p3207700921374"></a>Specifies the connection ID.</p>
</td>
</tr>
<tr id="row3324189521359"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.4.1.1 "><p id="p42330775213632"><a name="p42330775213632"></a><a name="p42330775213632"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.2 "><p id="p21800648213632"><a name="p21800648213632"></a><a name="p21800648213632"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.4.1.3 "><p id="p31253263213632"><a name="p31253263213632"></a><a name="p31253263213632"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row66728889213524"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.4.1.1 "><p id="p54759239213632"><a name="p54759239213632"></a><a name="p54759239213632"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.2 "><p id="p23617166213632"><a name="p23617166213632"></a><a name="p23617166213632"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.4.1.3 "><p id="p6069654213632"><a name="p6069654213632"></a><a name="p6069654213632"></a>Specifies the connection name.</p>
</td>
</tr>
<tr id="row15439121213515"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.4.1.1 "><p id="p53086796213632"><a name="p53086796213632"></a><a name="p53086796213632"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.2 "><p id="p59471933213632"><a name="p59471933213632"></a><a name="p59471933213632"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.4.1.3 "><p id="p31024005213632"><a name="p31024005213632"></a><a name="p31024005213632"></a>Provides supplementary information about the connection.</p>
</td>
</tr>
<tr id="row50661489213528"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.4.1.1 "><p id="p34534799213632"><a name="p34534799213632"></a><a name="p34534799213632"></a>port_type</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.2 "><p id="p5532130213632"><a name="p5532130213632"></a><a name="p5532130213632"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.4.1.3 "><p id="p48559645213632"><a name="p48559645213632"></a><a name="p48559645213632"></a>Specifies the type of the port used by the connection. The value can be <strong id="b1989512592"><a name="b1989512592"></a><a name="b1989512592"></a>1G</strong> or <strong id="b191632175"><a name="b191632175"></a><a name="b191632175"></a>10G</strong>.</p>
</td>
</tr>
<tr id="row5846484213534"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.4.1.1 "><p id="p55551229213632"><a name="p55551229213632"></a><a name="p55551229213632"></a>bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.2 "><p id="p16783167213632"><a name="p16783167213632"></a><a name="p16783167213632"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.4.1.3 "><p id="p63052895213632"><a name="p63052895213632"></a><a name="p63052895213632"></a>Specifies the connection bandwidth (unit: Mbit/s).</p>
</td>
</tr>
<tr id="row49999429213538"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.4.1.1 "><p id="p35507620213632"><a name="p35507620213632"></a><a name="p35507620213632"></a>location</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.2 "><p id="p29337441213632"><a name="p29337441213632"></a><a name="p29337441213632"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.4.1.3 "><p id="p13353953213632"><a name="p13353953213632"></a><a name="p13353953213632"></a>Specifies the connection access location.</p>
</td>
</tr>
<tr id="row62607450213545"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.4.1.1 "><p id="p61083552213632"><a name="p61083552213632"></a><a name="p61083552213632"></a>peer_location</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.2 "><p id="p12557904213632"><a name="p12557904213632"></a><a name="p12557904213632"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.4.1.3 "><p id="p7267427213632"><a name="p7267427213632"></a><a name="p7267427213632"></a>Specifies the physical location of the peer device accessed by the connection. The value can be a street, city, and province, or an IDC.</p>
</td>
</tr>
<tr id="row41934009213550"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.4.1.1 "><p id="p14049627213632"><a name="p14049627213632"></a><a name="p14049627213632"></a>device_id</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.2 "><p id="p63445678213632"><a name="p63445678213632"></a><a name="p63445678213632"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.4.1.3 "><p id="p28938027213632"><a name="p28938027213632"></a><a name="p28938027213632"></a>Specifies the gateway device ID of the connection.</p>
</td>
</tr>
<tr id="row25822170213553"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.4.1.1 "><p id="p2078158213632"><a name="p2078158213632"></a><a name="p2078158213632"></a>interface_name</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.2 "><p id="p47522281213632"><a name="p47522281213632"></a><a name="p47522281213632"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.4.1.3 "><p id="p66449147213632"><a name="p66449147213632"></a><a name="p66449147213632"></a>Specifies the name of the interface accessed by the connection.</p>
</td>
</tr>
<tr id="row5375448520281"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.4.1.1 "><p id="p4564411202825"><a name="p4564411202825"></a><a name="p4564411202825"></a>redundant_id</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.2 "><p id="p34173036202825"><a name="p34173036202825"></a><a name="p34173036202825"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.4.1.3 "><p id="p65689804202825"><a name="p65689804202825"></a><a name="p65689804202825"></a>Specifies the ID of the redundant connection using the same gateway.</p>
</td>
</tr>
<tr id="row318971213557"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.4.1.1 "><p id="p12907438213632"><a name="p12907438213632"></a><a name="p12907438213632"></a>provider</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.2 "><p id="p32214012213632"><a name="p32214012213632"></a><a name="p32214012213632"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.4.1.3 "><p id="p29079571213632"><a name="p29079571213632"></a><a name="p29079571213632"></a>Specifies the connection provider.</p>
</td>
</tr>
<tr id="row41217866213559"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.4.1.1 "><p id="p23411026145150"><a name="p23411026145150"></a><a name="p23411026145150"></a>provider_status</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.2 "><p id="p56606343145150"><a name="p56606343145150"></a><a name="p56606343145150"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.4.1.3 "><p id="p51755739145150"><a name="p51755739145150"></a><a name="p51755739145150"></a>Specifies the status of the provider's connection. The value can be <strong id="b942446070"><a name="b942446070"></a><a name="b942446070"></a>ACTIVE</strong> or <strong id="b802714008"><a name="b802714008"></a><a name="b802714008"></a>DOWN</strong>.</p>
</td>
</tr>
<tr id="row66457087113744"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.4.1.1 "><p id="p39573682113840"><a name="p39573682113840"></a><a name="p39573682113840"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.2 "><p id="p51351654113840"><a name="p51351654113840"></a><a name="p51351654113840"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.4.1.3 "><p id="p469315375815"><a name="p469315375815"></a><a name="p469315375815"></a>Specifies the connection type. The value can be <strong id="b1873552927"><a name="b1873552927"></a><a name="b1873552927"></a>hosted</strong>.</p>
</td>
</tr>
<tr id="row65870323113739"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.4.1.1 "><p id="p29166812113840"><a name="p29166812113840"></a><a name="p29166812113840"></a>hosting_id</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.2 "><p id="p13701604113840"><a name="p13701604113840"></a><a name="p13701604113840"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.4.1.3 "><p id="p37456908113840"><a name="p37456908113840"></a><a name="p37456908113840"></a>Specifies the ID of the hosting connection mapped to the hosted connection.</p>
</td>
</tr>
<tr id="row12695056113736"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.4.1.1 "><p id="p59887593113840"><a name="p59887593113840"></a><a name="p59887593113840"></a>vlan</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.2 "><p id="p19056878113840"><a name="p19056878113840"></a><a name="p19056878113840"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.4.1.3 "><p id="p8364989113840"><a name="p8364989113840"></a><a name="p8364989113840"></a>Specifies the pre-allocated VLAN to the hosted connection.</p>
</td>
</tr>
<tr id="row24770090113731"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.4.1.1 "><p id="p51377985113840"><a name="p51377985113840"></a><a name="p51377985113840"></a>charge_mode</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.2 "><p id="p867286113840"><a name="p867286113840"></a><a name="p867286113840"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.4.1.3 "><p id="p53123906113840"><a name="p53123906113840"></a><a name="p53123906113840"></a>Specifies the billing mode. The value can be <strong id="b1029543246"><a name="b1029543246"></a><a name="b1029543246"></a>prepayment</strong>, <strong id="b230962626"><a name="b230962626"></a><a name="b230962626"></a>bandwidth</strong>, or <strong id="b931451615"><a name="b931451615"></a><a name="b931451615"></a>traffic</strong>.</p>
<p id="p1329472151219"><a name="p1329472151219"></a><a name="p1329472151219"></a>Its value is left blank by default.</p>
</td>
</tr>
<tr id="row39466389113733"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.4.1.1 "><p id="p5513004113840"><a name="p5513004113840"></a><a name="p5513004113840"></a>apply_time</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.2 "><p id="p43900170113840"><a name="p43900170113840"></a><a name="p43900170113840"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.4.1.3 "><p id="p64883444113840"><a name="p64883444113840"></a><a name="p64883444113840"></a>Specifies the time when the connection is applied for.</p>
</td>
</tr>
<tr id="row43420664113728"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.4.1.1 "><p id="p55390672113840"><a name="p55390672113840"></a><a name="p55390672113840"></a>create_time</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.2 "><p id="p57459409113840"><a name="p57459409113840"></a><a name="p57459409113840"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.4.1.3 "><p id="p40696141113840"><a name="p40696141113840"></a><a name="p40696141113840"></a>Specifies the time when the connection is created.</p>
</td>
</tr>
<tr id="row1545172521215"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.4.1.1 "><p id="p125451025111216"><a name="p125451025111216"></a><a name="p125451025111216"></a>delete_time</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.2 "><p id="p895805311123"><a name="p895805311123"></a><a name="p895805311123"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.4.1.3 "><p id="p14966653201217"><a name="p14966653201217"></a><a name="p14966653201217"></a>Specifies the time when the connection is deleted.</p>
</td>
</tr>
<tr id="row61781628155015"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.4.1.1 "><p id="p61852912155018"><a name="p61852912155018"></a><a name="p61852912155018"></a>order_id</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.2 "><p id="p44029946155018"><a name="p44029946155018"></a><a name="p44029946155018"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.4.1.3 "><p id="p43926908155018"><a name="p43926908155018"></a><a name="p43926908155018"></a>Specifies the order number of a connection.</p>
</td>
</tr>
<tr id="row4132540155011"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.4.1.1 "><p id="p11787873155018"><a name="p11787873155018"></a><a name="p11787873155018"></a>product_id</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.2 "><p id="p15293679155018"><a name="p15293679155018"></a><a name="p15293679155018"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.4.1.3 "><p id="p14077379155018"><a name="p14077379155018"></a><a name="p14077379155018"></a>Specifies the product ID corresponding to a connection order.</p>
</td>
</tr>
<tr id="row3470610321362"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.4.1.1 "><p id="p37955181145150"><a name="p37955181145150"></a><a name="p37955181145150"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.2 "><p id="p28127726145150"><a name="p28127726145150"></a><a name="p28127726145150"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.4.1.3 "><p id="p63582831145150"><a name="p63582831145150"></a><a name="p63582831145150"></a>Specifies the connection status. The value can be <strong id="b1430420579"><a name="b1430420579"></a><a name="b1430420579"></a>ACTIVE</strong>, <strong id="b1008675173"><a name="b1008675173"></a><a name="b1008675173"></a>DOWN</strong>, <strong id="b182097766"><a name="b182097766"></a><a name="b182097766"></a>BUILD</strong>, <strong id="b320889391"><a name="b320889391"></a><a name="b320889391"></a>ERROR</strong>, <strong id="b573557709231737"><a name="b573557709231737"></a><a name="b573557709231737"></a>PENDING_DELETE</strong>, <strong id="b810642512231737"><a name="b810642512231737"></a><a name="b810642512231737"></a>DELETED</strong>, <strong id="b17872564231737"><a name="b17872564231737"></a><a name="b17872564231737"></a>APPLY</strong>, <strong id="b1765160533231737"><a name="b1765160533231737"></a><a name="b1765160533231737"></a>DENY</strong>, <strong id="b1723423809231737"><a name="b1723423809231737"></a><a name="b1723423809231737"></a>PENDING_PAY</strong>, <strong id="b733428447231737"><a name="b733428447231737"></a><a name="b733428447231737"></a>PAID</strong>, <strong id="b1888084103231737"><a name="b1888084103231737"></a><a name="b1888084103231737"></a>ORDERING</strong>, <strong id="b842352706151915"><a name="b842352706151915"></a><a name="b842352706151915"></a>ACCEPT</strong>, or <strong id="b1504845468231737"><a name="b1504845468231737"></a><a name="b1504845468231737"></a>REJECTED</strong>.</p>
</td>
</tr>
<tr id="row5737311521368"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.4.1.1 "><p id="p64345853213632"><a name="p64345853213632"></a><a name="p64345853213632"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.2 "><p id="p42048472213632"><a name="p42048472213632"></a><a name="p42048472213632"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.4.1.3 "><p id="p21010737202946"><a name="p21010737202946"></a><a name="p21010737202946"></a>Specifies the administrative state of the connection.</p>
<p id="p65467559213632"><a name="p65467559213632"></a><a name="p65467559213632"></a>The value can be <strong id="b2472364020194"><a name="b2472364020194"></a><a name="b2472364020194"></a>true</strong> or <strong id="b2118616920194"><a name="b2118616920194"></a><a name="b2118616920194"></a>false</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section38241653113834"></a>

-   Example request

    ```
    POST /v2.0/dcaas/direct-connects 
    { 
        "direct_connect" : { 
            "name" : "direct connect1", 
            "port_type" : "10G", 
            "bandwidth" : 100, 
            "location" : "Biere", 
            "device_id" : "172.16.40.2", 
            "provider" : "OTC" 
        } 
    } 
    ```


-   Example response

    ```
    {
        "direct_connect" : {
            "bandwidth" : 100,
            "create_time": "2018-10-19 09:53:26.389556", 
            "port_type" : "10G",
            "id" : "6ecd9cf3-ca64-46c7-863f-f2eb1b9e838a",
            "apply_time": "2018-10-19 09:53:26.389556", 
            "peer_location": "",
            "delete_time": null, 
            "location" : "Biere", 
            "provider" : "OTC"
            "interface_name": "Eth-Trunk2", 
            "type": "standard",
            "status": "BUILD",
            "description" : "",
            "provider_status": "ACTIVE", "order_id": "", "vlan": null,
            "device_id" : "172.16.40.2",
            "name" : "direct connect1", 
            "admin_state_up": true, 
            "tenant_id" : "6fbe9263116a4b68818cf1edce16bc4f",
            "redundant_id": null, "hosting_id": null, "product_id": "", "charge_mode": ""
        }
    }
    ```


## Returned Value<a name="section6416329132915"></a>

For details, see section  [Common Returned Values](common-returned-values.md).

