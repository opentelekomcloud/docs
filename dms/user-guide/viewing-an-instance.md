# Viewing an Instance<a name="EN-US_TOPIC_0143117188"></a>

## Scenario<a name="section21574462"></a>

View detailed information about a Kafka premium instance on the DMS console, for example, the connection address and port number for accessing the instance.

## Prerequisites<a name="section59952436"></a>

A Kafka premium instance has been created.

## Procedure<a name="section1860982374010"></a>

1.  Log in to the management console.
2.  Choose  **Application**  \>  **Distributed Message Service**  to open the DMS console.
3.  In the navigation pane, choose  **Kafka Premium**.
4.  Search for a Kafka premium instance by status and name.  [Table 1](#table5086721717534)  describes the various possible statuses of a Kafka premium instance.

    **Table  1**  Kafka premium instance status description

    <a name="table5086721717534"></a>
    <table><thead align="left"><tr id="row4878914717534"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.3.1.1"><p id="p50270420175321"><a name="p50270420175321"></a><a name="p50270420175321"></a><strong id="b5528115515254"><a name="b5528115515254"></a><a name="b5528115515254"></a>Status</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="83%" id="mcps1.2.3.1.2"><p id="p51272037175321"><a name="p51272037175321"></a><a name="p51272037175321"></a><strong id="b411817918264"><a name="b411817918264"></a><a name="b411817918264"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4409498617534"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.3.1.1 "><p id="p5195001718130"><a name="p5195001718130"></a><a name="p5195001718130"></a>Creating</p>
    </td>
    <td class="cellrowborder" valign="top" width="83%" headers="mcps1.2.3.1.2 "><p id="p6525251518130"><a name="p6525251518130"></a><a name="p6525251518130"></a>The instance is being created.</p>
    </td>
    </tr>
    <tr id="row4964581717534"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.3.1.1 "><p id="p3431187918130"><a name="p3431187918130"></a><a name="p3431187918130"></a>Running</p>
    </td>
    <td class="cellrowborder" valign="top" width="83%" headers="mcps1.2.3.1.2 "><p id="p3711473418130"><a name="p3711473418130"></a><a name="p3711473418130"></a>The instance is running properly.</p>
    <p id="p6559715218130"><a name="p6559715218130"></a><a name="p6559715218130"></a>Only Kafka premium instances in the <strong id="b1998783912610"><a name="b1998783912610"></a><a name="b1998783912610"></a>Running</strong> state can provide the DMS Kafka premium service.</p>
    </td>
    </tr>
    <tr id="row8089014121228"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.3.1.1 "><p id="p1022935121239"><a name="p1022935121239"></a><a name="p1022935121239"></a>Faulty</p>
    </td>
    <td class="cellrowborder" valign="top" width="83%" headers="mcps1.2.3.1.2 "><p id="p593735121239"><a name="p593735121239"></a><a name="p593735121239"></a>The instance is not running properly.</p>
    </td>
    </tr>
    <tr id="row23496423121248"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.3.1.1 "><p id="p549840112131"><a name="p549840112131"></a><a name="p549840112131"></a>Starting</p>
    </td>
    <td class="cellrowborder" valign="top" width="83%" headers="mcps1.2.3.1.2 "><p id="p3755454112131"><a name="p3755454112131"></a><a name="p3755454112131"></a>The instance is being started.</p>
    </td>
    </tr>
    <tr id="row5150934512136"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.3.1.1 "><p id="p43939024121312"><a name="p43939024121312"></a><a name="p43939024121312"></a>Restarting</p>
    </td>
    <td class="cellrowborder" valign="top" width="83%" headers="mcps1.2.3.1.2 "><p id="p51371030121312"><a name="p51371030121312"></a><a name="p51371030121312"></a>The instance is being restarted.</p>
    </td>
    </tr>
    <tr id="row11207195119405"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.3.1.1 "><p id="p172086516401"><a name="p172086516401"></a><a name="p172086516401"></a>Resizing</p>
    </td>
    <td class="cellrowborder" valign="top" width="83%" headers="mcps1.2.3.1.2 "><p id="p16599145113113"><a name="p16599145113113"></a><a name="p16599145113113"></a>Public access is being modified for the instance.</p>
    </td>
    </tr>
    <tr id="row72081651134015"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.3.1.1 "><p id="p420815120409"><a name="p420815120409"></a><a name="p420815120409"></a>Resizing failed</p>
    </td>
    <td class="cellrowborder" valign="top" width="83%" headers="mcps1.2.3.1.2 "><p id="p48321911203313"><a name="p48321911203313"></a><a name="p48321911203313"></a>Public access failed to be modified for the instance.</p>
    </td>
    </tr>
    </tbody>
    </table>

5.  Click the name of the chosen Kafka premium instance and view detailed information about the instance on the displayed page.

