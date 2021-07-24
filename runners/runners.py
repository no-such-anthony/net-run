from runners.runners_base import WithThreadPool, WithLoop
from runners.runners_async import WithSemaphore


runners = { 'async': WithSemaphore,
            'serial': WithLoop,
            'threads': WithThreadPool,
            'default': WithThreadPool,
            }