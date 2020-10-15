# Run Cloud Build
gcloud builds submit --tag gcr.io/nikhilbarthwal-knative/hello-world

#Deploy
gcloud beta run deploy --image gcr.io/nikhilbarthwal-knative/hello-world

