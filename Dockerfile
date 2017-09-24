FROM misli/django-cms-site

MAINTAINER Jakub Dorňák <jakub.dornak@misli.com>

# install other dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# copy files
COPY suncha /app/suncha

ENV SITE_MODULE=suncha

# run this command at the end of any dockerfile based on this one
RUN django-cms collectstatic --no-input
