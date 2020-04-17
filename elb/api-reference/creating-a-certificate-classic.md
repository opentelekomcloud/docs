# Creating a Certificate<a name="EN-US_TOPIC_0096561523"></a>

## Function<a name="en-us_topic_0032340347_section54999878"></a>

This API is used to create a certificate for an HTTPS listener.

## URI<a name="en-us_topic_0032340347_section25236858"></a>

POST /v1.0/\{project\_id\}/elbaas/certificate

**Table  1**  Parameter description

<a name="en-us_topic_0032340347_table33323423"></a>
<table><thead align="left"><tr id="en-us_topic_0032340347_row8420641"><th class="cellrowborder" valign="top" width="12%" id="mcps1.2.5.1.1"><p id="en-us_topic_0032340347_p10983320"><a name="en-us_topic_0032340347_p10983320"></a><a name="en-us_topic_0032340347_p10983320"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.2"><p id="en-us_topic_0032340347_p17233719"><a name="en-us_topic_0032340347_p17233719"></a><a name="en-us_topic_0032340347_p17233719"></a><strong id="b842352706192244"><a name="b842352706192244"></a><a name="b842352706192244"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="11%" id="mcps1.2.5.1.3"><p id="en-us_topic_0032340347_p4164548117122"><a name="en-us_topic_0032340347_p4164548117122"></a><a name="en-us_topic_0032340347_p4164548117122"></a><strong id="b842352706145623"><a name="b842352706145623"></a><a name="b842352706145623"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="63%" id="mcps1.2.5.1.4"><p id="en-us_topic_0032340347_p53754023"><a name="en-us_topic_0032340347_p53754023"></a><a name="en-us_topic_0032340347_p53754023"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0032340347_row53906008171138"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="p061745141417"><a name="p061745141417"></a><a name="p061745141417"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0032340347_p31143627171144"><a name="en-us_topic_0032340347_p31143627171144"></a><a name="en-us_topic_0032340347_p31143627171144"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0032340347_p39605860171144"><a name="en-us_topic_0032340347_p39605860171144"></a><a name="en-us_topic_0032340347_p39605860171144"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0032340347_p53958126171144"><a name="en-us_topic_0032340347_p53958126171144"></a><a name="en-us_topic_0032340347_p53958126171144"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0032340347_row33431272113959"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0032340347_p19792599161649"><a name="en-us_topic_0032340347_p19792599161649"></a><a name="en-us_topic_0032340347_p19792599161649"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0032340347_p50996812114013"><a name="en-us_topic_0032340347_p50996812114013"></a><a name="en-us_topic_0032340347_p50996812114013"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0032340347_p54126260114016"><a name="en-us_topic_0032340347_p54126260114016"></a><a name="en-us_topic_0032340347_p54126260114016"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.5.1.4 "><a name="ul688081181515"></a><a name="ul688081181515"></a><ul id="ul688081181515"><li>Specifies the certificate name.</li><li>The value is a string of 0 to 64 characters that consist of Chinese characters, letters, digits, underscores (_), and hyphens (-).</li></ul>
</td>
</tr>
<tr id="en-us_topic_0032340347_row59108624"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0032340347_p23069209"><a name="en-us_topic_0032340347_p23069209"></a><a name="en-us_topic_0032340347_p23069209"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0032340347_p56666602"><a name="en-us_topic_0032340347_p56666602"></a><a name="en-us_topic_0032340347_p56666602"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0032340347_p1784078717122"><a name="en-us_topic_0032340347_p1784078717122"></a><a name="en-us_topic_0032340347_p1784078717122"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.5.1.4 "><a name="ul418232112150"></a><a name="ul418232112150"></a><ul id="ul418232112150"><li>Provides supplementary information about the certificate.</li><li>The value contains a maximum of 128 characters and cannot contain angle brackets (&lt; and &gt;).</li></ul>
</td>
</tr>
<tr id="en-us_topic_0032340347_row3891908919147"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0032340347_p41594914191410"><a name="en-us_topic_0032340347_p41594914191410"></a><a name="en-us_topic_0032340347_p41594914191410"></a>domain</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0032340347_p13744837191410"><a name="en-us_topic_0032340347_p13744837191410"></a><a name="en-us_topic_0032340347_p13744837191410"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0032340347_p39590050191410"><a name="en-us_topic_0032340347_p39590050191410"></a><a name="en-us_topic_0032340347_p39590050191410"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0032340347_ul52677471191410"></a><a name="en-us_topic_0032340347_ul52677471191410"></a><ul id="en-us_topic_0032340347_ul52677471191410"><li>Specifies the domain name associated with the server certificate.</li><li>The value is a string that contains a maximum of 254 characters, can only contain letters, digits, hyphens (-), and periods (.), and must start with uppercase letters or digits.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0032340347_row58247484"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0032340347_p20425774"><a name="en-us_topic_0032340347_p20425774"></a><a name="en-us_topic_0032340347_p20425774"></a>certificate</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0032340347_p25968169161730"><a name="en-us_topic_0032340347_p25968169161730"></a><a name="en-us_topic_0032340347_p25968169161730"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0032340347_p3581766217122"><a name="en-us_topic_0032340347_p3581766217122"></a><a name="en-us_topic_0032340347_p3581766217122"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0032340347_ul3770359693139"></a><a name="en-us_topic_0032340347_ul3770359693139"></a><ul id="en-us_topic_0032340347_ul3770359693139"><li>Specifies the certificate content.</li><li>The value is in PEM coding format.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0032340347_row38446258"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0032340347_p27139175"><a name="en-us_topic_0032340347_p27139175"></a><a name="en-us_topic_0032340347_p27139175"></a>private_key</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0032340347_p48272001161733"><a name="en-us_topic_0032340347_p48272001161733"></a><a name="en-us_topic_0032340347_p48272001161733"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0032340347_p1554952217122"><a name="en-us_topic_0032340347_p1554952217122"></a><a name="en-us_topic_0032340347_p1554952217122"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0032340347_ul4557146493149"></a><a name="en-us_topic_0032340347_ul4557146493149"></a><ul id="en-us_topic_0032340347_ul4557146493149"><li>Specifies the private key of the certificate.</li><li>The value is in PEM coding format.</li></ul>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0032340347_section25805135"></a>

