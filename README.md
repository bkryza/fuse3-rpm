# Fuse 3 RPM package spec files

## Example

```
# Assumes the commands are performed as user 'centos'

sudo yum install epel-release

sudo yum install mock

sudo usermod -a -G mock centos

wget https://github.com/libfuse/libfuse/releases/download/fuse-3.1.1/fuse-3.1.1.tar.gz

# Build CentOS 7
mock -r /etc/mock/epel-7-x86_64.cfg --init

mock -r /etc/mock/epel-7-x86_64.cfg --buildsrpm --spec fuse3-epel7.spec --sources fuse-3.1.1.tar.gz

mock -r /etc/mock/epel-7-x86_64.cfg rebuild /home/centos/rpmbuild/SRPMS/fuse3-3.1.1-7.el7.centos.src.rpm

cp /var/lib/mock/epel-7-x86_64/result/* centos7-rpms

mock -r /etc/mock/epel-7-x86_64.cfg --clean

# Build Fedora 23
mock -r /etc/mock/fedora-23-x86_64.cfg --init

mock -r /etc/mock/fedora-23-x86_64.cfg --buildsrpm --spec fuse3-fedora23.spec --sources fuse-3.1.1.tar.gz

cp /var/lib/mock/fedora-23-x86_64/result/fuse3-3.1.1-7.fc23.src.rpm .
```
