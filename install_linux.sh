echo "This script will install zfind on your device and also add it to path"
echo "Installing Python if not already installed"
sudo apt update
sudo apt install python3-full
git clone https://github.com/itsmehecker/zfind-python.git
cd zfind-python
echo "Creating virtual Environment"
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
chmod +x start.sh
sudo ./start.sh
