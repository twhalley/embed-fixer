# embed-fixer
A Discord bot that will repost reddit, twitter to rxddit, vxtwitter, etc.

## Create a Discord Bot:

1. Go to the [Discord Developer Portal](https://discord.com/developers/)
2. Create a new application.
3. Create a bot user and get the bot token.
4. Invite the bot to your server with the appropriate permissions (Read and Manage Messages).
5. Enable Message Content Intent under the bot section.

![alt text](image.png)

Your DISCORD_BOT_TOKEN can be found here.

![alt text](image-1.png)

## Run pod
```bash
podman run --network host -e DISCORD_BOT_TOKEN="yourtokenhere" embed-fixer
```