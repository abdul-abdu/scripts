import os

os.system("cd ~/Dev")
os.system("echo 'Enter App Name'")
os.system("read app_name")
os.system("mkdir $app_name")
os.system("cd $app_name")
os.system("gh repo clone abdugaffor-abdurahimov/type-node-starter .")
os.system("rm -rf README.md")
os.system("npm i")
os.system("git init")
os.system("echo '# $app_name' >> README.md")
os.system("echo 'Description'")
os.system("read description")
os.system("gh repo create $app_name -y -d '$description' --public")
os.system("git add .")
os.system("git commit -m 'first commit'")
os.system("git branch -M main")
os.system("git push -u origin main")
os.system("code .")
