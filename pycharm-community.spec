# disable debuginfo subpackage
%global debug_package %{nil}
# don't strip bundled binaries because pycharm checks length (!!!) of binary fsnotif
# and if you strip debug stuff from it, it will complain
%global __strip /bin/true
# dont repack jars
%global __jar_repack %{nil}
# there are some python 2 and python 3 scripts so there is no way out to bytecompile them ^_^
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

%if 0%{?rhel} <= 7
%bcond_with python3
%else
%bcond_without python3
%endif

%global plugins_dir plugins

%global ansible_version 0.9.5
%global ansible_id 35585

%global bash_version 1.6.12.173
%global bash_id 38798

%global repmapper_version 2.2.0
%global repmapper_id 40747

%global docker_integration_version 173.3727.15
%global docker_integration_id 40538

%global editor_config_version 173.3727.2
%global editor_config_id 40563

%global git_lab_integration_version 1.0.6
%global git_lab_integration_id 17542

%global idea_multimarkdown_version 2.4.0
%global idea_multimarkdown_id 41124

%global ideavim_version 0.49
%global ideavim_id 41383

%global ini_version 173.3727.84
%global ini_id 40770

%global markdown_support_version 173.2696.26
%global markdown_support_id 39197

%global git_tool_box_version 173.1.2
%global git_tool_box_id 41251

%global ignore_plugin_version 2.3.2
%global ignore_plugin_id 40625

%global dbnavigator_version 17.0
%global dbnavigator_id 38969

%global rust_version 0.2.0.2082
%global rust_id 41348

Name:          pycharm-community
Version:       2017.3.1
Release:       1%{?dist}

Summary:       Intelligent Python IDE
License:       ASL 2.0
URL:           http://www.jetbrains.com/pycharm/

Source0:       http://download.jetbrains.com/python/%{name}-%{version}.tar.gz
Source1:       https://plugins.jetbrains.com/files/4230/%{bash_id}/BashSupport-%{bash_version}.zip#/BashSupport-%{bash_version}.zip
Source2:       https://plugins.jetbrains.com/files/8183/%{repmapper_id}/GitLink-%{repmapper_version}.zip#/GitLink-%{repmapper_version}.zip
Source3:       https://plugins.jetbrains.com/files/1800/%{dbnavigator_id}/DBN-%{dbnavigator_version}.zip#/DBN-%{dbnavigator_version}.zip
Source4:       https://plugins.jetbrains.com/files/7793/%{markdown_support_id}/markdown-%{markdown_support_version}.zip#/markdown-%{markdown_support_version}.zip
Source5:       https://plugins.jetbrains.com/files/7792/%{ansible_id}/intellij-ansible-%{ansible_version}.zip#/intellij-ansible-%{ansible_version}.zip
Source6:       https://plugins.jetbrains.com/files/7447/%{git_lab_integration_id}/gitlab-integration-plugin.zip#/gitlab-integration-plugin-%{git_lab_integration_version}.zip
Source7:       https://plugins.jetbrains.com/files/7724/%{docker_integration_id}/Docker-%{docker_integration_version}.zip#/Docker-plugin-%{docker_integration_version}.zip
Source8:       https://plugins.jetbrains.com/files/7896/%{idea_multimarkdown_id}/idea-multimarkdown.%{idea_multimarkdown_version}.zip#/idea-multimarkdown-%{idea_multimarkdown_version}.zip
Source9:       https://plugins.jetbrains.com/files/164/%{ideavim_id}/IdeaVim-%{ideavim_version}.zip#/IdeaVim-%{ideavim_version}.zip
Source10:      https://plugins.jetbrains.com/files/7294/%{editor_config_id}/editorconfig-%{editor_config_version}.zip#/editorconfig-%{editor_config_version}.zip
Source11:      https://plugins.jetbrains.com/files/6981/%{ini_id}/ini4idea-%{ini_version}.zip#/ini4idea-%{ini_version}.zip
Source12:      https://plugins.jetbrains.com/files/7499/%{git_tool_box_id}/GitToolBox-%{git_tool_box_version}.zip#/GitToolBox-%{git_tool_box_version}.zip
Source13:      https://plugins.jetbrains.com/files/7495/%{ignore_plugin_id}/idea-gitignore-%{ignore_plugin_version}.zip#/GitIgnore-%{ignore_plugin_version}.zip
Source14:      https://plugins.jetbrains.com/files/8182/%{rust_id}/intellij-rust-%{rust_version}.zip#/intellij-rust-%{rust_version}.zip

