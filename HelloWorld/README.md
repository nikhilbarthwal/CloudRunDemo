## Build and push Docker image

In folder of your language of choice, build and push the container image defined by `Dockerfile`. Replace `{project-id}` with your Project name:

```sh
docker build -t gcr.io/{project-id}/helloworld:v1 .

docker push gcr.io/{project-id}/helloworld:v1
```

## Deploy the Knative service

After the container is pushed, deploy the Knative service:

```sh
kubectl apply -f service-v1.yaml
```

Check that pods are created and all Knative constructs (service, configuration, revision, route) have been deployed:

```sh
kubectl get pod,ksvc,configuration,revision,route

NAME                                                      READY     STATUS    RESTARTS
pod/helloworld-c4pmt-deployment-7fdb5c5dc9-wf2bp   3/3       Running   0

NAME
service.serving.knative.dev/helloworld

NAME
configuration.serving.knative.dev/helloworld

NAME
revision.serving.knative.dev/helloworld-00001

NAME
route.serving.knative.dev/helloworld
```

## Test the service

To test the service, we need to find the IP address of the Istio ingress gateway and the URL of the service.

The IP address of Istio ingress is listed under `EXTERNAL_IP`:

```bash
kubectl get svc istio-ingressgateway -n istio-system
```

Let's set this `EXTERNAL_IP` to an `ISTIO_INGRESS` variable:

```bash
export ISTIO_INGRESS=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
```

The URL of the service follows this format: `{service}.{namespace}.example.com`. In this case, we have `helloworld.default.example.com`.

Make a request to your service:

```bash
curl http://helloworld.default.$ISTIO_INGRESS.xip.io

Hello v1
```

