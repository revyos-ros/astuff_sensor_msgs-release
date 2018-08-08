Name:           ros-indigo-astuff-sensor-msgs
Version:        2.2.1
Release:        1%{?dist}
Summary:        ROS astuff_sensor_msgs package

Group:          Development/Libraries
License:        MIT
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-delphi-esr-msgs
Requires:       ros-indigo-delphi-srr-msgs
Requires:       ros-indigo-derived-object-msgs
Requires:       ros-indigo-ibeo-msgs
Requires:       ros-indigo-kartech-linear-actuator-msgs
Requires:       ros-indigo-mobileye-560-660-msgs
Requires:       ros-indigo-neobotix-usboard-msgs
Requires:       ros-indigo-pacmod-msgs
Requires:       ros-indigo-radar-msgs
BuildRequires:  ros-indigo-catkin

%description
Messages specific to AStuff-provided sensors.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Aug 08 2018 AutonomouStuff Software Development Team <software@autonomoustuff.com> - 2.2.1-1
- Autogenerated by Bloom

* Wed Aug 08 2018 AutonomouStuff Software Development Team <software@autonomoustuff.com> - 2.2.1-0
- Autogenerated by Bloom

* Tue Aug 07 2018 AutonomouStuff Software Development Team <software@autonomoustuff.com> - 2.2.0-0
- Autogenerated by Bloom

* Wed Apr 25 2018 AutonomouStuff Software Development Team <software@autonomoustuff.com> - 2.0.1-0
- Autogenerated by Bloom