Source101:     pycharm.xml
Source102:     pycharm-community.desktop
Source103:     pycharm-community.appdata.xml

BuildRequires: desktop-file-utils
BuildRequires: /usr/bin/appstream-util
BuildRequires: python2-devel
%if %{with python3}
BuildRequires: python3-devel
%endif
%if 0%{?fedora} >= 24
Recommends:    %{name}-jre%{?_isa} = %{version}-%{release}
%endif

%if 0%{?fedora} <= 24 || 0%{?rhel} == 7
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
%endif
ExclusiveArch: x86_64

%description
The intelligent Python IDE with unique code assistance and analysis,
for productive Python development on all levels

%package plugins
Summary:       Plugins for intelligent Python IDE
Requires:      %{name}%{?_isa} = %{version}-%{release}

%package doc
Summary:       Documentation for intelligent Python IDE
BuildArch:     noarch
Requires:      %{name} = %{version}-%{release}

%package jre
Summary:       Patched OpenJDK for intelligent Python IDE by JetBrains
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description plugins
Intelligent Python IDE contains several plugins. This package
contains plugins like BashSupport, RemoteRepositoryMapper, GoLang, Markdown,
Idea Markdown, Intellij Ansible, GitLab integration plugin, etc.

%description doc
This package contains documentation for Intelligent Python IDE.

%description jre
This package contains patched OpenJDK designed specially for Intelligent
Python IDE by JetBrains, Inc.

%prep
%setup -q -n %{name}-%{version}
%setup -q -n %{name}-%{version} -D -T -a 1
%setup -q -n %{name}-%{version} -D -T -a 2
%setup -q -n %{name}-%{version} -D -T -a 3
%setup -q -n %{name}-%{version} -D -T -a 4
%setup -q -n %{name}-%{version} -D -T -a 5
%setup -q -n %{name}-%{version} -D -T -a 6
%setup -q -n %{name}-%{version} -D -T -a 7
%setup -q -n %{name}-%{version} -D -T -a 8
%setup -q -n %{name}-%{version} -D -T -a 9
%setup -q -n %{name}-%{version} -D -T -a 10
%setup -q -n %{name}-%{version} -D -T -a 11
%setup -q -n %{name}-%{version} -D -T -a 12
%setup -q -n %{name}-%{version} -D -T -a 13
%setup -q -n %{name}-%{version} -D -T -a 14

%install
mkdir -p %{buildroot}%{_javadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_datadir}/mime/packages
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/appdata
mkdir -p %{buildroot}%{_bindir}

cp -arf ./{lib,bin,jre64,help,helpers,plugins} %{buildroot}%{_javadir}/%{name}/
# Move all plugins to /usr/share/java/pycharm-community/plugins directory
cp -arf ./BashSupport %{buildroot}%{_javadir}/%{name}/%{plugins_dir}/
cp -arf ./GitLink %{buildroot}%{_javadir}/%{name}/%{plugins_dir}/
cp -arf ./DBNavigator %{buildroot}%{_javadir}/%{name}/%{plugins_dir}/
cp -arf ./markdown %{buildroot}%{_javadir}/%{name}/%{plugins_dir}/
cp -arf ./intellij-ansible %{buildroot}%{_javadir}/%{name}/%{plugins_dir}/
cp -arf ./gitlab-integration-plugin %{buildroot}%{_javadir}/%{name}/%{plugins_dir}/
cp -arf ./idea-multimarkdown %{buildroot}%{_javadir}/%{name}/%{plugins_dir}/
cp -arf ./IdeaVim %{buildroot}%{_javadir}/%{name}/%{plugins_dir}/
cp -arf ./editorconfig %{buildroot}%{_javadir}/%{name}/%{plugins_dir}/
cp -arf ./ini4idea %{buildroot}%{_javadir}/%{name}/%{plugins_dir}/
cp -arf ./GitToolBox %{buildroot}%{_javadir}/%{name}/%{plugins_dir}/
cp -arf ./Docker %{buildroot}%{_javadir}/%{name}/%{plugins_dir}/
cp -arf ./idea-gitignore %{buildroot}%{_javadir}/%{name}/%{plugins_dir}/
cp -arf ./intellij-rust %{buildroot}%{_javadir}/%{name}/%{plugins_dir}/

