# sys.spec

# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['sys.py'],  # Cambia 'my_program.py' por el nombre de tu archivo Python
             pathex=['.'],  # Ruta de búsqueda
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
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
          name='sys',  # Cambia 'my_program' por el nombre de tu ejecutable
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,  # Cambia a False si no necesitas una consola
          icon='OIG2.ico')  # Cambia la ruta al icono

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='sys')  # Cambia 'my_program' por el nombre de tu carpeta de salida
