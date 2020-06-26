# ALM-12055 The Certificate File Is About to Expire<a name="EN-US_TOPIC_0125375350"></a>

## Description<a name="sd9aeec2310ac47bc81225aabd708668a"></a>

The system checks the certificate file on 23:00 every day. This alarm is generated if the time left before the certificate file expires is shorter than the threshold. In this case, the certificate file is about to expire. For details about how to configure the alarm threshold duration, see section  **Configuring the Threshold for the Alarm Stating That the Certificate Is About to Expire**  in the  _Administrator Guide_.

This alarm is cleared if the status of the newly imported certificate is valid.

## Attribute<a name="s7b5ca672830a4f508a5465b0c0c71639"></a>

<a name="tf296455c588046a28a104272e077ce09"></a>
<table><thead align="left"><tr id="r5a3ae66d7c5948c0b087efbc88fece85"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="abf6521e9163f4421b67c3e9bab2b6ac6"><a name="abf6521e9163f4421b67c3e9bab2b6ac6"></a><a name="abf6521e9163f4421b67c3e9bab2b6ac6"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="a0a22d89481a14ca491b6a8a8046622b7"><a name="a0a22d89481a14ca491b6a8a8046622b7"></a><a name="a0a22d89481a14ca491b6a8a8046622b7"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="ad91287525a7a45c3ad4b9965533b5a2d"><a name="ad91287525a7a45c3ad4b9965533b5a2d"></a><a name="ad91287525a7a45c3ad4b9965533b5a2d"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="re8d3abc4d40940208695cc8f1cbbdbe2"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="a1fdc5016d0aa472385812eb16add56ba"><a name="a1fdc5016d0aa472385812eb16add56ba"></a><a name="a1fdc5016d0aa472385812eb16add56ba"></a>12055</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="a8e2f6963c65a4ae3b803ac5cafac5781"><a name="a8e2f6963c65a4ae3b803ac5cafac5781"></a><a name="a8e2f6963c65a4ae3b803ac5cafac5781"></a>Minor</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="a0a66d46e5b4d4dffb630d8a1e40f9bee"><a name="a0a66d46e5b4d4dffb630d8a1e40f9bee"></a><a name="a0a66d46e5b4d4dffb630d8a1e40f9bee"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s8ca1e184a22747f2b6ced22a442e063c"></a>

<a name="t634967707c654d6b9de0c7662761bf3f"></a>
<table><thead align="left"><tr id="r3f2199c235044da99bbb39e3eeb133f0"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="a50d6ab99c65c4b9a94e26173a72bbb1f"><a name="a50d6ab99c65c4b9a94e26173a72bbb1f"></a><a name="a50d6ab99c65c4b9a94e26173a72bbb1f"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="a47c5982dbcb44609baf67473df3e7153"><a name="a47c5982dbcb44609baf67473df3e7153"></a><a name="a47c5982dbcb44609baf67473df3e7153"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="rc5cc552a60fa4d34b3c312e4cc163061"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="abcabd7dcd69049bd9c1171048cceb1f8"><a name="abcabd7dcd69049bd9c1171048cceb1f8"></a><a name="abcabd7dcd69049bd9c1171048cceb1f8"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a11776622dc9a412a87cd547490016590"><a name="a11776622dc9a412a87cd547490016590"></a><a name="a11776622dc9a412a87cd547490016590"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="r82b3c1fe7bcd4660b82f4d8f67231651"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ad88cd80b5090407888a1c72198034695"><a name="ad88cd80b5090407888a1c72198034695"></a><a name="ad88cd80b5090407888a1c72198034695"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a9e4c5c4153c24a36861a22976cf6a837"><a name="a9e4c5c4153c24a36861a22976cf6a837"></a><a name="a9e4c5c4153c24a36861a22976cf6a837"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="r014b934da1684cda95282f30754139d9"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a52bbe445e81c4b9fa6a9e1214d6e979c"><a name="a52bbe445e81c4b9fa6a9e1214d6e979c"></a><a name="a52bbe445e81c4b9fa6a9e1214d6e979c"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="aa3bbbc34cac14ea7a424329849387043"><a name="aa3bbbc34cac14ea7a424329849387043"></a><a name="aa3bbbc34cac14ea7a424329849387043"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s1537d2dd490b4cf2a7767bfcb36e766d"></a>

The system reminds users that the certificate file is about to expire. If the certificate file expires, some functions are restricted and cannot be used properly.

## Possible Causes<a name="s96b159567e4042e99b93282c48266ad0"></a>

