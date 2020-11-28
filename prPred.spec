# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['prPred.py'],
             pathex=['./codes/', '/mnt/d/Wangys_data_postdoc/NLR_predictions/6_1_software/prPred'],
             binaries=[('/home/element/anaconda3/lib/libiomp5.so', '.')],
             datas=[],
             hiddenimports=['sklearn.neighbors.typedefs'],
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
          [],
          exclude_binaries=True,
          name='prPred',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='prPred')
