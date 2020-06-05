# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

added_files = [
         ( 'lib\\lab1_setting.ini', 'lib' ),
		 ( 'lib\\lab2_setting.ini', 'lib' ),
		 ( 'lib\\setting.log', 'lib' ),
		 ( 'lib\\RosAtom_logo_rus.ico', 'lib' )
         ]
		 
add_bins = [
			( 'wow64.dll', '.' ),
			( 'wow64win.dll', '.' ),
			( 'wow64cpu.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\combase.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\win32u.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\gdi32full.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\msvcp_win.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\shcore.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\windows.storage.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\UMPDC.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\kernel.appcore.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\winmmbase.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\dxcore.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\dataexchange.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\dcomp.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\twinapi.appcore.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\RMCLIENT.dll', '.' ),
			( 'C:\\Windows\\SYSTEM32\\ntdll.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\ntdll.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\KERNEL32.DLL', '.' ),
			( 'C:\\Windows\\SysWOW64\\KERNELBASE.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\ADVAPI32.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\msvcrt.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\sechost.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\RPCRT4.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\SspiCli.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\CRYPTBASE.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\bcryptPrimitives.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\WS2_32.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\SHLWAPI.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\ucrtbase.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\VERSION.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\GDI32.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\USER32.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\IMM32.DLL', '.' ),
			( 'C:\\Windows\\SysWOW64\\CRYPTSP.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\rsaenh.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\bcrypt.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\ole32.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\OLEAUT32.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\IPHLPAPI.DLL', '.' ),
			( 'C:\\Windows\\SysWOW64\\SHELL32.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\cfgmgr32.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\UxTheme.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\profapi.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\powrprof.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\dwmapi.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\d3d11.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\dxgi.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\MSVCP140.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\MPR.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\USERENV.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\NETAPI32.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\WINMM.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\SRVCLI.DLL', '.' ),
			( 'C:\\Windows\\SysWOW64\\NETUTILS.DLL', '.' ),
			( 'C:\\Windows\\SysWOW64\\CRYPT32.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\MSASN1.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\WTSAPI32.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\dwrite.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\d3d9.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\MSCTF.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\clbcatq.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\TextInputFramework.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\CoreMessaging.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\CoreUIComponents.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\ntmarta.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\wintypes.dll', '.' ),
			( 'C:\\Windows\\SysWOW64\\iertutil.dll', '.' )
			#( '', '.' ),
			]

a = Analysis(['labsos.py'],
             pathex=['C:\\py_virtual\\build_env\\progect\\labSOS'],
             binaries=add_bins,
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='lab_SOS',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False, icon='C:\\py_virtual\\build_env\\progect\\labSOS\\lib\\RosAtom_logo_rus.ico' )