-   Request parameters

    None


-   Example request

    ```
    {
        "name": "cert-bky",
        "description": "certificate",
        "certificate": "-----BEGIN CERTIFICATE-----\nMIIDXTCCAkWgAwIBAgIJANoPUy2NktS6MA0GCSqGSIb3DQEBBQUAMEUxCzAJBgNV\nBAYTAkFVMRMwEQYDVQQIDApTb21lLVN0YXRlMSEwHwYDVQQKDBhJbnRlcm5ldCBX\naWRnaXRzIFB0eSBMdGQwHhcNMTYwNjIyMDMyOTU5WhcNMTkwNjIyMDMyOTU5WjBF\nMQswCQYDVQQGEwJBVTETMBEGA1UECAwKU29tZS1TdGF0ZTEhMB8GA1UECgwYSW50\nZXJuZXQgV2lkZ2l0cyBQdHkgTHRkMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIB\nCgKCAQEArmUUhzm5sxxVr/ku4+6cKqnKgZvDl+e/6CNCAq8YMZXTpJP64DjDPny9\n+8s9MbFabEG3HqjHSKh3b/Ew3FXr8LFa9YuWuAi3W9ii29sZsOwmzIfQhIOIaP1Y\nNR50DDjbAGTaxzRhV40ZKSOCkaUTvl3do5d8ttD1VlF2r0w0DfclrVcsS5v3kw88\n9gJ3s3hNkatfQiSt4qLNMehZ8Xofx58DIAOk/f3Vusj3372PsJwKX39cHX/NpIHC\nHKE8qaGCpDqv0daH766eJ065dqO9DuorXPaPT/nxw4PAccb9fByLrTams0ThvSlZ\no6V3yvHR4KN7mmvbViEmWRy+9oiJEwIDAQABo1AwTjAdBgNVHQ4EFgQUlXhcABza\n2SdXPYpp8RkWvKblCNIwHwYDVR0jBBgwFoAUlXhcABza2SdXPYpp8RkWvKblCNIw\nDAYDVR0TBAUwAwEB/zANBgkqhkiG9w0BAQUFAAOCAQEAHmsFDOwbkD45PF4oYdX+\ncCoEGNjsLfi0spJ6b1CHQMEy2tPqYZJh8nGuUtB9Zd7+rbwm6NS38eGQVA5vbWZH\nMk+uq5un7YFwkM+fdjgCxbe/3PMkk/ZDYPHhpc1W8e/+aZVUBB2EpfzBC6tcP/DV\nSsjq+tG+JZIVADMxvEqVIF94JMpuY7o6U74SnUUrAi0h9GkWmeYh/Ucb3PLMe5sF\noZriRdAKc96KB0eUphfWZNtptOCqV6qtYqZZ/UCotp99xzrDkf8jGkm/iBljxb+v\n0NTg8JwfmykCj63YhTKpHf0+N/EK5yX1KUYtlkLaf8OPlsp/1lqAL6CdnydGEd/s\nAA==\n-----END CERTIFICATE-----",
        "private_key": "-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEArmUUhzm5sxxVr/ku4+6cKqnKgZvDl+e/6CNCAq8YMZXTpJP6\n4DjDPny9+8s9MbFabEG3HqjHSKh3b/Ew3FXr8LFa9YuWuAi3W9ii29sZsOwmzIfQ\nhIOIaP1YNR50DDjbAGTaxzRhV40ZKSOCkaUTvl3do5d8ttD1VlF2r0w0DfclrVcs\nS5v3kw889gJ3s3hNkatfQiSt4qLNMehZ8Xofx58DIAOk/f3Vusj3372PsJwKX39c\nHX/NpIHCHKE8qaGCpDqv0daH766eJ065dqO9DuorXPaPT/nxw4PAccb9fByLrTam\ns0ThvSlZo6V3yvHR4KN7mmvbViEmWRy+9oiJEwIDAQABAoIBACV47rpHuxEza24O\nevbbFI9OQIcs8xA26dN1j/+HpAkzinB4o5V+XOWWZDQwbYu58hYE4NYjqf6AxHk3\nOCqAA9yKH2NXhSEyLkP7/rKDF7geZg/YtwNiR/NXTJbNXl4p8VTaVvAq3yey188x\nJCMrd1yWSsOWD2Qw7iaIBpqQIzdEovPE4CG6GmaIRSuqYuoCfbVTFa6YST7jmOTv\nEpG+x6yJZzJ4o0vvfKbKfvPmQizjL+3nAW9g+kgXJmA1xTujiky7bzm2sLK2Slrx\n5rY73mXMElseSlhkYzWwyRmC6M+rWALXqOhVDgIGbaBV4IOzuyH/CUt0wy3ZMIpv\nMOWMNoECgYEA1LHsepCmwjlDF3yf/OztCr/DYqM4HjAY6FTmH+xz1Zjd5R1XOq60\nYFRkhs/e2D6M/gSX6hMqS9sCkg25yRJk3CsPeoS9v5MoiZQA8XlQNovcpWUI2DCm\naZRIsdovFgIqMHYh/Y4CYouee7Nz7foICzO9svrYrbOIVmMwDVJ8vzMCgYEA0ebg\nm0lCuOunyxaSBqOv4Q4sk7Ix0702dIrW0tsUJyU+xuXYH1P/0m+t4/KUU2cNwsg3\njiNzQR9QKvF8yTB5TB4Ye/9dKlu+BEOskvCpuErxc6iVJ+TZOrQDDPNcq56qez5b\nvv9EDdgzpjkjO+hS1j3kYOuG11hrP4Pox4PijqECgYEAz6RTZORKqFoWsZss5VK3\np0LGkEkfw/jYmBgqAQhpnSD7n20hd1yPI2vAKAxPVXTbWDFLzWygYiWRQNy9fxrB\n9F7lYYqtY5VagdVHhnYUZOvtoFoeZFA6ZeAph9elGCtM3Lq3PD2i/mmncsQibTUn\nHSiKDWzuk8UtWIjEpHze5BkCgYEAifD9eG+bzqTnn1qU2pIl2nQTLXj0r97v84Tu\niqF4zAT5DYMtFeGBBI1qLJxVh7342CH2CI4ZhxmJ+L68sAcQH8rDcnGui1DBPlIv\nDl3kW3280bJfW1lUvPRh8NfZ9dsO1HF1n75nveVwg/OWyR7zmWIRPPRrqAeua45H\nox5z/CECgYBqwlEBjue8oOkVVu/lKi6fo6jr+0u25K9dp9azHYwE0KNHX0MwRALw\nWbPgcjge23sfhbeqVvHo0JYBdRsk/OBuW73/9Sb5E+6auDoubCjC0cAIvs23MPju\nsMvKak4mQkI19foRXBydB/DDkK26iei/l0xoygrw50v2HErsQ7JcHw==\n-----END RSA PRIVATE KEY-----"
    }
    ```


