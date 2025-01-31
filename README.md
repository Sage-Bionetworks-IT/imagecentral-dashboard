# Deprecation
The listed images from here can still be used however we have decided to deprecate
using packer in favor of the AWS image builder to generate AMIs.
As of 1/16/2025 new AMIs will be created with the AWS image builder from
[Sage-Bionetworks-IT/aws-ami-monorepo](https://github.com/Sage-Bionetworks-IT/aws-ami-monorepo) repo.
The generated AMIs from that repo are searchable using the AWS EC2->Images->AMI console.


# AMI Dashboard
Here are a list of AMIs that can be used by Sage Bionetworks for provisioning. This dashboard is updated on a daily basis.


AMI Name | AMI Id
-------- | ------
weechat-v1.0.0 | `ami-0c437dfa321f0611e`
weechat-LATEST | `ami-09a6de893ca3fef75`
sagebio-base-ubuntu-bionic-v1.0.1 | `ami-0944334364827dc2d`
sagebio-base-ubuntu-bionic-v1.0.0 | `ami-0d576d466a205f6db`
sagebio-base-ubuntu-bionic-LATEST | `ami-0b8050b43cdfde2fc`
sagebio-base-aws-linux2-LATEST | `ami-0661708adf687a316`
rstudio-notebook-with-route | `ami-0eaa93068e1048e45`
rStudioAmi-LATEST | `ami-0af1602a4b2831345`
packer-workflows-v1.0.6 | `ami-02fb1df88e77ef400`
packer-workflows-v1.0.5 | `ami-0aa07b115676a7bb0`
packer-workflows-v1.0.4 | `ami-04e9c4e5c4e40ec12`
packer-workflows-v1.0.3 | `ami-039fd44e98891c664`
packer-workflows-v1.0.2 | `ami-0e42922cf0e599fbc`
packer-workflows-v1.0.1 | `ami-019e39721f2e229b0`
packer-workflows-v1.0.0 | `ami-0144434f91f561456`
packer-workflows-master | `ami-0dc5d26198ca64198`
packer-workflows-DEV | `ami-033de8bb079bc9d59`
packer-winserver-2022-v0.0.1 | `ami-08079232459aa7414`
packer-winserver-2022-master | `ami-0294577e656000b22`
packer-ubuntu-docker-DEV | `ami-00e7599be2ef4cb67`
packer-ubuntu-bionic-master | `ami-0e62409dac0ea5e55`
packer-shinyserver-pro-v1.0.0 | `ami-0cfb65d62cde639ea`
packer-shinyserver-pro-master | `ami-09bf84c8f4df6f509`
packer-rstudio-v3.0.7 | `ami-0121a609286ef5a2a`
packer-rstudio-v3.0.6 | `ami-0df37a032576697e4`
packer-rstudio-v3.0.5 | `ami-06f79674b25376754`
packer-rstudio-v3.0.4 | `ami-098145e0ba042dd12`
packer-rstudio-v3.0.3 | `ami-097a388987a40d952`
packer-rstudio-v3.0.2 | `ami-09a02d2456a2a8908`
packer-rstudio-v3.0.1 | `ami-08cd5d5244f82a25c`
packer-rstudio-v3.0.0 | `ami-0fcbd5266337cacab`
packer-rstudio-v2.1.6 | `ami-0d95d262d92cd5b77`
packer-rstudio-v2.1.5 | `ami-060506aa2a0847956`
packer-rstudio-v2.1.3-copy | `ami-0ea087058bb641a84`
packer-rstudio-v2.1.3 | `ami-0236faf14d520852a`
packer-rstudio-v2.1.2 | `ami-0fa2167c265c7ceae`
packer-rstudio-v2.1.1 | `ami-0c0f49c0711209967`
packer-rstudio-v2.1.0 | `ami-0b39fd2833e6520a0`
packer-rstudio-v2.0.0 | `ami-051310d409a32a5aa`
packer-rstudio-v1.0.7 | `ami-0ed2999f7cff2e3e3`
packer-rstudio-v1.0.6 | `ami-0d0ad473db2efe954`
packer-rstudio-v1.0.5 | `ami-0398809a941f2fa22`
packer-rstudio-v1.0.4 | `ami-0041ea40b4237353c`
packer-rstudio-v1.0.3 | `ami-01866cea595e4f968`
packer-rstudio-v1.0.2 | `ami-01db72ecb09a90a60`
packer-rstudio-v1.0.1 | `ami-0571ea73672b03ce7`
packer-rstudio-v1.0.0 | `ami-036688a77595e31cf`
packer-rstudio-master | `ami-0c9f157ae8c537765`
packer-base-winserver2019-v0.0.1 | `ami-0dbdf36ae5f30d8d1`
packer-base-winserver2019-master | `ami-07c6a09b7ba342265`
packer-base-ubuntu-jammy-v1.0.2 | `ami-04e92928ecf1c2066`
packer-base-ubuntu-jammy-v1.0.0 | `ami-0b710e028cd5ff838`
packer-base-ubuntu-jammy-master | `ami-0dbc619567e26c3b6`
packer-base-ubuntu-bionic-v1.0.9 | `ami-0b7906ab614596e7e`
packer-base-ubuntu-bionic-v1.0.8 | `ami-09ddd854571a732be`
packer-base-ubuntu-bionic-v1.0.7 | `ami-0447d7789ebc37ae3`
packer-base-ubuntu-bionic-v1.0.6 | `ami-093ca9e768e56b1bc`
packer-base-ubuntu-bionic-v1.0.5 | `ami-08030043dfd4f797a`
packer-base-ubuntu-bionic-v1.0.4 | `ami-0fe60e01dbcdcda49`
packer-base-ubuntu-bionic-v1.0.2 | `ami-0d383722ce22a6ea1`
packer-base-ubuntu-bionic-v1.0.10 | `ami-0a3c3e0cb6ae0cc6c`
packer-base-ubuntu-bionic-v1.0.1 | `ami-0c04e7f09a1fbcec0`
packer-base-ubuntu-bionic-v1.0.0 | `ami-05cce55c6aa92f55b`
packer-base-ubuntu-bionic-master | `ami-0e7392f5b190d6eef`
packer-base-amazonlinux2-v2.0.0 | `ami-03de634d807ca681e`
packer-base-amazonlinux2-v1.0.2 | `ami-0810a318c4b1243c5`
packer-base-amazonlinux2-v1.0.1 | `ami-06c6e00f3d3eaf56c`
packer-base-amazonlinux2-v1.0.0 | `ami-00a8e72bc0c50ba7c`
packer-base-amazonlinux2-master | `ami-0ff34a733d670d570`
packer-ami-template-master | `ami-0bfac444e0dfbf71b`
packer-ami-template | `ami-0cdae3c3f81d5b38f`
packer-amazonlinux-docker-v2.0.3 | `ami-07260db8d2b10c0ad`
packer-amazonlinux-docker-v2.0.2 | `ami-021590301011f74b3`
packer-amazonlinux-docker-v2.0.1 | `ami-0b0c7a592286b1ad4`
packer-amazonlinux-docker-v2.0.0 | `ami-0090a06306e93b1e1`
packer-amazonlinux-docker-v1.0.1 | `ami-01ceb2232292bf0d0`
packer-amazonlinux-docker-v1.0.0 | `ami-0559a96a9284c1223`
packer-amazonlinux-docker-master | `ami-0c556035361ff7831`
org-sagebase-agora-bastion | `ami-05b72d008a5718961`
kdpackerrstudio | `ami-022d6114ffa79500a`
kdbasejammy | `ami-04c661cd440be7b9e`
agora-data-manager-github-runner 2025-01-14T17-22-56.661830Z | `ami-03bfb6163b0bd8af2`
agora-bastian | `ami-055ca5683a7880ef2`
Windows_Server-2019-English-Full-Base-2019_12_16 2020-01-15T04-57-41.977Z | `ami-074545a6fb2313e2c`
Amazon-Linux-2-AMI-2020_01_08-x86_64-HVM-gp2 2020-01-15T06-08-48.730Z | `ami-0ca7208f904dc1874`
