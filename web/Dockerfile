FROM littlekbt/rails:5.1.4-alpine
MAINTAINER littlekbt

RUN apk update && apk add mysql-dev

WORKDIR /cloud-billing-web
ADD . /cloud-billing-web
RUN bundle install
# buildするたびにbundle install しないといけないため、必要。
# ただし最初はGemfileがないため、要検討
