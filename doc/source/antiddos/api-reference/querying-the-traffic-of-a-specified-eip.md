# Querying the Traffic of a Specified EIP<a name="antiddos_02_0025"></a>

## Function<a name="section37718351"></a>

This API allows you to query the traffic of a specified EIP in the last 24 hours. Traffic is detected in five-minute intervals.

## URI<a name="section3920839"></a>

-   URI format

    GET /v1/\{project\_id\}/antiddos/\{floating\_ip\_id\}/daily

-   Parameter description

    <a name="table61552586"></a>
    <table><thead align="left"><tr id="row9021289"><th class="cellrowborder" valign="top" width="25.28747125287471%" id="mcps1.1.5.1.1"><p id="p59635795"><a name="p59635795"></a><a name="p59635795"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.167683231676826%" id="mcps1.1.5.1.2"><p id="p65770110"><a name="p65770110"></a><a name="p65770110"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.798220177982195%" id="mcps1.1.5.1.3"><p id="p25778706"><a name="p25778706"></a><a name="p25778706"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.74662533746625%" id="mcps1.1.5.1.4"><p id="p7700405"><a name="p7700405"></a><a name="p7700405"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row19753106"><td class="cellrowborder" valign="top" width="25.28747125287471%" headers="mcps1.1.5.1.1 "><p id="p56497743"><a name="p56497743"></a><a name="p56497743"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.167683231676826%" headers="mcps1.1.5.1.2 "><p id="p12914452"><a name="p12914452"></a><a name="p12914452"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.798220177982195%" headers="mcps1.1.5.1.3 "><p id="p39437706"><a name="p39437706"></a><a name="p39437706"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.74662533746625%" headers="mcps1.1.5.1.4 "><p id="p40337624"><a name="p40337624"></a><a name="p40337624"></a>A user's ID</p>
    </td>
    </tr>
    <tr id="row27494304"><td class="cellrowborder" valign="top" width="25.28747125287471%" headers="mcps1.1.5.1.1 "><p id="p12446183"><a name="p12446183"></a><a name="p12446183"></a>floating_ip_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.167683231676826%" headers="mcps1.1.5.1.2 "><p id="p1507865"><a name="p1507865"></a><a name="p1507865"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.798220177982195%" headers="mcps1.1.5.1.3 "><p id="p55028256"><a name="p55028256"></a><a name="p55028256"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.74662533746625%" headers="mcps1.1.5.1.4 "><p id="p28103780"><a name="p28103780"></a><a name="p28103780"></a>ID corresponding to the EIP of a user</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section35287558"></a>

-   Request example

    ```
    GET /v1/67641fe6886f43fcb78edbbf0ad0b99f/antiddos/1df977c2-fdc6-4483-bc1c-ba46829f57b8/daily
    ```


## Response<a name="section49152572"></a>

