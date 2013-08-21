現在 g0v 太多東西放 hackpad, 除了 hackpad 自己的 history 功能, 應該另外作備份

# 備份
如果是 g0v 或是 open source 相關 project, 我可以幫忙 backup. 請聯絡我.
p.s. 如果是比較大的 site, 請開 admin 給我, 因為 hackpad 要 admin 才能 list uplodated pads

# 設定檔: 
(可以用 # 表示 comment)
- backup_list.txt 
  一行一個要備份的項目, 譬如 g0v/*
  目前不支援不是 * 的
  不是 admin 也可以, 只是比較沒有效率, 要 loop all pads
- api_keys.txt
  用來存取 hackpad 的 api key, 一行一個, 格式如
  [key] [secret] [site]

# api key
在 hackpad 網站上的 settings 裡可以找到. 注意每個 domain 的 key 是分開的.

# 使用方法
設好 backup_list.txt 跟 api_keys.txt, 執行
  python hackpad-backup.py
即可

程式會在 data/[site] 目錄建立 git repository, 以 padid.html 為檔名 commit 到 git 去.

# feature & limitation
- 會備份部份歷史版本 versions, 不過不會備份所有版本, 不然太大了
- 若整個 pad 被刪掉, 備份程式不會知道, 也不會備份刪掉前的版畚
- 預設以 html 格式備份, 因為這格式能保留比較多資訊
