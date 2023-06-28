# DIS_PROJECT
Components involved : 

1 HaProxy running the given configuration file
2 Eclipse IDE running the given war file
3 NodeJS express server running the given index file
4 Python agent running on each machine involved
5 wrk2 benchmarking utility running given benchmarks




Install HaProxy on Linux according to instructions given below : 

1) apt-get install haproxy
2)nano /etc/default/haproxy
3)Set the ENABLED option to 1 , that is :- ENABLED=1
4)To check if this change is done properly execute the init script of HAProxy without any parameters. You should see the following. 
root@haproxy:~# service haproxy Usage: /etc/init.d/haproxy {start|stop|reload|restart|status}
5) Create and edit a new configuration file: sudo nano /etc/haproxy/haproxy.cfg
6) Copy paste the given haproxy.cfg file content into this newly created file or already existing file.
7) Replace the IP addresses of all the servers/machines involved with your IP addresses and ports

If you face any difficulty, please refer this website : https://www.digitalocean.com/community/tutorials/how-to-use-haproxy-to-set-up-http-load-balancing-on-an-ubuntu-vps





Setting up Eclipse IDE

Given the .war file for the Eclipse Dynamic Web project
Follow the steps as shown in the video below (Assumes that you have Apache Tomcat 8.5 installed): https://www.loom.com/share/541aa4603eba4b9e8d0cc0291c214d57




Setting up NodeJS express server:

Make sure you have installed Node first: node -v

Initiate a project : npm init -y

Install the dependencies - 
npm install express@4.17.1
npm install connect-timeout
Do npm install "whatever additional dependency you have"

Copy paste the given index.js file

node index.js




Setting up load feedback agent:

Copy paste the python_agent.py anywhere
And run python3 python_agent.py
You have to run this agent on as many different machines you are using


Setting up wrk2 benchmarking utility:

git clone https://github.com/giltene/wrk2.git
cd wrk2
make
here copy paste the given test_request.lua file

then you can run the following commands


For java web servers - 

Generate heavy load : wrk -t2 -c100 -d30s -R500 -s test_request.lua http://localhost:80/TESTSERVER/testapi
Generate small load : wrk -t2 -c10 -d30s -R50 -s test_request.lua http://localhost:80/TESTSERVER/testapi

For Node web servers - 

Generate heavy load : wrk -t2 -c100 -d30s -R500 -s test_request.lua http://localhost:80/NODESERVER/testapi
Generate small load : wrk -t2 -c10 -d30s -R50 -s test_request.lua http://localhost:80/NODESERVER/testapi

You have to make sure that you are running these commands on the same machihne as your load balancer otherwise you will have to change the "localhost" in above commands to "load-balancer-ip-address"

You can always go to localhost://8404
This will show you the HaProxy statistics page which shows in great detail the stats about the load balancer.
There you can analyze the Total number of requests send and how many went to each server involved.