# Commands to Execute on google cloud shell

gcloud config set compute/zone us-central1-a
gcloud container clusters create nginx-cluster

# Create a nigix deployment

kubectl apply -f nginx.yml

# create a vm with ubuntu 14.04 image ssh into stackstorm

i. Run following command on the stackstorm container:-

curl -sSL https://stackstorm.com/packages/install.sh | bash -s -- --user=st2admin --password='Ch@ngeMe'
sudo apt-get install python-pip
pip install kubernetes st2client argcomplete pytz python-editor jsonschema prompt_toolkit

ii. install google cloud SDK setup using following link:-  https://cloud.google.com/sdk/docs/quickstart-debian-ubuntu

iii. configure it as follows
gcloud init

iv. get the gcloud container clusters command from clicking on connect button under clusters on google cloud site
gcloud container clusters get-credentials cluster-1 --zone us-central1-a --project <project id>   
sudo apt-get install kubectl


v. verify config file has proper creds using any kubectl command and copy the .kube folder from current users home directory to st2 user and then give 777 permission to the kube directory and config file
kubectl cluster-info 
sudo cp -r ~/.kube /home/st2/
sudo chmod 777 /home/st2/.kube
sudo chmod 777 /home/st2/.kube/config
st2 run packs.setup_virtualenv packs=pod_check

vi. modify pod_check/actions/send_email.py to provide your gmail creds and the reciever email id ans enable IMAP access and enable access for less secure apps for your gmail account.
1. IMAP access enable reference:- https://support.google.com/mail/answer/7126229?visit_id=1-636427416327709909-85869891&rd=1
2. Access for less secure apps:- https://support.google.com/accounts/answer/6010255?hl=en

vii.  copy the pod_check folder into /opt/stackstorm/configs/ directory and register it as follows:-

st2ctl reload --register-all

viii. registry for sensor,trigger,rule and action can be verified as follows:-
st2 trigger list | grep pod_check
st2 sensor list | grep pod_check
st2 action list | grep pod_check
st2 rule list | grep pod_check

# On Google cloud shell, resize replication from 3 to 6 using following command

kubectl scale --replicas=6 -f nginx.yml
 

ix. confirm trigger is triggered by using following command when replication goes above 5:-
st2 trigger-instance list --trigger pod_check.event1 -n 20 

x. a mail will be sent to recievers email id with message format :- Replication count exceed 5, current count is X

xi. In case you want to see trigger details or logs of sensors, trigger, rule getting applied and alarm getting trigger and parameters and data passed to it

1. st2-rule-tester --rule=/opt/stackstorm/packs/pod_check/rules/rule1.yaml --trigger-instance-id=<trigger id got from commmand in point ix> --config-file=/etc/st2/st2.conf
2. In /var/log/st2/ check st2sensorcontainer.log, st2rulesengine.log, s2actionrunner.xx[0-9]xx.log

# To delete the deployment

kubectl delete deployment <deployment name>
