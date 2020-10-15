# Run Cloud Build
gcloud builds submit --tag gcr.io/nikhilbarthwal-cloudrun-demo/hello-world

#Deploy
gcloud beta run deploy --image gcr.io/nikhilbarthwal-cloudrun-demo/hello-world

