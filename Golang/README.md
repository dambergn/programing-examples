# Golang
https://www.youtube.com/watch?v=YS4e4q9oBaU  
https://www.youtube.com/watch?v=SqrbIlUwR0U  
Go is a compilled language built by Google.

## Installation
https://golang.org/doc/install  
https://golang.org/dl/go1.16.5.linux-amd64.tar.gz  
```bash
wget https://golang.org/dl/go1.16.5.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.16.5.linux-amd64.tar.gz
export PATH=$PATH:/usr/local/go/bin/usr
cd ~
sudo nano .bashrc

# Golang
export GOROOT=/usr/local/go
export PATH=$PATH:$GOROOT/bin

source ~/.bashrc
go version

# Set up a project folder (note:do not use spaces)
cd ~
mkdir go
cd go
mkdir bin pkg src
cd src
mkdir github.com
cd github.com
mkdir "your github username"
cd "your github username"
mkdir "project name"

```