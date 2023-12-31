# Use Red Hat Universal Base Image (UBI) 9 as the base image
FROM fedora:latest

# Install Python 3 and pip
RUN yum install -y clang git ninja-build flex bison meson procps-ng

# Set the default command to run when the container starts
CMD ["/bin/bash"]
