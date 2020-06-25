# What Do I Do If Injecting the Key or Password Using Cloud-Init Fails After NetworkManager Is Installed?<a name="EN-US_TOPIC_0113992021"></a>

## Symptom<a name="section45171058315"></a>

A major cause is that the version of Cloud-Init is incompatible with that of NetworkManager. In Debian 9.0 and later versions, NetworkManager is incompatible with Cloud-Init 0.7.9.

## Solution<a name="section14764194672313"></a>

Uninstall the current Cloud-Init and install Cloud-Init 0.7.6 or an earlier version.

For details about how to install Cloud-Init, see  [Installing Cloud-Init](installing-cloud-init.md).

