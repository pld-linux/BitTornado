Summary:	BitTornado - an improved bittorrent client
Summary(pl.UTF-8):	BitTornado - ulepszony klient bittorrenta
Name:		BitTornado
Version:	0.3.18
Release:	1
License:	MIT
Group:		Applications/Communications
Source0:	http://download2.bittornado.com/download/%{name}-%{version}.tar.gz
# Source0-md5:	faeb137036cfaaeab91afc7f62c7dc30
URL:		http://bittornado.com/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
%pyrequires_eq	python-modules
Obsoletes:	BitTorrent < 4.2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BitTornado is an improved bittorrent client that was built on the
original BitTorrent. This client features an enhanced console/curses
mode, lots of new features under the hood, and is generally one of the
most advanced clients out there. It allows you to limit your bandwidth
consumption, and provides more control over your torrents. It does
everything the original bittorrent does, plus more.

%description -l pl.UTF-8
BitTornado jest ulepszonym klientem bittorrenta zbudowanym bazując na
oryginalnym BitTorrent. Klient charakteryzuje się rozszerzoną obsługą
konsoli, kilkoma nowymi właściwościami i jest generalnie jednym z
bardziej zaawansowanych klientów bittorrenta. Pozwala ograniczać
przepustowość oraz udostępnia dużą kontrolę nad torrentami. Umie
wszystko co umiał oryginalny klient bittorrenta i jeszcze troszkę
więcej.

%package gui
Summary:	GUI for BitTornado
Summary(pl.UTF-8):	Graficzny interfejs użytkownika dla BitTornado
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	python-wxPython >= 2.5.2
Obsoletes:	BitTorrent-gui < 4.2.0

%description gui
wxWindows based GUI for BitTorrent.

%description gui -l pl.UTF-8
Bazujący na wxWindows graficzny interfejs użytkownika dla BitTorrenta.

%prep
%setup -q -n %{name}-CVS
# enabled Psyco
%{__sed} -i 's,^psyco = 0,psyco = 1,' BitTornado/PSYCO.py

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
%{py_sitescriptdir}/%{name}

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/btdownloadgui.py
%attr(755,root,root) %{_bindir}/btcompletedirgui.py
%attr(755,root,root) %{_bindir}/btmaketorrentgui.py
%attr(755,root,root) %{_bindir}/bt-t-make.py
