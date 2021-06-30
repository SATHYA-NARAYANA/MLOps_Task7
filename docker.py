#!/usr/bin/python3
import cgi
import subprocess

print("content-type: text/html")
#Access-Control-Allow-Origin response header indicates whether the response can be shared with requesting code from the given origin.
# For requests without credentials, the literal value "*" is used
print("Access-Control-Allow-Origin: *")
# for differentiating header and body
print() 

form = cgi.FieldStorage()
cmd = form.getvalue("x")

x=subprocess.getoutput("sudo {}".format(cmd))
print(x)
'''
val = cmd.split()

#launch a new container
if  val[0]=="1":
    
    cname = val[2]
    iname = val[1]
    o=sp.getoutput("sudo docker run -dit --name={} {}".format(cname,iname)) 
    print(o)

#stop running container
elif  val[0]=="2":
   
    cname = val[1]
    o=sp.getoutput("sudo  docker stop {} ".format(cname)) 
    print(o)

#Delete container
elif  val[0]=="3":
    cname = val[1]
    o=sp.getoutput("sudo docker rm -f {}".format(cname))
    print(o)

#Download an image
elif  val[0]=="4":
    dname = val[1]
    o=sp.getoutput("sudo docker pull {}".format(dname))
    print(o)

#Execute a shell
elif  val[0]=="5":
  
    cname = val[1]
    o=sp.getoutput("sudo docker exec -dit {} ".format(cname))
    print(o)
    
#list running container
elif  val[0]=="6":
   
    o=sp.getoutput("sudo docker ps") 
    print(o)

#list all the container
elif val[0]=="7":
    o=sp.getoutput("sudo docker ps -a") 
    print(o)

#List all images
elif val[0]=="8":
    o=sp.getoutput("sudo docker images") 
    print(o) 


elif val[0]=="9":
     
    print("Thank you for Docker Assistance !!!!! OK bye") 

else:
    val[0]=="404"
    print("Sorry you have entered an incorrect option")
'''