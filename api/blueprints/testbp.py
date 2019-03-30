from flask import Blueprint

testbp=Blueprint('testbp', __name__)

@testbp.route('/')
def test():
    '''
    注意要task在函数体内部导入，因为flask会先初始化蓝图，
    如果在模块头部导入，会导致初始化本模块时开始配置celery，此时并没有app实例，会出现ImportError。
    '''
    from ..EmbedCelery.tasks import add_task
    add_task.delay(1,2)
    return 'hello world!'