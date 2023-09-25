echo Grab a drink, this may take a while...

sleep 2

cat wildcards | assetfinder --subs-only | anew domains

cat domains | httprobe -c 80 | anew hosts
#findomain -f wildcards | tee -a findomain.out

# anew only adds new lines, won't add duplicates
#cat findomain.out | anew domains | httprobe -c 50 | anew hosts

# goes through hosts and saves the body so you can grep through them
cat hosts | fff -d 1 -S -o roots

# get interesting status codes on each host
# loop through each host one at a time and run gobuster, save output to file
for host in $(cat hosts); do
    echo $host
    gobuster dir -u $host -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 50 -o $host.gobuster
done


# fff made .headers and .body files, headers has the headers of the response and body has the body of the response

aws s3 cp --recursive roots s3://mass-recon-warehouse/`basename $PWD`
aws s3 cp hosts s3://mass-recon-warehouse/`basename $PWD`/
aws s3 cp domains s3://mass-recon-warehouse/`basename $PWD`/
aws s3 cp wildcards s3://mass-recon-warehouse/`basename $PWD`/