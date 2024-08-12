EN
---

# Nuke Python Bot

## Overview

The Nuke Python Bot is a Discord bot designed for server management and testing. It features commands for server attacks, premium user management, and various administrative functionalities. This bot is built using Python and the `discord.py` library.

**Warning:** This bot includes commands that can cause significant changes to Discord servers, such as deleting channels, banning users, and more. Use this bot responsibly and only on servers where you have permission to perform these actions.

## Features

- **Server Attack**: Delete all channels, change server name, and create spam channels.
- **Premium Management**: Add and manage premium users.
- **Administrative Commands**: Ban all members, unban all users, prune offline members, and more.

## Installation

### Prerequisites

- Python 3.8 or higher
- `pip` for installing Python packages

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/danghuutruong/nuke-python-fumo-v2.git
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Configuration**

   - Create a `config.json` file in the root directory with the following content:

     ```json
     {
       "token": "YOUR_DISCORD_BOT_TOKEN",
       "newServerName": "NEW_SERVER_NAME"
     }
     ```

   - Ensure you have a file named `icon.jpg` for setting the server icon during attacks.

## Usage

1. **Run the Bot**

   ```bash
   python main.py
   ```

2. **Commands**

   - `!attack`: Perform an attack on the server.
   - `!unban_all`: Unban all users in the server.
   - `!help`: Display help message.
   - `!free`: Experience the premium package for free for 1 day.
   - `!config`: View bot configuration.
   - `!everyone_admin`: Grant admin permissions to everyone.
   - `!shuffle_channels`: Shuffle the positions of channels in the server.
   - `!spam [count] [context]`: Spam all channels with a specified context.
   - `!created_channels [count] [context]`: Create a specified number of channels with given context.
   - `!ban_all`: Ban all members in the server (excluding premium members).
   - `!prune_members`: Kick all users who have been offline for 1 day or more.
   - `!delete_channel`: Delete all channels.
   - `!delete_role`: Delete all roles (except everyone).
   - `!ls`: BOT leaves all the server

## Testing

- **Testing Commands**: Test bot commands by inviting the bot to a test server and executing commands as described in the "Commands" section.
- **Error Handling**: The bot includes error handling for various commands to provide feedback on issues like permissions and cooldowns.

## Notes

- Ensure that the bot has the required permissions to execute commands such as banning members or deleting channels.
- Using the `!attack` command will cause significant changes to the server. Use it with caution and only on servers where you have explicit permission.
- The `!everyone_admin` command grants admin permissions to everyone, which can be highly disruptive.

## Contributing

Feel free to open issues or pull requests if you have suggestions or improvements.

Feel free to adjust or add more details as needed!

VI

---

# Nuke Python Bot

## Tổng Quan

Nuke Python Bot là một bot Discord được thiết kế cho việc quản lý và thử nghiệm máy chủ. Nó bao gồm các lệnh cho tấn công máy chủ, quản lý người dùng premium và nhiều chức năng quản trị khác. Bot này được xây dựng bằng Python và thư viện `discord.py`.

**Cảnh báo:** Bot này bao gồm các lệnh có thể gây ra những thay đổi đáng kể trên máy chủ Discord, như xóa kênh, cấm người dùng, và nhiều hơn nữa. Hãy sử dụng bot này một cách có trách nhiệm và chỉ trên các máy chủ mà bạn có quyền thực hiện các hành động này.

## Tính Năng

- **Tấn Công Máy Chủ**: Xóa tất cả các kênh, thay đổi tên máy chủ và tạo kênh spam.
- **Quản Lý Premium**: Thêm và quản lý người dùng premium.
- **Lệnh Quản Trị**: Cấm tất cả các thành viên, gỡ cấm tất cả người dùng, lọc các thành viên offline, và nhiều hơn nữa.

## Cài Đặt

### Yêu Cầu

- Python 3.8 hoặc cao hơn
- `pip` để cài đặt các gói Python

### Các Bước

1. **Clone Repository**

   ```bash
   git clone https://github.com/danghuutruong/nuke-python-fumo-v2.git
   ```

2. **Tạo Môi Trường Ảo**

   ```bash
   python -m venv venv
   ```

3. **Kích Hoạt Môi Trường Ảo**

   - Trên Windows:

     ```bash
     venv\Scripts\activate
     ```

   - Trên macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Cấu Hình**

   - Tạo một tệp `config.json` trong thư mục gốc với nội dung sau:

     ```json
     {
       "token": "MÃ_TOKEN_CỦA_BOT_DISCORD",
       "newServerName": "TÊN_MÁY_CHỦ_MỚI"
     }
     ```

   - Đảm bảo bạn có một tệp tên là `icon.jpg` để đặt biểu tượng máy chủ trong các cuộc tấn công.

## Sử Dụng

1. **Chạy Bot**

   ```bash
   python main.py
   ```

2. **Các Lệnh**

   - `!attack`: Thực hiện một cuộc tấn công trên máy chủ.
   - `!unban_all`: Gỡ cấm tất cả người dùng trong máy chủ.
   - `!help`: Hiển thị tin nhắn trợ giúp.
   - `!free`: Trải nghiệm gói premium miễn phí trong 1 ngày.
   - `!config`: Xem cấu hình bot.
   - `!everyone_admin`: Cấp quyền admin cho tất cả mọi người.
   - `!shuffle_channels`: Xáo trộn vị trí của các kênh trong máy chủ.
   - `!spam [count] [context]`: Spam tất cả các kênh với một ngữ cảnh cụ thể.
   - `!created_channels [count] [context]`: Tạo số lượng kênh cụ thể với ngữ cảnh đã cho.
   - `!ban_all`: Cấm tất cả các thành viên trong máy chủ (ngoại trừ thành viên premium).
   - `!prune_members`: Đá tất cả người dùng đã offline từ 1 ngày trở lên.
   - `!delete_channel`: Xóa tất cả các kênh.
   - `!delete_role`: Xóa tất cả các vai trò (ngoại trừ vai trò everyone).
   - `!ls`: bot rời tất cả máy chủ

## Thử Nghiệm

- **Thử Nghiệm Các Lệnh**: Mời bot vào một máy chủ thử nghiệm và thực hiện các lệnh như đã mô tả trong phần "Các Lệnh".
- **Xử Lý Lỗi**: Bot bao gồm xử lý lỗi cho các lệnh khác nhau để cung cấp phản hồi về các vấn đề như quyền hạn và thời gian chờ.

## Lưu Ý

- Đảm bảo rằng bot có đủ quyền để thực hiện các lệnh như cấm người dùng hoặc xóa kênh.
- Sử dụng lệnh `!attack` có thể gây ra những thay đổi lớn trên máy chủ. Hãy sử dụng cẩn thận và chỉ trên các máy chủ mà bạn có sự cho phép rõ ràng.
- Lệnh `!everyone_admin` cấp quyền admin cho tất cả mọi người, điều này có thể gây ra sự gián đoạn lớn.

## Đóng Góp

Hãy mở các vấn đề hoặc yêu cầu kéo nếu bạn có ý tưởng hoặc cải tiến.

Hãy thoải mái điều chỉnh hoặc thêm chi tiết nếu cần!
