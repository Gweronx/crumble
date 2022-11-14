echo "NOTE: install.sh needs the Github CLI to be installed for it to work!"
cd $HOME
mkdir CRUMBLE
cd CRUMBLE  
gh repo clone Gweronx/crumble
cd crumble
echo "python3 main.py $1" >> crumble
chmod +x crumble
echo 'export PATH="$HOME/CRUMBLE/crumble:$PATH"' >> ~/.bashrc
