# Key Pair and Password<a name="EN-US_TOPIC_0140735214"></a>

## What Is a Key Pair?<a name="section131153585615"></a>

A key pair, or SSH key pair, is an authentication method for logging in to Linux instances remotely. A key pair is generated using an encryption algorithm. It contains a public key which is open to the public and a private key which is reserved for you. The public key is used to encrypt data \(for example, a password\), and the private key is used to decrypt the data.

The cloud platform stores the public key, and you need to store the private key. Anyone with your private key can decrypt your login information. Therefore, it is important that you keep your private key secure.

## Advantages<a name="section11136322132315"></a>

The key pair is more secure and convenient than the username/password method.

**Table  1**  Comparison between the key pair and username/password

<a name="table310419771318"></a>
<table><thead align="left"><tr id="row710518710136"><th class="cellrowborder" valign="top" width="23.22232223222322%" id="mcps1.2.4.1.1"><p id="p10105117151319"><a name="p10105117151319"></a><a name="p10105117151319"></a>Item</p>
</th>
<th class="cellrowborder" valign="top" width="35.31353135313531%" id="mcps1.2.4.1.2"><p id="p18105278138"><a name="p18105278138"></a><a name="p18105278138"></a>Key Pair</p>
</th>
<th class="cellrowborder" valign="top" width="41.46414641464147%" id="mcps1.2.4.1.3"><p id="p110515751320"><a name="p110515751320"></a><a name="p110515751320"></a>Username and Password</p>
</th>
</tr>
</thead>
<tbody><tr id="row510513714134"><td class="cellrowborder" valign="top" width="23.22232223222322%" headers="mcps1.2.4.1.1 "><p id="p1810527101311"><a name="p1810527101311"></a><a name="p1810527101311"></a>Security</p>
</td>
<td class="cellrowborder" valign="top" width="35.31353135313531%" headers="mcps1.2.4.1.2 "><a name="ul09081258171613"></a><a name="ul09081258171613"></a><ul id="ul09081258171613"><li>More secure than the password and free from brute-force attacks</li><li>The private key cannot be derived from the public key.</li></ul>
</td>
<td class="cellrowborder" valign="top" width="41.46414641464147%" headers="mcps1.2.4.1.3 "><p id="p1910620715133"><a name="p1910620715133"></a><a name="p1910620715133"></a>Poor security</p>
</td>
</tr>
<tr id="row7106573132"><td class="cellrowborder" valign="top" width="23.22232223222322%" headers="mcps1.2.4.1.1 "><p id="p1110667191319"><a name="p1110667191319"></a><a name="p1110667191319"></a>Convenience</p>
</td>
<td class="cellrowborder" valign="top" width="35.31353135313531%" headers="mcps1.2.4.1.2 "><p id="p31065716137"><a name="p31065716137"></a><a name="p31065716137"></a>Simultaneous login to a large number of Linux instances, simplifying management</p>
</td>
<td class="cellrowborder" valign="top" width="41.46414641464147%" headers="mcps1.2.4.1.3 "><p id="p1010618720136"><a name="p1010618720136"></a><a name="p1010618720136"></a>Login to only one Linux instance at one time, making batch maintenance unavailable</p>
</td>
</tr>
</tbody>
</table>

## Restrictions<a name="section1283812457235"></a>

-   Only Linux instances support the key pair.
-   Only RSA key pairs are supported. A key pair can contain 1024, 2048, or 4096 characters.
-   A Linux instance can have only one key pair. If a private key is bound to your BMS, binding a new private key to the BMS will replace the original one.

## Generation Method<a name="section13455325174014"></a>

-   Creating a key pair on the management console

    >![](/images/icon-note.gif) **NOTE:**   
    >When generating a key pair for the first time, download and properly save the private key.  

-   Using PuTTYgen to create a key pair and import the key pair into the cloud platform.

## Related Operations<a name="section1077412356484"></a>

[Using an SSH Key Pair](using-an-ssh-key-pair.md)

