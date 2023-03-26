import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler,ContextTypes

TOKEN = '6168560088:AAFiQQGye-VIIRQgUB7w5gHl27FBNI-KTsA'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

rule = '''
投稿内容(包括图片和文字)一并放入消息框并发送。

投稿要求：
• 图片限1张(选择"压缩图片"，别选"原图发送")
• 模版中标点符号"："是中文冒号
• 内容不要出现 < > 等符号
• 资源链接设置为永久

提示:
• 可以先输入文字再复制图片粘贴输入然后再发送

一键投稿格式模板：

[图片]

名称：
描述：
链接：
大小：
标签： 
'''


async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

'返回投稿格式'
async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=rule)

'返回用户的稿件'
async def update(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

'处理投稿逻辑'
async def upsert(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    '注册 handler'
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), upsert))
    application.add_handler(CommandHandler('search', search))
    application.add_handler(CommandHandler('list', list))
    application.add_handler(CommandHandler('add', add))
    application.add_handler(CommandHandler('update', update))
    
    application.run_polling()

