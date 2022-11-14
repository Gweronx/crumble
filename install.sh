echo "NOTE: install.sh needs the Github CLI to be installed for it to work!"
cd $HOME
mkdir CRUMBLE
cd CRUMBLE  
gh repo clone Gweronx/crumble
cd crumble
chmod +x crumble.py
echo 'export PATH="$HOME/CRUMBLE/crumble:$PATH"' >> ~/.bashrc
