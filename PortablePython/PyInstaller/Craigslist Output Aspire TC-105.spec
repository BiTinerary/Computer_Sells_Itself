# -*- mode: python -*-

block_cipher = None


a = Analysis(['C:\\Users\\Zack\\Desktop\\Newfolder/Craigslist Output Aspire TC-105.py'],
             pathex=['C:\\Users\\Zack\\Desktop\\Newfolder/PortablePython/PyInstaller/'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
             excludes=None,
             cipher=block_cipher)
pyz = PYZ(a.pure,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Craigslist Output Aspire TC-105.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
