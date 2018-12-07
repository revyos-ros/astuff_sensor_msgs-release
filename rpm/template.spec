Name:           ros-melodic-delphi-srr-msgs
Version:        2.3.1
Release:        0%{?dist}
Summary:        ROS delphi_srr_msgs package

Group:          Development/Libraries
License:        MIT
URL:            http://wiki.ros.org/delphi_srr_msgs
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-message-runtime
Requires:       ros-melodic-std-msgs
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-message-generation
BuildRequires:  ros-melodic-std-msgs

%description
Message definitions for the Delphi SRR

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Fri Dec 07 2018 AutonomouStuff Software Development Team <support@autonomoustuff.com> - 2.3.1-0
- Autogenerated by Bloom

* Thu Oct 04 2018 AutonomouStuff Software Development Team <support@autonomoustuff.com> - 2.3.0-0
- Autogenerated by Bloom

* Thu Aug 30 2018 AutonomouStuff Software Development Team <support@autonomoustuff.com> - 2.2.2-0
- Autogenerated by Bloom

* Wed Aug 08 2018 AutonomouStuff Software Development Team <support@autonomoustuff.com> - 2.2.1-0
- Autogenerated by Bloom

* Tue Aug 07 2018 AutonomouStuff Software Development Team <support@autonomoustuff.com> - 2.2.0-0
- Autogenerated by Bloom

* Thu May 24 2018 AutonomouStuff Software Development Team <support@autonomoustuff.com> - 2.0.1-0
- Autogenerated by Bloom

