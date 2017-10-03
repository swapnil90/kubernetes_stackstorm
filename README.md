# Commands to Execute on google cloud shell

gcloud config set compute/zone us-central1-a
gcloud container clusters create nginx-cluster

# Create a nigix and stackstorm deployment

kubectl apply -f nginx.yml
kubectl apply -f stackstorm.yml

# ssh into stackstorm pod

i. get stackstorm pod name

kubectl get pods --all-namespaces

ii. ssh into it

kubectl exec -it <pod name> -- /bin/bash 

iii. Run following command on the stackstorm container:-

apt-get install python-pip
pip install kubernetes st2client argcomplete pytz python-editor jsonschema prompt_toolkit

iv. copy ~/.kube/config from google cloud shell into stackstorm pod or refer to https://cloud.google.com/sdk/docs/quickstart-debian-ubuntu for installation and configuration and configure kubectl using command `gcloud container clusters get-credentials nginx-cluster --zone us-central1-a --project <project id>` got from clicking on connect button under clusters on google cloud site

v. modify pod_check/actions/send_email.py to provide your gmail creds and the reciever email id

vi. any one of the above 2 ways can be used to register a pack

1. copy the pod_check folder into /opt/stackstorm/configs/ directory and register it as follows:-

st2ctl reload --register-all

2. Directly install it from the git repo:-

st2 pack install <path to pod_check folder>/pod_check

# On Google cloud shell, resize replication from 3 to 6 using following command

kubectl scale --replicas=6 -f nginx.yml

# To delete the deployment

kubectl delete deployment <deployment name>
