# Run Cloud Build
gcloud builds submit --tag gcr.io/nikhilbarthwal-knative/cloud-run-demo

#Deploy
gcloud beta run deploy --image gcr.io/nikhilbarthwal-knative/cloud-run-demo