-   Element description

    <a name="table52988145"></a>
    <table><thead align="left"><tr id="row52657628"><th class="cellrowborder" valign="top" width="18.51185118511851%" id="mcps1.1.4.1.1"><p id="p37409505"><a name="p37409505"></a><a name="p37409505"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.003300330033%" id="mcps1.1.4.1.2"><p id="p10271087"><a name="p10271087"></a><a name="p10271087"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="48.484848484848484%" id="mcps1.1.4.1.3"><p id="p26651693"><a name="p26651693"></a><a name="p26651693"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row11303491"><td class="cellrowborder" valign="top" width="18.51185118511851%" headers="mcps1.1.4.1.1 "><p id="p43167578"><a name="p43167578"></a><a name="p43167578"></a>data</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.003300330033%" headers="mcps1.1.4.1.2 "><p id="p6912921"><a name="p6912921"></a><a name="p6912921"></a>Data structure</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.1.4.1.3 "><p id="p23075753"><a name="p23075753"></a><a name="p23075753"></a>Traffic in the last 24 hours</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Data structure description of  **data**

    <a name="table2422875"></a>
    <table><thead align="left"><tr id="row43246702"><th class="cellrowborder" valign="top" width="23.09%" id="mcps1.1.5.1.1"><p id="p13321984"><a name="p13321984"></a><a name="p13321984"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.029999999999998%" id="mcps1.1.5.1.2"><p id="p5338943"><a name="p5338943"></a><a name="p5338943"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="10.979999999999999%" id="mcps1.1.5.1.3"><p id="p29801234"><a name="p29801234"></a><a name="p29801234"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.9%" id="mcps1.1.5.1.4"><p id="p65089762"><a name="p65089762"></a><a name="p65089762"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row37779350"><td class="cellrowborder" valign="top" width="23.09%" headers="mcps1.1.5.1.1 "><p id="p40228503"><a name="p40228503"></a><a name="p40228503"></a>period_start</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.029999999999998%" headers="mcps1.1.5.1.2 "><p id="p37283276"><a name="p37283276"></a><a name="p37283276"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.979999999999999%" headers="mcps1.1.5.1.3 "><p id="p46493"><a name="p46493"></a><a name="p46493"></a>Long integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.9%" headers="mcps1.1.5.1.4 "><p id="p3766004"><a name="p3766004"></a><a name="p3766004"></a>Start time</p>
    </td>
    </tr>
    <tr id="row33894036"><td class="cellrowborder" valign="top" width="23.09%" headers="mcps1.1.5.1.1 "><p id="p61062380"><a name="p61062380"></a><a name="p61062380"></a>bps_in</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.029999999999998%" headers="mcps1.1.5.1.2 "><p id="p47105724"><a name="p47105724"></a><a name="p47105724"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.979999999999999%" headers="mcps1.1.5.1.3 "><p id="p4101901152217"><a name="p4101901152217"></a><a name="p4101901152217"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.9%" headers="mcps1.1.5.1.4 "><p id="p52485536172447"><a name="p52485536172447"></a><a name="p52485536172447"></a>Inbound traffic (bit/s)</p>
    </td>
    </tr>
    <tr id="row17737502"><td class="cellrowborder" valign="top" width="23.09%" headers="mcps1.1.5.1.1 "><p id="p27451543"><a name="p27451543"></a><a name="p27451543"></a>bps_attack</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.029999999999998%" headers="mcps1.1.5.1.2 "><p id="p8982509"><a name="p8982509"></a><a name="p8982509"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.979999999999999%" headers="mcps1.1.5.1.3 "><p id="p51325772152221"><a name="p51325772152221"></a><a name="p51325772152221"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.9%" headers="mcps1.1.5.1.4 "><p id="p12659789"><a name="p12659789"></a><a name="p12659789"></a>Attack traffic (bit/s)</p>
    </td>
    </tr>
    <tr id="row46829245"><td class="cellrowborder" valign="top" width="23.09%" headers="mcps1.1.5.1.1 "><p id="p35072497"><a name="p35072497"></a><a name="p35072497"></a>total_bps</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.029999999999998%" headers="mcps1.1.5.1.2 "><p id="p22300038"><a name="p22300038"></a><a name="p22300038"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.979999999999999%" headers="mcps1.1.5.1.3 "><p id="p29869642152225"><a name="p29869642152225"></a><a name="p29869642152225"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.9%" headers="mcps1.1.5.1.4 "><p id="p13230834"><a name="p13230834"></a><a name="p13230834"></a>Total traffic</p>
    </td>
    </tr>
    <tr id="row51968642"><td class="cellrowborder" valign="top" width="23.09%" headers="mcps1.1.5.1.1 "><p id="p48710492"><a name="p48710492"></a><a name="p48710492"></a>pps_in</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.029999999999998%" headers="mcps1.1.5.1.2 "><p id="p53235770"><a name="p53235770"></a><a name="p53235770"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.979999999999999%" headers="mcps1.1.5.1.3 "><p id="p10560569152228"><a name="p10560569152228"></a><a name="p10560569152228"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.9%" headers="mcps1.1.5.1.4 "><p id="p45362212"><a name="p45362212"></a><a name="p45362212"></a>Inbound packet rate (number of packets per second)</p>
    </td>
    </tr>
    <tr id="row5606727"><td class="cellrowborder" valign="top" width="23.09%" headers="mcps1.1.5.1.1 "><p id="p51491712"><a name="p51491712"></a><a name="p51491712"></a>pps_attack</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.029999999999998%" headers="mcps1.1.5.1.2 "><p id="p10079105"><a name="p10079105"></a><a name="p10079105"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.979999999999999%" headers="mcps1.1.5.1.3 "><p id="p1965784152232"><a name="p1965784152232"></a><a name="p1965784152232"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.9%" headers="mcps1.1.5.1.4 "><p id="p26779645"><a name="p26779645"></a><a name="p26779645"></a>Attack packet rate (number of packets per second)</p>
    </td>
    </tr>
    <tr id="row39690219"><td class="cellrowborder" valign="top" width="23.09%" headers="mcps1.1.5.1.1 "><p id="p60791181"><a name="p60791181"></a><a name="p60791181"></a>total_pps</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.029999999999998%" headers="mcps1.1.5.1.2 "><p id="p25138652"><a name="p25138652"></a><a name="p25138652"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.979999999999999%" headers="mcps1.1.5.1.3 "><p id="p27969958152235"><a name="p27969958152235"></a><a name="p27969958152235"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.9%" headers="mcps1.1.5.1.4 "><p id="p48219807"><a name="p48219807"></a><a name="p48219807"></a>Total packet rate</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    {"data": [ 
          { 
          "period_start": 1472713370609, 
          "bps_in": 0, 
          "bps_attack": 0, 
          "total_bps": 0, 
          "pps_in": 0, 
          "pps_attack": 0, 
          "total_pps": 0 
       }, 
       
    
       ...
    
    
          { 
          "period_start": 1472713670609, 
          "bps_in": 0, 
          "bps_attack": 0, 
          "total_bps": 0, 
          "pps_in": 0, 
          "pps_attack": 0, 
          "total_pps": 0 
       }] 
    }
    ```


## Returned Value<a name="section39719970"></a>

See  [Status Code](status-code.md).