rm -f %{buildroot}%{_javadir}/%{name}/bin/fsnotifier{,-arm}
# this will be in docs
rm -f %{buildroot}%{_javadir}/help/*.pdf
cp -af ./bin/pycharm.png %{buildroot}%{_datadir}/pixmaps/pycharm.png
cp -af %{SOURCE101} %{buildroot}%{_datadir}/mime/packages/%{name}.xml
cp -af %{SOURCE102} %{buildroot}%{_datadir}/pycharm-community.desktop
cp -a %{SOURCE103} %{buildroot}%{_datadir}/appdata
ln -s %{_javadir}/%{name}/bin/pycharm.sh %{buildroot}%{_bindir}/pycharm
desktop-file-install                          \
--add-category="Development"                  \
--delete-original                             \
--dir=%{buildroot}%{_datadir}/applications    \
%{buildroot}%{_datadir}/pycharm-community.desktop

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/pycharm-community.appdata.xml

%files
%{_datadir}/applications/pycharm-community.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/pixmaps/pycharm.png
%{_datadir}/appdata/pycharm-community.appdata.xml
%{_javadir}/%{name}
%exclude %{_javadir}/%{name}/jre64
%exclude %{_javadir}/%{name}/%{plugins_dir}/{BashSupport,GitLink,DBNavigator}
%exclude %{_javadir}/%{name}/%{plugins_dir}/{intellij-ansible,markdown,gitlab-integration-plugin}
%exclude %{_javadir}/%{name}/%{plugins_dir}/{IdeaVim,idea-multimarkdown,editorconfig,ini4idea}
%exclude %{_javadir}/%{name}/%{plugins_dir}/{GitToolBox,Docker,idea-gitignore,intellij-rust}
%{_bindir}/pycharm

%post
%if 0%{?fedora} <= 23 || 0%{?rhel} == 7
/bin/touch --no-create %{_datadir}/mime/packages &>/dev/null || :
%endif
%if 0%{?fedora} <= 24 || 0%{?rhel} == 7
/usr/bin/update-desktop-database &> /dev/null || :
%endif

%postun
%if 0%{?fedora} <= 23 || 0%{?rhel} == 7
if [ $1 -eq 0 ] ; then
    /usr/bin/update-mime-database %{_datadir}/mime &> /dev/null || :
fi
%endif
%if 0%{?fedora} <= 24 || 0%{?rhel} == 7
/usr/bin/update-desktop-database &> /dev/null || :
%endif

%posttrans
%if 0%{?fedora} <= 23 || 0%{?rhel} == 7
/usr/bin/update-mime-database %{?fedora:-n} %{_datadir}/mime &> /dev/null || :
%endif

%files plugins
%{_javadir}/%{name}/%{plugins_dir}/BashSupport
%{_javadir}/%{name}/%{plugins_dir}/GitLink
%{_javadir}/%{name}/%{plugins_dir}/DBNavigator
%{_javadir}/%{name}/%{plugins_dir}/intellij-ansible
%{_javadir}/%{name}/%{plugins_dir}/markdown
%{_javadir}/%{name}/%{plugins_dir}/gitlab-integration-plugin
%{_javadir}/%{name}/%{plugins_dir}/IdeaVim
%{_javadir}/%{name}/%{plugins_dir}/idea-multimarkdown
%{_javadir}/%{name}/%{plugins_dir}/Docker
%{_javadir}/%{name}/%{plugins_dir}/editorconfig
%{_javadir}/%{name}/%{plugins_dir}/ini4idea
%{_javadir}/%{name}/%{plugins_dir}/GitToolBox
%{_javadir}/%{name}/%{plugins_dir}/idea-gitignore
%{_javadir}/%{name}/%{plugins_dir}/intellij-rust

%files doc
%doc *.txt
%doc help/*.pdf
%license license/

%files jre
%{_javadir}/%{name}/jre64

%changelog
* Thu Dec 14 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 2017.3.1-1
- Updated to 2017.3.1.

* Wed Dec 06 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 2017.3-1
- Updated to 2017.3. Updated plugins.

* Fri Sep 08 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 2017.2.3-1
- Updated to 2017.2.3. Updated plugins.

* Thu Aug 24 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 2017.2.2-1
- Updated to 2017.2.2. Updated plugins.

* Thu Aug 17 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 2017.2.1-1
- Updated to 2017.2.1. Updated plugins.

* Mon Jun 19 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 2017.1.4-1
- Updated to 2017.1.4. Updated plugins.

* Fri May 26 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 2017.1.3-1
- Updated to 2017.1.3. Updated plugins.

* Thu May 04 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 2017.1.2-1
- Updated to 2017.1.2.

* Wed May 03 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 2017.1.1-2
- Updated scriptlets. Removed java from dependencies.

* Wed May 03 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 2017.1.1-1
- Updated to 2017.1.1. Updated plugins.

* Sat Mar 25 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 2017.1-1
- Updated to 2017.1. Updated plugins.

* Thu Mar 23 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 2016.3.3-1
- Updated to 2016.3.3. Updated plugins to latest compactible versions.

* Mon Dec 26 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 2016.3.1-2
- Added PHP plugin. Updated other plugins.

* Tue Dec 20 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 2016.3.1-1
- Updated to 2016.3.1. Updated plugins.

* Thu Nov 24 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 2016.3-2
- Build only for x86_64.

* Thu Nov 24 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 2016.3-1
- Updated to 2016.3. Updated plugins. Added GitToolBox to subpackage.

* Mon Oct 17 2016 Petr Hracek <phracek@redhat.com> - 2016.2.3-2
- Added GitToolBox plugin.

* Wed Sep 07 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 2016.2.3-1
- Updated to 2016.2.3.

* Sat Aug 27 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 2016.2.2-1
- Updated to 2016.2.2. Updated plugins to latest versions.

* Mon Aug 15 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 2016.2.1-1
- Updated to 2016.2.1. Updated appdata. Added screenshots to Gnome Software.

* Thu Jul 28 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 2016.2-3
- Updated SPEC: added check section, updated post sections, fixed warnings.

* Wed Jul 27 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 2016.2-2
- Added -doc and -jre subpackages. Lots of fixes. Fixed exclusion of plugins.

* Mon Jul 25 2016 Allan Lewis <allanlewis99@gmail.com> - 2016.2-1
- Update to latest upstream version, 2016.2.

* Wed Jul 13 2016 Allan Lewis <allanlewis99@gmail.com> - 2016.1.4-6
- Patch Pytest 'parametrize' skeleton to match Pytest 2.9.2.

* Wed Jul 13 2016 Petr Hracek <phracek@redhat.com> - 2016.1.4-5
- Fix %exclude syntax

* Wed Jun 01 2016 Petr Hracek <phracek@redhat.com> - 2016.1.4-4
- Added plugins EditorConfig, Git4Idea, ini4idea

* Tue May 31 2016 Petr Hracek <phracek@redhat.com> - 2016.1.4-3
- Update Go plugin, Markdown and BashSupport
- CppTools plugin aren't compatible with the latest PyCharm

* Fri May 27 2016 Tomas Hozza <thozza@redhat.com> - 2016.1.4-2
- Don't distribute plugins in the base package

* Fri May 27 2016 Petr Hracek <phracek@redhat.com> - 2016.1.4-1
- Update to the latest version 2016.1.4

* Fri May 20 2016 Petr Hracek <phracek@redhat.com> - 2016.1.3-2
- Update plugins Bash, Docker, MultiMarkdown

* Thu May 12 2016 Petr Hracek <phracek@redhat.com> - 2016.1.3-1
- Update to the latest version 2016.1.3

* Fri May 06 2016 Petr Hracek <phracek@redhat.com> - 2016.1.2-3
- SpecFile rewrite and add support for Docker Integration
- plugin Multimarkdown

* Thu May 05 2016 Petr Hracek <phracek@redhat.com> - 2016.1.2-2
- Add package pycharm-community-plugins which contains
  BashSupport, CppTools, markdown, Go, gitlab-integration

* Mon Apr 11 2016 Petr Hracek <phracek@redhat.com> - 2016.1.2-1
- Update to the latest version 2016.1.2

* Thu Apr 07 2016 Petr Hracek <phracek@redhat.com> - 2016.1.1-1
- Update to the latest version 2016.1.1

* Thu Mar 24 2016 Petr Hracek <phracek@redhat.com> - 2016.1-1
- Update to the latest version 2016.1

* Fri Jan 29 2016 Petr Hracek <phracek@redhat.com> - 5.0.4-1
- Update to the latest version, 5.0.4

* Mon Jan 04 2016 Petr Hracek <phracek@redhat.com> - 5.0.3-1
- update to the latest version, 5.0.3

* Fri Dec 11 2015 Allan Lewis <allanlewis@users.noreply.github.com> - 5.0.2-1
- update to the latest version, 5.0.2

* Tue Nov 17 2015 Allan Lewis <allanlewis@users.noreply.github.com> - 5.0.1-1
- update to the latest version, 5.0.1

* Thu Nov 05 2015 Petr Hracek <phracek@redhat.com> - 5.0-2
- Rebuild for Fedora 23

* Tue Nov 03 2015 Petr Hracek <phracek@redhat.com> - 5.0-1
- update to the latest version 5.0

* Tue Sep 08 2015 Petr Hracek <phracek@redhat.com> - 4.5.4-1
- update to the latest version 4.5.4

* Wed Jul 15 2015 Petr Hracek <phracek@redhat.com> - 4.5.3-1
- update to the latest version 4.5.3

* Tue Jun 30 2015 Petr Hracek <phracek@redhat.com> - 4.5.2-2
- pycharm.desktop fix done by Allan Lewis

* Mon Jun 29 2015 Allan Lewis <allanlewis@users.noreply.github.com> - 4.5.2-1
- update to the latest version 4.5.2

* Mon May 25 2015 Petr Hracek <phracek@redhat.com> - 4.5.1-1
- update to the latest version 4.5.1

* Thu Apr 16 2015 Petr Hracek <phracek@redhat.com> - 4.5-1
- update to the latest version 4.5

* Thu Apr 16 2015 Petr Hracek <phracek@redhat.com> - 4.0.6-1
- update to the latest version 4.0.6

* Wed Mar 25 2015 Petr Hracek <phracek@redhat.com> - 4.0.5-2
- Add metadata for Gnome Software Center

* Fri Mar 13 2015 Jiri Popelka <jpopelka@redhat.com> - 4.0.5-1
- update to the latest version 4.0.5

* Wed Feb 25 2015 Petr Hracek <phracek@redhat.com> - 4.0.4-2
- supports EPEL 7

* Tue Jan 20 2015 Petr Hracek <phracek@redhat.com> - 4.0.4-1
- update to the latest version 4.0.4

* Wed Dec 17 2014 Petr Hracek <phracek@redhat.com> - 4.0.3-1
- update to the latest version 4.0.3

* Tue Dec 16 2014 Petr Hracek <phracek@redhat.com> - 4.0.2-1
- update to the latest version 4.0.2

* Mon Dec 01 2014 Petr Hracek <phracek@redhat.com> - 4.0.1-1
- update to the latest version 4.0.1

* Fri Nov 21 2014 Petr Hracek <phracek@redhat.com> - 4.0-1
- new upstream version 4.0

* Fri Nov 07 2014 Tomas Hozza <thozza@redhat.com> - 3.4.1-3
- Install the icon with name used in .desktop file

* Thu Jul 31 2014 Tomas Tomecek <ttomecek@redhat.com> - 3.4.1-2
- new upstream version 3.4.1
- sanitize specfile

* Mon Jun 09 2014 Petr Hracek <phracek@redhat.com> - 3.4.1-1
- New upstream version

* Wed May 14 2014 Petr Hracek <phracek@redhat.com> - 3.1.3-1
- Initial package
