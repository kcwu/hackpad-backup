Update:
hackpad is shuting down and it provided "export" function to admins. So, if you are admin of
hackpad sites, it is suggested to use their "export" function, which preserve more information.

If you are not admin, you can use this script to backup.

----------------------
Besides hackpad's history feature, we should do backup ourselves.

# Backup
For large side, it's recommended to use admin account to backup because only admin can list recent updated pads.

# Configurations: 
(use # at line beginning as comment)
- backup_list.txt 
  One backup item per line, for example, "g0v/*" mean entire site of g0v.hackpad.com.
  Currently, it can only support * and unable to backup only individual pads.
  It's unnecessary for you account to be an admin of that site. But non-admin is less
  efficient because the program have to loop all pads. And of course, you cannot see
  hidden pads if you are not admin or owner.
- api_keys.txt
  The API key of hackpad, one key per line. The format is
  [key] [secret] [site]

# api key
You can find the api key on hackpad's setting page. Note different domain (site) use different key.

# How to use
After setup backup_list.txt and api_keys.txt, run
  python hackpad-backup.py

The script will create git repository in data/[site] folder. And commit files named as padid.html into the git repo.

# feature & limitation
- It can backup history of pads. But only partial, not full revisions, otherwise the size is too huge.
- The backup script is unable to know what pads are deleted and thus unable to backup the last revisions before delete.
- It backups in html format by default because this format can preserve more information.
