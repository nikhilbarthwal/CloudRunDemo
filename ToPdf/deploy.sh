# Run Cloud Build
gcloud builds submit --tag gcr.io/nikhilbarthwal-cloudrun-demo/cloud-run-demo-nbarthwal

#Deploy
gcloud beta run deploy --image gcr.io/nikhilbarthwal-cloudrun-demo/cloud-run-demo-nbarthwal
