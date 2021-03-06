from nonebot import  on_request, RequestSession,on_notice, NoticeSession,message
from config import managed_group#导入管理群列表
@on_request('group')
async def _(session: RequestSession):
    if str(session.event['group_id']) in managed_group and session.event['comment'].strip(" ").find("6CF2D42B629E5AA4E6C293B290798878")!=-1:
        await session.approve()
    else:
        await session.reject('呐呐呐!!暗号错啦!!')

# 将函数注册为群成员增加通知处理器
@on_notice('group_increase')
async def _(session: NoticeSession):
    # 发送欢迎消息
    if str(session.event['group_id']) in managed_group:
        await session.send(message.MessageSegment.at(session.event['user_id'])+' 欢迎小哥哥~使用项目时请遵守相关法律哦~啾咪~[CQ:emoji,id=128154]')