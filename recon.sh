echo Grab a drink, this may take a while...
echo What will you be having?

read drink_name

echo Don't drink your $drink_name all at once, we'll be finished shortly.

sleep 2

cat wildcards | assetfinder --subs-only | anew domains

cat domains | httprobe -c 80 | anew hosts
#findomain -f wildcards | tee -a findomain.out

# anew only adds new lines, won't add duplicates
#cat findomain.out | anew domains | httprobe -c 50 | anew hosts

# goes through hosts and saves the body so you can grep through them
cat hosts | fff -d 1 -S -o roots

# fff made .headers and .body files, headers has the headers of the response and body has the body of the response
cd ..
aws s3 cp --recursive recon-template/roots s3://mass-recon-warehouse/`basename $PWD`
aws s3 cp recon-template/hosts s3://mass-recon-warehouse/`basename $PWD`/hosts
aws s3 cp recon-template/domains s3://mass-recon-warehouse/`basename $PWD`/domains
aws s3 cp recon-template/wildcards s3://mass-recon-warehouse/`basename $PWD`/wildcards