# -*- mode: python -*-

block_cipher = None


a = Analysis(['/Users/mdobbali/Google', 'Drive/2017/Work_2.0/Git/URLChecker/ui.py'],
             pathex=['/Users/mdobbali/Google Drive/2017/Work_2.0/Git/URLChecker'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Google',
          debug=False,
          strip=False,
          upx=True,
          console=True )