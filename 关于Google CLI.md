

### 配置安装Google CLI

gcloud CLI 允许创建和管理多个配置文件。配置是一组命名的 gcloud CLI 属性，这些属性是按部分组织的键值对，用于控制 gcloud CLI 的行为。例如，可以在配置中设置默认的 Compute Engine 区域、详细程度级别、使用报告、项目 ID 和活动用户或服务帐户等属性。

配置存储在您的用户配置目录中（通常为 MacOS 和 Linux 上的 `~/.config/gcloud` 或 Windows 上的 `%APPDATA%\\gcloud`）；您可以通过运行 `gcloud info --format='value (config.paths.global_config_dir)'` 来查找配置目录的位置。您可以通过设置环境变量 `CLOUDSDK_CONFIG` 来更改配置目录。另外，请注意，配置目录必须具有写入权限

Google CLI 对python版本的要求是Python3.5到Python3.9，需创建在自己目录下，并将`CLOUDSDK_PYTHON` 环境变量设置为下载的路径



按照以下步骤在服务器上安装 Google Cloud SDK（也称为 Google CLI）：

##### 1.在文件夹中创建一个新目录，用于存放 Google Cloud SDK 的安装文件

```shell
mkdir google-cloud-sdk
cd google-cloud-sdk
```

##### 2.下载 Google Cloud SDK 的安装包。访问 Google Cloud 官网（https://cloud.google.com/sdk/docs/install）查找最新版本的下载链接，或者直接运行以下命令来下载适用于 Linux 64 位系统的安装包：

```shell
curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-440.0.0-linux-x86_64.tar.gz
```

#####  3.解压缩安装包并进入解压后的目录：

```shell
tar xvf google-cloud-sdk-440.0.0-linux-x86_64.tar.gz
cd google-cloud-sdk
```

#####  4.设置 `CLOUDSDK_PYTHON` 环境变量，指定使用 `/work/stu/gaojinhui/python3.9/bin/python3` 作为默认的 Python 解释器：

```shell
export CLOUDSDK_PYTHON=/work/stu/gaojinhui/python3.9/bin/python3
```

#####  5.运行安装脚本：

```shell
./install.sh
```

#####  6.安装完成后，将 gcloud CLI 添加到您的环境变量中，以便在命令行中直接使用 gcloud 命令。按照安装脚本的提示进行操作，或者手动修改shell 配置文件（例如 `.bashrc` 或 `.zshrc`），在其中添加以下内容：

```shell
# The next line updates PATH for the Google Cloud SDK.
if [ -f '$HOME/google-cloud-sdk/path.bash.inc' ]; then . '$HOME/google-cloud-sdk/path.bash.inc'; fi

# The next line enables shell command completion for gcloud.
if [ -f '$HOME/google-cloud-sdk/completion.bash.inc' ]; then . '$HOME/google-cloud-sdk/completion.bash.inc'; fi
```

#####  然后，重新加载您的 shell 配置文件，或者重新打开一个命令行窗口，即可开始使用 gcloud 命令进行初始化

```shell
gcloud iniit
```

### 更新下载数据集

Google Cloud Storage 的下载需要通过 `gsutil`访问和管理GCS中的数据，建议使用`-m` 多线程模式加快下载速率，下面是指令模板：

```shell
nohup gsutil -m cp <gsc path> . &
```