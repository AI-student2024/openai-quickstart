c.ServerApp.allow_root = True # 非 root 用户启动，无需修改
c.ServerApp.ip = '*'

c.NotebookApp.nbserver_extensions = {
    "@jupyterlab/completer-extension": True,
    "@jupyterlab/fileeditor-extension": True,
    "@jupyterlab/lsp-extension": True,
    "@jupyterlab/notebook-extension": True
}

