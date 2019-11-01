echo "from .base import *

from .production import *

try:
   from .local import *
except:
   pass
" > __init__.py