echo "This script will install zfind on your device and also add it to path"
echo "Installing Python if not already installed"
sudo apt update
sudo apt install python3-full
git clone https://github.com/itsmehecker/zfind-python.git
cd zfind-python
chmod +x start.sh
sudo ./start.sh
