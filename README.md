
# 📸 Locket Camera API

## 🚀 Giới thiệu
Đây là tập hợp các API để tương tác với Locket Camera. Dưới đây là danh sách các API và hướng dẫn sử dụng chi tiết.

## 📜 Danh sách API

### 1. 🕰️ getLastMoment
**Mô tả:** Lấy thông tin về các khoảnh khắc mới nhất.

- **URL:** `https://api.locketcamera.com/getLatestMomentV2`
- **Phương thức:** POST
- **Yêu cầu Header:**
  - `Authorization: Bearer [token]`
- **Payload:**
  ```json
  {
      "data": {
          "excluded_users": [],
          "sync_token": "5oImx73nFjTb1FTRkBC2",
          "last_fetch": {
              "@type": "type.googleapis.com/google.protobuf.Int64Value",
              "value": "1722073779706"
          },
          "fetch_streak": false,
          "should_count_missed_moments": true
      }
  }
  ```

### 2. 📝 changeProfileInfo
**Mô tả:** Thay đổi thông tin hồ sơ của người dùng.

- **URL:** `https://api.locketcamera.com/changeProfileInfo`
- **Phương thức:** POST
- **Yêu cầu Header:**
  - `Authorization: Bearer [token]`
  - `X-Firebase-AppCheck: [appCheckToken]`
- **Payload 1:**
  ```json
  {
      "data": {
          "badge": "locket_gold"
      }
  }
  ```
- **Payload 2:**
  ```json
  {
      "data": {
          "last_name": "Nguyen",
          "first_name": "Anh"
      }
  }
  ```

### 3. 📧 updateEmailAddress
**Mô tả:** Cập nhật địa chỉ email của người dùng.

- **URL:** `https://api.locketcamera.com/updateEmailAddress`
- **Phương thức:** POST
- **Yêu cầu Header:**
  - `Authorization: Bearer [token]`
  - `X-Firebase-AppCheck: [appCheckToken]`
- **Payload:**
  ```json
  {
      "data": {
          "email": "example@gmail.com"
      }
  }
  ```

### 4. 📱 sendVerificationCode
**Mô tả:** Gửi mã xác minh để thay đổi số điện thoại.

- **URL:** `https://api.locketcamera.com/sendVerificationCode`
- **Phương thức:** POST
- **Yêu cầu Header:**
  - `Authorization: Bearer [token]`
  - `X-Firebase-AppCheck: [appCheckToken]`
- **Payload:**
  ```json
  {
      "data": {
          "phone": "+84987654321",
          "operation": "change_number",
          "platform": "ios",
          "is_retry": false
      }
  }
  ```

### 5. 💬 sendChatMessageV2
**Mô tả:** Gửi tin nhắn tới người dùng khác.

- **URL:** `https://api.locketcamera.com/sendChatMessageV2`
- **Phương thức:** POST
- **Yêu cầu Header:**
  - `Authorization: Bearer [token]`
  - `X-Firebase-AppCheck: [appCheckToken]`
- **Payload:**
  ```json
  {
      "data": {
          "receiver_uid": "bmLzyn7UQTPtN7budBYirrWdDUb2",
          "client_token": "72652F96-0C4D-4CFE-9D59-B3251029B897",
          "msg": "Ê bro",
          "moment_uid": null,
          "from_memory": false
      }
  }
  ```

### 6. 🆕 createAccountWithEmailPassword
**Mô tả:** Tạo tài khoản mới.

- **URL:** `https://api.locketcamera.com/createAccountWithEmailPassword`
- **Phương thức:** POST
- **Yêu cầu Header:**
  - `Authorization: Bearer [token]`
  - `X-Firebase-AppCheck: [appCheckToken]`
- **Payload:**
  ```json
  {
      "data": {
          "password": "your_password",
          "client_token": "9e4add9a8ac5b41328cff18e93aa0ff87a814c80",
          "client_email_verif": true,
          "email": "example@gmail.com",
          "platform": "ios"
      }
  }
  ```

### 7. 🗑️ deleteUserAccount
**Mô tả:** Xóa tài khoản người dùng.

- **URL:** `https://api.locketcamera.com/deleteUserAccount`
- **Phương thức:** POST
- **Yêu cầu Header:**
  - `Authorization: Bearer [token]`
  - `X-Firebase-AppCheck: [appCheckToken]`
- **Phản hồi:** Xác nhận tài khoản người dùng đã được xóa thành công.

## 🛠️ Hướng dẫn bắt API
1. Tải về và cài đặt [HTTP Toolkit](https://httptoolkit.tech/) trên máy tính.
2. Kết nối điện thoại với cùng mạng Wi-Fi mà máy tính đang kết nối.
3. Trên điện thoại, vào phần cài đặt Wi-Fi, chọn mạng Wi-Fi đang kết nối, chỉnh proxy thành địa chỉ IP cục bộ (local IP) của máy tính và đặt port là `8000`.
4. Khởi động HTTP Toolkit và bắt đầu theo dõi các request API từ điện thoại của bạn.
