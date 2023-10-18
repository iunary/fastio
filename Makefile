.PHONY: build publish deploy argocd-create-app argocd-sync-app

build:
	@docker buildx build --platform linux/amd64 -t fastio -t qawba/fastio:latest .

publish:	
	@docker push qawba/fastio:latest

deploy:
	@helm upgrade --install fastio-app -f ./helm-chart -n default

argocd-create-app:
	@argocd app create fastio-app \
	--repo https://github.com/unary/fastio \
	--path helm-chart \
	--dest-server https://kubernetes.default.svc \
	--dest-namespace default \
	--sync-policy automated \
	--sync-option Validate=true \
	--sync-option Prune=true \
	--sync-option SelfHeal=true 

argocd-sync-app:
	@argocd app sync fastio-app