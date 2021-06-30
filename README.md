# MLOps_Task7
In this task you have to create a Web Application for Docker (one of the great Containerization Tool which provides the user Platform as a Service (PaaS)) by showing your own creativity and UI/UX designing skills to make the webportal user friendly.  
📌 This app will help the user to run all the docker commands like:  

👉docker images 

👉docker ps   

👉docker run   

👉docker rm -f 

👉docker exec 

👉 add more if you want. (Optional) 

Video Demo:https://youtu.be/sfbOMlR1eiY

# Steps for running Docker command in web UI:
## step 1: 
 1.Install Docker in your system
 2.Install httpd server(Apache)
 3.Install python
 
## Step 2:
 1.Create a python CGI program for server side and save it in /var/www/cgi-bin folder with docker.py extension
 
 ## Step 3: 
 
 1. Create a web UI with HTML, CSS, Js or any other front UI 

## Step 4: 
1.Go to /etc/sudoers and add apache services to run as admin powers and save it 
2. Start Docker services and Apache Webserver 

## Step 5: 
1. Stop firewalls using Systemctl stop firewalld command
2. Stop selinux using setenforce 0 command
3. Now run Docker Server and Apache webserver 
4. Optain IP address of webserver 
5. Give Ip address to your friend and tell them to run Docker commands in Web UI .


# THANK YOU...
