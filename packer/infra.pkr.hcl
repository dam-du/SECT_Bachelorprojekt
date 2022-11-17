packer {
  required_plugins {
    docker = {
      version = ">= 0.0.7"
      source  = "github.com/hashicorp/docker"
    }
  }
}

source "docker" "debian" {
  image  = "debian:10"
  commit = true
}

build {
  name = "debian-honeypot"
  sources = [
    "source.docker.debian",
  ]

  provisioner "shell" {
    scripts = [
      "./scripts/os_install_update.sh",
      "./scripts/os_install_dependencies.sh",
    ]
  }

  provisioner "shell" {
    inline = [
      "groupadd -r -g 1000 cowrie",
      "useradd -r -u 1000 -d /home/cowrie -m -g cowrie cowrie",
      "apt-get install authbind",
      "touch /etc/authbind/byport/22",
      "chown cowrie:cowrie /etc/authbind/byport/22",
      "chmod 770 /etc/authbind/byport/22",
    ]
  }

  provisioner "file" {
    source      = "./upload/honeypot/"
    destination = "/home/cowrie/"
  }

  provisioner "shell" {
    scripts = [
      "./scripts/setup_cowrie.sh",
      "./scripts/setup_iptables.sh",
      "./scripts/setup_honeypot_libs.sh",
    ]
  }

  post-processor "docker-tag" {
    repository = "honeypot_image"
    tags       = ["latest"]
    only       = ["docker.debian"]
  }
}

build {
  name = "debian-attacker"
  sources = [
    "source.docker.debian",
  ]

  provisioner "shell" {
    scripts = [
      "./scripts/os_install_update.sh",
      "./scripts/os_install_dependencies.sh",
      "./scripts/setup_attacker-env.sh",
      "./scripts/setup_iptables.sh",
    ]
  }

  provisioner "file" {
    source      = "./upload/testcase"
    destination = "/"
  }

  post-processor "docker-tag" {
    repository = "attacker_image"
    tags       = ["latest"]
    only       = ["docker.debian"]
  }
}
