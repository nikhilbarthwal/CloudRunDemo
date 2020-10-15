# "to PDF" as a service

A simple web service that transforms the given document into a PDF file. 

Run with `docker run -p 8080:8080 gcr.io/nikhilbarthwal-knative/pdf`

### URL parameters:

* `input`: URL of the document to transform.

## Running the server locally

* Build with `docker build . -t pdf`
* Start with `docker run -p 8080:8080 pdf`
* Open in your browser at `http://localhost:8080/?url=http://homepages.inf.ed.ac.uk/neilb/TestWordDoc.doc`

## Deploy to your server

The following container image always reflects the latest version of the `master` branch of this repo: `gcr.io/nikhilbarthwal-knative/pdf`

## Deploy to Google Cloud

[![Run on Google Cloud](https://storage.googleapis.com/cloudrun/button.svg)](https://deploy.cloud.run)

Or use `gcloud beta run deploy --image gcr.io/nikhilbarthwal-knative/pdf`
