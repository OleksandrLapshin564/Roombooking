#!/usr/bin/env bash
# wait-for-it.sh - waits for a TCP host:port to become available

set -e

if [ "$#" -lt 2 ]; then
    echo "Usage: $0 host:port command [args...]"
    exit 1
fi

hostport="$1"
shift
cmd="$@"

host=$(echo $hostport | cut -d: -f1)
port=$(echo $hostport | cut -d: -f2)

echo "Waiting for $host:$port to be available..."

while ! nc -z "$host" "$port"; do
    echo "Waiting for $host:$port..."
    sleep 1
done

echo "$host:$port is available, starting command..."
exec $cmd
