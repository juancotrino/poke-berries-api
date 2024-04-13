# Define custom function directory
ARG FUNCTION_DIR="/prod"

FROM python:3.11 AS build-image

# Include global arg in this stage of the build
ARG FUNCTION_DIR

# Copy function code
RUN mkdir -p ${FUNCTION_DIR}
COPY app ${FUNCTION_DIR}/app
COPY utils ${FUNCTION_DIR}/utils
COPY static/images ${FUNCTION_DIR}/static/images
COPY main.py ${FUNCTION_DIR}
COPY docs.py ${FUNCTION_DIR}
COPY requirements.txt ${FUNCTION_DIR}

# Install the function's dependencies, including your own package
RUN pip install \
    --target ${FUNCTION_DIR} \
        awslambdaric

RUN pip install -r ${FUNCTION_DIR}/requirements.txt \
    --target ${FUNCTION_DIR}

# COPY orm.py ${FUNCTION_DIR}/sqlalchemy_utils/functions/orm.py

# Use a slim version of the base Python image to reduce the final image size
FROM python:3.11-slim

# Include global arg in this stage of the build
ARG FUNCTION_DIR

# Set working directory to function root directory
WORKDIR ${FUNCTION_DIR}

# Copy in the built dependencies
COPY --from=build-image ${FUNCTION_DIR} ${FUNCTION_DIR}

# Update libraries
RUN apt-get update

# Set runtime interface client as default command for the container runtime
ENTRYPOINT [ "/usr/local/bin/python", "-m", "awslambdaric" ]
# Pass the name of the function handler as an argument to the runtime
CMD [ "main.handler" ]
