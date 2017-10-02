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

v. copy the pod_check folder into /opt/stackstorm/configs/ directory

vi. modify pod_check/actions/send_email.py to provide your gmail creds and the reciever email id

vii. To register a pack

st2ctl reload --register-all

# On Google cloud shell, change replication value from 3 to 6 in nginx.yml to test email getting generated

kubectl resize -f nginx.yml

# To delete the deployment

kubectl delete deployment <deployment name>
