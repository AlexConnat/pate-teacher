# Pate-Teacher

### Init Script 

```
#!/bin/bash
sudo apt update
sudo apt install -y python python-pip
git clone https://github.com/AlexConnat/pate-teacher
cd pate-teacher/
pip --no-cache-dir install -r requirements.txt
./script_train_teacher.sh
```
