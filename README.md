# ftp_python
例如:
  connect,192.168.137.2,2121
  login,qpyplus,qpyplus ========>send,user qpyplus;send,pass qpyplus
  ls============================>send,pasv;send,list
  exit============================>send,quit;exit(0)
  send,(command)
  例如:
    send,user qpyplus
    send,pass qpyplus
    send,pasv =======>  遇到227返回数，自动创建并连接新的socket，并等待返回，返回成功时关闭连接
    send,pwd
    send,cwp /
    ...............

目前= = 没能力搞好= =
