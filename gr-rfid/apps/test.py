from contextlib import redirect_stdout
import io
import sys

with io.StringIO() as buf, redirect_stdout(buf):
    print('redirected')
    output = buf.getvalue()

print(output)
