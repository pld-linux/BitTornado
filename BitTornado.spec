Summary:	BitTornado is an improved bittorrent client
Summary(pl):	BitTornado jest ulepszym klientem bittorrenta
Name:		BitTornado
Version:	0.3.7
Release:	1
License:	MIT
Group:		Applications/Communications
Source0:	http://e.scarywater.net/bt/download/%{name}-%{version}.tar.gz
# Source0-md5:	ffeccfa4ee6a5732ea036332ccf34e92
URL:		http://bittornado.com/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov 
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
Requires:	python-modules
BuildArch:	noarch
Obsoletes:	BitTorrent
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BitTornado is an improved bittorrent client that was built on the original
BitTorrent. This client features an enhanced console/curses mode, lots of new
features under the hood, and is generally one of the most advanced clients out
there. It allows you to limit your bandwidth consumption, and provides more
control over your torrents. It does everything the original bittorrent does,
plus more.

%description -l pl
BitTornado jest ulepszonym klientem bittorrenta zbudowanym bazuj±c na oryginalnym BitTorrent. Klient charakteryzuje siê rozszerzon± obs³ug± konsoli, kilkoma nowymi w³a¶ciwo¶ciami i jest generalnie jednym z bardziej zaawansowanych klientów bittorrenta. Pozwala ograniczaæ przepustowo¶æ oraz udostêpnia du¿± kontrolê nad torrentami. Umie wszystko co umia³ oryginalny klient bittorrenta i jeszcze troszkê wiêcej.

%package gui
Summary:	GUI for BitTornado
Summary:	Graficzny interfejs u¿ytkownika dla BitTornado
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	python-wxPython
Obsoletes:	BitTorrent-gui

%description gui
wxWindows based GUI for BitTorrent.

%description gui -l pl
Bazuj±cy na wxWindows graficzny interfejs u¿ytkownika dla BitTorrenta.

%prep
%setup -q -n %{name}-CVS

%build
find -type f -exec sed -i -e 's|#!.*python.*|#!%{_bindir}/python|g' "{}" ";"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

python ./setup.py install --optimize=2 --root=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT%{py_sitescriptdir} -type f -name "*.py" | xargs rm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt 
%attr(755,root,root) %{_bindir}/btcompletedir.py
%attr(755,root,root) %{_bindir}/btdownloadcurses.py
%attr(755,root,root) %{_bindir}/btdownloadheadless.py
%attr(755,root,root) %{_bindir}/btlaunchmany*.py
%attr(755,root,root) %{_bindir}/btmakemetafile.py
%attr(755,root,root) %{_bindir}/btr*.py
%attr(755,root,root) %{_bindir}/btt*.py
%attr(755,root,root) %{_bindir}/btshowmetainfo.py
%attr(755,root,root) %{_bindir}/btsethttpseeds.py
%attr(755,root,root) %{_bindir}/btcopyannounce.py
%{py_sitescriptdir}/%{name}/

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/btdownloadgui.py
%attr(755,root,root) %{_bindir}/btcompletedirgui.py
%attr(755,root,root) %{_bindir}/btmaketorrentgui.py
%attr(755,root,root) %{_bindir}/bt-t-make.py