The remaining validity period of the CA certificate, HA root certificate \(**root-ca.crt**\), or HA user certificate \(**server.crt**\) is smaller than the alarm threshold.

## Procedure<a name="s32e33c0adf31405a98efe69f7b48e893"></a>

**Locate the alarm cause.**

1.  On MRS Manager, view the real-time alarm list and locate the target alarm.

    In the  **Alarm Details**  area, view the additional information about the alarm.

    -   If  **CA Certificate**  is displayed in the additional information, use PuTTY to log in to the active OMS node as user  **omm**  and go to  [2](#le970e698ce7d4ba980e95bb127380924).
    -   If  **HA root Certificate**  is displayed in the additional information, check  **Location**  to obtain the name of the host involved in this alarm. Then use PuTTY to log in to the host as user  **omm**  and go to  [3](#lba52f9d95f2d432799bbbe7a2882869f).
    -   If  **HA server Certificate**  is displayed in the additional information, check  **Location**  to obtain the name of the host involved in this alarm. Then use PuTTY to log in to the host as user  **omm**  and go to  [4](#l38815a68eca147f29ea71c5db84ea030).


**Check the validity period of the certificate file.**

1.  <a name="le970e698ce7d4ba980e95bb127380924"></a>Check whether the remaining validity period of the CA certificate is smaller than the alarm threshold.

    Run the  **openssl x509 -noout -text -in $\{CONTROLLER\_HOME\}/security/cert/root/ca.crt**  command to check the effective time and due time of the CA certificate.

    -   If yes, go to  [5](#le6e61888406647cc8235e3a40800920c).
    -   If no, go to  [8](#l39714cbae01b4812b84780ac47d909f7).

2.  <a name="lba52f9d95f2d432799bbbe7a2882869f"></a>Check whether the remaining validity period of the HA root certificate is smaller than the alarm threshold.

    Run the  **openssl x509 -noout -text -in $\{CONTROLLER\_HOME\}/security/certHA/root-ca.crt**  command to check the effective time and due time of the HA root certificate.

    -   If yes, go to  [6](#l880dd50a9eac48b3b4f9ad41adbd1294).
    -   If no, go to  [8](#l39714cbae01b4812b84780ac47d909f7).

3.  <a name="l38815a68eca147f29ea71c5db84ea030"></a>Check whether the remaining validity period of the HA user certificate is smaller than the alarm threshold.

    Run the  **openssl x509 -noout -text -in $\{CONTROLLER\_HOME\}/security/certHA/server.crt**  command to check the effective time and expiration time of the HA user certificate.

    -   If yes, go to  [6](#l880dd50a9eac48b3b4f9ad41adbd1294).
    -   If no, go to  [8](#l39714cbae01b4812b84780ac47d909f7).

        The example of the effective time and expiration time of the HA/CA certificate:

        ```
        Certificate: 
            Data: 
                Version: 3 (0x2) 
                Serial Number: 
                    97:d5:0e:84:af:ec:34:d8 
                Signature Algorithm: sha256WithRSAEncryption 
                Issuer: C=CountryName, ST=State, L=Locality, O=Organization, OU=IT, CN=HADOOP.COM 
                Validity 
                    Not Before: Dec 13 06:38:26 2016 GMT             //The effective time. 
                    Not After : Dec 11 06:38:26 2026 GMT             //The expiration time.
        ```



**Import the certificate file.**

1.  <a name="le6e61888406647cc8235e3a40800920c"></a>Import a new CA certificate file.

    Apply for or generate a CA certificate file and import it to the system. For details, see section  **Replacing HA Certificates**  in the  _Administrator Guide_. Manually clear the alarm and check whether this alarm is generated again during periodic check.

    -   If yes, go to  [8](#l39714cbae01b4812b84780ac47d909f7).
    -   If no, no further action is required.

2.  <a name="l880dd50a9eac48b3b4f9ad41adbd1294"></a>Import a new HA certificate file.

    Apply for or generate an HA certificate file and import it to the system. For details, see section R**eplacing HA Certificates**  in the  _Administrator Guide_. Manually clear the alarm and check whether this alarm is generated again during periodic check.

    -   If yes, go to  [8](#l39714cbae01b4812b84780ac47d909f7).
    -   If no, no further action is required.


**Collect fault information.**

1.  On MRS Manager, choose  **System**  \>  **Export Log**.
2.  <a name="l39714cbae01b4812b84780ac47d909f7"></a>Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).

## Related Information<a name="s901091ae9f014c50b650aa87777e574f"></a>

N/A

