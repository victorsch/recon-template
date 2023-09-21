sudo apt-get update

sudo apt-get -y install golang
sudo apt-get -y install binutils

go install github.com/tomnomnom/anew@latest
go install github.com/tomnomnom/assetfinder@latest
go install github.com/tomnomnom/fff@latest
go install github.com/tomnomnom/gron@latest
go install github.com/tomnomnom/gf@latest
go install github.com/tomnomnom/httprobe@latest
go install github.com/tomnomnom/waybackurls@latestsudo vi

echo "export PATH=~/go/bin:$PATH" > ~/.zshrc
echo "export PATH=~/go/bin:$PATH" > ~/.bashrc