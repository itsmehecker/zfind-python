git clone https://github.com/itsmehecker/zfind-python.git
cd zfind-python
echo "Creating virtual Environment"
python3 -m venv venv
. venv/Scripts/activate
pip install -r requirements.txt
chmod +x start.sh
sudo ./start.sh
