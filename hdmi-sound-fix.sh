#!/bin/bash
# hdmi keepalive
aplay -q -c1 -r16000 -fS16_LE < /dev/zero &
