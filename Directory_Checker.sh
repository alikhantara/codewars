#!/bin/bash
#Set Correct Path for Monitored Directory
source_dir="/path/to/source/directory"
dest_server="username@destination-server:/path/to/destination/directory"
#Set Password for Archive
arch_password="Password123"


inotifywait -m -e CREATE --format "%w%f" "$source_dir" | while read new_file
do
    rsync -avz --progress "$new_file" "$dest_server"
    zip -P "$arch_password" archive-$(date +"%FT%T").zip "$new_file"
    echo "File $new_file Moved to $dest_server"
done
