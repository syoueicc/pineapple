from fabric import task


@task
def pack(c):
    c.run('ls -al')

