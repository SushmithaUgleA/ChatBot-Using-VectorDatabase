css = '''
<style>
.chat-message {
    padding: 1.8rem; border-radius: 1.5rem; margin-bottom: 1.5rem; display: flex
}
.chat-message.user {
    background-color: #1b312e
}
.chat-message.bot {
    background-color: #575123
}
.chat-message .avatar {
  width: 30%;
}
.chat-message .avatar img {
  max-width: 82px;
  max-height: 82px;
  border-radius: 40%;
  object-fit: cover;
}
.chat-message .message {
  width: 75%;
  padding: 0 1.5rem;
  color: #eff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.ibb.co/rdZC7LZ/Photo-logo-1.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
