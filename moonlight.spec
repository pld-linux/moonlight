Summary:	Moonlight Atelier - 3D Modeller
Summary(pl):	Moonlight Atelier - Modeler 3D
Name:		moonlight
Version:	0.9.2
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://moonlight3d.net/download/%{name}-setup-%{version}-beta.tar.gz
# Source0-md5:	740ce9efe5ea21cb32c9abf8a01702ac
URL:		http://moonlight3d.net/
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Moonlight3D is a free of charge modeller for 3-dimensional art. It
supports Nurbs- and Beziercurve based modelling.

%description -l pl
Moonlight3D jest darmowym modelerem 3D. Wspiera modelowanie bazuj±ce
na krzywych NURBS i Beziera.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
%{__make} RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
%attr(,,)
