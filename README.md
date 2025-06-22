# IoT_Final_Project: Smart Lamp

## 專案簡介

這是一個模擬的智慧燈泡系統，使用者可以透過app手動操縱電燈開關，也可以在自動模式下，透過感測器(模擬)接收的光強度資料，來自動控制電燈開關。
此外，這個開關燈的訊息，也會同步到燈泡IPE上。

## 專案目錄結構
```
iot_final_project/
├── Final_Project.apk          # App Inventor 編譯產生的 Android App
├── IOT final project .pdf     # 專案報告 PDF
├── IOT final project.pptx     # 專案簡報檔 PPTX
├── README.md                  # 說明文件
├── app_inventor.aia           # App Inventor 專案原始檔
├── github link.txt            # GitHub 連結
├── light_simulate.py          # 光強度感測器腳本
├── nodered_flows.json         # Node-RED 設定檔
├── postman_flows.json         # Postman 設定檔
```

## 使用說明
1. 開啟 in-cse, mn-cse。
```shell=
# in-cse
cd ~/Documents/org.eclipse.om2m/org.eclipse.om2m.site.in-cse/target/products/in-cse/linux/gtk/x86_64/
sh start.sh
# mn-cse
cd ~/Documents/org.eclipse.om2m/org.eclipse.om2m.site.mn-cse/target/products/mn-cse/linux/gtk/x86_64/
sh start.sh
```
2. 開啟 node-red，接著連上127.0.0.1:1880(nodered網址)，把除了最上面兩個 timestamp 以外的所有 timestamp 都值執行一次，以建立 mn 的 container。
3. 開啟 Postman，把所有 function 執行一次，以建立 in 的 container，並建立訂閱機制。
4. 在 mn 的 terminal 中，輸入`start 41`，來開啟燈泡 IPE。
5. 準備工作皆完成，此時可以在 Android 系統中開啟 Final_Project APP，以手動模式控制燈泡 IPE。
6. 可執行 python 腳本"light_simulate.py"，來模擬生產光強度資料，並將 APP 的控制模式調整 Auto mode，就會看到燈泡根據模擬的光強度資料自動 on, off。
