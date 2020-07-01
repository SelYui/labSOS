# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

added_files = [
         ( 'lib\\lab1_setting.ini', 'lib' ),
		 ( 'lib\\lab2_setting.ini', 'lib' ),
		 ( 'lib\\setting.log', 'lib' ),
		 ( 'lib\\library.ico', 'lib' )
         ]

a = Analysis(['labsos.py'],
             pathex=['C:\\py_virtual\\project\\labSOS'],
             binaries=[],
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
          console=False, icon='D:\\icon\\library.ico' )
