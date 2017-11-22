#FROM ubuntu:14.04
FROM ubuntu:latest
 
RUN apt update
RUN apt upgrade -y
 
RUN apt install -y nodejs
 
# needs this to find the nodejs exec
RUN ln -s /usr/bin/nodejs /usr/bin/node
 
RUN apt install -y npm
#RUN /usr/bin/npm install ws
#RUN /usr/bin/npm install node-static
COPY app /root/
 
EXPOSE 8080
EXPOSE 80
 
ENTRYPOINT ["/usr/bin/node" , "--harmony", "/root/server.js"]

