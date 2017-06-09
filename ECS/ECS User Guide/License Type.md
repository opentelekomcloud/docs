## License Type

### Use License from the System

Allows you to use the license provided by the public cloud platform. After
buying an ECS with a license authorized, you can use the authorized OS and pay
on demand.

### BYOL

**What Is BYOL?**

Bring your own license (BYOL) allows you to use your existing OS license. In
such a case, you do not need to apply for a license again. In BYOL license type,
you do not pay for the license fee when buying an ECS.

**How to Use BYOL?**

If you select the BYOL license type, you are required to manage licenses by
yourself. The public cloud platform provides functions for you to maintain
license compliance during the license life cycle, for example, deploying ECSs on
DeHs. If you have bought an OS license, you do not need to apply for a license
any more.

The OSs supporting BYOL are as follows:

-   SUSE Linux Enterprise Server
-   Oracle Enterprise Linux
-   Red Hat Enterprise Linux
-   Windows Server Edition OS (BYOL can be used on an ECS that is created on a DeH and runs Windows Server Edition OS.)

**Application Scenarios**

The system does not support dynamic license type changing. ECSs support BYOL in
the following scenarios:
<ul>
<li>Creating an ECS</li>
<dd>After creating an ECS, you cannot change its license type. If the license type must be changed, reinstall or change the ECS OS.</dd>
<li>Reinstalling an ECS OS</li>
<dd>When reinstalling an ECS OS, you can set the license type for the ECS.</dd>
<li>Changing an ECS OS</li>
<dd>When changing an ECS OS, you can set the license type for the ECS.</dd>
<li>Attaching a system disk</li>
<dd>The license type of a system disk is determined by the ECS license type after
  the ECS is created, the ECS OS is reinstalled, or the ECS OS is changed. If the
  system disk is detached and then attached to a new ECS or the original ECS,
  ensure that the ECS license type is the same as the system disk license type.</dd></ul>
