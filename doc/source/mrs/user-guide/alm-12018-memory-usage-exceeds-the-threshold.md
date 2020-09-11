# ALM-12018 Memory Usage Exceeds the Threshold<a name="EN-US_TOPIC_0125375965"></a>

## Description<a name="sa54ca492bf31487cb2205eb89b35e059"></a>

The system checks the memory usage every 30 seconds and compares it with the threshold. This alarm is generated when the host memory usage exceeds the threshold and is cleared when it is less than or equal to 90% of the threshold.

## Attribute<a name="s86b65e71c85d42bd87643e04f73b25dc"></a>

<a name="tdc6658845a4e4a9ba26b7eb0ab9a8fe8"></a>
<table><thead align="left"><tr id="r09417ecf86e64fd18856ad1371687935"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="ae4f2f7e65a444ad3b695e1b5830708a0"><a name="ae4f2f7e65a444ad3b695e1b5830708a0"></a><a name="ae4f2f7e65a444ad3b695e1b5830708a0"></a><strong id="a30737408805a4d9598b59f38003ece16"><a name="a30737408805a4d9598b59f38003ece16"></a><a name="a30737408805a4d9598b59f38003ece16"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="a5e7eaefec5984cc29a1e373158b400cb"><a name="a5e7eaefec5984cc29a1e373158b400cb"></a><a name="a5e7eaefec5984cc29a1e373158b400cb"></a><strong id="a5986db90db7944209e829266a93b9876"><a name="a5986db90db7944209e829266a93b9876"></a><a name="a5986db90db7944209e829266a93b9876"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="a7fd3b3bc3970494a8007c38b7a041a83"><a name="a7fd3b3bc3970494a8007c38b7a041a83"></a><a name="a7fd3b3bc3970494a8007c38b7a041a83"></a><strong id="a87a03f9492464af0b5d8c1021ab8e097"><a name="a87a03f9492464af0b5d8c1021ab8e097"></a><a name="a87a03f9492464af0b5d8c1021ab8e097"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r7899bd072b4144e2a08730899d366ef2"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="a094883d5d3d041a1b093095463733cda"><a name="a094883d5d3d041a1b093095463733cda"></a><a name="a094883d5d3d041a1b093095463733cda"></a>12018</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="abc87104c98274f55bbced9c774902648"><a name="abc87104c98274f55bbced9c774902648"></a><a name="abc87104c98274f55bbced9c774902648"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="ac283e5b2a00d4528817f5fcc083f6c93"><a name="ac283e5b2a00d4528817f5fcc083f6c93"></a><a name="ac283e5b2a00d4528817f5fcc083f6c93"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s75b62234a2444c748c8b119546cd3756"></a>

<a name="t83f8758f86434f15acc1b963024ef8d2"></a>
<table><thead align="left"><tr id="rb6a61f6f754b46248b6ce76d57561a35"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="a88ef38a5178e456ab83bfcae9dbe279d"><a name="a88ef38a5178e456ab83bfcae9dbe279d"></a><a name="a88ef38a5178e456ab83bfcae9dbe279d"></a><strong id="a461dc0d0acf34a3b84fe26ba9508ff5c"><a name="a461dc0d0acf34a3b84fe26ba9508ff5c"></a><a name="a461dc0d0acf34a3b84fe26ba9508ff5c"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="abbc987c059044805bf1b8e6836f837d1"><a name="abbc987c059044805bf1b8e6836f837d1"></a><a name="abbc987c059044805bf1b8e6836f837d1"></a><strong id="a86e2c56c0ec347f78fe1a5387850dc52"><a name="a86e2c56c0ec347f78fe1a5387850dc52"></a><a name="a86e2c56c0ec347f78fe1a5387850dc52"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r8fcd1b4c115b4a79b2e0996cd76c0295"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a6ad16161495c496fada432d1745f6f8d"><a name="a6ad16161495c496fada432d1745f6f8d"></a><a name="a6ad16161495c496fada432d1745f6f8d"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a777c060666a640dfb4443b956c0777e0"><a name="a777c060666a640dfb4443b956c0777e0"></a><a name="a777c060666a640dfb4443b956c0777e0"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="rafa38a4338d8452cab63d1bff9d8ece9"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a6ef26640a98d48548029e3729120ac07"><a name="a6ef26640a98d48548029e3729120ac07"></a><a name="a6ef26640a98d48548029e3729120ac07"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a7b9868de7f5c4d028778543af9efac9f"><a name="a7b9868de7f5c4d028778543af9efac9f"></a><a name="a7b9868de7f5c4d028778543af9efac9f"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="r91c1a5f11cdf48fc90a713b8e46054cd"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a9280f8763d7340e2a015316aea071586"><a name="a9280f8763d7340e2a015316aea071586"></a><a name="a9280f8763d7340e2a015316aea071586"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a68ccaa47ae764ec2a9b22221bceb0b63"><a name="a68ccaa47ae764ec2a9b22221bceb0b63"></a><a name="a68ccaa47ae764ec2a9b22221bceb0b63"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="r24e3d5f51c554ec0b0bdd6fd01fa87f9"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ac6a221dbd76c49cf851b72085c7f73c8"><a name="ac6a221dbd76c49cf851b72085c7f73c8"></a><a name="ac6a221dbd76c49cf851b72085c7f73c8"></a>Trigger Condition</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a568327c7760443b09e4d1476c2eca827"><a name="a568327c7760443b09e4d1476c2eca827"></a><a name="a568327c7760443b09e4d1476c2eca827"></a>Generates an alarm when the actual indicator value exceeds the specified threshold.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="sb398604bdf254939a614a89b9465e392"></a>

Service processes respond slowly or become unavailable.

## Possible Causes<a name="sb050ba28786f41cd954995e06bb939e7"></a>

Memory configuration does not meet service requirements. As a result, the memory usage reaches the upper limit.

## Procedure<a name="s275a6f36091f49c89511fce364b4a378"></a>

1.  Expand the system capacity.
    1.  In the alarm list on MRS Manager, locate the row that contains the alarm, and view the IP address of the alarm host in the alarm details.
    2.  Log in to the alarm node.
    3.  Run the  **free -m | grep Mem\\:** **| awk '\{printf\("%s,", \($3-$6-$7\) \* 100 / $2\)\}'**  command to check the system memory usage.
    4.  If the memory usage exceeds the threshold, expand the memory capacity.
    5.  Wait 5 minutes and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [2](#lb2a190224e14427ca92c6a3f4dc4d1a7).

2.  <a name="lb2a190224e14427ca92c6a3f4dc4d1a7"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## **Related Information**<a name="s131af69fdaa5435cb9fbef62f3f18cef"></a>

N/A