## Response<a name="en-us_topic_0032340347_section30919631"></a>

-   Response parameters

    **Table  2**  Response parameters

    <a name="en-us_topic_0032340347_table58268660154720"></a>
    <table><thead align="left"><tr id="en-us_topic_0032340347_row43546893154720"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.1"><p id="en-us_topic_0032340347_p37637446154720"><a name="en-us_topic_0032340347_p37637446154720"></a><a name="en-us_topic_0032340347_p37637446154720"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17%" id="mcps1.2.4.1.2"><p id="en-us_topic_0032340347_p15158425193624"><a name="en-us_topic_0032340347_p15158425193624"></a><a name="en-us_topic_0032340347_p15158425193624"></a><strong id="b842352706145623_1"><a name="b842352706145623_1"></a><a name="b842352706145623_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="65%" id="mcps1.2.4.1.3"><p id="en-us_topic_0032340347_p45778611154720"><a name="en-us_topic_0032340347_p45778611154720"></a><a name="en-us_topic_0032340347_p45778611154720"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0032340347_row513410112435"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0032340347_p5065952912439"><a name="en-us_topic_0032340347_p5065952912439"></a><a name="en-us_topic_0032340347_p5065952912439"></a>tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0032340347_p978118112439"><a name="en-us_topic_0032340347_p978118112439"></a><a name="en-us_topic_0032340347_p978118112439"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0032340347_p5407822612439"><a name="en-us_topic_0032340347_p5407822612439"></a><a name="en-us_topic_0032340347_p5407822612439"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0032340347_row3070025912523"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0032340347_p4562333112526"><a name="en-us_topic_0032340347_p4562333112526"></a><a name="en-us_topic_0032340347_p4562333112526"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0032340347_p450233212526"><a name="en-us_topic_0032340347_p450233212526"></a><a name="en-us_topic_0032340347_p450233212526"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0032340347_p2914464612526"><a name="en-us_topic_0032340347_p2914464612526"></a><a name="en-us_topic_0032340347_p2914464612526"></a>Specifies the certificate ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0032340347_row17079990154720"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0032340347_p53539591162227"><a name="en-us_topic_0032340347_p53539591162227"></a><a name="en-us_topic_0032340347_p53539591162227"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0032340347_p66205107193624"><a name="en-us_topic_0032340347_p66205107193624"></a><a name="en-us_topic_0032340347_p66205107193624"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0032340347_p63423313154720"><a name="en-us_topic_0032340347_p63423313154720"></a><a name="en-us_topic_0032340347_p63423313154720"></a>Specifies the certificate name.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0032340347_row33938912154720"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0032340347_p40111970162227"><a name="en-us_topic_0032340347_p40111970162227"></a><a name="en-us_topic_0032340347_p40111970162227"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0032340347_p4321605112554"><a name="en-us_topic_0032340347_p4321605112554"></a><a name="en-us_topic_0032340347_p4321605112554"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0032340347_p1083922212554"><a name="en-us_topic_0032340347_p1083922212554"></a><a name="en-us_topic_0032340347_p1083922212554"></a>Provides supplementary information about the certificate.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0032340347_row1099695819151"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0032340347_p3713832119154"><a name="en-us_topic_0032340347_p3713832119154"></a><a name="en-us_topic_0032340347_p3713832119154"></a>domain</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0032340347_p5541402319154"><a name="en-us_topic_0032340347_p5541402319154"></a><a name="en-us_topic_0032340347_p5541402319154"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0032340347_p5935084919154"><a name="en-us_topic_0032340347_p5935084919154"></a><a name="en-us_topic_0032340347_p5935084919154"></a>Specifies the domain name associated with the server certificate.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0032340347_row8871928154720"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0032340347_p49270530162227"><a name="en-us_topic_0032340347_p49270530162227"></a><a name="en-us_topic_0032340347_p49270530162227"></a>certificate</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0032340347_p359513812610"><a name="en-us_topic_0032340347_p359513812610"></a><a name="en-us_topic_0032340347_p359513812610"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0032340347_p2277078112610"><a name="en-us_topic_0032340347_p2277078112610"></a><a name="en-us_topic_0032340347_p2277078112610"></a>Specifies the certificate content.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0032340347_row794063512618"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0032340347_p14974587162227"><a name="en-us_topic_0032340347_p14974587162227"></a><a name="en-us_topic_0032340347_p14974587162227"></a>private_key</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0032340347_p3782791312633"><a name="en-us_topic_0032340347_p3782791312633"></a><a name="en-us_topic_0032340347_p3782791312633"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0032340347_p4416213212633"><a name="en-us_topic_0032340347_p4416213212633"></a><a name="en-us_topic_0032340347_p4416213212633"></a>Specifies the private key of the certificate.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0032340347_row16253572154720"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0032340347_p4904884012633"><a name="en-us_topic_0032340347_p4904884012633"></a><a name="en-us_topic_0032340347_p4904884012633"></a>create_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0032340347_p1353309912633"><a name="en-us_topic_0032340347_p1353309912633"></a><a name="en-us_topic_0032340347_p1353309912633"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0032340347_p2243924312633"><a name="en-us_topic_0032340347_p2243924312633"></a><a name="en-us_topic_0032340347_p2243924312633"></a>Specifies the time when the certificate was created.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0032340347_row1392188154720"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0032340347_p3818166162238"><a name="en-us_topic_0032340347_p3818166162238"></a><a name="en-us_topic_0032340347_p3818166162238"></a>update_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0032340347_p16061839162238"><a name="en-us_topic_0032340347_p16061839162238"></a><a name="en-us_topic_0032340347_p16061839162238"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0032340347_p6862238162238"><a name="en-us_topic_0032340347_p6862238162238"></a><a name="en-us_topic_0032340347_p6862238162238"></a>Specifies the time when the certificate was updated.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
    "name":"cert-bky",
    "description":"certificate",
    "certificate":"-----BEGIN CERTIFICATE-----\nMIIDXTCCAkWgAwIBAgIJANoPUy2NktS6MA0GCSqGSIb3DQEBBQUAMEUxCzAJBgNV\nBAYTAkFVMRMwEQYDVQQIDApTb21lLVN0YXRlMSEwHwYDVQQKDBhJbnRlcm5ldCBX\naWRnaXRzIFB0eSBMdGQwHhcNMTYwNjIyMDMyOTU5WhcNMTkwNjIyMDMyOTU5WjBF\nMQswCQYDVQQGEwJBVTETMBEGA1UECAwKU29tZS1TdGF0ZTEhMB8GA1UECgwYSW50\nZXJuZXQgV2lkZ2l0cyBQdHkgTHRkMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIB\nCgKCAQEArmUUhzm5sxxVr/ku4+6cKqnKgZvDl+e/6CNCAq8YMZXTpJP64DjDPny9\n+8s9MbFabEG3HqjHSKh3b/Ew3FXr8LFa9YuWuAi3W9ii29sZsOwmzIfQhIOIaP1Y\nNR50DDjbAGTaxzRhV40ZKSOCkaUTvl3do5d8ttD1VlF2r0w0DfclrVcsS5v3kw88\n9gJ3s3hNkatfQiSt4qLNMehZ8Xofx58DIAOk/f3Vusj3372PsJwKX39cHX/NpIHC\nHKE8qaGCpDqv0daH766eJ065dqO9DuorXPaPT/nxw4PAccb9fByLrTams0ThvSlZ\no6V3yvHR4KN7mmvbViEmWRy+9oiJEwIDAQABo1AwTjAdBgNVHQ4EFgQUlXhcABza\n2SdXPYpp8RkWvKblCNIwHwYDVR0jBBgwFoAUlXhcABza2SdXPYpp8RkWvKblCNIw\nDAYDVR0TBAUwAwEB/zANBgkqhkiG9w0BAQUFAAOCAQEAHmsFDOwbkD45PF4oYdX+\ncCoEGNjsLfi0spJ6b1CHQMEy2tPqYZJh8nGuUtB9Zd7+rbwm6NS38eGQVA5vbWZH\nMk+uq5un7YFwkM+fdjgCxbe/3PMkk/ZDYPHhpc1W8e/+aZVUBB2EpfzBC6tcP/DV\nSsjq+tG+JZIVADMxvEqVIF94JMpuY7o6U74SnUUrAi0h9GkWmeYh/Ucb3PLMe5sF\noZriRdAKc96KB0eUphfWZNtptOCqV6qtYqZZ/UCotp99xzrDkf8jGkm/iBljxb+v\n0NTg8JwfmykCj63YhTKpHf0+N/EK5yX1KUYtlkLaf8OPlsp/1lqAL6CdnydGEd/s\nAA==\n-----END CERTIFICATE-----",
    "private_key":"-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEArmUUhzm5sxxVr/ku4+6cKqnKgZvDl+e/6CNCAq8YMZXTpJP6\n4DjDPny9+8s9MbFabEG3HqjHSKh3b/Ew3FXr8LFa9YuWuAi3W9ii29sZsOwmzIfQ\nhIOIaP1YNR50DDjbAGTaxzRhV40ZKSOCkaUTvl3do5d8ttD1VlF2r0w0DfclrVcs\nS5v3kw889gJ3s3hNkatfQiSt4qLNMehZ8Xofx58DIAOk/f3Vusj3372PsJwKX39c\nHX/NpIHCHKE8qaGCpDqv0daH766eJ065dqO9DuorXPaPT/nxw4PAccb9fByLrTam\ns0ThvSlZo6V3yvHR4KN7mmvbViEmWRy+9oiJEwIDAQABAoIBACV47rpHuxEza24O\nevbbFI9OQIcs8xA26dN1j/+HpAkzinB4o5V+XOWWZDQwbYu58hYE4NYjqf6AxHk3\nOCqAA9yKH2NXhSEyLkP7/rKDF7geZg/YtwNiR/NXTJbNXl4p8VTaVvAq3yey188x\nJCMrd1yWSsOWD2Qw7iaIBpqQIzdEovPE4CG6GmaIRSuqYuoCfbVTFa6YST7jmOTv\nEpG+x6yJZzJ4o0vvfKbKfvPmQizjL+3nAW9g+kgXJmA1xTujiky7bzm2sLK2Slrx\n5rY73mXMElseSlhkYzWwyRmC6M+rWALXqOhVDgIGbaBV4IOzuyH/CUt0wy3ZMIpv\nMOWMNoECgYEA1LHsepCmwjlDF3yf/OztCr/DYqM4HjAY6FTmH+xz1Zjd5R1XOq60\nYFRkhs/e2D6M/gSX6hMqS9sCkg25yRJk3CsPeoS9v5MoiZQA8XlQNovcpWUI2DCm\naZRIsdovFgIqMHYh/Y4CYouee7Nz7foICzO9svrYrbOIVmMwDVJ8vzMCgYEA0ebg\nm0lCuOunyxaSBqOv4Q4sk7Ix0702dIrW0tsUJyU+xuXYH1P/0m+t4/KUU2cNwsg3\njiNzQR9QKvF8yTB5TB4Ye/9dKlu+BEOskvCpuErxc6iVJ+TZOrQDDPNcq56qez5b\nvv9EDdgzpjkjO+hS1j3kYOuG11hrP4Pox4PijqECgYEAz6RTZORKqFoWsZss5VK3\np0LGkEkfw/jYmBgqAQhpnSD7n20hd1yPI2vAKAxPVXTbWDFLzWygYiWRQNy9fxrB\n9F7lYYqtY5VagdVHhnYUZOvtoFoeZFA6ZeAph9elGCtM3Lq3PD2i/mmncsQibTUn\nHSiKDWzuk8UtWIjEpHze5BkCgYEAifD9eG+bzqTnn1qU2pIl2nQTLXj0r97v84Tu\niqF4zAT5DYMtFeGBBI1qLJxVh7342CH2CI4ZhxmJ+L68sAcQH8rDcnGui1DBPlIv\nDl3kW3280bJfW1lUvPRh8NfZ9dsO1HF1n75nveVwg/OWyR7zmWIRPPRrqAeua45H\nox5z/CECgYBqwlEBjue8oOkVVu/lKi6fo6jr+0u25K9dp9azHYwE0KNHX0MwRALw\nWbPgcjge23sfhbeqVvHo0JYBdRsk/OBuW73/9Sb5E+6auDoubCjC0cAIvs23MPju\nsMvKak4mQkI19foRXBydB/DDkK26iei/l0xoygrw50v2HErsQ7JcHw==\n-----END RSA PRIVATE KEY-----",
    "tenant_id":"ed9edbc66b8b47c09f5d2fcd89430b33",
    "id":"5b8f908b5495452aa13beede0afc5d99",
    "create_time":"2016-06-27 08:14:42",
    "update_time":"2016-06-27 08:14:42"
    }
    ```


## Status Code<a name="en-us_topic_0032340347_section9841225"></a>

-   Normal

    200

-   Abnormal

    <a name="en-us_topic_0032340347_table11098151151527"></a>
    <table><thead align="left"><tr id="en-us_topic_0032340347_row16678161151527"><th class="cellrowborder" valign="top" width="10.56%" id="mcps1.1.4.1.1"><p id="en-us_topic_0032340347_p8753830151527"><a name="en-us_topic_0032340347_p8753830151527"></a><a name="en-us_topic_0032340347_p8753830151527"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="43.2%" id="mcps1.1.4.1.2"><p id="p19984112420239"><a name="p19984112420239"></a><a name="p19984112420239"></a>Message</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.239999999999995%" id="mcps1.1.4.1.3"><p id="en-us_topic_0032340347_p37971652151527"><a name="en-us_topic_0032340347_p37971652151527"></a><a name="en-us_topic_0032340347_p37971652151527"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0032340347_row55804946151527"><td class="cellrowborder" valign="top" width="10.56%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0032340347_p23906744151527"><a name="en-us_topic_0032340347_p23906744151527"></a><a name="en-us_topic_0032340347_p23906744151527"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.2%" headers="mcps1.1.4.1.2 "><p id="p1471874262320"><a name="p1471874262320"></a><a name="p1471874262320"></a>badRequest</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0032340347_p57398111151527"><a name="en-us_topic_0032340347_p57398111151527"></a><a name="en-us_topic_0032340347_p57398111151527"></a>Request error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0032340347_row46820954151527"><td class="cellrowborder" valign="top" width="10.56%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0032340347_p34400933151527"><a name="en-us_topic_0032340347_p34400933151527"></a><a name="en-us_topic_0032340347_p34400933151527"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.2%" headers="mcps1.1.4.1.2 "><p id="p9718124272316"><a name="p9718124272316"></a><a name="p9718124272316"></a>unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0032340347_p35012164151527"><a name="en-us_topic_0032340347_p35012164151527"></a><a name="en-us_topic_0032340347_p35012164151527"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0032340347_row46674023151527"><td class="cellrowborder" valign="top" width="10.56%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0032340347_p22499488151527"><a name="en-us_topic_0032340347_p22499488151527"></a><a name="en-us_topic_0032340347_p22499488151527"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.2%" headers="mcps1.1.4.1.2 "><p id="p671820428238"><a name="p671820428238"></a><a name="p671820428238"></a>userDisabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0032340347_p10519201151527"><a name="en-us_topic_0032340347_p10519201151527"></a><a name="en-us_topic_0032340347_p10519201151527"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0032340347_row27563948151527"><td class="cellrowborder" valign="top" width="10.56%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0032340347_p18087341151527"><a name="en-us_topic_0032340347_p18087341151527"></a><a name="en-us_topic_0032340347_p18087341151527"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.2%" headers="mcps1.1.4.1.2 "><p id="p37191142192310"><a name="p37191142192310"></a><a name="p37191142192310"></a>Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0032340347_p55788555151527"><a name="en-us_topic_0032340347_p55788555151527"></a><a name="en-us_topic_0032340347_p55788555151527"></a>The requested page does not exist.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0032340347_row32334952151527"><td class="cellrowborder" valign="top" width="10.56%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0032340347_p1885468151527"><a name="en-us_topic_0032340347_p1885468151527"></a><a name="en-us_topic_0032340347_p1885468151527"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.2%" headers="mcps1.1.4.1.2 "><p id="p57191942132312"><a name="p57191942132312"></a><a name="p57191942132312"></a>authFault</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0032340347_p18505183151527"><a name="en-us_topic_0032340347_p18505183151527"></a><a name="en-us_topic_0032340347_p18505183151527"></a>System error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0032340347_row32328927151527"><td class="cellrowborder" valign="top" width="10.56%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0032340347_p1397439151527"><a name="en-us_topic_0032340347_p1397439151527"></a><a name="en-us_topic_0032340347_p1397439151527"></a>503</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.2%" headers="mcps1.1.4.1.2 "><p id="p07197424236"><a name="p07197424236"></a><a name="p07197424236"></a>serviceUnavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0032340347_p46083715151527"><a name="en-us_topic_0032340347_p46083715151527"></a><a name="en-us_topic_0032340347_p46083715151527"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


