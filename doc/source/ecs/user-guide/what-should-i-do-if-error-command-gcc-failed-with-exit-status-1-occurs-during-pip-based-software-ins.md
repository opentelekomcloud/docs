# What Should I Do If Error "command ´gcc´ failed with exit status 1" Occurs During PIP-based Software Installation<a name="EN-US_TOPIC_0107412162"></a>

## Symptom<a name="section4545101482614"></a>

When installing the Python library software, you need to configure the PIP source. Take the official image source as an example:

```
[root@test home]# cat /root/.pip/pip.conf 
[global]
index-url = https://pypi.python.org/simple
trusted-host = pypi.python.org
```

During the installation, the system displays the message "command ´gcc´ failed with exit status 1". However, GCC has been installed by running the yum command before the Python library software is installed using the PIP.

**Figure  1**  Installation error<a name="fig15547217122815"></a>  
![](figures/installation-error.png "installation-error")

## Possible Causes<a name="section2028651416307"></a>

openssl-devel is not supported.

## Solution<a name="section12023073012"></a>

The following operations use psutil as an example:

1.  Run the following command to install openssl-devel:

    **yum install gcc libffi-devel python-devel openssl-devel -y**

2.  Use PIP to install the Python library software again. The error message is cleared.

    **Figure  2**  Successful installation<a name="fig850134793413"></a>  
    ![](figures/successful-installation-18.png "successful-installation-18")


